---
title: Detecting Password-Spraying with a Honeypot Account
url: https://trustedsec.com/blog/detecting-password-spraying-with-a-honeypot-account
source: TrustedSec
date: 2025-09-10
fetch_date: 2025-10-02T19:54:49.595275
---

# Detecting Password-Spraying with a Honeypot Account

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
* [Detecting Active Directory Password-Spraying with a Honeypot Account](https://trustedsec.com/blog/detecting-password-spraying-with-a-honeypot-account)

September 09, 2025

# Detecting Active Directory Password-Spraying with a Honeypot Account

Written by
Sean Metcalf

Red Team Adversarial Attack Simulation
Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PasswordSprayingHoneypotAccount_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1756911014&s=5f6b4fc68a7ff385d0f570b0e546d99b)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#17286462757d7274632a547f72747c322527786263322527637f7e643225277665637e747b723225277165787a3225274365626463727344727432252631767a672c7578736e2a5372637274637e79703225275674637e6172322527537e6572746378656e32252747766464607865733a446765766e7e7970322527607e637f322527763225275f7879726e677863322527567474786279633224563225277f63636764322456322551322551636562646372736472743974787a322551757b78703225517372637274637e79703a67766464607865733a646765766e7e79703a607e637f3a763a7f7879726e6778633a76747478627963 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdetecting-password-spraying-with-a-honeypot-account "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Detecting%20Active%20Directory%20Password-Spraying%20with%20a%20Honeypot%20Account%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdetecting-password-spraying-with-a-honeypot-account "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdetecting-password-spraying-with-a-honeypot-account&mini=true "Share on LinkedIn")

Password-spraying is a popular technique which involves guessing passwords to gain control of accounts. This automated password-guessing is performed against all users and typically avoids account lockout since the logon attempts with a specific password are performed against every user. This [technique](https://attack.mitre.org/techniques/T1110/003/) is popular with penetration testers, Red Teams, and threat actors alike because it works so well. Password-spray detection typically involves correlating bad password attempts based on time. This detection method is fraught with false positives since standard users mistype and/or forget their passwords regularly. This article describes how to detect password-spraying without false positives by leveraging a honeypot account.

### **Password-Spraying**

Password-spraying tooling works by running through a list of potential passwords and, one by one, attempting to authenticate as each user starting with the first password on this list. If successful, the tool notes this and continues. The tool may pause after completing password-spraying of each password for all users before attempting the next one. This avoids the password lockout policy since the attacker can limit the number of bad password attempts over time.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Password-Spraying_Metcalf/Fig01_Metcalf_DetectingPasswords.png?w=320&q=90&auto=format&fit=max&dm=1756919435&s=771c1cc158b838044b0e3e4000ae6658)

Password-Spraying Approach:

* Attempt authentication for user #1 using password #1
* Attempt authentication for user #2 using password #1
* Continue until attempted authentication has been performed using password #1 for all targeted users
* Pause for a few minutes to avoid account lockout
* Attempt authentication for user #1 using password #2
* Attempt authentication for user #2 using password #2
* Continue until attempted authentication has been performed using password #2 for all targeted users
* Pause for a few minutes to avoid account lockout

Pausing after each password attempt iteration enables the attacker to avoid the standard lockout rules. In the following figure is an example of a domain password policy which has a lockout threshold of 5 and a lockout observation window of 20 minutes. This means that if there are 5 bad password attempts for a specific user within 20 minutes, the account will be locked out and cannot authenticate until the lockout duration is met (20 minutes) or the account is manually unlocked. Ensuring that the password-spraying tool performs less than 5 bad password attempts in 20 minutes avoids locking out any specific user.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Password-Spraying_Metcalf/Fig02_Metcalf_DetectingPasswords.png?w=320&q=90&auto=format&fit=max&dm=1756919436&s=d6ae31c77e5b6e07bb6630e518f4736c)

This approa...