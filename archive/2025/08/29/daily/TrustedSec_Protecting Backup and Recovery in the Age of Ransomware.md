---
title: Protecting Backup and Recovery in the Age of Ransomware
url: https://trustedsec.com/blog/protecting-backups
source: TrustedSec
date: 2025-08-29
fetch_date: 2025-10-07T00:51:11.592768
---

# Protecting Backup and Recovery in the Age of Ransomware

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
* [Protecting Backup and Recovery in the Age of Ransomware](https://trustedsec.com/blog/protecting-backups)

August 28, 2025

# Protecting Backup and Recovery in the Age of Ransomware

Written by
Mike Owens

Organizational Effectiveness
Security Remediation
Ransomware

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ProtectingBackupRecovery_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1756230956&s=0a87673e9a09e4cce1780f31d1ca668a)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#b38cc0c6d1d9d6d0c78ef0dbd6d0d8968183dcc6c7968183c7dbdac0968183d2c1c7dad0dfd6968183d5c1dcde968183e7c1c6c0c7d6d7e0d6d096818295d2dec388d1dcd7ca8ee3c1dcc7d6d0c7daddd4968183f1d2d0d8c6c3968183d2ddd7968183e1d6d0dcc5d6c1ca968183dadd968183c7dbd6968183f2d4d6968183dcd5968183e1d2ddc0dcdec4d2c1d69680f2968183dbc7c7c3c09680f29681f59681f5c7c1c6c0c7d6d7c0d6d09dd0dcde9681f5d1dfdcd49681f5c3c1dcc7d6d0c7daddd49ed1d2d0d8c6c3c0 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fprotecting-backups "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Protecting%20Backup%20and%20Recovery%20in%20the%20Age%20of%20Ransomware%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fprotecting-backups "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fprotecting-backups&mini=true "Share on LinkedIn")

Ransomware attackers frequently target backups and recovery systems to force victims into paying ransoms, making robust protection strategies essential for all organizations. This blog introduces the **Defensive Backup Infrastructure Controls** framework, a process I've developed from first principals to safeguard backups, harden systems, and maintain recovery capabilities during worst-case data corruption or ransomware incidents.

This may be hard to hear, but:

* Ransomware attacks aren't going away anytime soon.
* Attackers specifically target backups once they get into your environment.
* Most backup systems are designed for site loss and are not prepared for a malicious technical attack like ransomware.

I've [worked with dozens of organizations over the past few years](https://trustedsec.com/services/system-hardening)—ranging from nonprofits to SMBs to global enterprises—to figure out the critical capabilities that must be achieved so your backups survive a ransomware attack *and* so you can actually recover the organization and get back on your feet. I emphasize that these controls are designed around **capabilities**, not tools, so they are just as relevant whether you are a small business with a server in the back room, are completely cloud-native, or have thousands of systems in datacenters around the world. Processes and implementation are what matter—not which brand of blinky-box you plugged into the server rack.

Without further ado, let me present the Defensive Backup Infrastructure Controls framework:

## Defensive Backup Infrastructure Controls Framework

The Defensive Backup Infrastructure Controls (DBIC) framework is a customized set of controls developed by TrustedSec. The framework presents a strategy and prescriptive guidance for hardening backups and backup systems against the threat of human-operated ransomware and similar destructive attacks.

The core principle of the framework is that the ability to recover critical data and IT capabilities from backups is the last line of defense against catastrophic business losses due to ransomware and other enterprise-scale destructive cyberattacks.

Successful recovery depends on achieving five (5) strategic objectives prior to any attack:

* Backups of critical systems are performed
* Backups are hardened against destruction
* Backup data is accessible during a full network outage
* Critical systems can be restored from backups at enterprise scale
* Supportive controls increase resiliency and prevent variance

The strategic objectives and technical controls in the DBIC are based on threat modeling of the common trends and tactics employed by ransomware attackers. The framework is informed by experiences of the TrustedSec Incident Response and Remediation teams and draws from industry best practice control frameworks including CIS Controls, the NIST Cybersecurity Framework (CSF), and NIST Special Publication (SP) 800-53: Security and Privacy Controls for Information Systems and Organizations. The framework is not a replacement for comprehensive, risk-informed business continuity (BC) and disaster recovery (DR) planning.

### DBIC Strategic Objectives

###...