---
title: Hashcat Cheatsheet
url: https://www.blackhillsinfosec.com/hashcat-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:19.839381
---

# Hashcat Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [Hashcat](https://www.blackhillsinfosec.com/tag/hashcat/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [Hashcat Cheatsheet](https://www.blackhillsinfosec.com/hashcat-cheatsheet/)

Created by [Justin Wang](https://www.linkedin.com/in/hsiaoan-wang-4514ab45/) || Revised by [Kent Ickler](https://x.com/Krelkci)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_7.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**Hashcat Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_Hashcat.pdf)

Find the tool here: <https://github.com/hashcat/hashcat>

---

Hashcat is a powerful tool for recovering lost passwords, and, thanks to GPU acceleration, it’s one of the fastest. It works by rapidly trying different password guesses to determine the original password from its scrambled (hashed) version. Hashcat uses various clever techniques, like dictionary attacks (testing common passwords), leetspeak tricks (e.g., replacing “e” with “3”), pattern-based guessing, and combining different words or phrases. This helps expose weak passwords and poor security habits, which many people rely on when configuring and registering accounts online. Because of its effectiveness, Hashcat is widely used in cybersecurity training, ethical hacking, and penetration testing to improve password security and help organizations strengthen their defenses.

```
hashcat -m # <file storing your hash> <path to wordlist> -a <attack>
```

## Commonly Used Modes (-m)

|  |  |
| --- | --- |
| 0 | MD5 |
| 900 | MD4 |
| 1700 | SHA2-512 |
| 10 | MD5 ($pass.$salt) |
| 20 | MD5 ($salt.$pass) |
| 110 | SHA1:salt |
| 120 | SHA1:pass |
| 2600 | md5(md5($pass)) |
| 4500 | sha1(sha1($pass)) |
| 400 | phpass |
| 8900 | scrypt |
| 2500 | WPA/WPA2 |
| 2501 | WPA/WPA2 PMK |
| 4800 | iSCSI CHAP authentication, MD5(CHAP) |
| 5500 | NetNTLMv1 / NetNTLMv1+ESS |
| 5600 | NetNTLMv2 |
| 7500 | Kerberos 5, etype 23, AS-REQ Pre-Auth |
| 7300 | IPMI 2 RAKP HMAC-SHA1 |
| 7350 | IPMI2 RAKP HMAC-MD5 |
| 13100 | Kerberos 5, etype 23, TGS-REP |
| 18200 | Kerberos 5, etype 23, AS-REP |
| 19600 | Kerberos 5, etype 17, TGS-REP |
| 19700 | Kerberos 5, etype 18, TGS-REP |
| 19800 | Kerberos 5, etype 17, Pre-Auth |
| 19900 | Kerberos 5, etype 18, Pre-Auth |
| 27000 | NetNTLMv1 / NetNTLMv1+ESS (NT) |
| 27100 | NetNTLMv2 (NT) |
| 27300 | SNMPv3 HMAC-SHA512-384 |
| 28900 | Kerberos 5, etype 18, DB |
| 1000 | NTLM |

|  |  |
| --- | --- |
| 1100 | Domain Cached Credentials (DCC), MS Cache |
| 1800 | sha512crypt $6$, SHA512 (Unix) |
| 3000 | LM |
| 5700 | Cisco-IOS type 4 (SHA256) |
| 7400 | sha256crypt $5$, SHA256 (Unix) |
| 8100 | Citrix NetScaler (SHA1) |
| 12800 | MS-AzureSync PBKDF2-HMAC-SHA256 |
| 131 | MSSQL (2000) |
| 132 | MSSQL (2005) |
| 200 | MySQL323 |
| 300 | MySQL4.1/MySQL5 |
| 1731 | MSSQL (2012, 2014) |
| 1600 | Apache $apr1$ MD5, md5apr1, MD5 (APR) |
| 8300 | DNSSEC (NSEC3) |
| 15000 | FileZilla Server > 0.9.55 |
| 22100 | Bitlocker |
| 22400 | AES Crypt (SHA256) |
| 29521 | LUKS v1 SHA-256 + AES |
| 9500 | MS Office 2010 |
| 9600 | MSOffice 2013 |
| 5200 | Password Safe v3 |
| 6800 | LastPass + LastPass sniffed |
| 13400 | KeePass 1 (AES/Twofish) and KeePass 2 (AES) |
| 29700 | KeePass 1 (AES/Twofish) and KeePass 2 (AES) – keyfile only mode |
| 11600 | 7Zip |
| 13600 | WinZip |

## **Attack Modes (-a)**

|  |
| --- |
| **0 = Straight Dictionary Attack** *Example:* `hashcat -m 500 -a 0 hash.txt dict.txt` |
| **1 = Combination Attack** *Example:* **`hashcat -m 500 -a 1 hash.txt dict1.txt dict2.txt`** |
| **3 = Brute Force Attack** *Example:* `hashcat -m 500 -a 3 hash.txt ?l?d?u` |
| **6 = Hybrid Wordlist + Mask** *Example:* `hashcat -m 500 -a 6 hash.txt wordlist.txt ?d?s` |
| **7 = Mask + Wordlist** *Example:* `hashcat -m 500 -a 7 hash.txt ?d?s wordlist.txt` |

## **Useful Command Arguments**

|  |  |
| --- | --- |
| `"--runtime=X"` | Abort session after X seconds of runtime. |
| `"--session=X"` | Define session name to be string X. |
| `"--restore"` | Restore Session from –session. |
| `"-o"` | Define output file for recove...