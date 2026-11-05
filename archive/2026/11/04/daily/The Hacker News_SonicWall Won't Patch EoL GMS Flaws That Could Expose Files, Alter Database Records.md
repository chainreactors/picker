---
title: SonicWall Won't Patch EoL GMS Flaws That Could Expose Files, Alter Database Records
url: https://thehackernews.com/2026/11/sonicwall-wont-patch-eol-gms-flaws-that.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:12.354099
---

# SonicWall Won't Patch EoL GMS Flaws That Could Expose Files, Alter Database Records

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

# [SonicWall Won't Patch EoL GMS Flaws That Could Expose Files, Alter Database Records](https://thehackernews.com/2026/11/sonicwall-wont-patch-eol-gms-flaws-that.html)

**Ravie Lakshmanan**Nov 04, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgME1T4MkjI8UEzzSmlLgbPG6a__VNQNoKkhuxiaW5zF5fnHLPmsTdkGoIL06JTeER1jcOMH-WLuNYyva_sSW_8DnZojbMC8ikgNME3ZPUAdkij-9nVm8joHHdaZRoLNbVgcSVLNSc6Tt7UJ3YPhQmea3OtQwg-H2UzUPIgWq7nFwoEQcMsGCKf-0fImEvd/s1700-nu-rw-lo-l85-e365/sonic.jpg)

SonicWall has [warned](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0019) of two vulnerabilities impacting end-of-life Global Management System (GMS) systems that it said will not be patched.

Details of the security flaws, which affect SonicWall GMS 9.5.2 and earlier versions, are below -

* **CVE-2026-109593** (CVSS score: 9.1) - An unauthenticated file read vulnerability that could allow an attacker with network access to read internal GMS files, potentially exposing sensitive information.
* **CVE-2026-109594** (CVSS score: 6.8) - A post-authentication SQL injection vulnerability that could allow an authenticated attacker to access or modify information stored in the GMS database under specific conditions.

"The affected product has reached End-of-life (EoL)," SonicWall said in a Tuesday alert.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

"As a result, no remediation or security update will be released for these vulnerabilities. Organizations using the product should be aware of the associated security risks and are strongly encouraged to upgrade to the SonicWall Network Security Manager (NSM)."

The development comes less than a month after SonicWall [shipped fixes](https://thehackernews.com/2026/10/sonicwall-patches-cvss-100-pre.html) for CVE-2026-102255 (CVSS score: 10.0), a critical pre-authenticated server-side request forgery (SSRF) flaw that could have allowed an attacker to reach internal functionality and perform unauthorized operations.

The vulnerability has since come under [active exploitation in the wild](https://thehackernews.com/2026/10/critical-sonicwall-sma-1000-flaw.html), with telemetry data from Previdian recording [2,541 attack attempts](https://previdian.com/CVE-2026-102255#telemetry) from eight unique IP addresses from Singapore and the U.S. since October 9, 2026. As many as 30 exploitation attempts were registered on November 3, 2026.

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

[enterprise security](https://thehackernews.com/search/label/enterprise%20security), [network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

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

Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls](https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html)

[![The Hacker News](data:image/svg+xml;base64...)

China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility](https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html)

[![The Hacker News](data:image/svg+xml;base64...)

Attackers Exploit PHP2Shell Flaws in Internet-Exposed Palo Alto Networks Management Interfaces](https://thehackernews.com/2026/10/attackers-exploit-php2shell-flaws-in.html)

[![The Hacker News](data:image/svg+xml;base64...)

PHP2Shell Attack Roots 25 Servers, Breaches U.S. Government-Affiliated Network](https://thehackernews.com/2026/10/php2shell-attack-roots...