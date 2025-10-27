---
title: Beaches and breaches
url: https://blog.talosintelligence.com/beaches-and-breaches/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-12
fetch_date: 2025-10-02T20:02:26.545719
---

# Beaches and breaches

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

# Beaches and breaches

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, September 11, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

I took a two-week vacation (thanks to Bill for covering my author shift last week) and made the deliberate choice to leave my laptop behind. No emails, IMs, no IT at all. Thank you, European work culture! It was a complete break.

Well, almost.

The weather didn’t always cooperate, so instead of freezing on a beach, I found myself catching up on TV — mostly news and a few series. But wherever I clicked, I just couldn’t escape the daily dose of AI. What can we do about invasive mosquitos? Ask AI. Government doesn’t move the needle? Ask AI. Want the weather forecast? AI, obviously. There are countless ads with people asking AI whether or not to wear a jacket “because it might rain.” Even with your favorite TV shows, gone are the days when the hoodied hacker sits in front of a black terminal with green text running a dangerous (haha) ping or nmap. Now, they're writing lines like, “Did you try breaking the firewall with our latest AI algorithm, bro?”

Coming back to work and catching up on our industry news, I almost expected AI to be dominating the headlines. But it wasn't, and neither was ransomware. Instead, they were all about breaches. Many — but not all — reports referenced compromised OAuth tokens linked to Salesloft’s Drift integration, with a notable number of high-profile victims. Sure, this isn’t a scientific or qualitative analysis (ransomware isn’t disappearing anytime soon), but the reporting and the headlines have definitely shifted from one to the other.

Looking past the buzzwords and catchphrases, the headlines really boiled down to two main themes: supply chain and identity attacks. In a SaaS world, I think it’s time to rethink their definitions and priority levels.

Why? First, supply chain attacks aren’t limited to hardware or [software](https://hackread.com/npm-packages-2-billion-downloads-hacked-attack/) anymore. We need to consider the datapath (or where data possibly is processed) as a key part of the supply chain.

Second, identity attacks don’t just target users; interconnected applications are increasingly at risk, too. I’m not saying we can ignore the users, especially with [current reporting](https://trust.salesloft.com/?uid=Update+on+Mandiant+Drift+and+Salesloft+Application+Investigations) that it started with access through a GitHub account or software vulnerabilities in our “classic” applications, but we absolutely need to broaden our focus. Last week’s headlines made that clear.

## The one big thing

Cisco Talos’ [latest blog post](https://blog.talosintelligence.com/maturing-the-cyber-threat-intelligence-program/) details the Cyber Threat Intelligence Capability Maturity Model (CTI-CMM), a framework that helps organizations assess and enhance their cyber threat intelligence programs across 11 key domains. By outlining clear maturity levels and improvement cycles, CTI-CMM can help your team benchmark your current capabilities and develop a strategy for continuous (and practical) growth.

### Why do I care?

Understanding and improving your CTI program’s maturity can help your organization better anticipate, detect, and respond to cyber threats, no matter your budget or staffing level. It also makes the security investments you do have more effective, and ensure your team’s efforts are aligned with business priorities.

### So now what?

Check out the [CTI-CMM framework](https://blog.talosintelligence.com/maturing-the-cyber-threat-intelligence-program/) to assess where your organization stands, identify gaps and opportunities, and create a roadmap to practical improvements for your organization.

## Top security headlines of the week

**Huge NPM supply chain attack goes out with whimper**
A supply chain attack involving multiple NPM packages had the potential to be one of the most impactful security incidents in recent memory, but such fears seemingly have proved unrealized. ([Dark Reading](https://www.darkreading.com/application-security/huge-npm-supply-chain-attack-whimper))

**Swiss Re warns of rate deterioration in cyber insurance**
Increased competition among insurers has led to a third consecutive year of reduced rates, according to the report, as the available supply of cyber coverage has exceeded current demand. ([Cybersecurity Dive](https://www.cybersecuritydive.com/news/swiss-re-rate-deterioration-cyber-insurance/759370/))

**Critical SAP vulnerability actively exploited by hackers**
A critical security flaw has been found in several SAP products, and could allow a malicious actor to gain administrator-level control. ([HackRead](https://hackread.com/hackers-exploit-cve-2025-42957-sap-vulnerability/?utm_source=tldrinfosec))

**No gains, just pains: 1.6M fitness phone call recordings exposed**
Sensitive info from hundreds of thousands of gym customers and staff was left sitting in an unencrypted, non-password protected database. Audio recordings spanned from 2020 to 2025. ([The Register](https://www.theregister.com/2025/09/09/gym_audio_recordings_exposed/?utm_source=tldrinfosec))

**US offers $10M reward for Ukrainian ransomware operator**
Volodymyr Tymoshchuk allegedly hit hundreds of organizations with the LockerGoga, MegaCortex, and Nefilim ransomware families. According to an indictment, the intrusions caused hundreds of millions of dollars in losses. ([Security Week](https://www.securityweek.com/us-offers-10-million-reward-for-ukrainian-ransomware-operator/))

**China accuses Dior's Shanghai branch of illegal data transfer**
China's public security authority alleges that Dior's Shanghai branch has ...