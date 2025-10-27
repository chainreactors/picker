---
title: Researchers Uncover 4-Month Cyberattack on U.S. Firm Linked to Chinese Hackers
url: https://thehackernews.com/2024/12/researchers-uncover-4-month-cyberattack.html
source: The Hacker News
date: 2024-12-06
fetch_date: 2025-10-06T19:45:53.273415
---

# Researchers Uncover 4-Month Cyberattack on U.S. Firm Linked to Chinese Hackers

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

# [Researchers Uncover 4-Month Cyberattack on U.S. Firm Linked to Chinese Hackers](https://thehackernews.com/2024/12/researchers-uncover-4-month-cyberattack.html)

**Dec 05, 2024**Ravie LakshmananThreat Intelligence / Cyber Espionage

[![Chinese Hackers](data:image/png;base64... "Chinese Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjG8n5LOH9EpZ2WInLskY3CSsM98nn-RxEVVX4pVGHpAJlOqUj7_REBEYT4IVW7KkEuKC8FzQvRLawjlseV_OoZgKYssHnuO64KS_3WthD2PxwAoL6tdlPzMtN7If9HDIHrJISdQ9DGUF74iEqf22qD6FvluAjO17JVDdj5iP79LTj3iPfiyjGYOfW_usSQ/s790-rw-e365/china.png)

A suspected Chinese threat actor targeted a large U.S. organization earlier this year as part of a four-month-long intrusion.

According to Broadcom-owned Symantec, the first evidence of the malicious activity was detected on April 11, 2024 and continued until August. However, the company doesn't rule out the possibility that the intrusion may have occurred earlier.

"The attackers moved laterally across the organization's network, compromising multiple computers," the Symantec Threat Hunter Team [said](https://symantec-enterprise-blogs.security.com/threat-intelligence/us-china-espionage) in a report shared with The Hacker News.

"Some of the machines targeted were Exchange Servers, suggesting the attackers were gathering intelligence by harvesting emails. Exfiltration tools were also deployed, suggesting that targeted data was taken from the organizations."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The name of the organization that was impacted by the persistent attack campaign was not disclosed, but noted that the victim has a significant presence in China.

The links to China as the potential culprit stem from the use of DLL side-loading, which is a preferred tactic among various Chinese threat groups, and the presence of artifacts previously identified as employed in connection with a state-sponsored operation codenamed [Crimson Palace](https://thehackernews.com/2024/09/experts-identify-3-chinese-linked.html).

Another point of interest is that the organization was targeted in 2023 by an attacker with tentative links to another China-based hacking crew called [Daggerfly](https://thehackernews.com/2024/10/chinese-hackers-use-cloudscout-toolset.html), which is also referred to as Bronze Highland, Evasive Panda, and StormBamboo.

Besides using DLL side-loading to execute malicious payloads, the attack entails the use of open-source tools like FileZilla, Impacket, and PSCP, while also employing living-off-the-land (LotL) programs like Windows Management Instrumentation (WMI), PsExec, and PowerShell.

The exact initial access mechanism used to breach the network remains unknown at this stage. That said, Symantec's analysis has found that the machine on which the earliest indicators of compromise were detected included a command that was run via WMI from another system on the network.

"The fact that the command originated from another machine on the network suggests that the attackers had already compromised at least one other machine on the organization's network and that the intrusion may have begun prior to April 11," the company said.

Some of the other malicious activities that were subsequently performed by the attackers ranged from credential theft and executing malicious DLL files to targeting Microsoft Exchange servers and downloading tools such as FileZilla, PSCP, and WinRAR.

"One group the attackers were particularly interested in is 'Exchange servers,' suggesting the attackers were attempting to target mail servers to collect and possibly exfiltrate email data," Symantec said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as Orange Cyberdefense detailed the private and public relationships within the [Chinese cyber offensive ecosystem](https://intel471.com/blog/a-look-at-trending-chinese-apt-techniques), while also highlighting the role played by [universities for security research](https://thehackernews.com/2024/11/fbi-seeks-public-help-to-identify.html) and hack-for-hire contractors for conducting attacks under the direction of state entities.

"In many instances, individuals linked to the [Ministry of State Security] or [People's Liberation Army] units register fake companies to obscure the attribution of their campaigns to the Chinese state," it [said](https://www.orangecyberdefense.com/global/blog/cert-news/the-hidden-network-how-china-unites-state-corporate-and-academic-assets-for-cyber-offensive-campaigns).

"These fake enterprises, which engage in no real profit-driven activities, may help procure digital infrastructure needed for conducting the cyberattacks without drawing unwanted attention. They also serve as fronts for recruiting personnel for roles that support hacking operations."

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

[china](https://thehackernews.com/search/label/china)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[hacking tool](https://thehack...