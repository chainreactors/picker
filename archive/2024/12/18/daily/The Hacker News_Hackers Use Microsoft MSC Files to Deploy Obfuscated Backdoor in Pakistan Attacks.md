---
title: Hackers Use Microsoft MSC Files to Deploy Obfuscated Backdoor in Pakistan Attacks
url: https://thehackernews.com/2024/12/hackers-use-microsoft-msc-files-to.html
source: The Hacker News
date: 2024-12-18
fetch_date: 2025-10-06T19:45:08.728852
---

# Hackers Use Microsoft MSC Files to Deploy Obfuscated Backdoor in Pakistan Attacks

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

# [Hackers Use Microsoft MSC Files to Deploy Obfuscated Backdoor in Pakistan Attacks](https://thehackernews.com/2024/12/hackers-use-microsoft-msc-files-to.html)

**Dec 17, 2024**Ravie LakshmananCyber Attack / Malware

[![Obfuscated Backdoor](data:image/png;base64... "Obfuscated Backdoor")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWu76V7X7N6EmmPB39gaTXKEG4sLqoVUNlBW2eKzbeGjwns_5wjL-qUIg8gjVrCddtOM-b_WadNapczU9iDUqjtd8RmKVz884ZJqUOs7Mj94xg_Ae2PI39cWauypgUST2O1NsL1jW0i2YBzWc9T7mU8u73OEkKUUHsU0HYFvLTbNBvUaiuGfNOQdAJocOQ/s790-rw-e365/main.png)

A new phishing campaign has been observed employing tax-themed lures to deliver a stealthy backdoor payload as part of attacks targeting Pakistan.

Cybersecurity company Securonix, which is tracking the activity under the name **FLUX#CONSOLE**, said it likely starts with a phishing email link or attachment, although it said it couldn't obtain the original email used to launch the attack.

"One of the more notable aspects of the campaign is how the threat actors leverage MSC (Microsoft Common Console Document) files to deploy a dual-purpose loader and dropper to deliver further malicious payloads," security researchers Den Iuzvyk and Tim Peck [said](https://www.securonix.com/blog/analyzing-fluxconsole-using-tax-themed-lures-threat-actors-exploit-windows-management-console-to-deliver-backdoor-payloads/).

It's worth noting that the abuse of specially crafted management saved console (MSC) files to execute malicious code has been codenamed [GrimResource](https://thehackernews.com/2024/06/new-attack-technique-exploits-microsoft.html) by Elastic Security Labs.

The starting point is a file with double extensions (.pdf.msc) that masquerades as a PDF file (if the setting to display file extensions is disabled) and is designed to execute an embedded JavaScript code when launched using the Microsoft Management Console (MMC).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This code, in turn, is responsible for retrieving and displaying a decoy file, while also covertly loading a DLL file ("DismCore.dll") in the background. One such document used in the campaign is named "Tax Reductions, Rebates and Credits 2024," which is a legitimate document associated with Pakistan's Federal Board of Revenue (FBR).

"In addition to delivering the payload from an embedded and obfuscated string, the .MSC file is able to execute additional code by reaching out to a remote HTML file which also accomplishes the same goal," the researchers said, adding that persistence is established using scheduled tasks.

The main payload is a backdoor capable of setting up contact with a remote server and executing commands sent by it to exfiltrate data from compromised systems. Securonix said the attack was disrupted 24 hours after initial infection.

It's currently not clear who is behind the malware campaign, although the threat actor known as [Patchwork](https://thehackernews.com/2024/07/patchwork-hackers-target-bhutan-with.html) has been previously observed using a similar [tax-related document from FBR](https://x.com/ginkgo_g/status/1731870687562752375) in early December 2023.

Securonix told The Hacker News that while it's "definitely possible" Patchwork could be behind the attacks, it said it was unable to build solid connections based on known TTPs and other telemetry sources to confidently state attribution.

"The referenced phishing lures look similar, however we've seen threat actors piggy back lures before in the past, especially with either PDFs or even image file lures," Peck, senior threat researcher at Securonix, said. "However, if this is the case and Patchwork is responsible, it would provide further insights into their operations and current attack chains."

"From the highly obfuscated JavaScript used in the initial stages to the deeply concealed malware code within the DLL, the entire attack chain exemplifies the complexities of detecting and analyzing contemporary malicious code," the researchers said.

"Another notable aspect of this campaign is the exploitation of MSC files as a potential evolution of the classic LNK file which has been popular with threat actors over the past few years. Like LNK files, they also allow for the execution of malicious code while blending into legitimate Windows administrative workflows."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[JavaScript](https://thehackernews.com/search/label/JavaScript)[Malware](https://thehackernews.com/search/label/Malware)[Microsoft](https://thehackernews.com/search/label/Microsoft)[MSC](https://thehackernews.com/search/label/MSC)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[Securonix](https://thehackernews.com/search/label/Securonix)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/20...