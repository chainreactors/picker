---
title: Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root
url: https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:12.176369
---

# Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Debian and Ubuntu APT Flaw Lets MitM Attackers Swap Verified Packages and Run Code as Root](https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html)

**Swati Khandelwal**Nov 04, 2026Linux / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUPaNgRQEg3TU6-9BBgKse77CGVpbBFbn48cBnN1aanKvaMzk_mT74RxyWZA3_NbcrYe0UnRAQlELRYKGiGNrLUDcBMSKXFgRNxaND7RoaVFOs1Q7rkFFtlpoAzYQ7C8i6RAY4bNNTarEMUI-iFR4A_IfjIkFE9vpyQjG-0QFngy5cRE8f2GhGfTltkaI/s1700-nu-rw-lo-l85-e365/linux-apt.jpg)

A flaw in **APT**, the package manager for Debian and Ubuntu, allows an attacker who can modify package downloads to swap a checked package for their own.

The attacker's code then runs as root, according to advisories that [Debian](https://lists.debian.org/debian-security-announce/2026/msg00526.html), [Ubuntu](https://ubuntu.com/security/CVE-2026-109518), and [APT's developers](https://lists.debian.org/deity/2026/11/msg00005.html) published on November 4. The attack needs APT to retry failed downloads, which it does by default from Debian 12 and Ubuntu 22.04 onward.

Debian has released fixed versions of APT for the flaw, **CVE-2026-109518**. APT's developers, who call the flaw critical, say updates for Ubuntu and its Ubuntu Pro subscription service are being released. Ubuntu 14.04 users with Ubuntu Pro can already get one.

Older releases, such as Debian 11 and Ubuntu 20.04, are not exposed by default, according to Ubuntu. But many user scripts may have turned on the retry setting, Acquire::Retries, on those releases anyway, APT's developers say.

Debian's testing branch was still on the [vulnerable version 3.3.5](https://security-tracker.debian.org/tracker/CVE-2026-109518) at 14:58 UTC on November 4. For Debian 11, whose [Debian long-term support ended on August 31](https://www.debian.org/releases/bullseye/), APT's developers have published a fixed version, 2.2.5.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Ubuntu rates the flaw as high priority, with a CVSS 4.0 score of 7.7, and says that distributions built on Debian and Ubuntu are affected as well, without naming any.

Ubuntu published new APT builds for four of its releases to its [security archive](https://launchpad.net/ubuntu/%2Bsource/apt) at 14:25 UTC on November 4:

* Ubuntu 26.10: 3.3.3ubuntu0.1
* Ubuntu 26.04 LTS: 3.2.1ubuntu0.1
* Ubuntu 24.04 LTS: 2.8.4ubuntu0.1
* Ubuntu 22.04 LTS: 2.4.15ubuntu0.1

At 15:46 UTC, Ubuntu still marked all eight releases it tracks for the flaw, from 14.04 LTS to 26.10, as vulnerable.

The attacker can be anyone who can change the HTTP traffic between APT and the package server, including a malicious mirror or proxy, according to Ubuntu. The attack runs when the computer installs a package. The attacker uses HTTP redirects and ordinary temporary server errors to make APT retry the download, APT's developers say.

Max Justicz reported the flaw. None of the three advisory reports describe attacks exploiting the flaw or offer a workaround for systems that cannot update yet. They describe the attack over HTTP and do not say whether package sources reached over HTTPS are exposed.

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

[linux](https://thehackernews.com/search/label/linux), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide](https://thehackernews.com/2026/10/chinese-hackers-use-ai-powered-artex-to.html)

[![The Hacker News](data:image/svg+xml;base64...)

TeamViewer Flaw Lets Remote Computers Attack Users Who Connect to Control Them](https://thehackernews.com/2026/10/teamviewer-flaw-lets-remote-computers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Official Claude Code Extension on Cursor Marketplace Trojanized with Persistent SSH Backdoor](https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html)

[![The Hacker News](data:image/svg+xml;base64...)

Binance Suffers Security Breach Affecting $6.3 Billion in Assets, Nearly $3 Billion Frozen](https://thehackernews.com/2026/10/binance-suffers-security-breach.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Critical Firewall Flaws, Banking Trojans Rented, Weaponized PDF, Token Theft + 26 More Stories](https://thehackernews.com/2026/10/threatsday-critical-firewall-flaws.html)

[![The Hacker News](data:image/svg+xml;base64...)

Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions](https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html)

[![The Hacker News](data:image/svg+xml;base64...)

Cisco Patches Actively Exploited ASA and F...