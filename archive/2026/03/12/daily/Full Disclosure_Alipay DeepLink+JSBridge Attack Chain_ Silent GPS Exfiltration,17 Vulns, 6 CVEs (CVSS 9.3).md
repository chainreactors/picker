---
title: Alipay DeepLink+JSBridge Attack Chain: Silent GPS Exfiltration,	17 Vulns, 6 CVEs (CVSS 9.3)
url: https://seclists.org/fulldisclosure/2026/Mar/4
source: Full Disclosure
date: 2026-03-12
fetch_date: 2026-03-13T04:08:10.460915
---

# Alipay DeepLink+JSBridge Attack Chain: Silent GPS Exfiltration,	17 Vulns, 6 CVEs (CVSS 9.3)

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# Alipay DeepLink+JSBridge Attack Chain: Silent GPS Exfiltration, 17 Vulns, 6 CVEs (CVSS 9.3)

---

*From*: Feng Ning via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 12 Mar 2026 02:33:20 +0000

---

```
Subject: Alipay DeepLink+JSBridge Attack Chain: Silent GPS Exfiltration, 17 Vulns, 6 CVEs (CVSS 9.3)

# Alipay DeepLink + JSBridge Attack Chain
# Silent GPS Exfiltration via Crafted URL

## Overview

Researcher: Jiqiang Feng / Innora AI Security Research
Vendor: Ant Group (蚂蚁集团) / Alibaba Group
Product: Alipay (支付宝) v10.x (Android & iOS)
Users Affected: 1 billion+
CVEs: 6 submitted to MITRE CNA-LR (2026-03-12)
CVSS: 7.4–9.3
Vendor Response: "Normal functionality"
Disclosure: Responsible (Feb 25 → Mar 11 public)

## Vulnerability Chain

A single crafted URL triggers the following attack chain:

1. Open Redirect (CWE-601): ds.alipay.com/?scheme= accepts arbitrary URL parameters, redirecting to Alipay app via deep
link
2. Whitelist Bypass (CWE-939): ds.alipay.com is a whitelisted Alipay domain, so the deep link handler trusts the
redirect target
3. WebView Loading: Attacker-controlled page loads in Alipay's privileged WebView with JSBridge access
4. API Abuse: AlipayJSBridge.call() exposes sensitive native APIs without user consent

## Exploitable APIs (Verified)

| # | API | Data Extracted | Android | iOS |
|---|-----|---------------|---------|-----|
| 1 | getLocation | GPS coords (8.8m accuracy) | ✓ | ✓ |
| 2 | getNetworkType | WiFi/cellular, carrier info | ✓ | ✓ |
| 3 | getSystemInfo | Device model, OS, screen | ✓ | ✓ |
| 4 | getCameraPermission | Camera auth status | ✓ | ✓ |
| 5 | getMicrophonePermission | Mic auth status | ✓ | ✓ |
| 6 | tradePay | Pre-fill payment screen | ✗ | ✓ |
| 7 | share | Trigger share dialog | ✗ | ✓ |
| 8 | scan | Activate QR scanner | ✗ | ✓ |
| 9 | chooseImage | Access photo picker | ✗ | ✓ |

iOS attack surface is significantly larger than Android.

## PoC

Trigger URL pattern:
https://ds.alipay.com/?scheme=alipays://platformapi/startapp?appId=20000067&url=[BASE64_ENCODED_ATTACKER_URL]

Verification page (read-only, no data collection):
https://innora.ai/zfb/poc/trigger.html

## Verification

- 3 devices: Samsung S25 Ultra (NZ), Xiaomi Redmi 12 (MY), iPhone 16 Pro (CN-Hangzhou)
- 308 server-side exfiltration logs
- 42 screenshots
- Vendor's own security lead tested on iPhone from Hangzhou (Alipay HQ) — GPS captured silently in 7 seconds, accuracy
8.8m

## Timeline

2026-02-25: Initial TLS/SSL report to vendor
2026-03-06: Vendor: "cannot be practically exploited"
2026-03-07: Expanded report (17 vulns, full E2E proof)
2026-03-07: Whitelist bypass achieved in 2 min during live call with vendor
2026-03-08: Vendor's security lead's iPhone tested from Hangzhou — GPS captured
2026-03-10: Vendor final: "normal functionality"
2026-03-11: Public disclosure
2026-03-11: Vendor's law firm files takedown complaint (4 hours later)
2026-03-12: 6 CVEs submitted to MITRE

## Full Report

https://innora.ai/zfb/ (bilingual EN/ZH)

## Notes

- Alibaba is a registered CNA (CNA-2017-0006) but refused to assign CVEs
- Vendor's law firm complaint targets an article that never once mentions "Alipay" or "Ant Group" by name
- Vendor's security contact privately called it a "洞" (hole/vuln) while officially classifying as "normal functionality"

## Contact

Jiqiang Feng | feng () innora ai | Innora AI Security Research
```

**Attachment:
[publickey - Jiqiang Feng - 0x7D1A285E.asc](att-4/publickey_-_Jiqiang_Feng_-_0x7D1A285E_asc.bin)**
*Description:*

**Attachment:
[signature.asc](att-4/signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

### Current thread:

* **Alipay DeepLink+JSBridge Attack Chain: Silent GPS Exfiltration, 17 Vulns, 6 CVEs (CVSS 9.3)** *Feng Ning via Fulldisclosure (Mar 12)*

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