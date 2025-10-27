---
title: Clear, Concise, and Comprehensive: The Formula for Great SOC Tickets
url: https://www.blackhillsinfosec.com/the-formula-for-great-soc-tickets/
source: Black Hills Information Security
date: 2024-10-18
fetch_date: 2025-10-06T18:52:31.115296
---

# Clear, Concise, and Comprehensive: The Formula for Great SOC Tickets

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

17
Oct
2024

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Hayden Covington](https://www.blackhillsinfosec.com/category/author/hayden-covington/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/)
[Security Operations Center](https://www.blackhillsinfosec.com/tag/security-operations-center/), [SOC](https://www.blackhillsinfosec.com/tag/soc/)

# [Clear, Concise, and Comprehensive: The Formula for Great SOC Tickets](https://www.blackhillsinfosec.com/the-formula-for-great-soc-tickets/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/HCovington-150x150.png)

| [Hayden Covington](https://twitter.com/kilobytethedust)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/BLOG_chalkboard_00693.png)

A lot of emphasis and focus is put on the investigative part of SOC work, with the documentation and less glamorous side of things brushed under the rug. One such example is the simple SOC ticket: this could be internal or customer-facing, it could include a few sentences or paragraphs, it could contain everything necessary or be found lacking. I’m here to help you see your SOC tickets in a different light.

There are a few core pieces to a good ticket, as well as some general criteria that must be met, whether that ticket is internal or external facing. For the sake of this blog, I will be writing with the assumption that a customer might see the ticket you are working on.

**## 1: A Good SOC Ticket Includes All the Necessary Evidence**

Our investigations should build a case for the final part of our ticket — the assessment. Most of that case needs to be your supporting evidence, whether that is screenshots, logs, artifacts, etc. Weak evidence is not going to fly; probably not internally, and definitely not externally.

Based on the alert type you are working on, you need to provide solid log evidence, links, and screenshots that build a case for whether or not the alert is a true positive.

**## 2: A Good SOC Ticket is Clear and Concise**

There is such a thing as too much supporting evidence. Your ticket doesn’t need to include every unproductive rabbit hole you went down. As I mentioned above, the goal of your investigation is to build a case to support your assessment: what you think occurred and whether or not it is malicious activity. You can certainly do so in a few paragraphs, and while you do need to support your notes with evidence, you don’t want to overwhelm a customer or waste your own time by going over the top. Should more evidence be needed in the future, you can always build on your original investigation.

**## 3: A Good SOC Ticket Needs Solid Logical Reasoning**

One of the biggest things I’ve run into when performing quality checks on SOC tickets is that analysts will sometimes think either too broadly or too specifically about the alert they are working on. There is a middle ground to be had. If you think too broadly, you may be looking across weeks and months of logs, looking at unrelated activity, or looking over hundreds of hosts. If you are thinking too specifically, you might be missing one of the most important facets of an alert: it is supposed to be a warning sign of an attack, not an isolated task.

A story that I often use to illustrate that point is about a SOC ticket I once returned to an analyst at a prior organization. The alert that created the ticket was a data exfiltration alert that fired when a certain amount of data left an organization within a short timeframe. This alert hit on a cloud provider’s domain, specifically going to one of their storage services. However, since we used some services from that provider at our company, the analyst closed the ticket as an upload to a “vendor,” missing the key point that anyone could utilize the storage functions of that cloud provider.

Another good example is if during your investigation you discover that the alerting activity was blocked by a security control. That should not mean the ticket gets closed out and we move on. In a real attack scenario, the attacker isn’t going to shrug and say, “Well you got me,” and go home; they are going to try and find a way around that control. As previously stated, a SOC alert is often just an early warning system for an attack.

**## 4: A Good SOC Ticket is Reproducible**

Including queries used, links to results, or chains of events that brought you to a certain conclusion isn’t often going to make or break your ticket, but it will save you time and pain in the future. When looking at another analyst’s ticket, you should be able to reproduce their results or follow their reasoning. This al...