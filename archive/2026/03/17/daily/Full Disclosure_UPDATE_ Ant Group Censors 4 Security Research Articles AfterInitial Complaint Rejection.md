---
title: UPDATE: Ant Group Censors 4 Security Research Articles After	Initial Complaint Rejection
url: https://seclists.org/fulldisclosure/2026/Mar/7
source: Full Disclosure
date: 2026-03-17
fetch_date: 2026-03-18T04:22:47.873394
---

# UPDATE: Ant Group Censors 4 Security Research Articles After	Initial Complaint Rejection

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# UPDATE: Ant Group Censors 4 Security Research Articles After Initial Complaint Rejection

---

*From*: Jiqiang Feng via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 15 Mar 2026 12:18:43 +0000

---

```
[This is an update to communications sent March 12-14 regarding Alipay security vulnerabilities.]

---

On March 15, 2026, four WeChat articles documenting security vulnerabilities in Alipay were forcibly deleted from the
public account AI-security-innora. The deletion was carried out by Tencent at the request of Beijing Geyun Law Firm,
acting on behalf of Ant Group, citing China's Cybersecurity Law.

The same complaint had been rejected by WeChat four days earlier on grounds of "reputation infringement" -- at that
point WeChat found it did not meet the threshold for removal. When resubmitted under a different legal theory, the
articles were deleted without further review.

---

WHAT WAS DELETED

1. "Whitelist bypass as a universal attack key" (当白名单绕过沦为全网攻击的钥匙)
2. "The gag order rejected by WeChat, then reversed" (巨头的封口令被微信驳回)
3. "GPS location silently exfiltrated from 1B+ users' payment app" (位置被秒偷)
4. "Security research vs. a cease-and-desist for an article with zero mentions of Alipay"

---

THE BROADER DISCLOSURE RECORD

The underlying research covers 17 vulnerabilities (CVSS 7.4-9.3) in Alipay for iOS/Android, reported to Ant Group
through responsible disclosure. Ant Group's formal response: "normal functionality."

Independent verification and institutional acceptance:
- MITRE: 6 CVEs accepted, Ticket #2005801
- Packet Storm: Advisory #217089 published
- CSSF Luxembourg: Whistleblowing case CSSFWB-2026-080
- HKMA Hong Kong: Case CE20260313175412
- PDPC Singapore: Investigation #00629724
- Apple Product Security: Case OE01052449093014
- Google Play: Policy violation review #9-7515000040640
- CIRCL Luxembourg: Case #4782984 (relayed to Alibaba SRC)
- 38+ institutions across 22 jurisdictions have acknowledged the report

Full technical report: https://innora.ai/zfb/
GitHub: https://github.com/sgInnora/alipay-deeplink-research

---

THE CENSORSHIP PATTERN

This escalation follows a documented sequence:

1. Oral denial by vendor ("normal functionality," March 10)
2. Public blog published after disclosure window elapsed (March 11)
3. Cease-and-desist via Beijing Geyun Law Firm (March 11, 4h29m after publication)
4. Initial WeChat complaint REJECTED (reputation infringement standard not met)
5. Re-filed under Cybersecurity Law -- all 4 articles deleted without further notice (March 15)
6. Server-side blocking of PoC demonstration traffic (documented separately)

This pattern is consistent with suppression of security research rather than legitimate legal remedy. disclose.io
maintains a researcher threats database at https://threats.disclose.io/ that tracks this category of legal and
platform-based retaliation against good-faith researchers.

A full bilingual analysis of this censorship event is available at: https://innora.ai/zfb/

---

I am available for verification, additional documentation, or technical questions.

Jiqiang Feng
Innora AI Security Research
feng () innora ai
https://innora.ai/zfb/
```

**Attachment:
[publickey - Jiqiang Feng - 0x7D1A285E.asc](att-7/publickey_-_Jiqiang_Feng_-_0x7D1A285E_asc.bin)**
*Description:*

**Attachment:
[signature.asc](att-7/signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **UPDATE: Ant Group Censors 4 Security Research Articles After Initial Complaint Rejection** *Jiqiang Feng via Fulldisclosure (Mar 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")