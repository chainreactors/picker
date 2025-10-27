---
title: New GodRAT Trojan Targets Trading Firms Using Steganography and Gh0st RAT Code
url: https://thehackernews.com/2025/08/new-godrat-trojan-targets-trading-firms.html
source: The Hacker News
date: 2025-08-20
fetch_date: 2025-10-07T00:50:27.741547
---

# New GodRAT Trojan Targets Trading Firms Using Steganography and Gh0st RAT Code

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New GodRAT Trojan Targets Trading Firms Using Steganography and Gh0st RAT Code](https://thehackernews.com/2025/08/new-godrat-trojan-targets-trading-firms.html)

**Aug 19, 2025**Ravie LakshmananMalware / Cyber Attack

[![Steganography and Gh0st RAT Code](data:image/png;base64... "Steganography and Gh0st RAT Code")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsq_GI_YykIgjctOcC0P903Hdw-Zu02tnPUipIblNrMNmL-phCyBPLUxwMo487iM6BdZyMxmlXyBOjydhgoSVEZ4hYNIEysl-Vah4vBLhCQAsaEHNBG0pgDYLg5Q_UVDrhuRfxlyAG9-Sx0la_8JBEb9iu7sMaiadKbZIOy58x8tZOXymxNpFX7mcfDh0g/s790-rw-e365/trading.jpg)

Financial institutions like trading and brokerage firms are the target of a new campaign that delivers a previously unreported remote access trojan called **GodRAT**.

The malicious activity involves the "distribution of malicious .SCR (screen saver) files disguised as financial documents via Skype messenger," Kaspersky researcher Saurabh Sharma [said](https://securelist.com/godrat/117119/) in a technical analysis published today.

The attacks, which have been active as recently as August 12, 2025, employ a technique called steganography to conceal within image files shellcode used to download the malware from a command-and-control (C2) server. The screen saver artifacts have been detected since September 9, 2024, targeting countries and territories like Hong Kong, the United Arab Emirates, Lebanon, Malaysia, and Jordan.

Assessed to be based on Gh0st RAT, GodRAT follows a plugin-based approach to augment its functionality in order to harvest sensitive information and deliver secondary payloads like AsyncRAT. It's worth mentioning that Gh0st RAT had its source code [leaked](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html) publicly in 2008 and has since been [adopted](https://thehackernews.com/2024/07/gh0st-rat-trojan-targets-chinese.html) by [various Chinese hacking groups](https://thehackernews.com/2024/06/chinese-hackers-deploy-spicerat-and.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Russian cybersecurity company said the malware is an evolution of another Gh0st RAT-based backdoor known as AwesomePuppet that was first documented in 2023 and is likely believed to be the handiwork of the prolific Chinese threat actor, [Winnti](https://thehackernews.com/2025/02/winnti-apt41-targets-japanese-firms-in.html) (aka APT41).

The screen saver files act as a self-extracting executable incorporating various embedded files, including a malicious DLL that's sideloaded by a legitimate executable. The DLL extracts shellcode hidden within a .JPG image file that then paves the way for the deployment of GodRAT.

The trojan, for its part, establishes communication with the C2 server over TCP, collects system information, and pulls the list of installed antivirus software on the host. The captured details are sent to the C2 server, after which the server responds with follow-up instructions that allow it to -

* Inject a received plugin DLL into memory
* Close the socket and terminate the RAT process
* Download a file from a provided URL and launch it using the CreateProcessA API
* Open a given URL using the shell command for opening Internet Explorer

One of the plugins downloaded by the malware is a FileManager DLL that can enumerate the file system, perform file operations, open folders, and even run searches for files at a specified location. The plugin has also been used to deliver additional payloads, such as a password stealer for Google Chrome and Microsoft Edge browsers and the AsyncRAT trojan.

Kaspersky said it discovered the complete source code for the GodRAT client and builder that was [uploaded](https://www.virustotal.com/gui/file/67c713a44186315d7cbfec4745b7dd199d86711f48c5f0778a71871ac3b02624/details) to the VirusTotal online malware scanner in late July 2024. The builder can be used to generate either an executable file or a DLL.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

When the executable option is chosen, users have the choice of selecting a legitimate binary from a list to which the malicious code is injected into: svchost.exe, cmd.exe, cscript.exe, curl.exe, wscript.exe, QQMusic.exe and QQScLauncher.exe. The final payload can be saved with one of the following file types: .exe, .com, .bat, .scr, and .pif.

"Old implant codebases, such as Gh0st RAT, which are nearly two decades old, continue to be used today," Kaspersky said. "These are often customized and rebuilt to target a wide range of victims."

"These old implants are known to have been used by various threat actors for a long time, and the GodRAT discovery demonstrates that legacy codebases like Gh0st RAT can still maintain a long lifespan in the cybersecurity landscape."

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

[Chinese Hackers](https://thehackernews.com/search/label/Chinese%20Hackers)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Kaspersky](https://thehackernews.com/search/label/Kaspersky)[Malware](https://thehackernews.com/search/label/Malware)[...