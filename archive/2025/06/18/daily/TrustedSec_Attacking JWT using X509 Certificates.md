---
title: Attacking JWT using X509 Certificates
url: https://trustedsec.com/blog/attacking-jwt-using-x509-certificates
source: TrustedSec
date: 2025-06-18
fetch_date: 2025-10-06T22:54:29.195290
---

# Attacking JWT using X509 Certificates

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
* [Attacking JWT using X509 Certificates](https://trustedsec.com/blog/attacking-jwt-using-x509-certificates)

June 17, 2025

# Attacking JWT using X509 Certificates

Written by
Kurt Muhl

Penetration Testing
Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AttackingJWTX509Certs_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1749668420&s=4bd64da4486a0a249f6f0daa774e1609)

Table of contents

* [1.1 Setup](#Setup)
* [1.2 Anatomy of the attack](#Anatomy)
* [1.3 Proof of Concept](#PoC)
* [1.4 Attacking x5u](#Attacking)
* [1.5 Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#cdf2beb8afa7a8aeb9f08ea5a8aea6e8fffda2b8b9e8fffdb9a5a4bee8fffdacbfb9a4aea1a8e8fffdabbfa2a0e8fffd99bfb8beb9a8a99ea8aee8fffcebaca0bdf6afa2a9b4f08cb9b9acaea6a4a3aae8fffd879a99e8fffdb8bea4a3aae8fffd95f8fdf4e8fffd8ea8bfb9a4aba4aeacb9a8bee8fe8ce8fffda5b9b9bdbee8fe8ce8ff8be8ff8bb9bfb8beb9a8a9bea8aee3aea2a0e8ff8bafa1a2aae8ff8bacb9b9acaea6a4a3aae0a7bab9e0b8bea4a3aae0b5f8fdf4e0aea8bfb9a4aba4aeacb9a8be "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fattacking-jwt-using-x509-certificates "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Attacking%20JWT%20using%20X509%20Certificates%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fattacking-jwt-using-x509-certificates "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fattacking-jwt-using-x509-certificates&mini=true "Share on LinkedIn")

While pulling together some information for a [previous blog](https://trustedsec.com/blog/attacking-jwt-with-self-signed-claims), I had identified an interesting ***JSON Web Signature (JWS)*** header that I wanted to learn more about. In [RFC 7515 Section 4.1](https://datatracker.ietf.org/doc/html/rfc7515#section-4.1), a list of registered header parameters is outlined. This time, the ***x5u*** and ***x5c*** headers caught my attention. These headers make use of X.509 certificates and define where the public key is stored to validate the JWS integrity.

For both of these headers, an attacker could sign the token with their own private key and modify the header value to specify their public key for signature verification. At this point, an attacker would have full access to modify the token claims, and the server would accept the information. While this is not a new attack, I could not find a Burp extension that would allow me to easily exploit this flaw. In this blog, I will walk you through the breakdown of the attack and demonstrate a Burp Suite extension that I built for exploiting these headers.

## 1.1 Setup

To get started with this attack, we will need a vulnerable application to test against. I have created a vulnerable API in flask for this purpose.

<https://github.com/Tsynack/JWT_X509_Re-Signer/tree/main/Example%20API>

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JWT_X.509Certs_Kurt/Fig01_Kurt_JWT509Certs.png?w=320&q=90&auto=format&fit=max&dm=1749672164&s=75168606044b78d48713d1afcb235b40)

Figure 1 - Running the Example API

To make testing a little easier, I also built a custom Burp extension that will allow for modifying the headers and claims. The extension can also be used to re-sign the token. You can find the extension here:

<https://github.com/Tsynack/JWT_X509_Re-Signer/tree/main/Burp%20Extension>

NOTE: The extension relies on Jython being set up in Burp’s extension settings.

To install the extension, navigate to ***Extensions > Add > Extension Type: Python >***and select the ***JWT\_x509\_Re-Sign.py*** file.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JWT_X.509Certs_Kurt/Fig02_Kurt_JWT509Certs.jpg?w=320&q=90&auto=format&fit=max&dm=1749672165&s=10147154b0b714583e023eeae5f5ee97)

Figure 2 - Load JWT Re-signer

Once the extension is loaded, any requests that contain a JWS in Burp’s HTTP history or repeater should have a tab labeled ***Re-sign JWT***.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JWT_X.509Certs_Kurt/Fig03_Kurt_JWT509Certs.jpg?w=320&q=90&auto=format&fit=max&dm=1749672166&s=8e7081cacc810413039a1d61ad8b5000)

Figure 3 - Extension Installed

The last thing we will need in order to perform this attack is an X.509 private key for signing the token, and the associated certificate, so the server can validate the signature. Using OpenSSL, this can be done with the below command.

```
openssl req -newkey rsa:2048 -nodes -keyout private_key...