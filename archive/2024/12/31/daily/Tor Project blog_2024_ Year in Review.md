---
title: 2024: Year in Review
url: https://blog.torproject.org/2024-year-in-review/
source: Tor Project blog
date: 2024-12-31
fetch_date: 2025-10-06T19:43:09.550764
---

# 2024: Year in Review

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# 2024: Year in Review

by [pavel](/author/pavel)
| December 30, 2024

![](/2024-year-in-review/lead.png)

Whenever people talk about Tor, a few key concerns are consistently brought up: performance, security and network health, censorship circumvention, and compatibility for third-party integrations. These are essential priorities of the Tor Project's work, and this year we've made significant progress in each of these areas. [As we reflect on the past year](https://blog.torproject.org/tor-in-2024/), let's revisit some of our new and ongoing projects that address these core questions and challenges.

## Improving performance and security

* *Onion Services improvements:* Onion Services are a communication technology for exchanging data using the Tor network. They provide end-to-end encryption and enhanced anonymity by keeping all communication within the Tor network. In 2024, we launched [OnionSpray](https://onionservices.torproject.org/apps/web/onionspray/), a plug-and-play toolkit making it easier to convert existing websites into .onion domains. OnionSpray functions as a proxy, allowing existing websites to seamlessly integrate with Onion Services. By simplifying the setup, operators can quickly benefit from the censorship resistance and denial-of-service protection of .onion sites without modifying their existing infrastructure. For a deeper dive, [check out the case study from one of our early adopters.](https://blog.torproject.org/mediapart-launches-onion-service/)
* *Vanguards support:* As of this summer, [Arti supports Vanguards](https://blog.torproject.org/announcing-vanguards-for-arti), a defense against guard discovery attacks targeting onion services and onion service clients. First introduced in 2018 as an add-on to v3 onion services, Vanguards serve to mitigate the risk of de-anonymization attacks and keep users safe.
* *Memory quota tracking:* Tor engineers and volunteers have made significant progress with [Arti, a modern rewrite of the Tor core in Rust](https://arti.torproject.org/). Arti's modular design improves maintainability, security, and performance. To defend against memory exhaustion attacks, this year, [we implemented memory quota tracking](https://blog.torproject.org/arti_1_3_0_released/). This feature allows Tor to monitor and limit its memory usage, prioritizing the closing of older connections to lower memory usage and maintain system stability. This enhances reliability for all users and reduces the risk of system overload during high traffic periods.
* *Bandwidth scanners:* Tor's ongoing strategies to maintain a stable and healthy network rely on the ability to effectively leverage network data. [Bandwidth scanners](https://tpo.pages.torproject.net/network-health/bandwidth_scanners/index.html) play an important role in the performance and security of the network by measuring relay capacity in the Tor network. This data is then used to inform how the paths that form a connection to the Tor network are built. The goal is to optimize load distribution in the network, ultimately boosting browsing speed and reliability.

## Expanding anti-censorship capabilities

* *WebTunnel launch:* At the beginning of the year, we successfully [launched WebTunnel](https://blog.torproject.org/introducing-webtunnel-evading-censorship-by-hiding-in-plain-sight/), a new bridge type designed to blend seamlessly into regular web traffic, making it harder for censors to block Tor connections. By mimicking common internet protocols, WebTunnel improves the resilience of the Tor network in regions with heavy censorship. And since its launch earlier this year, we've made sure to prioritize small download sizes for more convenient distribution and simplified the support of uTLS integration further mimicking the characteristics of more widespread browsers. This makes Webtunnel safe for general users because it helps conceal the fact that a tool like Tor is being used. This approach has already shown promise in providing users with reliable access to the open web, especially in highly censored regions like Russia. We're currently hoping to scale these efforts. [If you have the technical know-how to support Tor by running new bridges, please consider getting engaged.](https://blog.torproject.org/call-for-webtunnel-bridges/)
* *Snowflake updates:* When it launched in 2021, the Snowflake browser extension was a major leap forward in Tor's fight against online censorship. It makes [setting up a proxy as easy as opening a webpage](https://snowflake.torproject.org/). To comply with changes to Google Chrome's extension framework, we reworked Snowflake's WebExtension to align with Manifest V3 standards. The updated version was successfully deployed in September, ensuring Snowflake remains available for users on Chrome after Google phased out Manifest V2 support. We're also continually refining Snowflake by automating the release process, replacing outdated content delivery networks, and protocol revisions.These efforts ensure Snowflake stays reliable and effective for users around the world.
* *Transition to Rdsys:* This year marked the successful transition from [BridgeDB to Rdsys](https://blog.torproject.org/making-connections-from-bridgedb-to-rdsys/), our next-generation bridge distribution system. Built with a modular architecture, Rdsys helps us to adapt quickly to emerging censorship tactics and allows us to experiment with bridge distribution channels and reach users more effectively where they are.

## Advancing outreach and advocacy

* *Joining forces with Tails:* Collaboration has been at the center of our work, exemplified [by the Tor Project's merger with Tails](https://blog.torproject.org/tor-tails-join-forces/)--a portable operating system that uses Tor to protect users from digital surveillance. [Tails](https://tails.net/news/index.en.html) has introduced several impactful updates this year, including a new backup feature to prevent data loss. Looking ahead, the team is exploring ways to support messaging apps like Signal on Tails, enabling users to communicate securely while isolating sensitive communications from potentially compromised devices.
* *Decentralized training efforts:* We transitioned from conducting global training sessions ourselves to equipping local trainers with the skills to teach Tor. We expanded the Privacy Resilience Grants Program, first launched in 2022, to 49 countries, enabling trainers to conduct localized Tor activities. Trainers have reported significant impacts, such as improved protections from surveillance and collaborative learning.
* *Relay advocacy:* We've continued to [expand our partnerships with universities to promote relay operations](https://toruniversity.eff.org/). These efforts not only strengthen Tor's network with access to powerful relays but also encourage more organizations to contribute to its infrastructure by setting a positive example.

## Preparing Tor for the future

* *RPC subsystem:* One of the most significant advancements for Arti this year is the development of [a completely reimagined RPC subsystem](https://blog.torproject.org/arti_1_2_6_released/). This system redefines how applications interact with Tor by offering an out-of-process API, improving modularity and application isolation. Unlike the existing control port, the RPC subsystem prevents applications from accessing sensitive information. This design will make it easier and safer for developers to build tools and services that use Tor.
* *Human-friendly .onion addresses:* Long and complex .onion domains have been a usability challenge. This year, we began research into creating more human-readable alternatives, aiming to improve accessibility for n...