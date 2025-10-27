---
title: Finding Access Control Vulnerabilities with Autorize
url: https://www.blackhillsinfosec.com/finding-access-control-vulnerabilities-with-autorize/
source: Black Hills Information Security
date: 2024-11-22
fetch_date: 2025-10-06T19:16:39.741793
---

# Finding Access Control Vulnerabilities with Autorize

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
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
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

21
Nov
2024

[Craig Vincent](https://www.blackhillsinfosec.com/category/author/craig-vincent/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)
[Access Control Vulnerability](https://www.blackhillsinfosec.com/tag/access-control-vulnerability/), [Access Controls](https://www.blackhillsinfosec.com/tag/access-controls/), [Autorize](https://www.blackhillsinfosec.com/tag/autorize/), [IDOR](https://www.blackhillsinfosec.com/tag/idor/)

# [Finding Access Control Vulnerabilities with Autorize](https://www.blackhillsinfosec.com/finding-access-control-vulnerabilities-with-autorize/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/CVincent-150x150.png)

| [Craig Vincent](https://www.blackhillsinfosec.com/team/craig-vincent/)

*Craig is a former software developer and red teamer. He has been pentesting at Black Hills Infosec since 2018.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/BLOG_chalkboard_00699.png)

In the most recent revision of the OWASP Top 10, Broken Access Controls leapt from fifth to first.[1](#8bdd48a6-d76b-447c-ad67-5e8d4191a989)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/Autorize_01.png)

**OWASP Top 10 Updates**

OWASP describes an access control as something that “enforces policy such that users cannot act outside of their intended permissions.” So, whenever we find that we can do something in a web application that we should not be allowed to do with our current permissions, then we have found an access control vulnerability. In addition to being common, access control vulnerabilities are often high impact when exploited.

Access control vulnerabilities can manifest in several different ways. For now, we’ll focus on the two types you are most likely to see in the wild: vertical access control vulnerabilities and horizontal access control vulnerabilities. Vertical access control vulnerabilities occur when an application has distinct privilege levels but does not correctly enforce access control across these privilege levels. For example, an application that has both regular users and higher-privileged administrative users should restrict regular users from performing actions reserved for administrative users. If the application does not prevent regular users from performing these privileged administrative actions, then that would be a vertical access control vulnerability. Horizontal access control vulnerabilities occur when users have equal privileges but are restricted to a subset of access/actions. For example, a self-service medical application that allows patients to log in and view their personal medical information should restrict users from accessing the data of other patients.

Before we dive into looking for access control vulnerabilities with Autorize, let’s do some setup. We want to be able to interact with the target application from multiple authentication contexts simultaneously, so we need to be able to log into the application with different user accounts at the same time. My preferred method of doing this is to run Firefox with the *–no-remote* and –*p* flags.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/Autorize_02.png)

**Launching Firefox**

The *–no-remote* flag[2](#e987d403-c612-498f-a41c-d983ea9c2657) tells Firefox to start a new instance and not to talk to any other existing instances. The *-p* flag tells Firefox to allow you to select a profile.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/Autorize_03.png)

**Firefox Prompt to Select a Profile**

I have created two profiles for penetration testing web applications: “Primary” and “Secondary”. These profiles are customized with useful extensions, UI modifications for quality screenshots, and some configurations[3](#3ccf630d-e041-40be-9836-5e2492aba8cf) (courtesy of Brian “BB” King) that quiet down some of the background noise Firefox typically makes. Once we’ve launched two separate instances of Firefox with two different profiles and configured them to proxy requests through Burp Suite, we are ready to start up Burp Suite and configure Autorize.

To install Autorize, you will need to select the “Extensions” tab in the top of Burp Suite, then select the “BApp Store” tab, and scroll down to the Autorize extension, and click the “Install” button. Fortunately, Burp Suite Pro is not required, and Autorize can be used with Burp’s free Community Edition.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/Autorize_04.png)

**Installing Autorize Extension**

If you have not been using other Burp Suite extensions that leverage Python, you will likely see a mes...