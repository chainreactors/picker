---
title: Stopping ransomware before it starts: Lessons from Cisco Talos Incident Response
url: https://blog.talosintelligence.com/stopping-ransomware-before-it-starts/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-09
fetch_date: 2025-10-02T19:52:09.322937
---

# Stopping ransomware before it starts: Lessons from Cisco Talos Incident Response

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

![](/content/images/2025/09/talos-evergreen-ransomware-2000x1000.jpg)

# Stopping ransomware before it starts: Lessons from Cisco Talos Incident Response

By
[Lexi DiScola](https://blog.talosintelligence.com/author/lexi/)

Monday, September 8, 2025 06:00

[Cisco Talos Incident Response](/category/cisco-talos-incident-response/)
[ransomware](/category/ransomware/)

* Over the past two and a half years (January 2023 through June 2025), Cisco Talos Incident Response (Talos IR) has responded to numerous engagements that we classified as pre-ransomware incidents.
* Talos looked back to analyze what key security measures were credited with deterring ransomware deployment in each pre-ransomware engagement, finding that the top two factors were swift engagement with the incident response team and rapid actioning of alerts from security solutions (predominantly within two hours of the alert).
* We also classified almost two dozen observed pre-ransomware indicators in these engagements, as the top observed tactics provide insight into what malicious activity frequently preempts a more severe attack. Finally, we analyzed Talos IR’s most frequent recommendations to customers to ascertain common security gaps.
* Aggregation of this data and the follow-on analysis is intended to provide actionable guidance that can assist organizations in improving their defenses against ransomware activity.

---

## What characterizes an incident as “pre-ransomware?”

Talos IR associates specific adversary actions with pre-ransomware activity. When threat actors attempt to gain enterprise-level domain administrator access, they often conduct a series of account pivots and escalations, deploy command-and-control (C2) or other remote access solutions, harvest credentials and/or deploy automation to execute the modification of the OS. Though the specific tools or elements in the attack chain vary by adversary, Talos IR has seen these same classic steps in practice for years. These actions, along with observed indicators of compromise (IOCs) or tactics, techniques and procedures (TTPs) that we associate with known ransomware threats without the end result of enterprise-wide encryption, lead us to categorize an incident as “pre-ransomware.”

It is worth noting that some of the above attack techniques are also often deployed by initial access brokers (IABs) who seek to gain and sell access to compromised systems, and it is possible some of the incidents involved in this case study could have therefore been perpetrated by IABs instead of ransomware operators. While it is often challenging to determine a threat actor’s end goal, we have high confidence that all incidents involved tactics are consistently seen preceding ransomware deployment. If the adversary was instead an IAB, we have seen these types of IAB campaigns very frequently result in a ransomware attack after access has been sold, rendering the activity relevant to this analysis.

## Key security actions and measures that deter ransomware deployment

Talos analyzed incident response engagements spanning the past two and a half years that we categorized as pre-ransomware attacks, identifying actions and security measures that we assessed were key in halting adversaries’ attack chains before encryption. An overview of our findings can be found in Figure 1, followed by a more thorough breakdown of each category to explore exactly how certain actions impeded ransomware execution.

![](https://blog.talosintelligence.com/content/images/2025/09/pre-ransomware-hindered.jpg)

Figure 1. Pie chart of factors hindering ransomware deployment.

### Swift engagement of Talos IR

[Engaging Talos IR](https://blog.talosintelligence.com/talos-ir-ransomware-engagements-and-the-significance-of-timeliness-in-incident-response/) within one to two days of first observed adversary activity (though we advise engagement as quickly as possible) was credited with preventing a more serious ransomware attack in approximately a third of engagements, providing benefits such as:

* **Extensive knowledge of the threat landscape:** In multiple engagements, Talos IR was able to correlate TTPs and IOCs on customers’ networks with other ransomware and pre-ransomware engagements we had responded to, identifying when the infection was part of a larger, widespread campaign. This insight helped Talos IR anticipate and intercept adversaries’ next steps as well as provide customers additional IOCs to block that were seen in other engagements.
* **Actionable recommendations for isolation and remediation:** In some engagements, the customers quickly acted on Talos’ pre-ransomware security guide, which Talos IR assessed prevented more catastrophic events.
* **Enhanced monitoring:** The Cisco Extended Detection and Response (Cisco XDR) team can provide extra vigilance in their monitoring after containment of the pre-ransomware threat to ensure full eradication.

We observed numerous incidents where Talos IR was not engaged by the customer immediately, which enabled the adversary to continue working through their attack chain and conduct data theft and/or ransomware deployment. This often results in consequences such as backup files being corrupted or encrypted, endpoint detection and response (EDR) and other security tools being disabled, disruption to day-to-day operations and more.

### EDR/MDR alert prompted security teams’ rapid containment

Vigilant monitoring of security solutions and logs allows network administrators to act quickly when a threat is first detected, isolate the malicious activity and cut off threat actors’ ability to escalate their attack. In our case study, action from the security team within two hours of an alert from the organization’s EDR or managed detection and response (MDR) solution correlated with successful isolation of the th...