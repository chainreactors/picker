---
title: WSUS Is SUS: NTLM Relay Attacks in Plain Sight
url: https://trustedsec.com/blog/wsus-is-sus-ntlm-relay-attacks-in-plain-sight
source: TrustedSec
date: 2025-09-13
fetch_date: 2025-10-02T20:06:14.152568
---

# WSUS Is SUS: NTLM Relay Attacks in Plain Sight

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
* [WSUS Is SUS: NTLM Relay Attacks in Plain Sight](https://trustedsec.com/blog/wsus-is-sus-ntlm-relay-attacks-in-plain-sight)

September 12, 2025

# WSUS Is SUS: NTLM Relay Attacks in Plain Sight

Written by
Austin Coontz

Penetration Testing
Active Directory Security Review

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/WSUSisSUS_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1757425953&s=41375664b2de8425ce1d7f8dfc4fcba7)

Table of contents

* [WSUS Primer](#Primer)
* [WSUS Enumeration](#Enumeration)
* [Lab Setup](#Setup)
* [HTTP Exploitation](#HTTP)
* [HTTPS Exploitation](#HTTPS)
* [Mitigations](#Mitigations)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#dfe0acaabdb5babcabe29cb7babcb4faedefb0aaabfaedefabb7b6acfaedefbeadabb6bcb3bafaedefb9adb0b2faedef8badaaacabbabb8cbabcfaedeef9beb2afe4bdb0bba6e2888c8a8cfaedef96acfaedef8c8a8cfaec9efaedef918b9392faedef8dbab3bea6faedef9eababbebcb4acfaedefb6b1faedef8fb3beb6b1faedef8cb6b8b7abfaec9efaedefb7ababafacfaec9efaed99faed99abadaaacabbabbacbabcf1bcb0b2faed99bdb3b0b8faed99a8acaaacf2b6acf2acaaacf2b1abb3b2f2adbab3bea6f2beababbebcb4acf2b6b1f2afb3beb6b1f2acb6b8b7ab "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwsus-is-sus-ntlm-relay-attacks-in-plain-sight "Share on Facebook")
* [Share on X](http://twitter.com/share?text=WSUS%20Is%20SUS%3A%20NTLM%20Relay%20Attacks%20in%20Plain%20Sight%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwsus-is-sus-ntlm-relay-attacks-in-plain-sight "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwsus-is-sus-ntlm-relay-attacks-in-plain-sight&mini=true "Share on LinkedIn")

Windows Server Update Services (WSUS) is a trusted cornerstone of patch management in many environments, but its reliance on HTTP/HTTPS traffic makes it a prime target for attackers operating on the local network. By intercepting and relaying WSUS authentication flows, it’s possible to capture NTLM hashes from both user and machine accounts, turning routine update traffic into an opportunity for credential theft and relay attacks. In this post, I’ll show how to identify WSUS traffic, demonstrate how HTTP and HTTPS WSUS endpoints can be abused, and share the path that led me to exploring this attack vector in the first place.

My interest in WSUS exploitation started after coming across [Alex Neff’s post on X](https://x.com/al3x_n3ff/status/1936809178913267986) about [wsuks](https://github.com/NeffIsBack/wsuks), a tool for serving malicious updates through WSUS. While weaponizing updates is a unique attack method, that angle isn’t the focus of this blog. Not long after, I came across [GoSecure’s excellent write-up](https://gosecure.ai/blog/2021/11/22/gosecure-investigates-abusing-windows-server-update-services-wsus-to-enable-ntlm-relaying-attacks) on abusing WSUS for NTLM relaying. This shifted my focus from update weaponization to interception and pushed me to dig deeper into how WSUS traffic could be abused in real-world environments.

## WSUS Primer

WSUS is Microsoft’s patch distribution platform that is designed to centralize and control how updates flow into an enterprise. Instead of every workstation reaching out directly to Microsoft’s update servers, organizations deploy WSUS to act as a trusted middleman. Endpoints register with a WSUS server, periodically check in, and download updates that have been approved by administrators. By default, this traffic flows over port **8530/TCP** for **HTTP** or port **8531/TCP** for **HTTPS.**

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/WSUS_Coontz/FigA_Coontz_WSUS.jpg?w=320&q=90&auto=format&fit=max&dm=1757607602&s=625484a362a3af31e57070b73b9c76cc)

WSUS can be configured directly via Group Policy ([Microsoft Docs](https://learn.microsoft.com/en-us/windows/deployment/update/waas-manage-updates-wsus)), integrated into System Center Configuration Manager (SCCM) ([Microsoft Docs](https://learn.microsoft.com/en-us/intune/configmgr/core/clients/deploy/deploy-clients-to-windows-computers)), or even tied in to Intune and Windows Update for Business in co-management scenarios ([Microsoft Docs](https://learn.microsoft.com/en-us/windows/deployment/update/wufb-wsus)). In September 2024, Microsoft officially announced that WSUS is deprecated ([Microsoft Post](https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-server-update-services-wsus-deprecation/4250436)). While the role is still available and supported in Windows...