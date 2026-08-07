---
title: CL.0 desync in www.microsoft.com
url: https://seclists.org/fulldisclosure/2026/Aug/34
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:28:03.320681
---

# CL.0 desync in www.microsoft.com

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

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

![](/shared/images/nst-icons.svg#search)

# CL.0 desync in www.microsoft.com

---

*From*: shed riot <shed.riot () gmail com>
*Date*: Fri, 24 Jul 2026 10:21:16 +0100

---

```
# Summary

I reported the issue to the Microsoft Security Response Center twice:

* VULN-165381, MSRC case 102964
* VULN-165876, MSRC case 103259

In both cases, they do not appear to have even looked at the PoCs, and so
have failed to adequately investigate before reaching a decision.

# Vulnerability

CWE-444: HTTP Request/Response Smuggling

The observed behaviour was consistent with CL.0 HTTP desync within the
request-processing chain.

# Impact

HTTP desync can cause attacker-controlled bytes to be interpreted as
the beginning of another request on a shared back-end connection.

Depending on routing and connection reuse, this vulnerability class
can potentially be used to:

* alter or prefix another user's request;
* redirect users to attacker-controlled content;
* deliver reflected or stored client-side payloads;
* poison application or intermediary responses; or
* disclose information associated with another request or user.

I deliberately limited testing to a non-destructive proof of concept.
I did not attempt to deliver an active payload to unrelated Microsoft
users or extract their data.

Testing a desync issue against production infrastructure can affect
third-party requests. A fully weaponised test would therefore have
created an unacceptable risk to legitimate users.

# Proof of concept

The supplied proof of concept used two independent clients.

The attacker client submitted a crafted request containing bytes
after the declared request body.

The victim client then made an ordinary request.

The attacker-controlled content was subsequently observed in the
victim-side transaction.

The result demonstrated cross-request interference, rather than an
unusual response confined to the attacker's own connection.

The second submission also included screenshots, as MSRC couldn't
be arsed to run the PoCs themselves.

# Timeline

26 October 2025

I submitted the initial report as VULN-165381 and uploaded separate
exploit and victim scripts.

27 October 2025

MSRC opened case 102964.

29 October 2025

MSRC requested a video and asked which internal component was
affected.

30 October 2025

I explained that a video would only show the supplied scripts running.
Microsoft would need to trace the crafted request through its own
application stack to identify where it was split.

I also asked whether MSRC had run the scripts.

31 October 2025

MSRC closed the case as "not a vulnerability".

4 November 2025

I submitted the issue again as VULN-165876, including the scripts and
screenshots showing the attacker, victim and successful result.

5 November 2025

MSRC opened case 103259.

10 November 2025

MSRC stated that it required a proof of concept "demonstrating an
exploit", despite the scripts already having been supplied. The
responses indicate that the proof of concept had not been run.

18 November 2025

I asked whether MSRC had run and validated the proof of concept.

19 November 2025

Microsoft closed the second case, stating:

"You have not submitted sufficient evidence of HTTP desync. You have
only provided 2 shell scripts and no other information confirming that
the exploit works."

The second submission also contained screenshots demonstrating the
attacker, victim and successful result.

20 November 2025

I challenged the assessment and pointed out that the proof of concept
displayed the issue clearly, and that both reports appeared to have
been closed without MSRC running the PoC.

MSRC maintained its position and requested a copy of the disclosure
draft for technical review.

# Resolution

Microsoft closed both reports and stated that it would not track the
issue further. At no point do they appear to have run any of the
supplied PoC scripts.

The vuln still exists, and isn't difficult to find for someone
willing to scan the site. Fill your boots!

# References

* MSRC submission VULN-165381, case 102964
* MSRC submission VULN-165876, case 103259
* CWE-444: HTTP Request/Response Smuggling
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](33)
[By Date](date.html#34)
[![Next](/images/right-icon-16x16.png)](35)

[![Previous](/images/left-icon-16x16.png)](33)
[By Thread](index.html#34)
[![Next](/images/right-icon-16x16.png)](35)

### Current thread:

* **CL.0 desync in www.microsoft.com** *shed riot (Aug 06)*

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