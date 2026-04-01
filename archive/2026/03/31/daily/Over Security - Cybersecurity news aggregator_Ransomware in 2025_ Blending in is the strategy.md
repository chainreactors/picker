---
title: Ransomware in 2025: Blending in is the strategy
url: https://blog.talosintelligence.com/ransomware-in-2025-blending-in-is-the-strategy/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:36.445709
---

# Ransomware in 2025: Blending in is the strategy

[Blog](/)

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

![](/content/images/2026/03/2025YiR-topic_ransomware.jpg)

# Ransomware in 2025: Blending in is the strategy

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Tuesday, March 31, 2026 06:00

[2025YiR](/category/2025yir/)
[Year In Review](/category/year-in-review/)
[ransomware](/category/ransomware/)

Ransomware attacks aren’t smash-and-grab anymore. They’re built on access that already looks legitimate — closer to positioning chess pieces than breaking the door down.

That’s the big trend that comes through in the ransomware data from the [Talos 2025 Year in Review](https://blog.talosintelligence.com/2025yearinreview/). Once attackers have initial access (and 40% of the time it’s through phishing) they move the way a user or administrator would: logging in, checking systems, and using the same remote access tools that are already installed.

In fact, one of the biggest challenges for defenders today is that ransomware actors are deliberately trying to overlap with everyday activity. RDP, PowerShell, and PsExec are the top three tools that are used by ransomware actors, but in many environments, these tools are part of normal operations.

The difference is how they’re being used. If they’re being used to expand access and move across systems, this should raise a few red flags. I’m not sure it’s possible to emphasise enough how important your asset management comes into play here — having clear asset inventories and network behaviour baselines and conducting continuous anomaly monitoring.

Like the rest of the Talos Year in Review, identity is what ties everything together. Valid accounts show up across nearly every stage of ransomware attacks: initial access, lateral movement, and execution.

## Top-targeted sectors

From our ransomware data analysis, manufacturing continues to be the most targeted sector, which reflects how challenging these environments are to monitor closely. There’s a mixture of systems, users, and processes, often with limited tolerance for disruption.

Professional, scientific, and technical services (second on the most targeted sectors list) face similar exposure, especially when access spans multiple systems or organizations.

## Most prolific ransomware groups

The ransomware-as-a-service (RaaS) groups have had a bit of a shakeup. After LockBit topped our 2024 report, the group fell to 35th this year following sustained law enforcement pressure. Qilin, a constant pain in the “you-know-what” for our incident responders for over a year now, came in at No. 1.

![](https://blog.talosintelligence.com/content/images/2026/03/data-src-image-f5271f1b-9f69-4f7c-950e-efb1ced6a44d.jpeg)

Qilin uses a double-extortion approach, combining data encryption with threats to release stolen information publicly. According to their data leak site, in 2025, Qilin targeted more than 40 victims every month except January, signaling that this ransomware group will remain a persistent and significant threat in 2026.

Akira and Play (No. 2 and 3 in the chart) had continued success, which can likely be credited to their evolving and adaptable tactics and absorption of affiliates from defunct ransomware groups (i.e., LockBit).

## An opportunity for defenders

What’s interesting to note is that for the second year running, January saw lower activity, likely tied to holiday slowdowns and Eastern European public holidays.

It may be wise for security teams to consider testing ransomware defenses in months where activity levels are generally lower, such as January, as there is a reduced chance of interfering with real incidents.

## Defender recommendations

* Strengthen identity protections. Actors predominately targeted the person who holds the key rather than the lock itself (i.e., the target’s infrastructure). Phishing and social engineering training is highly recommended.
* Monitor the use of built-in administrative tools such as RDP, PowerShell, and PsExec for lateral movement. Look for unexpected usage patterns, and abnormal access requests.
* Basics, basics, basics! They very much still hold true. Strengthen your backup, EDR, segmentation, logging, and recovery capabilities.
* Regularly test ransomware response readiness.

Read the full [2025 Talos Year in Review](https://blog.talosintelligence.com/2025yearinreview/) to dig deeper into ransomware trends, vulnerability exploitation, phishing and MFA bypass, state-sponsored activity, and how AI is shaping the threat landscape.

##### Share this post

#### Related Content

[### Talos Takes: 2025 insights from Talos and Splunk

March 26, 2026 08:48

This episode of Talos Takes breaks down the 2025 Year in Review as well as Splunk's Top 50 Cybersecurity Threats report.](/cybersecuritys-double-header-2025-insights-from-talos-and-splunk/)

[### Beers with Talos breaks down the 2025 Talos Year in Review

March 23, 2026 08:55

The Beers with Talos team unpack the biggest cybersecurity threats of 2025, from React2Shell to ransomware and identity abuse, and what it all means for defenders going forward.](/beers-with-talos-breaks-down-the-2025-talos-year-in-review/)

[### 2025 Talos Year in Review: Speed, scale, and staying power

March 23, 2026 08:01

The 2025 Talos Year in Review is available now. Understand evolving adversary playbooks and how to strengthen your organization’s defenses.](/2025-talos-year-in-review-speed-scale-and-staying-power/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://t...