---
title: DDoS simulation tutorial, WebRTC IP leak and vulnerable RTC libraries
url: https://www.rtcsec.com/newsletter/2022-11-rtcsec-news/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2022-12-01
fetch_date: 2025-10-04T00:10:51.399820
---

# DDoS simulation tutorial, WebRTC IP leak and vulnerable RTC libraries

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

# DDoS simulation tutorial, WebRTC IP leak and vulnerable RTC libraries

Published on Nov 30, 2022

It is the end of November and with it, we bring some of our own publications and coverage of various advisories, papers and news items in the VoIP and WebRTC security world.

In this edition, we cover:

* How to simulate DDoS attacks on your own
* Details about the new WebRTC IP leak issue
* Coverage of interesting talks at Blackhat and TADSummit
* Advisories concerning Sofia-SIP, Drachtio, PJSIP and more

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let me know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### We are hiring freelance pentesters

Last month we announced that we are looking for persons who are do security testing services on a freelance basis. Our hiring process involves video calls to get to know each other and to understand if we can work together. Then we have the chance of doing a simulation of a penetration test, which allows both parties to experience how an actual engagement would look like and everything that it involves. This includes documentation (reporting), typical challenges involved in pentesting, research and development and discussions that are mostly done over asynchronous chat.

We had a number of very interesting applications but we are looking for more than just one person. Therefore the hiring page will remain open. If you know someone who might be interested and happens to be a freelancer, do send them to this page: [Penetration Testers - Freelancer/Contract-based & Remote](https://hs.enablesecurity.com/join-us/pentester).

### Simulating DDoS attacks: our talk and blog post are out

We published various materials detailing how to simulate DDoS attacks:

1. Video of the talk at TADSummit: <https://www.youtube.com/watch?v=gaVBOuwyON0>
2. Slides for the presentation: <https://www.slideshare.net/sandrogauci/tadsummit-2022-how-to-bring-your-own-rtc-platform-down>
3. Article for those who prefer to read: <https://www.enablesecurity.com/blog/how-to-perform-ddos-simulation/>

TL;DR: A DDoS simulation is a practical exercise that various organisations are capable of doing. Understand the reasons why you would want to do this, then combine custom with off-the-shelf attack tools. Follow the best practices, apply solutions and mitigation; and you can finally answer: *what if we got attacked*?

## What’s happening?

### New WebRTC IP leak discovered and fixed

The audience of this newsletter might be familiar with the fact that the WebRTC browser stack makes IP information available through JavaScript. This has been abused to track users’ internal and external IP addresses and to help sell VPN services too!

Anyway, this actually worked pretty well until around 3 years ago (or Chrome 77) when the behavior of the web browsers was changed so that internal IP addresses are no longer exposed through JavaScript. Instead, the internal IPs were replaced with mDNS addresses as described in a draft RFC [draft-ietf-mmusic-mdns-ice-candidates](https://datatracker.ietf.org/doc/draft-ietf-mmusic-mdns-ice-candidates/). This turned out to be a decent solution to that particular issue.

Except that someone figured that the reference libwebrtc implementation for computing foundations returns a random looking string that is calculated as follows: `CRC32(baseaddress, protocol, relayprotocol)`. This `baseaddress` is actually the IP address that the mDNS technique tried to hide. Trackers could then make use of this hash with a pre-computed lookup table to get the original IP address again. For those familiar with offline password cracking, this is very similar to the rainbow table techniques used to crack MD5 hashes and various other schemes. There is a nifty demo of this by the original reporter on a Github page.

Fear not, however, because our friend Philippe Hancke (and various others) has been on it making sure that a fix is out there. The solution involves seeding the CRC32 with a random 64 bit integer.

At the time, the official Chrome release build does have a fix and this no longer works since Chrome 107. So, we are once again safe from the IP trackers out there.

References:

* Demo: <https://niespodd.github.io/webrtc-local-ip-leak/>
* Repository for demo: <https://github.com/niespodd/webrtc-local-ip-leak>
* Fixes: <https://chromiumdash.appspot.com/commit/08b882d762edadb9797334859d915c5c1e34896b>
* “No longer works” ticket: <https://github.com/niespodd/webrtc-local-ip-leak/issues/3>
* About mDNS fix: <https://bloggeek.me/psa-mdns-and-local-ice-candidates-are-coming/>
* Talk about fixing WebRTC IP leaks: <https://www.youtube.com/watch?v=SqcW8kJAMJg>
* General information about IP leaks in WebRTC: <https://getstream.io/blog/webrtc-ip-leaks/>

### XMPP Stanza Smuggling presentation video

The video of the talk given by Ivan Fratric at Black Hat about “how he hacked Zoom” is now out. We have previously linked to blog posts and bug reports related to this but the talk is what you want to watch if you want to be entertained.

Reference: <https://www.youtube.com/watch?v=ERaRNsvCBrw>

### Talks of interest at TADSummit 2022

I’m writing this almost 3 weeks after returning from TADSummit 2022 in Portugal. Here are some comments about presentations that caught my attention:

* Title: Welcome to vCon! The next leap forward in the programmable communications industry. Thomas Howe
  + <https://www.youtube.com/watch?v=ZBRJ6FcVblc>
  + Why is this interesting? Although not actually a security technology, this open format is there for privacy and tracking purposes, to track content and purpose of the various parts of a conversation, especially personal information. It comes with security properties such as digital identity and tamper proof features. The nice thing about vCon is that this could allow the transfer, sharing and tracking of such information since it is a standard.
* Title: What Everyone Needs to Know about Protecting the CPaaS Ecosystem from Unlawful Robocalls. Gerry Christensen, VP YouMail.
  + <https://www.youtube.com/watch?v=EWBJ-Q4mmEo>
  + It talks about limitations of STIR/SHAKEN and alternative approaches to prevent unlawful calls.

Videos for both days:

* Day 1: <https://www.youtube.com/playlist?list=PLO-gJ4-4x_IKOzIplTKPU-B_vWzCKzVab>
* Day 2: <https://www.youtube.com/playlist?list=PLO-gJ4-4x_ILsSmIWu6w8iBVfvxUSAe6g>

### Sofia-SIP STUN overflow

A Janus user posted on the Sofia-SIP bug tracker asking about a heap-buffer-overflow issue that he is experiencing. The error indicates that the library was compiled using the AddressSanitizer. Further down in the ticket, a security r...