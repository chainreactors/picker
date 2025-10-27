---
title: New PHP-Based Interlock RAT Variant Uses FileFix Delivery Mechanism to Target Multiple Industries
url: https://thehackernews.com/2025/07/new-php-based-interlock-rat-variant.html
source: The Hacker News
date: 2025-07-15
fetch_date: 2025-10-06T23:58:29.381953
---

# New PHP-Based Interlock RAT Variant Uses FileFix Delivery Mechanism to Target Multiple Industries

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

# [New PHP-Based Interlock RAT Variant Uses FileFix Delivery Mechanism to Target Multiple Industries](https://thehackernews.com/2025/07/new-php-based-interlock-rat-variant.html)

**Jul 14, 2025**Ravie LakshmananMalware / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibmDtZ91P5aTWYCmIs7_zyT_PqNJlpFhQ1sB5DrkGg8o6i1N9qOrRsYtNwhyphenhyphen4n3n3NAWsosune4VioGVm-Ana81idhFQXqwwFRHKu0jiR_9pod1_z9Iw-xY8G58Wdo0bKDBWJ32mpw42ryE5_r9nKJYKdzs4VsKH7rUWPuUd8BXhpCrXqHn8_iqF5F_GxA/s790-rw-e365/click.jpg)

Threat actors behind the Interlock ransomware group have unleashed a new PHP variant of its bespoke remote access trojan (RAT) as part of a widespread campaign using a variant of ClickFix called FileFix.

"Since May 2025, activity related to the Interlock RAT has been observed in connection with the [LandUpdate808](https://thehackernews.com/2025/06/anubis-ransomware-encrypts-and-wipes.html) (aka KongTuke) web-inject threat clusters," The DFIR Report [said](https://thedfirreport.com/2025/07/14/kongtuke-filefix-leads-to-new-interlock-rat-variant/) in a technical analysis published today in collaboration with Proofpoint.

"The campaign begins with compromised websites injected with a single-line script hidden in the page's HTML, often unbeknownst to site owners or visitors."

The JavaScript code acts as a traffic distribution system (TDS), using IP filtering techniques to redirect users to fake CAPTCHA verification pages that leverage ClickFix to entice them into running a PowerShell script that leads to the deployment of NodeSnake (aka Interlock RAT or [Supper](https://c-b.io/2025-06-29%2B-%2BSupper%2Bis%2Bserved)).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The use of NodeSnake by Interlock was [previously documented](https://thehackernews.com/2025/06/former-black-basta-members-use.html) by Quorum Cyber as part of cyber attacks targeting local government and higher education organizations in the United Kingdom in January and March 2025. The malware facilitates persistent access, system reconnaissance, and remote command execution capabilities.

While the name of the malware is a reference to its Node.js foundations, new campaigns observed last month have led to the distribution of a PHP variant by means FileFix. The activity is assessed to be opportunistic in nature, aiming for a broad range of industries.

"This updated delivery mechanism has been observed deploying the PHP variant of the Interlock RAT, which in certain cases has then led to the deployment of the Node.js variant of the Interlock RAT," the researchers said.

FileFix is an evolution of ClickFix that takes advantage of the Windows operating system's ability to instruct victims into copying and executing commands using the File Explorer's address bar feature. It was first [detailed](https://thehackernews.com/2025/06/new-filefix-method-emerges-as-threat.html) as a proof-of-concept (PoC) last month by security researcher mrd0x.

Once installed, the RAT malware carries out reconnaissance of the infected host and exfiltrate system information in JSON format. It also checks its own privileges to determine if it's being run as USER, ADMIN, or SYSTEM, and establishes contact with a remote server to download and run EXE or DLL payloads.

Persistence on the machine is accomplished via Windows Registry changes, while the Remote Desktop Protocol (RDP) is used to enable lateral movement.

A noteworthy feature of the trojan is its abuse of [Cloudflare Tunnel subdomains](https://thehackernews.com/2025/06/new-malware-campaign-uses-cloudflare.html) to obscure the true location of the command-and-control (C2) server. The malware further embeds hard-coded IP addresses as a fallback mechanism so as to ensure that the communication remains intact even if the Cloudflare Tunnel is taken down.

"This discovery highlights the continued evolution of the Interlock group's tooling and their operational sophistication," the researchers said. "While the Node.js variant of Interlock RAT was known for its use of Node.js, this variant leverages PHP, a common web scripting language, to gain and maintain access to victim networks."

### Threat Actors Join the FileFix Exploitation Bandwagon

Cybersecurity firm Check Point, in an analysis published on July 16, 2025, said it has observed cybercriminals actively testing the FileFix attack method for future malware distribution. This includes a threat actor that's known for leveraging the ClickFix technique to propagate malware loaders, remote access Trojans (RATs), and information stealers.

"This threat actor has a history of targeting users of major cryptocurrency exchanges and other legitimate services," the company [said](https://blog.checkpoint.com/research/filefix-the-new-social-engineering-attack-building-on-clickfix-tested-in-the-wild). "Their primary lure technique is SEO poisoning, which involves manipulating search engine results to promote malicious sites to the top."

While the FileFix tests so far use benign payloads, the development signals an imminent shift to delivering real malware, underscoring how threat actors are swiftly incorporating new attack methods into their arsenal.

Check Point noted that FileFix is stealthier than ClickFix, as it weaponizes user trust in everyday Windows actions, such as opening Windows File Explorer, to execute harmful code without raising any suspicion.

"Threat actors began using FileFix less than two weeks after it was published, showing just how quickly cyber criminals adapt," Eli Smadja, Group Manager of Security Research at Check Point Software Technologies, said in a statement.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Like ClickFix, this technique doesn't rely on complex exploits, but on manipulating routine user behavior. By shifting from the Run dialog to File Explorer, attackers are now hiding in plain sight, making detection harder and the threat...