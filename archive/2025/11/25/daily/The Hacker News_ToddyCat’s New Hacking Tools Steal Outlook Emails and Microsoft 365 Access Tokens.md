---
title: ToddyCat’s New Hacking Tools Steal Outlook Emails and Microsoft 365 Access Tokens
url: https://thehackernews.com/2025/11/toddycats-new-hacking-tools-steal.html
source: The Hacker News
date: 2025-11-25
fetch_date: 2025-11-26T03:17:15.611191
---

# ToddyCat’s New Hacking Tools Steal Outlook Emails and Microsoft 365 Access Tokens

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [ToddyCat's New Hacking Tools Steal Outlook Emails and Microsoft 365 Access Tokens](https://thehackernews.com/2025/11/toddycats-new-hacking-tools-steal.html)

**Nov 25, 2025**Ravie LakshmananMalware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNpga80w98u9OErGtSp29H9OnZOEqxJ6f5M0tMxrFaWffBBWGE4K8AS6vy1-WEB5f0_L-lUaQGvY_b4YVdEq9fukFedxw18lq0C8p2IsM9-cZ51Jk4fP0hyphenhyphenCIt7KmoNjqVU1CVBUcUeqy_abUgacC0aWHUaOTpKBJ2iLc3zZvhD3TMJQ5ccBBcckpsHerD/s790-rw-e365/dc.jpg)

The threat actor known as **ToddyCat** has been observed adopting new methods to obtain access to corporate email data belonging to target companies, including using a custom tool dubbed TCSectorCopy.

"This attack allows them to obtain tokens for the OAuth 2.0 authorization protocol using the user's browser, which can be used outside the perimeter of the compromised infrastructure to access corporate mail," Kaspersky [said](https://securelist.ru/toddycat-apt-steals-email-data-from-outlook/114045/) in a technical breakdown.

ToddyCat, assessed to be active since 2020, has a [track record](https://thehackernews.com/2024/04/russian-hacker-group-toddycat-uses.html) of targeting various organizations in Europe and Asia with various tools, Samurai and TomBerBil to retain access and steal cookies and credentials from web browsers like Google Chrome and Microsoft Edge.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

Earlier this April, the hacking group was [attributed](https://thehackernews.com/2025/04/new-tcesb-malware-found-in-active.html) to the exploitation of a security flaw in ESET Command Line Scanner (CVE-2024-11859, CVSS score: 6.8) to deliver a previously undocumented malware codenamed TCESB.

Kaspersky said it detected in attacks that took place between May and June 2024 a PowerShell variant of TomBerBil (as opposed to C++ and C# versions flagged before), which comes with capabilities to extract data from Mozilla Firefox. A notable feature of this version is that it runs on domain controllers from a privileged user and can access browser files via shared network resources using the SMB protocol.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgg_ZUsMZTqebH2nUZggC1nzEGmJX_tVt0DpUtfuEKHqWtLdEAudHJizWrlWk8ST3Ter00nFEJUut3ekJKpdiDzVVjGDVwvmgBilsiKGYdgJwQeD2KrYXR4liC-MAfLi180YnJiWH1Ph20_ySdQ5yMoTvnjRxRO8ujtvdLiZN71ixL5EKqTF4GFK-6BAHg/s790-rw-e365/dc-2.png)

The malware, the company added, was launched by means of a scheduled task that executed a PowerShell command. Specifically, it searches for browser history, cookies, and saved credentials in the remote host over SMB. While the copied files containing the information are encrypted using the Windows Data Protection API ([DPAPI](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)), TomBerBil is equipped to capture the encryption key necessary to decrypt the data.

"The previous version of TomBerBil ran on the host and copied the user token. As a result, DPAPI was used to decrypt the master key in the user's current session, and subsequently the files themselves," researchers said. "In the newer server version, TomBerBil copies files containing user encryption keys that are used by DPAPI. Using these keys, as well as the user's SID and password, attackers can decrypt all copied files locally."

The threat actors have also been found to access corporate emails stored in local Microsoft Outlook storage in the form of OST (short for Offline Storage Table) files using TCSectorCopy ("xCopy.exe"), bypassing restrictions that limit access to such files when the application is running.

Written in C++, TCSectorCopy accepts as input a file to be copied (in this case, OST files) and then proceeds to open the disk as a read-only device and sequentially copy the file contents sector by sector. Once the OST files are written to a path of the attacker's choosing, the contents of the electronic correspondence are extracted using [XstReader](https://github.com/Dijji/XstReader), an open-source viewer for Outlook OST and PST files.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Another tactic adopted by ToddyCat involves efforts to obtain access tokens directly from memory in cases where victim organizations used the Microsoft 365 cloud service. The JSON web tokens (JWTs) are obtained through an open-source C# tool named [SharpTokenFinder](https://github.com/HuskyHacks/SharpTokenFinder), which enumerates Microsoft 365 applications for plain text authentication tokens.

But the threat actor is said to have faced a setback in at least one investigated incident after security software installed on the system blocked SharpTokenFinder's attempt to dump the Outlook.exe process. To get around this restriction, the operator used the [ProcDump](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump) tool from the Sysinternals package with specific arguments to take a memory dump of the Outlook process.

"The ToddyCat APT group is constantly developing its techniques and looking for those that would hide activity to gain access to corporate correspondence within the compromised infrastructure," Kaspersky said.

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
[![F...