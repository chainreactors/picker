---
title: Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely
url: https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html
source: The Hacker News
date: 2026-11-12
fetch_date: 2026-11-13T09:07:46.337334
---

# Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgueiGhtTJ4g8vfPjVOP22mnT6eczZI-CgiOkXQ_Zv0gVno2MkG5UlOExxvSSAylm8NAtCfFkeaPxbyR3vYtpyOVi9ROWrrVZ9FKHFBH1IrQCCR46b2kh7JNKxenqefzCkCUewWhqRlds-IYjwzH7N7iWGpXxzeqhS6vIHDWIohTDx2ZZZReOOwVWv-SAmG/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-infographic-d)

# [Critical Apache HTTP/2 Flaw Could Let Unauthenticated Attackers Execute Code Remotely](https://thehackernews.com/2026/11/critical-apache-http2-flaw-could-let.html)

**Swati Khandelwal**Nov 12, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLpi_uN6PmG2Gn1agNMsOrsCp324eH-utKkDl_SPe32ggjcWFPjxZSyeA1KvAtvI9SQ4VAN_zssvdJLJ59IXE8_-MatPOyFXY-FcwtL7HtfKyW3MtsKwglIe2X62WBOcUkPMv-klM1h8T2EBMWFOWyPG89bfbAHS5byyfXATXN_lUUJWmUGWChekyWxTQ/s1700-nu-rw-lo-l85-e365/apache-http.jpg)

A critical flaw in Apache HTTP Server's HTTP/2 module, **mod\_http2**, can let a remote attacker run code on the server. Tracked as **CVE-2026-119618**, it affects versions 2.4.55 through 2.4.70 and is fixed in version 2.4.71, released yesterday.

Only servers with HTTP/2 enabled are affected, according to Red Hat, which ships the server as part of Red Hat Enterprise Linux.

An attacker who can reach the server needs no authentication to exploit the flaw and could take full control of the server process, the Linux vendor says. It rates the flaw 9.8 out of 10 on the CVSS scale.

The vendor's assessment, published yesterday, also says "public research has demonstrated a reliable exploit" against a server in its default configuration with mod\_http2 enabled. It does not name or link that research. Security company Wiz said later that day that no exploit was available and that no exploitation in the wild had been reported.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

HTTP/2 runs only where the Protocols directive turns it on, as the [module documentation](https://httpd.apache.org/docs/2.4/mod/mod_http2.html) explains. The directive uses h2 for HTTP/2 over TLS and h2c for HTTP/2 over plain TCP. It can be set for the whole server or for a single virtual host, so admins should check the server-wide setting and every virtual host.

Standalone builds of the module, released on GitHub as mod\_h2, are affected from version 2.0.8 through 2.0.42.

Admins who run the Apache HTTP Server project's own releases should move to version 2.4.71, the fixed release named in its [security advisory](https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2026-119618). That release also fixes a crash in mod\_md, rated important, and a one-byte overwrite of stack memory in mod\_vhost\_alias, rated low.

The distributions in the table below ship their own builds of the server, with their own package version numbers. On Red Hat Enterprise Linux 9, for example, the fix ships as mod\_http2-2.0.26-7.el9\_9.1.

Red Hat shipped fixes for Red Hat Enterprise Linux 9 and 10 yesterday and rates the flaw Important on those releases rather than Critical. Their mod\_http2 packages give each HTTP/2 stream its own memory allocator, which makes an attack much harder, according to the vendor's [severity assessment](https://access.redhat.com/security/cve/cve-2026-119618). Red Hat Enterprise Linux 8 and earlier do not contain the vulnerable code.

| Platform | Status | Fixed package |
| --- | --- | --- |
| Apache HTTP Server project releases | Fixed | 2.4.71 |
| Red Hat Enterprise Linux 9 | Fixed (RHSA-2026:98981) | `mod_http2-2.0.26-7.el9_9.1` |
| Red Hat Enterprise Linux 10 | Fixed (RHSA-2026:98978) | `mod_http2-2.0.29-5.el10_3.1` |
| Red Hat Enterprise Linux 9.4 Update Services for SAP Solutions, and 9.6, 9.8, 10.0 and 10.2 Extended Update Support | Fixed (RHSA-2026:98968, RHSA-2026:98954, RHSA-2026:98982, RHSA-2026:98953 and RHSA-2026:98979) | See each advisory |
| Red Hat Enterprise Linux 6, 7 and 8 | Not affected | None needed |
| Red Hat JBoss Core Services and Red Hat Hardened Images | Affected, no fix listed | None listed |
| Debian unstable (sid) | Fixed | `apache2 2.4.71-1` |
| Debian bookworm, trixie and forky | Vulnerable | None listed |
| Amazon Linux 2 (Core), Amazon Linux 2023 and Amazon Linux 2027 Preview | Pending fix | None listed |
| Ubuntu | No status page | None listed |

The Debian rows come from Debian's [security tracker](https://security-tracker.debian.org/tracker/CVE-2026-119618), and the Amazon row from the [Amazon Linux tracker](https://explore.alas.aws.amazon.com/CVE-2026-119618.html). Ubuntu's CVE tracker had no page for the flaw when The Hacker News checked it today.

The Apache HTTP Server advisory offers no workaround. In its [vulnerability analysis](https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability), Wiz advises admins who cannot update yet to remove h2 and h2c from the Protocols directive, leaving Protocols http/1.1.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The standalone mod\_h2 project has published no fixed release so far. Its [release list](https://github.com/icing/mod_h2/releases) on GitHub ends at 2.0.42, the last affected version, and its repository has been read-only since it was archived on June 9. The Protocols change above also applies to servers that use those builds.

The flaw was reported on October 26 by Anthropic's OSS Scanner, a [free scanning service](https://thehackernews.com/2026/10/anthropic-launches-free-ai.html) for open-source projects that uses the company's AI models. Anthony Weems and Simon Scannell of Google Cloud Vulnerability Research reported it last week.

An [earlier HTTP/2 flaw](https://thehackernews.com/2026/05/critical-apache-http2-flaw-cve-2026.html), CVE-2026-23918, was fixed in version 2.4.67, released on May 4. Servers updated to that release, or to any later one up to 2.4.70, still run a version that the new flaw affects.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**
...