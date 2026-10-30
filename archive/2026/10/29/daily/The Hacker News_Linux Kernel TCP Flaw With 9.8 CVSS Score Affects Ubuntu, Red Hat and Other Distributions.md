---
title: Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions
url: https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html
source: The Hacker News
date: 2026-10-29
fetch_date: 2026-10-30T07:56:33.070249
---

# Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html)

**Swati Khandelwal**Oct 29, 2026Vulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfCJ0ttE8v4hkDjJRqbTvxlxFcoNtFJhbYCQ-o8NtaiyFLImEyA8aSO967eeZG9fRebhc8oVA-OloE9X9KVVAxM-H3wKvUlh8XmN6bGlEz2IJwMgcssmA7yIRi7YNOwVQYD6nhQCaWUg6fPy-QXVjfw6rV55LueKlLvZLazjKjTL94KJMMUZ2uZ3R019Km/s1700-nu-rw-lo-l85-e365/linux-flaw.jpg)

A flaw in the Linux kernel's TCP code, tracked as [**CVE-2026-98432**](https://www.cve.org/CVERecord?id=CVE-2026-98432), affects Ubuntu, Red Hat Enterprise Linux (RHEL), and other Linux distributions. The kernel's own CVE team rates it 9.8 out of 10 on the CVSS scale.

[Anthropic said](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude) on October 27 that its AI model wrote an exploit that uses the flaw to let a remote attacker with no credentials run commands as root on Linux servers with a multipath TCP listener.

As of October 29, Ubuntu and RHEL have not released a fixed kernel. Red Hat, Amazon, Oracle, and SUSE score the flaw between 5.9 and 8.1, lower than the kernel team's 9.8.

The flaw is a race condition in the code that sets up new IPv4 TCP connections. It can make the kernel read memory it has already freed, a bug type known as a use-after-free.

[The kernel fix](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e3f33b0a1d89d738e2b913dab519226eaf76e15b) credits Anthropic researcher Xinyang Ge with reporting the bug. Neither the CVE record nor the fix mentions multipath TCP (MPTCP). The link between that feature and this bug comes from Anthropic's post.

[MPTCP](https://docs.kernel.org/networking/mptcp.html) lets one connection use several network paths at once. On Linux, an application must request MPTCP when it opens a socket.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Anthropic's post says the flaw "was patched upstream and backported to all maintained stable kernel branches." For distribution users, that fix arrives only in the vendor's kernel package. Debian, Oracle Linux, SUSE, and Amazon Linux have shipped fixed packages, at least for some of their kernels, but Ubuntu and RHEL have not.

### Which Distributions Have a Fix

| Distribution | Vendor rating | Status as of October 29 | Fixed package or advisory |
| --- | --- | --- | --- |
| [Ubuntu](https://ubuntu.com/security/CVE-2026-98432) 22.04 LTS, 24.04 LTS, 26.04 LTS and 26.10 | Priority High | Work in progress | None released |
| Ubuntu 16.04, 18.04 and 20.04 | Priority High | Vulnerable | None released |
| [RHEL 8, 9 and 10](https://access.redhat.com/security/cve/cve-2026-98432), OpenShift 4 | Moderate, 5.9 (CVE page)  Important, 8.1 ( [advisory file](https://security.access.redhat.com/data/csaf/v2/vex/2026/cve-2026-98432.json)) | Fix deferred | None released |
| RHEL 7 | Not applicable | Not affected | Not needed |
| [Amazon Linux 2023](https://explore.alas.aws.amazon.com/CVE-2026-98432.html), kernel6.18 package | Important, 7.0 | Fixed October 24 | `kernel6.18-6.18.56-125.164.amzn2023` ([ALAS2023-2026-3251](https://alas.aws.amazon.com/AL2023/ALAS2023-2026-3251.html)) |
| Amazon Linux 2023, kernel6.12 package | Important, 7.0 | Fixed October 29 in Amazon's advisory; Amazon's CVE page still says pending | `kernel6.12-6.12.113-138.209.amzn2023` ([ALAS2023-2026-3335](https://alas.aws.amazon.com/AL2023/ALAS2023-2026-3335.html)) |
| Amazon Linux 2  Amazon Linux 2023, kernel package | Important, 7.0 | Pending fix | None released |
| [Oracle Linux 7, 8, 9 and 10](https://linux.oracle.com/cve/CVE-2026-98432.html), UEK kernel | Important, 8.1 | Fixed October 16 | ELSA-2026-500397, ELSA-2026-500398, ELSA-2026-500399 |
| [Debian](https://security-tracker.debian.org/tracker/CVE-2026-98432) trixie (stable) | No score listed | Fixed October 16 | `linux` 6.12.113-1 ([DSA-6568-1](https://lists.debian.org/debian-security-announce/2026/msg00482.html)) |
| Debian 12 (bookworm) | No score listed | Fixed October 17 and October 22 | `linux` 6.1.190-1 ([DLA-4841-1](https://lists.debian.org/debian-lts-announce/2026/10/msg00035.html))   `linux-6.12` 6.12.113-1~deb12u1 ([DLA-4850-1](https://lists.debian.org/debian-lts-announce/2026/10/msg00044.html)) |
| [SUSE Linux Micro 6.2](https://www.suse.com/security/cve/CVE-2026-98432.html), openSUSE Leap 16.0 | Important, 8.1 | Fixed | `kernel-default` 6.12.0-160000.40.1 or later |
| SLES 15 SP4 to SP6 LTSS, SLES 16.0, SLE Micro 5.3 to 5.5 | Important, 8.1 | In testing | None released |
| SLES 15 SP7 | Important, 8.1 | Affected, fix in progress | None released |

Ubuntu also lists its cloud, FIPS, and real-time kernels as vulnerable or as work in progress. Red Hat says its fixes are "currently deferred to a future update." Neither Red Hat nor Ubuntu gives a release date.

### How the Bug Works

The race happens during the TCP handshake. When a connection is completed, the kernel hands the IP options stored with the pending request to the new socket without copying them.

If that socket is destroyed while another CPU is still using the options to answer a resent connection request, the kernel reads freed memory.

IPv6 is not affected by this race because the kernel copies the options for IPv6 connections.

The bug was introduced in Linux 4.4. Kernel developers applied a fix on October 5, ten days before the CVE was published.

The fix makes the kernel wait until other CPUs finish reading the options before it frees them.

### Why the Scores Differ

The kernel's CVE team added the 9.8 score to the CVE record on October 24, nine days after publishing the CVE.

Its score assumes an attacker who sends a TCP connection request carrying IPv4 Record Route or Timestamp options, then resends the request to try to win the race. The team rated attack complexity low, saying ...