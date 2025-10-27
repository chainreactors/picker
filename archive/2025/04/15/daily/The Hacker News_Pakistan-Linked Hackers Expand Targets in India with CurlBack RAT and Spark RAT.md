---
title: Pakistan-Linked Hackers Expand Targets in India with CurlBack RAT and Spark RAT
url: https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html
source: The Hacker News
date: 2025-04-15
fetch_date: 2025-10-06T22:09:15.118514
---

# Pakistan-Linked Hackers Expand Targets in India with CurlBack RAT and Spark RAT

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

# [Pakistan-Linked Hackers Expand Targets in India with CurlBack RAT and Spark RAT](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html)

**Apr 14, 2025**Ravie LakshmananCyber Attack / Malware

[![Pakistan-Linked Hackers](data:image/png;base64... "Pakistan-Linked Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHdxRuX44rzcNSq1lr55ivGhactRjIYLLTqUQNOyWrAWSGTcKZS-RXviCtiMcwWf2YSPil43T617kGoYreElbArRojklK7CKtM9P6DFHmuTm0FVDigxAsLP41pPKxojIOczZ8cFryQK2S38kPfNjvp-p5Ra2gQd9UG8j7BjvN9y44yHNHwP2IL-NxxWZJF/s790-rw-e365/pak-hackers.jpg)

A threat actor with ties to Pakistan has been observed targeting various sectors in India with various remote access trojans like Xeno RAT, Spark RAT, and a previously undocumented malware family called **CurlBack RAT**.

The activity, detected by SEQRITE in December 2024, targeted Indian entities under railway, oil and gas, and external affairs ministries, marking an expansion of the hacking crew's targeting footprint beyond government, defence, maritime sectors, and universities.

"One notable shift in recent campaigns is the transition from using HTML Application (HTA) files to adopting Microsoft Installer (MSI) packages as a primary staging mechanism," security researcher Sathwik Ram Prakki [said](https://www.seqrite.com/blog/goodbye-hta-hello-msi-new-ttps-and-clusters-of-an-apt-driven-by-multi-platform-attacks/).

[SideCopy](https://thehackernews.com/2023/11/sidecopy-exploiting-winrar-flaw-in.html) is suspected to be a sub-cluster within [Transparent Tribe](https://thehackernews.com/2024/06/pakistani-hackers-use-disgomoji-malware.html) (aka APT36) that's active since at least 2019. It's so named for [mimicking the attack chains](https://thehackernews.com/2021/07/sidecopy-hackers-target-indian.html) associated with another threat actor called [SideWinder](https://thehackernews.com/2025/03/sidewinder-apt-targets-maritime-nuclear.html) to deliver its own payloads.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In June 2024, SEQRITE [highlighted](https://www.seqrite.com/blog/umbrella-of-pakistani-threats-converging-tactics-of-cyber-operations-targeting-india/) SideCopy's use of obfuscated HTA files, leveraging a technique previously observed in SideWinder attacks. The files were also found to contain references to URLs that hosted RTF files identified as used by SideWinder.

The attacks culminated in the deployment of [Action RAT](https://thehackernews.com/2023/05/sidecopy-using-action-rat-and-allakore.html) and [ReverseRAT](https://thehackernews.com/2023/02/researchers-warn-of-reverserat-backdoor.html), two known malware families attributed to SideCopy, and several other payloads, including Cheex to steal documents and images, a USB copier to siphon data from attached drives, and a .NET-based Geta RAT that's capable of executing 30 commands sent from a remote server.

The RAT is also equipped to steal both Firefox and Chromium-based browser data of all accounts, profiles, and cookies, a feature borrowed from AsyncRAT.

"APT36 focus is majorly Linux systems whereas SideCopy targets Windows systems adding new payloads to its arsenal," SEQRITE noted at the time.

[![CurlBack RAT and Spark RAT](data:image/png;base64... "CurlBack RAT and Spark RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBggth0_hEh4ncGOqfsQEXz0uf2kWMoqD_sHJPVj0bvcg5ekmpAPbe_Ta3l_0nNjLhV1cvxb63rhFQzvZO7Y7cE0KU6ujEGjsqZTlAmxpnsCdz732kIRYqhQwpkkaciEa8-pFjjwSb3tWrJ955SAe5f6MW811-mi9COjYNGX6E3oISdHXuoR26-c8W8zff/s790-rw-e365/sidecopy.png)

The latest findings demonstrate a continued maturation of the hacking group, coming into its own, while leveraging email-based phishing as a distribution vector for malware. These email messages contain various kinds of lure documents, ranging from holiday lists for railway staff to cybersecurity guidelines issued by a public sector undertaking called the Hindustan Petroleum Corporation Limited (HPCL).

One cluster of activity is particularly noteworthy given its ability to target both Windows and Linux systems, ultimately leading to the deployment of a cross-platform remote access trojan known as [Spark RAT](https://thehackernews.com/2024/07/tag-100-new-threat-actor-uses-open.html) and a new Windows-based malware codenamed CurlBack RAT that can gather system information, download files from the host, execute arbitrary commands, elevate privileges, and list user accounts.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A second cluster has been observed using the decoy files as a way to initiate a multi-step infection process that drops a custom version of [Xeno RAT](https://thehackernews.com/2024/02/open-source-xeno-rat-trojan-emerges-as.html), which incorporates basic string manipulation methods.

"The group has shifted from using HTA files to MSI packages as a primary staging mechanism and continues to employ advanced techniques like DLL side-loading, reflective loading, and AES decryption via PowerShell," the company said.

"Additionally, they are leveraging customized open-source tools like Xeno RAT and Spark RAT, along with deploying the newly identified CurlBack RAT. Compromised domains and fake sites are being utilized for credential phishing and payload hosting, highlighting the group's ongoing efforts to enhance persistence and evade detection."

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
[**Share on Reddit](#...