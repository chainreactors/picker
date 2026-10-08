---
title: One breach, please, and make no mistakes
url: https://blog.talosintelligence.com/one-breach-please-and-make-no-mistakes/
source: Over Security
date: 2026-10-07
fetch_date: 2026-10-08T08:08:14.237419
---

# One breach, please, and make no mistakes

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/OneBreachPlease-BlogHeader.jpg)

# One breach, please, and make no mistakes

By
[Jerzy ‘Yuri’ Kramarz](https://blog.talosintelligence.com/author/jerzy/)

Wednesday, October 7, 2026 06:00

[On The Radar](/category/on-the-radar/)

For some time now, the cybersecurity community has seen examples of autonomous agents, built inside AI labs, attacking public infrastructure (to name a few, [Hugging Face](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), [DSEWiki](https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/), and [RubyGems](https://www.reuters.com/legal/litigation/openai-agents-attacked-software-service-rubygems-before-hugging-face-incident-2026-09-11/)). Of course, frontier labs have built-in security to prevent these attacks from occurring, but every now and then, the training or prompting appears to be [insufficient](https://collusion.wiki/) — especially when the agents themselves attempt to use logic to probe and bypass the restrictions placed on them. The question that matters is not whether AI attacks are coming, because the age of AI agents executing cyber attacks is already here. The question is what to do about it and how to harden the stack against a swarm of agents who will relentlessly lie, deceive, and probe until the objective is met.

Imagine your organization is a target for a creative human-driven AI adversary whose many agentic friends like to discuss and brainstorm different attack techniques. The limit here is the group’s own imagination, tools, prompts, and skills. However, there is a difference between the human 1) prompting the group (or an AI agent) to “break into an organization,” and 2) preparing it with information — a detailed tool mapping, markup files with instructions for agents, offensive security prompts, agents.md with guidance, and specific skills that would be invoked in different situations to guide agents into how to interpret an output of tools or access gained. The swarm of AI agents might fabricate employee identities and social profiles, contact the HR team with a plausible onboarding request, walk in by exploiting an unpatched vulnerability, or simply mail out phishing invoices at volume. The sky is the [limit here](https://blog.talosintelligence.com/keep-going-bro-youve-got-this-a-data-driven-look-at-how-adversaries-are-weaponizing-ai/).

These types of attacks can be executed all at once, with agents comparing notes and adapting in near real time to challenges (and your environment). What used to take a red team months of dedicated work, scoping, building and hiding infrastructure, and running the campaign now compresses into hours for a swarm of communicating agents that do not tire, lose focus, or need weekends, and can stand up infrastructure quickly.

## Penetration test today, red team tomorrow

I would argue that most of the public “attacks” seen so far more closely resemble a [penetration](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html) test (pentest) than a true red team operation. They are loud, visible, lean on volume, and appear to use off-the-shelf tooling with thousands of agents working together. [RubyGems](https://www.reuters.com/legal/litigation/openai-agents-attacked-software-service-rubygems-before-hugging-face-incident-2026-09-11/) is the clear example of a loud attack. The registration was hammered, packages stuffed, spam everywhere, and maintainers alerted within days — not exactly a stealth attack.

In red team operations, operational security (OPSEC) is the name of the game. It is the difference between getting in and getting caught by a capable Security Operations Center (SOC) team. Real red teaming means maintaining stealth and a low signal while gaining footholds and persistence that survive normal monitoring.

Volume is a property of this generation of AI agents, not a law of nature. The moment agent swarms are trained or prompted to prioritize staying hidden over moving fast, the noise drops and the pentest flavor turns into a genuine red team with machine endurance behind it. The plan of defense needs to assume that while we will probably see loud attacks now, the noise will start going down over time.

## How to build resilience

1. **Have an** [**incident response plan**](https://blog.talosintelligence.com/the-features-of-incident-response-plan/) **(IRP) and rehearse it.** A plan that lives in a drawer that hasn’t been opened for few years will probably not work when it’s needed. You’ll need named owners and decision authorities, specified out-of-band communications for when your primary channels are under attack, and a clear line to legal and to law enforcement. Map the IRP to a recognized incident lifecycle so nothing gets improvised under pressure. Preparation, detection and analysis, containment, eradication, recovery, and a post-incident review is what makes difference between a plan that *might* work and the one that *will* work.
2. **Test your own infrastructure and know its footprint.** Where do your systems reach out to, and what can reach in? Map the full context of every attack path from start to end. For example, going to an external switch, then front-end server, then application, then database, then Active Directory, then user accounts, then customer data is a perfectly [valid attack path](https://blog.talosintelligence.com/arcanedoor-new-espionage-focused-campaign-found-targeting-perimeter-network-devices/) that somebody could try to explore to get into the environment. An attacker's footprint expands naturally as they traverse, so an assumed-breach exercise (start from "they already have a foothold, now what?") tells you far more than a scan ...