---
title: Amplitude customers using domain proxies should update their configuration immediately.
url: https://seclists.org/fulldisclosure/2026/Jul/27
source: Full Disclosure
date: 2026-07-23
fetch_date: 2026-07-24T05:05:43.924238
---

# Amplitude customers using domain proxies should update their configuration immediately.

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# Amplitude customers using domain proxies should update their configuration immediately.

---

*From*: shed riot <shed.riot () gmail com>
*Date*: Tue, 21 Jul 2026 09:17:13 +0100

---

```
After receiving live analytics requests intended for `api2.amplitude.com`,
I contacted `security () amplitude com` and was invited to submit the issue
through Amplitude's private Bugcrowd programme.

In my view, Amplitude's handling of the report, including closing it as
"Not applicable" despite evidence of intercepted customer traffic, caused
by insecure configurations and documentation, constitutes a negligent
approach to protecting customer data, and a bad-faith bug bounty programme.

Two conditions combined to make interception possible.

1. Stale DNS and ephemeral IP reuse

Amplitude infrastructure used ephemeral addresses from an AWS public IP
pool. After an address was released, it could be reassigned to another
party, while systems with a cached DNS answer continued sending traffic to
it until the cached record expired.

This is not a conventional dangling-CNAME takeover. It is an IP "afterlife"
condition involving stale DNS resolutions and recycled public-cloud
addresses.

2. Missing upstream TLS certificate validation

Amplitude's documentation recommends using a domain proxy to front its
services. However, its example NGINX configuration does not enable
validation of the upstream TLS certificate. Similar certificate-validation
gaps also exist in default or commonly deployed configurations for some
cloud load balancers, CDNs and WAFs.

Consequently, affected customer proxies accepted invalid or self-signed
certificates when forwarding requests towards `api2.amplitude.com`.

The combination of stale address resolution and missing certificate
validation enabled traffic intended for Amplitude to be intercepted by a
party controlling a reassigned cloud address. The duration and full scope
of the exposure are not known.

The sample intercepted traffic provided privately to Amplitude contained
requests originating from the following sites:

* `www.f5.com`
* `uplatform.team`
* `mystylus.ai`

No captured traffic, identifiers, payloads or user data are being disclosed.

Timeline:

* 26 June 2026: Contacted `security () amplitude com`.
* 9 July 2026: Received an invitation to Amplitude's private Bugcrowd
programme and submitted the report.
* 16 July 2026: Amplitude disputed that the evidence demonstrated
interception.
* 17 July 2026: I clarified that the requests contained data categorised as
personal data in Amplitude's own documentation, including persistent device
identifiers, session identifiers and linkable usage data.
* 18 and 20 July 2026: Reported additional batches of live traffic.
* 20 July 2026: Identified that Amplitude's recommended NGINX domain-proxy
configuration omitted upstream certificate validation.
* 21 July 2026: Amplitude acknowledged that the captured traffic had passed
through customer domain proxies that did not validate upstream
certificates. Bugcrowd subsequently closed the report as "Not applicable".

Recommended action:

Amplitude should contact affected customers, advise them of the potential
interception of personal data, review its DNS and load-balancer
architecture, and revise its domain-proxy documentation so that upstream
certificate and hostname validation are enabled by default.

Customers should enable certificate-chain and hostname validation on every
HTTPS connection from a proxy, CDN, WAF, service mesh or load balancer to
Amplitude.

Customers should also review DNS caches and forwarding logs, identify
traffic sent to previously assigned cloud addresses, assess whether
analytics events were intercepted or lost, and rotate any sensitive values
present in affected requests.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

### Current thread:

* **Amplitude customers using domain proxies should update their configuration immediately.** *shed riot (Jul 22)*

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