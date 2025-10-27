---
title: Researchers Expose NonEuclid RAT Using UAC Bypass and AMSI Evasion Techniques
url: https://thehackernews.com/2025/01/researchers-expose-noneuclid-rat-using.html
source: The Hacker News
date: 2025-01-09
fetch_date: 2025-10-06T20:14:51.253753
---

# Researchers Expose NonEuclid RAT Using UAC Bypass and AMSI Evasion Techniques

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

# [Researchers Expose NonEuclid RAT Using UAC Bypass and AMSI Evasion Techniques](https://thehackernews.com/2025/01/researchers-expose-noneuclid-rat-using.html)

**Jan 08, 2025**The Hacker NewsMalware / Windows Security

[![Evasion Techniques](data:image/png;base64... "Evasion Techniques")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8k_A0Bhb1RQBbWChY1Qe6gwlEOBNoM25mqrPs9qNpOS47qrnKQawCucEGVKZSOSlFXraAeU3RUy1jPucIe8KNcUK0yLyhkV7XR8NzKtgiiZMS9MEAeSBSd7qe8p7p-xXvE4VJ8PX5O6z2pSEpZ8yjnFJJJXcA5NlBXPGa09F-xZabijG3OUZt3dh6lL8/s790-rw-e365/malware.png)

Cybersecurity researchers have shed light on a new remote access trojan called **NonEuclid** that allows bad actors to remotely control compromised Windows systems.

"The NonEuclid remote access trojan (RAT), developed in C#, is a highly sophisticated malware offering unauthorised remote access with advanced evasion techniques," Cyfirma [said](https://www.cyfirma.com/research/noneuclid-rat/) in a technical analysis published last week.

"It employs various mechanisms, including antivirus bypass, privilege escalation, anti-detection, and ransomware encryption targeting critical files."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

NonEuclid has been advertised in underground forums since at least late November 2024, with tutorials and discussions about the malware discovered on popular platforms like Discord and YouTube. This points to a concerted effort to distribute the malware as a crimeware solution.

At its core, the RAT commences with an initialization phase for a client application, after which it performs a series of checks to evade detection prior to setting up a TCP socket for communication with a specified IP and port.

It also configures Microsoft Defender Antivirus exclusions to prevent the artifacts from being flagged by the security tool, and keeps tabs on processes like "taskmgr.exe," "processhacker.exe," and "procexp.exe" which are often used for analysis and process management.

"It uses Windows API calls (CreateToolhelp32Snapshot, Process32First, Process32Next) to enumerate processes and check if their executable names match the specified targets," Cyfirma said. "If a match is found, depending on the AntiProcessMode setting, it either kills the process or triggers an exit for the client application."

[![NonEuclid RAT](data:image/png;base64... "NonEuclid RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlXNr-7pJyGIbjmj3g1yiQmemw5vjRT_jTIooh1ETVyYZPHm5ZhIDkGgIwEI7bsys4kma0t1Qyv2HpamzXd7m3VXTyIyEhjaMYFufui4gSm9Bl5PSGiYX6kymCDf4xWpDuWGMilpLhIJ0PELML15yrDpuO9GPocK2roeb7_FzLTOtEb-ZTmipKGF9H3tI/s790-rw-e365/rat02-16.jpg)

Some of the anti-analysis techniques adopted by the malware include checks to determine if it's running in a virtual or sandboxed environment, and if found to be so, immediately terminate the program. Furthermore, it incorporates features to bypass the Windows Antimalware Scan Interface ([AMSI](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)).

While persistence is accomplished by means of scheduled tasks and Windows Registry changes, NonEuclid also attempts to elevate privileges by circumventing User Account Control (UAC) protections and execute commands.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A relatively uncommon feature is its ability to encrypt files matching certain extension types (e.g., .CSV, .TXT, and .PHP) and renaming them with the extension ". NonEuclid," effectively turning into ransomware.

"The NonEuclid RAT exemplifies the increasing sophistication of modern malware, combining advanced stealth mechanisms, anti-detection features, and ransomware capabilities," Cyfirma said.

"Its widespread promotion across underground forums, Discord servers, and tutorial platforms demonstrates its appeal to cyber-criminals and highlights the challenges in combating such threats. The integration of features like privilege escalation, AMSI bypass, and process blocking showcases the malware's adaptability in evading security measures."

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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

[Antivirus](https://thehackernews.com/search/label/Antivirus)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[ransomware](https://thehackernews.com/search/label/ransomware)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-conte...