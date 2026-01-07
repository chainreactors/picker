---
title: Fake Booking Emails Redirect Hotel Staff to Fake BSoD Pages Delivering DCRat
url: https://thehackernews.com/2026/01/fake-booking-emails-redirect-hotel.html
source: The Hacker News
date: 2026-01-06
fetch_date: 2026-01-07T03:30:45.320698
---

# Fake Booking Emails Redirect Hotel Staff to Fake BSoD Pages Delivering DCRat

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Fake Booking Emails Redirect Hotel Staff to Fake BSoD Pages Delivering DCRat](https://thehackernews.com/2026/01/fake-booking-emails-redirect-hotel.html)

**Jan 06, 2026**Ravie LakshmananMalware / Endpoint Security

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlFgZ371OJLB7x0fK_3a34h710DpAHQLeyLQyaBpp1jhfsFyRD0-tmkLhXAvv0VD1XnU_WK8g5O16VUob1aHIyQf2smhkn6llIaC_H5_6MwogFRD11Hfp-w2kPc9vgiBUTlnftXM7VuCMsFmBPwxtyvAokqOJbgSAndESDU3qZV6-R9SH6meqbyuyoFk8n/s790-rw-e365/windows.jpg) |
| Source: Securonix |

Cybersecurity researchers have disclosed details of a new campaign dubbed **PHALT#BLYX** that has leveraged [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)-style lures to display fixes for fake blue screen of death ([BSoD](https://en.wikipedia.org/wiki/Blue_screen_of_death)) errors in attacks targeting the European hospitality sector.

The end goal of the multi-stage campaign is to deliver a remote access trojan known as [DCRat](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html), according to cybersecurity company Securonix. The activity was detected in late December 2025.

"For initial access, the threat actors utilize a fake Booking.com reservation cancellation lure to trick victims into executing malicious PowerShell commands, which silently fetch and execute remote code," researchers Shikha Sangwan, Akshay Gaikwad, and Aaron Beardslee [said](https://www.securonix.com/blog/analyzing-phaltblyx-how-fake-bsods-and-trusted-build-tools-are-used-to-construct-a-malware-infection/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The starting point of the attack chain is a phishing email impersonating Booking.com that contains a link to a fake website (e.g., "low-house[.]com"). The messages warn recipients of unexpected reservation cancellations, urging them to click the link to confirm the cancellation.

The website to which the victim is redirected masquerades as Booking.com, and serves a fake CAPTCHA page that leads them to a bogus BSoD page with "recovery instructions" to open the Windows Run dialog, paste a command, and press the Enter key. In reality, this results in the execution of a PowerShell command that ultimately deploys DCRat.

Specifically, this entails a multi-step process that commences with the PowerShell dropper downloading an MSBuild project file ("v.proj") from "2fa-bns[.]com", which is then executed using "MSBuild.exe" to run an embedded payload responsible for configuring Microsoft Defender Antivirus exclusions to evade detection, setting up persistence on the host in the Startup folder, and launching the RAT malware after downloads it from the same location as the MSBuild project.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaiCRJxbmwsaaHbvZIve5KXKNMhbTLKMUy7b0jGdJRKGcXUK7-DlQ8ynmE3AyXv5SCETiUDm564-rPYcwxITGEkkEzU8Z2fZMB0N2B4gL51q7TBjoJzhCtDSPRyGJTbchKqb3fln-kEGAARNBEnLaq6k9nKv0k9tokx4p2bKxZCTF7jowQbSwnrJ2DU5hY/s790-rw-e365/booking.jpg)

It's also capable of disabling the security program altogether if found to be running with administrator privileges. If it doesn't have elevated rights, the malware enters a loop that triggers a Windows User Account Control (UAC) prompt every two seconds for three times in hopes that the victim will grant it the necessary permissions out of sheer frustration.

In tandem, the PowerShell code takes steps to open the legitimate Booking.com admin page in the default browser as a distraction mechanism and to give an impression to the victim that the action was legitimate.

[DCRat](https://thehackernews.com/2025/03/cert-ua-warns-dark-crystal-rat-targets.html), also called Dark Crystal RAT, is an off-the-shell .NET trojan that can harvest sensitive information and expand its functionality by means of a plugin-based architecture. It's equipped to connect to an external server, profile the infected system, and await incoming commands from the server, enabling the attackers to log keystrokes, run arbitrary commands, and deliver additional payloads like a cryptocurrency miner.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

The campaign is an example of how threat actors are leveraging living-off-the-land (LotL) techniques, such as abusing trusted system binaries like "MSBuild.exe," to move the attack to the next stage, establish a deeper foothold, and maintain persistence within compromised hosts.

"The phishing emails notably feature room charge details in Euros, suggesting the campaign is actively targeting European organizations," Securonix said. "The use of the Russian language within the 'v.proj' MSBuild file links this activity to Russian threat factors using DCRat."

"The use of a customized MSBuild project file to proxy execution, coupled with aggressive tampering of Windows Defender exclusions, demonstrates a deep understanding of modern endpoint protection mechanisms."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[endpoint security](https://thehackernews...