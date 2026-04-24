---
title: China-Linked GopherWhisper Infects 12 Mongolian Government Systems with Go Backdoors
url: https://thehackernews.com/2026/04/china-linked-gopherwhisper-infects-12.html
source: The Hacker News
date: 2026-04-23
fetch_date: 2026-04-24T04:57:38.677190
---

# China-Linked GopherWhisper Infects 12 Mongolian Government Systems with Go Backdoors

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [China-Linked GopherWhisper Infects 12 Mongolian Government Systems with Go Backdoors](https://thehackernews.com/2026/04/china-linked-gopherwhisper-infects-12.html)

**Ravie Lakshmanan**Apr 23, 2026Threat Intelligence / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcPZEHQ2ePgeeD1JO3nqkHDxu5XWd53XZ8GsPxgX5Gl3vY-isf7bdT1_8ZGbMGOwic5gJKYXp0G5rIiSacQvidnb3_voREgqsyanhwo0uQs1HLNXACrsV2tLmHXlxA4FizErdbwb5o35MEDIrZKMkDsAAzIVPt0g6pTMbsZSN7SIwTEozmgX7MO26XxapY/s1700-e365/chinese-hacking.jpg)

Mongolian governmental institutions have emerged as the target of a previously undocumented China-aligned advanced persistent threat (APT) group tracked as **GopherWhisper**.

"The group wields a wide array of tools mostly written in Go, using injectors and loaders to deploy and execute various backdoors in its arsenal," Slovakian cybersecurity company ESET [said](https://www.welivesecurity.com/en/eset-research/gopherwhisper-burrow-full-malware/) in a report shared with The Hacker News. "GopherWhisper abuses legitimate services, notably Discord, Slack, Microsoft 365 Outlook, and file.io for command-and-control (C&C) communication and exfiltration."

The group was first discovered in January 2025 following the discovery of a never-before-seen backdoor codenamed LaxGopher on a system belonging to a Mongolian governmental entity. GopherWhisper is assessed to be active at least since November 2023. Besides LaxGopher, some of the other malware families part of the threat actor's arsenal are Golang-based tools to receive instructions from the C&C server, execute them, and send the results back.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

Also used by the threat actor is a file collection tool to gather files of interest and exfiltrate them in compressed format to the file[.]io file sharing service and a C++ backdoor that offers remote control over compromised hosts.

Telemetry data from ESET shows that about 12 systems associated with the Mongolian governmental institution were infected by the backdoors, with C&C traffic from the attacker-controlled Discord and Slack servers indicating dozens of other victims.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhezmThtbQaAIr1oji9r1qi7xmhJcbkHN77X7k14XQm-EwAtlpHIDflocEAqjoanruHZh9Vs7p1lHXQkN4ch_XR3MrhCd5aO-KHlObqSOdd2u4CmwpNHgdmjlmJJE_OlBu6Yapamyh69WV88qdG1SCbuGHopvjQPjJxDrxB2iyYJPPISzM-UNah1k3SblKk/s1700-e365/go.jpg)

Exactly how GopherWhisper obtains initial access to the target networks is currently not known. But a successful foothold is followed by attempts to deploy a wide range of tools and implants -

* **JabGopher**, an injector that executes the LaxGopher ("whisper.dll") backdoor.
* **LaxGopher**, a Go-based backdoor that uses Slack for C2 to execute commands via "cmd.exe" and publish the results back to the Slack channel, as well as download additional malware.
* **CompactGopher**, a Go-based file collection utility dropped by LaxGopher to filter files of interest by extensions (.doc, .docx, .jpg, .xls, .xlsx, .txt, .pdf, .ppt, and .pptx.), compress them into ZIP files, encrypt the archives using AES-CFB-128, and exfiltrate them to file[.]io.
* **RatGopher**, a Go-based backdoor that uses a private Discord server to receive C&C messages, execute commands, and publish the results back to the configured Discord channel, as well as upload and download files from file[.]io.
* **SSLORDoor**, a C++-based backdoor that uses OpenSSL BIO for communication via raw sockets on port 443 to enumerate drives, perform file operations, and run commands based on C&C input via "cmd.exe."
* **FriendDelivery**, a malicious DLL that serves as a loader and injector for BoxOfFriends.
* **BoxOfFriends**, a Go-based backdoor that uses the Microsoft Graph API to craft draft emails for C2 using hard-coded credentials, with the earliest Outlook account created for this purpose ("barrantaya.1010@outlook[.]com") created on July 11, 2024.

"Timestamp inspection of the Slack and Discord messages showed us that the bulk of them were being sent during working hours, i.e., between 8 a.m. and 5 p.m., which aligns with China Standard Time," ESET researcher Eric Howard said. "Furthermore, the locale for the configured user in Slack metadata was also set to this time zone. We therefore believe that GopherWhisper is a China-aligned group."

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

[Advanced Persistent Threat](https://thehackernews.com/search/label/Advanced%20Persistent%20Threat), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Discord](https://thehackernews.com/search/label/Discord), [Golang](https://thehackernews.com/search/label/Golang), [Malware](https://thehackernews.com/search/label/Malware), [Microsoft 365](https://thehackernews.com/search/label/Microsoft%20365), [Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

Trending News

[![108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](data:image/svg+xml;base64... "108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users")

108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000 Users](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)

[![Mirax Android RAT Turns Devices into SOCKS5 Proxies, Reaching 220,000 via Meta Ads](data:image/svg+xml;base...