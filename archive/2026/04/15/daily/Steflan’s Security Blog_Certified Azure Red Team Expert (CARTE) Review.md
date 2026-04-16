---
title: Certified Azure Red Team Expert (CARTE) Review
url: https://steflan-security.com/certified-azure-red-team-expert-carte-review/?utm_source=rss&utm_medium=rss&utm_campaign=certified-azure-red-team-expert-carte-review
source: Steflan’s Security Blog
date: 2026-04-15
fetch_date: 2026-04-16T04:53:55.647726
---

# Certified Azure Red Team Expert (CARTE) Review

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

![](https://i0.wp.com/steflan-security.com/wp-content/uploads/2026/04/CARTE.png?fit=1024%2C409&ssl=1)

[Certifications](https://steflan-security.com/category/reviews/certifications/), [Learning Material](https://steflan-security.com/category/reviews/learning-material/), [Reviews](https://steflan-security.com/category/reviews/), [Training Labs](https://steflan-security.com/category/reviews/training-platforms/)

# Certified Azure Red Team Expert (CARTE) Review

April 15, 2026
| by Stefano Lanaro
| [Leave a comment](https://steflan-security.com/certified-azure-red-team-expert-carte-review/#respond)

## In**troduction**

The Certified Azure Red Team Expert is a penetration testing/red teaming certification and course provided by Altered Security, which is known in the industry for providing great courses and bootcamps.

In this review, I take the time to talk about my experience with this certification, the pros, and cons of enrolling in the course, my thoughts after taking and passing the exam, and a few tips and tricks.

## **Pros**

* At a starting price of $449 USD, it provides great value for your money, especially in the cloud-based pentesting world.
* In terms of advanced Azure/Entra ID Active Directory courses, due to the complexity and cost involved in setting up practice labs, this will be the best way to get some hands-on experience.
* As always the Altered Security support team is amazing. They are always be very quick to reply to any issue or question I had. Keep in mind their support team is based in India so try to get in touch with them between 8am-10pm GMT+5:30, although they often did reply to my queries outside of those hours.
* The teacher for the course is Keanu Nys, who is a very well known pentester/red teamer, and the creator of [GraphSpy](https://github.com/RedByte1337/GraphSpy).
* The course not only shows the attack themselves, but also ways that you can automate them or make them more OPSEC-safe.
* For almost every technique and attack used throughout the course, a mitigation/remediation strategy is provided in the course which is something that is often overlooked in penetration testing courses.
* The security tools offered by Microsoft to help protect Azure Cloud are explained in detail throughout the course, which is invaluable knowledge for red teamers.
* The content of the course, which you have lifetime access to, often gets updated with new content or additional commands.

## **Cons**

* Altered Security still isn’t as recognized as other providers such as Offensive Security, so the certification won’t look as shiny on your resume.
* While it’s great to have a cloud environment to practice Azure AD pentesting on, I wish the course came with a CTF or simulated exam environment that students could practice on prior to sitting the exam. At the time when I took the course, the environment used to walk through the lab material is the only one available to practice.
* Some of the techniques and commands shown during the course may not work as well in the student VM provided and due to the shared nature of the course and CTF cloud environments, these would sometimes have issues due to other students accidentally breaking them. I was stuck for a few hours on a few exercises for a few hours because of this but the support team was very quick to help.
* The flag system it uses follows the course material, meaning it can be completed by using all of the commands prior to the exercise, I personally would have appreciated if there were flags to capture that simulated an entire environment (in order to give students an idea of what the exam is like) rather than one-off tasks.
* The course does not cover Azure basics, which for some may be a negative, but to me this is totally fair to avoid bloating the course content with repeated material from their CARTP course.

## **Background**

I have been wanting to improve my Azure pentesting skills for a while, and after dealing with the beast that OSWE is I felt like I was finally ready. I had already passed the CARTP exam a few years ago and since then I had gained some more cloud pentesting experience, however I felt like I still wanted to learn more.

It is recommended to tackle the CARTP course and exam before diving into CARTE, however if you are already quite experienced with Azure and Entra ID pentesting you may be able to jump straight into it. Additionally, knowledge of PowerShell can also help greatly although it isn’t necessary at all.

## **The Course**

![](https://i0.wp.com/steflan-security.com/wp-content/uploads/2026/04/image.png?fit=900%2C536&ssl=1)

The course provides both videos and PDF slides to follow along (with a web-style lab manual), the content walks through various advanced enumeration, exploitation, lateral movement, privilege escalation, and persistence techniques that can be used in an Azure Active Directory environment.

Unlike the CARTP course, basic enumeration techniques are not covered, which is something I personally liked. When I did the CRTE course, I found that there was a lot of repetition from the CRTP content that shouldn’t really be part of an advanced course. Instead, CARTE focuses on more advanced attacks and concepts, while still developing on top of the foundation that CARTP built.

The material is very easy to follow, and all of the commands and techniques are very well explained by the instructor, not only explaining the command itself but how it works under the hood. This also helped me understand all of the different ways that Microsoft has designed to interact with Azure and Entra ID services.

The following are some of the techniques taught throughout the course:

* Manual and Dynamic Device Code Phishing.
* Family of Client IDs (FOCI).
* Evading MFA.
* JWT Assertion.
* ​Attributed-based Access Control (ABAC).
* Application permissions.
* ​Authentication Strength and Conditional Access.
* Temporary Access Pass (TAP).
* ​Privileged Identity Management (PIM) role assignments.
* Mutable claims in applications.
* Logic apps.
* Hybrid identity and Cloud Sync.
* GitHub Actions and Components.
* Automation Accounts.
* Microsoft Entra Kerberos and Azure File Shares.
* Illicit Consent Grant.
* Session Cookie Replay.
* Cloud Service Provi...