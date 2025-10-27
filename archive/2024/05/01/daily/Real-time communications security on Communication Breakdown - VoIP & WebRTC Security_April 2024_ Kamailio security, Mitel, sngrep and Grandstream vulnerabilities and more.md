---
title: April 2024: Kamailio security, Mitel, sngrep and Grandstream vulnerabilities and more
url: https://www.rtcsec.com/newsletter/2024-04-rtcsec-news/
source: Real-time communications security on Communication Breakdown - VoIP & WebRTC Security
date: 2024-05-01
fetch_date: 2025-10-06T17:17:29.273176
---

# April 2024: Kamailio security, Mitel, sngrep and Grandstream vulnerabilities and more

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

# April 2024: Kamailio security, Mitel, sngrep and Grandstream vulnerabilities and more

Published on Apr 30, 2024

Welcome to the April edition of the VoIP and WebRTC security monthly newsletter.

In this edition, we cover:

* Kamailio World 2024 review
* Our short and longer presentation on insecure Kamailio configuration patterns
* Changes to the newsletter
* Updates to T-Pot honeypot, sngrep security fixes, Mitel IP Phone vulnerabilities
* New security course on WebRTC by BlogGeek.me
* And some more!

RTCSec newsletter is a free periodic newsletter bringing you commentary and news around VoIP and WebRTC security. We cover both defensive and offensive security as they relate to Real-time Communications.

What is RTC security anyway? Real-time communications security is what determines if you can safely communicate in real time - whether it be with other humans or machines.

You may sign up to receive the RTCSec newsletter [here](https://www.enablesecurity.com/subscribe/). If you like what we’re doing, you’re most welcome to:

* forward to those that may find this newsletter particularly fruitful.
* let us know if we should include or cover any RTC security news.

To view past issues, please visit our website at <https://www.enablesecurity.com/newsletter/>.

---

## Our news

### Enable Security at Kamailio World and a very short presentation

This month I had the pleasure of visiting Kamailio World in Berlin and attend various presentations, some of which we cover below in this newsletter. The second day included a session called *5 Minutes 5 Slides*, which encourages participants to present about what they do, and also talk about how they use Kamailio.

I took the opportunity to introduce this very newsletter, briefly tell the audience about our penetration tests on VoIP and WebRTC environments. In the main part of this short presentation I showed two examples of Kamailio configurations that we reviewed during our work that were vulnerable to specific security issues. One of them showed misuse of the `dns_query` function that could lead to DoS, while the other showed misuse of the `avp_db_query` function that could lead to SQL injection.

My 5 minute slot can be watched on [Youtube](https://youtu.be/_e0fWnWWOeY?list=PLDaEs5k2Xy-sGcdNOWHfiB6zYKd4q0roM&t=11704) and the [slides also available](https://docs.google.com/presentation/d/1iFoumNzDfCraoEbcglGm320hbl_dbFhc2chLOlC2Msw/edit?usp=sharing).

### Migrating the newsletter and content to EnableSecurity.com

We have an update regarding this newsletter: over the next few weeks and months, we will be transitioning all content, including this very newsletter, from rtcsec.com to enablesecurity.com. As you may know, Enable Security has always been the driving force behind RTCSec, a fact we’ve proudly shared. However, managing multiple websites has proven to be inefficient for a variety of reasons. By consolidating our resources under one roof, we aim to make our efforts to bring cybersecurity to VoIP and WebRTC domains more effective. If you notice any glitches, please do not hesitate to let us know!

### Security Pitfalls in Kamailio Configuration Patterns

During the 5 minutes 5 slides session at Kamailio World this year, I briefly alluded to having a more complete presentation with further examples of significant security findings from our past security audits of Kamailio environments. The work-in-progress document currently includes the following:

* Open relay via R-URI may lead to SIP amplification DoS abuse and more (CVSS: 9.3)
* Open relay via Route header may lead to SIP amplification DoS abuse and more (CVSS: 9.3)
* Use of the function `avp_db_query` in Kamailio configuration leads to SQL injection (CVSS: 9.8)
* The function `dns_query` in Kamailio configuration might lead to DoS (CVSS: 7.5)
* Kamailio configured to relay all calls to carrier without any authentication (CVSS: 7.5)
* Remote Code Execution via unauthenticated specially crafted NOTIFY message (CVSS: 10.0)
* SIP MESSAGE does not require authentication, leading to spam (CVSS: 5.3)
* Denial of Service via in-dialog INVITE messages (CVSS: 7.5)

If you are interested in discussing these vulnerabilities further, I would be happy to share this document. All I ask in return is honest feedback to help us improve our material!

Simply reply to this newsletter or [use the Enable Security communication channels](https://www.enablesecurity.com/contact/), introduce yourself and say hello.

## What’s happening?

### Major update in T-Pot release 24.04.0

T-Pot is a honeypot platform from Deutsche Telekom Security that includes a number of VoIP deception components. They have a [new major release v24.04](https://github.security.telekom.com/2024/04/honeypot-tpot-24.04-released.html). In terms of VoIP, we see the following honeypots being included that support SIP:

* [SentryPeer](https://sentrypeer.org/)
* [qHoneypots](https://github.com/qeeqbox/honeypots) (includes QSIPServer which uses Twisted.sip)

The data collected from T-Pot installations is (by default) fed into [Sicherheitstacho](https://www.sicherheitstacho.eu/) which is quite fun to watch, although somehow I see none of the VoIP related traffic; which should be showing up since port 5060 receives a lot of scans.

### Mitel IP Phone vulnerabilities walk through and security fixes

Danish company Baldur released a [blog post](https://baldur.dk/blog/embedded-mitel-exploitation.html) about vulnerabilities that they found in Mitel IP phones. They identified various vulnerabilities which they chained to get their favorite music playing on the phone and take full control of the devices.

This blog post is a valuable resource for security researchers and developers interested in the intricacies of compromising hardware SIP phones. Following this research, Mitel issued several security fixes, which are documented on the [Mitel Security Advisories](https://www.mitel.com/support/security-advisories) page. The issues are tracked under the following identifiers:

* [CVE-2024-31963 (Mitel Advisory ID 24-0006)](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0006)
* [CVE-2024-31964 (Mitel Advisory ID 24-0007)](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0007)
* [CVE-2024-31965 (Mitel Advisory ID 24-0008)](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0008)
* [CVE-2024-31966 (Mitel Advisory ID 24-0009)](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0009)
* [CVE-2024-31967 (Mitel Advisory ID 24-0010)](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-24-0010)

### Update on the WebRTC vulnerability (CVE-2024-1580) that affected Apple software

[Last month](https://www.enablesecurity.com/newsletter/2024-03-rtcsec-news/#details-on-cve-2024-1580-vulnerability-in-ios-ipados-macos-and-safaris-webrtc-and-coremedia) we wrote about a security fix affecting Safari’s WebRTC and CoreMedia, which was due to a vulnerability in the library dav1d. Philipp Hancke clar...