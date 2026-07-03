---
title: Catan and Mouse
url: https://blog.talosintelligence.com/catan-and-mouse/
source: Over Security
date: 2026-07-02
fetch_date: 2026-07-03T05:48:32.467985
---

# Catan and Mouse

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

# Catan and Mouse

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Thursday, July 2, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

> *“I do not know everything; still many things I understand.”*
> ― Madeleine L'Engle, A Wrinkle in Time

> *“Don't try to comprehend with your mind. Your minds are very limited. Use your intuition.”*
> ― Madeleine L'Engle, A Wind in the Door

The World Cup. The 4th of July as the US turns 250. Dungeon Crawler Carl. LeBron moving on. Wimbledon. AI. There are so many things that I could draw a parallel to farm for this week’s newsletter content. So let’s talk about board games.

A lot of skills come and go, and your journey with cybersecurity will be full of tools that you learn and then are gone. It’s a never-ending journey of learning. And it’s honestly the best thing about this career path for the kind of minds that are drawn to it. Innate curiosity is the currency of our cyber family.

Learning new and interesting board games (and I use the term broadly to circle in RPGs, card games, etc) is an incredible way to hone your mind and keep it focused on some of the most important tools that you will have.

Games will harness your ability to highlight anomalous activity, by players, by rulesets, by structure. They will also highlight your personal brand of brain activity and allow you to leverage your singular style and intuition into a weapon.

There are countless ways to win *Ticket to* *Ride* and your play style may be completely counter to someone you play with. That then creates patterns that you must learn to break. Nothing is more important to your defensive strategies than knowing yourself (know your environment!) and then breaking your tendencies to force your opponent to change their comfortable tactics (maybe, you’ve created some honeypot fake accounts to trigger identity alerts to track threat actors, to track their tooling and methodologies quietly).

This is nothing compared to the chaotic variance of a game like *Go* with its simplistic ruleset yet cascading complexity of each stone’s placement.

Learning a new game is a challenge and a great practice in and of itself, but learning how YOU and your strategies evolve as you learn the game will give you a microcosmic view into taking on new technologies, new coding languages, and new skill sets.

You will have peaks and valleys. So often in the work world we let the complexities and our imposter syndrome keep us from taking a risk or next step in our learning evolutions – next steps that we boldly take in our gaming lives.

So take what you learn from a *Machi Koro*, or *Pathfinder*, or *Catan*, or *Wingspan*, or *ADnD* *2e*, or ... you get the idea, take that same aggressive inquisitive mindset to your current work, turn it on its head and find a new way to do something you are already good at. And then look at something you struggle with and treat it like the next level. In the end, the worst that can happen is you fail. Because that’s where we learn.

> *"If the rule you followed brought you to this, of what use was the rule?"*
> – Cormac McCarthy, No Country for Old Men

## The one big thing

Cisco Talos is highlighting research into [ARToken](https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/) a fully-featured phishing-as-a-service (PhaaS) operator panel, branded "ARToken," that shares infrastructure, API contracts, and operational patterns with the EvilTokens platform documented by Sekoia and Microsoft in early 2026, and features capabilites previously not documented.

### Why do I care?

The ARToken panel exposes 80+ API endpoints for device code phishing, Primary Refresh Token (PRT) persistence, email access, business email compromise (BEC) operations, and SharePoint exfiltration — all accessible to operators through a React-based dashboard. These features indicate the platform is more mature than a simple device code phishing kit — it is a complete BEC operations environment.

### So now what?

Defenders should be aware of the kind of capabilities that this panel gives and use the [IOCs provided by Talos](https://github.com/Cisco-Talos/IOCs/blob/main/2026/07/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365.txt) to block malicious activity and use them as pivots for their internal hunts if they are present.

## Top security headlines of the week

**An aggressive password-spraying campaign targeting Microsoft 365 environments generated more than 81 million login attempts over a two-week period**
The threat actor tried to authenticate via Microsoft's Azure command-line interface (CLI) using still valid username and password combinations that had been exposed in past breaches. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-target-microsoft-365-accounts-with-81-million-login-attempts/))

**Threat actors are trying to leverage organization-owned AI agents to power complex threat activity**
By exploiting misconfigured or exposed AI endpoints, adversaries are increasingly turning enterprise-grade automation tools against their owners to facilitate more sophisticated and evasive cyberattacks. ([DarkReading](https://www.darkreading.com/cloud-security/attackers-hijack-exposed-ai-endpoints-power-offensive-ops))

**A recent authentication bypass vulnerability in the SimpleHelp remote monitoring and management (RMM) software has been exploited for malware delivery**
Tracked as CVE-2026-48558, the bug impacts SimpleHelp’s OpenID Connect authentication flow and allows a remote attacker to obtain a fully authenticated technician session. ([Security Week](https://www.securityweek.com/critical-simplehelp...