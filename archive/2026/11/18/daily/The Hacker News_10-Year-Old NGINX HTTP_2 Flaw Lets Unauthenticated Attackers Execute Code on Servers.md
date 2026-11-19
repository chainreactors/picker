---
title: 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers
url: https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
source: The Hacker News
date: 2026-11-18
fetch_date: 2026-11-19T09:47:33.737396
---

# 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1FgbfB9gCsTYnkXg_UHMHoWinmHvbkdAdbnpnrFQzzIG00gtoQsaz3DVhUgvHic2vd-yM_5XIb9H5N6i7stc2WQFHqPn9bN7B_IIFDtEJbNnNcvNZ3IbmHi-kKM8V_3VaZj1zzoHwCVjkzUQwFzzTMhaTH7W2jlKhsI9m3HEBAVjHyuBiJBdX0l8jX9Ll/s727-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/claude-security-tips-d)

# [10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on Servers](https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html)

**Swati Khandelwal**Nov 18, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi7_qqPophooIauX16fMWm3KB24tzQ3Fd7rCuseCXfMkDPPGpIgmHqWvZjn_jffDqHwNWKu8Zf57QeKb4qsRFgdgisSAn0sMj59CscimR16RLXI1kspH0w7VYQgrsM_hPcePQOFL8QUyDC2p9W7AV0UjH3sW7oOvdWPWAZW6DITDvqIHaC_696e5kHTieY/s1700-nu-rw-lo-l85-e365/nginx-rce.jpg)

A flaw in **NGINX**'s HTTP/2 support can allow an attacker to run code on servers with HTTP/2 enabled, without needing to log in.

The decade-old flaw, **CVE-2026-123007,** dubbed "**nginx2root**," has been present in NGINX's open-source code since version 1.9.5, released on September 22, 2015. Fixed versions 1.31.9 and 1.30.7 came out today.

**F5**, the company behind NGINX, says attackers can run code where ASLR is turned off or can be bypassed. Security researchers at **Wiz** said they bypassed ASLR and ran code through the flaw in tests. Xint's researchers said they ran code through it with nothing more than a reachable HTTP/2 port.

Code run this way gets the permissions of an NGINX worker process. Getting root on the host takes a second way to raise privileges, according to CIRCL, the Computer Incident Response Center Luxembourg.

In Xint's tests, code running as a worker could get root on the host through a separate bug in the Linux kernel's SCTP code, even when NGINX ran inside a Docker container.

Neither the vendor nor the Wiz and Rapid7 researchers have reported any attacks exploiting the flaw so far. CISA's Known Exploited Vulnerabilities catalog did not list it as of today.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threat-protection-d)

[Proof-of-concept code](https://github.com/sfewer-r7/CVE-2026-123007) for the flaw is publicly available on GitHub, but its notes state it is suitable only for demonstrating the attack against a freshly started Docker container on the same machine.

Every open-source release from 1.9.5 through 1.31.8 is vulnerable, according to NGINX's [security advisories](https://nginx.org/en/security_advisories.html). That includes 1.31.8 from October 21, as well as the October 14 [security releases](https://thehackernews.com/2026/10/nginx-fixes-5-flaws-including-possible.html) 1.31.7 and 1.30.6.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbokJwpAhyjrniUZuUDLtYlNLYspzJ8DZiXN_b-mc6aEZWxDDRlrUa_C4bjo4ue0bAaykvwDcsRM69Nv0-pQC0B_WQ8dQ1xzJpLrQqR9hT8cynGdLqQfChGOcdSgLoRX0UDDXnWDGv4ZcSOtqzoNvMBugbzzda2jzHAvnyZAIz2K8QjZgSGtAGt9yLXwI/s1700-nu-rw-lo-l85-e365/wiz.gif) |
| Wiz PoC |

NGINX Plus is affected too, in 37.x releases before the fixed builds and in R34 to R36, according to the [vendor advisory](https://my.f5.com/manage/s/article/K000163926).

Today's releases also fix four more flaws that the vendor says can lead to code execution under the same ASLR condition. It scores all five 9.2 out of 10 on CVSS 4.0.

Each flaw can be reached only in a particular setup:

| Flaw | What it needs |
| --- | --- |
| CVE-2026-123007 | HTTP/2 turned on |
| CVE-2026-123633 | HTTP/2, with requests passed to a backend server while the worker is running low on `worker_connections` |
| CVE-2026-123634 | A proxied server name built from variables, plus a server-side include (SSI) or `mirror` subrequest to a location that looks up the same name |
| CVE-2026-121810 | HTTP/3 turned on |
| CVE-2026-113425 | NGINX used as a mail proxy |

HTTP/2 is on where a `listen` directive includes `http2`, or where `http2 on` is set. Running `openssl s_client` with `-alpn h2` against a server shows whether it accepts HTTP/2: the output reads `ALPN protocol: h2` if it does. Behind a CDN, test the NGINX origin itself, because an origin that accepts only HTTP/1.1 cannot be attacked through HTTP/2.

### Fixes, Workarounds and Signs of Attack

These releases fix CVE-2026-123007, according to F5:

* NGINX Open Source 1.31.0 to 1.31.8 (mainline): fixed in 1.31.9
* NGINX Open Source 1.9.5 to 1.30.6, including older branches such as 1.28: fixed in 1.30.7
* NGINX Plus 37.1.0 to 37.2.0.1: fixed in 37.3.0.1
* NGINX Plus 37.0.0 to 37.0.7.1: fixed in 37.0.8.1
* NGINX Plus R34 to R36: no fix listed

Versions 1.31.9 and 1.30.7 fix all five flaws, according to NGINX's [release notes](https://nginx.org/en/CHANGES). On NGINX Plus, 37.3.0.1 and 37.0.8.1 fix four of the flaws, and the CVE-2026-123633 fix was introduced in the earlier builds 37.2.0.1 and 37.0.7.1.

After upgrading, restart NGINX fully or use its live binary upgrade. A reload alone leaves the old executable running, and existing connections can stay on old worker processes.

The [official Docker images](https://hub.docker.com/_/nginx/tags?name=1.31.9) for NGINX had 1.31.9 and 1.30.7 tags as of today, including Alpine variants.

Ubuntu and Debian had not shipped fixed packages as of today. Ubuntu's [CVE status page](https://ubuntu.com/security/CVE-2026-123007) listed nginx as vulnerable on its releases from 16.04 to 26.10, and Debian's [security tracker](https://security-tracker.debian.org/tracker/CVE-2026-123007) listed it as vulnerable in bookworm, trixie, forky and sid. A distribution package can carry a fix without changing the version number that `nginx -v` reports, so compare the full package version with the distribution's own advisory.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiK0N4lFh6FzbyZpN46BG96-etDeegqvajihYo41G6mQH3jKnjp4zTyt-eg9qOy1kopOllZdE3rs8_BOlLURy20YVIk8-pWCs4JXVB0lO6F46p0C9iFGcePs5rm3uCmisbSXywalW020F4SZGPWS0i23g_SPcQ6v2GBywfvOs72KkyEkORlVtkb2Pbp8Y/s1700-nu-rw-lo-l85-e365/poc.gif) |
| Xint PoC |

The vendor lists workarounds for only two of the five flaws. For the resolver flaw, CVE-2026-123634, avoid SSI and `mirror` directives, and do not build a pro...