---
title: Worok Hackers Abuse Dropbox API to Exfiltrate Data via Backdoor Hidden in Images
url: https://thehackernews.com/2022/11/worok-hackers-abuse-dropbox-api-to.html
source: The Hacker News
date: 2022-11-15
fetch_date: 2025-10-03T22:48:58.047932
---

# Worok Hackers Abuse Dropbox API to Exfiltrate Data via Backdoor Hidden in Images

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

# [Worok Hackers Abuse Dropbox API to Exfiltrate Data via Backdoor Hidden in Images](https://thehackernews.com/2022/11/worok-hackers-abuse-dropbox-api-to.html)

**Nov 14, 2022**Ravie Lakshmanan

[![Worok Malware](data:image/png;base64... "Worok Malware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjyImt_ja580R1Rb_X6991WjylIGhY1WTIta0-H1lX34KBTUakEygTmXDIaiXfPu11Fh0T6CuhkTALy2C7y9yuQdab_sfKUb2gBsQ-0a3yY9jgliDC3-prKY1G9Ws1s82nW1i2h9VSU__t7yh-IF7Trt_4LmV8g4CPQHS9e-pM1jk9CzilFHvK-kYd/s790-rw-e365/hackingg-1.jpg)

A recently discovered cyber espionage group dubbed **Worok** has been found hiding malware in seemingly innocuous image files, corroborating a crucial link in the threat actor's infection chain.

Czech cybersecurity firm Avast said the purpose of the PNG files is to conceal a payload that's used to facilitate information theft.

"What is noteworthy is data collection from victims' machines using Dropbox repository, as well as attackers using Dropbox API for communication with the final stage," the company [said](https://decoded.avast.io/martinchlumecky/png-steganography/).

The development comes a little over two months after ESET disclosed details of attacks carried out by [Worok](https://thehackernews.com/2022/09/worok-hackers-target-high-profile-asian.html) against high-profile companies and local governments located in Asia and Africa. Worok is believed to share tactical overlaps with a Chinese threat actor tracked as [TA428](https://thehackernews.com/2022/08/chinese-hackers-targeted-dozens-of.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Slovak cybersecurity company also documented Worok's compromise sequence, which makes use of a C++-based loader called **CLRLoad** to pave the way for an unknown PowerShell script embedded within PNG images, a technique known as steganography.

That said, the initial attack vector remains unknown as yet, although certain intrusions have entailed the use of [ProxyShell vulnerabilities](https://thehackernews.com/2021/11/hackers-exploiting-proxylogon-and.html) in Microsoft Exchange Server to deploy the malware.

Avast's findings show that the adversarial collective makes use of [DLL side-loading](https://attack.mitre.org/techniques/T1574/002/) upon gaining initial access to execute the CLRLoad malware, but not before performing lateral movement across the infected environment.

[![CLRLoad Malware Loader](data:image/png;base64... "CLRLoad Malware Loader")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZKWN96jhZiilNfM3ha8DI95mFfLKfvxX-_6hIfbL9Zdq84bQ2X2DGBNUfRSgt21GKjOmDR059NJWPOkQnIYWSAzVmUPSOOSsc-MdkzJuiwQhDLT9cQ_hkxocjLbMzQ9B08EIKw53cHJed2m7HxikRDFn90cQUqHjloY9Ti9YJwywPl_s06h24pKMk/s790-rw-e365/malware-hacking.jpg)

PNGLoad, which is launched by CLRLoad (or alternatively another first-stage called PowHeartBeat), is said to come in two variants, each responsible for decoding the malicious code within the image to launch either a PowerShell script or a .NET C#-based payload.

The PowerShell script has continued to be elusive, although the cybersecurity company noted it was able to flag a few PNG files belonging to the second category that dispensed a steganographically embedded C# malware.

"At first glance, the PNG pictures look innocent, like a fluffy cloud," Avast said. "In this specific case, the PNG files are located in C:\Program Files\Internet Explorer, so the picture does not attract attention because Internet Explorer has a similar theme."

This new malware, codenamed DropboxControl, is an information-stealing implant that uses a Dropbox account for command-and-control, enabling the threat actor to upload and download files to specific folders as well as run commands present in a certain file.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Some of the notable commands include the ability to execute arbitrary executables, download and upload data, delete and rename files, capture file information, sniff network communications, and exfiltrate system metadata.

Companies and government institutions in Cambodia, Vietnam, and Mexico are few of the prominent countries affected by DropboxControl, Avast said, adding the authors of the malware are likely different from those behind CLRLoad and PNGLoad owing to "significantly different code quality of these payloads."

Regardless, the deployment of the third-stage implant as a tool to harvest files of interest clearly indicates the intelligence-gathering objectives of Worok, not to mention serves to illustrate an extension to its killchain.

"The prevalence of Worok's tools in the wild is low, so it can indicate that the toolset is an APT project focusing on high-profile entities in private and public sectors in Asia, Africa, and North America," the researchers concluded.

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

[avast](https://thehackernews.com/search/label/avast)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[DLL Side Loading](https://thehackernews.com/search/label/DLL%20Side%20Loading)[dropbox](https://thehackernews.com/search/label/dropbox)[ESET](https://thehackernew...