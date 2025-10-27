---
title: Chinese Hackers Use CloudScout Toolset to Steal Session Cookies from Cloud Services
url: https://thehackernews.com/2024/10/chinese-hackers-use-cloudscout-toolset.html
source: The Hacker News
date: 2024-10-29
fetch_date: 2025-10-06T18:56:11.031177
---

# Chinese Hackers Use CloudScout Toolset to Steal Session Cookies from Cloud Services

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

# [Chinese Hackers Use CloudScout Toolset to Steal Session Cookies from Cloud Services](https://thehackernews.com/2024/10/chinese-hackers-use-cloudscout-toolset.html)

**Oct 28, 2024**Ravie LakshmananCloud Security / Cyber Attack

[![Steal Session Cookies](data:image/png;base64... "Steal Session Cookies")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgu7q_zWLyL82YGiO2WXwwYD3bWkoWx26cz9VjU85mggmhuzsHOv_nf94wrXL1aagcro1xyXIfhTpKPREs1EcgmvdKoXC7oAnOchFXiowOpxBWHUaI6O7zMx-Qhn8NPpCeZPRfZ3lnDKzjA7l0UHDzEpebPW523zxKp0QcuFmNwoAB_-vnC7BE-9nezBrYe/s790-rw-e365/machine.png)

A government entity and a religious organization in Taiwan were the target of a China-linked threat actor known as **Evasive Panda** that infected them with a previously undocumented post-compromise toolset codenamed CloudScout.

"The CloudScout toolset is capable of retrieving data from various cloud services by leveraging stolen web session cookies," ESET security researcher Anh Ho [said](https://www.welivesecurity.com/en/eset-research/cloudscout-evasive-panda-scouting-cloud-services/). "Through a plugin, CloudScout works seamlessly with MgBot, Evasive Panda's signature malware framework."

The use of the .NET-based malware tool, per the Slovak cybersecurity company, was detected between May 2022 and February 2023. It incorporates 10 different modules, written in C#, out of which three are meant for stealing data from Google Drive, Gmail, and Outlook. The purpose of the remaining modules remains unknown.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Evasive Panda, also tracked as Bronze Highland, Daggerfly, and StormBamboo, is a [cyber espionage group](https://thehackernews.com/2024/08/china-linked-hackers-compromise-isp-to.html) that has a track record of striking various entities across Taiwan and Hong Kong. It's also known for orchestrating watering hole and supply chain attacks targeting the Tibetan diaspora.

What sets the threat actor apart from the rest is the use of several initial access vectors, ranging from newly disclosed security flaws to compromising the supply chain by means of DNS poisoning, to breach victim networks and deploy MgBot and Nightdoor.

ESET said the CloudScout modules are designed to hijack authenticated sessions in the web browser by stealing the cookies and using them to gain unauthorized access to Google Drive, Gmail, and Outlook. Each of these modules is deployed by an MgBot plugin, programmed in C++.

"At the heart of CloudScout is the CommonUtilities package, which provides all necessary low-level libraries for the modules to run," Ho explained.

"CommonUtilities contains quite a few custom-implemented libraries despite the abundant availability of similar open-source libraries online. These custom libraries give the developers more flexibility and control over the inner workings of their implant, compared to open-source alternatives."

This includes -

* HTTPAccess, which provides functions to handle HTTP communications
* ManagedCookie, which provides functions to manage cookies for web requests between CloudScout and the targeted service
* Logger
* SimpleJSON

The information gathered by the three modules – mail folder listings, email messages (including attachments), and files matching certain extensions (.doc, .docx, .xls, .xlsx, .ppt, .pptx, .pdf, and .txt) – is compressed into a ZIP archive for subsequent exfiltration by either MgBot or Nightdoor.

That said, new security mechanisms introduced by Google such as Device Bound Session Credentials ([DBSC](https://thehackernews.com/2024/04/google-chrome-beta-tests-new-dbsc.html)) and [App-Bound Encryption](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html) are bound to render cookie-theft malware obsolete.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"CloudScout is a .NET toolset used by Evasive Panda to steal data stored in cloud services," Ho said. "It is implemented as an extension to MgBot and uses the pass-the-cookie technique to hijack authenticated sessions from web browsers."

The development comes as the Government of Canada accused a "sophisticated state-sponsored threat actor" from China of conducting broad reconnaissance efforts spanning several months against numerous domains in Canada.

"The majority of affected organizations targeted were Government of Canada departments and agencies, and includes federal political parties, the House of Commons, and Senate," it [said](https://www.cyber.gc.ca/en/news-events/statement-peoples-republic-china-reconnaissance-canadian-systems) in a statement.

"They also targeted dozens of organizations, including democratic institutions, critical infrastructure , the defense sector, media organizations, think tanks, and NGOs."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Cyber Defense](https://thehackernews.com/search/label/Cyber%20Defense)[cyber espionage](https://thehackernews.com/search/label/cyber%20espionage)[Cyber Threat](https://thehackernews.com/se...