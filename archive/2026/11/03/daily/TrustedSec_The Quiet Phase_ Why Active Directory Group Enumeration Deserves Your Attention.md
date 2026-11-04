---
title: The Quiet Phase: Why Active Directory Group Enumeration Deserves Your Attention
url: https://trustedsec.com/blog/the-quiet-phase-active-directory-group-enumeration
source: TrustedSec
date: 2026-11-03
fetch_date: 2026-11-04T08:19:09.835614
---

# The Quiet Phase: Why Active Directory Group Enumeration Deserves Your Attention

[Skip to Main Content](#main)

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
* [The Quiet Phase: Why Active Directory Group Enumeration Deserves Your Attention](https://trustedsec.com/blog/the-quiet-phase-active-directory-group-enumeration)

November 03, 2026

# The Quiet Phase: Why Active Directory Group Enumeration Deserves Your Attention

Written by
Lakeith Collins

Active Directory Security Review
Threat Hunting

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/TheQuietPhaseActiveDirectory_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1793300784&s=41efe372a74db7ccbbcd2fe307645d06)

Table of contents

* [Why Enumeration is the Signal Worth Catching](#Why)
* [How Enumeration Auditing Works](#How)
* [Noise and Blind Spots](#Spots)
* [Resources to help you on your way](#Help)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#dee1adabbcb4bbbdaae39db6bbbdb5fbeceeb1abaafbeceeaab6b7adfbeceebfacaab7bdb2bbfbeceeb8acb1b3fbecee8aacabadaabbba8dbbbdfbeceff8bfb3aee5bcb1baa7e38ab6bbfbecee8fabb7bbaafbecee8eb6bfadbbfbed9ffbecee89b6a7fbecee9fbdaab7a8bbfbecee9ab7acbbbdaab1aca7fbecee99acb1abaefbecee9bb0abb3bbacbfaab7b1b0fbecee9abbadbbaca8bbadfbecee87b1abacfbecee9faaaabbb0aab7b1b0fbed9ffbeceeb6aaaaaeadfbed9ffbec98fbec98aaacabadaabbbaadbbbdf0bdb1b3fbec98bcb2b1b9fbec98aab6bbf3afabb7bbaaf3aeb6bfadbbf3bfbdaab7a8bbf3bab7acbbbdaab1aca7f3b9acb1abaef3bbb0abb3bbacbfaab7b1b0 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-quiet-phase-active-directory-group-enumeration "Share on Facebook")
* [Share on X](https://twitter.com/share?text=The%20Quiet%20Phase%3A%20Why%20Active%20Directory%20Group%20Enumeration%20Deserves%20Your%20Attention%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-quiet-phase-active-directory-group-enumeration "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-quiet-phase-active-directory-group-enumeration&mini=true "Share on LinkedIn")

## Watching the Door, Ignoring the Window

Almost every security team alerts when someone is added to **Domain Admins**, but almost no one alerts when someone asks who is in **Domain Admins**.

By the time an attacker changes group membership, they already hold privileged access and the damage is underway. The reconnaissance that led them there (mapping who the admins are and which accounts to target) happened days or weeks earlier. It was quiet but visible to anyone who had turned on the right auditing.

This post explains why group enumeration deserves a place in your Active Directory (AD) monitoring, how to audit it with native Windows features, and how pairing it with honeypot groups turns a noisy signal into a high-confidence alarm.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/QuietPhase_Collins/FigA_Collins_quietphase.png?w=320&q=90&auto=format&fit=max&dm=1793301581&s=bf2cddc992bea0217f7779dd929c5f59)

## Why Enumeration is the Signal Worth Catching

Enumeration is how an attacker turns one compromised account into a plan. After the first foothold, often a phished user or an exposed service, the attacker wants to know:

* Who holds Domain Admin, Enterprise Admin, or other Tier 0 rights?
* Which service accounts or Help Desk groups have a path to those rights?
* Which of those accounts are worth stealing credentials from next?

MITRE ATT&CK tracks this as [Permission Groups Discovery: Domain Groups (T1069.002).](https://attack.mitre.org/techniques/T1069/002/) Tools like ***BloodHound***’s***SharpHound*** collector, ***PowerView***, and plain ***ActiveDirectory PowerShell*** cmdlets gather it in minutes. Any authenticated user can read group membership by default, which is why it is valuable to detect. It happens early, before privilege escalation, lateral movement, or data theft. An alert at this stage buys time to respond while the attacker still holds only low-privilege access.

Watching group *changes* tells you a breach is in progress, but watching group *reads* can tell you one is being planned. The auditing described here uses built-in Windows features, requires no new product, and targets the phase where response is cheapest.

## How Enumeration Auditing Works

Two (2) pieces must be in place before a domain controller logs enumeration attempts. Many environments have one, almost none have the second:

* An Audit policy on every domain controller. Enable ***Audit Directory Service Access (Success)*** under ***Advanced Audit Policy > DS Access***, ideally in a GPO linked to the Domain Controllers OU.
* A System Access-Control List (***SACL***) must be defined on each group you care about. Add an audit entry for **Everyone** (or **Authenticated Users**), type ***Success***, applied to ***This object only, for Read member***.

You can confirm the policy on...