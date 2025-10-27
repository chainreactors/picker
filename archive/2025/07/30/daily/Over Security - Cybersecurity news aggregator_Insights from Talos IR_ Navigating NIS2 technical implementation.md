---
title: Insights from Talos IR: Navigating NIS2 technical implementation
url: https://blog.talosintelligence.com/insights-from-talos-ir-navigating-nis2-technical-implementation/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-30
fetch_date: 2025-10-06T23:54:03.671342
---

# Insights from Talos IR: Navigating NIS2 technical implementation

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

# Insights from Talos IR: Navigating NIS2 technical implementation

By
[Jerzy ‘Yuri’ Kramarz](https://blog.talosintelligence.com/author/jerzy/)

Tuesday, July 29, 2025 06:00

[The Need to Know](https://blog.talosintelligence.com/category/the-need-to-know/)

When the [NIS2 Directive arrived in 2023](https://blog.talosintelligence.com/what-is-nis2-and-how-can-you-best-prepare-for-the-new-cybersecurity-requirements-in-the-eu/), organizations [across Europe](https://www.cisco.com/site/us/en/solutions/security/cybersecurity-for-government/index.html#accordion-03a94d77f3-item-545e220524) began preparing for [enhanced](https://www.cisco.com/site/us/en/solutions/security/cybersecurity-for-government/index.html) cybersecurity requirements. Many focused on obligations such as rapid incident notifications and comprehensive security policies. However, while the directive provided the "what," it left the "how" largely undefined. Organizations understood that they needed incident response capabilities and swift reporting mechanisms, but the details of implementation remained unclear.

The release of [ENISA's Technical Implementation Guidance](https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf) in June 2025 revealed the true complexity of compliance with the [NIS2 standard](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive). The technical guidance now reveals requirements that fundamentally challenge conventional security operations, particularly during incidents. Organizations that once prioritized operational continuity over forensic response and detailed analysis must now balance all three.

## Competing objectives in incident response

Under the old approach, organizations had the flexibility to isolate, investigate and report incidents at their own pace. These processes were typically be dictated by business needs, with exceptions for when personal data was [involved under GDPR](https://gdpr-info.eu/art-33-gdpr/).

Now, the clock starts ticking toward a 24-hour deadline from the moment an incident happens ([Article 23 of the NIS2 Directive](https://www.nis-2-directive.com/NIS_2_Directive_Article_23.html)).

The incident response procedures outlined in Section 3.5.2 of the [ENISA guidance](https://www.enisa.europa.eu/sites/default/files/2025-06/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1.0.pdf) illustrate this shift perfectly. Security teams must now "recognize and address potential conflicts between forensic activities, incident response activities, and operational continuity." The guidance explicitly acknowledges that teams face competing objectives:

1. Preserve evidence for legal purposes
2. Mitigate current threats to minimize business disruption
3. Minimize IT service downtime to maintain operational continuity

Traditional incident response playbooks assume you can prioritize one or two of these objectives. NIS2 demands all three simultaneously.

Let’s consider an example. A ransomware attack hits payment processing systems at midnight. According to Section 3.2.3, teams must maintain comprehensive logs including "all privileged access to systems and applications and activities performed by administrative accounts," while Section 3.5.4 requires logging all incident response activities and recording evidence. At the same time, the business operations would require system restoration to process morning transactions so that the bottom line is not impacted.

Throughout this process, someone must compile an initial report meeting the notification requirements within 24 hours as mandated by Article 23(3) of the NIS2 Directive. This is followed by a more detailed report with impact assessment details within 72 hours. Not to mention, organizations operating across borders may need country-specific procedures to support notification timelines.

The guidance acknowledges the inherent conflict in these objectives and requires organizations to "establish a clear decision-making process that prioritizes based on the accepted risk tolerance levels, business impact and legal obligations."

## Logging requirements

Another key challenge lies in the depth of logging requires. Section 3.2.3 specifies that logs shall include, where appropriate: "(a) relevant outbound and inbound network traffic; (b) creation, modification or deletion of users of the relevant entities' network and information systems and extension of the permissions; (c) access to systems and applications; (d) authentication-related events; (e) all privileged access to systems and applications and activities performed by administrative accounts" as well as 7 additional categories, for 12 total. All this assumes visibility into shadow IT and appropriate configuration of user activity tracking so that a proper audit trail can be constructed, reviewed and stored for analysis.

Furthermore, the guidance notes in Section 3.2.6 that monitoring and logging systems must be redundant, and that "the availability of the monitoring and logging systems shall be monitored independent of the systems they are monitoring." Although this is music to an incident responder’s ears, setting up the complex systems needed to correlate, analyze, store and retrieve detailed audits is a significant challenge.

## Forensic activities vs. business recovery

Traditional incident response strategies often prioritize rapid recovery to ensure that business operations can return to normal while simultaneously analyzing evidence. Incident response teams often want to acquire all evidence upfront so that business recovery can begin alongside the forensic investigation. The business can also decide what to recover and even go as far as to simply make decision to rebu...