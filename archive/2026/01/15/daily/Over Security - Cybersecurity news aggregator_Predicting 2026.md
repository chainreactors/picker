---
title: Predicting 2026
url: https://blog.talosintelligence.com/predicting-2026/
source: Over Security - Cybersecurity news aggregator
date: 2026-01-15
fetch_date: 2026-01-16T03:30:12.936513
---

# Predicting 2026

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

# Predicting 2026

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Thursday, January 15, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

It’s become traditional at this time of year to make predictions about cybersecurity for the coming year. Obviously, no one has a crystal ball to predict the future, and if they did, they would be quietly making a fortune rather than sharing their insights in a newsletter. Any predictions about what lies ahead in the coming year should be taken with a generous pinch of salt.

However, the exercise isn’t futile. Taking time to pause and reflect on the current threat landscape, the forces driving change, and how our own exposure is evolving can help us form reasonable guesses about what might happen during the forthcoming year.

We’re living in a very tense geopolitical environment. We should expect continued use of infostealer malware and phishing campaigns as adversaries seek to map supply chains, and understand how organisations and governments may react to escalating aggression. As part of this activity, we’ll continue to see proxy actors conducting destructive attacks and financing their activities through extorting payment. Less sophisticated groups may also engage in website defacements or deploy disruptive malware in pursuit of political visibility or ideological goals.

Suffice to say that we are living in tense and difficult times. In a globally connected world, no one is isolated from the effects of conflict, no matter how distant it may seem.

At the same time, our use of technology continues to evolve, reshaping our threat exposure. Many organizations have already enthusiastically embraced generative AI. As AI systems are given more autonomy and broader access to internal systems, we can imagine that we will see breaches caused by poorly constrained or insufficiently governed AI agents.

Many accidental or malicious insider attacks are caused by individuals having excessive permissions or unfettered access to data with little oversight. We can imagine AI agents provoking similar incidents, whether through flawed design, unintended behavior, or deliberate prompt manipulation by an attacker.

While it is important to consider these newer and more exotic threats, we should not lose sight of the familiar ones. Unpatched systems, leaked credentials, accounts lacking multi-factor authentication, and poor network visibility continue to underpin many successful attacks.

One thing is certain: Cybersecurity teams will remain busy throughout 2026.  There will be threat actors attempting to compromise our systems, there will be new techniques that they will use, but there will be many more attacks using techniques that we *have* seen before.

It’s going to be a demanding year. Wishing good fortune and happy threat hunting to everyone.

## The one big thing

Cisco Talos is [monitoring UAT-8837](https://blog.talosintelligence.com/uat-8837), which we assess with medium confidence is a China-nexus advanced persistent threat (APT) actor. They have been actively targeting critical infrastructure organizations in North America since at least 2025. They typically gain access by exploiting vulnerabilities or using stolen credentials, then use a mix of open-source tools to steal sensitive data and create multiple ways back into the network. UAT-8837 adapts quickly, constantly changing up their tools to evade detection.

### Why do I care?

This group is focused on high-value targets and uses advanced, constantly evolving techniques that can bypass traditional defenses — even leveraging zero-day vulnerabilities. Their actions can lead to stolen credentials, persistent access, and potentially large-scale supply chain or infrastructure disruptions.

### So now what?

Stay vigilant by keeping systems patched, monitoring for the specific tools and behaviors outlined in [the report](https://blog.talosintelligence.com/uat-8837), and using up-to-date detection rules from sources like Talos. Proactively hunting for these IOCs and unusual user/account activity, combined with strong credential and privilege management, will be crucial to reducing risk from UAT-8837.

## Top security headlines of the week

**BreachForums** **breached, exposing** **324K cybercriminals**
In an ironic development, an individual using the moniker "James" published a database containing detailed information of hundreds of thousands of BreachForum users who believed they were operatinganonymously. ([DarkReading](https://www.darkreading.com/threat-intelligence/breachforums-breached-exposing-324k-cybercriminals))

**Target's dev server offline after hackers claim to steal source code**
An unknown threat actor has claimed to have stolen a trove of Target's internal source code and documentation and is selling it on dark web marketplaces. Multiple Target employees have now confirmed the authenticity of leaked source code sample set. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/targets-dev-server-offline-after-hackers-claim-to-steal-source-code/?utm_source=tldrinfosec))

**Predator spyware turns failed attacks into intelligence for future exploits**
New research reveals previously undocumented mechanisms that return information to developers on failed individual attacks. This means Predator can learn from its own failures so that future versions may be hardened against detection and analysis. ([SecurityWeek](https://www.securityweek.com/predator-spywares-granular-anti-analysis-features-exposed/))

**Instagram** **fixes** **password** **reset** **vulnerability** **amid** **user** **data** **leak**
Social media giant Meta confirmed an Instagram password reset vulnerability but denied being ...