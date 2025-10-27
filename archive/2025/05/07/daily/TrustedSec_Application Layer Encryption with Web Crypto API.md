---
title: Application Layer Encryption with Web Crypto API
url: https://trustedsec.com/blog/application-layer-encryption-with-web-crypto-api
source: TrustedSec
date: 2025-05-07
fetch_date: 2025-10-06T22:30:18.944044
---

# Application Layer Encryption with Web Crypto API

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
* [Application Layer Encryption with Web Crypto API](https://trustedsec.com/blog/application-layer-encryption-with-web-crypto-api)

May 06, 2025

# Application Layer Encryption with Web Crypto API

Written by
Drew Kirkpatrick

Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ApplicationLayerEncryption_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1745954231&s=71578fb98ae0f794b1f7ba1b7fa15267)

Table of contents

* [Overview](#Overview)
* [A Key Starting Point](#StartingPoint)
* [Make it Hybrid](#Hybrid)
* [Wrap-Up](#WrapUp)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e5da9690878f808691d8a68d80868ec0d7d58a9091c0d7d5918d8c96c0d7d58497918c868980c0d7d583978a88c0d7d5b1979096918081b68086c0d7d4c3848895de878a819cd8a49595898c8684918c8a8bc0d7d5a9849c8097c0d7d5a08b86979c95918c8a8bc0d7d5928c918dc0d7d5b28087c0d7d5a6979c95918ac0d7d5a4b5acc0d6a4c0d7d58d91919596c0d6a4c0d7a3c0d7a391979096918081968086cb868a88c0d7a387898a82c0d7a3849595898c8684918c8a8bc889849c8097c8808b86979c95918c8a8bc8928c918dc8928087c886979c95918ac884958c "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fapplication-layer-encryption-with-web-crypto-api "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Application%20Layer%20Encryption%20with%20Web%20Crypto%20API%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fapplication-layer-encryption-with-web-crypto-api "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fapplication-layer-encryption-with-web-crypto-api&mini=true "Share on LinkedIn")

## Overview

In web and mobile applications, we’ve been fortunate over the years to have such widespread use of HTTPS by way of TLS. The proliferation of HTTPS is in no small part due to [Let’s Encrypt](https://letsencrypt.org/), which provides free and easily automated TLS certificates. In 2013 when ***Let’s Encrypt*** was founded, 27% of websites used HTTPS. Today, over 85% of websites are using HTTPS (Electronic Frontier Foundation (EFF) [reference](https://www.eff.org/deeplinks/2023/08/celebrating-ten-years-encrypting-web-lets-encrypt)). The use of public Wi-Fi often resulted in use of VPNs by the more security minded of us years ago, but with HTTPS in use on most sensitive applications, this is rarely needed these days, even on untrusted networks.

Still, there are scenarios where the robust security of TLS encryption might not be quite enough. Untrusted end-users of an application can easily view and manipulate web traffic before TLS encryption. Intermediary proxies or TLS termination points also may not be trusted. It’s common to perform TLS termination in third-party vendors like Cloudflare, but some applications may consider that undesired exposure of their data.

There’s also the possibility that the server itself doesn’t need to know the unencrypted data and is simply storing or forwarding the data on behalf of the client. Some sneaky individuals may also be obfuscating C2 traffic using application-level encryption :eyes:

These scenarios are where application layer encryption can be useful, and the Web Crypto API is built into web browsers just for this use case and is accessible through JavaScript. It provides several efficient encryption and secure random number generation features to JavaScript code.

## A Key Starting Point

Let’s start with a simpler example of using symmetrical keys in Web Crypto. Note that while symmetrical key encryption/decryption is very efficient, you must find a way to securely transmit the key. In the case where the server will never decrypt the traffic and is simply storing or forwarding the encrypted data, symmetrical is likely a fine design choice with the client-side holding onto the key.

A more common use is to leverage public/private keys to establish a secure channel to share a symmetrical key and then shift to using the symmetric key for efficiency. We’ll demo symmetric key usage, public/private key usage, and then the hybrid approach where public/private keys are used to share a symmetric key securely.

For the example of symmetrical keys, we’ll generate an encryption key, encrypt a message, and send it to the server to decrypt and return. For the server to be able to decrypt this, it will need the encryption key, which we’ll simply add to the message for demonstration purposes. In practice, you would have transmitted the key using asymmetric keys or some other mechanism.

In a simple webapp we have an input element where we can ...