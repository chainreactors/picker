---
title: PLAYFULGHOST Delivered via Phishing and SEO Poisoning in Trojanized VPN Apps
url: https://thehackernews.com/2025/01/playfulghost-delivered-via-phishing-and.html
source: The Hacker News
date: 2025-01-05
fetch_date: 2025-10-06T20:10:06.951901
---

# PLAYFULGHOST Delivered via Phishing and SEO Poisoning in Trojanized VPN Apps

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

# [PLAYFULGHOST Delivered via Phishing and SEO Poisoning in Trojanized VPN Apps](https://thehackernews.com/2025/01/playfulghost-delivered-via-phishing-and.html)

**Jan 04, 2025**Ravie LakshmananMalware / VPN Security

[![Trojanized VPN Apps](data:image/png;base64... "Trojanized VPN Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXLFjQ-4GEdcIHBm4mPIgrG7KMXG-E4nN5eg9XXB3A8D43aPW76K8F0NKKLUHOzmsI4viak9AVcvTaqIWou9wb1xg8U_vUMGOSKnutsllqPjE8jeUyw6VatXvBRciWKHI7ey_yBIoTMcUv_8h5rrGbbndour7C-qle4AEgAp9_IL-qQmdMXGD_3LFQMgMe/s790-rw-e365/PLAYFULGHOST.gif)

Cybersecurity researchers have flagged a new malware called **PLAYFULGHOST** that comes with a wide range of information-gathering features like keylogging, screen capture, audio capture, remote shell, and file transfer/execution.

The backdoor, according to Google's Mandiant Managed Defense team, shares functional overlaps with a known remote administration tool referred to as [Gh0st RAT](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html), which had its source code publicly leaked in 2008.

PLAYFULGHOST's initial access pathways include the use of phishing emails bearing code of conduct-related lures or search engine optimization (SEO) poisoning techniques to distribute trojanized versions of legitimate VPN apps like LetsVPN.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"In one phishing case, the infection begins by tricking the victim into opening a malicious RAR archive disguised as an image file by using a .jpg extension," the company [said](https://www.googlecloudcommunity.com/gc/Community-Blog/Finding-Malware-Unveiling-PLAYFULGHOST-with-Google-Security/ba-p/850676). "When extracted and executed by the victim, the archive drops a malicious Windows executable, which eventually downloads and executes PLAYFULGHOST from a remote server."

Attack chains employing SEO poisoning, on the other hand, seek to deceive unsuspecting users into downloading a malware-laced installer for LetsVPN, which, when launched, drops an interim payload responsible for retrieving the backdoor components.

The infection is notable for leveraging methods such as DLL search order hijacking and side-loading to launch a malicious DLL that's then used to decrypt and load PLAYFULGHOST into memory.

Mandiant said it also observed a "more sophisticated execution scenario" wherein a Windows shortcut ("QQLaunch.lnk") file, combines the contents of two other files named "h" and "t" to construct the rogue DLL and sideload it using a renamed version of "curl.exe."

[![Trojanized VPN Apps](data:image/png;base64... "Trojanized VPN Apps")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5K1swc8iNrcPFyfTHHuPv7lGi7ZUAnvnqnSvcBcUJ_uDRiGVK-11arog1tQzihzz3qHbI-UyBooSFoPx5DymWp_KzLe6gDYO29A3eCJWpP8U4fMmb56yxZreRP4QJS1d1dYJN2PPc4NRt-AFok1t3lZNq7gaw7MozucTI61i6gn8-O2lwPlJhkfQIBHSu/s790-rw-e365/malware.png)

PLAYFULGHOST is capable of setting up persistence on the host using four different methods: Run registry key, scheduled task, Windows Startup folder, and Windows service. It boasts an extensive set of features that allow it to gather extensive data, including keystrokes, screenshots, audio, QQ account information, installed security products, clipboard content, and system metadata.

It also comes with capabilities to drop more payloads, block mouse and keyboard input, clear Windows event logs, wipe clipboard data, perform file operations, delete caches and profiles associated with web browsers like Sogou, QQ, 360 Safety, Firefox, and Google Chrome, and erase profiles and local storage for messaging applications such as Skype, Telegram, and QQ.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Some of the other tools deployed via PLAYFULGHOST are Mimikatz and a rootkit that's capable of hiding registry, files, and processes specified by the threat actor. Also dropped along with the download of PLAYFULGHOST components is an open-source utility called [Terminator](https://thehackernews.com/2024/10/hackers-abuse-edrsilencer-tool-to.html) that can kill security processes by means of a Bring Your Own Vulnerable Driver ([BYOVD](https://www.halcyon.ai/blog/blocking-byovd-techniques-to-prevent-av-edr-xdr-bypasses)) attack.

"On one occasion, Mandiant observed a PLAYFULGHOST payload being embedded within BOOSTWAVE," the tech giant said. "BOOSTWAVE is a shellcode that acts as in-memory dropper for an appended Portable Executable (PE) payload."

The targeting of applications like Sogou, QQ, and 360 Safety and the use of LetsVPN lures raise the possibility that these infections are targeting Chinese-speaking Windows users. In July 2024, Canadian cybersecurity vendor eSentire [revealed](https://thehackernews.com/2024/07/gh0st-rat-trojan-targets-chinese.html) a similar campaign that leveraged fake installers for Google Chrome to propagate Gh0st RAT using a dropper dubbed Gh0stGambit.

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

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernew...