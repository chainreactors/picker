---
title: Researchers Warn of MystRodX Backdoor Using DNS and ICMP Triggers for Stealthy Control
url: https://thehackernews.com/2025/09/researchers-warn-of-mystrodx-backdoor.html
source: The Hacker News
date: 2025-09-03
fetch_date: 2025-10-02T19:34:45.676059
---

# Researchers Warn of MystRodX Backdoor Using DNS and ICMP Triggers for Stealthy Control

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

# [Researchers Warn of MystRodX Backdoor Using DNS and ICMP Triggers for Stealthy Control](https://thehackernews.com/2025/09/researchers-warn-of-mystrodx-backdoor.html)

**Sep 02, 2025**Ravie LakshmananCyber Espionage / Network Security

[![MystRodX Backdoor](data:image/png;base64... "MystRodX Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifyMQps9wMSJxUhmH1pRHENqxmqR-4lKpoRAJtjQ61i3YeIKnzEgcVy63CUUSnD5XHpeKKzkm8LyR1sjS6sOon_hDhMgqwe4-j1LvaDsrUORztFMvBb38ZuvbIX4VhGJTWVHgRxLE-Kq9ftynUyGVBjKthk3g9Okaa6JggIhugP3dj4HBFn7NucsPFLxTd/s790-rw-e365/malware-attack.jpg)

Cybersecurity researchers have disclosed a stealthy new backdoor called **MystRodX** that comes with a variety of features to capture sensitive data from compromised systems.

"MystRodX is a typical backdoor implemented in C++, supporting features like file management, port forwarding, reverse shell, and socket management," QiAnXin XLab [said](https://blog.xlab.qianxin.com/mystrodx_covert_dual-mode_backdoor_en/) in a report published last week. "Compared to typical backdoors, MystRodX stands out in terms of stealth and flexibility."

MystRodX, also called ChronosRAT, was [first documented](https://thehackernews.com/2025/08/cl-sta-0969-installs-covert-malware-in.html) by Palo Alto Networks Unit 42 last month in connection with a threat activity cluster called CL-STA-0969 that it said exhibits overlaps with a China-nexus cyber espionage group dubbed Liminal Panda.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The malware's stealth stems from the use of various levels of encryption to obscure source code and payloads, while its flexibility allows it to dynamically enable different functions based on a configuration, such as choosing TCP or HTTP for network communication, or opting for plaintext or AES encryption to secure network traffic.

MystRodX also supports what's called a wake-up mode, thereby enabling it to function as a passive backdoor that can be triggered following the receipt of specially crafted DNS or ICMP network packets from incoming traffic. There is evidence to suggest that the malware may have been around since at least January 2024, based on an activation timestamp set in the configuration.

"Magic value is verified, MystRodX establishes communication with the C2 [command-and-control] using the specified protocol and awaits further commands," XLab researchers said. "Unlike well-known stealth backdoors like [SYNful Knock](https://thehackernews.com/2025/08/fbi-warns-russian-fsb-linked-hackers.html), which manipulates TCP header fields to hide commands, MystRodX uses a simpler yet effective approach: it hides activation instructions directly in the payload of ICMP packets or within DNS query domains."

The malware is delivered by means of a dropper that makes use of a spate of debugger- and virtual machine-related checks to determine if the current process is being debugged or it's being run within a virtualized environment. Once the validation step is complete, the next-stage payload is decrypted. It contains three components -

* daytime, a launcher responsible for launching chargen
* chargen, the MystRodX backdoor component, and
* [BusyBox](https://en.wikipedia.org/wiki/BusyBox), a legitimate Unix utility software suite (removed in subsequent iterations)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

MystRodX, once executed, continuously monitors the daytime process, and if it is not found to be running, immediately launches it. Its configuration, which is encrypted using the AES algorithm, contains information pertaining to the C2 server, backdoor type, and main and backup C2 ports.

"When the Backdoor Type is set to 1, MystRodX enters passive backdoor mode and waits for an activation message," XLab said. "When the value of Backdoor Type is not 1, MystRodX enters active backdoor mode and establishes communication with the C2 specified in the configuration, waiting to execute the received commands."

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

[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[encryption](https://thehackernews.com/search/label/encryption)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersona...