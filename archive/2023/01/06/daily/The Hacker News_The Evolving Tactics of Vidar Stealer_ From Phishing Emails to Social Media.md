---
title: The Evolving Tactics of Vidar Stealer: From Phishing Emails to Social Media
url: https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html
source: The Hacker News
date: 2023-01-06
fetch_date: 2025-10-04T03:12:31.597371
---

# The Evolving Tactics of Vidar Stealer: From Phishing Emails to Social Media

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

# [The Evolving Tactics of Vidar Stealer: From Phishing Emails to Social Media](https://thehackernews.com/2023/01/the-evolving-tactics-of-vidar-stealer.html)

**Jan 05, 2023**Ravie LakshmananData Security / Malware

[![Phishing Emails to Social Media](data:image/png;base64... "Phishing Emails to Social Media")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQuZSiaxornSB1Ph7__9WstNaifLaa2QfLzI3Fpcmrxp6tHUpDDA5ugB5wnfu45ZI98kiImeMEVxFu5dWB7wrpzus5lc0uQRmetlf7kZOWUXliQbBS4aRXh3sZo9pvMrEIFMAR-qFAxZ4eDyxQsJkqdyQ3S7AsrGNQZwmTJcwuTPaELKqPn0HL3ESK/s790-rw-e365/malware.jpg)

The notorious information-stealer known as **Vidar** is continuing to leverage popular social media services such as TikTok, Telegram, Steam, and Mastodon as an intermediate command-and-control (C2) server.

"When a user creates an account on an online platform, a unique account page that can be accessed by anyone is generated," AhnLab Security Emergency Response Center (ASEC) disclosed in a technical analysis [published](https://asec.ahnlab.com/en/44554/) late last month. "Threat actors write identifying characters and the C2 address in parts of this page."

In other words, the technique relies on actor-controlled throwaway accounts created on social media to retrieve the C2 address.

An advantage to this approach is that should the C2 server be taken down or blocked, the adversary can trivially get around the restrictions by setting up a new server and editing the account pages to allow the previously distributed malware to communicate with the server.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Vidar, first identified in 2018, is a [commercial](https://blog.cyble.com/2021/10/26/vidar-stealer-under-the-lens-a-deep-dive-analysis/) [off-the-shelf](https://asec.ahnlab.com/en/30875/) [malware](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/vidar-malware-launcher-concealed-in-help-file/) that's capable of harvesting a wide range of information from compromised hosts. It typically relies on delivery mechanisms like phishing emails and cracked software for propagation.

"After information collection is complete, the extorted information is compressed into a ZIP file, encoded in Base64, and transmitted to the C2 server," ASEC researchers said.

What's new in the latest version of the malware (version 56.1) is that the gathered data is encoded prior to exfiltration, a change from the previous variants that have been known to send the compressed file data in plaintext format.

[![Vidar](data:image/png;base64... "Vidar")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTEWdAmLObDXx6DgBfq5nAr0RdhGlH4ly6rCPYErRkd6Ti0CFvGv3D4lyN9giiv_L7KnrsDMe2z1e8PTuCLv_NQlfOHRE2gvwGCsYGbpHl7uAArr6gXf4o_gILY0ey9LfqKsBCDcDZAOB9rX0TK438B2XtD0gGXVm-T-vuZQNWtu0oyPpZeBUz_S6z/s790-rw-e365/malware.png)

"As Vidar uses famous platforms as the intermediary C2, it has a long lifespan," the researchers said. "A threat actor's account created six months ago is still being maintained and continuously updated."

The development comes amid recent findings that the malware is being distributed using a variety of methods, including malicious [Google Ads](https://thehackernews.com/2022/12/new-malvertising-campaign-via-google.html) and a [malware loader](https://thehackernews.com/2022/08/hackers-using-bumblebee-loader-to.html) dubbed [Bumblebee](https://research.checkpoint.com/2022/bumblebee-increasing-its-capacity-and-evolving-its-ttps/), the latter of which is attributed to a threat actor tracked as Exotic Lily and [Projector Libra](https://unit42.paloaltonetworks.com/bumblebee-malware-projector-libra/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Risk consulting firm Kroll, in an [analysis](https://www.kroll.com/en/insights/publications/cyber/threat-actors-google-ads-deploy-vidar-stealer) published last month, said it discovered an ad for the GIMP open source image editor that, when clicked from the Google search result, redirected the victim to a typosquatted domain hosting the Vidar malware.

If anything, the evolution of malware delivery methods in the threat landscape is in part a response to Microsoft's decision to block macros by default in Office files downloaded from the internet since July 2022.

This has led to an increase in the abuse of [alternative](https://thehackernews.com/2022/12/hacking-using-svg-files-to-smuggle-qbot.html) [file](https://thehackernews.com/2022/12/bluenoroff-apt-hackers-using-new-ways.html) [formats](https://thehackernews.com/2022/12/apt-hackers-turn-to-malicious-excel-add.html) like ISO, VHD, SVG, and XLL in email attachments to bypass Mark of the Web (MotW) protections and evade anti-malware scanning measures.

"Disk image files can bypass the MotW feature because when the files inside them are extracted or mounted, MotW is not inherited to the files," ASEC researchers [said](https://asec.ahnlab.com/en/44662/), detailing a Qakbot campaign that leverages a combination of HTML smuggling and VHD file to launch the malware.

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

[AhnLab](https://thehackernews.com/search/label/AhnLab)[Info Stealer...