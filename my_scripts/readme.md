#  NTLM Password Sprayer

A custom-built, Python-based Red Teaming tool designed to perform stealthy **Password Spraying** attacks against web applications and exposed services that utilize Windows Authentication (NetNTLM). 

Unlike traditional brute-force attacks that quickly trigger Active Directory account lockout policies, this tool takes a single password and tests it across a list of users, helping penetration testers secure an initial foothold smoothly and quietly.

##  Features
* **Object-Oriented Design:** Clean, modular, and easy-to-read Python code.
* **Stealthy Execution:** Avoids account lockouts by employing a one-password-to-many-users approach.
* **HTTP Status Code Analysis:** Automatically evaluates responses (`200 OK` for success, `401 Unauthorized` for failure) to validate credentials.
* **Command-Line Interface (CLI):** Easy to use with flexible arguments for custom wordlists, domains, and target URLs.

##  Prerequisites

Before running the script, ensure you have Python 3 installed along with the required libraries. 

You can install the dependencies using `pip`:

```bash
pip install requests requests_ntlm
```
Installation
Clone the repository to your local machine:

```Bash
git clone https://github.com/hatemharby98/python_ethical_hacking.git
cd python_ethical_hacking/my_scripts
```
Usage
To see the help menu and required arguments, use the -h flag:

```Bash
python3 ntlm_passwdSpray.py -h
```

```Bash
python3 ntlm_passwdSpray.py -u <userfile> -d <fqdn> -p <password> -U <attackurl>
Arguments:

-u / --userfile : Path to the text file containing the list of usernames.

-d / --fqdn : The Fully Qualified Domain Name (e.g., za.tryhackme.com).

-p / --password : The single password you want to spray (e.g., Changeme123).

-U / --url : The target endpoint that prompts for Windows Authentication.
```
 Example
```Bash
python3 ntlm_passwdSpray.py -u usernames.txt -d targetdomain.local -p Fall2023! -U http://ntlmauth.targetdomain.local/
Expected Output:

Plaintext
[*] Starting passwords spray attack using the following password: Fall2023!
[-] invalid
[-] invalid
[+] valid username j.doe and password Fall2023!
[-] invalid
[*] count: 1
```
 Disclaimer
For Educational and Authorized Testing Purposes Only!
This tool was developed for ethical hacking, penetration testing, and security assessments. Do not use this tool against any network, system, or infrastructure without explicit, written permission from the owner. The author is not responsible for any misuse or damage caused by this script.
