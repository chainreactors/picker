---
title: grub-btrfs initramfs hook Command Injection
url: https://cxsecurity.com/issue/WLB-2026020020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-19
fetch_date: 2026-02-20T04:07:01.076082
---

# grub-btrfs initramfs hook Command Injection

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
|  |  | |  | | --- | | **grub-btrfs initramfs hook Command Injection**  **2026.02.19**  Credit:  **[cardosource](https://cxsecurity.com/author/cardosource%2B/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2026-25828](https://cxsecurity.com/cveshow/CVE-2026-25828/ "Click to see CVE-2026-25828")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

CVE-2026-25828 is a critical command injection vulnerability in the grub-btrfs package used in Arch Linux and derivative distributions.
The issue exists in the initramfs hook "grub-btrfs-overlayfs" which passes the $root kernel parameter directly into resolve\_device() without proper sanitization, allowing an attacker with local or bootloader access to inject shell commands during early boot.
Affected Product:
- grub-btrfs – all versions up to 2026-01-31 on Arch and derivatives
Vulnerability:
Unsanitized usage of the $root variable from the kernel command line allows shell metacharacter injection and arbitrary code execution as root during boot.
Proof of Concept:
Example exploit modifying GRUB kernel line:
linux /vmlinuz-linux root="/dev/sda1; echo 'root::0:0:root:/root:/bin/bash' >> /etc/passwd; #" rw quiet
Impact:
- Arbitrary command execution as root
- Privilege escalation
- System compromise during boot stage

**##### References:**

References:

https://github.com/cardosource/CVE-2026-25828

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020020)

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