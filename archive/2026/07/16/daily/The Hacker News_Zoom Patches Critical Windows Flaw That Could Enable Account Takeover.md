---
title: Zoom Patches Critical Windows Flaw That Could Enable Account Takeover
url: https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:25.162875
---

# Zoom Patches Critical Windows Flaw That Could Enable Account Takeover

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

# [Zoom Patches Critical Windows Flaw That Could Enable Account Takeover](https://thehackernews.com/2026/07/zoom-patches-critical-windows-flaw-that.html)

**Ravie Lakshmanan**Jul 16, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPR-qLKvfH8KZydz4_DnqiB9bJDjgFi6KdfrbbCHNkywiDcR_1SILe12UqjuyM_1yQXEDBok-ZeYRX0hEjIZpx-Dz2hnIW2xXnwAqrmA3voWWfG_vnGMavgE4-E_DFzICLfizByiwAis02VEJqSoxQrEECCMibS0X27D5k0o08IPp1JR0tVCnXwpj2u3e2/s1700-e365/zoom.jpg)

Zoom has released security updates for a critical security flaw impacting Zoom Workplace for Windows that could facilitate account takeover.

The vulnerability, tracked as **CVE-2026-53412** (CVSS score: 9.8), affects Zoom Desktop Client for Windows, Zoom VDI Client for Windows, and Zoom Meeting SDK for Windows.

"Improper Input Validation in Zoom Desktop Client for Windows, Zoom VDI Client for Windows, and Zoom Meeting SDK for Windows may allow an unauthenticated user to conduct an account takeover via network access," Zoom [said](https://www.zoom.com/en/trust/security-bulletin/zsb-26014/) in an advisory released this week.

The latest security fixes also address three high-severity flaws -

* **[CVE-2026-53411](https://www.zoom.com/en/trust/security-bulletin/zsb-26013/)** (CVSS score: 7.8) - An improper input validation vulnerability in the Zoom Workplace VDI Plugin for Windows before version 6.6.14 that may allow an authenticated user to conduct an escalation of privilege via local access.
* **[CVE-2026-53410](https://www.zoom.com/en/trust/security-bulletin/zsb-26012/)** (CVSS score: 7.0) - A time-of-check to time-of-use (TOCTOU) race condition vulnerability in the installation and uninstallation process of certain Zoom Clients for Windows that could allow an authenticated local user to escalate privileges.
* **[CVE-2026-53409](https://www.zoom.com/en/trust/security-bulletin/zsb-26011/)** (CVSS score: 7.8) - An improper privilege management vulnerability in Zoom Rooms for Windows before version 7.1.0 that may allow an authenticated user to conduct an escalation of privilege via local access.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHcvlLVmAqlffm6kG54_0cGVf8WfcgzqT9B0fBSizSSeIjh8tBepXnrf6BMqKiG344WgqNejcRtEFKT1PmOzQNQBhdmu2iz9Po10z0SSDlFuZ37iip2uYibJDoxTEkbUI7Bx8NJM2Io_z_nl5p4YA-ZhqFLfi0GW1axyu-lQx-iytCn9RGSJ2iqCwdyv8m/s1600/sy-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

It's worth noting that CVE-2026-53410 affects the following products -

* Zoom Workplace for Windows before version 7.0.5
* Zoom Workplace VDI Client for Windows before 6.5.17 and 6.6.14 in their respective branch
* Zoom Workplace VDI plugin for Windows before 6.5.17 and 6.6.14 in their respective branch
* Zoom Rooms for Windows before 7.0.5
* Remote Control for Zoom Contact Center for Windows before version 7.0.0

As of writing, there are no indications that any of the flaws are being exploited in real-world attacks. Users can stay protected by applying the latest updates.

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

[account takeover](https://thehackernews.com/search/label/account%20takeover), [Application Security](https://thehackernews.com/search/label/Application%20Security), [endpoint security](https://thehackernews.com/search/label/endpoint%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows](https://thehackernews.com/search/label/Windows)

⚡ Top Stories This Week

[![16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](data:image/svg+xml;base64... "16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems")

16-Year-Old Linux KVM Flaw Lets Guest VMs Escape to Host on Intel and AMD x86 Systems](https://thehackernews.com/2026/07/16-year-old-linux-kvm-flaw-lets-guest.html)

[![BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA](data:image/svg+xml;base64... "BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA")

BeyondTrust Patches Critical Auth Bypass Flaws in Remote Support and PRA](https://thehackernews.com/2026/07/beyondtrust-patches-critical-auth.html)

[![Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker](data:image/svg+xml;base64... "Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker")

Court Filing Reveals Windows Device ID Helped FBI Trace Alleged Scattered Spider Hacker](https://thehackernews.com/2026/07/court-filing-reveals-windows-device-id.html)

[![Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots](data:image/svg+xml;base64... "Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots")

Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots](https://thehackernews.com/2026/07/rogue-agent-flaw-could-...