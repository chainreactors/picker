---
title: 2024 Wrapped: Outflank’s Top Tracks
url: https://www.outflank.nl/blog/2024/12/17/2024-wrapped-outflanks-top-tracks/
source: Publications | Outflank
date: 2024-12-18
fetch_date: 2025-10-06T19:38:28.850183
---

# 2024 Wrapped: Outflank’s Top Tracks

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [2024 Wrapped: Outflank’s Top Tracks](https://www.outflank.nl/blog/2024/12/17/2024-wrapped-outflanks-top-tracks/ "2024 Wrapped: Outflank’s Top Tracks")

[Marc Smeets](https://www.outflank.nl/blog/author/marc/ "Posts by Marc Smeets")
 |
December 17, 2024

As 2024 nears its end, we feel it is a great time to look back at what we achieved in 2024.

***TLDR*: No one would call this a quiet year for Outflank.**

## OST Releases: New Tools and Major Releases

22 releases! **We managed to put out 22 releases of OST in 2024.**

Rapid development remains a cornerstone of OST and has allowed us to match the pace of evolving threat landscape to deliver cutting edge tools and capabilities. We have a [release note tracker](https://www.outflank.nl/products/outflank-security-tooling/releases/) covering every release, but highlights include:

### EDR Presets

With EDRs becoming more powerful, and bypasses requiring more EDR-specific tricks, it was becoming hard to keep track of the countless options OST operators have for evasion of those EDRs. Our solution: EDR presets. **A preset is a predefined configuration set that uses multiple evasion techniques and has been proven to bypass specific EDRs at a given point in time.** Though they only debuted this year, presets are already a key feature of [PE Payload Generator](https://www.outflank.nl/outflank-security-tooling/pe-payload-generator/).

Though presets dramatically increase efficiency, they do have a limited shelf life. While the Outflank team updates and maintains the library of effective presets, we decided that this new feature also provided an opportunity for collaboration with our [user community](https://www.outflank.nl/products/outflank-security-tooling/ost-community/). This has quickly proven fruitful—we have already received 23 EDR bypass presets from community members! More details about this introduction was detailed in our [blog post](https://www.outflank.nl/blog/2024/04/29/ost-release-blog-edr-tradecraft-presets-powershell-tradecraft-and-more/) and can be seen in action in a [short demo video](https://www.outflank.nl/videos/ost-demo-videos/?wchannelid=vvx09qkoge&wmediaid=w8vdctgxct) we created.

### Outflank C2

With its evolution from an initial access tool to a full-featured C2 framework, we decided it was time to **rebrand our C2 framework, Stage 1, to Outflank C2**. With this rebrand came exciting new capabilities. Most notably, **[full native support](https://www.outflank.nl/blog/2024/08/07/introducing-outflank-c2-with-implant-support-for-windows-macos-and-linux/) for Windows, macOS and Linux implants**, full linking, and SOCKS proxying capabilities were added, making Outflank C2 impressively versatile. More info can be in our [release blog introducing Outflank C2](https://www.outflank.nl/blog/2024/08/07/introducing-outflank-c2-with-implant-support-for-windows-macos-and-linux/) and it can be seen in action in a [short demo video](https://www.outflank.nl/videos/ost-demo-videos/?wchannelid=vvx09qkoge&wmediaid=mhzzoafudk).

### In-Phase Builder

In-Phase Builder is an easily extendible tool that **allows operators to create script-based payloads for initial access.** Each transformation in the infection chain has been carefully optimized for OPSEC and incorporates tradecraft that reduces victim-facing warnings or converts them to less alarming notifications.

This tool also includes our fully weaponized research into an initial infection file format that faces fewer browser restrictions and Mark-of-the-Web controls compared to conventional formats.

### PhisherPrice

PhisherPrice is more than just an awesome pun— **this handy tool that helps with performing Azure Device Code Flow phishing.** Minimal setup is required to self-host a convincing phishing website and capture those Azure authentication tokens, allowing another way to gain initial access to your target organisation.

### ROADtune

The Outflank team worked with [Dirk-jan Mollema](https://x.com/_dirkjan) of Outsider Security to c**reate this new tool for offensive Intune operations. This tool is exclusive to OST customers only.**

ROADtune abuses non publicly known insecurities in Microsoft Intune with the goal of getting into a target network. A full attack chain with ROADtune allows operators to enroll a fake compliant device into a target’s Intune environment and download applications pushed to compliant devices. Red teamers can then analyse those applications and use these to progress the attack. For example, you could use a pushed VPN application to gain access to the network, gather and abuse credentials stored in those applications, etc.

### OPSEC Improvements

Lastly, we made numerous OPSEC improvements this year, including new loaders, new injection techniques, new droppers, new guardrails. Basically, too many and too private to mention details here. However, for one specific case we did publish publicly, **namely the [Early Cascade Injection](https://www.outflank.nl/blog/2024/10/15/introducing-early-cascade-injection-from-windows-process-creation-to-stealthy-injection/) technique we blogged about, and subsequently was picked up by other researchers [here](http://(https://x.com/C5pider/status/1854648777023332666) and [here](https://x.com/Teach2Breach/status/1854696901863408057).** This is a stealthy technique that effectively evades even top tier EDRs. Obviously until the EDR vendors play catch-up again. We hope you can make the most of this public research while it lasts…

## Tradecraft

In addition to tooling, a fundamental pillar of OST is [tradecraft](https://www.outflank.nl/products/outflank-security-tooling/tradecraft/). OST users have access to exclusive technical deep dives to demonstrate effective tool usage within OST and deliver broader operational guidance. This year’s topics included:

* **EDR Tradecraft & Presets**
* **PowerShell Tradecraft**
* **Microsoft Defender Static Signature Detection**
* **macOS and Linux operations with OST**
* **ROADtune**

## Global Knowledge Sharing

Outflank has always been dedicated to advancing the red team community through various knowledge sharing initiatives. We started the year off with a bang with **a free training on Microsoft Office offensive tradecraft. We were aiming for 100 registrants—and ended up getting over 1000 in just 48 hours.**

For the rest of the year, team members traveled the globe to present at different conferences, including: [x33fcon](https://github.com/outflanknl/Presentations/blob/master/x33fcon2024_Smeets_Innovate_Navigate_Elevate_A_Journey_into_OffSec_Entrepreneurship.pdf), [Blackhat US](https://github.com/outflanknl/Presentations/...