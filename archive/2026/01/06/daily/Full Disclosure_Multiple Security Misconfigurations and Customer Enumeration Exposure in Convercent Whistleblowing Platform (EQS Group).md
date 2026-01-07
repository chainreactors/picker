---
title: Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)
url: https://seclists.org/fulldisclosure/2026/Jan/4
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:39.770580
---

# Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)

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

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#4)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#4)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)

---

*From*: Yuffie Kisaragi via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sun, 04 Jan 2026 22:01:57 +0000

---

```
UPDATE:

Following the publication of these vulnerabilities and the subsequent CVE
assignments, the CVE identifiers have now been revoked.

The vendor (EQS Group) contacted the CVE Program (via a CNA) and disputed the
records, stating that the affected product is an exclusively hosted SaaS
platform with no customer-managed deployment or versioning. Based on this
argument, the CVE Program concluded that CVE assignment is “not a suitable
solution for vulnerability identification” in this case, as customers do not
take direct action to apply fixes.

In other words, because the service is centrally hosted and patched at the
provider’s discretion, the vulnerabilities are no longer considered eligible for
CVE tracking, despite being real, independently discovered, responsibly
disclosed, and acknowledged by the vendor.

The vendor has stated that fixes are being implemented and that private customer
notifications will be issued internally.

While remediation is of course welcome, this outcome highlights a broader issue:
vulnerabilities in SaaS platforms can effectively disappear from public
vulnerability tracking, simply because the deployment model removes user agency,
a model that arguably incentivizes security through obscurity, rather than
transparency.

The technical findings remain valid.

This update is shared purely for accuracy and record-keeping.

On Sun, Jan 4, 2026 at 4:40 PM <yuffie.kisaragi () atomicmail io
[yuffie.kisaragi () atomicmail io]> wrote:
```

> ```
> UPDATE:
>
>
> The reported vulnerabilities have now been assigned CVE identifiers:
> CVE-2025-34411: https://www.cve.org/cverecord?id=CVE-2025-34411
> [https://www.cve.org/cverecord?id=CVE-2025-34411]
> CVE-2025-34412: https://www.cve.org/cverecord?id=CVE-2025-34412
> [https://www.cve.org/cverecord?id=CVE-2025-34412]
> ```

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](11)
[By Date](date.html#4)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](11)
[By Thread](index.html#4)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Multiple Security Misconfigurations and Customer Enumeration Exposure in Convercent Whistleblowing Platform (EQS Group)** *Yuffie Kisaragi via Fulldisclosure (Jan 05)*

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