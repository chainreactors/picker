---
title: UAC-0226 Deploys GIFTEDCROOK Stealer via Malicious Excel Files Targeting Ukraine
url: https://thehackernews.com/2025/04/uac-0226-deploys-giftedcrook-stealer.html
source: The Hacker News
date: 2025-04-09
fetch_date: 2025-10-06T22:10:04.026623
---

# UAC-0226 Deploys GIFTEDCROOK Stealer via Malicious Excel Files Targeting Ukraine

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

# [UAC-0226 Deploys GIFTEDCROOK Stealer via Malicious Excel Files Targeting Ukraine](https://thehackernews.com/2025/04/uac-0226-deploys-giftedcrook-stealer.html)

**Apr 08, 2025**Ravie LakshmananBrowser Security / Malware

[![Malicious Excel Files Targeting Ukraine](data:image/png;base64... "Malicious Excel Files Targeting Ukraine")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiirsVM3a3Xf2MGmAoAbn7uwZQNG-Ru2kfwlGKcqENR5DoJ9FCk-Cs1FAJh4CG2He3OH1_JuTmVHAcahP5qjMeMA5z0ib6YePLf8dcXd4_KAOJ_YIiRNoYguRnrC_6ehh_b2kZknWbJ7I6g3kw5Bf4Uq1kFr77l7QAExf5GoIne8TiLj0FjWv1h3qTM9oH0/s790-rw-e365/cyber.jpg)

The Computer Emergency Response Team of Ukraine (CERT-UA) has [revealed](https://cert.gov.ua/article/6282946) a new set of cyber attacks targeting Ukrainian institutions with information-stealing malware.

The activity is aimed at military formations, law enforcement agencies, and local self-government bodies, particularly those located near Ukraine's eastern border, the agency said.

The attacks involve distributing phishing emails containing a macro-enabled Microsoft Excel spreadsheet (XLSM), which, when opened, facilities the deployment of two pieces of malware, a PowerShell script taken from the [PSSW100AVB](https://github.com/tihanyin/PSSW100AVB) ("Powershell Scripts With 100% AV Bypass") GitHub repository that opens a reverse shell, and a previously undocumented stealer dubbed GIFTEDCROOK.

"File names and email subject lines reference relevant and sensitive issues such as demining, administrative fines, UAV production, and compensation for destroyed property," CERT-UA said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"These spreadsheets contain malicious code which, upon opening the document and enabling macros, automatically transforms into malware and executes without the user's knowledge."

Written in C/C++, GIFTEDCROOK facilitates the theft of sensitive data from web browsers like Google Chrome, Microsoft Edge, and Mozilla Firefox, such as cookies, browsing history, and authentication data.

The email messages are sent from compromised accounts, often via the web interface of email clients, to lend the messages a veneer of legitimacy, and trick prospective victims into opening the documents. CERT-UA has attributed the activity to a threat cluster UAC-0226, although it has not been linked to a specific country.

[![Malicious Excel Files Targeting Ukraine](data:image/png;base64... "Malicious Excel Files Targeting Ukraine")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEistIEoKNZKFdjgpTUH14bm4yzSZDKsFbJviBP3oN3xjFu7z-HLqK9gCd-pmoYdzVWf0T2uHvLQgl5xAUGaM0cxFn1HbkOQqm53ve60rTdb3QOyk7eX5SBzJyCchwtjcGxn9QS6xAbFnm3vOOntt2aHYItyDH88lzwTOWJXcGZAaelF51aEMwVNA_XDUaFA/s790-rw-e365/uk.png)

The development comes as a suspected Russia-nexus espionage actor dubbed UNC5837 has been linked to a phishing campaign targeting European government and military organizations in October 2024.

"The campaign employed signed .RDP file attachments to establish Remote Desktop Protocol (RDP) connections from victims' machines," the Google Threat Intelligence Group (GTIG) [said](https://cloud.google.com/blog/topics/threat-intelligence/windows-rogue-remote-desktop-protocol).

"Unlike typical RDP attacks focused on interactive sessions, this campaign creatively leveraged resource redirection (mapping victim file systems to the attacker servers) and RemoteApps (presenting attacker-controlled applications to victims)."

It's worth noting that the RDP campaign was [previously](https://thehackernews.com/2024/10/cert-ua-identifies-malicious-rdp-files.html) [documented](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html) by CERT-UA, Amazon Web Services, and Microsoft in October 2024 and subsequently by Trend Micro in December. CERT-UA is tracking the activity under the name UAC-0215, while the others have attributed it to the Russian state-sponsored hacking group APT29.

The attack is also notable for the likely use of an open-source tool called PyRDP to automate malicious activities such as file exfiltration and clipboard capture, including potentially sensitive data like passwords.

"The campaign likely enabled attackers to read victim drives, steal files, capture clipboard data (including passwords), and obtain victim environment variables," the GTIG said in a Monday report. "UNC5837's primary objective appears to be espionage and file stealing."

In recent months, phishing campaigns have also been observed using [fake CAPTCHAs](https://www.netskope.com/blog/fake-captchas-malicious-pdfs-seo-traps-leveraged-for-user-manual-searches) and [Cloudflare Turnstile](https://thehackernews.com/2025/03/clearfake-infects-9300-sites-uses-fake.html) to distribute [Legion Loader](https://thehackernews.com/2023/06/new-malware-campaign-leveraging-satacom.html) (aka Satacom), which then serves as a conduit to drop a malicious Chromium-based browser extension named "Save to Google Drive."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"The initial payload is spread via a drive-by download infection that starts when a victim searches for a specific document and is lured to a malicious website," Netskope Threat Labs [said](https://www.netskope.com/blog/new-evasive-campaign-delivers-legionloader-via-fake-captcha-cloudflare-turnstile). "The downloaded document contains a CAPTCHA that, once clicked by the victim, will redirect it to a Cloudflare Turnstile CAPTCHA and then eventually to a notification page."

The page prompts users to allow notifications on the site, after which the victims are redirected to a second Cloudflare Turnstile CAPTCHA that, upon completion, is redirected again to a page that provides [ClickFix-style instructions](https://thehackernews.com/2025/03/microsoft-warns-of-clickfix-phishing.html) to download the document they are looking for.

In reality, the attack paves the way for the delivery and execution of an MSI i...