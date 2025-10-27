---
title: The Curious Case of the Password Database
url: https://www.trustedsec.com/blog/the-curious-case-of-the-password-database/
source: TrustedSec
date: 2022-10-21
fetch_date: 2025-10-03T20:30:39.735327
---

# The Curious Case of the Password Database

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
* [The Curious Case of the Password Database](https://trustedsec.com/blog/the-curious-case-of-the-password-database)

October 20, 2022

# The Curious Case of the Password Database

Written by
Travis Kaun

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/CuriousCasePasswordDatabase_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695570639&s=ab87eefffaefcdd1d77b994f1a85bee2)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#a39cd0d6c1c9c6c0d79ee0cbc6c0c8869193ccd6d7869193d7cbcad0869193c2d1d7cac0cfc6869193c5d1ccce869193f7d1d6d0d7c6c7f0c6c086919285c2ced398c1ccc7da9ef7cbc6869193e0d6d1caccd6d0869193e0c2d0c6869193ccc5869193d7cbc6869193f3c2d0d0d4ccd1c7869193e7c2d7c2c1c2d0c68690e2869193cbd7d7d3d08690e28691e58691e5d7d1d6d0d7c6c7d0c6c08dc0ccce8691e5c1cfccc48691e5d7cbc68ec0d6d1caccd6d08ec0c2d0c68eccc58ed7cbc68ed3c2d0d0d4ccd1c78ec7c2d7c2c1c2d0c6 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database "Share on Facebook")
* [Share on X](http://twitter.com/share?text=The%20Curious%20Case%20of%20the%20Password%20Database%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-curious-case-of-the-password-database&mini=true "Share on LinkedIn")

Nowadays, password managers are king. We use password managers to secure our most sensitive credentials to a myriad of services and sites; a compromise of the password manager could prove devastating.

Due to recently [*disclosed critical Common Vulnerabilities and Exposures (CVEs*](https://www.manageengine.com/products/passwordmanagerpro/issues-fixed.html)) involving ManageEngine's Password Manager Pro software, a client came to us at TrustedSec, wondering: *If an attacker gained access to our Password Manager Pro server, would our passwords be compromised?*

![Scooby Doo meme](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun1-meme.jpg)

Since the client was assured that data within the Password Manager Pro server was encrypted, our answer was assuredly, "No." Right? We set off to find out!

The [*recent CVEs affecting the Password Manager Pro software*](https://thehackernews.com/2022/09/cisa-warns-of-hackers-exploiting-recent.html) were some of the worst kind: Remote Code Execution (RCE). For the sake of this engagement, we were focused not so much on the initial attack vector, but rather on the extent of the post-exploitation possibilities. Simply, with access to the system's data, could we recover the encrypted secrets stored within?

We started with access an attacker would presumably have:

* [*Password Manager Pro v10.5*](https://archives2.manageengine.com/passwordmanagerpro/10501/)

Note: Mid-engagement, we identified some newly published work by [*smaury at Shielder*](https://www.shielder.com/blog/2022/09/how-to-decrypt-manage-engine-pmp-passwords-for-fun-and-domain-admin-a-red-teaming-tale/) regarding tearing apart Password Manager Pro. The timing was astounding. Our collective articles may look similar; but our approaches, experience, and code differ. We highly suggest checking out his terrific write-up regarding this topic.

## Step 1 - Application Enumeration

We staged an instance of Linux running ManageEngine’s Password Manager Pro version 10.5 to replicate the client's environment. After fetching the [*application software*](https://archives2.manageengine.com/passwordmanagerpro/10501/) and initiating a [*restore*](https://www.manageengine.com/products/passwordmanagerpro/help/disaster_recovery.html), we started by analyzing the running processes and identifying key information. The application was running Java and PostgreSQL as the primary components.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_1-1.png)

Figure 1 - ManageEngine's Running Processes

TrustedSec then explored the Password Manager Pro application directory, revealing a collection of Java JAR application and configuration files. By reading application documentation, TrustedSec identified the username and encrypted database password stored in the ***database-params.conf*** file.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_2.png)

Figure 2 - Encrypted Database Password

The ***pmp\_key.key*** file reveals the PMP key, which will come in handy later.

![](https://www.trustedsec.com/wp-content/uploads/2022/10/Kaun_3.png)

Figure 3 - PMP Key

## Step 2 - PostgreSQL Password Recovery

One of the best...