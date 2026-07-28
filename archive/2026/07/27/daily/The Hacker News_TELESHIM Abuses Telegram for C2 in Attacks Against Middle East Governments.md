---
title: TELESHIM Abuses Telegram for C2 in Attacks Against Middle East Governments
url: https://thehackernews.com/2026/07/teleshim-abuses-telegram-for-c2-in.html
source: The Hacker News
date: 2026-07-27
fetch_date: 2026-07-28T05:00:17.026905
---

# TELESHIM Abuses Telegram for C2 in Attacks Against Middle East Governments

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

# [TELESHIM Abuses Telegram for C2 in Attacks Against Middle East Governments](https://thehackernews.com/2026/07/teleshim-abuses-telegram-for-c2-in.html)

**Ravie Lakshmanan**Jul 27, 2026Cyber Attack / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikuWOQRYm6WQ1zHmOlYkI7jlVOUUKGBIlo68iWyUVuaZ5n3i7ODu8DYpntAk2aGZQ_7LsYpXpp5v0PcQMLxP8LQOajtKl-WaDBb7_wDpo8P3-iCcAwr74JY4rXNeHJJv9h6EB447wPEnrZE08YfDO_WI9N4B_C1lPvxILfvv00Z_J8yHntLSfNYbPVCDjS/s1700-e365/telegram-c2.jpg)

Cybersecurity researchers have flagged fresh malicious cyber activity by a threat actor with ties to East Asia targeting government entities in the Middle East.

The intrusions have resulted in the deployment of previously unreported malware families dubbed TELESHIM, MIXEDKEY, and BINDCLOAK, according to Zscaler ThreatLabz. The cybersecurity firm said it detected the campaign earlier this month.

"The campaign used a multi-stage attack chain to establish and maintain access on infected systems, with TELESHIM abusing the Telegram API for command-and-control (C2) communication to blend in with legitimate internet traffic," Sudeep Singh, senior manager of APT research at Zscaler ThreatLabz, [said](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1) in a technical write-up published last week.

The attack chain starts with an ISO file containing a legitimate executable ("RegSchdTask.exe") that's used to sideload a rogue DLL ("AsTaskSched.dll"), a 32-bit Windows backdoor called TELESHIM that then leverages Telegram as C2 to retrieve next-stage components.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Two of these payloads are used to trigger a second [DLL side-loading](https://techzone.bitdefender.com/en/tech-explainers/what-is-dll-sideloading.html) chain comprising "GoProAlertService.exe" and "pthreadVC2.dll," with the latter acting as a reflective loader codenamed MIXEDKEY to decrypt the contents of "C99F29AC08454855B3D538960BB2F34F.PCPKEY" and execute it.

Both TELESHIM and MIXEDKEY have been found to rely on heavy code obfuscation techniques, including string encryption, control flow flattening (CFF), mixed boolean arithmetic (MBA), and opaque predicates to deter reverse engineering efforts. TELESHIM also employs an array of methods to detect the presence of virtualization-based analysis environments. Some of these are listed below -

* Hypervisor detection using CPUID
* RAM speed check using the Windows Management Instrumentation (WMI)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjo4MNoLdWkaFbymCqdVoDciMnf-egEkhnzeo8GiIMB7pABTqeqp8rEvYgy9AUjh5nFaCaG7VC0Yo3okpSF0FaevJxFYGYPGaiqb3IuCjoR_m6oRpLQx5FCPnqcJWhEOoy25SKfNeIPClt5sLGyJcluRkiuaKH7TU3rK9YYRfVWnhiqAd-BOuT5uL48cYb/s1700-e365/zzkey.jpg)

TELESHIM C2 communications supports two types of messages -

* Control messages, which are used to register the infected host by sending the host's MAC address and executing received commands and exfiltrating the results back to the server in chunks if the output is larger than 1,000 bytes
* Download and execute messages, which are used to download and run secondary payloads as scheduled tasks

What's notable about the final payload is that it's locked behind two layers of XOR encryption, the second layer using a technique called [environmental keying](https://attack.mitre.org/techniques/T1480/001/) by encrypting it by means of a decryption key derived from the infected machine's volume serial number. This is done so that the malware detonates only on intended targets.

The attack sequence culminates with the deployment of BINDCLOAK, a 64-bit C2 implant written in C++ that contacts an external server ("cert.hypersnet[.]com").

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh3-o9La7DYm6jz5qcavVBLvRXUoQLqwrMmrvB529PbUxdg7TJZS3BMjVi4D7vd6V9vlSf_OX48mmXQWPgah_SPITaGgg4AP9YxB2AH-63YeWU39N3DXadwc_2zjIpTwCt0iyTdPZIM-KzKhDf_JDPWDGu3IbYfi1ilQE8Ly29HiKYagSIur-il4k7MMNv8/s728-e100/sygnia-d-3.png)](https://thn.news/sygnia-webinar)

ThreatLabz noted that it identified post-compromise activity from the C2 operator, such as system, user, and network reconnaissance commands, as well as the delivery of next-stage payloads, most of which occurred between July 7, 2026 and July 9, 2026. The C2 commands have been executed only between 4 a.m. and 12 p.m. UTC, with a major chunk of the activity taking place between 7 a.m. and 11 a.m. UTC.

Based on the threat actor's public IP address, the system locale configured on their Windows server, the geolocation of the IP address, and the active operational hours, it's assessed with moderate-to-high confidence that the campaign is the work of an adversary originating from East Asia. It has not been attributed to any known threat actor or group at this stage.

"The activity also reflects broader trends such as EDR evasion, blending in with legitimate internet traffic through abuse of trusted platforms, and the use of code-obfuscation techniques such as MBA and CFF to hinder reverse engineering," Singh said.

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#li...