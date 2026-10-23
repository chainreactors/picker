---
title: Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes
url: https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:43.048513
---

# Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes

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

# [Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before Kernel Fixes](https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html)

**Swati Khandelwal**Oct 22, 2026Vulnerability / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdNNyKzD2udgIl0X434MI2ucEwGFB_B-QqyjMnMuvTfwZv7clEo3n0ASA_aEQtUmQ7wqPSREwq1Cvi3iQLtubfUkK7p017Q6SrliTkwHiJyhfDIzahdof71Mxs4LXqJWoLkAnwikxy2KmZ1pkMg5Qto-RwPnvQx71Ol4G7sO20eeVNr_pfstT2WbDg3Nk/s1700-nu-rw-lo-l85-e365/linux-rce.jpg)

Linux servers running KSMBD, the kernel's built-in SMB server, are exposed to two publicly reported remote code execution flaws rated 9.0 by [Trend Micro's Zero Day Initiative](https://www.zerodayinitiative.com/advisories/upcoming), with no fix yet in the mainline kernel.

One of them, ZDI-CAN-33774, can be triggered before any network authentication. The other, ZDI-CAN-33549, requires the SMB Direct transport and an RDMA-capable network interface.

[ZDI-CAN-33549](https://lore.kernel.org/lkml/BYAPR01MB3830472B5702C089B0BBB77D80662%40BYAPR01MB3830.prod.exchangelabs.com/) is an integer underflow in KSMBD's SMB Direct path. A client can supply RDMA buffer descriptors in which the first is longer than the declared payload, causing the server's size counter to wrap and allowing a subsequent memory copy to overrun the end of an allocated buffer.

It requires three things: an RDMA-capable interface (hardware or the rxe software driver), a writable KSMBD share, and a client negotiating SMB Direct.

[ZDI-CAN-33774](https://lore.kernel.org/lkml/BYAPR01MB383076AC412E19C48CFBEAE980662%40BYAPR01MB3830.prod.exchangelabs.com/) requires no authentication, exposing any server running KSMBD on port 445. The flaw is a race in how KSMBD assigns its handler table: a burst of short SMB1 packets followed by an SMB2 packet in the same TCP write causes workers to handle SMB1 data with an SMB2 handler, reading past the end of the shorter buffer. A path to writing past the buffer also exists once an attacker has access to a share.

As of Thursday, neither flaw has a named fix in the mainline kernel or in [linux-next](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/log/fs/smb), the integration tree that feeds it. [Linux news site Phoronix](https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities) said SMB Direct maintainer Stefan Metzmacher submitted a fix for ZDI-CAN-33549 targeting the next kernel development cycle, but this has not been confirmed elsewhere.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Fixes to mainline typically take weeks to reach stable branches and distribution kernels after that. Neither flaw has a CVE identifier, since the [kernel project](https://docs.kernel.org/process/cve.html) assigns those only after a stable-tree fix is available.

Running systemctl status ksmbd or lsmod | grep ksmbd confirms whether the module is active. Red Hat Enterprise Linux does not include KSMBD by default, [according to Red Hat's support documentation](https://access.redhat.com/solutions/6991749).

The ZDI reports credit TrendAI, Trend Micro's AI scanner, as the finder. The Linux kernel's [security documentation](https://docs.kernel.org/process/security-bugs.html), updated in May 2026 following [guidance from Linus Torvalds](https://lwn.net/Articles/1073193/), states that bugs found by AI tools are, by definition, already public and should be sent to subsystem developer lists.

ZDI's routing appeared to follow that logic, copying public mailing lists alongside the private kernel security address without attaching patches to any of the reports.

Stable-kernel maintainer Greg Kroah-Hartman replied to three of the five kernel reports within minutes of each other. To the [report on the VMware GPU driver](https://lore.kernel.org/dri-devel/2026102254-protector-seventy-6454%40gregkh/), he wrote: "For some reason you sent this to public lists, and did not include a patch, so there's not much we can do with this." On the [NVMe driver report](https://lore.kernel.org/all/2026102226-duly-imprison-a2c1%40gregkh/), seventeen seconds later: "Again, no patch, and sent to a public list? Please fix your submission process."

| ZDI ID | Subsystem | Flaw class | CVSS | Affects KSMBD? |
| --- | --- | --- | --- | --- |
| [ZDI-CAN-33549](https://lore.kernel.org/lkml/BYAPR01MB3830472B5702C089B0BBB77D80662%40BYAPR01MB3830.prod.exchangelabs.com/) | KSMBD SMB Direct | Remote code execution | 9.0 | Yes (SMB Direct and RDMA required) |
| [ZDI-CAN-33774](https://lore.kernel.org/lkml/BYAPR01MB383076AC412E19C48CFBEAE980662%40BYAPR01MB3830.prod.exchangelabs.com/) | KSMBD protocol dispatch | Remote code execution | 9.0 | Yes (any KSMBD install) |
| [ZDI-CAN-33367](https://lore.kernel.org/lkml/BYAPR01MB3830CECF5D0871064C59BA0280662%40BYAPR01MB3830.prod.exchangelabs.com/) | Networking (skb\_zerocopy) | Local privilege escalation | 7.8 | No |
| ZDI-CAN-34068 | VMware GPU driver (vmwgfx) | Local privilege escalation | 8.8 | No |
| ZDI-CAN-34076 | NVMe target driver (nvmet) | Information disclosure | 8.6 | No |

Three of the five kernel reports are not related to SMB. [ZDI-CAN-33367](https://lore.kernel.org/lkml/BYAPR01MB3830CECF5D0871064C59BA0280662%40BYAPR01MB3830.prod.exchangelabs.com/), discovered by researcher **p1r0x**, is a local privilege escalation in the kernel's networking stack that requires local access. ZDI-CAN-34068 is a local privilege escalation in the VMware virtual GPU driver, ZDI-CAN-34076 is an information disclosure in the NVMe target driver, and neither affects KSMBD servers.

A sixth ZDI report, ZDI-CAN-32005, is a [buffer overflow in ConnMan](https://lore.kernel.org/all/BYAPR01MB383046745372577D8F5902D580672%40BYAPR01MB3830.prod.exchangelabs.com/), a network daemon separate from the Linux kernel.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUt...