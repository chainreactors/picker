---
title: Threat Spotlight: WarmCookie/BadSpace
url: https://blog.talosintelligence.com/warmcookie-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-24
fetch_date: 2025-10-06T18:55:46.261667
---

# Threat Spotlight: WarmCookie/BadSpace

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2024/10/WarmCookie.jpg)

# Threat Spotlight: WarmCookie/BadSpace

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/),
[Jordyn Dunk](https://blog.talosintelligence.com/author/jordyn/),
[Nicole Hoffman](https://blog.talosintelligence.com/author/nicole/),
[Holger Unterbrink](https://blog.talosintelligence.com/author/holger-unterbrink/)

Wednesday, October 23, 2024 06:02

[SecureX](/category/securex-3/)
[Threat Spotlight](/category/threat-spotlight/)
[Stealer](/category/stealer/)

* WarmCookie is a malware family that emerged in April 2024 and has been distributed via regularly conducted malspam and malvertising campaigns.
* WarmCookie, observed being used for initial access and persistence, offers a means for continuous long-term access to compromised environments and is used to facilitate delivery of additional malware such as [CSharp-Streamer-RAT](https://malpedia.caad.fkie.fraunhofer.de/details/win.csharpstreamer) and [Cobalt Strike](https://malpedia.caad.fkie.fraunhofer.de/details/win.cobalt_strike).
* Post-compromise intrusion activity associated with WarmCookie overlaps with previously observed activity we attribute to TA866.
* We [assess](https://blog.talosintelligence.com/on-conveying-doubt/) that WarmCookie was likely developed by the same threat actor(s) as [Resident](https://www.esentire.com/blog/esentire-threat-intelligence-malware-analysis-resident-campaign) backdoor, a post-compromise implant previously deployed in intrusion activity that Cisco Talos attributes to [TA866](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/).

# What is WarmCookie?

[WarmCookie](https://malpedia.caad.fkie.fraunhofer.de/details/win.warmcookie), also known as BadSpace, is a malware family that has been distributed since at least April 2024. Throughout 2024, we have observed several distribution campaigns conducted using a variety of lure themes to entice victims to take actions that result in malware infection.

These campaigns typically rely on malspam or malvertising to initiate the infection process that results in the delivery of WarmCookie. WarmCookie offers a variety of useful functionality for adversaries including payload deployment, file manipulation, command execution, screenshot collection and persistence, making it attractive to use on systems once initial access has been gained to facilitate longer-term, persistent access within compromised network environments.

In previously analyzed intrusion activity involving WarmCookie, we have observed that it is used as an initial payload and that CSharp-Streamer-RAT and [Cobalt Strike](https://malpedia.caad.fkie.fraunhofer.de/details/win.cobalt_strike) were delivered following the initial WarmCookie infection.

While analyzing the campaigns, intrusion activity, and infrastructure associated with WarmCookie over the course of 2024, we also identified multiple overlaps with activity conducted by [TA866](https://blog.talosintelligence.com/highlighting-ta866-asylum-ambuscade/) in 2023.

# Typical infection chains

As previously mentioned, we have observed WarmCookie campaigns being conducted since at least April 2024. These campaigns rely on malspam or malvertising to facilitate the delivery of malicious content.

In the case of malspam, we have observed consistent use of invoice-related and job agency themes that entice victims to access hyperlinks present in either the email body, or within attached documents, such as PDFs.

Examples of common message subjects observed in campaigns conducted between April and August 2024 are listed below.

* `United Rentals Inc: Invoice# [0-9]{9}\-[0-9]{3}`
* `Invoice and Remittance`

In a recent campaign conducted in August, the messages contained PDF attachments. The attachment filenames were randomized but typically use the following format.

* `Attachment_[0-9]{3}\-[0-9]{3}\.pdf`

While there have been variations over time, below is a representative example of one of these emails and the associated PDF attachment.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-a9bcabae-965d-49a2-9fa4-f95fff22e06f.png)

**WarmCookie emails and attachments.**

The PDFs contain hyperlinks that direct victims to web servers hosting malicious JavaScript files that continue the infection process.

We have also observed WarmCookie campaigns leveraging infrastructure associated with traffic distribution and malware delivery systems. In one early campaign, we observed the use of the LandUpdates808 cluster of infrastructure described [here](https://malasada.tech/the-landupdate808-fake-update-variant/). In observed cases, malicious JavaScript downloaders were being hosted at the following paths on servers associated with the LandUpdates808 cluster of web servers.

/wp-content/upgrade/update[.]php

Regardless of whether the delivery stage of the attack was conducted via malspam or malvertising, an obfuscated JavaScript downloader is delivered that is responsible for continuing the infection process. We have observed the use of ZIP archives to compress the JavaScript file and the delivery of the JavaScript file directly from the distribution infrastructure.

When executed, it deobfuscates and executes a PowerShell command that uses Bitsadmin to retrieve and execute the WarmCookie DLL using syntax, like that shown below.

![](https://blog.talosintelligence.com/content/images/2024/10/image-23.png)

**PowerShell execution.**

We have observed a relatively small number of distribution servers hosting WarmCookie DLLs compared to the infrastructure used in earlier stages of the infection chain.

## WarmCookie

The main WarmCookie payload has been extensively analyzed in prior reporting [here](https://www.gdatasoftware.com/blog/2024/06/37947-badspace-backdoor) and [here](https://www.elasti...