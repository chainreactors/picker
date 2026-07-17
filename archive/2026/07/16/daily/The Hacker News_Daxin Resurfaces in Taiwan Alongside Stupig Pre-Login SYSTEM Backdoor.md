---
title: Daxin Resurfaces in Taiwan Alongside Stupig Pre-Login SYSTEM Backdoor
url: https://thehackernews.com/2026/07/daxin-resurfaces-in-taiwan-alongside.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:24.526440
---

# Daxin Resurfaces in Taiwan Alongside Stupig Pre-Login SYSTEM Backdoor

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

# [Daxin Resurfaces in Taiwan Alongside Stupig Pre-Login SYSTEM Backdoor](https://thehackernews.com/2026/07/daxin-resurfaces-in-taiwan-alongside.html)

**Ravie Lakshmanan**Jul 16, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoN2-EflBc7bABKWw8GsIF_E9I7A9Ond88d-yFCAc6t850C9RGNxpGFAP3G9NichaP7JHa_BA-4bsMDNze5837hGCFGuAbyEHPVsxmQgMNS9A8e1jFL19Z1MVv9KOq0TX5ShDG46Xrv3MxH-vR3sQtEcDkH5OMxQQo11NXMKWRicC8T1OwTqw3ENoXEdIK/s1700-e365/WINDOWS-malware.jpg)

An advanced malware previously attributed to a China-linked threat actor has resurfaced after more than four years within a Taiwan manufacturing firm, along with a previously unreported backdoor dubbed **Stupig**.

**Daxin** ("srt64.sys"), as the kernel-mode rootkit is referred to, was [first documented](https://thehackernews.com/2022/03/china-linked-daxin-malware-targeted.html) by Broadcom-owned Symantec in March 2022, with evidence indicating its use in targeted attacks aimed at governments and other critical infrastructure targets since 2013.

The latest findings from the Symantec and Carbon Black Threat Hunter Team show that Daxin is still operational, after it was found running on a compromised host in Taiwan in 2026. The same machine, belonging to a Taiwan-based subsidiary of a multinational high-tech manufacturer, is also said to have been infected with Stupig ("a.dll" or "kbdus1.dll"). The file name is an attempt to masquerade as "kbdus.dll," a legitimate Microsoft DLL associated with the U.S. English keyboard layout.

"Stupig uses a technique not documented in any known malware family," the cybersecurity arm of Broadcom [said](https://www.security.com/threat-intelligence/daxin-returns-stupig). "A trojanized keyboard-layout DLL loaded by 'winlogon.exe' lets an attacker run commands as System directly from the Windows logon screen, before anyone signs in and without raising a logon audit event."

What makes the intrusion stand out is that both the artifacts carry a compilation timestamp from early 2013, although the compromised machine did not begin reporting telemetry until May 12, 2026. Given the threat actor's ability to stay undetected for extended periods of time, it's suspected that the attack may have gone unnoticed for 13 years.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

No code-level overlaps have been identified between Daxin and Stupig, although their co-deployment on the same host, coupled with complementary functions, similarities in development practices, and the 2013 compile timestamps, suggest that they may have been the work of the same threat actor.

Daxin has an unusual approach to command-and-control. Rather than directly establishing outbound connections with attacker-controlled infrastructure, the Windows kernel-mode driver backdoor monitors incoming TCP traffic for specific patterns and hijacks existing legitimate connections for encrypted C2 communications so as to blend in with regular activity. It's equipped to interact with machines that are physically disconnected from the internet.

"This made Daxin exceptionally difficult to identify with conventional network monitoring," Broadcom noted. "The malware also supported multi-hop communications through chains of infected hosts, allowing operators to reach systems on isolated network segments."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgg1dKmQy6UuEcQ0BORFJl9nj4rExlkohJXsIKaaUfz630E0zZe2db_Tpt1fviWHucZQ2j-Vgn36djlLpX31M6gCAGqmBgocofCgsF-mmKPpIqo3UWM5yDFU6eQ1CLsmIz1fo9LuT6iqLTMQ4suQfBwvqtoyeCkE4ePnnCu7hldacXi8KjA1vv-oeQR_ddV/s1700-e365/daxin-dark.jpg)

Exactly how and when the host was compromised remains unknown, but it's suspected to be an outdated version of the [Digiwin single sign-on (SSO) portal](https://www.digiwin.com.tw/software/715.html) that was using end-of-life Java Development Kit (JDK) 1.5 and 1.6 installations going back to 2009 to 2011.

"Stupig is a DLL backdoor that achieves persistence by registering as a keyboard-layout provider, causing win32k.sys to load it into winlogon.exe at system startup," the threat hunter team explained. "The DLL returns a valid KBDTABLES pointer so the keyboard layout functions normally, giving nothing away to any process or administrator inspecting the loaded module."

Once it starts running inside "winlogon.exe," it keeps an eye out for usernames beginning with the string "stupig" in the Windows logon screen. When the username is entered, any string that follows the prefix is interpreted as a command and executed with SYSTEM privileges. If no command is entered after the prefix, it spawns a command prompt session as SYSTEM on the logon screen.

The discovery of Daxin in 2026 shows that the cyber espionage operation never completely stopped. Rather, it went quiet, maintaining stealthy persistence in targeted networks.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

"By hiding inside the Windows logon process and registering as a keyboard-layout provider, Stupig gives operators SYSTEM-level command execution and credential theft before a user signs in, an access method most defenders are not aware of nor watching for," Symantec and Carbon Black said. "Whether the same operators deployed both tools cannot be confirmed, but their functions are complementary."

The disclosure comes as Hunt.io said it observed a suspected China-linked threat actor using Anthropic Claude Code and DeepSeek models to automate intrusions against government and financial systems in Afghanistan, Thailand, Taiwan, and the U.S. The discovery is based on an open directory ("112.213.124[.]132") that...