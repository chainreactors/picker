---
title: Offensive OSINT s05e09 - Open Source Surveillance - Anomaly detection
url: https://www.offensiveosint.io/offensive-osint-s05e09-open-source-surveillance-anomaly-detection/
source: Offensive OSINT
date: 2025-05-30
fetch_date: 2025-10-06T22:26:32.008005
---

# Offensive OSINT s05e09 - Open Source Surveillance - Anomaly detection

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

## Offensive OSINT s05e09 - Open Source Surveillance - Anomaly detection

* Wojciech

  [![Wojciech](/content/images/size/w100/2023/02/OffensiveOsint-logo-RGB-2.png)](/author/wojciech/)

[Wojciech](/author/wojciech/)
29 May 2025 • 9 min read

![Offensive OSINT s05e09 - Open Source Surveillance - Anomaly detection](/content/images/2025/05/removebg.png)

The one and only situational awareness platform OS-Surveillance is evolving faster than ever, integrating powerful new data sources and innovative features designed to make real-time geospatial intelligence gathering super intuitive.

In today’s episode, I will walk you through the latest enhancements to the platform and share insights into the world of live geospatial OSINT.

We will explore why geospatial context is crucial for situational awareness, how to harness real-time data feeds effectively, and what tools and techniques can give you the advantage if you are in security, journalism, emergency response, or simply someone who wants to stay up to date with everything what is going on in the world.

> Big changes to the situational awareness system: smarter anomaly detection, better filtering, and deeper context across air, sea, and ground data. It’s now easier to focus on what’s happening, where, and why. Try it on [https://t.co/LzCES00cwK](https://t.co/LzCES00cwK?ref=offensiveosint.io) [#osint](https://twitter.com/hashtag/osint?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [#geospatial](https://twitter.com/hashtag/geospatial?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [#intelligence](https://twitter.com/hashtag/intelligence?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io)… [pic.twitter.com/fL6L7OKPNt](https://t.co/fL6L7OKPNt?ref=offensiveosint.io)
>
> — Offensive OSINT (@the\_wojciech) [May 29, 2025](https://twitter.com/the_wojciech/status/1928203197497364655?ref_src=twsrc%5Etfw&ref=offensiveosint.io)

Try it for free and share your thoughts or feature requests

[OSINT Platform for Real-Time Intelligence | Surveillance

Discover an advanced Open Source Intelligence (OSINT) platform for real-time data analysis. Enhance your investigations with tools for monitoring, facial recognition, geolocation, and more. Start today!

![](https://www.offensiveosint.io/content/images/icon/66d505ba263255696d7c80d8_c1a7a189e3091f0fc2bda80dcdb57e8f-32bits-32.png)Surveillance

![](https://www.offensiveosint.io/content/images/thumbnail/66d1b3f24427e9c56d02ca71_logo-v2.png)](https://os-surveillance.io/?ref=offensiveosint.io)

# Introduction

For quite some time now, os-surveillance.io has evolved significantly and it's not just a tool or data aggregator anymore but a comprehensive, all-in-one system for geospatial and situational awareness investigations. With powerful features for correlating events, tracking individuals, and monitoring locations in real time, the platform supports even the most complex OSINT workflows, making research faster, smarter, and more efficient.

One of the latest updates brings even more value - the ability to detect contextually significant anomalies within your chosen area of interest. Whether you're scanning for aircraft or maritime activity, you no longer need to look through every single detection to spot something unusual. The system automatically flags aircraft or vessels used by military, law enforcement, or medical services, providing immediate hints that something operational or critical may be happening.

In this post, I will walk you through how this feature works under the hood, and share what to consider if you’re building a similar system. From anomaly detection to contextual enrichment, this is how modern geospatial intelligence should work.

# Latest updates

It’s been a while since my last update, that’s because I’ve been deep in development and research to make the system better and better. While a few sneak peeks were shared on Twitter, it’s time to give a proper rundown of the latest features.

One major addition is the new Share button, which lets you generate a direct link to any event and send it to anyone, no account required. It’s perfect for quick collaboration or public sharing. Try to access this [https://osint.os-surveillance.io/#/shared/events4/abd2c649-12b0-48f8-874b-f0242d79a9ed](https://osint.os-surveillance.io/?ref=offensiveosint.io#/shared/events4/abd2c649-12b0-48f8-874b-f0242d79a9ed)

But that’s just the beginning. You can now:

* Add custom markers directly on the map,
* Search for active fires in real time,
* Instantly gather description of critical infrastructure facilities,
* Access data on US missing persons

> OS-Surveillance now provides access to US missing persons data. Search cases by location or access the latest ones in the dashboard. Use hashtag/username search, facial recognition or extract and correlate activities in nearby areas. Try it on [https://t.co/LzCERZZEHc](https://t.co/LzCERZZEHc?ref=offensiveosint.io) [#OSINT](https://twitter.com/hashtag/OSINT?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io)… [pic.twitter.com/W9DiqlIIBx](https://t.co/W9DiqlIIBx?ref=offensiveosint.io)
>
> — Offensive OSINT (@the\_wojciech) [April 28, 2025](https://twitter.com/the_wojciech/status/1916971956261241080?ref_src=twsrc%5Etfw&ref=offensiveosint.io)

* Access latest crimes in UK

> To all my UK followers, get free access to the latest crime data and stop-and-search events across the UK. Explore locations, analyse trends, and export data for deeper insights. Register and try on [https://t.co/sXiTUvAUP1](https://t.co/sXiTUvAUP1?ref=offensiveosint.io) [#OSINT](https://twitter.com/hashtag/OSINT?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [#geospatial](https://twitter.com/hashtag/geospatial?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [#intelligence](https://twitter.com/hashtag/intelligence?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io) [#geoint](https://twitter.com/hashtag/geoint?src=hash&ref_src=twsrc%5Etfw&ref=offensiveosint.io)… [pic.twitter.com/YIDjP5tox7](https://t.co/YIDjP5tox7?ref=offensiveosint.io)
>
> — Offensive OSINT (@the\_wojciech) [March 16, 2025](https://twitter.com/the_wojciech/status/1901401030774161676?ref_src=twsrc%5Etfw&ref=offensiveosint.io)

* View contextual info about the author of a post or the owner of a vessel or aircraft, right from the map tile.

![](https://www.offensiveosint.io/content/images/2025/05/Screenshot_51.png)

Each of these updates moves us closer to the vision of a truly interactive, real-time situational awareness system. And to achieve that vision, the system must do more than just display data. It needs to intelligently detect anomalies and extract suspicious or meaningful activity as it happens.

# Anomaly & suspicious activities

> Anomaly (noun) - a deviation from the normal or expected pattern.

When working with large volumes of variety geospatial data, one of the biggest challenges is real-time categorization and correlation. Surfacing meaningful signals from noise. right at the time of search is no easy task. That’s exactly what this latest update addresses.

I'm happy to introduce a text-based anomaly scanner that analyses indicators from multiple data sources to identify whether a vessel or aircraft should be flagged as potentially suspicious. It cross-references callsigns, aircraft types, and contextual patterns to surface anomalies automatically with no manual filtering required. Alongside that, the system presents the latest relevant social media activity and crime reports in the same area, enabling rapid situational awareness and recon.

## Vessels & Plan...