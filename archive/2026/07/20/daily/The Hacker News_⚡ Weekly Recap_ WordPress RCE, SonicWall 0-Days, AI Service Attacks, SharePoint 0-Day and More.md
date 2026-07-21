---
title: ⚡ Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More
url: https://thehackernews.com/2026/07/weekly-recap-wordpress-rce-sonicwall-0.html
source: The Hacker News
date: 2026-07-20
fetch_date: 2026-07-21T05:03:16.950862
---

# ⚡ Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [⚡ Weekly Recap: WordPress RCE, SonicWall 0-Days, AI Service Attacks, SharePoint 0-Day and More](https://thehackernews.com/2026/07/weekly-recap-wordpress-rce-sonicwall-0.html)

**Ravie Lakshmanan**Jul 20, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjA-JVLR3XITNdsuoWZQFMu12z6UeqsAdKWjS4Iu6piGP-4Natjx3GZ4obTdwddY5YHPgNoYDJljFCpAh9YRUntTakZeiGikoJYjjgEcv2ZVPchuCuyIfRh_3aTJ64Ktke9RkdRxH7DalTVqGf0YgF3fDj2lHgvVyIDANaMn1KVy1d1CBXTZxAwyJBqEClL/s1700-e365/cyberrecap.jpg)

A single request should not be able to do this much. But this week, small inputs led to code execution, memory loss, stolen keys, and disabled security tools.

The paths were often simple: exposed systems, weak checks, old drivers, fake prompts, and public code used for malware delivery. Some bugs were new. Others were already being used before defenders had time to patch.

Here is the full recap of what broke, what was exploited, and what needs attention now.

## **⚡ Threat of the Week**

**[New wp2shell WordPress Core Flaw Lets Unauthenticated Attackers Run Code](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html)** - Searchlight Cyber disclosed a pre-authenticated remote code execution vulnerability in WordPress Core that can be exploited anonymously on a standard WordPress installation, without requiring any plugins or other special conditions. It is a combination of [CVE-2026-63030](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-ff9f-jf42-662q) (REST API batch-route confusion) and [CVE-2026-60137](https://github.com/WordPress/wordpress-develop/security/advisories/GHSA-fpp7-x2x2-2mjf) (SQL injection in WordPress core) that can be chained to turn an anonymous request into code execution. watchTowr said it's already seeing proof-of-concept (PoC) exploits in circulation and that it's beginning to see the first signs of in-the-wild exploitation. "This is going to hurt," watchTowr CEO Benjamin Harris said. "WordPress runs on hundreds of millions of websites globally. Some of those will be auto-patched by their hosting providers, but plenty will not, and that is where the damage will be done. Our advice is simple: patch as fast as you possibly can, and do not stop there. Put the controls and investigations in place to determine whether an attacker got there first and to detect and remove any backdoors that may already have been dropped before you patched." The cybersecurity company said it's the latest example of vulnerabilities being surfaced by AI-assisted tooling and how the technology is being abused by attackers to weaponize them.

[![Vulnerability Management](data:image/png;base64... "Vulnerability Management")

## AI Broke Vulnerability Management. Here Is the CISO Case

The AI security job market is no longer theoretical. SANS tracked hiring across 10 specific roles and mapped verified job data, salary ranges, and the skills required to get there. The three-tier framework gives your team a clear view of which roles to prioritize now and which to develop toward.](https://thehackernews.uk/vuln-ai-fix)
[Download Now ➝](https://thehackernews.uk/vuln-ai-fix)

## **🔔 Top News**

* **[SonicWall SMA Zero-Days Exploited as 0-Days](https://thehackernews.com/2026/07/sonicwall-sma-zero-days-exploited.html)** - A previously undocumented threat actor codenamed UTA0533 has been attributed to the exploitation of recently disclosed SonicWall Secure Mobile Access (SMA) 1000 series VPN appliances as zero-days prior to their public disclosure since June 22, 2026. The discovery was made following an incident response investigation initiated earlier this month. The impacted organization has not been identified. "This threat actor was observed using multiple zero-day exploits, malware designed specifically for SonicWall SMA VPN appliances, as well as other attacker tradecraft," Volexity said. The vulnerabilities in question are CVE-2026-15409 (CVSS score: 10.0) and CVE-2026-15410 (CVSS score: 7.2), both of which could be chained to facilitate arbitrary command execution and take over susceptible devices. Patches for both vulnerabilities were released by SonicWall last week.
* **[DoS Flaw in OpenSSL](https://thehackernews.com/2026/07/openssl-hollowbyte-flaw-could-freeze.html)** - The Okta Red Team disclosed details of HollowByte, a denial-of-service (DoS) flaw in OpenSSL. "By sending a malicious payload of just 11 bytes, a remote, unauthenticated attacker can force a server to allocate disproportionate chunks of memory before any security handshake even begins," Okta said. Put differently, an unauthenticated attacker -- through 11 bytes of carefully crafted data -- can convince OpenSSL to reserve up to 128 KB of heap memory for a handshake message that never actually arrives, causing a server to exhaust available RAM and trigger a DoS condition. The OpenSSL team resolved the issue in versions 4.0.1, 3.6.3, 3.5.7, 3.4.6, and 3.0.21. "Instead of trusting the header outright, OpenSSL now grows the buffer only as bytes actually land on the wire. A claim with no follow-through now costs the server nothing," Okta said.
* **[CISA Adds New SharePoint RCE Zero-Day to KEV Catalog](https://thehackernews.com/2026/07/cisa-adds-exploited-sharepoint-rce-zero.html)** - The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added a newly patched security flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the fixes by July 19, 2026. The vulnerability, CVE-2026-58644 (CVSS score: 9.8), is a critical deserialization of untrusted data vulnerability that allows an unauthorized attacker to execute arbitrary code. Patches for the flaw have been released as part of the Patch Tuesday updates released on July 14, 2026. Microsoft revised its bulletin to clarify that CVE-2026-58644 has been exploited in the wild, meaning the shortcomi...