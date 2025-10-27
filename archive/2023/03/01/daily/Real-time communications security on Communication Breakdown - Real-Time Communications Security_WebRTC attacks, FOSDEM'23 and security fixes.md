---
title: WebRTC attacks, FOSDEM'23 and security fixes
url: https://www.rtcsec.com/newsletter/2023-02-rtcsec-news/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2023-03-01
fetch_date: 2025-10-04T08:19:18.142341
---

# WebRTC attacks, FOSDEM'23 and security fixes

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

# WebRTC attacks, FOSDEM'23 and security fixes

Published on Feb 28, 2023

Welcome to the February 2023 edition of RTCSec newsletter. If you are reading this on your email client, you might notice slight formatting changes - the red color of the Communication Breakdown blog and the mascot on the side. Hope that this makes it more distinguishable. Do let me know if you have feedback, by replying to this email.

In this edition, we cover:

* A chat with Arin Sime of WebRTC.Ventures about the WebRTC infrastructure attacks
* A glimpse of SIPVicious PRO running on an Android phone
* Our review of FOSDEM'23 talks of interest to the RTCSec audience
* Various security reports involving FreePBX, FreeSWITCH, Chromium, BIG-IP and Oracle’s WebRTC session controller

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let me know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Webinar about WebRTC infrastructure attacks

I was invited on WebRTC Live by WebRTC.ventures to talk about the WebRTC infrastructure vulnerabilities. I started by presenting a mind-map of the attack surface, showing the different parts of the infrastructure that may be attacked and each individual attack that might apply. Then I did a quick demo showing how WebRTC signalling servers might be attacked to cause denial of service. For that, I used our Attack Platform. Finally told the story so far about the TURN relay abuse vulnerability that affected a number of WebRTC platforms, how we found it, reported it to various companies and what happened next.

Watch the video here: <https://www.youtube.com/watch?v=qlQJuyp7nS8>

## SIPVicious PRO on Android phones: a quick demo

We have a short video showing SIPVicious PRO running on an Android test phone in our lab. This may be useful when doing security testing or penetration testing on IMS (IP Multimedia Subsystem) targets, for example in a VoLTE environment.

The video is called *First glimpse of SIPVicious PRO running on Android* and it can be enjoyed here: <https://www.youtube.com/watch?v=TjeazO1i8mQ>.

[![SIPVicious PRO on Android test phone](SIPVicious-PRO-on-Android.png)](https://www.youtube.com/watch?v=qlQJuyp7nS8)

## What’s happening?

### FOSDEM'23 talks of interest

The open source conference happened on 4 & 5 February 2023. Unfortunately we were not able to attend but we still kept an eye out for interesting talks. Here is our quick review of talks that looked relevant to this newsletter’s audience. Do get in touch if we missed anything that you think should be covered or at least mentioned!

#### Modernizing Authentication and Authorization in XMPP

This presentation by Matthew Wild covers XMPP authentication, starting with a great introduction to the topic in general. Then he describes the new authentication mechanism for XMPP called FAST, which stands for Fast Authentication Streamlining Tokens. This allows the use of things like WebAuthn, FIDO2 and Passkeys for authenticating to your XMPP account, bringing XMPP authentication up to date.

Watch the presentation: <https://fosdem.org/2023/schedule/event/modern_xmpp_auth/>

#### Secure payments over VoIP calls in the cloud

This is a talk by Nuno M Reis on how Talkdesk achieved PCI compliance with Open Source VoIP software - Kamailio and RTPEngine. He talked about how the proprietary solutions were difficult to work with, in contrast to using Open Source. This is an excellent presentation about designing and hardening a VoIP solution and limiting its security exposure. What I like about this is that, by choosing the right software and architecture, they seem to have obtained the level of control that was needed to certify their VoIP platform.

The last slide in this presentation was about the certification audit results which said *pentests passed flawlessly*; this of course made me smile. He did explain that while with the previous proprietary solution had various open issues (vulnerabilities), with the open-source solution this was no longer a problem.

This reflects our own personal experience where we were for some time testing the security of a proprietary VoiceXML solution that was meant to be PCI complaint. This had major security issues such as default passwords on administrative interfaces, and keeping such a system up to date with the latest security patches was described as a nightmare by the engineers!

One thing that I should mention is that PCI Penetration Testing is often extremely limited in scope and most security testers doing PCI pentesting are likely to simply look for vulnerabilities that are either detected by vulnerability scanners or web application security issues. Thus they are likely to miss VoIP-specific vulnerabilities through this approach.

Watch the presentation: <https://fosdem.org/2023/schedule/event/secure_voip_payments/>

#### Talks of interest at FOSDEM on robustness, availability and denial of service (DoS)

* Performance optimization for VoIP services, Henning Westerholt
  + The video for this presentation is not online but the slides are. This talk gives some useful tips and hints as to what to avoid and how to address performance issues in VoIP servers (Kamailio).
  + <https://fosdem.org/2023/schedule/event/jitsi_p10k/>
  + <https://skalatan.de/en/archive/presentations/fosdem-2023-presentation.pdf>
* P10K: getting 10000 participants into a Jitsi meeting, Saúl Ibarra Corretgé
  + Tricks about how Jitsi can achieve some impressive statistics. It is interesting to see how they simulate such a number of participants with Selenium Grid.
  + <https://fosdem.org/2023/schedule/event/jitsi_p10k/>
* Scaling Open Source Realtime Messaging System for Millions, Floris van Geel
  + A talk about Rocket.Chat and what they did to scale up.
  + <https://fosdem.org/2023/schedule/event/scaling_rtc_messaging/>
* DDoS attack detection with open source FastNetMon Community, Pavel Odintsov
  + <https://fosdem.org/2023/schedule/event/network_ddos_detection/>

#### Other talks of relevance

* Secure voice/video over IP communications today and tomorrow thanks to post-quantum encryption!
  + Presentation at <https://fosdem.org/2023/schedule/event/security_linphone/>
* How regulating software for the European market could impact FOSS
  + Lightning talks and a panel about the Cyber Resilience Act. It is increasingly looking like an important topic!
  + <https://fosdem.org/2023/schedule/event/cyber_resilience/>
* Peer-to-peer Browser Connectivity
  + Leveraging WebRTC and the new WebTransport protocol to connect libp2p browser nodes.
  + <https://fosdem.org/2023/schedule/event/network_p2p_browser_connectivity/>

### Reports ...