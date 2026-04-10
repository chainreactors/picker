---
title: From the field to the report and back again: How incident responders can use the Year in Review
url: https://blog.talosintelligence.com/from-the-field-to-the-report-and-back-again-how-incident-responders-can-use-the-year-in-review/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:47:19.194678
---

# From the field to the report and back again: How incident responders can use the Year in Review

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/2025YiR-topic_IR.jpg)

# From the field to the report and back again: How incident responders can use the Year in Review

By
[Jerzy ‘Yuri’ Kramarz](https://blog.talosintelligence.com/author/jerzy/)

Thursday, April 9, 2026 06:00

[2025YiR](/category/2025yir/)
[Year In Review](/category/year-in-review/)

Every year, Cisco Talos publishes [Year in Review](https://blog.talosintelligence.com/category/year-in-review/), a comprehensive look at the previous year’s threat landscape. It’s drawn from an enormous volume of telemetry, such as endpoint detections, network traffic, email data, and boots-on-the-ground [Cisco Talos Incident Response (Talos IR) engagements](https://blog.talosintelligence.com/category/ctir-trends/).

As incident responders, we see threats mid-detonation in the wreckage of an Active Directory environment, or in the lateral movement artifacts left behind by an affiliate who got in using nothing more than a valid account. The Year in Review distills those raw observations into structured intelligence, but that intelligence loop works both ways. The same report that our IR casework feeds into is the report that defenders should be feeding back into their own preparation cycles.

## IR casework shapes the Year in Review, the Year in Review shapes your readiness

When Talos IR closes out an engagement with customers, the tactics, techniques, and procedures (TTPs) we observe through forensic work and analysis are catalogued, aggregated, and analyzed alongside broader Cisco telemetry. When we track the emergence of a new exploit like React2Shell redefining attacker speed, or when we see Qilin rise to dominate the ransomware landscape while legacy groups like others maintain rare, sustained momentum, those shifts in the adversary ecosystem become the intelligence that informs what we are on the lookout for during the next investigation. When we observe patterns of behavior, they may form trend lines that [span multiple years](https://blog.talosintelligence.com/ir-trends-q4-2025/) and reveal how the landscape is evolving.

For defenders, this means the Year in Review is not a theoretical document. It is a distillation of what actually happened to organizations we respond to, investigated by the people who were in the room when things broke down. Here are some suggestions on how to operationalize these findings.

## Turning findings into tabletop scenarios

One of the most immediate and practical applications of Year in Review is raw material for tabletop exercises. The report hands you the adversary playbook. For example, the 2024 Year in Review highlighted that identity-based attacks accounted for 60% of all Talos IR cases, with Active Directory being the focal point in 44% of those incidents. Attackers were not breaking down doors with zero-days; rather, they were walking through the front door with stolen credentials, often bypassing multi-factor authentication (MFA) through push fatigue, misconfigured policies, or the simple fact that MFA was never fully enrolled in the first place for some accounts.

The [2025 Year in Review](https://blog.talosintelligence.com/2025yearinreview) reinforces and deepens this picture. Attacks against MFA evolved significantly, with MFA spray attacks doubling down on identity and access management (IAM) infrastructure while expanding efforts against high-value privileged accounts. Device compromise attacks saw a significant rise in activity, showing that actors increasingly value reliable, repeatable access methods over one-off exploitation. These are adversary preferences that should directly shape your exercise scenariosand cybersecurity preparedness.

That is a ready-made tabletop scenario. Work with your team on this exact entry scenario and walk through it just as adversary would. An adversary authenticates to your VPN. MFA fires, but the user approves the push because they were already expecting a login prompt. The attacker is now inside your perimeter with legitimate access. What does your detection look like? How quickly do your analysts identify the anomaly? Who makes the call to force a password reset and revoke sessions? These are some good questions to cover in this scenario. The 2025 Year in Review found that actors tailor their MFA attack style depending on the sector, and that manufacturing was the most impacted sector for ransomware in 2025, underscoring persistent risk to repeatedly targeted industries. If you operate in manufacturing, health care, or another sector that has appeared consistently in ransomware targeting data, your tabletop should reflect the specific TTPs directed at your vertical — not a generic ransomware exercise. These are just some ideas to get started on scenarios.

## Validate your detections against real-world tradecraft

Beyond tabletops, the Year in Review provides a prioritized list of what to test your detections against. Year after year, Talos IR engagements reveal a consistent core of adversary tradecraft that organizations are still struggling to detect. Tools like PowerShell and Mimikatz appear in a significant portion of engagements. Remote services such as RDP and SSH continue to be abused for lateral movement. Ransomware operators are increasingly disabling security solutions before deploying payloads, and in 2024, they succeeded in doing so at an alarming rate.

The 2025 Year in Review adds critical nuance to detection priorities through its vulnerability analysis. The top 10 most targeted vulnerabilities tell a story about what attackers reach for. React2Shell redefined attacker speed and targeting, [compressing the window between disclosure and exploitation](https://blog.talosintelligence.com/2025yearinreview). ToolShell's quick rise to the top five highl...