---
title: Progress Kemp LoadMaster Flaw Could Let Attackers Run Root Commands Pre-Auth
url: https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:41.406634
---

# Progress Kemp LoadMaster Flaw Could Let Attackers Run Root Commands Pre-Auth

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Progress Kemp LoadMaster Flaw Could Let Attackers Run Root Commands Pre-Auth](https://thehackernews.com/2026/06/progress-kemp-loadmaster-flaw-could-let.html)

**Swati Khandelwal**Jun 30, 2026Vulnerability / API Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtFZGtJwnGA8dQHmNpd8Pzgx4p0wSq_e2hyphenhyphen2bZwWBQEDK8QPAi2CEOR_Nbns5jhRw9mMSPv6RBe2IqRO1c9fIMvMlUAV14B3VQE7-csMvfMQK6Qr3THGlxQY3C9HiYW_TYHGzok-TWFmMoMkto0OA8fNsQuvADEaJNFQYdIrXXzHGJEhyqpKRC2IFCaRM6/s1700-e365/loadmaster.jpg)

A critical vulnerability in Progress Kemp LoadMaster can let an unauthenticated attacker execute arbitrary commands as root on the appliance by sending a crafted request to its API.

The flaw, tracked as **CVE-2026-8037**, carries a CVSS score of [9.8 according to ZDI](https://www.zerodayinitiative.com/advisories/ZDI-26-342/). A patch is available. If you run LoadMaster with the API enabled, update now.

Progress [published its advisory on June 4](https://community.progress.com/s/article/LoadMaster-Critical-Security-Bulletin-June-2026-CVE-2026-8037-CVE-2026-33691) and says it has not received any reports of exploitation. On June 29, researchers at watchTowr Labs published a [detailed](https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/) technical write-up that walks through the full exploit chain.

## What the Flaw Does

LoadMaster is an application delivery controller and load balancer used by enterprises to manage traffic across servers. It sits at the network edge, which makes any pre-auth flaw in it especially dangerous.

The vulnerability lives in a function called **escape\_quotes()**, which is supposed to sanitize user input before it gets passed into a shell command. The function's job is to escape single quotes so that an attacker cannot break out of a quoted string and inject commands. The problem: it allocated a memory buffer without clearing it first and never wrote a null terminator at the end of the sanitized string.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

That missing terminator is the whole exploit. Without it, the system keeps reading past the end of the sanitized input into whatever data happens to sit next to it in memory. An attacker can control what sits there by stuffing extra JSON keys into the same API request, each carrying a command injection payload. The system reads the sanitized input, keeps going, hits the attacker's payload, and executes it.

The attack targets the **/accessv2**endpoint, which handles API credential validation. The attacker sends a JSON body with a specially crafted apiuser value and dozens of extra key-value pairs sprayed with the command they want to run. No valid credentials are needed. The command runs as root.

## Affected Versions and Fix

The flaw affects LoadMaster GA v7.2.63.1 and older, and LTSF v7.2.54.17 and older, when the API is enabled. Progress has released fixed versions: GA v7.2.63.2 and LTSF v7.2.54.18.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiR4ufDYRjg4d9LjrvECvtH9o43nseVfdQRIGpWF1jWin05z8wuyMWvo69GR650R6TPcOFhSsYbWexR-tWSTcRY1kVv8F0I_Mnr6zicjHEDjgAinA-c5ZfUZUgUP3u_cFgffUetsiSgTM8CVc6K0lnN_FGS5FtjA5IXeszrSxKW5au7QOr5iZAktRTWSJdB/s1700-e365/poc.png)

The patch itself is minimal. Two changes: the memory allocation function was swapped from one that leaves the buffer uninitialized to one that zero-fills it, and an explicit null terminator was added after the escaped output. Two lines of code that close a path to the root.

The vulnerability was discovered by Syed Ibrahim Ahmed of TrendAI Research and reported to Progress through the Zero Day Initiative on April 15, 2026. ZDI coordinated the public advisory release on June 9. watchTowr Labs independently analyzed the patch diff and published their own full technical breakdown with a working proof of concept on June 29.

Progress also patched a second, high-severity flaw in the same advisory: CVE-2026-33691, a WAF bypass where whitespace padding in filenames could circumvent file upload extension checks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

## A Pattern Worth Watching

This is not LoadMaster's first critical flaw. In November 2024, CISA [added a previous LoadMaster command injection flaw](https://thehackernews.com/2024/11/cisa-alert-active-exploitation-of.html) (CVE-2024-1212, CVSS 10.0) to its Known Exploited Vulnerabilities catalog after confirmed exploitation in the wild.

In April 2026, Progress patched five more high-severity LoadMaster flaws, four of them command injection issues. Progress is also the maker of MOVEit, whose 2023 vulnerabilities fueled a mass exploitation campaign by the Cl0p ransomware group.

The [Canadian Centre for Cyber Security](https://www.cyber.gc.ca/en/alerts-advisories/progress-security-advisory-av26-552) has also issued an advisory urging administrators to apply the updates.

No attacks on CVE-2026-8037 have been reported yet. A working proof of concept is now public. Patch, and then ask whether the API needs to be reachable at all.

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
[![Facebook Messenger](data:image/png;base64...)Share ...