---
title: China-Linked CeranaKeeper Targeting Southeast Asia with Data Exfiltration
url: https://thehackernews.com/2024/10/china-linked-ceranakeeper-targeting.html
source: The Hacker News
date: 2024-10-03
fetch_date: 2025-10-06T18:55:59.430926
---

# China-Linked CeranaKeeper Targeting Southeast Asia with Data Exfiltration

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

# [China-Linked CeranaKeeper Targeting Southeast Asia with Data Exfiltration](https://thehackernews.com/2024/10/china-linked-ceranakeeper-targeting.html)

**Oct 02, 2024**Ravie LakshmananCyber Espionage / Cloud Security

[![Data Exfiltration](data:image/png;base64... "Data Exfiltration")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIm4nR9-Ey_LMAKdmk2FDEbQyEWQmmcERixyaYQxLA4EcwISk0GHUxvH67ILILJct59dd65xKWqTdXRNV0jm4a_gqiQ1e__IYdWYTEtbOmmq7QzjM7vKmU7QBLXpDGDe4BrH6Q-uuEdgoUoGezhjcYV2euex-1Xjlq5OX78beXixhHquY7W599tG31ZZ4P/s790-rw-e365/chinese-hackers.png)

A previously undocumented threat actor called **CeranaKeeper** has been linked to a string of data exfiltration attacks targeting Southeast Asia.

Slovak cybersecurity firm ESET, which observed campaigns targeting governmental institutions in Thailand starting in 2023, attributed the activity cluster as aligned to China, leveraging tools previously identified as used by the [Mustang Panda](https://thehackernews.com/2024/09/mustang-panda-deploys-advanced-malware.html) actor.

"The group constantly updates its backdoor to evade detection and diversifies its methods to aid massive data exfiltration," security researcher Romain Dumont [said](https://www.welivesecurity.com/en/eset-research/separating-bee-panda-ceranakeeper-making-beeline-thailand/) in an analysis published today.

"CeranaKeeper abuses popular, legitimate cloud and file-sharing services such as Dropbox and OneDrive to implement custom backdoors and extraction tools."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the other countries targeted by the adversary include Myanmar, the Philippines, Japan, and Taiwan, all of which have been targeted by Chinese state-sponsored threat actors in recent years.

ESET described CeranaKeeper as relentless, creative, and capable of swiftly adapting its modus operandi, while also calling it aggressive and greedy for its ability to move laterally across compromised environments and hoover as much information as possible via various backdoors and exfiltration tools.

"Their extensive use of wildcard expressions for traversing, sometimes, entire drives clearly showed their aim was massive data siphoning," the company said.

The exact initial access routes employed by the threat actor remain unknown as yet. However, a successful initial foothold is abused to gain access to other machines on the local network, even turning some of the compromised machines into proxies or update servers to store updates for their backdoor.

The attacks are characterized by the use of malware families such as TONESHELL, TONEINS, and PUBLOAD – all [attributed](https://thehackernews.com/2022/11/chinese-mustang-panda-hackers-actively.html) to the [Mustang Panda](https://thehackernews.com/2023/09/new-report-uncovers-three-distinct.html) group – while also making use of an arsenal of never-before-seen tools to aid data exfiltration.

"After gaining privileged access, the attackers installed the TONESHELL backdoor, deployed a tool to dump credentials, and used a legitimate Avast driver and a custom application to disable security products on the machine," Dumont said.

"From this compromised server, they used a remote administration console to deploy and execute their backdoor on other computers in the network. Additionally, CeranaKeeper used the compromised server to store updates for TONESHELL, turning it into an update server."

The newly discovered custom toolset is as follows -

* WavyExfiller - A Python uploader that harvests data, including connected devices like USBs and hard drives, and uses Dropbox and PixelDrain as exfiltration endpoints

* DropboxFlop - A Python DropboxFlop that's a variant of a publicly-available reverse shell called [DropFlop](https://github.com/pauln23/DropFlop/tree/master) that comes with upload and download features and uses Dropbox as a command-and-control (C&C) server

* OneDoor - A C++ backdoor that abuses [Microsoft OneDrive REST API](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/) to receive commands and exfiltrate files

* BingoShell - A Python backdoor that abuses GitHub's pull request and issues comment features to create a stealthy reverse shell

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"From a high-level point of view, [BingoShell] leverages a private GitHub repository as a C&C server," ESET explained. "The script uses a hard-coded token to authenticate and the pull requests and issues comments features to receive commands to execute and send back the results."

Calling out CeranaKeeper's ability to quickly write and rewrite its toolset as required to evade detection, the company said the threat actor's end goal is to develop bespoke malware that can allow it to collect valuable information on a large scale.

"Mustang Panda and CeranaKeeper seem to operate independently of each other, and each has its own toolset," it said. "Both threat actors may rely on the same third party, such as a digital quartermaster, which is not uncommon among China-aligned groups, or have some level of information sharing, which would explain the links that have been observed."

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Mes...