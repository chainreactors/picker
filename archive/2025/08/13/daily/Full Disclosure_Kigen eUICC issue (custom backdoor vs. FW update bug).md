---
title: Kigen eUICC issue (custom backdoor vs. FW update bug)
url: https://seclists.org/fulldisclosure/2025/Aug/4
source: Full Disclosure
date: 2025-08-13
fetch_date: 2025-10-07T00:58:01.809854
---

# Kigen eUICC issue (custom backdoor vs. FW update bug)

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

# Kigen eUICC issue (custom backdoor vs. FW update bug)

---

*From*: Security Explorations <contact () security-explorations com>
*Date*: Tue, 12 Aug 2025 10:01:43 +0200

---

```
Dear All,

On Jul 28, 2025 we provided Kigen with a report describing new security
issue potentially affecting company's eUICC cards. We did it regardless
of Kigen refusal to provide us with patches / patching instructions, so
that we could verify the content / quality of the fixes released by the
company for previously reported JavaCard issues [1] (more on that and
patching formula proposed by the company can be found on eSIM project
pages).

While Kigen claims it "takes security issues extremely seriously and
welcomes feedback from security researchers to improve the security of
its services" [2], the company has not provided response / confirmation
of our report reception as of Aug 11, 2025 (Kigen CTO and media person
CC'ed to all messages).

Depending on the evaluation of the issue (custom backdoor vs. bug in FW
patching mechanism), this might constitute a base for some spec changes
at GSMA end.

SGP.22 specification leaves it up to the vendor how eUICC FW patching is
to be performed. This may lead to security issues if not done properly
(there is some potential the new report will highlight the need for spec
changes of which GSMA was notified on Jul 29, 2025).

The new issue seems more dangerous when compared to the initial JavaCard
exploit due to the potential for arbitrary eUICC firmware change. There
is no requirement for a malicious JavaCard app installation / presence.
Our analysis indicates that an attacker just needs physical access to
target card (over-the-wire exploit scenario) or to know the OTA / RFM
keys (over-the-air exploit). The new issue relies on secret keys embedded
in eUICC firmware, which cannot be deemed secret taking into account
their symmetric nature and JavaCard exploit leading to complete card
compromise.

We provided Kigen with a sample exploitation / backdoor implementation
scenario (an idea) too (an approach for arbitrary FW patching making it
possible to return prv ECC key as a response to given GET DATA APDU).

It's worth to note that beside some incosistencies / confusion carried
in Kigen security bulletin [3] (confusing root cause) and with respect
to CVSS score provided by the company (implicating physical exploit
vector only even though we relied on simulated OTA), we also found out
that the vulnerability impact information provided by Kigen was not
correct. More specifically, we verified that cards with "ECu1029"
version string are also prone to JavaCard issues (Kigen indicated that
"ECu10.13" string identifies vulnerable eUICC card).

Due to inability to verify / confirm reported issue with the company
we suggest Kigen customers to request information pertaining to all
secret / shared keys embedded in Kigen eUICC FW and ECASD domain
(those keys that are out of customers control in particular, ECASD
key ver 7f [4]).

Thank you.

Best Regards,
Adam Gowdiak

----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------

[1] eSIM security
    https://security-explorations.com/esim-security.html
[2] Kigen Security Center
    https://kigen.com/company/policies/security-center/
[3] Kigen Security Bulletin, Jul 2025
    https://kigen.com/company/policies/security-center/security-bulletin-kgnsb-07-2025/
[4] Sample Kigen eUICC secret keys dump
    https://security-explorations.com/samples/kigen_euicc_keys_dump.txt
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

* **Kigen eUICC issue (custom backdoor vs. FW update bug)** *Security Explorations (Aug 12)*

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