---
title: Highlights from the past year and various security fixes
url: https://www.rtcsec.com/newsletter/2022-12-rtcsec-news/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2022-12-23
fetch_date: 2025-10-04T02:19:13.746297
---

# Highlights from the past year and various security fixes

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

# Highlights from the past year and various security fixes

Published on Dec 22, 2022

Welcome to the last RTCSec newsletter of 2022!

In this edition, we cover:

* Looking back at the past year and best wishes for the New Year
* Jitsi gets verification for E2EE
* OSS-Fuzz now testing PJSIP
* Vulnerabilities fixed in Drachtio, BigBlueButton, Cisco IP Phones and more

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let me know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### So long and see you in 2023!

It has been quite a good year for this newsletter. It grew from just over a hundred subscribers to almost 400. Given its niche topic, no actual advertising, this doesn’t sound too bad. We are very grateful to you, dear reader, for sharing this newsletter with your friends and colleagues who also benefit from reading its contents.

Here are some RTCSec newsletter highlights from 2022:

* The WebRTC vulnerability (CVE-2022-2294) that was abused in the wild to deliver malware covered in [July](https://www.enablesecurity.com/newsletter/2022-07-rtcsec-news/#security-issue-in-webrtc-project-abused-to-deliver-spyware) and [September](https://www.enablesecurity.com/newsletter/2022-09-rtcsec-news/#updates-to-the-heap-buffer-overflow-in-webrtc)
* A [new WebRTC IP leak discovered and fixed](https://www.enablesecurity.com/newsletter/2022-11-rtcsec-news/#new-webrtc-ip-leak-discovered-and-fixed)
* [How Microsoft Teams Direct Routing can be abused in certain SBC configurations](https://www.enablesecurity.com/newsletter/2022-09-rtcsec-news/#abusing-microsoft-teams-direct-routing)
* A number of major vulnerabilities and exploitation in the wild for Mitel equipment, covered in [March](https://www.enablesecurity.com/newsletter/2022-03-rtcsec-news/#cve-2022-26143-mitel-micollab-and-mivoice-business-express-used-to-launch-ddos-attacks), [May](https://www.enablesecurity.com/newsletter/2022-05-rtcsec-news/#mitel-6800-and-6900-series-sip-phone-devices-undocumented-behavior), [June](https://www.enablesecurity.com/newsletter/2022-06-rtcsec-news/#mitel-voip-appliances-used-in-ransomware-attack), [July](https://www.enablesecurity.com/newsletter/2022-07-rtcsec-news/#short-news-and-commentary) and [September](https://www.enablesecurity.com/newsletter/2022-09-rtcsec-news/#mitel-mivoice-abused-for-ransomware)
* For our own personal highlights, do keep reading.

We are issuing this month’s edition a bit earlier because, like most, we are going to take some time off for the next few weeks. We’ll be doing our fair share of reflecting over the past year but also very much looking forward and preparing for the next one.

Until then, we wish you all restful holidays!

### Looking back at 2022 for Enable Security

It was a very busy year for us this one. Yet, we had less publications than some of the past years because our customers kept us truly busy. Most of the work that we did, naturally, we cannot talk about given the nature of [penetration testing](https://www.enablesecurity.com/security-audits/). To cater for our and our customer’s success, we have been expanding and hiring security researchers, both as part of the core team at Enable Security and [specialized freelancers](https://hs.enablesecurity.com/join-us/pentester) . As anyone doing any hiring knows, this is not easy, but we have quite some progress on that front.

That said, we did have a couple of publications that I would like to celebrate:

* [Exploiting CVE-2022-0778, a bug in OpenSSL vis-à-vis WebRTC platforms](https://www.enablesecurity.com/blog/exploiting-cve-2022-0778-in-openssl-vs-webrtc-platforms/)
* [How to perform a DDoS attack simulation](https://www.enablesecurity.com/blog/how-to-perform-ddos-simulation/) and the related [TADSummit talk which is available on Youtube](https://www.youtube.com/watch?v=gaVBOuwyON0)
* The [OpenSIPS security audit report is out](https://www.enablesecurity.com/newsletter/2022-05-rtcsec-news/)
* [SIPVicious PRO experimental now supports STIR/SHAKEN and 5 new tools](https://www.enablesecurity.com/blog/sipviciouspro-with-stir-shaken-support-and-new-tools/)
* [SIPVicious PRO is now available as a docker image](https://github.com/EnableSecurity/svpro-docker/)

We have been constantly refining and developing our internal tools and knowledge that hopefully, we’ll be able to publish more of next year. In fact, we wrote a little about an internal tool called [Gasoline v2](https://www.enablesecurity.com/newsletter/2022-08-rtcsec-news/#gasoline-v2-giving-us-decent-results) and our [Attack Platform](https://www.enablesecurity.com/newsletter/2022-08-rtcsec-news/#enable-securitys-attack-platform-being-used-by-customers) in August’s newsletter. Thanks to these improvements, we have covered a number of DDoS simulations and Penetration Testing of various targets, many SIP based, a number of APIs, messaging protocols such as SMPP and MM4, and most interestingly - our latest favourite complex beast: WebRTC. Finally, we have made consultancy a regular thing that brings us closer to our customers which is an approach that we are very comfortable with.

If you have been considering working with us for the next year, now seems like a good time as [ever to get in touch](https://www.enablesecurity.com/contact/).

## What’s happening?

### Jitsi Meet upgraded its E2EE with verification

Jitsi Meet has had end-to-end-encryption (E2EE) support since a while but until now, you could not verify the users. Thus as a participant in a call, you did not have straightforward cryptographic proof that who you’re speaking to is who they claim to be. Well, now Jitsi also has user verification. One fun part is that when doing user verification, you get to read off the names of various Emojis and confirm with the other party that that is also what they see on their screen. Then you can mark the other user as verified so that future calls do not require this fancy, but useful procedure.

It is still beta - but essentially looks exactly like Matrix’s simply because Jitsi’s developers are using the Matrix open source protocol and libraries.

Incidentally, this was something that Martin R. Albrecht and other researchers helped convince Jitsi in finally implementing. These same researchers have previously published vulnerabilities (also covered in a past RTCSec newsletter) in other E2EE chat and conferencing services like Matrix.

References:

* Jitsi blog post: <https://jitsi.org/blog/trust-but-verify-introducing-user-verification/>
* Tweet from Albrecht: <https://twitter.com/martinralbrecht/status/1600241405703516160>
* Matrix vulnerabilities: <https://nebuchadnezzar-megolm.gi...