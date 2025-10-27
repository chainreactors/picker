---
title: “The Hidden GPS Threat: Unstripped Metadata on Redacted.com led 5K Rubel in bounties” ️‍♂️
url: https://infosecwriteups.com/the-hidden-gps-threat-unstripped-metadata-on-redacted-com-led-5k-rubel-in-bounties-%EF%B8%8F-%EF%B8%8F-fd044d2031b6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-08
fetch_date: 2025-10-06T19:37:29.455313
---

# “The Hidden GPS Threat: Unstripped Metadata on Redacted.com led 5K Rubel in bounties” ️‍♂️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffd044d2031b6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-gps-threat-unstripped-metadata-on-redacted-com-led-5k-rubel-in-bounties-%25EF%25B8%258F-%25EF%25B8%258F-fd044d2031b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-hidden-gps-threat-unstripped-metadata-on-redacted-com-led-5k-rubel-in-bounties-%25EF%25B8%258F-%25EF%25B8%258F-fd044d2031b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fd044d2031b6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fd044d2031b6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🌟 **“The Hidden GPS Threat: Unstripped Metadata on Redacted.com led 5K Rubel in bounties”** 🕵️‍♂️📍

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--fd044d2031b6---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--fd044d2031b6---------------------------------------)

2 min read

·

Dec 6, 2024

--

1

Share

[**Free Read**](https://medium.com/%40jeetpal2007/the-hidden-gps-threat-unstripped-metadata-on-redacted-com-led-5k-rubel-in-bounties-%EF%B8%8F-%EF%B8%8F-fd044d2031b6?sk=7354483a7f17b0c42b4375d668471b8d)

## 🚨 Overview:

What if every photo you uploaded to **Redacted.com** could unknowingly share your **exact location** with the world? 😱 That’s exactly what I discovered! Images uploaded to Redacted.com don’t strip their **EXIF metadata**, which includes sensitive details like GPS coordinates, timestamps, and device info.

🚀 Reporting this issue not only helped secure user privacy but also earned me a **5000 Rubles bounty!** 🤑 Here’s the story of how I uncovered it and the steps to reproduce. If you find this helpful, **give this write-up 50 claps** and join my **Discord community** for more tips! 🔥

**👉 Join the Discord:** <https://discord.gg/Y467qAFM4X>

## 🔍 Steps to Reproduce:

1. **Take a photo** using a device with GPS/location services enabled. 📸
2. **Upload the image** to Redacted.com. ⬆️
3. **Download the uploaded image** from Redacted.com. ⬇️
4. **Inspect the metadata** with an EXIF viewer — voilà! GPS coordinates and sensitive details are still there. 🔎

## 🌐 Impact:

This vulnerability exposes:

* **Exact User Locations:** GPS data reveals where photos were taken. 📍
* **Personal Information:** Details like device make, model, and timestamps. 🤳

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fd044d2031b6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fd044d2031b6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--fd044d2031b6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--fd044d2031b6---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--fd044d2031b6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--fd044d2031b6---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--fd044d2031b6---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--fd044d2031b6---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--fd044d2031b6---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--fd044d2031b6---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----fd044d2031b6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----fd044d2031b6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----fd044d2031b6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----fd044d2031b6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----fd044d2031b6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----fd044d2031b6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----fd044d2031b6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----fd044d2031b6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----fd044d2031b6---------------------------------------)