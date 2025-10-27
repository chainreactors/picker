---
title: Hackers Using Cracked Software on GitHub to Spread RisePro Info Stealer
url: https://thehackernews.com/2024/03/hackers-using-cracked-software-on.html
source: The Hacker News
date: 2024-03-17
fetch_date: 2025-10-04T12:10:10.402378
---

# Hackers Using Cracked Software on GitHub to Spread RisePro Info Stealer

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

# [Hackers Using Cracked Software on GitHub to Spread RisePro Info Stealer](https://thehackernews.com/2024/03/hackers-using-cracked-software-on.html)

**Mar 16, 2024**Ravie LakshmananMalware / Cybercrime

[![Cracked Software on GitHub](data:image/png;base64... "Cracked Software on GitHub")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHUatPWHbLuUh0uKxlbNZFAneQoVE-g-TE2WGdyoWbkhbQjUCRTK53LbqQCznca94Q2dpJHjTCyzTsq_4exzuGD0OqKVNAtrWtTnQp4cs27VY0eOiNOj01jJGInVsOCU7JwL0IyADdROLLb9qM7U8NSIWJFIDQP2xxUMNgZ8-fVil_4mDnZbeO1sBnacwc/s790-rw-e365/crack.jpg)

Cybersecurity researchers have found a number of GitHub repositories offering cracked software that are used to deliver an information stealer called RisePro.

The campaign, codenamed **gitgub**, includes 17 repositories associated with 11 different accounts, according to G DATA. The repositories in question have since been taken down by the Microsoft-owned subsidiary.

"The repositories look similar, featuring a README.md file with the promise of free cracked software," the German cybersecurity company [said](https://www.gdatasoftware.com/blog/2024/03/37885-risepro-stealer-campaign-github).

"Green and red circles are commonly used on Github to display the status of automatic builds. Gitgub threat actors added four green Unicode circles to their README.md that pretend to display a status alongside a current date and provide a sense of legitimacy and recency."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The list of repositories is as follows, with each of them pointing to a download link ("digitalxnetwork[.]com") containing a RAR archive file -

* andreastanaj/AVAST
* andreastanaj/Sound-Booster
* aymenkort1990/fabfilter
* BenWebsite/-IObit-Smart-Defrag-Crack
* Faharnaqvi/VueScan-Crack
* javisolis123/Voicemod
* lolusuary/AOMEI-Backupper
* lolusuary/Daemon-Tools
* lolusuary/EaseUS-Partition-Master
* lolusuary/SOOTHE-2
* mostofakamaljoy/ccleaner
* rik0v/ManyCam
* Roccinhu/Tenorshare-Reiboot
* Roccinhu/Tenorshare-iCareFone
* True-Oblivion/AOMEI-Partition-Assistant
* vaibhavshiledar/droidkit
* vaibhavshiledar/TOON-BOOM-HARMONY

The RAR archive, which requires the victims to supply a password mentioned in the repository's README.md file, contains an installer file, which unpacks the next-stage payload, an executable file that's inflated to 699 MB in an effort to crash analysis tools like IDA Pro.

The actual contents of the file – amounting to a mere 3.43 MB – act as a loader to inject RisePro (version 1.6) into either AppLaunch.exe or RegAsm.exe.

RisePro burst into the spotlight in late 2022 when it was [distributed](https://thehackernews.com/2022/12/privateloader-ppi-service-found.html) using a pay-per-install (PPI) malware downloader service known as PrivateLoader.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Written in C++, it's designed to [gather sensitive information](https://thehackernews.com/2023/09/new-hijackloader-modular-malware-loader.html) from infected hosts and exfiltrate it to two Telegram channels, which are often used by threat actors to extract victims' data. Interestingly, recent research from Checkmarx [showed](https://checkmarx.com/blog/how-we-were-able-to-infiltrate-attacker-telegram-bots/) that it's possible to infiltrate and forward messages from an attacker's bot to another Telegram account.

The development comes as Splunk detailed the tactics and techniques adopted by [Snake Keylogger](https://thehackernews.com/2023/02/researchers-discover-dozens-samples-of.html), describing it as a stealer malware that "employs a multifaceted approach to data exfiltration."

"The use of FTP facilitates the secure transfer of files, while SMTP enables the sending of emails containing sensitive information," Splunk [said](https://www.splunk.com/en_us/blog/security/under-the-hood-of-snakekeylogger-analyzing-its-loader-and-its-tactics-techniques-and-procedures.html). "Additionally, integration with Telegram offers a real-time communication platform, allowing for immediate transmission of stolen data."

Stealer malware have become increasingly popular, often becoming the primary vector for ransomware and other high impact data breaches. According to a [report](https://specopssoft.com/blog/top-password-credential-stealing-malware/) from Specops published this week, RedLine, Vidar, and Raccoon have emerged as the most widely-used stealers, with RedLine alone accounting for the theft of more than 170.3 million passwords in the last six months.

"The current rise of information-stealing malware is a stark reminder of constantly evolving digital threats," Flashpoint [noted](https://flashpoint.io/blog/evolution-stealer-malware/) in January 2024. "While the motivations behind its use is almost always rooted in financial gain, stealers are continually adapting while being more accessible and easier to use."

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

[Cracked Software](https://thehackernews.com/search/label/Cracked%20Software)[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](...