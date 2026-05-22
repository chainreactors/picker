---
title: The art of being ungovernable
url: https://blog.talosintelligence.com/the-art-of-being-ungovernable/
source: Over Security
date: 2026-05-21
fetch_date: 2026-05-22T06:08:10.803007
---

# The art of being ungovernable

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

# The art of being ungovernable

By
[William Largent](https://blog.talosintelligence.com/author/william-largent/)

Thursday, May 21, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

*“It takes very little to govern good people. Very little. And bad people can’t be governed at all. Or if they could, I never heard of it.” ― Cormac McCarthy, No Country for Old Men*

Most of my career has been built on dichotomy: striving to be a supportive teammate while also pushing every boundary in front of me. I've often been told to “never do X, only do Y,” but I’ve invariably chosen to do X anyway (even when fraught with peril) to get to the deeper answer. For years, I was told that I should perform in certain ways — instead of in ways that made sense for my brain and way of learning.

I wasn’t governable, but I wasn’t bad. Just ... challenging. While Sheriff Ed Tom Bell’s view of good vs. bad is compelling, maybe our careers should be defined as “acquiescent” vs. “challenging.” It’s less of an existential crisis that way.

Over the past few years, I’ve been enjoying the mentoring aspect of my career. One of the things that I love to share with people is that being ungovernable is very challenging early in career; it’snot a favorite of middle management, but it can take you to places that you really want to be (i.e., Talos). The road is going to be longer and much bumpier than your governable cohort, but this is the long con.

The path to Talos was long and arduous, but I've learned to make my career choices through the lens of the axiom, “If you’re the smartest person in the room, you’re in the wrong room.” It's been the only guidepost I’ve needed. I don’t know that it applies to everyone, because everyone is unique, but it absolutely helps me decide what I want to learn, what I want to dive into, who I want to surround myself with.

The secret lies in the last comment — it's the people. If you continue to search for the smartest people in the room, you’ll find it and when you do, you’ll find that you aren’t ungovernable — rather, you’re understood. Be ungovernable (but kind) in the short term, find new ways to solve problems, think around solutions in new ways, program in different languages, and be the person in the meeting that says, “I think we should do Y instead, and here’s why.”

I suspect that this is the same approach many of you already take in your daily roles when identifying threats vs. benign activity, choosing your pivots in hunting, or deciding the priorities in device replacement. It’s a natural direction for the intellectually curious, so be kind, but ungovernable.

*“The future of intelligence must be about search, while the future of ignorance must be about the inability to evaluate information.” ― Patricia Lockwood, No One Is Talking About This*

## The one big thing

Cisco Talos has recently discovered a [commodity BadIIS malware variant](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/) fueling a thriving malware-as-a-service (MaaS) ecosystem for Chinese-speaking cybercrime groups. Identifiable by its embedded "demo.pdb" strings, this toolset boasts a multi-year development cycle complete with builder tools and persistence mechanisms. Threat actors are leveraging this robust framework to easily execute malicious search engine optimization (SEO) fraud, hijack server content, and redirect traffic to illicit sites.

### Why do I care?

This is a highly active, commercially driven malware ecosystem. The author constantly pushes rapid updates to introduce new features and actively evade specific security vendors, making it a persistent headache for defenders. Because this BadIISvariant is sold as a commodity tool, it lowers the barrier to entry for cybercriminals, leading to widespread attacks that silently hijack server traffic without triggering obvious alarms.

### So now what?

Defenders should actively monitor IIS environments for unauthorized traffic redirection, unexpected reverse proxying, or sudden spikes in "503 Service Unavailable" errors. Threat hunting efforts should also target the distinct "demo.pdb" strings and associated Chinese-language folder paths within IIS binaries. Ensure your endpoint detection solutions are updated to catch these reactive evasion tactics, and [read the full blog](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/) for complete coverage and indicators of compromise (IOCs).

## Top security headlines of the week

**CISA exposes secrets, credentials in “private” repo**
A researcher discovered a public GitHub repository belonging to CISA that contained 844MB of sensitive data, including plain-text passwords, authentication tokens, and other secrets. ([Dark Reading](https://www.darkreading.com/cybersecurity-operations/cisa-exposes-secrets-credentials-private-repo))

**NYC Health + Hospitals says hackers stole medical data and fingerprints, affecting at least** **1.8 million people**
The breach is particularly sensitive because hackers stole biometric information, including fingerprints and palm prints, which affected individuals have for life and cannot replace. ([TechCrunch](https://techcrunch.com/2026/05/18/nyc-health-and-hospitals-says-hackers-stole-medical-data-and-fingerprints-during-breach-affecting-at-least-1-8-million-people/?utm_source=tldrinfosec))

**Bug bounty businesses bombarded with AI slop**
Companies that pay hackers to find flaws in their software are being inundated with low-quality (often false) reports generated by AI, forcing some to suspend the programs altogether. ([Ars Technica](https://arstechnica.com/ai/2026/05/bug-bounty-businesses-bombarded-with-ai-slop/...