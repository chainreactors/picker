---
title: The Dangers of Transition Mode
url: https://trustedsec.com/blog/the-dangers-of-transition-mode
source: TrustedSec
date: 2024-07-03
fetch_date: 2025-10-06T17:45:30.479759
---

# The Dangers of Transition Mode

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [The Dangers of Transition Mode](https://trustedsec.com/blog/the-dangers-of-transition-mode)

July 02, 2024

# The Dangers of Transition Mode

Written by
Michael Bond and
David Boyd

Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/DangersOfTransitionMode_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1719499083&s=22187f8cf6f3d5a2272dbb4f745c7307)

Table of contents

* [Remediation](#Remediation)
* [Conclusion](#Conclusion)
* [References](#References)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#edd29e988f87888e99d0ae85888e86c8dfdd829899c8dfdd9985849ec8dfdd8c9f99848e8188c8dfdd8b9f8280c8dfddb99f989e998889be888ec8dfdccb8c809dd68f828994d0b98588c8dfdda98c838a889f9ec8dfdd828bc8dfddb99f8c839e8499848283c8dfdda0828988c8deacc8dfdd8599999d9ec8deacc8dfabc8dfab999f989e9988899e888ec38e8280c8dfab8f81828ac8dfab998588c0898c838a889f9ec0828bc0999f8c839e8499848283c080828988 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode "Share on Facebook")
* [Share on X](http://twitter.com/share?text=The%20Dangers%20of%20Transition%20Mode%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode&mini=true "Share on LinkedIn")

With the introduction of WPA3, it is becoming increasingly difficult to successfully exploit a wireless network. One of the main enhancements introduced in WPA3 is the Simultaneous Authentication of Equals (SAE) model. SAE was designed to replace the vulnerable Pre-Shared Key (PSK) method used in WPA2.

A WPA2 Personal network is susceptible to PSK passphrase brute-force attacks, where the 4-way handshake packets are captured during the authentication process. The hashed PSK is then extracted from these packets and transferred off-line in an attempt to recover the cleartext password with an application like [Hashcat](https://hashcat.net/hashcat/).

Once the cleartext PSK has been recovered, it can be used to connect to the wireless network and eavesdrop on other connected devices, or potentially used to gain a foothold within the internal network. One of the security enhancements with WPA3 is that the packets remain encrypted, and eavesdropping is not possible, even if the PSK password is guessed or known.

Another security enhancement is that WPA3 networks require the use of Protected Management Frames (PMF). With this requirement, management frames are not vulnerable to PKMID clientless attacks.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_1.png?w=320&q=90&auto=format&fit=max&dm=1719499195&s=65fad30e6d592f4fb2b3de09684ff997)

Figure 1 - WPA3 Handshake Layout

During a recent Wireless Penetration Test, we encountered a wireless network where WPA3 was advertised. Knowing the WPA3 security enhancements, it was assumed this assessment would be quick, with very little to be reported. However, an interesting discovery was made while reviewing the packet capture. The Service Set Identifier (SSID) of the WPA3 network was also being advertised as a WPA2 network.

To recreate the attack, we configured a lab environment with an SSID utilizing WPA3, in order to test what attack possibilities existed. Additional sample sets were collected against a MikroTik wireless router, a Cisco Meraki AP, an Ubiquiti wireless AP, and an Aruba AP.

To begin, we needed to locate and determine visible and hidden SSIDs, hardware information, signal strength, clients connecting, and encryption protocols in use. Within the lab environment, we leveraged the [aircrack-ng](https://www.aircrack-ng.org/) suite toolkit.

First, we enumerated the SSIDs with airodump-ng. We took note of the channels utilized, as well as the Basic Service Set Identifier (BSSID).

```
sudo airodump-ng <wlan>
```

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_2.png?w=320&q=90&auto=format&fit=max&dm=1719499196&s=4f206fc9e81f02ed18dd91494f424ad3)

Figure 2 - Enumerating SSIDs

Next, we began capturing packets:

```
sudo airodump-ng <wlan> --channel <channel> --bssid <bssid> -w capture
```

*Tip: Click the 'Tab' key when seeing multiple SSIDs to add color for better readability and be able and shift through the list.*

 Looking at the captured data, we found a wireless network that was configured with WPA3 Personal.

![](https://trusted-sec.transforms...