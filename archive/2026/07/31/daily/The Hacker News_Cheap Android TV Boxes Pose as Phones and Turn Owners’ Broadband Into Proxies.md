---
title: Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies
url: https://thehackernews.com/2026/07/cheap-android-tv-boxes-pose-as-phones.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:34.981185
---

# Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

![cybersecurity](data:image/svg+xml;base64...)

# [Cheap Android TV Boxes Pose as Phones and Turn Owners’ Broadband Into Proxies](https://thehackernews.com/2026/07/cheap-android-tv-boxes-pose-as-phones.html)

**Swati Khandelwal**Jul 31, 2026IoT Security / Botnet

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhxfc7_NuArKSujgjgzPzENagYVTlBxcvnFBXSbptnFs_TI1o-Zt5SINHtPEO5MNkJ3vwkKUTX68vwmCzVxRQVFcgnb9eXwAsLKayCtzMLVRuqwV3RDaWTgQNOm0CVXcV_jX1v4x4mgEthTDjAsZdF4BSPSuTTRqKnM6qbIhPVjZP38dHmpptNurSmXRM/s1700-e365/android-tv.jpg)

Bitsight says some cheap Android TV boxes have shipped with apps that rewrite their hardware identity to mimic Samsung, Huawei, Xiaomi, or Vivo phones, then click ads on websites run by the same operators.

Researchers named the operation **Fuyao** and attributed it to Zhejiang Fengwo IoT Technology Co., Ltd., a mainland China company founded in 2019.

The same apps have a second job. When a box detects an HDMI signal, it usually switches to relaying other people's traffic through the owner's broadband line as a SOCKS5 exit node. With HDMI off, it goes back to waiting for ad-fraud tasks.

Bitsight found the operation by registering an expired domain used as a factory backdoor and telemetry collector. Most identifiable devices reported the model name H96\_MAX\_V11, though Bitsight said its sinkhole view was skewed toward older models from one brand and did not establish a complete affected-model list.

In one day, after filtering for devices carrying the Fuyao apps, the sinkhole received 65,957 reports from about 38,000 unique MAC addresses. Most reports described the devices as phones. That is not a confirmed device count because the system can rotate spoofed identifiers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The report separately shows Fengwo advertising more than 120,000 "AI digital humans," but does not establish what that marketing term counts. These figures are not interchangeable, and none establishes the physical fleet size. Google told The Hacker News that the off-brand devices were not Play Protect certified Android devices.

The command-and-control (C2) server pushes complete phone profiles to each device, merging a base configuration with a per-model diff and deleting chipset properties that would expose a Rockchip, Amlogic, or Allwinner board underneath.

Fuyao uses machine vision inside its automation workflow to locate ads. The Script app carries a YOLOv8s object-detection model named lourui\_2, trained on 12 screen elements, including generic banner regions and Taboola widgets. The app combines the model with Android accessibility data and Google ML Kit optical character recognition.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiewGOrRmGvCyp6ovWupjvgRiSt-hemzwWSSlB_0PcRXZvcBsS7iMP928U_Uhv68o1GwEiqYnWq7d7LQ1If6t5NjWFXmUMbheAL1Pj25RSZPtCe0A0uIfpxeMr_4DX2TsI-PDf9DkcOdsotunWLq0Q5jmHPAT3iMb5r-Ewl5rsvMTFBvDfwOBBhZ15_bbg/s1700-e365/devices.png)

Pedro Falé, a Bitsight threat researcher, [wrote](https://www.bitsight.com/blog/fuyao-enterprise-building-ad-fraud-empire-ai-and-kids-coding-blocks) that the operation "fuses three vision and reasoning systems into a single interface."

Operators assemble campaign logic in a custom editor built on [Blockly](https://www.blockly.com/), Google's drag-and-drop programming framework. They export each fraud routine as JavaScript, upload it to S3, and send it to the box for execution.

Across four test devices, Bitsight captured about 40 fraud tasks, 21 unique campaigns, and 166 unique modules. A recovered developer comment said the template system let a small group of skilled engineers support less-skilled campaign operators, cutting costs.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjs__0U0CWgUOBiDMeMMpZgNY7xw5jxDjP4jmZCrfXIZzfZf5j2jF47ZOHflOPoWQILMRssXYjCMa-OfKPevajv4IvlbgdP2nKPiGGpmJO1MeFCCjl1c1AVh5MdC5zHYEEZGnxc-IvzHXJBQjpZW8N5Si0kDT9K4gLWoKVc4TYHoVHwXN4GngdoSJZDlT8/s1700-e365/apps.png)

Fuyao's payout chain runs through a publishing network. Bitsight mapped 144 operator-owned domains across seven beneficiary clusters. At least 84 of them loaded a Taboola tag on the homepage. The researchers said they used Taboola's public [sellers.json](https://www.taboola.com/sellers.json) file to connect the domains to revenue-collecting entities in Hong Kong and Singapore. Bitsight modeled gross returns at $1.25 per device per day, or about $47,500 daily if 38,000 devices were active.

It separately estimated annual revenue could reach $40 million at the advertised fleet size, citing 30-40% fraud flagging and a 70% ad-fill rate, but did not show the full calculation. Those are estimates, not observed revenue.

Attribution to Fengwo rests on Bitsight, which cited shared TLS certificate data, exposed wiki files, reused email addresses, revenue links, and patents.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Public Chinese patent records independently identify Zhejiang Fengwo as the assignee of related digital-human execution and monitoring technologies. [CN117421142B](https://patents.google.com/patent/CN117421142B/en), granted in November 2024, covers execution-flow tracking for digital-human behavior modules, while [CN117478834A](https://patents.google.com/patent/CN117478834A/en) describes monitoring remote screens through cloud-hosted thumbnails and keyframe comparison. Neither filing describes advertising, and the records do not establish that the company operated Fuyao or engaged in ad fraud.

The sources checked also do not establish who installed the apps or at what point in the device supply chain they appeared.

As of 7:48 p.m. IST on July 31, 2026, [Bitsight's blog index](https://www.bitsight.com/blog) still listed only the July 30 overview for Fuyao, and The Hacker News could not find either promised technical follow-up in exact-title site searches. The material checked still lacked a complete list of affected packages, firmware builds, and network indicators. Fuyao-specific identification guidance therefore remains incomplete.

"These off-brand devices were not [Play Protect certified Android devices](https://support.google.com/androidtv/thread/21...