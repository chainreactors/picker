---
title: OneDrive Phishing Scam Tricks Users into Running Malicious PowerShell Script
url: https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html
source: The Hacker News
date: 2024-07-31
fetch_date: 2025-10-06T17:47:05.172338
---

# OneDrive Phishing Scam Tricks Users into Running Malicious PowerShell Script

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

# [OneDrive Phishing Scam Tricks Users into Running Malicious PowerShell Script](https://thehackernews.com/2024/07/onedrive-phishing-scam-tricks-users.html)

**Jul 30, 2024**Ravie LakshmananMalware / Email Security

[![PowerShell Script](data:image/png;base64... "PowerShell Script")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEix0XfsY-0wZPr2_Yi8a79zevrySzlxI-CwIdApE5nY6G6aNV8Lk1XHnBZeco3n1ZZ6-rUMXMXgDbSxMu1tXg3yEi119jW178oCBRpxPPSVPXExJuJaCPvuLXI1pe6fj8Q6Xgzzwmat54qjDcTSOEuQUtqfOKQbhGS0EBHQjHDXjzeMuPoqK3saYMjm2att/s790-rw-e365/windws.png)

Cybersecurity researchers are warning about a new phishing campaign that targets Microsoft OneDrive users with the aim of executing a malicious PowerShell script.

"This campaign heavily relies on social engineering tactics to deceive users into executing a PowerShell script, thereby compromising their systems," Trellix security researcher Rafael Pena [said](https://www.trellix.com/blogs/research/onedrive-pastejacking/) in a Monday analysis.

The cybersecurity company is tracking the "crafty" phishing and downloader campaign under the name OneDrive Pastejacking.

The attack unfolds via an email containing an HTML file that, when opened, displays an image simulating an OneDrive page and includes the error message that says: "Failed to connect to the 'OneDrive' cloud service. To fix the error, you need to update the DNS cache manually."

The message also comes with two options, namely "How to fix" and "Details," with the latter directing the email recipient to a legitimate Microsoft Learn page on Troubleshooting DNS.

However, clicking "How to fix" prompts the user to follow a series of steps, which includes pressing "Windows Key + X" to open the Quick Link menu, launching the PowerShell terminal, and pasting a Base64-encoded command to supposedly fix the issue.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The command [...] first runs ipconfig /flushdns, then creates a folder on the C: drive named 'downloads,'" Pena explained. "Subsequently, it downloads an archive file into this location, renames it, extracts its contents ('script.a3x' and 'AutoIt3.exe'), and executes script.a3x using AutoIt3.exe."

The campaign has been observed targeting users in the U.S., South Korea, Germany, India, Ireland, Italy, Norway, and the U.K.

The disclosure builds upon similar findings from [ReliaQuest, Proofpoint](https://thehackernews.com/2024/06/cybercriminals-exploit-free-software.html), and [McAfee Labs](https://thehackernews.com/2024/07/spanish-hackers-bundle-phishing-kits.html), indicating that phishing attacks employing this technique – also tracked as ClickFix – are becoming increasingly prevalent.

The development comes amid the discovery of a new email-based social engineering campaign [distributing](https://www.threatdown.com/blog/new-phishing-campaign-uses-discord-for-payload-delivery/) bogus Windows shortcut files that lead to the execution of malicious payloads hosted on Discord's Content Delivery Network (CDN) infrastructure.

[![PowerShell Script](data:image/png;base64... "PowerShell Script")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg5g-UcU9N8sEdX7_-01ZrxRfkiJhyphenhyphenXbOrPP08xPaHfGeWPfv1PGscyzyiNvI3tuop-XLoCWMgZuou_dpVCIwScfBWwcsMLMcmBCchPhAV9Lz1S-upMbY8DD79BnClbDQRhJX3zJURJQNrkk3Fl51ERKHT0agdtrRTupvm5-9G1cuykUllcmqq7nVDEsyY/s790-rw-e365/pp.png)

Phishing campaigns have also been increasingly observed sending emails containing links to Microsoft Office Forms from previously compromised legitimate email accounts to entice targets into divulging their Microsoft 365 login credentials under the pretext of restoring their Outlook messages.

"Attackers create legitimate-looking forms on Microsoft Office Forms, embedding malicious links within the forms," Perception Point [said](https://perception-point.io/blog/two-step-phishing-campaign-exploits-microsoft-office-forms/). "These forms are then sent to targets en-masse via email under the guise of legitimate requests such as changing passwords or accessing important documents, mimicking trusted platforms and brands like Adobe or Microsoft SharePoint document viewer."

What's more, other attack waves have [utilized](https://www.forcepoint.com/blog/insights/threat-actors-harvesting-credentials-telegram-api) invoice-themed lures to trick victims to sharing their credentials on phishing pages hosted on [Cloudflare R2](https://thehackernews.com/2023/08/cybercriminals-abusing-cloudflare-r2.html) that are then exfiltrated to the threat actor via a Telegram bot.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's no surprise that adversaries are constantly on the lookout for [different ways](https://thehackernews.com/2024/07/proofpoint-email-routing-flaw-exploited.html) to stealthily smuggle malware past Secure Email Gateways (SEGs) so as to increase the likelihood of success of their attacks.

According to a recent report from Cofense, bad actors are abusing how SEGs scan ZIP archive attachments to deliver the [Formbook](https://thehackernews.com/2023/08/new-variant-of-xloader-macos-malware.html) information stealer by means of [DBatLoader](https://thehackernews.com/2023/03/stealthy-dbatloader-malware-loader.html) (aka ModiLoader and NatsoLoader).

Specifically, this involves passing off the HTML payload as an MPEG file to evade detection by taking advantage of the fact that many common archive extractors and SEGs parse the file header information but ignore the file footer that may contain more accurate information about the file format.

"The threat actors utilized a .ZIP archive attachment and when the SEG scanned the file contents, the archive was detected as containing a .MPEG video file and was not blocked or filtered," the company [noted](https://cofense.com/blog/malware-exploit-bypasses-segs-leaving-organizations-at-risk/).

"When this attachment was opened with common/popular archive extraction tools such as 7-Zip ...