---
title: June 2023: Talks on VoIP security, WebRTC server-side attacks and WISH/WHIP
url: https://www.rtcsec.com/newsletter/2023-06-rtcsec-news/
source: Real-time communications security on Communication Breakdown - VoIP & WebRTC Security
date: 2023-07-01
fetch_date: 2025-10-04T11:53:42.726293
---

# June 2023: Talks on VoIP security, WebRTC server-side attacks and WISH/WHIP

[Skip to main content](#content)

[![Enable Security logo](https://www.enablesecurity.com/assets/img/logo-header-white.min.ac2c259ad95c9e369b3d7e44d9986a07c2c45fec663fbceaefe184e92011793a.svg)](/)

* [Get in touch](/contact/)

* Security Testing
  + [VoIP Penetration Testing](/voip-penetration-testing/)
  + [WebRTC Penetration Testing](/penetration-testing/)
  + [VoIP Security Assessment](/voip-security-assessment/)
  + [DDoS Resilience Testing](/ddos-testing/)
  + [Code & Config Analysis](/code-and-config-analysis/)
  + [Fuzz Testing](/fuzz-testing/)
* [SIPVicious](/sipvicious/)
* [Consultancy](/consultancy/)
* [Research](/research/)
* [Blog](/blog/)
* [Newsletter](/newsletter/)
* [About](/about/)
* [Contact](/contact/)

RTC Security Newsletter

Curated VoIP and WebRTC security news, research and updates by [Enable Security](https://www.enablesecurity.com).

Subscribe

# June 2023: Talks on VoIP security, WebRTC server-side attacks and WISH/WHIP

Published on Jun 30, 2023

It is finally conference season and so this newsletter covers 3 different events focused on RTC and opensource communications as well as the latest and greatest security fixes related to VoIP and WebRTC.

In this edition, we cover:

* Kamailio World, CommCon and OpenSIPS summit presentations of interest
* Our own work especially on WebRTC and WISH (WHIP) security
* More open SIP relay attacks in the wild
* DDoS, botnets and VoIP
* RTC vulnerabilities and fixes in MacOS, iOS, WebRTC and more

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let us know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Our Attack Platform Dangerous Demo at Kamailio World

One of my personal favorites at Kamailio World is a regular session called Dangerous Demos run by James Body. For this year’s dangerous demo, we collaborated with Fred Posner who set up a test machine running Kamailio ready to be attacked. We then used our Attack Platform to do a number of denial of service tests against the SIP interface. We ran the following tests:

* INVITE flood
* indialog INVITE flood
* indialog NOTIFY flood
* indialog CANCEL flood
* fuzzing

We had “3 minutes to completely vaporize Fred’s machine” (according to James). Although Fred’s system certainly felt the attack, it seems that it was able to reliably recover! You may watch the session on Youtube: <https://youtu.be/yehYE34d3mI?t=9443>

### WebRTC & Video Delivery application security - what could possibly go wrong?

CommCon is a residential conference in the UK that happened during June, where we had the pleasure to present about WebRTC and video delivery security. The talk was split between providing a high level overview of vulnerabilities that *may* affect WebRTC infrastructure and actually diving into some of the details. In relation to WebRTC environments, we covered the following vulnerabilities in some detail:

* CVE-2022-0778: Denial of Service vulnerability in OpenSSL
* RTP Injection
* RTP Bleed
* RTP Flood
* TURN relay abuse

Following that, we then looked at the new WISH / WHIP video delivery protocol - how it inherits the security features of WebRTC infrastructure, as well as the same attack surface too. Finally we outlined potential security issues that may affect this signalling protocol and gave examples of our concerns. More on that in the next part of this newsletter!

Anyone wanting to stream the presentations from CommCon is able to do so by buying a CommCon streaming ticket: <https://2023.commcon.xyz/live>

The presentation slides are made public: <https://www.slideshare.net/sandrogauci/commcon-2023-webrtc-video-delivery-application-security-what-could-possibly-go-wrong>

We would like to thank Dan Jenkins and his team for organising this conference and making it all happen!

### WISH (WHIP) security updates thanks to our CommCon presentation

Our presentation at CommCon included a brief security review of the WISH/WHIP draft RFC which caused a bit of stir. We will be publishing a longer blog post about the topic but in short, we listed the following potential security issues with regards to this new protocol:

* Access control issues (IDOR) on resource location
* ICE restart flooding (PATCH)
* POST flooding
* Traditional HTTP-style attacks

As a result of our presentation, a number of public projects were updated by their respective authors. The following is the list we have so far:

* Sergio Garcia Murillo [updated](https://github.com/wish-wg/webrtc-http-ingest-protocol/commit/6196413f6d12798c9ee6557ce3a2dcfa0ebef16a) the WHIP draft document to include our concerns as security considerations
* Lorenzo Miniero updated his simple WHIP server to randomize the resource address - [see pull request](https://github.com/meetecho/simple-whip-server/pull/10)
* The SRS server project updated both their [FFmpeg WebRTC fork](https://github.com/ossrs/ffmpeg-webrtc/pull/1/commits/76bdb71eabb20f1b00390190f796fc8a173db405) and [SRS](https://github.com/ossrs/srs/pull/3595) to cater for some of the concerns that we raised

### The SIPVicious PRO demo server at Kamailio World

Our demo server is an Internet-facing machine that is used as an attack target and is purposely vulnerable to a number of VoIP and WebRTC security issues. It can be reached at `demo.sipvicious.pro`.

At Kamailio World, attendees had the opportunity to present their deployment of Kamailio in production in a 5 minute talk. Thus, we showed where Kamailio fits in the demo server’s stack and how it provides us with a stable environment for reproducing security issues using our tools. We finished off by showing an example of an SQL injection flaw that is present on the demo server by misusing the sqlops Kamailio module in a way that is vulnerable.

Watch the presentation here: <https://youtu.be/EhjJMjZnfe8?t=30317>

## What’s happening?

### Kamailio World 2023: DDoS Attacks Are Coming For SIP and APIBAN talk

Kamailio World happened in Berlin during June and included a number of high quality presentations from the community. Here we cover two presentations of interest:

* Attacks Are Coming For SIP: Are You Ready? by Lucas Christian and Andreas Jansson from Twilio
* Using APIBan In Productions by Fred Posner

Lucas’ and Andreas’ talk was very interesting because they spoke about a topic that is close to heart for us. They classified VoIP DDoS attacks as one of the following:

* Low sophistication consisting of bandwidth saturation, reflection / amplification attacks and ICMP flooding; not SIP specific
* Medium sophistication targeting the actual application ports but not SIP specific either; including TCP SYN flood, TLS handshake attacks and HTTP specific attacks
* High sophistication which targets specifically SIP application servers especially SIP authentication flows

If you would like to learn about what Twilio have been doing to prepare for future DDoS attacks, this is the most comprehensive public presentation on the topic so far.

Fred Posner’s latest talk about APIBAN was given at Kamailio World. The resources, including slide and Kamailio configuration examples can be found at <https://pgpx.io/kw2023/>.

References:

* [Lucas Christian // DDoS Attacks Are Coming For SIP: Are You Ready](https://www.youtube.com/watch?v=EhjJMjZnfe8&t=3790s)
* [Fred Posner // Using APIBan In Productions](https://www.youtube.com/watch?v=EhjJMjZnfe8&t=7510s)

### Ano...