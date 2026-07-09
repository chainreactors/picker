---
title: Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage
url: https://www.blackhillsinfosec.com/the-goldilocks-zone/
source: Black Hills Information Security, Inc.
date: 2026-07-08
fetch_date: 2026-07-09T06:02:25.533099
---

# Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/traditional-penetrating-testing/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [Web Application Testing](https://www.blackhillsinfosec.com/services/web-application-testing/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [Fusion PenTest](https://www.blackhillsinfosec.com/fusion-penetration-testing/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
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

8
Jul
2026

[Active SOC](https://www.blackhillsinfosec.com/category/blue-team/active-soc/), [Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [DFIR](https://www.blackhillsinfosec.com/category/dfir/), [Hayden Covington](https://www.blackhillsinfosec.com/category/author/hayden-covington/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[Alert Traige](https://www.blackhillsinfosec.com/tag/alert-traige/), [Detection Logic](https://www.blackhillsinfosec.com/tag/detection-logic/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/), [Orange Book](https://www.blackhillsinfosec.com/tag/orange-book/), [SIEM](https://www.blackhillsinfosec.com/tag/siem/)

# [Finding the “Goldilocks” Zone: A Practical Approach to Alert Triage](https://www.blackhillsinfosec.com/the-goldilocks-zone/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/10/HCovington-150x150.png)

| [Hayden Covington](https://twitter.com/kilobytethedust)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/07/goldilocks_header-1.png)

*This article was originally published in the InfoSec Survival Guide: Orange Book — Incident Response. Read it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-infosec-survival-guide-orange-book/), or grab it on the [Spearphish General Store](https://spearphish-general-store.myshopify.com/collections/infosec-survival-guides/products/the-infosec-survival-guide-orange-book-incident-response) (free digital download or a $1.25 physical copy, your call).*

Security engineers, analysts, and incident responders all have one thing in common, and I’m not talking about 3 AM phone calls concerning incidents. I’m talking about triage: that challenging moment of urgency when assessments must be made and classifications communicated—for the right things to be decided on to prevent the bad stuff from happening.

We’re all petrified about missing a critical event or misclassifying an alert, but when we’re talking about incident response (IR), there are often hundreds if not thousands of alerts to parse through. It’s easy to get caught up with one alert because it feels “too hot” or maybe not spend enough time looking into something that initially seems “too cold.” I’ll provide some tips, tricks, and techniques to help find that “Goldilocks Zone” of spending just the right amount of time on an alert, allowing you to quickly triage and move on to the next.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2026/07/coffee_first_classify_later_bordered-1024x375.png)

### Consider the Severities

The simplest way to triage events is to consider the severity of the alert. Initially, most Low-severity alerts should be entirely ignored. On any given case, time is limited, and the value return of going over hundreds of Low alerts is not even remotely comparable to that of reviewing higher priority findings.

Mediums will often be the bulk of your alert volume, with these being right in that uncomfortable middle of the “Probably nothing” of Lows and the “Definitely something” of Highs or Criticals. To move quickly on an IR engagement, I categorically relegate the Medium alerts to a later time on that case; and almost every time, the High and Critical alerts tell the real story, giving concrete direction on how to search the Mediums and Lows in a more targeted fashion.

### Anomalies Against the Baseline

One of the most surefire ways to quickly classify an event as a true or false positive is to compare the activity against the normal baseline: **“Does this happen regularly on this host,” “in this environment,” or maybe even “in any of the environments I can observe?”**

While a certain execution or activity on one host may appear anomalous, once you discover that it happens on a number of hosts across multiple environments, either you’ve just found your answer, or you’ve discovered a much bigger issue…

### Actions on Objective

One of my favorite tactics is considering “actions on objective.” If an attacker gains access to a host, they have an end goal in mind. Whether that goal is financially motivated, a desire to steal data, or even if they just want to observe activity in the environment—they broke in for a purpose. Someone ...