---
title: North Korean Hackers Targets Job Seekers with Fake FreeConference App
url: https://thehackernews.com/2024/09/north-korean-hackers-targets-job.html
source: The Hacker News
date: 2024-09-05
fetch_date: 2025-10-06T18:30:34.503833
---

# North Korean Hackers Targets Job Seekers with Fake FreeConference App

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

# [North Korean Hackers Targets Job Seekers with Fake FreeConference App](https://thehackernews.com/2024/09/north-korean-hackers-targets-job.html)

**Sep 04, 2024**Ravie LakshmananCryptocurrency / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiBB9ZcpErY96m12zTHmpAjWSz85vx3RP4bPUv4Qqu3WrToApYYBUyVHQ2VHl04c6Eg2HhKpz8LsW7H_REOrQ81Dq4HdRvjV9_P6X7xMsoxpFEPuYDKCo7RCUOrwaXbkEkOtieNifdeAgDpccT_H9l30Bsm-2UVm6abTquTlIk0j8L9lMiKYPDjt6i_Y9z/s790-rw-e365/northkorea.jpg)

North Korean threat actors have leveraged a fake Windows video conferencing application impersonating FreeConference.com to backdoor developer systems as part of an ongoing financially-driven campaign dubbed Contagious Interview.

The new attack wave, [spotted](https://www.group-ib.com/blog/apt-lazarus-python-scripts/) by Singaporean company Group-IB in mid-August 2024, is yet another indication that the activity is also leveraging native installers for Windows and Apple macOS to deliver malware.

Contagious Interview, also tracked as DEV#POPPER, is a [malicious campaign](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html) orchestrated by a North Korean threat actor tracked by CrowdStrike under the moniker Famous Chollima.

The attack chains begin with a fictitious job interview, tricking job seekers into downloading and running a Node.js project that contains the BeaverTail downloader malware, which in turn delivers InvisibleFerret, a cross-platform Python backdoor that's equipped with remote control, keylogging, and browser stealing capabilities.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some iterations of BeaverTail, which also functions as an information stealer, have manifested in the form of JavaScript malware, typically distributed via [bogus npm packages](https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html) as part of a purported technical assessment during the interview process.

But that changed in July 2024 when Windows MSI installer and Apple macOS disk image (DMG) files masquerading as the legitimate MiroTalk video conferencing software were discovered in the wild, acting as a conduit to deploy an updated version of BeaverTail.

The latest findings from Group-IB, which has attributed the campaign to the infamous Lazarus Group, suggest that the threat actor is continuing to lean on this specific distribution mechanism, the only difference being that the installer ("FCCCall.msi") mimics FreeConference.com instead of MiroTalk.

It's believed that the phony installer is downloaded from a website named freeconference[.]io, which uses the same registrar as the fictitious mirotalk[.]net website.

"In addition to Linkedin, Lazarus is also actively searching for potential victims on other job search platforms such as WWR, Moonlight, Upwork, and others," security researcher Sharmine Low said.

"After making initial contact, they would often [attempt to move the conversation](https://www.reddit.com/r/webdev/comments/1ddpmiz/beware_of_scammers/) onto Telegram, where they would then ask the potential interviewees to download a video conferencing application, or a Node.js project, to perform a technical task as part of the interview process."

In a sign that the campaign is undergoing active refinement, the threat actors have been observed injecting the malicious JavaScript into both cryptocurrency- and gaming-related repositories. The JavaScript code, for its part, is designed to retrieve the BeaverTail Javascript code from the domain ipcheck[.]cloud or regioncheck[.]net.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIl98NSMSy4UDfnG2hVv0nLXYLn4DdHXBTIS33LgpizDZVjriXMOoO6GFZ9oLnZyjMx0jA8IxduUNv3nHIS7zlHB4gDKq4SFh5ZDWOWVqh-4pEJRxx1b2mLBFwackr11lf7ojEiTxP5riNlvxf3-v21zQbzxce_oDQeQx46tJ4iIc-EXQsdT9_W7PPBzys/s790-rw-e365/gib.png)

It's worth mentioning here that this behavior was also recently highlighted by software supply chain security firm Phylum in connection with an npm package named [helmet-validate](https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html), suggesting that the threat actors are simultaneously making use of different propagation vectors.

Another notable change is that BeaverTail is now configured to extract data from more cryptocurrency wallet extensions such as Kaikas, Rabby, Argent X, and Exodus Web3, in addition to implementing functionality to establish persistence using AnyDesk.

That's not all. BeaverTail's information-stealing features are now realized through a set of Python scripts, collectively called CivetQ, which is capable of harvesting cookies, web browser data, keystrokes, and clipboard content, and delivering more scripts. A total of 74 browser extensions are targeted by the malware.

"The malware is able to steal data from Microsoft Sticky Notes by targeting the application's SQLite database files located at `%LocalAppData%\Packages\Microsoft.MicrosoftStickyNotes\_8wekyb3d8bbwe\LocalState\plum.sqlite,` where user notes are stored in an unencrypted format," Low said.

"By querying and extracting data from this database, the malware can retrieve and exfiltrate sensitive information from the victim's Sticky Notes application."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The emergence of CivetQ points to a modularized approach, while also underscoring that the tools are under active development and have been constantly evolving in little increments over the past few months.

"Lazarus has updated their tactics, upgraded their tools, and found better ways to conceal their activities," Low said. "They show no signs of easing their efforts, with their campaign targeting job seekers extending into 2024 and to the present day. Their attacks have become increasingly creative, and they are now expanding their reach across more platforms."

The disclosure comes as the U.S. F...