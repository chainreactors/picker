---
title: GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft
url: https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html
source: The Hacker News
date: 2026-07-17
fetch_date: 2026-07-18T04:46:39.787463
---

# GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft

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

# [GoldenEyeDog Subgroup Linked to DigiCert Breach and Code-Signing Certificate Theft](https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html)

**Ravie Lakshmanan**Jul 17, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixZDZh8TkRVQHu6QNFvHOayTdDxLn-JWDRkPmvVCNkvEL9vhyphenhyphensADIyUB0uXlhXmBhACxMotz-lU1B61HGsRPee80GkLfk-mypQd6Ba4Hr4K-2QCz7BtyRKFCiUYuiUlmPw71Wdn6YnNTjncnGDPQBJV-P0MyS7CjTmPd-p_aHKBCQJr0JA396lL-Yxd3A9/s1700-e365/digicert-hack.jpg)

Cybersecurity researchers have attributed the April 2026 DigiCert security incident to a threat activity cluster dubbed **CylindricalCanine**.

Expel, which shared technical details of the event, described the threat actor as a sub-group of **[GoldenEyeDog](https://ti.qianxin.com/blog/articles/operation-dragon-breath-%28apt-q-27%29-dimensionality-reduction-blow-to-the-gambling-industry/)** (aka APT-Q-27, Dragon Breath, and Miuuti Group), a Chinese cybercrime group known for its [targeting](https://thehackernews.com/2023/05/dragon-breath-apt-group-using-double.html) of the gambling and gaming sectors using counterfeit websites to push malware-laced software. It's known to be active since at least 2015.

"In April 2026, GoldenEyeDog used their malware to access a support member's device at DigiCert, a code-signing certificate provider, and leveraged their access to steal certificates intended for DigiCert customers," Expel security researcher Aaron Walton [said](https://expel.com/blog/introducing-cylindricalcanine/) in an analysis. "This attack highlighted the capability of the malware and operators."

Central to the threat actor's operations is a modified version of [Gh0st RAT](https://thehackernews.com/2025/12/silver-fox-uses-fake-microsoft-teams.html) (aka Farfli), a remote access trojan (RAT) widely used by Chinese hacking groups, including another prolific Chinese cybercrime group tracked as [Silver Fox](https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html). The modular malware, referred to as Golden Gh0st RAT, is delivered by means of Golden Gh0st Loader.

In a report published in November 2025, Elastic Security Labs [detailed](https://thehackernews.com/2025/11/dragon-breath-uses-roningloader-to.html) the adversary's use of a multi-stage loader codenamed RONINGLOADER to distribute a Gh0st RAT variant through NSIS installers masquerading as legitimate programs like Google Chrome and Microsoft Teams.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Earlier this year, another campaign linked to the hacking group was [observed](https://thehackernews.com/2026/03/threatsday-bulletin-pqc-push-ai-vuln.html#apt-targets-web3-support-teams) orchestrating a multi-stage attack directed at customer support staff working for Web3 companies, using suspicious links sent via customer support chat to deliver Gh0st RAT.

"These actors are using malware and targeting victims consistent with other Chinese cybercrime activity, including targeting finance organizations in the Asia-Pacific region," Expel said. "The malware targets finance organizations in the Asia-Pacific region."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiB9gxSgmBWRDYSSuiv6Gtywla5gMEiMHljLTr7hkdMDdy0Ub5j9igWnqjN34jDM3SA0XlNw6fdVxpjgQ8fEaJMkOvjTRPX4xDFnn2CQAdWmD9-SYcNfot_uknyPrqQi46kdXr7gX6GOrFkBYpMpMdogDRu-t64aJG_ylkc5v6UR0pT9SXkQ3Zg2lH3Rzmh/s1700-e365/expel.jpg)

Golden Gh0st RAT shares behavioral and tactical overlaps with a payload [detected](https://mp.weixin.qq.com/s?__biz=MzI2MDc2MDA4OA==&mid=2247490831&idx=1&sn=54def291b6bd573186734895b7ed03b6&poc_token=HPRBWmqj5lsfkGkPbguuxtcdb_nRiKydNweAfJH8) by Chinese security vendor QiAnXin back in 2020 in connection with an attack campaign aimed at the gambling industry since 2019. It also overlaps with a malware documented by ANY.RUN in February 2025 as [Zhong Stealer](https://thehackernews.com/2025/02/new-malware-campaign-uses-cracked.html).

### The DigiCert Compromise

What's more, CylindricalCanine has been [observed](https://x.com/SquiblydooBlog/status/2046190826791870739) abusing code-signing certificates, gaining unauthorized access to DigiCert to intercept code-signing certificates intended for DigiCert customers, and then using them to sign their own malware to avoid detection.

In April 2026, the certificate authority (CA) revealed it revoked certificates fraudulently obtained from its internal support portal after gaining access to two support analyst workstations by executing a malicious payload delivered via a customer chat channel.

"On 2026-04-02, a threat actor contacted DigiCert's support team via a customer chat channel and delivered a ZIP file disguised as a customer screenshot," DigiCert [explained](https://bugzilla.mozilla.org/show_bug.cgi?id=2033170) at the time. "The file contained a .scr executable with a malicious payload."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNwNBadaCcL9DUbXV7L2PSYXlViCjvMWtiT2FZyPUJiFtFFtA-gFcEdGoUnZX4bXupp3bNH9DeyPd7L05OdE0_clOnUkhob6lbksUdnxH09O340DNF6BqlisbcJFZzvepvYIx5Cm36WuwlYyeM5dzdHnetrGDJz_SpW3t_SKuHm8gRPpa-ZklUEwh2YM-L/s1700-e365/breach-digicert.jpg)

"The threat actor used a limited function within the customer-support portal, which allows authenticated DigiCert support analysts to access customer accounts from the customer's perspective to facilitate support tasks. The threat actor was able to use this function to access [initialization codes](https://knowledge.digicert.com/solution/set-up-your-digicert-provided-etoken) for orders that were approved but pending delivery for EV Code Signing certificate orders across a finite set of customer accounts."

The fatal oversight here was that the possession of an initialization code, coupled with an approved order, was "functionally sufficient" to obtain EV Code Signing certificates across a set of ...