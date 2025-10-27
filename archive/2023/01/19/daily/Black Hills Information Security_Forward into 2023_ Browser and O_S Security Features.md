---
title: Forward into 2023: Browser and O/S Security Features
url: https://www.blackhillsinfosec.com/forward-into-2023-browser-and-os-security-features/
source: Black Hills Information Security
date: 2023-01-19
fetch_date: 2025-10-04T04:17:38.865158
---

# Forward into 2023: Browser and O/S Security Features

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

18
Jan
2023

[General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Joff Thyer](https://www.blackhillsinfosec.com/category/author/joff-thyer/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)

# [**Forward into 2023: Browser and O/S Security Features**](https://www.blackhillsinfosec.com/forward-into-2023-browser-and-os-security-features/)

[Joff Thyer](https://www.blackhillsinfosec.com/team/joff-thyer/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/01/BLOG_chalkboard_00608-1024x576.png)

## Introduction

We have already arrived at the end of 2022; wow, that was fast. As with any industry or aspect of life, we find ourselves peering into 2023 and wondering in which direction the information security landscape will evolve. As I contemplated this idea today, I thought I would write down a few introspective thoughts myself.

Firstly, the traditional security perimeter stack has evolved dramatically. We live in a world where the archaic concentric circles model — aka the moat around the castle — has completely dissolved. Anywhere from cloud migration to highly functional apps delivered directly in the browser, to end-user enabled shadow IT, zero trust security models, and so on has resulted in a complete rethinking of boundaries, along with a considerable amount of anxiety of behalf of security professionals. Just where is our data? How well is it protected? Are the dev-ops engineers trained well enough to keep security front of mind in an agile delivery world? Do all these cloud providers give us the right tools to secure our organization?

We must all adapt to these challenges through change. Holding onto an illusion of control through the castle and moat model is a fool’s errand. While I could write about the plethora of information security implications that this rapidly evolving model has introduced, I wish to focus for now on the commonly used Windows workstation endpoint.

With the endpoint we have seen a dramatic improvement in the deployed security technologies that protect the operating system itself. The endpoint/extended detection and response (EDR/XDR) software capabilities have matured significantly, making both initial compromise and post exploitation activities on the Windows endpoint extraordinarily challenging assuming mature deployment and tuning.

While I think we can all agree this is fabulous news for the industry, we should ask ourselves whether maximizing desktop O/S protections still matters as much as it used to. Otherwise said, we must concede that the web browser is where critical business data is increasingly being managed.

The natural corollary question is whether sufficient security technologies are deployed in the browser. Do these protections rival the O/S deployed protections? Are these protections integrated with the O/S level defensive deployments?

## Google Chrome and Chromium Project

Let’s start with the web browser market share[1](#references). Google Chrome clearly leads the pack in adoption. There are additionally browsers based on Google’s Chromium project, such as Opera and Microsoft Edge, which notably holds second place to Chrome. From this data, we can conclude that any security vulnerabilities in the Chromium open-source project will be very significant and that proprietary security-related code in the Chrome and Edge browsers is also critically important.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/01/Picture1.png)

**Web Browser Market Share**

Given this backdrop, what security features are implemented in Chrome and Chromium that help defend the browser and its user[2](#references)?

The team at Google have created a security architecture[3](#references) diagram which does a pretty good job of identifying the attack surfaces from a process level perspective below[4](#references). The major target areas of concern are the browser process and the renderer processes.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/01/Picture2.png)

**Chrome Security Architecture from Process Perspective**

Given the browser architecture landscape and process level concerns above, let’s break down some of the protective technologies that have been authored in response to browser security concerns. Please note that much of the below information has been researched and somewhat paraphrased from Google blogs and design documents available online. There are several key architectural foundations and features in the Chrome/Chromium browser effort th...