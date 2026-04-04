---
title: China-Linked TA416 Targets European Governments with PlugX and OAuth-Based Phishing
url: https://thehackernews.com/2026/04/china-linked-ta416-targets-european.html
source: The Hacker News
date: 2026-04-03
fetch_date: 2026-04-04T04:17:50.012582
---

# China-Linked TA416 Targets European Governments with PlugX and OAuth-Based Phishing

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [China-Linked TA416 Targets European Governments with PlugX and OAuth-Based Phishing](https://thehackernews.com/2026/04/china-linked-ta416-targets-european.html)

**Ravie Lakshmanan**Apr 03, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgi-dKCldJqtZI1CocMVxHNKusU5tcnMKjx7mzG9EfehvGacnTy4tsTfZLMfhyphenhyphenC5W210OxrxijBNAP8UumXAZH15ZSOM4x8xb9VTIHxN1HCouzROU0pn7sCJki9zJOkk9_8SRns73KxO1KvxUY4YgKGbbme6ZcKdbt4cqSHUkG5WQQPgDDTx_OLRbms35Dv/s1700-e365/chinese-hackers.jpg)

A China-aligned threat actor has set its sights on European government and diplomatic organizations since mid-2025, following a two-year period of minimal targeting in the region.

The campaign has been attributed to **[TA416](https://thehackernews.com/2025/01/reddelta-deploys-plugx-malware-to.html)**, a cluster of activity that overlaps with DarkPeony, RedDelta, Red Lich, SmugX, UNC6384, and Vertigo Panda.

"This TA416 activity included multiple waves of web bug and malware delivery campaigns against diplomatic missions to the European Union and NATO across a range of European countries," Proofpoint researchers Mark Kelly and Georgi Mladenov [said](https://www.proofpoint.com/us/blog/threat-insight/id-come-running-back-eu-again-ta416-resumes-european-government-espionage).

"Throughout this period, TA416 regularly altered its infection chain, including abusing Cloudflare Turnstile challenge pages, abusing OAuth redirects, and using C# project files, as well as frequently updating its custom PlugX payload."

TA416 has also been observed orchestrating multiple campaigns aimed at diplomatic and government entities in the Middle East following the outbreak of the U.S.-Israel-Iran conflict in late February 2026. The effort is likely an attempt to gather regional intelligence pertaining to the conflict, the enterprise security company added.

It's worth mentioning here that TA416 also shares historical technical overlaps with another cluster known as [Mustang Panda](https://thehackernews.com/2026/03/three-china-linked-clusters-target.html) (aka CerenaKeeper, Red Ishtar, and UNK\_SteadySplit). The two activity groups are collectively tracked under the monikers Earth Preta, Hive0154, HoneyMyte, Stately Taurus, Temp.HEX, and Twill Typhoon.

While TA416's attacks are characterized by the use of bespoke PlugX variants, the Mustang Panda cluster has repeatedly deployed tools like TONESHELL, PUBLOAD, and COOLCLIENT in recent attacks. What's common to both of them is the use of DLL side-loading to launch the malware.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

TA416's renewed focus on European entities is driven a mix of web bug and malware delivery campaigns, with the threat actors using freemail sender accounts to conduct reconnaissance and deploy the PlugX backdoor via malicious archives hosted on Microsoft Azure Blob Storage, Google Drive, domains under their control, and compromised SharePoint instances. The PlugX malware campaigns were previously documented by [StrikeReady](https://thehackernews.com/2025/10/from-healthkick-to-govershell-evolution.html) and [Arctic Wolf](https://thehackernews.com/2025/10/china-linked-hackers-exploit-windows.html) in October 2025.

"A web bug (or tracking pixel) is a tiny invisible object embedded in an email that triggers an HTTP request to a remote server when opened, revealing the recipient's IP address, user agent, and time of access, allowing the threat actor to assess whether the email was opened by the intended target," Proofpoint said.

Attacks carried out by TA416 in December 2025 have been found to leverage third-party Microsoft Entra ID cloud applications to initiate redirects that lead to the download of malicious archives. Phishing emails used as part of this attack wave contain a link to Microsoft's legitimate [OAuth](https://www.wiz.io/blog/detecting-malicious-oauth-applications) authorization endpoint that, when clicked, redirects the user to the attacker-controlled domain and ultimately deploys PlugX.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8WUad_W3hN7-F9zcLmhAA3PyWa1DzcPEQUiREMVI2hYG4YY1vS32SlatDnFBBhV2UckTMlU9UzQ9nkiagFFRYLOsLNthz22QDLPEsbiM35Bdxq5JZDkSQ_Pxga46Uxn0ok_EXo-j5kY2bbmIOrvVom-E-ZEfqf9Zx3b6S0eEzEz97wFqPKEgKHjjCn-RR/s1700-e365/map.png)

The use of this technique has not escaped Microsoft's notice, which last month [warned](https://thehackernews.com/2026/03/microsoft-warns-oauth-redirect-abuse.html) of phishing campaigns targeting government and public-sector organizations that employ OAuth URL redirection mechanisms to bypass conventional phishing defenses implemented in email and browsers.

Further refinements to the attack chain were observed in February 2026, when TA416 began linking to archives hosted on Google Drive or a compromised SharePoint instance. The downloaded archives, in this case, include a legitimate Microsoft MSBuild executable and a malicious C# project file.

"When the MSBuild executable is run, it searches the current directory for a project file and automatically builds it," the researchers said. "In the observed TA416 activity, the CSPROJ file acts as a downloader, decoding three Base64-encoded URLs to fetch a DLL side-loading triad from a TA416-controlled domain, saving them to the user's temp directory, and executing a legitimate executable to load PlugX via the group's typical DLL side-loading chain."

The PlugX malware remains a consistent presence throughout TA416's intrusions, although the legitimate, signed executables abused for DLL side-loading have varied over time. The backdoor is also known to establish an encrypted communication channel with its command-and-control (C2) server, but not before performing anti-analysis checks to sidestep detection.

PlugX accepts five different commands -

* **0x00000002**, to capture system information
* **0x000010...