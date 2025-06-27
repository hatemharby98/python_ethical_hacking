#! usr/bin/env python
from wsgiref.util import request_uri
import scapy.all as scapy
import argparse

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="enter the target_ip / ip_range")
    options= parser.parse_args()
    if not options.target:
        parser.error("[-] please enter the right target!")
    return options


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)    # create packet
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  #send brodcast
    arp_request_brodcast = brodcast/arp_request      #combining arp and brodcast
# answered_take_frist_element[0], unanswered_take_second_element[1] = scapy.srp(arp_request_brodcast, timeout=1)  # send and receive ( this is list)
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]  #choose the first list
    cleints_list = []    #create list append ip and mac
    for each_element in answered_list:
        cleints_dic = {"ip":each_element[1].psrc , "mac": each_element[1].hwsrc  } #psrc and hwsrc this calss show ==> scapy.ls(scapy.ARP)
        cleints_list.append(cleints_dic)
    return cleints_list

def print_result(scan_result):
    print("ip\t\t\tMac Address\n------------------------------------------------")
    for client in scan_result:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_argument()
scan_result = scan(options.target)
print_result(scan_result)
