---
title: Researcher Uncovers Potential Wiretapping Bugs in Google Home Smart Speakers
url: https://thehackernews.com/2022/12/researcher-uncovers-potential.html
source: The Hacker News
date: 2022-12-31
fetch_date: 2025-10-04T02:48:52.978706
---

# Researcher Uncovers Potential Wiretapping Bugs in Google Home Smart Speakers

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

# [Researcher Uncovers Potential Wiretapping Bugs in Google Home Smart Speakers](https://thehackernews.com/2022/12/researcher-uncovers-potential.html)

**Dec 30, 2022**Ravie LakshmananBug Bounty / Privacy

[![Google Home Smart Speakers](data:image/png;base64... "Google Home Smart Speakers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZMVFACPB9r45XFCQ95H6qYl3JPtxP7GK4MM_OqTlA4VdpcQOFWeQDm-aM7q6lwWSahvjbluAgrs05hDDFXYbAcEx7LH8wHyud_NWRl6tPLKwsSuhbv3yXYHSRPkAehCrztjRDfEA5WCCvqa-MXypIEbdCQfMpV9V1n85PBLuEVnIieJlr9K8zfulh/s790-rw-e365/speaker.png)

A security researcher was awarded a bug bounty of $107,500 for identifying security issues in Google Home smart speakers that could be exploited to install backdoors and turn them into wiretapping devices.

The flaws "allowed an attacker within wireless proximity to install a 'backdoor' account on the device, enabling them to send commands to it remotely over the internet, access its microphone feed, and make arbitrary HTTP requests within the victim's LAN," the researcher, who goes by the name Matt Kunze, [disclosed](https://downrightnifty.me/blog/2022/12/26/hacking-google-home.html) in a technical write-up published this week.

In making such malicious requests, not only could the Wi-Fi password get exposed, but also provide the adversary direct access to other devices connected to the same network. Following responsible disclosure on January 8, 2021, the issues were remediated by Google in April 2021.

The problem, in a nutshell, has to do with how the Google Home software architecture can be leveraged to add a rogue Google user account to a target's home automation device.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In an attack chain detailed by the researcher, a threat actor looking to eavesdrop on a victim can trick the individual into installing a malicious Android app, which, upon detecting a Google Home device on the network, issues stealthy HTTP requests to link an attacker's account to the victim's device.

Taking things a notch higher, it also emerged that, by staging a [Wi-Fi deauthentication attack](https://en.wikipedia.org/wiki/Wi-Fi_deauthentication_attack) to force a Google Home device to [disconnect from the network](https://hackernoon.com/forcing-a-device-to-disconnect-from-wifi-using-a-deauthentication-attack-f664b9940142), the appliance can be made to enter a "setup mode" and create its own open Wi-Fi network.

The threat actor can subsequently connect to the device's setup network and [request details](https://arxiv.org/abs/2001.04574) like device name, cloud\_device\_id, and certificate, and use them to link their account to the device.

[![Google Home Smart Speakers](data:image/png;base64... "Google Home Smart Speakers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNUvTyMmn7pFBsaHriEBGe6P_jzqh2Qwapu4XPYGa34sA-lrIXAK6BFpSVTq9OFoxDOGVk-a935gd147WW6V0Vj2prxzviZVk3GmeVPH582EjueTEIHaZRe5LoIJHV-o87X3XAvV9lpIIdmJF9AQDzcUV041EuHVtvVc5NqHSVP14RyjkxQJNPNv8m/s790-rw-e365/wire.png)

Regardless of the attack sequence employed, a successful link process enables the adversary to take advantage of [Google Home routines](https://support.google.com/googlenest/answer/7029585) to turn down the volume to zero and [call a specific phone number](https://support.google.com/googlenest/answer/9849261) at any given point in time to spy on the victim through the device's microphone.

[![Google Home Smart Speakers](data:image/png;base64... "Google Home Smart Speakers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPuy9afFSn5NHDlTfJcrYGk689JXtjfTR6QISiJ_ahU0U07xlNA4yATydVm4BWgzmtK0_e18gMhQM3VOnmV1pMmN4ucG-lfwsQORncrzjyv82rtAEWZsOgERoLYftJLxJWA5IdvdC2z_HZBbhYqfwxY3bFtcj6tLBB1mzwavcV2xngCCyKXn3teOkd/s790-rw-e365/routine.png)

"The only thing the victim may notice is that the device's LEDs turn solid blue, but they'd probably just assume it's updating the firmware or something," Kunze said. "During a call, the LEDs do not pulse like they normally do when the device is listening, so there is no indication that the microphone is open."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Furthermore, the attack can be extended to make arbitrary HTTP requests within the victim's network and even read files or introduce malicious modifications on the linked device such that they would get applied after a reboot.

Among the patches deployed by the internet giant to fix the issues include an invite-based mechanism so as to link a Google account using the API and disabling remote initiation of call commands through routines.

This is not the first time such attack methods have been devised to covertly snoop on potential targets through voice-activated devices.

In November 2019, a group of academics disclosed a technique called [Light Commands](https://thehackernews.com/2019/11/hacking-voice-assistant-laser.html), which refers to a vulnerability of [MEMS microphones](https://thehackernews.com/2020/03/voice-assistants-ultrasonic-waves.html) that permits attackers to remotely inject inaudible and invisible commands into popular voice assistants like Google Assistant, Amazon Alexa, Facebook Portal, and Apple Siri using light.

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
[![Facebook Messenger](data:image...