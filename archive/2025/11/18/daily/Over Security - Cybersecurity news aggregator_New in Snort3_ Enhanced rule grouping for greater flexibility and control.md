---
title: New in Snort3: Enhanced rule grouping for greater flexibility and control
url: https://blog.talosintelligence.com/new-in-snort3-enhanced-rule-grouping-for-greater-flexibility-and-control/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-18
fetch_date: 2025-11-19T03:14:35.729166
---

# New in Snort3: Enhanced rule grouping for greater flexibility and control

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

# New in Snort3: Enhanced rule grouping for greater flexibility and control

By
[Alex McDonnell](https://blog.talosintelligence.com/author/alex-mcdonnell/)

Tuesday, November 18, 2025 06:00

[Snort](https://blog.talosintelligence.com/category/snort/)
[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

Today, Cisco Talos is introducing new capabilities for Snort3 users within Cisco Secure Firewall. These enhancements are designed to give you greater flexibility in how you manage, organize, and prioritize detection rules. They also make it easier to align SNORT® rules with your organization’s specific security needs.

## The new “Severity” rule group

In Snort3, rule groups let you organize and manage detection rules according to specific criteria. Previously, only two top-level groups were available:

* Rule Category: groups rules by Snort2 categories such as FILE-OTHER, MALWARE-CNC, etc.
* MITRE ATT&CK: groups rules by attacker behaviors and techniques

These groups allow you to set a security level from 0 (all rules disabled) to 4 (all rules enabled).

The new Severity rule group introduces a third way to organize rules — by vulnerability severity, using CVSS scores. Rules are grouped as low, medium, high, or critical, allowing your team to prioritize detection based on the impact and urgency of vulnerabilities, rather than just category or behavior.

This makes it easier to focus attention and resources where they matter most.

## Flexible rule group creation based on time range

With the Severity group, you can define how far back in time you want your coverage to extend:

|  |  |  |
| --- | --- | --- |
| Level | Coverage | Description |
| 0 | None | No rules enabled |
| 1 | Last 2 years | Focuses on recent, high-impact vulnerabilities |
| 2 | Last 5 years | Balanced coverage of recent and mid-term threats |
| 3 | Last 10 years | Broad coverage for long-lived environments |
| 4 | All | Includes all vulnerabilities detected to date |

This approach gives you precise control over rule selection and volume. It helps optimize performance while ensuring your detection policies match your organization’s patching cycles, compliance requirements, and risk profile.

We’re also looking to develop more top-level groupings in the coming quarters. More details will be shared in due course.

## What this means for your environment

Configuring Snort3 previously required enabling rules individually or applying a predefined ruleset and then tuning manually. We know this wasn’t the most time-efficient process, so the Snort analyst team worked to simplify it with the new features announced today.

You can now:

* Enable rule groups aligned with your own internal policies
* Scale configurations across multiple environments without managing individual rules
* Adjust detection depth easily by time range or severity level

These capabilities make it simpler to maintain consistent, targeted detection coverage — whether you’re running large, distributed networks or smaller environments with tailored security priorities.

## Conclusion

The new Severity rule group and expanded rule group model give Snort3 users more flexibility and control.

By organizing rules based on vulnerability severity and timeframe, you can focus detection where it has the greatest impact, improving both efficiency and accuracy in threat management.

##### Share this post

#### Related Content

[### ICS protocol coverage using Snort 3 service inspectors

September 26, 2023 08:00

Service inspectors are an evolution of Snort 2's preprocessors, providing access to additional built-in rules that look for protocol-level abnormalities.](/ics-protocol-coverage-snort-3/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://talosintelligence.com/incident_response)
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* + ###### Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* + ###### Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* + ###### Support
  + [Support Documentation](https://support.talosintelligence.com)
* + ###### Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)
  + [Cisco Security](https://www.cisco.com/c/en/us/products/security/product-listing.html)

###### Follow us

[![Cisco](https://blog.talosintelligence.com/assets/images/logo_cisco_white.svg)](http://tools.cisco.com/security/center/home.x)

©
Cisco Systems, Inc. and/or its affiliates. All rights
reserved. View our
[Privacy Policy.](http://www.cisco.com/web/siteassets...