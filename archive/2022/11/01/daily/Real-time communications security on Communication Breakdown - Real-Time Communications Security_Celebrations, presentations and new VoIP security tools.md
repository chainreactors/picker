---
title: Celebrations, presentations and new VoIP security tools
url: https://www.rtcsec.com/newsletter/2022-10-rtcsec-news/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2022-11-01
fetch_date: 2025-10-03T21:24:48.907773
---

# Celebrations, presentations and new VoIP security tools

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

# Celebrations, presentations and new VoIP security tools

Published on Oct 31, 2022

Welcome to a jam-packed edition of RTCSec newsletter for October. What have we this month?

In this edition, we cover:

* This very newsletter is one year old!
* We’re looking for freelance pentesters to join us
* This time, 12 years ago in VoIP security incidents (Sality botnet scanning)
* Upcoming and past presentations of interest at TADSummit, CTI-Summit, Blackhat & ClueCon
* WebRTC security news: the “most secure VoIP” award and censorship busting
* New VoIP security tools and workshop by Jose Luis Verdeguer (Pepelux)
* And various security advisories, and other reports of concern

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let me know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Happy birthday to RTCSec newsletter!

We launched this newsletter back in [October 2021](https://www.enablesecurity.com/newsletter/2021-10-rtcsec-news/) which makes it now one year old. And growing it has been, covering more and more VoIP and WebRTC security related matters each month. As always, if you have suggestions, we’re [all ears](https://www.enablesecurity.com/contact/). And if you think it is useful to any of your friends and colleagues, do share it with them or let them know that they can subscribe here: <https://www.enablesecurity.com/subscribe/>.

### We are looking for Freelance Penetration Testers

We’re looking for pentesters who love dealing with network protocols, debugging obscure behaviors and perhaps, share a familiarity with real-time communications security. Do you know someone (maybe you!) who might be fit? Please find the description of the role here: [Penetration Testers - Freelancer/Contract-based & Remote](https://hs.enablesecurity.com/join-us/pentester)

### Distributed SIP scanning, 12 years ago over Halloween weekend

Apart from scoring one year since we launched RTCSec newsletter, this month also marks 12 years since we first observed distributed SIP scanning *in the wild*. The traffic came from a botnet that had deployed a modified version of SIPVicious OSS. Eventually we learned that this botnet was called Sality which was documented later in 2011.

References:

* original blog post from November 2010: <https://blog.sipvicious.com/2010/11/distributed-sip-scanning-during/>
* CAIDA research paper on Sality botnet and SIP scanning: <https://catalog.caida.org/paper/2015_analysis_slash_zero>

## What’s happening?

### TADSummit 2022 is happening on 8 and 9 November

GoContact will be hosting TADSummit 2022 next month, where yours truly will be presenting about DDoS as they affect real-time communications systems. I will also be joining Alan Quayle in coordinating a workshop / discussion session about this very topic. While many of the scheduled talks are not RTC security specific, the following might be interesting to this audience:

* Open Source Telecom Software Survey Results. Alan Quayle (covers various aspects of security)
* eSIM as Root of Trust for IoT security. João Casal, Head of R&D at Truphone
* Playing at the intersection of CPaaS and Digital Identity. Kola Layokun, Telesign
* What Everyone Needs to Know about Protecting the CPaaS Ecosystem from Unlawful Robocalls. Gerry Christensen, VP YouMail
* Supercharging CPaaS Growth & Margins with Identity and Authentication. Aditya Khurjekar, GM Prove Protocol

If you’re around, do come say hello! And if not, check out the timings and live-stream the sessions of interest.

References

* <https://blog.tadsummit.com/2022/10/20/tadsummit-2022-timings/>
* <https://www.youtube.com/user/TADSummit>

### WebRTC is the most secure VoIP protocol

Bloggeek.me published a new post explaining why WebRTC is by design, the most secure “VoIP protocol”, as opposed to traditional SIP-based VoIP. The article is short and to the point, listing why WebRTC is superior, essentially because (I quote):

* It is encrypted
* Requires signaling to be encrypted
* Enables end-to-end encryption via media servers by using Insertable Streams

At round tables and in various private conversations, this has also been my personal conclusion. If you are designing a new RTC solution, it makes a lot of sense to make use of WebRTC because of the various built-in security advantages. That said, I have also argued that the WebRTC attack surface is quite large given the number of protocols, layers and applications involved. This makes it a very interesting target especially since almost every WebRTC solution relies on just a few software projects in combination with various custom signalling protocols. So, although I would recommend WebRTC for new projects, I would also caution that in terms of threat modelling, one has to account for more elements and complexity than in a simpler SIP-based VoIP solution.

In response to the Bloggeek.me’s article, Nir Simionovich wrote the following on his [Linkedin](https://www.linkedin.com/posts/nir-simionovich_webrtc-activity-6983166820807553024-A3Q3):

> WebRTC is superior to traditional VoIP in many aspects - however, as you stated yourself - it’s just a building block. And just like any other block, in the hands of the unskilled - it’s a ticking time bomb.
>
> An encrypted media and signalling layer doesn’t help, if your implementation doesn’t account for proper authorization. An encrypted signalling layer doesn’t do any good if the payloads are predictable.
>
> In other words, WebRTC is awesome in providing the developer with the right tools - but like any other tool out there, it doesn’t explicitly enforce a “secured solution design”. It is the job of the various platforms and libraries to provide an “opinionated” WebRTC design/architecture/work-flow, to ensure the developed applications are really secured.
>
> Over the course of the past 15 years I’ve helped companies secure their VoIP products. Same applies for the past 6 years with WebRTC. We invested countless hours into designing our platform worksflows, to ensure tighter security and privacy - be it traditional VoIP (SIP) or WebRTC. Please don’t turn WebRTC into 1999’s equivalent of a firewall - it’s not a magical solution or a silver bullet. It’s just a tool - a good one - but even the best hammer can smash your finger.

Reference to the original article: <https://bloggeek.me/webrtc-is-the-most-secure-voip-protocol/>

### Snowflake uses WebRTC data channels to bypass censorship

Tor project describes Snowflake in these ways:

> Snowflake is a system that **allows people from all over the world to access censored websites and applications**.

> Snowflake is a new WebRTC Pluggable Transport....