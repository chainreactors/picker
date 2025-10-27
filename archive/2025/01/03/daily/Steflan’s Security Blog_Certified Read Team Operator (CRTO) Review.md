---
title: Certified Read Team Operator (CRTO) Review
url: https://steflan-security.com/certified-read-team-operator-crto-review/?utm_source=rss&utm_medium=rss&utm_campaign=certified-read-team-operator-crto-review
source: Steflan’s Security Blog
date: 2025-01-03
fetch_date: 2025-10-06T20:14:31.846653
---

# Certified Read Team Operator (CRTO) Review

* [Home](https://steflan-security.com)
* [CTF Walkthroughs](https://steflan-security.com/category/walkthrough/)
  + [Hack The Box](https://steflan-security.com/category/walkthrough/hack-the-box/)
  + [TryHackMe](https://steflan-security.com/category/walkthrough/tryhackme/)
  + [VulnHub](https://steflan-security.com/category/walkthrough/vulnhub/)
* [Guides](https://steflan-security.com/category/guides/)
  + [Enumeration](https://steflan-security.com/category/guides/enumeration/)
  + [Privilege Escalation](https://steflan-security.com/category/guides/privilegeescalation/)
    - [Linux](https://steflan-security.com/category/guides/privilegeescalation/linux/)
    - [Windows](https://steflan-security.com/category/guides/privilegeescalation/windows/)
  + [Web](https://steflan-security.com/category/guides/web/)
  + [Buffer Overflow](https://steflan-security.com/category/guides/bufferoverflow/)
    - [Stack Buffer Overflow](https://steflan-security.com/category/guides/bufferoverflow/stack-buffer-overflow/)
* [Reviews](https://steflan-security.com/category/reviews/)
  + [Certifications](https://steflan-security.com/category/reviews/certifications/)
  + [Training Labs](https://steflan-security.com/category/reviews/training-platforms/)
  + [Learning Material](https://steflan-security.com/category/reviews/learning-material/)
* [Resources](https://steflan-security.com/category/resources/)
  + [Cheat Sheets](https://steflan-security.com/category/resources/cheatsheet/)
  + [Checklists](https://steflan-security.com/category/resources/checklists/)
* [About](https://steflan-security.com/about-us/)

[![Steflan’s Security Blog](https://steflan-security.com/wp-content/uploads/2021/03/cropped-Logo.png)](https://steflan-security.com)

![](https://i0.wp.com/steflan-security.com/wp-content/uploads/2025/01/CRTO.png?fit=1024%2C409&ssl=1)

[Certifications](https://steflan-security.com/category/reviews/certifications/), [Learning Material](https://steflan-security.com/category/reviews/learning-material/), [Reviews](https://steflan-security.com/category/reviews/), [Training Labs](https://steflan-security.com/category/reviews/training-platforms/)

# Certified Read Team Operator (CRTO) Review

January 2, 2025
| by Stefano Lanaro
| [Leave a comment](https://steflan-security.com/certified-read-team-operator-crto-review/#respond)

## **Introduction**

Certified Red Team Operator (CRTO) is a penetration testing/red teaming certification and course that teaches the basic red team principles, tools and techniques, entirely through the Cobalt Strike command and control (C2) framework.

In this review, I take the time to talk about my experience with this certification, the pros, and cons of enrolling in the course, my thoughts after taking and passing the exam, and a few tips and tricks.

## **Pros**

* At about $450 USD, it provides great value at an affordable price.
* When it comes to performing attacks using a C2, this is definitely one of the best and most comprehensive courses out there.
* The forum and Discord channel were always very quick to reply and super helpful with any technical issue I had during the course.
* The course is provided by Zero Point Security, which is well known in the industry for creating exceptional training resources and labs.
* For almost every technique and attack used throughout the course, a corresponding detection and mitigation/remediation strategy is provided.
* The course sometimes gets updated with new attacks and techniques, which I was pleasantly surprised about.

## **Cons**

* This certification probably won’t look as shiny as something from OffSec on your resume, despite the great material and value provided.
* Some of the techniques taught throughout the course won’t always work in the lab environment or during the exam.
* Guacamole is the only way to access the lab and exam resources, meaning that transferring files and tools to your VM will be quite difficult.
* The lab time is limited in the total number of hours that it can be run for (40/80/120hours for the 30/60/90 day options respectively), meaning that if you forget to turn off your lab while taking a break, you will still be using lab time.
* The exam environment felt a little empty, and not very realistic, which made finding the intended attack path a little too easy and straightforward.

## **Background**

I decided to take on this course after having completed a bunch of other Active Directory and red teaming-related certifications as I become more interested in red team engagements.

While I was very familiar with Active Directory attacks and techniques, as I had been doing internal tests for a while, what I lacked was proficiency with a C2 framework such as Cobalt Strike and performing certain attacks in a more stealthy way.

I also heard a lot of great feedback from friends and colleagues who had taken this course before and recommended it to me, so this was a no-brainer to me.

Before enrolling I would recommend having a good knowledge of Active Directory/Windows attacks and tools as well as basic PowerShell and C#, in order to be able to understand all of the concepts taught throughout the course. Experience using C2 frameworks would also come in handy for this course.

## **The Course**

![](https://i0.wp.com/steflan-security.com/wp-content/uploads/2025/01/1665228893090.jpg?resize=810%2C376&ssl=1)

The course provides text content and videos to follow along, it starts with setting up Cobalt Strike and then going through various enumeration, exploitation, lateral movement, privilege escalation, persistence and evasion techniques that can be used in an Active Directory environment, all using a C2. The material is very easy to follow, all of the commands and techniques are very well explained by the instructor, detailing how they work under the hood as opposed to just showcasing them.

The following are some of the areas covered by the course:

* Command & Control Setup
* External Reconnaissance
* Initial Compromise
* Host Reconnaissance & Privilege Escalation
* Host Persistence
* Host Privilege Escalation
* Credential Theft & User Impersonation
* Domain Reconnaissance
* Lateral Movement
* Kerberos Attacks
* Pivoting
* Active Directory Certificate Services
* Group Policy
* MS SQL Servers
* Microsoft Configuration Manager
* Forest & Domain Trusts
* Local Administrator Password Solution (LAPS)
* Defender Antivirus & Applocker
* Data Hunting & Exfiltration
* Extending Cobalt Strike

The course was extremely hands on, and it demonstrated attacks using different tools. From my experience, pretty much all of the attacks could be run in the lab without any major issues, and the support was always available for any questions.

I thoroughly enjoyed the course material and learning about all the functionality offered by Cobalt Strike. I was seriously impressed by how powerful it is and how easy it is to configure to simulate various APTs, evade detection and move laterally within a domain with ease. Pretty much all the attacks showcased in the course are applicable to real-world penetration testing that I have experienced in actual engagements.

As during red team engagements you are meant to be evading detection and generating as little noise as possible, as such the course doesn’t leverage any automated enumeration tooling such as BloodHound and instead focuses on manual enumeration using PowerView and built-in Windows binaries. While this approach can seem easy in a lab-like environment, it’s going to be very time consuming in a more realistic domain with hundred and thousands of objects.

What I also liked about the course is that it focused a lot on running attacks from a Windows environment, unlike more traditional internal tests that may be conducted from an attacking Linux machine using Python-based tooling such as Impacket, CrackMapExec or Certipy. This is often going to be the case in red team engagements, where access is provided through a compromised workstation.

While al...