---
title: Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices
url: https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html
source: The Hacker News
date: 2026-07-02
fetch_date: 2026-07-03T05:48:49.095900
---

# Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices

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

# [Google Disrupts NetNut Residential Proxy Network Spanning 2 Million Home Devices](https://thehackernews.com/2026/07/google-disrupts-netnut-residential.html)

**Swati Khandelwal**Jul 02, 2026Cybercrime / Botnet

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAH6tBAe18U0FqA-i5kNNNQYeXjY_LBflzBqVD5rq81OAC6q9c8UsDBsQb5K2F7IAfof5_JZCBpS51DNp63jsXfk4qqwLkckDh4nq-z-Gj0zoRwQu5IZYiNHiBlpp3C-6OR84JeDfPmIr4VLTp2NN6uHRYl0qT273wrbpcnUmd5SbIJH07cPHQxMo6VgI/s1700-e365/proxy.jpg)

Google has significantly degraded **NetNut**, one of the biggest networks that turns home devices into [rented relays](https://thehackernews.com/2024/05/us-dismantles-worlds-largest-911-s5.html) for other people's traffic.

Working with the FBI, Lumen, and others, Google's Threat Intelligence Group (GTIG) [said this week](https://cloud.google.com/blog/topics/threat-intelligence/google-continued-disruption-residential-proxy-networks) it had reduced the network's pool of usable devices by millions.

Google identifies NetNut, also tracked as **Popa**, as a network spread across home devices worldwide, including [smart TVs and streaming boxes](https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html), and GTIG estimates the network holds at least 2 million devices.

If one of those devices is in your home, strangers can route their own traffic through your internet connection, and your address gets the blame for whatever they do with it.

## How It Works

A residential proxy network sells access to real home internet addresses. Attackers pay to route their traffic through your connection so it looks like ordinary home browsing, not the datacenter traffic that security tools tend to block.

To build that pool, operators need their code running on home devices. Some devices ship with it pre-installed on cheap off-brand hardware; others pick it up when someone installs a [free app that hides](https://thehackernews.com/2024/04/malicious-apps-caught-secretly-turning.html) it. Once it is running, the device becomes an "exit node," a doorway that other people's traffic flows through.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Google says an exit node brings outside traffic inside the home network, giving attackers a foothold to reach other devices on it. Some of these home gadgets have also been pulled into large attack botnets such as [Mirai](https://thehackernews.com/2026/05/mirai-based-xlabsv1-botnet-exploits-adb.html) and [Badbox 2.0](https://thehackernews.com/2025/03/badbox-20-botnet-infects-1-million.html).

In a single week in June, GTIG counted 316 distinct threat clusters using suspected NetNut exit nodes, including cybercriminal and espionage groups, to hide their real location and run [password-guessing attacks](https://thehackernews.com/2026/07/azure-cli-password-spray-hits-at-least.html).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_37-m-7T9PZh0Q-MjcgM35aDLuM511z2n89DP0HmW-ZX7rdm9asspDGk-9FbTqUqMCujO-EJYuOQI8OcUCGI3fMb4sxrRG9nVt6a_nVsEpS_D1q3qmsA-04T68CwGJOCMD4wyIg6grU40cVC3pOP87hEpAqRAUzwFA7FkcfgCpkyjQnb45n3g-x9nuT8/s1700-e365/apps.jpg)

## The Company Behind It

Unlike most [proxy botnets](https://thehackernews.com/2026/03/authorities-disrupt-socksescort-proxy.html), NetNut traces back to a public company. In June, [researchers](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/) at Qurium, Synthient, Nokia Deepfield, and Spur tied Popa to NetNut.

NetNut is a proxy provider owned by publicly traded Israeli company Alarum Technologies (NASDAQ: ALAR). In a controlled test, [Synthient said](https://synthient.com/blog/popa-from-sourcing-to-distribution) traffic it sent into NetNut's commercial gateway came out through a device it had enrolled in Popa.

Synthient framed that as evidence of the traffic path, not proof of what NetNut knew or intended. Google's own intelligence aligns: it treats NetNut and Popa as the same network, and says the public reporting matches its view of how NetNut builds its botnet. The Hacker News [covered the researchers' findings](https://thehackernews.com/2026/06/weekly-recap-browser-bugs-edr-killers.html#:~:text=Israeli%20Company%20Linked%20to%20Popa%20Android%20TV%20Box%20Botnet) when they were published.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdIoUZwZqKP6HXDU7ie-374WXkD2okoAm-CmpnoFy76NBADEL1doCjedBvnGtEu0fhCUEDySNiJkXwXwQkzI7QTN6ZPTQ7EnVp_r9gcW1JndP24vQcDjHDnkZvfdFitf5Ff5wzGFF3ZpRbBcShltP6ETgeM-22ZXtC8IUBYBOT59x_91tLStqNNvUylGw/s1700-e365/access.jpg)

Alarum rejects the "botnet" label. It calls the research "demonstrably inaccurate assertions and flawed deductions rather than verified facts," and says its software is for consented bandwidth-sharing that does not compromise the devices it runs on.

The researchers' testing complicates that defense: Synthient reported that none of the more than 20 apps it examined actually showed users a consent prompt.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCF1XD5we-N0vbnLfp5XhOWJacZczXncVJ_wHP6C11_8w7glmIrppIrRq_NOkyjCqnWNfnKhECzaTOjW7sqMDuFJ6-aat7eH5bU-YeMpMLcrlHaGo6K01WKem2tm6kuSInVbt1Eb7IPYrhNfeOzJT8ujnzPvzLvQwPHD8qMOKARMBCqgRUqNMP-6GjvHA/s1700-e365/proxy-home.png)

## Why One Takedown Isn't Enough

Cutting off NetNut is messy by design. NetNut runs a reseller program that lets other companies sell its network under their own brand names. Google says it has high confidence that many popular, seemingly separate proxy brands are really reselling the same NetNut pool.

So a single takedown ripples across a lot of brands that look independent but are not.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWV...