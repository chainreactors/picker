---
title: Offensive OSINT s05e08 - OS Surveillance 2.0
url: https://www.offensiveosint.io/offensive-osint-s05e08-os-surveillance-2-0/
source: Offensive OSINT
date: 2024-09-10
fetch_date: 2025-10-06T18:27:28.505741
---

# Offensive OSINT s05e08 - OS Surveillance 2.0

[![Offensive OSINT](https://www.offensiveosint.io/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://www.offensiveosint.io)

* [Home](/)
* [About me](/about-me/)
* [Open Source Surveillance](https://www.os-surveillance.io)
* [kamerka.io](https://www.kamerka.io)
* [Sign up](/signup/)
* [Account](/account/)
* [Sign in](/signin/)
* [Patreon](https://patreon.com/offensiveosint)

##### Search Here

×

## Offensive OSINT s05e08 - OS Surveillance 2.0

* Wojciech

  [![Wojciech](/content/images/size/w100/2023/02/OffensiveOsint-logo-RGB-2.png)](/author/wojciech/)

[Wojciech](/author/wojciech/)
9 Sep 2024 • 13 min read

![Offensive OSINT s05e08 - OS Surveillance 2.0](/content/images/2024/08/cheng-feng-MhKXrKqmtJk-unsplash.jpg)

In this article we will take a journey with Open Source Surveillance system through real-life use cases, from conflict zones to biggest American cities, to see how it can help you find crucial information. We’ll explore how researchers can use it to uncover new leads and support various investigations, while also touching on other cool techniques for identifying people, places, and behaviours.

In today's episode we also have tensions on Poland-Belarus border, Israeli military facilities, Washington under the radar and who lives in Beverly Hills.

Telegram location (turned off already), Twitter module, reverse address lookup or hashtag search, amongst other, are newest features that gives you even better situational awareness coverage.

If you don't know the system yet and what is capable of, please read previous posts

[Offensive OSINT s05e06 - Situational Awareness

Open Source Surveillance is an affordable and powerful OSINT system designed for both companies and individuals. It allows to gather real-time geo data from a variety of social media platforms and numerous other open sources. Try it on Open Source SurveillanceReal time intelligence gathering toolLinks Other projects & Social Offensive OSINT

![](https://www.offensiveosint.io/content/images/size/w256h256/2020/07/oo.png)Offensive OSINTWojciech

![](https://www.offensiveosint.io/content/images/size/w1200/2024/04/victor-rodriguez-IiLFMkqiFrM-unsplash.jpg)](https://www.offensiveosint.io/offensive-osint-s05e06-osint-situational-awareness/)

**Flickr module is available for limited time for everyone, just register and start searching on**

[OSINT Platform for Real-Time Intelligence | Surveillance

Discover an advanced Open Source Intelligence (OSINT) platform for real-time data analysis. Enhance your investigations with tools for monitoring, facial recognition, geolocation, and more. Start today!

![](https://cdn.prod.website-files.com/66d0903c7b71665b03444bfe/66d505ba263255696d7c80d8_c1a7a189e3091f0fc2bda80dcdb57e8f-32bits-32.png)Surveillance

![](https://cdn.prod.website-files.com/66d0903c7b71665b03444bfe/66d1b3f24427e9c56d02ca71_logo-v2.png)](https://www.os-surveillance.io/?ref=offensiveosint.io)

TL;DR

*Open Source Surveillance is an innovative real-time situational awareness system that captures social media, events, cameras and other data from open sources, with geolocation. It enhances various investigations, supports OSINT operations, and aids in law enforcement and public safety efforts. Specific applications include monitoring conflict zones or maintaining urban safety in crowdy areas.*

Before we go into the today's main topics, let's quickly look on latest update and how the platform evolved.

## Open Source Surveillance 2.0

[![](https://img.spacergif.org/v1/1280x720/0a/spacer.png)](https://www.offensiveosint.io/content/media/2024/09/v2222.mp4)

0:00

/0:57

1×

The initial public release of the system occurred almost a year ago, and since then, it has changed drastically. Numerous new modules, useful features, a new design, and an API for integrations have been added. These are just a few of the many changes that have taken place over the past months.

Now, you can choose from nearly 50 modules across various categories to gain actionable insights into any location, whether remote or urban, as long as someone has left a digital footprint there. This is incredibly useful for tracking historical or real-time events and cross-referencing them with social media activity. Additional features such as Username Search, People API, Face Recognition, Territory Analysis, Timeline, AI Geolocate, Search Nearby and recently improved dashboard enable anyone to utilize the same techniques for open-source investigations as law enforcement and professional intelligence analysts.

### API

![](https://www.offensiveosint.io/content/images/2024/08/apiad-2.png)

First ever situational awareness API is ready and has been released couple days ago. Just provide coordinates (latitude, longitude and bounding box) and optionally keywords and timestamp. API supports ~50 modules and basic documentation is available on

[Offensive OSINT Documentation

Documentation published in Theneo

![](https://app.theneo.io/favicon.svg)Theneo Documentation

![](https://app.theneo.io/icons/sun.svg)](https://app.theneo.io/offensive-osint/oss/open-source-surveillance-api?ref=offensiveosint.io)

Contact me directly if you want to know more about the API and limits.

### New design

The overall design has undergone a significant refresh. It’s now easier than ever to filter findings, retrieve statistics, and achieve exactly what you need—all while maintaining a modern and fresh look.

![](https://www.offensiveosint.io/content/images/2024/08/Screenshot_18.png)

![](https://www.offensiveosint.io/content/images/2024/08/Screenshot_17.png)

The search menu has been moved to the left side, with all additional modules now available as icons at the top of the map, and the search feature located at the top centre. You can easily switch between dark and light themes in the top right corner, near the legend that explains how the modules operate.

![](https://www.offensiveosint.io/content/images/2024/09/66cf7cbf3f11a930b6400f81_Screenshot_41-1.png)

![](https://www.offensiveosint.io/content/images/2024/09/territoryanalysis.png)

![](https://www.offensiveosint.io/content/images/2024/09/Screenshot_48.png)

![](https://www.offensiveosint.io/content/images/2024/09/Screenshot_49.png)

![](https://www.offensiveosint.io/content/images/2024/09/addresslookup.png)

Sidebar with information about the items has been replaced and now it does not take so much place what improve readability on the map.

![](https://www.offensiveosint.io/content/images/2024/08/Screenshot_16.png)

![](https://www.offensiveosint.io/content/images/2024/09/Screenshot_54.png)

Every view has been refreshed and important information properly highlighted to give better investigative experience. Let me know whether you like it and if this change was for good.

![](https://www.offensiveosint.io/content/images/2024/09/author_info.png)

![](https://www.offensiveosint.io/content/images/2024/09/Screenshot_43.png)

![](https://www.offensiveosint.io/content/images/2024/09/Screenshot_63.png)

That's being said, let's focus on how to track, find and follow any digital lead and transform it into the intelligence.

## Introduction

Situational awareness and OSINT are critical in today’s security and intelligence landscapes. Open Source Surveillance serves as a vital tool in these areas by offering comprehensive data collection and analysis capabilities.

**Situational Awareness:**

* **Crisis Response:** Real-time data enables quick response to natural disasters, public health emergencies, and other crises.
* **Event Monitoring:** Whether it's a large-scale public event or a sudden protest, OSS can track the flow of information and people that were active, helping authorities maintain order and ensure public safety.
* **Predictive analysis:** Gather information about the past events and criminal activity to predict where next major incidents might happen and where to focus your attention.
* **Public safety:** By utilizing many real-time events source, OS - Survei...