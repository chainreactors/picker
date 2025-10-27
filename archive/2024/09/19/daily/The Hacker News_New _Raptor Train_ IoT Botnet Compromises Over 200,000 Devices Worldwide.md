---
title: New "Raptor Train" IoT Botnet Compromises Over 200,000 Devices Worldwide
url: https://thehackernews.com/2024/09/new-raptor-train-iot-botnet-compromises.html
source: The Hacker News
date: 2024-09-19
fetch_date: 2025-10-06T18:29:40.172610
---

# New "Raptor Train" IoT Botnet Compromises Over 200,000 Devices Worldwide

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

# [New "Raptor Train" IoT Botnet Compromises Over 200,000 Devices Worldwide](https://thehackernews.com/2024/09/new-raptor-train-iot-botnet-compromises.html)

**Sep 18, 2024**Ravie LakshmananIoT Security / Threat Intelligence

[![IoT Botnet](data:image/png;base64... "IoT Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXz9TOfv93Ndqmr5_lX60979DgYHZPNx5x8TWp73bJmLig64jnYTQ6BsKIvRC7qZJIboPSCVrm5VYk1LXJ6HmI_oZQL-DlIbxjakNVXRhN_yvymcViq61XXYMHCh2KX3t3mdLn1QgEjOE2PPEqIy_nMx1FH-FSgKMcid_ks1DlL6YP8Edir7OK7L2RKZqs/s790-rw-e365/botnet.png)

Cybersecurity researchers have uncovered a never-before-seen botnet comprising an army of small office/home office (SOHO) and IoT devices that are likely operated by a Chinese nation-state threat actor called [Flax Typhoon](https://thehackernews.com/2024/06/redjuliett-cyber-espionage-campaign.html) (aka Ethereal Panda or RedJuliett).

The sophisticated botnet, dubbed **Raptor Train** by Lumen's Black Lotus Labs, is believed to have been operational since at least May 2020, hitting a peak of 60,000 actively compromised devices in June 2023.

"Since that time, there have been more than 200,000 SOHO routers, NVR/DVR devices, network attached storage (NAS) servers, and IP cameras; all conscripted into the Raptor Train botnet, making it one of the largest Chinese state-sponsored IoT botnets discovered to-date," the cybersecurity company [said](https://blog.lumen.com/derailing-the-raptor-train) in a 81-page report shared with The Hacker News.

The infrastructure powering the botnet is estimated to have ensnared hundreds of thousands of devices since its formation, with the network powered by a three-tiered architecture consisting of the following -

* Tier 1: Compromised SOHO/IoT devices
* Tier 2: Exploitation servers, payload servers, and command-and-control (C2) servers
* Tier 3: Centralized management nodes and a cross-platform Electron application front-end referred to as Sparrow (aka Node Comprehensive Control Tool, or NCCT)

The way it works is, that bot tasks are initiated from Tier 3 "Sparrow" management nodes, which are then routed through the appropriate Tier 2 C2 servers, and subsequently sent to the bots themselves in Tier 1, which makes up a huge chunk of the botnet.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Some of the devices targeted include routers, IP cameras, DVRs, and NAS from various manufacturers such as ActionTec, ASUS, DrayTek, Fujitsu, Hikvision, Mikrotik, Mobotix, Panasonic, QNAP, Ruckus Wireless, Shenzhen TVT, Synology, Tenda, TOTOLINK, TP-LINK, and Zyxel.

A majority of the Tier 1 nodes have been geolocated to the U.S., Taiwan, Vietnam, Brazil, Hong Kong, and Turkey. Each of these nodes has an average lifespan of 17.44 days, indicating the threat actor's ability to reinfect the devices at will.

"In most cases, the operators did not build in a persistence mechanism that survives through a reboot," Lumen noted.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhy_GiFlTR5fOw0KrrSed1PNQGHpNlosqdiTusAQMHG1XXKu7WcvaozOCfH0iufCFkkq7FML1cl0s24GdPNairvTg_B84HqHhgqO2-tGqXz4Tqw1HW7to-HQn7WoWgi-8OYyLxM0Kr_8kIRC7_xX6GEZWD70VpJSnJW595uwiaKc-mbRW7AULQecDl49BjU/s790-rw-e365/raptor1.jpg)

"The confidence in re-exploitability comes from the combination of a vast array of exploits available for a wide range of vulnerable SOHO and IoT devices and an enormous number of vulnerable devices on the Internet, giving Raptor Train somewhat of an 'inherent' persistence."

The nodes are infected by an in-memory implant tracked as Nosedive, a custom variant of the [Mirai botnet](https://thehackernews.com/2024/08/unpatched-avtech-ip-camera-flaw.html), via Tier 2 payload servers explicitly set up for this purpose. The ELF binary comes with capabilities to execute commands, upload and download files, and mount DDoS attacks.

Tier 2 nodes, on the other hand, are rotated about every 75 days and are primarily based in the U.S., Singapore, the U.K., Japan, and South Korea. The number C2 nodes has increased from approximately 1-5 between 2020 and 2022 to no less than 60 between June 2024 and August 2024.

These nodes are flexible in that they also act as exploitation servers to co-opt new devices into the botnet, payload servers, and even facilitate reconnaissance of targeted entities.

At least four different campaigns have been linked to the ever-evolving Raptor Train botnet since mid-2020, each of which are distinguished by the root domains used and the devices targeted -

* Crossbill (from May 2020 to April 2022) - use of the C2 root domain k3121.com and associated subdomains
* Finch (from July 2022 to June 2023) - use of the C2 root domain b2047.com and associated C2 subdomains
* Canary (from May 2023 to August 2023) - use of the C2 root domain b2047.com and associated C2 subdomains, while relying on multi-stage droppers
* Oriole (from June 2023 to September 2024) - use of the C2 root domain w8510.com and associated C2 subdomains

The Canary campaign, which heavily targeted ActionTec PK5000 modems, Hikvision IP cameras, Shenzhen TVT NVRs, and ASUS routers, is notable for employing a multi-layered infection chain of its own to download a first-stage bash script, which connects to a Tier 2 payload server to retrieve Nosedive and a second-stage bash script.

The new bash script, in turn, attempts to download and execute a third-stage bash script from the payload server every 60 minutes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPI6jkmjEp4HU_BjdHQfim7_sVCZLegFUXUvjacZ6x7iKurkMEUX5CWzpw5f_SqH_VkthRhEXejLn1GnycTK8n1pPiNLXtT1BmseErNGJdlnsvlrrSWPc5kM4lUAbZZ39Tf9Y96TPZ99tq5UvpalvABL1CeSXXFpeqpt_mAvxpa9o74xDBy1P2jdPbNI-B/s790-rw-e365/raptor6.jpg)

"In fact, the w8510.com C2 domain for [the Oriole] campaign became so prominent amongst compromised IoT devices, that by June 3, 2024, it was included in the Cisco Umbrella domain rankings," Lumen said.

"By at ...