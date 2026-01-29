---
title: Social Engineering and Microsoft SSPR: The Road to Pwnage is Paved with Good Intentions
url: https://www.blackhillsinfosec.com/social-engineering-and-microsoft-sspr/
source: Black Hills Information Security, Inc.
date: 2026-01-28
fetch_date: 2026-01-29T04:04:44.974529
---

# Social Engineering and Microsoft SSPR: The Road to Pwnage is Paved with Good Intentions

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

28
Jan
2026

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [John Malone](https://www.blackhillsinfosec.com/category/author/john-malone/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Social Engineering](https://www.blackhillsinfosec.com/category/red-team/social-engineering/)

# [Social Engineering and Microsoft SSPR: The Road to Pwnage is Paved with Good Intentions](https://www.blackhillsinfosec.com/social-engineering-and-microsoft-sspr/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/02/johnmalone-150x150.jpg)

| [John Malone](https://www.blackhillsinfosec.com/team/john-malone/)

*John Malone is a penetration tester for Black Hills Information Security. He regularly performs external, internal, and social engineering-based assessments. His favorite tools are confidence and charisma.*

![Social Engineering and Microsoft SSPR](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/ms-sspr-engineering-header-1024x576.png)

## Introduction

Most organizations treat Microsoft Self-Service Password Reset (SSPR) and push-based MFA as pure wins: fewer help desk tickets, less lockout drama, and more convenience for everyone. You’d think everyone would win here, right?

It might seem that way at a high level, but when I worked in physical security, it became clear that with more convenience often came less security. The same concept, it seems, holds true here.

In this blog, we’ll look at a social engineering technique that combines Microsoft SSPR with social engineering phone calls to gain initial access to Microsoft 365. The best part? The tester will never need to talk to the help desk.

We’ll cover:

* How the ruse works (from a red team perspective)

* Why it’s so effective psychologically

* How to scope and run it ethically in an engagement

* Why this should be part of regular social engineering testing

**Legal / ethical note: Everything here is for authorized testing and defense only.** Using these techniques without explicit written permission is illegal and unethical. Don’t be that person. Don’t be a jerk.

## The Technique

Let’s get right to it. At a high level, the attack looks like this:

1. The attacker performs reconnaissance and checks to see if the target’s tenant has Microsoft SSPR enabled. This is done by visiting https://aka.ms/sspr and entering a valid username and solving a captcha.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/SSPR_01.png)

Microsoft SSPR Access Interface

2. If successful, options will appear that allow you to specify how you would like to reset the user’s password. This can come in the form of entering a number provided by SSPR (extremely potent, as you can tell call targets that you are “assigning them a security code”), security questions configured by the user, or accepting a push notification or phone call.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/SSPR_02.png)

Options for Account Reset

3. The attacker calls the user, claiming to be from the service desk / security team following up on a security issue.
4. The attacker coaches the user into approving the MFA prompts as part of a “verification.”
5. After the MFA is approved, the attacker resets the user’s password via SSPR.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/SSPR_03.png)

Assigning a New Password

6. The attacker logs into Microsoft 365 with the new password, then lies to the user and says they did not receive the first push and will need the employee to send another.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/SSPR_04.png)

MFA Code for Target

7. To keep the user quiet, the attacker gives the user “their new password” and instructs them to reset all devices and then change it again later.
8. The user feels in control, and so the call goes unreported while the tester now has initial access.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/01/SSPR_05.png)

Initial Access in Microsoft 365

From the user’s perspective, this all feels normal:

“IT called me, said there was an issue, sent me MFA prompts and a new password. They fixed it.”

From a red team / attacker perspective, it’s a clean path to initial access that completely bypasses help desk hardening.

## How the Ruse Works in Practice

Below is a conceptual walkthrough that you can adapt into a RoE-approved playbook. I’ve sorted this into a list of bullet points because I’m pretty sure that’s going to be easier reading than a giant wall of text 😊.

**1. Start with a Rules of Engagement Call**

Before you do anything, ensure you and your cl...