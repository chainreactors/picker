---
title: Bad Habits: An ANTISOC Operation
url: https://www.blackhillsinfosec.com/antisoc-operation/
source: Black Hills Information Security, Inc.
date: 2026-05-27
fetch_date: 2026-05-28T06:01:51.514037
---

# Bad Habits: An ANTISOC Operation

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
  + [Admin Team](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [Active SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
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

27
May
2026

[Corey Ham](https://www.blackhillsinfosec.com/category/author/corey-ham/), [Fun & Games](https://www.blackhillsinfosec.com/category/fun-games/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[ANTISOC](https://www.blackhillsinfosec.com/tag/antisoc/), [Continuous Penetration Testing](https://www.blackhillsinfosec.com/tag/continuous-penetration-testing/), [PROMPT#](https://www.blackhillsinfosec.com/tag/prompt/)

# [Bad Habits: An ANTISOC Operation](https://www.blackhillsinfosec.com/antisoc-operation/)

![Corey Ham](https://www.blackhillsinfosec.com/wp-content/uploads/2021/08/Corey-150x150.jpg)

| [Corey Ham](https://www.blackhillsinfosec.com/team/corey-ham/)

*Corey Ham leads the ANTISOC team at BHIS, delivering continuous pentesting services. When he’s not working, you’ll find him out in the woods or on a mountain somewhere.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/antisocop_header.png)

*This article was originally published in the ANTISOC Issue *(Continuous Penetration Testing)* of our free infosec zine, PROMPT#. Find it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-antisoc-edition/) or order your $3 physical copy on the [Spearphish General Store.](https://spearphish-general-store.myshopify.com/collections/prompt/products/prompt-infosec-zine-antisoc)*

[**ANTISOC**](https://www.blackhillsinfosec.com/services/antisoc/) uses a mix of techniques from traditional penetration tests like red teams, cloud, web applications, externals, internals, and, of course, social engineering. We combine this mix of techniques with a wide-open scope, with the goal of going beyond what a typical pentest can discover.

*Let’s dive into an example:*

Carl was a helpdesk technician.

As one of only two technicians working for ACME Inc, he was responsible for anything and everything that users needed help with. Carl was always confused by how many users needed their passwords reset. How could people be so forgetful of something they use every day? This issue was compounded by the fact that the security team had recently added the requirement that all users must pick longer, more complex passwords. It was difficult to even describe to a user what the criteria were: 15 or more characters, including a variety of uppercase, lowercase, numerical, and special characters.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/antisoc-2-1.png)

At first, he generated random passwords using the tool provided by the security team, but these were difficult to read to users over the phone. “M as in MARY, Janice, and by the way I think you need a new phone; I can barely hear you.” These random passwords were slowing things down too much. To save time, Carl came up with a secure password that was easy to dictate over the phone and met the password complexity requirements. He started assigning this password to all users who requested a reset, and it became second nature for him to recite it. He also set that password on any contractor accounts that expired because keeping track of all those different passwords was too complicated.

Carl figured the risks of doing this were minimal, as users would eventually change their passwords. What Carl didn’t realize is that when security changed the password policy to 15 characters, they also removed the requirement for users to change their passwords at a regular interval. This meant that over time, more and more users ended up using the identical password that had been set for them by Carl.

Eventually, an ANTISOC operator placed a social engineering phone call to Carl’s helpdesk and asked him to reset the password for a target user. Later, when the security team contacted him during an investigation, Carl found out that this particular password reset had led to an account compromise. The security team assured Carl that they had detected and contained the compromise, so he didn’t worry too much about it.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/04/antisoc-1.png)

ANTISOC operators noted that the password set by Carl wasn’t random. They had obtained a listing of all users from Entra ID during post-exploitation and decided to spray Carl’s password across these accounts. This led to the compromise of more than 100 accounts that Carl had reset passwords for over the years.

Most of these accounts had multi-factor authentication (MFA) set up properly, but some had not been used in years and did not have MFA configured. ANTISOC operators slowly picked through each account, taking note of any accounts that had not completed MFA enrollment. They configured MFA for them and quietly enume...