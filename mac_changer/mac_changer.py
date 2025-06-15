#! usr/bin/env python
# organic_mac=fe80::f51e:86f3:f328:7df4
import subprocess
import optparse
import re


def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="change it's mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] please specify a mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(f"[+] Changing mac Adress for {interface} to {new_mac}")

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result.decode("utf-8"))
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not find mac address! ")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("[+] current_mac:", current_mac)

change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac address was successfully change to: ", current_mac)
else:
    print("[-] Mac address did not change! ")




#-------------------------------------------------------------------------------------------

