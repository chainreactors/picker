---
title: Ghosted by a cybercriminal
url: https://blog.talosintelligence.com/ghosted-by-a-cybercriminal/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-23
fetch_date: 2025-10-06T22:29:56.115003
---

# Ghosted by a cybercriminal

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

# Ghosted by a cybercriminal

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, May 22, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Talos recently [published research](https://blog.talosintelligence.com/compartmentalized-threat-modeling/) into how threat actors are increasingly teaming up across the attack chain. Each group handles a slice of the operation, passing the breach along like a relay baton.

It’s a concerning trend — one that we believe calls for [rethinking traditional threat modeling](https://blog.talosintelligence.com/compartmentalized-threat-modeling/). But one thing stood out to me while reading: cybercriminals are often terrible at teamwork.

What if the ransomware affiliate is waiting on credentials that never arrive? The access broker sells a foothold, but the tooling meant to exploit it isn’t ready, doesn’t work in the target environment or never shows up at all?

Ghosting isn’t limited to dating apps or job interviews (and if you’ve been through six interview rounds and still heard nothing, I see you). Cybercriminals flake too — whether it’s bad timing, better targets, internal drama… or maybe they just went to get a haircut (an [actual complaint](https://www.wired.com/story/conti-leaks-ransomware-work-life) that a Conti member made about a fellow actor not showing up).

In this compartmentalized model, the threat chain becomes a fragile supply line, stitched together in real time. Efficient, yes — but brittle. If one actor drops out, the whole operation can unravel. And let’s not pretend there’s honour among cybercriminals. They're opportunists. What’s to stop a broker from selling the same credentials to multiple buyers? Or backing out entirely if a better offer lands?

Of course, this ecosystem isn’t monolithic. Some groups run like structured businesses — access brokers, malware builders, “customer” (aka victim) services, the works. Others are looser, relying on whoever turns up in their DMs with access for sale. It’s the latter where ghosting seems more likely. In organised crews, a flaky broker risks reputational damage. In the freelance underworld, it’s just Tuesday.

Oof, I didn’t mean to knock freelancers there. Just, you know, *those* ones…

History suggests fallouts are inevitable. Conti's collapse, as [Wired](https://www.wired.com/story/conti-leaks-ransomware-work-life)reported, started with a single angry post and spiraled into a full on leak about poor performance records:

> *“I have 100 people here, half of them, even 10 percent, do not do what they need.”*

> *- Stern (or Demon), former Conti CEO*

LAPSUS$ imploded under its own infighting. One REvil affiliate even ranted on a cybercrime forum like a scammed eBay buyer.

To twist a familiar phrase: compartmentalized threats are only as strong as their weakest link. What if that link has poor communication skills, no follow-through and a serious case of commitment issues?

## The one big thing

In Talos’ [most recent blog post](https://blog.talosintelligence.com/uat-6382-exploits-cityworks-vulnerability), we shared that UAT-6382, Chinese-speaking threat actors, have exploited Cityworks, a widely-used asset management system, through a remote code execution vulnerability (CVE-2025-0994). The actors are deploying advanced malware for long-term persistence and control.

### Why do I care?

UAT-6382 is not only exploiting this vulnerability, but they're also employing sophisticated tools like web shells, Rust-based malware loaders, and frameworks like Cobalt Strike to burrow deep into systems. This could lead to data breaches and operational downtime.

### So now what?

While the intrusions we mentioned in the blog have been contained, exploitation may be continuing in the wild. Use the indicators of compromise (IOCs) listed in the blog to scan your environment.

## Top security headlines of the week

**NATO-Flagged Vulnerability Tops Latest VMware Security Patch Batch**
VMware patches flaws that expose users to data leakage, command execution and denial-of-service attacks. No temporary workarounds available.  ([SecurityWeek](https://www.securityweek.com/nato-flagged-vulnerability-tops-latest-vmware-security-patch-batch/))

**NIST's 'LEV' Equation to Determine Likelihood a Bug Was Exploited**
The new equation, introduced by the National Institute of Standards and Technology (NIST), aims to offer a mathematical likelihood index that could be a game-changer for SecOps teams and vulnerability patch prioritization. ([Dark Reading](https://www.darkreading.com/vulnerabilities-threats/nist-lev-equation-determine-likelihood-bug-exploited))

**Kettering Health hit by system-wide outage after ransomware attack**
Kettering Health, a healthcare network that operates 14 medical centers in Ohio, was forced to cancel inpatient and outpatient procedures following a cyberattack that caused a system-wide technology outage. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/kettering-health-hit-by-system-wide-outage-after-ransomware-attack/))

## Can’t get enough Talos?

* [Duping Cloud Functions: An emerging serverless attack vector](https://blog.talosintelligence.com/duping-cloud-functions-an-emerging-serverless-attack-vector/)
* Talos Takes: [Inside the Kill Chain: Compartmentalized Threat Modeling Explained](https://www.buzzsprout.com/2018149/episodes/17204075)

## Upcoming events where you can find Talos

* [BotConf](https://www.botconf.eu/) (May 20 – 23) Angers, France
* [Cisco Live U.S.](https://www.ciscolive.com/global.html) (June 8 – 12) San Diego, CA
* [NIRMA](https://nirma.org/annual-symposium/) (July 28 – 30) St. Augustine, FL
* [Black Hat USA](https://www.blackhat.com/us-25/) (A...