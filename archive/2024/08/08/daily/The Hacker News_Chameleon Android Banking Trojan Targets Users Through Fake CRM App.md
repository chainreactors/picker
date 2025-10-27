---
title: Chameleon Android Banking Trojan Targets Users Through Fake CRM App
url: https://thehackernews.com/2024/08/chameleon-android-banking-trojan.html
source: The Hacker News
date: 2024-08-08
fetch_date: 2025-10-06T18:08:44.026239
---

# Chameleon Android Banking Trojan Targets Users Through Fake CRM App

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

# [Chameleon Android Banking Trojan Targets Users Through Fake CRM App](https://thehackernews.com/2024/08/chameleon-android-banking-trojan.html)

**Aug 07, 2024**Ravie LakshmananAndroid / Mobile Security,

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh__D-FkusoGmCGUYPI4XFzZ09qUAKQZHhQZ5xVREHFZ28GfYKZse_LbdAJRUrp6yFacH37UBX8ps3-XYRRrgQ4U_QjMPj2hh8OfmFGvMQyAeJlNnhvMiL83qbQuQercRN8cSBn-rhFvJS9hD69k_OWzucuW4ogf15nPTlA9o4FnMvSB8UaA97jT8Pty8Qd/s790-rw-e365/android.png)

Cybersecurity researchers have lifted the lid on a new technique adopted by threat actors behind the [Chameleon](https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html) Android banking trojan targeting users in Canada by masquerading as a Customer Relationship Management (CRM) app.

"Chameleon was seen masquerading as a CRM app, targeting a Canadian restaurant chain operating internationally," Dutch security outfit ThreatFabric [said](https://www.threatfabric.com/blogs/chameleon-is-now-targeting-employees-masquerading-as-crm-app) in a technical report published Monday.

The campaign, spotted in July 2024, targeted customers in Canada and Europe, indicating an expansion of its victimology footprint from Australia, Italy, Poland, and the U.K.

The use of CRM-related themes for the malicious dropper apps containing the malware points to the targets being customers in the hospitality sector and Business-to-Consumer (B2C) employees.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The dropper artifacts are also designed to bypass Restricted Settings imposed by Google in Android 13 and later in order to prevent sideloaded apps from requesting for dangerous permissions (e.g., accessibility services), a technique previously employed by [SecuriDroper](https://thehackernews.com/2024/02/anatsa-android-trojan-bypasses-google.html) and [Brokewell](https://thehackernews.com/2024/04/new-brokewell-android-malware-spread.html).

Once installed, the app displays a fake login page for a CRM tool and then displays a bogus error message urging the victims to reinstall the app, when, in reality, it deploys the Chameleon payload.

[![Android Banking Trojan](data:image/png;base64... "Android Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpFdYUQRHEfZ3IFlQDEixQwzaB-QyXcmSMgQeHB3hVfxhKeq0gHtwLi5Gb_mWF0uPDpkRB7fMnY1FVlnCWn4LH9W627xFsBFBgtl0FZNmm6fcqRJjL-mEqTLmtAG71O_sj0TeeS3S4-rYXd-8Khk7JARbWKDOJVcG_n9uuH-wyv1CrLyY1umkzeBjtvQ-O/s790-rw-e365/fake.png)

This step is followed by loading the phony CRM web page again, this time asking them to complete the login process, only to display a different error message stating "Your account is not activated yet. Contact the HR department."

Chameleon is equipped to conduct on-device fraud (ODF) and fraudulently transfer users' funds, while also leveraging overlays and its wide-ranging permissions to harvest credentials, contact lists, SMS messages, and geolocation information.

"If the attackers succeed in infecting a device with access to corporate banking, Chameleon gets access to business banking accounts and poses a significant risk to the organization," ThreatFabric said. "The increased likelihood of such access for employees whose roles involve CRM is the likely reason behind the choice of the masquerading during this latest campaign."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes weeks after IBM X-Force detailed a Latin American banking malware campaign undertaken by the CyberCartel group to steal credentials and financial data as well as deliver a trojan named Caiman by means of malicious Google Chrome extensions.

"The ultimate objective of these malicious activities is to install a harmful browser plugin on the victim's browser and use the [Man-in-the-Browser](https://thehackernews.com/2023/05/hackers-targeting-italian-corporate.html) technique," the company [said](https://securityintelligence.com/posts/unveiling-latest-banking-trojan-threats-latam/).

"This allows the attackers to illegally collect sensitive banking information, along with other relevant data such as compromised machine information and on-demand screenshots. Updates and configurations are disseminated via a Telegram channel by the threat actors."

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

[Android](https://thehackernews.com/search/label/Android)[banking Trojan](https://thehackernews.com/search/label/banking%20Trojan)[CRM Security](https://thehackernews.com/search/label/CRM%20Security)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Fraud Prevention](https://thehackernews.com/search/label/Fraud%20Prevention)[mobile security](https://thehackernews.com/search/label/mobile%20security)[Threat Analysis](https://thehackernews.com/search/label/Threat%20Analysis)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+...