---
title: Remote DoS in httpx 1.7.0 – Out-of-Bounds Read via Malformed <title> Tag
url: https://seclists.org/fulldisclosure/2025/Jun/26
source: Full Disclosure
date: 2025-06-27
fetch_date: 2025-10-06T22:57:04.104671
---

# Remote DoS in httpx 1.7.0 – Out-of-Bounds Read via Malformed <title> Tag

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

![](/shared/images/nst-icons.svg#search)

# Remote DoS in httpx 1.7.0 – Out-of-Bounds Read via Malformed <title> Tag

---

*From*: Brian Carpenter via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 24 Jun 2025 16:04:56 +0000

---

```
Hey list,

You can remotely crash httpx v1.7.0 (by ProjectDiscovery) by serving a malformed <title> tag on your website. The bug
is a classic out-of-bounds read in trimTitleTags() due to a missing bounds check when slicing the title string. It
panics with:

panic: runtime error: slice bounds out of range [9:6]

Affects anyone using httpx in their automated scanning pipeline. One malformed HTML response = scanner down. Unit
testing or fuzzing this function would’ve caught it in 5 minutes. But it’s “just a bug.” 😂

💥 Trigger input:

<title</></title>0

📍 Vulnerable code:

func trimTitleTags(title string) string {
    titleBegin := strings.Index(title, ">")
    titleEnd := strings.Index(title, "</")
    if titleEnd < 0 || titleBegin < 0 {
        return title
    }
    return title[titleBegin+1 : titleEnd] // ← PANIC here
}

✅ Fix:
https://github.com/projectdiscovery/httpx/pull/2198

📂 PoC + context:
https://github.com/projectdiscovery/httpx/issues/2197

Crash scanners. Create blind spots. Chain with HTML injection. Happy hunting.

Stay glitchy,

—geeknik
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
[![Next](/images/right-icon-16x16.png)](27)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
[![Next](/images/right-icon-16x16.png)](27)

### Current thread:

* **Remote DoS in httpx 1.7.0 – Out-of-Bounds Read via Malformed <title> Tag** *Brian Carpenter via Fulldisclosure (Jun 25)*

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