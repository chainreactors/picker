---
title: Revisiting the Detection and Response Gap
url: https://www.jumpsec.com/guides/revisiting-the-detection-and-response-gap/
source: JUMPSEC
date: 2023-01-20
fetch_date: 2025-10-04T04:24:37.189978
---

# Revisiting the Detection and Response Gap

[Skip to main content](#ajax-content-wrap)

* [twitter](https://twitter.com/JUMPSEC)
* [linkedin](https://www.linkedin.com/company/jumpsec/)
* [youtube](https://www.youtube.com/channel/UCpwVvJpDfFzBClzGhLUAZBw)

[New Blog - Building resilience against modern cyber threats -Read here](https://www.jumpsec.com/guides/building-resilience-against-modern-cyber-threats/)

* [About](https://www.jumpsec.com/about/ "About")
* [Careers](https://www.jumpsec.com/careers/ "Careers")
* [Accreditations](https://www.jumpsec.com/accreditations-awards/ "Accreditations")

Hit enter to search or ESC to close

Close Search

[![JUMPSEC](https://www.jumpsec.com/wp-content/uploads/2022/08/JUMPSEC-2021-Retina.png)![JUMPSEC](https://www.jumpsec.com/wp-content/uploads/2022/08/jumpsec-white-logo.png)](https://www.jumpsec.com)

[search](#searchbox)

[Menu](#slide-out-widget-area)

* [Home](https://www.jumpsec.com/ "Home")
* [Solutions](https://www.jumpsec.com/solutions/ "Solutions")
  + [Offensive](/solutions/#off "Offensive")
    - [Adversary Simulation Services](https://www.jumpsec.com/red-teaming-advanced-simulated-attack/ "Adversary Simulation Services")
    - [Purple Teaming](https://www.jumpsec.com/purple-teaming/ "Purple Teaming")
    - [Red Teaming](https://www.jumpsec.com/red-teaming/ "Red Teaming")
    - [Penetration Testing Services](https://www.jumpsec.com/penetration-testing/ "Penetration Testing Services")
  + [Defensive](/solutions/#def "Defensive")
    - [Continuous Attack Surface Management (CASM)](https://www.jumpsec.com/continuous-attack-surface-management-casm/ "Continuous Attack Surface Management (CASM)")
    - [Attack Path Mapping](https://www.jumpsec.com/attack-path-mapping/ "Attack Path Mapping")
    - [Incident Response Services](https://www.jumpsec.com/incident-response/ "Incident Response Services")
    - [Cyber Incident Exercising](https://www.jumpsec.com/cyber-incident-exercising/ "Cyber Incident Exercising")
    - [Cyber Incident Readiness](https://www.jumpsec.com/cyber-incident-readiness/ "Cyber Incident Readiness")
    - [Managed Extended Detection and Response (MXDR)](https://www.jumpsec.com/managed-detection-and-response-mdr/ "Managed Extended Detection and Response (MXDR)")
  + [Strategic](/solutions/#str "Strategic")
    - [Cyber Maturity Development](https://www.jumpsec.com/cyber-maturity-development/ "Cyber Maturity Development")
    - [Cyber Security Audit](https://www.jumpsec.com/security-audit-compliance/ "Cyber Security Audit")
  + [Casm](/continuous-attack-surface-management-casm/ "Casm")
* Resources
  + –
    - [InsightsUnderstand the threats you face and threats in the industry](https://www.jumpsec.com/insights/)
    - [Threat Intelligence HubHelping you to understand the threats you face](https://www.jumpsec.com/threat-intelligence-hub/)
    - [Case StudiesChallenges we have helped to resolve for leading organisations](https://www.jumpsec.com/case-studies/)
  + –
    - [VideosHave a look at our video guides to the cybersecurity sector](https://www.jumpsec.com/videos/)
    - [Ebooks and BrochuresWhat our experts have written about keeping your network safe](https://www.jumpsec.com/ebooks-and-brochures/)
    - [Jargon BustersNavigate the complex world of cyber security](https://www.jumpsec.com/jargon-busters/)
  + [–](https://www.jumpsec.com/new-events/)
    - [EventsWhat JUMPSEC has coming up and our previous events](https://www.jumpsec.com/new-events/)
    - [Webinars and PodcastsWatch our previous live events from industry professionals](https://www.jumpsec.com/webinars-and-podcasts/)
  + [Newest Blog PostUK Ransomware Payment Ban Implications](https://www.jumpsec.com/guides/uk-ransomware-payment-ban-implications-what-it-means-for-public-and-private-sector-cybersecurity/)
* [About](https://www.jumpsec.com/about/ "About")
  + [About Us](https://www.jumpsec.com/about/ "About Us")
  + [Leadership Team](https://www.jumpsec.com/leadership-team/ "Leadership Team")
  + [Accreditations & Awards](https://www.jumpsec.com/accreditations-awards/ "Accreditations & Awards")
  + [Careers](https://www.jumpsec.com/careers/ "Careers")
  + [News & Press Releases](https://www.jumpsec.com/news/ "News & Press Releases")
* [Labs](https://labs.jumpsec.com/ "Labs")
* [Contact](https://www.jumpsec.com/contact/ "Contact")

* [search](#searchbox)

![Overcoming the Cyber Detection and Response Gap](https://www.jumpsec.com/wp-content/uploads/2024/10/16x9.png)

# Overcoming the Cyber Detection and Response Gap

By [Miles](https://www.jumpsec.com/guides/author/miles/ "Posts by Miles")January 19, 2023August 1st, 2025[Consultant Blog](https://www.jumpsec.com/guides/category/consultant-blog/), [Insights](https://www.jumpsec.com/guides/category/insights/), [MXDR](https://www.jumpsec.com/guides/category/mxdr/)13 min read

[No Comments](https://www.jumpsec.com/guides/overcoming-the-cyber-detection-and-response-gap/#respond)

Share

ShareShareSharePin

*Matt Lawrence, Head of Defensive Security, and Dan Green, Head of Solutions, write about why compromise is inevitable – and the practical steps that organisations can take to build a security operating model capable of weathering the storm of cyber threats today.*

Despite the evolution of cyber threats, the common practices associated with threat detection and incident response remain largely unchanged.

The failure to adapt or advance means that many organisations rely on processes, procedures, and third-party services which are not able to effectively combat the nature of the threats faced today. This results in many organisations failing to take advantage of the capabilities, tooling, and approaches now available to defensive security professionals.

In this article, we discuss some of the limitations of conventional detection and response services and highlight the characteristics of an effective approach, appropriate for modern cyber threats.

### What is the detection and response gap?

The detection and response gap is defined as the time between an organisation identifying indicators of malicious activity or compromise, and undertaking triage, containment, and response activity.

**This gap exists for a number of reasons – and it’s becoming more impactful.**

Most MSSPs prioritise detection over response, where the containment and eradication of threats is not always included in the service offering and is often handed back to the client, or to a third-party. Where response is included, it is often slow moving, hampered by the absence of joint operating procedures, poorly clarified roles and responsibilities, and a limited understanding of what systems and functions are important to the client’s business.

Further, attacker ‘dwell time’ (the amount of time an attacker spends on a network before attempting to achieve their objective) is falling rapidly, rendering many typical detection and response solutions ineffective. A [2022 report from Mandiant](https://www.mandiant.com/m-trends) estimated the median dwell time for a ransomware attack in the Americas and EMEA as just 4 days, and **there is evidence in the wild of dwell times as short as 90 minutes**. Just a few years ago, the standard dwell time was considered to be weeks or months, with attackers persisting for long periods of time before executing an attack. By comparison in its [2020 threat report](https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf), Mandiant reported a global median dwell time of 56 days, compared to a 78 day global median dwell time reported in the same publication in 2019.

Whilst falling dwell times were previously seen as positive (i.e. the ability to detect persistent actors was improving) the simple reality is that attackers today are moving much faster. In many ways, this change is due to the ever-increasing maturity of the ransomware ecosystem. It indicates that initial access brokers (IABs) are highly synchronised with ransomware operators and that new information and access is quickly acted upon. There is le...