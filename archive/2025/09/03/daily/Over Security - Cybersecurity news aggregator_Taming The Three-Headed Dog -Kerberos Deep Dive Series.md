---
title: Taming The Three-Headed Dog -Kerberos Deep Dive Series
url: https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-03
fetch_date: 2025-10-02T19:34:29.962932
---

# Taming The Three-Headed Dog -Kerberos Deep Dive Series

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Taming The Three-Headed Dog -Kerberos Deep Dive Series](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/ "Taming The Three-Headed Dog -Kerberos Deep Dive Series")

[September 2, 2025](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/ "Taming The Three-Headed Dog -Kerberos Deep Dive Series")
 /
[Alex Joss](https://blog.compass-security.com/author/ajoss/ "Posts by Alex Joss")
 /
[0 Comments](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/#respond)

[![](https://blog.compass-security.com/wp-content/uploads/2025/08/cerberus.png)](https://blog.compass-security.com/wp-content/uploads/2025/08/cerberus.png)

***Update 10. September 2025:** The slides shown in the YouTube videos are now available on [our website](https://www.compass-security.com/de/research/praesentationen)*.

Kerberos is the default authentication protocol in on-prem Windows environments (and has even reached the Cloud by now). It allows users to seamlessly authenticate to file shares, web apps, databases, and countless other services in a corporate network using their domain credentials.

Originally designed to replace NTLM and fix its long-standing security flaws, Kerberos brought stronger security, but along with that also its own peculiarities, security considerations, and lastly, a whole lot of complexity. And where there’s complexity, there’s also a high chance of misconfiguration, misunderstanding, and ultimately, exploitation.

For [penetration testers](https://www.compass-security.com/en/services/penetration-tests?_gl=1*ecyvqc*_up*MQ..*_ga*NTM2NTA2NTc3LjE3NTU2OTA3Njg.*_ga_RVE27ZCMBR*czE3NTU2OTA3NjgkbzEkZzAkdDE3NTU2OTA3NjgkajYwJGwwJGgw) and [red teamers](https://www.compass-security.com/en/services/red-teaming?_gl=1*ecyvqc*_up*MQ..*_ga*NTM2NTA2NTc3LjE3NTU2OTA3Njg.*_ga_RVE27ZCMBR*czE3NTU2OTA3NjgkbzEkZzAkdDE3NTU2OTA3NjgkajYwJGwwJGgw), Kerberos often sits at the heart of privilege escalation and lateral movement in Active Directory. Some vulnerabilities are obvious and quick to fix. Others are deeply embedded, interconnected, and have consequences that are far from intuitive.

To tackle this situation, it is essential to understand how the Kerberos protocol works under the hood. This reveals why and how well-known attacks such as Kerberoasting actually work, and more importantly, how they can be prevented.

That’s why we’re launching a **[6-part YouTube series](https://www.youtube.com/playlist?list=PLyphfaqpz_mmCmFtVQxAu3jnE4lXPy3lL)**, a technical deep dive into Kerberos. We’ll break down the protocol, dissect well-known attacks, and cover defensive strategies to keep your environment secure.

## What’s in the Series?

**Part 1: Introduction to the Kerberos Protocol**

The first part will focus on the basic functionality of the Kerberos protocol and reveal its inner workings. You will learn about the most important building blocks, concepts, and goals in a Kerberos eco system, what messages are exchanged between the participants, and how they can be analyzed and inspected.

**Part 2: Kerberoasting**

Part 2 focuses on an attack called Kerberoasting, where adversaries can abuse Kerberos to extract and crack passwords of service accounts in an Active Directory environment.

**Part 3: AS-REP Roasting**

In part 3, we’ll look at another attack called AS-REP roasting. While sharing similarities with Kerberoasting, this technique allows attackers to target and compromise misconfigured user accounts via the Kerberos protocol.

**Part 4: Unconstrained Delegation**

Kerberos provides a powerful impersonation feature called delegation. In part 4 of this series, we dive into the oldest and most insecure form of this impersonation mechanism: Unconstrained Delegation. We cover how it works under the hood, how it can be abused by attackers and how you can secure your environment accordingly.

**Part 5: Constrained Delegation**

Constrained delegation is the successor of unconstrained delegation and the main topic in part 5. While Microsoft has addressed the most prevalent security concerns affecting unconstrained delegation, this newer form of delegation still has potential for abuse and may pose a risk to the security of your infrastructure if configured incorrectly.

**Part 6: Resource-Based Constrained Delegation**

The last part of the series will focus on the latest addition to the delegation mechanisms available in Kerberos: Resource-Based Constrained Delegation (or RBCD for short). While almost identical to constrained delegation, RBCD opens up new ways for adversaries to exploit misconfigurations in your environment.

## Why Watch?

As you can see, there is a lot to talk about. In this video series we will cover both the offensive and defensive side of Kerberos and highlight important aspects for attackers as well as defenders. So whether you are working as a penetration tester, system engineer, or security consultant, we are sure that this series will give you the insights you need to handle Kerberos with confidence.

## When and Where?

Starting on September 2, 2025, two videos will be released each week on our [YouTube channel](https://www.youtube.com/%40compass-security). Keep an eye on [this playlist](https://www.youtube.com/playlist?list=PLyphfaqpz_mmCmFtVQxAu3jnE4lXPy3lL) so you don’t miss any new releases!

You can also find the slides shown in the YouTube videos on [our website](https://www.compass-security.com/de/research/praesentationen).

[Youtube](https://blog.compass-security.com/category/youtube/)

[Active Directory](https://blog.compass-security.com/tag/active-directory/)[Kerberos](https://blog.compass-security.com/tag/kerberos/)[Microsoft](https://blog.compass-security.com/tag/microsoft/)

[##### Previous post

Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/ "Previous post: Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases")
[##### Next post

Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/ "Next post: Collaborator Everywhere v2")

### Leave a Reply [Cancel reply](/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name \*

Email \*

### Recent Posts

* [Ensuring NIS2 Compliance: The Importance of Penetration Testing](https://blog.compass-security.com/2025/09/ensuring-nis2-compliance-the-importance-of-penetration-testing/)
* [Collaborator Everywhere v2](https://blog.compass-security.com/2025/09/collaborator-everywhere-v2/)
* [Taming The Three-Headed Dog -Kerberos Deep Dive Series](https://blog.compass-security.com/2025/09/taming-the-three-headed-dog-kerberos-deep-dive-series/)
* [Into the World of Passkeys: Practical Thoughts and Real-Life Use Cases](https://blog.compass-security.com/2025/08/into-the-world-of-passkeys-practical-thoughts-and-real-life-use-cases/)
* [xvulnhuntr](https://blog.compass-security.com/2025/07/xvulnhuntr/)

### Categories

Categories
Select Category
APT  (8)
Authentication  (18)
Bug Bounty  (6)
Entra ID  (3)
Evasion  (3)
Event  (34)
Exploiting  (18)
Forensic  (25)
Hacking-Lab  (18)
Hardening  (33)
Incident Respons...