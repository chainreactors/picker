---
title: This Malicious App Abused Hacked Devices to Create Fake Accounts on Multiple Platforms
url: https://thehackernews.com/2022/11/this-malicious-app-abused-hacked.html
source: The Hacker News
date: 2022-12-01
fetch_date: 2025-10-04T00:13:53.367011
---

# This Malicious App Abused Hacked Devices to Create Fake Accounts on Multiple Platforms

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

# [This Malicious App Abused Hacked Devices to Create Fake Accounts on Multiple Platforms](https://thehackernews.com/2022/11/this-malicious-app-abused-hacked.html)

**Nov 30, 2022**Ravie Lakshmanan

[![Fake Accounts](data:image/png;base64... "Fake Accounts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7TPk77MVmCfpD48717CxBJqhBPNgn8lP8DhJLiCRQbkY9W6fFZwzmnX9tv2elIN1uMvak6xjOqwgRwGA2kH_bL_bu_gpveRZ-OzThk7lZaAz5hD0pNc4Dd0w3MOURnRr2nGyj9RN_kooAZmL4vVN8DiabC5Ra9eVHDatSt6_rcnZtHP2_4cDhEcp2/s790-rw-e365/app.png)

A malicious Android SMS application discovered on the Google Play Store has been found to stealthily harvest text messages with the goal of creating accounts on a wide range of platforms like Facebook, Google, and WhatsApp.

The app, named [Symoo](https://play.google.com/store/apps/details?id=com.vanjan.sms) (com.vanjan.sms), had over 100,000 downloads and functioned as a relay for transmitting messages to a server, which advertises an account creation service.

This is achieved by using the phone numbers associated with the infected devices as a means to gather the one-time password that's typically sent to verify the user when setting up new accounts.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The malware asks the phone number of the user in the first screen," security researcher Maxime Ingrao, who discovered the malware, [said](https://twitter.com/IngraoMaxime/status/1597224157233942528), while also requesting for SMS permissions.

"Then it pretends to load the application but remains all the time on this page, it is to hide the interface of the received SMS and that the user does not see the SMS of subscriptions to the various services."

[![Fake Accounts](data:image/png;base64... "Fake Accounts")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9xt0Ut3kS9f3dQHFJmCif663uJIpvXxb_IVqWiR-yhzKw7oaDtbZq_QycH6XL_m9BkWTLbN7QxyeAxMXz_SXi1pmYIn-c1qesA-sLr6rkfIP_WRr3VC5uLze8lE3-EJJfxLv84n7IKFdNDab63-ZvOQ5U-cEW19tS2DPbVVtevvOfE3iYeMYktvn1/s790-rw-e365/apppp.png)

Some of the major services illegally signed up using the phone numbers include Amazon, Discord, Facebook, Google, Instagram, KakaoTalk, Microsoft, Nike, Telegram, TikTok, Tinder, Viber, and WhatsApp, among others.

Additionally, the data collected by the malware is exfiltrated to a domain named "goomy[.]fun," which was previously used in another malicious application called Virtual Number (com.programmatics.virtualnumber) that has since been taken down from the Play Store.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The app's developer, Walven, has also been linked to another Android app known as [ActivationPW - Virtual numbers](https://play.google.com/store/apps/details?id=com.programmatics.activation) (com.programmatics.activation) that claims to offer "virtual numbers to receive SMS verification" from more than 200 countries for less than 50 cents.

According to Ingrao, Symoo and ActivationPW represent the two ends of the fraudulent scheme, wherein the phone numbers of the hacked devices that have the former installed are employed to help users buy accounts through the latter.

Google told The Hacker News that the two apps have been removed from the Play Store and that the developer has been banned.

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

[Android](https://thehackernews.com/search/label/Android)[Google Play Store](https://thehackernews.com/search/label/Google%20Play%20Store)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclos...