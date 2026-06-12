---
title: A tale of two eras
url: https://blog.talosintelligence.com/a-tale-of-two-eras/
source: Over Security
date: 2026-06-11
fetch_date: 2026-06-12T06:27:33.470686
---

# A tale of two eras

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

# A tale of two eras

By
[Amy Ciminnisi](https://blog.talosintelligence.com/author/amy-ciminnisi/)

Thursday, June 11, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

To the surprise of absolutely no one who has seen my face, I’m one of the younger employees at Talos. As my industry veteran colleagues were buying the first iPods, navigating the switch from dial-up to broadband, saying goodbye to floppy disks, and making Myspace accounts, I was playing with my [Password Journal and Friend Chips](https://www.youtube.com/watch?v=qMpGEokqOVs). It’s a funny contrast, but I still experienced the beginning of the “always-on” era.

Ah, those were the days. One of my most vivid tech memories is begging my dad to play games on his [Handspring Visor](https://www.youtube.com/watch?v=7L8l44HI5YY) — a classic personal digital assistant (PDA) launched in late 1999 by Handspring, a company formed by the original creators of the PalmPilot. Handspring stopped producing the Visor line in 2002 and it eventually became obsolete, mostly because its desktop sync feature couldn't keep up with modern OS updates. Despite the tech debt, I spent hours playing Asteroid, Centipede, and Hardball (aka Breakout) on that thing. My dad, meanwhile, mostly used the Memo function to store his passwords... which he still does today. (Yeah, I’m still working on getting him to see the wonders of 1Password.)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/Untitled-1.png)

You might be wondering what made me reminisce on childhood toys. A few weeks back, my fiancée and I drove a few hours to visit my family. Even if we get in at 9:00 p.m., it’s tradition for us to stay up late eating pizza and talking about random stuff.

We got on the topic of phones because my parents still have a landline, and I mentioned that walkie talkies were my first introduction to having my own personal device. My dad dug some old ones out, set them on the table, and put them on scan while we chatted.

At some point, the conversation petered out just when the walkie talkie captured a channel. Radio static, and then a kid’s voice broke our silence: “Your butt crack is out.”

My dad got an impish grin and brought the talkie up to his mouth. My mom pleaded, “No. Honey, no. Don’t.” The rest of us were already wheezing and crying.

He pressed the talk button and, in his best crotchety old man voice, bellowed, “Hey, you kids. Get off my lawn!”

Imagine being those poor kids. It’s a funny story, but if you don’t want people like my dad intercepting your comms, maybe stick to encrypted channels.

## The one big thing

Talos' Yuri Kramarz [published a blog](https://blogs.cisco.com/security/security-in-the-post-mythos-era) highlighting how AI-driven vulnerability discovery has completely outpaced human patching capabilities. With frontier AI models autonomously discovering and exploiting zero-days in minutes, the traditional vulnerability lifecycle has completely collapsed. To survive this hyper-accelerated threat environment, organizations must abandon patch-reliant strategies and embrace a three-stage fallback model built on foundational security principles.

### Why do I care?

Speed is the new, terrifying multiplier in the traditional risk equation. When an AI can uncover a decades-old zero-day and write an exploit for it in minutes, relying solely on vulnerability management is a losing game. Defenders must accept that some exploitation will inevitably slip through the cracks. The true measure of security is no longer just prevention, but how well your environment can absorb, detect, and survive the initial blow.

### So now what?

Stop treating security basics like optional compliance checkboxes. Enforce multi-factor authentication (MFA) everywhere, harden devices using CIS benchmarks, and implement strict network segmentation to limit an attacker's blast radius. Since hardened systems only slow attackers down, deploy behavioral-based EDR, NDR, and XDR to catch the post-exploitation activity that signatures miss. Finally, validate these controls through penetration testing and purple team exercises so your incident response playbooks become muscle memory, not just wishful thinking. [Read the full blog for more.](https://blogs.cisco.com/security/security-in-the-post-mythos-era)

## Top security headlines of the week

**CISA gives U.S. federal agencies three days to fix a VPN bug under attack by** **Qilin**
Check Point Software said the bug affects several of its remote access tools, firewalls, and VPNs, which act as digital gatekeepers to protect company networks from unauthorized access. ([TechCrunch](https://techcrunch.com/2026/06/09/cisa-gives-us-federal-agencies-three-days-to-fix-a-vpn-bug-under-attack-by-a-ransomware-gang/))

**Anthropic launches Claude Fable 5: Mythos-class AI with cybersecurity guardrails**
The AI giant says this marks the first time a model of this capability class has been deemed safe enough for widespread public and developer access. ([SecurityWeek](https://www.securityweek.com/anthropic-launches-claude-fable-5-mythos-class-ai-with-cybersecurity-guardrails/))

**Microsoft fixes** **two** **high-severity zero-days disclosed by researcher**
The vulnerability is a local privilege escalation, meaning it can be chained to a separate vulnerability to give users or processes with low-level privileges the ability to defeat OS protections and gain full SYSTEM rights needed to install malware. ([Ars Technica](https://arstechnica.com/security/2026/06/locked-in-heated-rivalry-with-researcher-microsoft-fixes-0-day-they-disclosed/))

**WhatsApp catches spyware firm NSO defying no-hacking court order**
According to WhatsApp, the...