---
title: RTCSec Newsletter March 2023: Trojan 3CX Client, CRA talk, OpenSIPS audit report and much more
url: https://www.rtcsec.com/newsletter/2023-03-rtcsec-news/
source: Real-time communications security on Communication Breakdown - VoIP & WebRTC Security
date: 2023-04-01
fetch_date: 2025-10-04T11:20:34.329648
---

# RTCSec Newsletter March 2023: Trojan 3CX Client, CRA talk, OpenSIPS audit report and much more

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

# March 2023: Trojan 3CX Client, CRA talk, OpenSIPS audit report and much more

Published on Mar 31, 2023

Welcome to the end of March, and this month’s edition of the RTCSec Newsletter. A lot has accumulated in March on the VoIP and IP Communication security front. In fact, this one is packed!

In this edition, we cover:

* Our news, involving CI/CD automation of VoIP security testing with SIPVicious PRO
* More news from us, including the OpenSIPS security audit report and a chat about the Cyber Resilience Act
* 3CX Phone Client turned into a trojan
* Critical vulnerabilities affecting Samsung and Pixel phones via VoLTE and 5G
* Silent fix in Kamailio gets a CVE, vulnerable door phones and various other security reports

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can communicate in real time in a safe way - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). Do:

* forward to that person who may find this newsletter particularly fruitful.
* let us know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Gitlab CI/CD examples with the latest SIPVicious PRO update

On the first week of March, we released a new version of SIPVicious PRO to our customers which makes the toolset more feature-complete. For example, we added new SIP methods to the SIP Flood tool, SRTP support for the RTP fuzzer and the ability to set the RTP payload ID and SSRC for the RTP inject tool.

There were a couple more new features and a number of bug fixes (naturally) - but the main highlight for us was the documentation, actually! The update includes practical examples of how SIPVicious PRO integrates with Gitlab CI/CD pipelines and a live example of SIPVicious PRO running on the public Gitlab CI/CD.

Read all about this on our blog post: [SIPVicious PRO incremental update - and Gitlab CI/CD examples](https://www.enablesecurity.com/blog/sipvicious-pro-with-various-fixes-and-gitlab-ci/), or [get in touch](https://www.enablesecurity.com/contact/) for more details.

### Full OpenSIPS Security Audit Report is published

The OpenSIPS Security Audit was a very important project that we worked on with the OpenSIPS developers during 2021 and 2022. The report is now fully public and we wrote about this in a post which included the following details:

* [What is the OpenSIPS security audit?](https://www.enablesecurity.com/blog/opensips-security-audit-report/#what-is-the-opensips-security-audit)
* [Details about the vulnerability findings and security fixes](https://www.enablesecurity.com/blog/opensips-security-audit-report/#vulnerability-findings-and-security-fixes)
* [The methodology taken, i.e. how OpenSIPS was tested and root cause analysis](https://www.enablesecurity.com/blog/opensips-security-audit-report/#the-actual-work)
* [Do any of these vulnerabilities affect Kamailio too?](https://www.enablesecurity.com/blog/opensips-security-audit-report/#do-any-of-these-vulnerabilities-affect-kamailio-too)
* [How we plan on automating such security testing and making it more future-proof](https://www.enablesecurity.com/blog/opensips-security-audit-report/#the-future-of-security-testing-according-to-us)
* [How we worked with the OpenSIPS developers and community](https://www.enablesecurity.com/blog/opensips-security-audit-report/#thanks-to-the-opensips-developers-and-community)

Something that we’ve been trying to get an answer for in the past days is the question about Kamailio. The answer has proven to be more elusive that originally thought but we’re getting closer to a proper answer.

### TADSummit Special: The EU Cyber Resilience act

The CRA (Cyber Resilience Act) is new legislation that is coming to the EU that enforces a certain level of security for products in the market. Together with Olle E. Johansson, I was invited to talk about how this relates to the IP Communications world. The session was split as follows:

1. Olle first gave an excellent introduction about the Cyber Resilience Act.
2. I presented my mindmap which shows VoIP & WebRTC vulnerabilities in relationship with the CRA’s requirements.
3. Olle gave a presentation of how this all applies to IP Communications.

It was not a short session and packs a lot, taking an hour and a half in total. If you are involved in VoIP and IP Communications, then you should be interested in the CRA - please do watch the whole thing. Alan Quayle did the important job of summarizing the session and included our presentation materials for download on the TADSummit blog. He also linked back to our blog and this very newsletter which covers a lot of the vulnerabilities that were talked about during the session.

Reference: <https://blog.tadsummit.com/2023/03/21/eu-cyber-resilience-act/>

## What’s happening?

### 3CX Phone Client used to distribute malware

Anyone monitoring either VoIP or cyber-security news, could not miss the news that 3CX started distributing a trojanized version of their 3CX Client software. Being a major PBX vendor means that such an incident must have had a wide reach at the level of other incidents such as the one involving SolarWinds.

In preparing this newsletter, I tried to figure out what happened based on the publicly available information. This is also the reason why this edition is particularly late. Anyway, here is my take.

The following is a timeline of what appears to have happened, based on various reports and articles:

* 2022-02-XX: earliest indication of adversary’s infrastructure that was part of this incident was registered
* 2022-12-07: presence of a Github repository used to host icon files with encoded malware; used in stage 2 of the infection
* 2023-03-08: Telemetry from SentinelOne indicated this is the earliest infection attempt for the MacOS infected components
* 2023-03-13: `3CXDesktopApp.exe` malicious binary signed by 3CX
* 2023-03-16: compilation date of the infostealer DLL used in the second stage of the infection
* 2023-03-22: SentinelOne began to see a spike in behavioral detections of the 3CXDesktopApp; 3CX users began discussion of (assumed false-positive) malware detection of 3CXDesktopApp
* 2023-03-29: various blog posts and analysis published about this - SentinelOne, Sophos, Crowdstrike
* 2023-03-30: Mac version is confirmed to also be infected
* 2023-03-30:
  + SentinelOne confirm that the MacOS installer is also trojanized
  + 3CX CEO and CISO posts on their website about the infection, apologizing for the incident and providing some details about affected versions etc
  + US CISA, German BSI issued alerts about the incident
* 2023-03-31: Mandiant appointed to help review 3CX’s security incident

#### What happened?

According to 3CX, their 3CX Client Updat...