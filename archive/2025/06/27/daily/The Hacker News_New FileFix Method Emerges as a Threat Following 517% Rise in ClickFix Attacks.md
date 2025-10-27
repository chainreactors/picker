---
title: New FileFix Method Emerges as a Threat Following 517% Rise in ClickFix Attacks
url: https://thehackernews.com/2025/06/new-filefix-method-emerges-as-threat.html
source: The Hacker News
date: 2025-06-27
fetch_date: 2025-10-06T22:57:07.791497
---

# New FileFix Method Emerges as a Threat Following 517% Rise in ClickFix Attacks

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

# [New FileFix Method Emerges as a Threat Following 517% Rise in ClickFix Attacks](https://thehackernews.com/2025/06/new-filefix-method-emerges-as-threat.html)

**Jun 26, 2025**Ravie LakshmananCyber Attack / Malware Analysis

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh29mMZPN4Ikh93mdJPT-KI3hsUemB2ds1p4Cat2MAfbRV8pan97BHRnUw4CG0Qkk8TC-w6aU5FyXbO2ziRnPxURdzAxVaDvjFQGx6idDozOD5IBXgWbzlXmL4ZJjcJ8EYjxlKK2q9oZ5F0eN9QQo2yEawrwBoKLCf3ENqc4NknAXKZkOS2neqLFlukysMR/s790-rw-e365/clickfix.jpg)

The ClickFix social engineering tactic as an initial access vector using fake CAPTCHA verifications increased by 517% between the second half of 2024 and the first half of this year, according to data from ESET.

"The list of threats that ClickFix attacks lead to is growing by the day, including infostealers, ransomware, remote access trojans, cryptominers, post-exploitation tools, and even custom malware from nation-state-aligned threat actors," Jiří Kropáč, Director of Threat Prevention Labs at ESET, [said](https://www.welivesecurity.com/en/eset-research/eset-threat-report-h1-2025/).

ClickFix has [become](https://thehackernews.com/2025/03/microsoft-warns-of-clickfix-phishing.html) a [widely popular](https://thehackernews.com/2025/04/state-sponsored-hackers-weaponize.html) and [deceptive method](https://thehackernews.com/2025/04/ransomhub-went-dark-april-1-affiliates.html) that employs bogus error messages or CAPTCHA verification checks to entice victims into copying and pasting a malicious script into either the Windows Run dialog or the Apple macOS Terminal app, and running it.

The Slovak cybersecurity company said the highest volume of ClickFix detections are concentrated around Japan, Peru, Poland, Spain, and Slovakia.

The prevalence and effectiveness of this attack method have led to threat actors [advertising](https://www.virusbulletin.com/conference/vb2025/abstracts/you-definitely-dont-want-copypaste-fakecaptcha-ecosystem/) builders that provide other attackers with ClickFix-weaponized landing pages, ESET added.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiDFrZgkFu-xrVo4ALRNHBH-rjSelOeXAi5vJj4g5_dF0Imx5_SGDvwrkIT8k4H6Xvw4uq6qGrr5bVPbzbxEq-kMYL4UxPjfW6rj1Ow5Kr3dvSoyA7P6E0KOFotpMETUTx8Kuyme3PFZ0R9M7s2nwNxq00tyx9auDl-poyUocC1WNRUpQHs6hjUOwVUcUj/s790-rw-e365/eset.jpg)

### From ClickFix to FileFix

The development comes as security researcher [mrd0x](https://thehackernews.com/2022/03/new-browser-in-browser-bitb-attack.html) [demonstrated](https://mrd0x.com/filefix-clickfix-alternative/) a proof-of-concept (PoC) alternative to ClickFix named FileFix that works by tricking users into copying and pasting a file path into Windows File Explorer.

The technique essentially involves achieving the same as ClickFix but in a different manner by combining File Explorer's ability to execute operating system commands through the address bar with a web browser's file upload feature.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In the attack scenario devised by the researcher, a threat actor may devise a phishing page that, instead of displaying a fake CAPTCHA check to the prospective target, presents a message stating a document has been shared with them and that they need to copy and paste the file path on the address bar by pressing CTRL + L.

The phishing page also includes a prominent "Open File Explorer" that, upon clicking, opens the File Explorer and copies a malicious PowerShell command to the user's clipboard. Thus, when the victim pastes the "file path," the attacker's command is executed instead.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiA2sUGzyUOIi4LX2BRWMi64RDSBoZpeesL9m_DzfvYJMHp2hsPEzJx5m65BLrAQcghHLVtf4p2TVnyvULd8sbKW9P0v3cagNUM3eXnPiVE78RmulmI1WO_vpXR8Hb-Fj6cf3cuKH529-hfF2oymZTvK3LW1MoXmvu8sPNetyr5i9iqdwGF8lRi3VLOKvr/s790-rw-e365/filefix.gif)

This, in turn, is achieved by altering the copied file path to prepend the PowerShell command before it followed by adding spaces to hide it from view and a pound sign ("#") to treat the fake file path as a comment: "*Powershell.exe -c ping example.com<space># C:\\<path\_to\_file>\\decoy.doc*"

"Additionally, our PowerShell command will concatenate the dummy file path after a comment in order to hide the command and show the file path instead," mrd0x said.

### Phishing Campaigns Galore

The surge in ClickFix campaigns also coincides with the discovery of various phishing campaigns in recent weeks that -

* Leverage a .gov domain to [send phishing emails](https://cofense.com/blog/txtag-takedown-busting-phishing-email-schemes) that masquerade as unpaid toll to take users to bogus pages that are designed to collect their personal and financial information
* Make use of long-lived domains (LLDs), a technique called [strategic domain aging](https://thehackernews.com/2023/05/new-decoy-dog-malware-toolkit-uncovered.html), to [either host or use them to redirect users](https://cofense.com/blog/immunity-evasion-defeating-security-with-active-measures-long-lived-domains) to custom CAPTCHA check pages, completing which they are led to spoofed Microsoft Teams pages to steal their Microsoft account credentials
* Distribute [malicious Windows shortcut (LNK) files](https://www.forcepoint.com/blog/x-labs/remcos-malware-new-face) within ZIP archives to launch PowerShell code responsible for deploying Remcos RAT
* Employ lures which supposedly [warn users that their mailbox is almost full](https://www.forcepoint.com/blog/x-labs/phishing-malware-combo-threat) and that they need to "clear storage" by clicking a button embedded in the message, performing which takes the user to a phishing page hosted on [IPFS](https://thehackernews.com/2022/07/researchers-warns-of-increase-in.html) that steals users email credentials. Interestingly, the emails also include a RAR archive attachment that, once extracted and executed, drops...