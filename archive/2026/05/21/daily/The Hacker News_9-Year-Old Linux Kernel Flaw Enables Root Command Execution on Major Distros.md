---
title: 9-Year-Old Linux Kernel Flaw Enables Root Command Execution on Major Distros
url: https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html
source: The Hacker News
date: 2026-05-21
fetch_date: 2026-05-22T06:08:40.284085
---

# 9-Year-Old Linux Kernel Flaw Enables Root Command Execution on Major Distros

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [9-Year-Old Linux Kernel Flaw Enables Root Command Execution on Major Distros](https://thehackernews.com/2026/05/9-year-old-linux-kernel-flaw-enables.html)

**Ravie Lakshmanan**May 21, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCjgJwva2lZrAwxHWPZFiphHAhxBdWRyU4gUiAZIStkUP4JU6yej3Z1xVhUtrhaIYVu4IL5KpvOomBDHU_aLtvgHV-R9_41nUSrngG0BGBlCv2pByfkVZNKxmwA3Nf6NR7pi6XgwdUjkwFw27lm_vNR_w2Cr1An46yOM8kfIEphrSCq2aRcaKNNj9D-PiN/s1700-e365/linux-exploit.gif)

Cybersecurity researchers have disclosed details of a vulnerability in the Linux kernel that remained undetected for nine years.

The vulnerability, tracked as [CVE-2026-46333](https://thehackernews.com/2026/05/dirtydecrypt-poc-released-for-linux.html) (CVSS score: 5.5), is a case of improper privilege management that could permit an unprivileged local user to disclose sensitive files and execute arbitrary commands as root on default installations of several major distributions like Debian, Fedora, and Ubuntu. It's also codenamed ssh-keysign-pwn.

According to Qualys, which discovered the flaw, the problem is rooted in the kernel's \_\_ptrace\_may\_access() function and was introduced in November 2016.

"The primitive is reliable and turns any local shell into a path to root or to sensitive credential material," Saeed Abbasi, senior manager of Threat Research Unit at Qualys, [said](https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

Successful exploitation of the flaw could permit a local attacker to disclose /etc/shadow and host private keys under /etc/ssh/\*\_key, as well as execute arbitrary commands as root through four different exploits targeting chage, ssh-keysign, pkexec, and accounts-daemon.

The disclosure comes as a proof-of-concept (PoC) exploit for the vulnerability was [released](https://github.com/0xdeadbeefnetwork/ssh-keysign-pwn/) last week, shortly after a public kernel commit emerged. CVE-2026-46333 is the latest security vulnerability disclosed in the Linux kernel after Copy Fail, [Dirty Frag](https://kb.cert.org/vuls/id/980487), and Fragnesia over the past month.

It's recommended to apply the latest kernel update released by Linux distributions. If the updates cannot be carried out immediately, temporary workarounds include raising "kernel.yama.ptrace\_scope" to 2.

"On hosts that have allowed untrusted local users during the exposure window, treat SSH host keys and locally cached credentials as potentially disclosed," Qualys said. "Rotate host keys and review any administrative material that lived in the memory of set-uid processes."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyABc30y-6FJS8pbsf2yHI1xiyGUCdTf449yj2qfWl3E27s1stzGg2L03d3pwIxexQOglShR4p9jmvpatdbA5HruPGPpb4llfRmmbJPAN_-hXf4mefY5sw2BqYTzKrh6tMIefl8wgPLaAwSyPc9eKVQvbpfsA0EqBiY4BzoYLn-KC0zSA-EH4OEUrHncwL/s1700-e365/pin.jpg)

The development follows the release of a PoC for a local privilege escalation flaw called **PinTheft** that allows local attackers to gain root privileges on Arch Linux systems. The exploit requires the Reliable Datagram Sockets (RDS) module to be loaded on the target system, io\_ring to be enabled, a readable SUID-root binary, and x86\_64 support for the included payload.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"PinTheft is a Linux local privilege escalation exploit for an RDS zerocopy double-free that can be turned into a page-cache overwrite through io\_uring fixed buffers," Zellic and the V12 security team [said](https://github.com/v12-security/pocs/tree/09e835b587bf71249775654061ae4c79e92cf430/pintheft).

"The bug lived in the RDS zerocopy send path. rds\_message\_zcopy\_from\_user() pins user pages one at a time. If a later page faults, the error path drops the pages it already pinned, and later RDS message cleanup drops them again because the scatterlist entries and entry count remain live after the zcopy notifier is cleared. Each failed zerocopy send can steal one reference from the first page."

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

[Debian](https://thehackernews.com/search/label/Debian), [fedora](https://thehackernews.com/search/label/fedora), [Kernel](https://thehackernews.com/search/label/Kernel), [linux](https://thehackernews.com/search/label/linux), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Qualys](https://thehackernews.com/search/label/Qualys), [Ubuntu](https://thehackernews.com/search/label/Ubuntu), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](data:image/svg+xml;base64... "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak")

Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vu...