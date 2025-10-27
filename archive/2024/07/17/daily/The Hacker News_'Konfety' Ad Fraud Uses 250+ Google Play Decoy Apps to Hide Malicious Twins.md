---
title: 'Konfety' Ad Fraud Uses 250+ Google Play Decoy Apps to Hide Malicious Twins
url: https://thehackernews.com/2024/07/konfety-ad-fraud-uses-250-google-play.html
source: The Hacker News
date: 2024-07-17
fetch_date: 2025-10-06T17:46:49.174052
---

# 'Konfety' Ad Fraud Uses 250+ Google Play Decoy Apps to Hide Malicious Twins

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

# ['Konfety' Ad Fraud Uses 250+ Google Play Decoy Apps to Hide Malicious Twins](https://thehackernews.com/2024/07/konfety-ad-fraud-uses-250-google-play.html)

**Jul 16, 2024**Ravie LakshmananMobile Security / Online Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjj3n8LqIZNDzJcuKx7CQUVlR5ZwalOSwtyU4b_lWTC1SkD7n8vL1UShOD5vIX3WUOEYsCCaJ_dXOeHB_Nl2eKgYaqXzfoBGPuIxBWhf5vClfbrILP2Po7ZXdwWIUjlUnAmvxqlHMscjV8KRQ9A7ll8H_FTAK27vSbovoM9KIbJodWWAPhIg5JgtBnZzo23/s790-rw-e365/cyber.png)

Details have emerged about a "massive ad fraud operation" that leverages hundreds of apps on the Google Play Store to perform a host of nefarious activities.

The campaign has been codenamed **Konfety** – the Russian word for Candy – owing to its abuse of a mobile advertising software development kit (SDK) associated with a Russia-based ad network called [CaramelAds](https://github.com/CaramelAds).

"Konfety represents a new form of fraud and obfuscation, in which threat actors operate 'evil twin' versions of 'decoy twin' apps available on major marketplaces," HUMAN's Satori Threat Intelligence Team said in a technical [report](https://www.humansecurity.com/learn/blog/the-partys-over-humans-satori-threat-intelligence-and-research-team-cleans-up-konfety-mobile-ad-fraud-campaign) shared with The Hacker News.

While the decoy apps, totaling more than 250 in number, are harmless and distributed via the Google Play Store, their respective "evil twins" are disseminated through a malvertising campaign designed to facilitate ad fraud, monitor web searches, install browser extensions, and sideload APK files code onto users' devices.

The most unusual aspect of the campaign is that the evil twin masquerades as the decoy twin by spoofing the latter's app ID and advertising publisher IDs for rendering ads. Both the decoy and evil twin sets of apps operate on the same infrastructure, allowing the threat actors to exponentially scale their operations as required.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

That having said, not only do the decoy apps behave normally, a majority of them do not even render ads. They also incorporate a GDPR consent notice.

"This 'decoy/evil twin' mechanism for obfuscation is a novel way for threat actors to represent fraudulent traffic as legitimate," HUMAN researchers said. "At its peak, Konfety-related programmatic volume reached 10 billion requests per day."

Put differently, Konfety takes advantage of the SDK's ad rendering capabilities to commit ad fraud by making it a lot more challenging to distinguish malicious traffic from legitimate traffic.

The Konfety evil twin apps are said to be propagated via a malvertising campaign promoting APK mods and other software like Letasoft Sound Booster, with the booby-trapped URLs hosted on attacker-controlled domains, compromised WordPress sites, and other platforms that allow content uploads, including Docker Hub, Facebook, Google Sites, and OpenSea.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_ZnK1du4eDdAprFQWWWac8Fw8arGOfHM4tNm9Cm8LU6ly_eYiwdniCAQ-slx6is6QBtKTIZHiF0lm6-iNBREPVUMNhKrBINRmnFwgzRaXhJdE3qpz0SCyGUgSIgHbD1qIMPhMllcqun5WEusuO5d9bdnUP5kx5WOl_MilJ2GHjg7dPWaVhnFC-a-6nl4q/s790-rw-e365/apps.png)

Users who end up clicking on these URLs are redirected to a domain that tricks them into downloading the malicious evil twin app, which, in turn, acts as a dropper for a first-stage that's decrypted from the assets of the APK file and is used to set up command-and-control (C2) communications.

The initial stager further attempts to hide the app's icon from the device's home screen and runs a second-stage DEX payload that performs fraud by serving out-of-context, full-screen video ads when the user is either on their home screen or using another app.

"The crux of the Konfety operation lies in the evil twin apps," the researchers said. "These apps mimic their corresponding decoy twin apps by copying their app ID/package names and publisher IDs from the decoy twin apps."

"The network traffic derived from the evil twin applications is functionally identical to network traffic derived from the decoy twin applications; the ad impressions rendered by the evil twins use the package name of the decoy twins in the request."

Other capabilities of the malware include weaponizing the CaramelAds SDK to visit websites using the default web browser, luring users by sending notifications that prompt them into clicking on the bogus links, or sideloading modified versions of other advertising SDKs.

That's not all. Users installing the evil twins apps are urged to add a search toolbar widget to the device home screen, which surreptitiously monitors their searches by sending the data to domains named vptrackme[.]com and youaresearching[.]com.

"Threat actors understand that hosting malicious apps on stores is not a stable technique, and are finding creative and clever ways to evade detection and commit sustainable long term fraud," the researchers concluded. "Actors setting up mediation SDK companies and spreading the SDK to abuse high-quality publishers is a growing technique."

The disclosure comes a little over three months after HUMAN uncovered another malicious Android VPN app campaign dubbed [PROXYLIB](https://thehackernews.com/2024/04/malicious-apps-caught-secretly-turning.html) that leveraged a different SDK from LumiApps to incorporate proxyware functionality without users' consent or knowledge.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"I see exploitation of openly available mobile SDKs, like the one covered in the PROXYLIB investigation and the CaramelAds SDK covered in this investigation as part of a larger trend around more effectively hiding malicious functionality, along the same lines as some of the very well-known supply chain attacks and abuses of legitimate software," Lindsay Kaye, vice pr...