---
title: 18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers
url: https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:01.181040
---

# 18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers

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

![cybersecurity](data:image/svg+xml;base64...)

# [18-Year-Old Linux SCTP Flaw Could Let Local Users Gain Root and Escape Containers](https://thehackernews.com/2026/08/18-year-old-linux-sctp-flaw-could-let.html)

**Swati Khandelwal**Aug 07, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmTGemKyDLZPr_sBbt2AdOQMEBEcRFzic8_Ddtkx92vtPOfFdoiwxJ60b00usecTjHuIGUJuUIR2aB8MU2P7-GLc0NOuWsa3ctofrA2-wD38wgI4Fke3moSskWjiRJEXT8Yxl7Ye56NgGl9DZKr8zf974rHRsc1PtHie_iIPVyD18HMx49S02tGZ2EeDY/s1700-e365/linux-sctp.jpg)

A use-after-free bug in Linux's SCTP networking code can be turned into full root on a host, and Tencent researchers say they used it to escape a container and reach the machine underneath.

The flaw has existed since 2008. The fix already shipped: stable kernels 7.1.6, 6.18.42, 6.12.101 and 6.6.148, released August 3, close it. Anyone running an older kernel with SCTP reachable should update.

Tracked as **CVE-2026-64564** and named **SCTPhantom** by its finders, the flaw was disclosed publicly on August 6, two days after the kernel CVE team assigned it. No public exploit code had surfaced at the time of writing, and The Hacker News found no entry for the flaw in CISA's Known Exploited Vulnerabilities catalog as of August 7.

The flaw is local, not remote, and it needs SCTP reachable on the target, which limits exposure. Where those conditions held, Tencent Zhuque Lab reports it got root on the kernel builds it tested for Debian 13, Ubuntu 24.04, Rocky Linux 9 and RHEL 9, and OpenCloudOS.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

SCTP is a transport protocol that lets one connection run over several network paths at once. A companion feature, dynamic address reconfiguration, lets a peer add or drop those addresses mid-connection.

The bug is a mix-up over identity: the kernel checks a delete request against the packet's source address, but acts on a path it picked using a different address inside the message. [Per the kernel's own advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-64564), one message can carry an address, a delete for that same address, then a wildcard delete. That sequence frees the path, then reuses the dead pointer, leaving the connection pointing at memory the kernel has already released.

The patch refuses a delete aimed at the path the message is being processed against. The bug traces to Linux 2.6.25 in 2008 and has been in every kernel released since.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgr1n4W_206IL6KR8ZAkQSA9d1yKLCcylm2qX5k6Fgv595138hgpjhgWUo5IFiqs6KdPAvHtHsjul5jdVqhT5hc9QMa6je4UMGyeRK_S2TzYuhQ-yJ1drhUL8PUmvxvjPcE_LHYHXzAWMOmbADlwP5gCdfRNzszsWLMCp6fFYEkzvF2qSgf2LwjOmv5ni0/s1700-e365/linux.gif) |
| Source: [Fourier](https://x.com/Khanmlgb/status/2085332680636584174) on X. |

Tencent's container escape claim is based on its own testing. In [its write-up](https://matrix.tencent.com/en/2026/08/06/sctphantom-CVE-2026-64564), the lab says an early version of its exploit needed the net.sctp.addip\_enable and net.sctp.addip\_noauth\_enable sysctls switched on, which made CAP\_NET\_ADMIN look like a prerequisite. It later found a route that leaves both untouched by enabling the features per socket instead.

The lab says its escape test kept the default seccomp profile and granted neither CAP\_NET\_ADMIN nor CAP\_SYS\_ADMIN. By its count, six of eight attempts reached root on the host.

No one outside the lab has reproduced any of that, and the write-up does not name the container runtime it tested against. The lab itself notes that socket access, seccomp profiles, and user-namespace policy all shift exposure elsewhere. An [openKylin advisory](https://bbs.openkylin.top/t/topic/173441) covering the same bug goes no further than kernel panic and denial of service.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The severity number is unsettled too. Tencent scored it 8.5 under CVSS v4.0. NVD had assigned neither a score nor a weakness classification as of August 7.

Vendors often backport fixes without moving to a new upstream version, so a kernel version string alone will not tell you whether you are covered; check your distribution's tracker. [A second dangling-transport use-after-free in the same code](https://kernel.googlesource.com/pub/scm/linux/kernel/git/netdev/net-next/%2B/c9158ceaf27780ef64534ad72f44ffde3f8ccc49) was patched on August 6, after the August 3 stable releases shipped, so those kernels do not carry it. Where SCTP is not needed, blocking the module removes the attack surface outright.

Tencent credits the find to Corvus AI, a multi-agent research pipeline it built for kernel work, making SCTPhantom the latest in a run of long-dormant kernel flaws [surfaced with machine assistance this year](https://thehackernews.com/2026/07/researcher-says-ai-helped-develop-linux.html), alongside [GhostLock](https://thehackernews.com/2026/07/15-year-old-ghostlock-flaw-enables-root.html) in July. It also lands the same day as [Zapscape](https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html), an unrelated KVM escape, and the same four stable releases carry both fixes.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Container Security](https://thehackernews.com/search/label/Container%20Security), [Kernel Security](https://thehackernews.com/search/label/Kernel%20Security), [linux](https:/...