---
title: Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone
url: https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:39.059390
---

# Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone

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

# [Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)

**Swati Khandelwal**Sep 17, 2026Vulnerability / DNS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiFNFekCjM7qSAMNaeoNatwUPsjJY0Nj67yGKdlhq_zzLH9tyjQrXAByn9B6BvXEcMabyWnO5oWWE11_orN2h7G-7jRjGPSW48xtd4HySWIkI1fQzCbUDCVzRyc_KG3curUoXk4LgyckPwUO8aP65kR0CYnc90pkfXctHKXVQ7grKsc43drFZ63yRur20/s1700-nu-rw-lo-l85-e365/dns-admin.jpg)

Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an [advisory](https://nlnetlabs.nl/projects/unbound/security-advisories/) on Wednesday.

An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution.

Unbound 1.26.1, released the same day, fixes the bug, tracked as [CVE-2026-81642](https://nlnetlabs.nl/downloads/unbound/CVE-2026-81642.txt), along with eight other flaws. One of the eight, [CVE-2026-82717](https://nlnetlabs.nl/downloads/unbound/CVE-2026-82717.txt), is a heap corruption bug in CNAME synthesis reported by Ben Morris of Anthropic. It could also lead to remote code execution "under certain systems and compilation options," NLnet Labs said.

NLnet Labs has not reported exploitation of either bug, and CISA's entry for CVE-2026-81642 marked exploitation as "none" on Wednesday.

NLnet Labs rates the DNSKEY flaw Critical, with a CVSS score of 4.0 (9.1), and its scoring lists a network attack vector requiring no privileges or user interaction. NVD listed the CVE as "Awaiting Analysis" on Wednesday, so the 9.1 is the maintainer's own score.

The overflow happens while the validator digests a DNSKEY record whose owner name is a compression pointer into the record's own data. The impact NLnet Labs lists is denial of service, with remote code execution possible "through attacker controlled data."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Every version up to and including 1.26.0 is affected. That includes 1.25.2, the security release from July, and 1.26.0, released on August 4. The Critical validator bug NLnet Labs fixed in May, [CVE-2026-33278](https://nlnetlabs.nl/downloads/unbound/CVE-2026-33278.txt), is a different flaw, and the 1.25.1 update that fixed it does not fix this one.

NLnet Labs attaches no configuration condition to that range, and it has not said whether a resolver with DNSSEC validation switched off is reachable.

### Upgrade or Patch

[Unbound 1.26.1](https://nlnetlabs.nl/projects/unbound/download/) is available as source, with checksums and a PGP signature, and as Windows installers and binaries. If you cannot upgrade, the advisory gives two ways to patch the source tree:

* Apply the [minimal patch](https://nlnetlabs.nl/downloads/unbound/patch_CVE-2026-81642.diff) or the [complete patch](https://nlnetlabs.nl/downloads/unbound/patch_CVE-2026-81642_with.diff) for CVE-2026-81642 alone with patch -p1, for example patch -p1 < patch\_CVE-2026-81642\_with.diff, then run make install.
* Apply the [combined patch](https://nlnetlabs.nl/downloads/unbound/patch_combined_with-1.26.1_v2.diff) for all nine fixes instead. A minimal version of it also exists.

NLnet Labs says the standalone patches for CVE-2026-81642 and CVE-2026-82717 have been tested and work on 1.26.0. Its [security policy](https://nlnetlabs.nl/security-report/) is to patch the latest released version.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/enterprise-ai-security-a)

[Debian's security tracker](https://security-tracker.debian.org/tracker/source-package/unbound) listed unbound 1.26.1-1 as fixed in unstable on Thursday, with the bookworm, trixie, and forky branches still listed as vulnerable.

### The Nine Fixes

The [release notes](https://github.com/NLnetLabs/unbound/releases/tag/release-1.26.1) name nine CVEs. The table gives each one's affected range and trigger condition in NLnet Labs' wording.

| CVE | Severity | Affected versions | Needs | Impact |
| --- | --- | --- | --- | --- |
| CVE-2026-81642 | Critical | Up to and including 1.26.0 | An attacker who controls a malicious zone and queries the resolver | Denial of service, possible remote code execution |
| CVE-2026-82717 | High | Up to and including 1.26.0 | CNAME synthesis during an upstream response. Code execution "under certain systems and compilation options" | Denial of service, possible remote code execution |
| CVE-2026-81634 | High | Up to and including 1.26.0 | A 255-length query name with a large TCP response, from a malicious name server or a tampered response | Denial of service |
| CVE-2026-77955 | Medium | 1.13.2 up to and including 1.26.0 | Zones with zonemd-check: yes located below, but not at, a trust anchor | Denial of service, a window where tampered zone data is served before the ZONEMD check |
| CVE-2026-78227 | Medium | 1.22.0 up to and including 1.26.0 | Built with --with-libngtcp2 and quic-port configured | Denial of service |
| CVE-2026-80225 | Medium | Up to and including 1.26.0 | A sustained stream of distinct uncached names over one TCP or DoT connection | Degradation of service |
| CVE-2026-82720 | Medium | 1.12.0 up to and including 1.26.0 | Built with --with-libnghttp2 and https-port configured. NLnet Labs calls the impact limited | Denial of service |
| CVE-2026-85501 | Medium | Up to and including 1.26.0 | Malicious zones serving the ReTrap algorithmic complexity attacks (TagTrap, DelegationTrap, NsecTrap, AdditionalTrap) | Degradation of service |
| CVE-2026-77860 | Low | 1.20.0 up to and including 1.26.0 | The serve-expired code path, bypassing a countermeasure added for [DNSBomb](https://thehackernews.com/2024/05/researchers-warn-of-catddos-botnet-and.html) | Could take part in a pulsing DoS amplification attack |

The ReTrap fix also changes a d...