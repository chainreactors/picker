---
title: One newsletter to rule them all
url: https://blog.talosintelligence.com/one-newsletter-to-rule-them-all/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-11
fetch_date: 2025-12-12T03:22:39.870913
---

# One newsletter to rule them all

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

# One newsletter to rule them all

By
[Hazel Burton](https://blog.talosintelligence.com/author/hazel-burton/)

Thursday, December 11, 2025 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

*“It’s a dangerous business, going out your door. You step onto the road, and if you don’t keep your feet, there’s no knowing where you might be swept off to.” — Bilbo Baggins*

It’s almost the end of the year, which feels like the perfect time to start an epic quest.

So, Middle-earth. I’m walking across it. Not with the intention of destroying the One Ring, but to increase my daily step count in the nerdiest way possible.

As I suspect is the origin story for most quests these days, my journey began by downloading an app.

![](https://blog.talosintelligence.com/content/images/2025/12/threatsource_2.png)

It’s called “The Conqueror.” There are many different distances you can choose from, but I chose Middle-earth because I’m that person who watched all the behind-the-scenes footage from Peter Jackson’s *Lord of the Rings* extended edition box set and physically shed tears because I wasn’t there.

Heeding Bilbo’s warnings about roads, I’m using a treadmill. After receiving my official race bib (#199574), I hopped on and muttered under my breath, “So it begins.”

So far, I’ve passed Bag End, South Farthing, Woody End, Maggot’s Farm, and I’m currently doing a stopover at Buckleberry Ferry. That’s 130km (55% of the Shire) done. Only 120km until Bree, where I can rest up with a pint at The Prancing Pony. And a mere 2,787km to go until I get to Mount Doom. If only Frodo hadn’t taken so many detours…

I’ve been rewarded at each milestone with postcards full of extremely nerdy facts about the landscape. And because of The Conqueror’s partnership with an ocean clean-up charity, I’ve also “saved” 20 plastic bottles from entering the sea, which feels very cool to have accomplished while never leaving the house.

![](https://blog.talosintelligence.com/content/images/2025/12/threatsource_1.png)

It’s a strange, delightful journey: half fitness plan, half fantasy pilgrimage. And it got me thinking about the value of knowing your destination.

Oftentimes when I’m speaking to defenders, one of their main challenges is “I’m struggling to do all the things, all the time.” When everything gets a bit overwhelming, and threats either shift unpredictably or circle back to tactics we thought we’d left behind, it’s easy to lose your sense of direction and say, “What are we doing this for again?”

That’s what I’ve come to like about this quest across Middle-earth: there’s a destination, and there are milestones. Mount Doom is a f\*\*\*\*\*g long way from Buckleberry Ferry. But I like just knowing the next marker even if I can’t yet see the (Bag)end.

As you’re making plans for next year, it might be worth using that idea: Where are you heading? What are the things you’re doing right now are actually helping you get there? Which detours/madness will lead you into Fangorn Forest?

If in doubt, follow your nose.

## The one big thing

While tracking ransomware activities, Cisco Talos [uncovered new tactics, techniques, and procedures](https://blog.talosintelligence.com/byovd-loader-deadlock-ransomware/) (TTPs) linked to a financially motivated threat actor targeting victims with DeadLock ransomware. The DeadLock ransomware targets Windows machines with a custom stream cipher encryption algorithm that uses time-based cryptographic keys to encrypt files.

### Why do I care?

There’s a few things that the threat actor does as part of this campaign to make recovery for victims more complicated. First, they use the Bring Your Own Vulnerable Driver (BYOVD) technique with a previously unknown loader to exploit the Baidu Antivirus driver vulnerability ([CVE-2024-51324](https://nvd.nist.gov/vuln/detail/CVE-2024-51324)), enabling the termination of endpoint detection and response (EDR) processes. Also, the custom encryption method allows DeadLock ransomware to effectively encrypt different file types in enterprise environments while preventing system corruption through selective targeting and anti-forensics techniques.

### So now what?

The Talos blog has a [full breakdown](https://blog.talosintelligence.com/byovd-loader-deadlock-ransomware/) of the attack, including the new TTPs, attempts at lateral movement, the ways the actor attempts to impair defenses, and the encryption process. Snort SIDs for the threats are: 65576, 65575 and 301358. ClamAV detections are also available for this threat:

* Win.Tool.EDRKiller-10058432-0
* Win.Tool.VulnBaiduDriver-10058431-1
* Ps.Tool.DeleteShadowCopies-10058429-0
* Win.Ransomware.Deadlock-10058428-0

## Top security headlines of the week

**Chinese hackers are using “stealthy and resilient” Brickstorm malware to target VMware servers**
The Cybersecurity and Infrastructure Security Agency (CISA) is warning that China-sponsored threat actors are using Brickstorm malware to achieve long-term persistence in critical infrastructure networks. [(ITPro)](https://www.itpro.com/security/malware/chinese-hackers-are-using-stealthy-and-resilient-brickstorm-malware-to-target-vmware-servers-and-hide-in-networks-for-months-at-a-time)

**Critical Apache Tika vulnerability leads to XXE injection**
A critical-severity vulnerability in the Apache Tika open source analysis toolkit could allow attackers to perform XML External Entity (XXE) injection attacks. [(Security Week)](https://www.securityweek.com/critical-apache-tika-vulnerability-leads-to-xxe-injection/)

**Zero-click agentic browser attack can delete entire Google Drive using crafted emails**
A new agentic browser attack targeting Perplexity's Comet browser that's capable of turning a seemingly inn...