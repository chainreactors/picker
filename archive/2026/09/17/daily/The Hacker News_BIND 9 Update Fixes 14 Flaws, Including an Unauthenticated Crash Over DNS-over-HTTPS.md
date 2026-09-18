---
title: BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS
url: https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:39.803676
---

# BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [BIND 9 Update Fixes 14 Flaws, Including an Unauthenticated Crash Over DNS-over-HTTPS](https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html)

**Swati Khandelwal**Sep 17, 2026Vulnerability / DNS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEd6WLqBvkSx9Y2P6HrNL-VApj7Xb05Wlhnw4pPW6-X9NwGiAeAm_Hf4KYj_1hEy6uITGe8kh3xgYeTAha8nR5inx0snMzfWGP2Qd8kRuiOp0h4O49J-33kPpA1cuGhClV2qAvPyhyr2BqSYj9ZIvI6c-wncUNGESpGK-3tivnS-HIrOj9ZdSJALq_8Ts/s1700-nu-rw-lo-l85-e365/bind9.jpg)

The Internet Systems Consortium (ISC) has released [BIND 9.20.29 and 9.21.26](https://www.isc.org/download/) to fix fourteen security flaws it [disclosed](https://www.openwall.com/lists/oss-security/2026/09/16/4) on 16 September in BIND 9, its open-source DNS server software. One of them affects any BIND server that answers DNS-over-HTTPS (DoH).

A sender with no credentials can crash the server process, named, with a single request that carries an invalid SIG(0) signature, if the sender closes the connection before named finishes checking the signature.

ISC said in its advisories that it is not aware of any of the fourteen being exploited.

### Which Release Fixes What

The fixed releases, described in ISC's [release notes](https://bind9.readthedocs.io/en/stable/notes.html#notes-for-bind-9-20-29), are:

* BIND 9.20.29, on the current stable branch: fixes all fourteen
* BIND 9.21.26, on the development branch: fixes thirteen, because CVE-2026-19662 does not affect 9.21
* BIND 9.20.29-S1, the Supported Preview Edition for support customers: fixes all fourteen

ISC lists no workarounds for any of the fourteen.

Twelve of the fourteen also affect the older 9.18 branch, up to and including 9.18.50, its final release. ISC [ended support for 9.18](https://kb.isc.org/docs/bind-9-end-of-life-dates) at the end of June and lists no 9.18 release that fixes them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

ISC said [in May](https://www.isc.org/blogs/2026-05-12-bind-security-updates/) that 9.18 users should plan to update to 9.20 as soon as possible. Its vulnerability matrix adds that "EOL versions should be assumed to be vulnerable to new CVEs."

Operating-system packages are a separate matter. Debian 12 ships a package based on 9.18.49, and its [security tracker](https://security-tracker.debian.org/tracker/source-package/bind9) had not listed any of the fourteen as of 06:20 UTC on 17 September.

### What an Attacker Needs

Two of the fourteen can be triggered by a request alone, without the attacker needing a DNS server of their own, and both affect only the 9.20 and 9.21 branches. The DoH crash is **CVE-2026-77692**. The second, **CVE-2026-76163**, lets a query of type TKEY crash named when the server's named.conf has no global options block.

The other crashes need a recursive resolver, the kind of server that looks up names on behalf of clients, to receive crafted data from a server the attacker controls.

A single crafted response can crash a resolver on a default configuration (CVE-2026-19667), a resolver using dns64 with break-dnssec yes (CVE-2026-19666), or a validating resolver that receives a wildcard answer carrying both NSEC and NSEC3 proofs (CVE-2026-80274). A fourth, CVE-2026-19662, needs a particular order and timing of answers and does not affect 9.21.

Four more use up a resolver's CPU or memory instead of crashing it, two of them through cached SVCB/HTTPS alias records (CVE-2026-81563 and CVE-2026-81736). ISC rates seven of the fourteen High, all at 7.5 on CVSS 3.1: the crashes above except CVE-2026-19662, plus the two SVCB/HTTPS flaws. The other seven are Medium, from 5.3 to 6.5.

The remaining four flaws concern the integrity of DNS data, what a server serves or what a resolver accepts, rather than crashes or exhaustion. ISC rates all four Medium, and each comes with conditions on where the attacker sits or what they already control.

Two let a validating resolver accept the wrong DNSSEC proof. With CVE-2026-19941, a signed NSEC record from an unrelated zone can pass as proof that no wildcard exists. An on-path attacker, or a malicious forwarder, that controls a signed zone could use that to get a forged NXDOMAIN answer accepted for a name that should resolve through a wildcard, and the answer would pass DNSSEC validation.

With CVE-2026-77119, a signed NSEC3 record from an unrelated sibling zone can pass as proof that a delegation is unsigned. An attacker able to inject responses to the resolver's queries could then get a forged unsigned answer accepted for names beneath that delegation. ISC describes both outcomes as cache poisoning.

CVE-2026-19033 concerns a secondary server that copies a zone from a primary and accepts only transfers signed with a TSIG key. During a multi-message incremental transfer (IXFR) over TCP, named could start serving the new zone data before the final message carrying the signature arrived, and did not roll back if that signature never came. A party able to deliver such a transfer could get unauthorized zone contents served without holding the key.

The fix requires a TSIG on every message of an incoming transfer, and ISC says modern name servers already sign every message, so it expects no change in practice.

CVE-2026-78301 needs more access: an attacker who can get a malformed zone loaded onto an authoritative server, for example through a zone transfer. A zone containing an NS or DNAME node above its own origin is then treated as a zone cut, so queries for names inside the zone return an out-of-zone delegation instead of the zone's data.

If the server also recurses, it can follow delegation and cache attacker-supplied records for names outside the zone, and the effect lasts as long as the malformed zone remains loaded.

### The Fourteen Flaws

| CVE | ISC score | Effect | Condition | Affected (open source) | Fixed in |
| --- | --- | --- | --- | --- | -...