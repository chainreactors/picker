---
title: July 2024: WebRTC flaws that suddenly appear out of nowhere, hardphone security and more!
url: https://www.rtcsec.com/newsletter/2024-07-rtcsec-news/
source: Real-time communications security on Communication Breakdown - VoIP & WebRTC Security
date: 2024-08-01
fetch_date: 2025-10-06T18:03:00.387994
---

# July 2024: WebRTC flaws that suddenly appear out of nowhere, hardphone security and more!

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

# July 2024: WebRTC flaws that suddenly appear out of nowhere, hardphone security and more!

Published on Jul 31, 2024

Welcome to the July edition of your favorite VoIP and WebRTC security newsletter. While many are slowing down this time of year, we are ramping up our efforts.

In this edition, we cover:

* Much news from us, including a podcast, pentesting and OWASP ASVS
* WebRTC project vulnerabilities that were previously hidden
* Hardware phone security research and exploitation
* Low-latency VoIP Security Analytics and Anonymization challenges and Twilio troubles

The RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security determines if you can safely communicate in real time - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). If you like what we’re doing, you’re most welcome to:

* Forward it to those who may find this newsletter particularly fruitful.
* Let us know if there are any RTC security news items we should cover.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### OWASP ASVS: Adding WebRTC Security Requirements

We’re excited to share our recent involvement in a significant initiative to add WebRTC security requirements to the OWASP ASVS. For those unfamiliar, the OWASP Application Security Verification Standard (ASVS) project is a comprehensive framework that sets a standard for application security verification. It provides a basis for testing web application security controls and offers developers a list of requirements for secure development.

Our team has been actively contributing to a GitHub issue titled “[Request for Addition of WebRTC Security Subcategory in ASVS](https://github.com/OWASP/ASVS/issues/1612).”

Recognizing the growing importance of WebRTC in modern web applications, we are adding relevant entries specific to WebRTC security. Our contributions are based on our extensive experience in penetration testing, security research, and bug bounties within the WebRTC security domain.

Some key areas we’re focusing on include:

* Robust signalling that withstands Denial of Service attacks
* Handling media attacks
* TURN server vulnerabilities
* Best practices for implementing WebRTC securely

This conversation is ongoing, and the work is still in progress. We are keen to ensure that the ASVS evolves to address the unique security challenges posed by WebRTC implementations.

We invite our readers with expertise or insights in WebRTC security to join the conversation. Your contributions could help shape the future of WebRTC security standards and practices. If you have any suggestions or would like to participate, please visit the GitHub issue and share your thoughts.

By collaborating on this initiative, we aim to enhance the overall security posture of WebRTC applications and contribute to a safer web ecosystem for all users.

### TADSummit Innovators Podcast reviews the Last 6 Months of RTC Security Trends

Last week, I had the pleasure of joining Alan Quayle on the TADSummit Innovators Podcast to review the last six months of VoIP and WebRTC security news, which means that this very newsletter was the main feature of the episode. We delved into some of the most intriguing trends emerging in the RTC security space.

We covered the following RTC security trends for 2024 so far:

1. Increasing focus on WebRTC vulnerabilities and security
2. Growing concern over VoIP and conferencing platform security
3. Emerging threats from AI and machine learning in audio manipulation
4. Growing importance of resilience in communication systems
5. SMS/Voice 2FA is hugely problematic

Here are the top 10 insights that emerged from our discussion:

1. Specialized knowledge in WebRTC and VoIP security is crucial for addressing niche vulnerabilities.
2. AI can scale attacks on VoIP systems, making them more dangerous.
3. The resilience of communication technologies is critical for maintaining security during crises.
4. Continuous improvement and adaptation are essential for cybersecurity in the face of evolving threats.
5. Reliance on outdated security practices exposes modern communication systems to greater risks.
6. The RTC Security Newsletter is essential reading for telecom and IP communications professionals.
7. Denial of service attacks remain a major threat to real-time communications.
8. Two-factor authentication via SMS and voice calls is insecure and outdated.
9. The industry needs more security testers with expertise in VoIP and WebRTC.
10. Regular pentesting is critical to identify and fix vulnerabilities in VoIP and WebRTC systems.

For more detailed insights, [read Alan’s podcast episode summary](https://blog.tadsummit.com/2024/07/24/sandro-gauci-enable-security/) on the TADSummit blog or watch and listen to the whole episode on [YouTube](https://www.youtube.com/watch?v=TpDUd3tzGdw).

### Migrating the newsletter and content to EnableSecurity.com

As we had [already announced](https://www.enablesecurity.com/newsletter/2024-04-rtcsec-news/#migrating-the-newsletter-and-content-to-enablesecuritycom), over the next few weeks and months, we will be transitioning all content, including this newsletter, from rtcsec.com to enablesecurity.com. Enable Security has always been the driving force behind RTCSec, a fact we’ve proudly shared. However, managing multiple websites has proven to be inefficient for various reasons. By consolidating our resources under one platform, we aim to enhance our efforts in bringing cybersecurity to VoIP and WebRTC domains. If you notice any glitches, please do not hesitate to let us know!

## What’s happening?

### Two New CVEs Published for WebRTC Vulnerabilities Fixed in the Past Two Years

Two new CVEs have been published for vulnerabilities in the WebRTC project that were fixed in the past two years.

The first vulnerability, tracked as CVE-2023-7010, is a dangling pointer issue discovered by Ned Williamson of Google Project Zero last year. The now-public [bug report](https://issues.chromium.org/issues/40070891) describes it as follows:

> A dangling pointer vulnerability is present in WebRTC’s `PacketRouter` due to an SDP SIM group SSRC from one track (e.g., video) colliding with an existing SSRC from a different track (e.g., audio). This inconsistency between the `send_modules_map_` and the `send_modules_list_` can lead to a use after free.

The second vulnerability, tracked as CVE-2024-3170, was reported by an anonymous individual and [verified using Google’s Clusterfuzz](https://issues.chromium.org/issues/41488824). It appears to have been discovered through new test cases added to an internal Chrome fuzzer (`b0ring_webidl_fuzzer`), which is [private](https://groups.google.com/a/chromium.org/g/clusterfuzz-dev/c/U9pWs3Dt1lw?pli=1).

Both security issues were fix...