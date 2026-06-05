---
title: Reporting from Vegas: Networking, AI, and good boys
url: https://blog.talosintelligence.com/reporting-from-vegas-networking-ai-and-good-boys/
source: Over Security
date: 2026-06-04
fetch_date: 2026-06-05T06:14:20.109951
---

# Reporting from Vegas: Networking, AI, and good boys

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

# Reporting from Vegas: Networking, AI, and good boys

By
[Joe Marshall](https://blog.talosintelligence.com/author/joe-marshall/)

Thursday, June 4, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s edition of the Threat Source newsletter.

Howdy friends, and hello from Cisco Live U.S., here in sunny (and very hot) Las Vegas!

An interesting quirk of being sent to one of these events is you learn to understand your limits as a person. Cisco Live is a three-day event, and it encompasses so many people, partners, workshops, CTFs (!!), and symposiums. I can confidently say that here on day three, I’ve had rarely a moment’s rest and, as they say, my dogs are barking.

Speaking of dogs, did you know that at Cisco Live we have therapy dogs? Healing Hounds is a local Las Vegas therapy dog volunteer group, and Splunk sponsored them this year. Every two hours, the goodest boys and girls rotate in and you can stop what you are doing to immediately go give them pets. Look at these cute faces. LOOK AT THEM.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/doggies.jpg)

Back to limits. One thing I’ve discovered is that conferences like this can be *loud*. I don’t mind loud. Loud is fine. But eight hours of noise at high levels is stressful. So, I use my Apple AirPods in noise cancelling mode, and it keeps even a massive conference like CLUS to a very manageable dull roar. If you own a pair, or any earplugs, trust me. Use them. It’s not going to shut out the world, but it will give you more stamina in an environment with bright lights and loud noises.

With that much stimuli for an extended period, you must create some space for yourself. Conferences that have quiet or chill spaces, shout out to you! A place for humans to find a moment of rest in the endurance contest that is a technology convention is a wonderful thing.

So what is the vibe at CLUS? AI. All the AI. Not from a product perspective, but from an infrastructure and security perspective. How do folks plan to move and manage that much data, especially in an agentic world? It’s a hot debate, given what I’ve listened to so far. Every business is struggling with it in their own ways, and conferences like CLUS are good opportunities to put those companies in the same room and ideate on ways to process and defend in an AI world. We’re talking many hundreds of zettabytes of data daily, the kind of data pipelines the entire world runs on. At that scale, the challenge is just wild and almost incomprehensible. I’m glad I could help and be a part of those discussions.

As the summer starts, the great patchening is coming as vendors start issuing rapid patches and CVE advisories. This is the quiet before the storm, so enjoy these cute dog photos! Black Hat and DEF CON are around the corner, as well! And always find time during these fire drills to take care of yourself, and if you can, pet some dogs.

## The one big thing

Cisco Talos is [expanding our Threat Hunting program](https://blog.talosintelligence.com/hypotheses-telemetry-and-human-judgment-inside-cisco-talos-threat-hunting) to proactively track down advanced adversaries who deliberately slip past traditional detection thresholds. By combining AI-driven telemetry analysis with human expert validation, we continuously hunt for hidden threats across endpoint, network, and identity data. This hypothesis-driven approach allows us to identify complex intrusions — like a recent KongTuke command-and-control (C2) discovery — before a formal detection signature even exists.

### Why do I care?

Most security tools operate on a simple principle: If a known-bad pattern appears, fire an alert. But as threat actors increasingly leverage AI to move faster and intentionally stay under the radar, relying solely on automated alerts leaves massive blind spots. Hypothesis-driven hunting addresses this gap by correlating weak signals across an environment, allowing defenders to piece together ambiguous anomalies and uncover sophisticated intrusions that would otherwise go unnoticed.

### So now what?

If your team lacks the dedicated headcount for continuous hunting, Cisco Talos Threat Hunting can bridge the gap. Reach out to your Cisco account team, explore our new dedicated portal in Cisco Security Cloud Control, and [read the full blog](https://blog.talosintelligence.com/hypotheses-telemetry-and-human-judgment-inside-cisco-talos-threat-hunting) for a detailed breakdown of our recent KongTuke C2 investigation.

## Top security headlines of the week

**Global stock exchange hit by monthslong email campaign**
A threat actor got a near-continuous view into an influential finance executive's email inbox, thanks to clever use of legitimate, native Windows tools. ([Dark Reading](https://www.darkreading.com/cyberattacks-data-breaches/global-stock-exchange-hit-monthslong-email-campaign))

**One-click GitHub dev attack lets attackers steal full GitHub OAuth tokens**
The vulnerability allows attackers to install malicious VS Code extensions that steal GitHub OAuth tokens when they are passed to GitHub.dev by exploiting a message-passing mechanism between the main VS Code window and webviews. ([The Hacker News](https://thehackernews.com/2026/06/one-click-github-dev-attack-lets.html))

**FBI-flagged phishing kit “Kali365” expands its reach**
Once targeting just Microsoft 365, the phishing-as-a-service platform now aims at AWS, Okta, and Russian platforms, while relying on device code phishing. ([Dark Reading](https://www.darkreading.com/cyber-risk/fbi-flagged-phishing-kit-kali365-expands-its-reach))

**Dozens of Red Hat packages backdoored through its official NPM channel**
Official Red Hat NPM accounts have been compromised and used to push a mali...