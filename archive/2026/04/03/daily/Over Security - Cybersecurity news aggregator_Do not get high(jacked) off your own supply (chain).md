---
title: Do not get high(jacked) off your own supply (chain)
url: https://blog.talosintelligence.com/protecting-supply-chain-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-03
fetch_date: 2026-04-04T04:17:30.147268
---

# Do not get high(jacked) off your own supply (chain)

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

# Do not get high(jacked) off your own supply (chain)

By
[Dave Liebenberg](https://blog.talosintelligence.com/author/dave-liebenberg/)

Friday, April 3, 2026 13:31

[On The Radar](https://blog.talosintelligence.com/category/on-the-radar/)

In the span of just a few weeks, we have observed a dizzying array of major supply chain attacks. Prominent examples include the malicious modification of [Axios](https://blog.talosintelligence.com/axois-npm-supply-chain-incident/), a popular HTTP client library for JavaScript, as well as cascading compromises from TeamPCP, a “chaos-as-a-service” group that injected malicious code into hijacked GitHub repositories for open-source projects, including Trivy, an open-source security scanner.

The impact of these supply chain attacks can be vast. Axios receives 100 million downloads weekly and innumerable organizations rely on the frameworks and libraries compromised by TeamPCP. The headache they pose to organizations and their security personnel is considerable as well; affected utilities can be integrated so deeply that it may be difficult to fully catalog, let alone remediate.

Although the timing, scale, and severity of these attacks can be shocking, this is not a new phenomenon. The supply chain has remained an attractive target for some time because of its fragility and the fact that a successful compromise can lead to countless additional downstream victims.

Findings from the recently published [Talos 2025 Year in Review](https://blog.talosintelligence.com/2025yearinreview/) illustrate these long-standing trends. Nearly 25% of the top 100 targeted vulnerabilities we observed in 2025 affect widely used frameworks and libraries. Digging deeper into the list reveals additional insights. The React2Shell vulnerability affecting React Server Components became the top-targeted vulnerability of 2025 despite being disclosed in December, reflecting the speed at which these supply chain attacks can reach massive scale. The presence of Log4j vulnerabilities shows how deeply embedded these utilities can be and therefore how difficult it can be to reduce the attack surface. Although these particular examples represent extant vulnerabilities that can be weaponized by numerous adversaries versus a deliberate attack carried out by a single adversary, they show how impactful and disruptive threats to the supply chain can be. Follow-on attacks can range from ransomware to espionage, which is reflective of the broad swath of adversaries that carry them out — from sophisticated state-sponsored groups to teenage cyber criminals.

If we are all building on such shaky foundation, what can we do to keep safe? After all, it certainly seems dire when a tool such as Trivy that we could normally use to scan for supply chain vulnerabilities becomes compromised itself. But there are concrete steps we can take to improve our security posture.

As highlighted in the Year in Review, protecting identity is key. This includes securing CI/CD pipelines to prevent these types of compromises from occurring in the first place, as well as limiting the impact and lateral movement of an adversary should they obtain access to a downstream victim.

In addition, organizations must try to the best of their abilities to inventory the software libraries and frameworks they employ, stay informed of security incidents, and respond rapidly to implement patching and other mitigations.

Just as supply chain attacks are evergreen, so too is the efficacy of security fundamentals, such as segmentation, robust logging, multi-factor authentication (MFA), and the implementation of emergency response plans.

As trust continues to break down, the only viable solution may be to double down on vigilance. Since this recent spate of attacks represents a trend that will likely only grow in intensity and breadth, the time for action and planning is now.

## Coverage

Below, find a sample of the some of the recent coverage we offer to protect against these threats:

ClamAV:
Txt.Trojan.TeamPCP-10059839-0

Txt.Trojan.TeamPCP-10059839-0

Behavioral Protections:
LiteLLM Supply Chain Compromise – alerts during installation of compromised packages

##### Share this post

#### Related Content

[### New in Snort3: Enhanced rule grouping for greater flexibility and control

December 9, 2025 06:00

Today, Cisco Talos is introducing new capabilities for Snort3 users within Cisco Secure Firewall to give you greater flexibility in how you manage, organize, and prioritize detection rules.](/new-in-snort3-enhanced-rule-grouping-for-greater-flexibility-and-control/)

[### Spy vs. spy: How GenAI is powering defenders and attackers

December 4, 2025 06:00

Generative AI is rapidly transforming cybersecurity for both defenders and attackers. This blog highlights current uses, emerging threats, and the evolving landscape as capabilities advance.](/spy-vs-spy-how-genai-is-powering-defenders-and-attackers/)

[### Think passwordless is too complicated? Let's clear that up

October 24, 2025 06:00

We’ve relied on passwords for years to protect our online accounts, but they’ve also become one of the easiest ways attackers get in. Cisco Duo helps clear up some of the biggest passwordless myths.](/passwordless-mythbusting-with-cisco-duo/)

* + ###### [Intelligence Center](https://talosintelligence.com/reputation)
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* + ###### [Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* + ###### [Incident Response](https://talosintelligence.com/incident_response)
  + [Reactive Se...