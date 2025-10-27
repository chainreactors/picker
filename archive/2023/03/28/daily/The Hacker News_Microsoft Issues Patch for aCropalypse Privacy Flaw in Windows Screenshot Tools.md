---
title: Microsoft Issues Patch for aCropalypse Privacy Flaw in Windows Screenshot Tools
url: https://thehackernews.com/2023/03/microsoft-issues-patch-for-acropalypse.html
source: The Hacker News
date: 2023-03-28
fetch_date: 2025-10-04T10:56:04.467085
---

# Microsoft Issues Patch for aCropalypse Privacy Flaw in Windows Screenshot Tools

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

# [Microsoft Issues Patch for aCropalypse Privacy Flaw in Windows Screenshot Tools](https://thehackernews.com/2023/03/microsoft-issues-patch-for-acropalypse.html)

**Mar 27, 2023**Ravie LakshmananPrivacy / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_TRu02a7KFr2INRPcQn_Tutxu_9L4hN--p-SOwhRLzVmy7xOtm9oieG3UeRyJGTtFJb18oR2u2iA2W6QzqSkHT9t91nMjzq4lq4T0dXq7-dZpOUwTVFRlPnKFANwHK3OryHgL8IjJQqMb_SgwGPQL_gei3Jeseyz4VjKu9hiYC0aGndADK-9Q1bg_/s790-rw-e365/MS.png)

Microsoft has released an out-of-band update to address a privacy-defeating flaw in its screenshot editing tool for Windows 10 and Windows 11.

The [issue](https://twitter.com/David3141593/status/1638222624084951040), dubbed **aCropalypse**, could enable malicious actors to recover edited portions of screenshots, potentially revealing sensitive information that may have been cropped out.

Tracked as **CVE-2023-28303**, the vulnerability is rated 3.3 on the CVSS scoring system. It affects both the Snip & Sketch app on Windows 10 and the Snipping Tool on Windows 11.

"The severity of this vulnerability is Low because successful exploitation requires uncommon user interaction and several factors outside of an attacker's control," Microsoft [said](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28303) in an advisory released on March 24, 2023.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Successful exploitation requires that the following two prerequisites are met -

* The user must take a screenshot, save it to a file, modify the file (for example, crop it), and then save the modified file to the same location.
* The user must open an image in Snipping Tool, modify the file (for example, crop it), and then save the modified file to the same location.

However, it does not impact scenarios where an image is copied from the Snipping Tool or modified before saving it.

"If you take a screenshot of your bank statement, save it to your desktop, and crop out your account number before saving it to the same location, the cropped image could still contain your account number in a hidden format that could be recovered by someone who has access to the complete image file," Microsoft explains.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinNs7X1jsIhDWlxCF4nSsWdVKUmN7gwPxvc9qfHK0oNlHk1mf1P7b-RGDsky180tCh7UI3BjqTzgF6rL6rlWKsUkiUycv3q7PuRjED0X0DrBrxcpHoksWa4skF7c4H9d0SChNZy4D9DKbM5VZO-lCCrqqn9bAfrobXgZ3eoJ_wNibNWzWQx9QtlFeD/s790-rw-e365/app.png)

"However, if you copy the cropped image from Snipping Tool and paste it into an email or a document, the hidden data will not be copied, and your account number will be safe."

The vulnerability has been addressed in-app version 10.2008.3001.0 of Snip and Sketch installed on Windows 10 and version 11.2302.20.0 of Snipping Tool installed on Windows 11.

aCropalypse first came to light on March 18, 2022, when it was [found](https://www.da.vidbuchanan.co.uk/blog/exploiting-acropalypse.html) that a bug in Google Pixel's Markup tool made it possible to retroactively reverse the changes introduced to screenshots, thereby recovering personal information from redacted screenshots and images, including those that have been cropped or had their contents masked.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Credited with discovering the problem are reverse engineers Simon Aarons and David Buchanan. The Pixel-related high-severity flaw, tracked as CVE-2023-21036, was reported to Google on January 2, 2023, and was [fixed](https://source.android.com/docs/security/bulletin/pixel/2023-03-01) via an update released on March 6, 2023 for Pixel 4A, 5A, 7, and 7 Pro devices.

The [shortcoming](https://acropalypse.app/) has existed since the release of the Markup utility with Android 9 Pie in 2018, and images already shared over the past five years are vulnerable to the Acropalypse attack, raising possible privacy concerns.

"You can patch it, but you can't easily un-share all the vulnerable images you may have sent," Buchanan [said](https://twitter.com/David3141593/status/1636979464688087040) in a tweet, describing it as a "bad one."

A similar issue with reversible cropping was [recently disclosed](https://theintercept.com/2023/02/14/whistleblower-image-crop-document/) in Google Docs as well, allowing users with view-only access to recover original versions of cropped images in shared documents without having the edit permissions to do so.

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

[Microsoft](https://thehackernews.com/search/label/Microsoft)[Privacy](https://thehackernews.com/search/label/Privacy)[windows security](https://thehackernews.com/search/label/windows%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](ht...