---
title: April 2023: 3CX incident updates, WebRTC security and H264
url: https://www.rtcsec.com/newsletter/2023-04-rtcsec-news/
source: Real-time communications security on Communication Breakdown - VoIP & WebRTC Security
date: 2023-04-29
fetch_date: 2025-10-04T11:32:42.177712
---

# April 2023: 3CX incident updates, WebRTC security and H264

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

# April 2023: 3CX incident updates, WebRTC security and H264

Published on Apr 28, 2023

April brings with it conference announcements, updates to the 3CX incident and a very interesting paper about the most popular video codec.

In this edition, we cover:

* New fuzzing of RTP codecs with SIPVicious PRO
* Details about our WebRTC security presentation for CommCon
* News about the 3CX compromise
* and much much more!

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let us know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Fuzzing more RTP codecs with SIPVicious PRO

SIPVicious PRO’s experimental build allows fuzzing of VoIP media or RTP. When we introduced this back in July 2022, we supported ulaw, alaw and opus. This gave some interesting results and uncovered crashes for our customers. Therefore we have been expanding our coverage and the next experimental release will support the following new codecs:

* GSM (gsm0610)
* G722
* G729
* G726-32

A bit of testing against real-life software shows that this is effective and important because we did find new crashes during our limited testing. We’ll be adding more, publishing some results and making this available to our SIPVicious PRO [self-serve members and up](https://www.enablesecurity.com/membership/). Reply to this email or [get in touch for more details](https://www.enablesecurity.com/contact/).

### CommCon in June and our presentation about WebRTC & Video Delivery security

CommCon is a residential conference in the UK covering the open source media industry. It will take place in June this year and, for the first time, we’ll be visiting in person after having covered the online versions that happened during the pandemic. There are various interesting topics that will be covered by the different speakers but till now, it looks like our presentation is the only one that is primarily about security.

Therefore, we’re very pleased to announce our talk called: *WebRTC & Video Delivery application security - what could possibly go wrong?*

The synopsis is as follows:

> WebRTC is often considered to be *secure by default* - with most security concerns being around IP address leakage which is more of a privacy issue than anything. Well, I have news for you - the applications and infrastructure that handles WebRTC can be attacked. It may indeed have various types of security vulnerabilities which are often overlooked. This presentation is based on experiences gained through security testing of WebRTC applications with anecdotal stories to illustrate the dangers. We will also take a peek at Video Delivery mechanisms such as RIST and SRT and discuss what could possibly go wrong there too!

More details:

* Details of our talk: <https://2023.commcon.xyz/talks/webrtc-video-delivery-application-security-what-could-possibly-go-wrong/>
* Rest of the talks at CommCon: <https://2023.commcon.xyz/talks/>

## What’s happening?

### Updates on the 3CX supply chain compromise

When we published [last month’s newsletter](https://www.enablesecurity.com/newsletter/2023-03-rtcsec-news/#3cx-phone-client-used-to-distribute-malware), the 3CX incident was still unfolding. Since then, researchers continued the investigation on the incident and revealed more information.

On April 3rd, Kaspersky published [a report](https://securelist.com/gopuram-backdoor-deployed-through-3cx-supply-chain-attack/109344/) on the incident which emphasizes that the Lazarus group as the threat actor, and reports that they found “**Gopuram**” Windows malware which is linked to the threat actor.

On April 11th, 3CX published the initial results from Mandiant (who they hired) in [a blog post](https://www.3cx.com/blog/news/mandiant-initial-results/). In the blog post they mention three pieces of malware:

* **TAXHAUL** for persistence on Windows
* **POOLRAT** for MacOS
* **COLDCAT** for Windows

They highlight that COLDCAT is different from Gopuram. They also mention that the threat actor is UNC4736 which *has a North Korean nexus*.

On April 20th, Mandiant published [a full detail report](https://www.mandiant.com/resources/blog/3cx-software-supply-chain-compromise) on the incident and said that they *identified that the initial compromise vector of 3CX’s network was via malicious software (**X\_TRADER**) downloaded from Trading Technologies website by one of the employees*. The software contained **VEILEDSIGNAL** malware which stole the employee’s 3CX corporate credentials from his system. *This is the first time Mandiant has seen a software supply chain attack lead to another software supply chain attack*.

So finally we can draw the steps as below:

1. Compromise of `www.tradingtechnologies[.]com` and distribution of compromised **X\_TRADER** updates
2. Infecting a 3CX employee and stealing employee’s 3CX corporate credentials
3. Accessing 3CX build environments and infecting them
4. Infecting 3CX clients and users

References:

* <https://securelist.com/gopuram-backdoor-deployed-through-3cx-supply-chain-attack/109344/>
* <https://www.3cx.com/blog/news/mandiant-initial-results/>
* <https://www.mandiant.com/resources/blog/3cx-software-supply-chain-compromise>

### H.264; The Most Dangerous Codec in the World?

Three researchers from the University of Texas and Oberlin College published a paper titled “The Most Dangerous Codec in the World: Finding and Exploiting Vulnerabilities in H.264 Decoders”. The paper begins by describing the complexity of H.264 codec which is one of the most popular video codecs:

> The H.264 specification is 800 pages long—despite specifying only how to decode video, not how to encode it.
>
> *from the paper*

The paper introduces H26FORGE which is a *domain-specific infrastructure for analyzing, generating, and manipulating syntactically correct but semantically spec-non-compliant video files*. In other words, it is a toolset consisting of a grammar-aware fuzzer for generating H.264 video files, and tools for analyzing and manipulating the files. The researchers used the tool to discover vulnerabilities in video decoder ecosystems and found the following vulnerabilities and more:

* CVE-2022-32939: Buffer overflow in AppleD5500, the video decoder driver shipped with iOS and iPadOS operating systems; causes memory corruption and kernel panic
* CVE-2022-42846: Infinite loop in AppleD5500 affected iOS and iPadOS; causes DoS and kernel panic
* CVE-2022-3266: out-of-bounds read (led Firefox GPU utility process to crash) and ...