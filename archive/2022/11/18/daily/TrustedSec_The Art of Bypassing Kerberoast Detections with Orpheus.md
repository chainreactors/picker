---
title: The Art of Bypassing Kerberoast Detections with Orpheus
url: https://www.trustedsec.com/blog/the-art-of-bypassing-kerberoast-detections-with-orpheus/
source: TrustedSec
date: 2022-11-18
fetch_date: 2025-10-03T23:07:48.320729
---

# The Art of Bypassing Kerberoast Detections with Orpheus

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
* [The Art of Bypassing Kerberoast Detections with Orpheus](https://trustedsec.com/blog/the-art-of-bypassing-kerberoast-detections-with-orpheus)

November 17, 2022

# The Art of Bypassing Kerberoast Detections with Orpheus

Written by
Ben Mauch

Penetration Testing
Purple Team Adversarial Detection & Countermeasures
Red Team Adversarial Attack Simulation
Research
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ArtOfBypassingKerberoast_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695568818&s=994be4206a4c8fdeba02d24967bfd2b9)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#06397573646c6365723b456e63656d233436697372233436726e6f752334366774726f656a632334366074696b2334365274737572636255636523343720676b763d6469627f3b526e632334364774722334366960233436447f766775756f68612334364d6374646374696775722334364263726365726f696875233436716f726e2334364974766e6373752335472334366e72727675233547233440233440727473757263627563652865696b233440646a6961233440726e632b6774722b69602b647f766775756f68612b6d6374646374696775722b6263726365726f6968752b716f726e2b6974766e637375 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-art-of-bypassing-kerberoast-detections-with-orpheus "Share on Facebook")
* [Share on X](http://twitter.com/share?text=The%20Art%20of%20Bypassing%20Kerberoast%20Detections%20with%20Orpheus%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-art-of-bypassing-kerberoast-detections-with-orpheus "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-art-of-bypassing-kerberoast-detections-with-orpheus&mini=true "Share on LinkedIn")

Back in May of 2018, I wrote a [blog post](https://trustedsec.com/blog/art_of_kerberoast) detailing the steps I took to detect Kerberoast ([T1558.003](https://attack.mitre.org/techniques/T1558/003/)) attacks. This research allowed us to help organizations build a detection for when a threat actor requests the Kerberos ticket for accounts with a service principal name established. In this blog post, I am going to demonstrate how I was able to bypass my own detection, and the detections of many other systems, with slight modifications of the Kerberos request.

Later in the post is a demo if you don't want all the technical details and just want to [see a video](https://www.youtube.com/watch?v=SwbSq1dTz7Y) of the bypass technique in action.

## **Detecting Kerberoast (or so we thought)**

In my [2018 blog post](https://trustedsec.com/blog/art_of_kerberoast), I highlighted several factors for identifying a Kerberoast attack. These identifiers were as follows:

* Windows Event Code 4769
* Ticket Encryption Type of RC4 or 0x17
* Ticket Options with a value of 0x40810010
* Accounts that didn't end with a dollar sign ($)
* A count of the number of SPNs requested that goes over a specified threshold

One of the great things about working at TrustedSec on our Tactical Awareness and Countermeasures (TAC) team is that we get to be both offense and defense. Because of this, we are often presented with the opportunity to defeat our own detections.

This is when I began to dive deep into RFCs 4120 and 1510 ([The Kerberos Network Authentication Service (V5)](https://www.rfc-editor.org/rfc/rfc4120)) to see if there was anything I could do to avoid my detections. I started with the encryption parts of the requests.

## **Encryption Types**

The encryption types are defined by the MsDS-SupportedEncryptionTypes values in Group Policy Objects (GPO). The default Kerberos encryption type for Windows XP and Server 2003 is RC4, whereas Windows 7 and later and Windows Server 2008 and later are defaulted to AES-256.

In the Kerberos exchange, these show up as eTypes in the message. eType 18 (0x12) is AES-256, and eType 23 (0x17) is RC4. When looking at normal traffic on updated Windows systems, we typically see 0x12 as part of the normal encryption process for Kerberos activity.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Mauch_2.png)

RC4 is a weaker cryptographic algorithm than AES-256 and it is therefore easier to recover the NTLM password that was attached to the ticket. This is why tools like GetUserSPNs.py and others will attempt to downgrade the request to the Key Distribution Center (KDC) to use RC4 encryption. Windows Server 2019 still allows for encryption downgrade to RC4!

Several defensive tools will automatically detect when a Kerberos request is downgraded from AES-256 (0x12) to RC4 (0x17). You can see in the followin...