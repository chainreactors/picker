---
title: Dangling DNS record for bastion.certb.cdp.bethesda.net
url: https://seclists.org/fulldisclosure/2026/Aug/35
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:27:51.887340
---

# Dangling DNS record for bastion.certb.cdp.bethesda.net

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

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Dangling DNS record for bastion.certb.cdp.bethesda.net

---

*From*: shed riot <shed.riot () gmail com>
*Date*: Fri, 24 Jul 2026 10:43:16 +0100

---

```
# Summary

The hostname resolved to an address within a dynamic cloud IP pool.
The address had been released and was no longer controlled by the
organisation operating the hostname.

This condition is referred to as an "afterlife" issue.

Unlike a conventional CNAME-based subdomain takeover, the DNS record
pointed directly to a reusable cloud IP address. An attacker obtaining
that address could receive traffic intended for the Microsoft-owned
hostname and serve content from it.

I reported the issue to the Microsoft Security Response Center as:
VULN-198489

MSRC closed the report as a non-MSRC case, because the IP address was
not in Azure. Doh.

# Vulnerability

Persistent dangling DNS record to a reusable cloud IP address.
CWE-16: Configuration

# Impact

Impact includes:

* obtaining trusted TLS certificates for the affected hostname;
* serving attacker-controlled content from a trusted hostname;
* receiving traffic intended for the previous service;
* exposure of cookies, bearer tokens or session identifiers;
* exposure of request bodies, API keys or webhook payloads;
* abuse of CORS, OAuth or other domain-based allowlists;
* abuse of same-site cookie and browser trust relationships; and
* phishing or malware hosted under the organisation's domain.

## Proof of Concept (PoC)

1. open a browser and navigate to
   `https://bastion.certb.cdp.bethesda.net`
2. an `afterlife` holding page will be served from the affected
   hostname
3. observe that the browser reports a valid trusted TLS certificate
   for the affected hostname
4. navigate to `https://crt.sh/?q=bastion.certb.cdp.bethesda.net`
   and observe that a new Let's Encrypt certificate has been issued
   (may require a few refreshes as over-subscribed)
5. navigate to `https://bethesda.net/` and login (create an account
   if required)
6. navigate to `https://bastion.certb.cdp.bethesda.net/request.txt`
   and observe that the full request is displayed, along with the
   domain scoped cookies that were received

# Vendor response and timeline

30 June 2026

I submitted the report as VULN-198489.

The portal did not assign an MSRC case number. The recorded status was
"Complete - NA".

MSRC's rejected the issue as outside MSRC's scope, because the IP was
not in Azure.

# References

* MSRC submission VULN-198489
* CWE-16: Configuration
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](34)
[By Date](date.html#35)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](34)
[By Thread](index.html#35)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **Dangling DNS record for bastion.certb.cdp.bethesda.net** *shed riot (Aug 06)*

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