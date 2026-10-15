---
title: The Threat Hunting Flywheel: Why Threat Hunting Isn’t About Finding Bad Things
url: https://www.blackhillsinfosec.com/threat-hunting-fly-wheel/
source: Black Hills Information Security
date: 2026-10-14
fetch_date: 2026-10-15T06:44:00.960425
---

# The Threat Hunting Flywheel: Why Threat Hunting Isn’t About Finding Bad Things

[Skip to main content](#main-content)

[![BHIS](/uploads/media/bhis-text-bhis-f909d4808e69428ba2547d42a650842f.png)![BHIS](/uploads/media/bhis-text-bhis-light-f0fc7d40d92b4eccb72ef18ffe68bef6.png)](/)

Services

[All Services](/services/ "All Services")

[Penetration Testing](/services/traditional-penetrating-testing/ "Penetration Testing")

[Continuous Penetration Testing](/services/antisoc/ "Continuous Penetration Testing")

[Web Application Testing](/services/web-appllication-testing/ "Web Application Testing")

[ActiveSOC](https://activesoc.blackhillsinfosec.com/ "ActiveSOC")

[Fusion PenTest](/fusion-penetration-testing/ "Fusion PenTest")

[AI Security Assessments](/services/ai-security-assessments/ "AI Security Assessments")

[Incident Response](/services/incident-response/ "Incident Response")

[Blue Team Services](/services/blue-team-services/ "Blue Team Services")

[Blockchain Security](/services/blockchain-security/ "Blockchain Security")

[High-Profile Risk Assessments](/services/high-profile-risk-assessments/ "High-Profile Risk Assessments")

[Complete Service Guide](/services/complete-service-guide/ "Complete Service Guide")

[Governance, Risk and Compliance](/grc/ "Governance, Risk and Compliance")

[Contact Us](/contact-us/ "Contact Us")

About Us

[BHIS Tribe of Companies](/bhis-tribe-of-companies/ "BHIS Tribe of Companies")

[Admin Staff](/about/admin-staff/ "Admin Staff")

[Security Consultants](/about/security-consultants/ "Security Consultants")

[BHIS Privacy Policy](/bhis-online-privacy-policy/ "BHIS Privacy Policy")

Free Resources

[Blogs](/blog/ "Blogs")

[Webcasts](/webcasts/ "Webcasts")

[Free Cyber Security Tools](/free-cybersecurity-tools/ "Free Cyber Security Tools")

[Free Cybersecurity Webcasts](/free-cybersecurity-webcasts/ "Free Cybersecurity Webcasts")

[BHIS Podcasts](/bhis-podcasts/ "BHIS Podcasts")

[RITA](/rita/ "RITA")

Training

[BHIS & Antisyphon Training](/bhis-and-antisyphon-training/ "BHIS & Antisyphon Training")

[Wild West Hackin' Fest](/wild-west-hackin-fest/ "Wild West Hackin' Fest")

Community

[Connect](/community/ "Connect")

[Discord](https://discord.gg/BHIS "Discord")

[LinkedIn](https://www.linkedin.com/company/black-hills-information-security/ "LinkedIn")

[YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos "YouTube")

[Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social "Bluesky")

[Twitter/X](https://twitter.com/BHinfoSecurity "Twitter/X")

[Upcoming Events](/community/events/ "Upcoming Events")

Fun Stuff

[Backdoors and Breaches](/tools/backdoorsandbreaches/ "Backdoors and Breaches")

[Free Lab Fridays](/free-lab-fridays/ "Free Lab Fridays")

[Merch, Zines & More](/spearphish-general-store/ "Merch, Zines & More")

[PROMPT# Zine](/prompt-zine/ "PROMPT# Zine")

[REKCAH](/rekcah/ "REKCAH")

[Books](/tools/books/ "Books")

[Game of Life](/game-of-life/ "Game of Life")

1. [Home](/)
2. [Blog](/blog)
3. The Threat Hunting Flywheel: Why Threat Hunting Isn’t About Finding Bad Things

![Faan Rossouw](/uploads/media/img-5129-1-360x360-826439fa6cd94404bee8cab2968983a4.webp)

[Faan Rossouw](/blog?author=Faan%20Rossouw "See all posts by Faan Rossouw")Guest Author

![](/uploads/media/why-threat-hunting-isnt-about-finding-bad-things-1-c730fb68c93a4c8c8478f470c63861f2.png)

|  |
| --- |
| *This article was originally published in the InfoSec Survival Guide: Teal Book — Threat Hunting. Read it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/), or grab it on the [Spearphish General Store](https://spearphish-general-store.myshopify.com/collections/infosec-survival-guides) (free digital download or a $1.25 physical copy, your call).* |

Here’s a counterintuitive truth: the ultimate goal of threat hunting isn’t to find more security incidents—it’s to drive continuous improvement across your entire security program. We’re not hunting merely to find present bad; we’re hunting to decrease the probability of future bad.

Think of it like debugging. You don’t debug just to find bugs—you debug to build better software. Each bug you find teaches you something about your system, improves your testing, and makes future bugs less likely. Threat hunting works the same way.

### The Cyclical Nature of Threat Hunting

Every threat hunting framework can be thought of as a cycle that improves with every revolution.

## Step 1: Determine Your Focus

The biggest challenge in threat hunting? Answering this question: “Where do we even start?” You can’t just randomly poke around in logs hoping to find something interesting. You need a method to focus your efforts.

The good news is that there are several effective approaches, and you don’t have to pick just one. In fact, most mature programs blend approaches over time.

**Hypothesis-driven hunting** starts with an educated guess, perhaps informed by the latest threat intelligence. Maybe something like, “I bet adversaries are using scheduled tasks for persistence on our web servers.”

**Baseline hunting** flips the question entirely: instead of rooting around for specific threats, you map what “normal” looks like in your environment, then investigate anything that doesn’t fit the pattern.

**Statistical analysis tools** like RITA let you approach those patterns from yet another angle. They surface statistically weird behaviors and connections, giving you a prioritized list of anomalies to consider and maybe investigate.

**Machine learning models** can highlight specific events that deviate from learned baselines, essentially saying “start here” with confidence scores attached.

![](/uploads/content/7281e56d60d34bb0a6f80a4bea9f8fc0.png)

## Step 2: Investigation

The real detective work happens here. Investigation is iterative and rarely linear. You start broad, progressively narrow your focus by filtering out known-good activity, and follow interesting patterns wherever they lead. One scheduled task leads to a user account, which leads to authentication logs, which leads to source IPs, which leads to ... you get it.

The “art” is knowing which threads to pull and which to drop. Something can be technically anomalous but contextually benign, like a DBA running weird queries at 2 AM because production is on fire.

## Step 3: Discovery and Analysis

Eventually you reach a conclusion. Maybe you found a threat. Awesome! Now hand it to incident response.

But maybe, or most likely in fact, you found nothing…

Here’s the critical mindset shift: finding nothing isn’t failure. It’s validation—discovery of a different kind, even. A thorough hunt might confirm that your defenses are working and that an attack isn’t happening (win!). Or it might reveal that a detection you thought existed doesn’t, or that it’s misconfigured and wouldn’t fire even if the attack happened (also a win because now you know what to fix).

Approached with this mindset, any outcome is a win, and every hunt ultimately makes you more secure.

## Step 4: Knowledge Refinement and Improvement

This is where threat hunting transforms from investigation into force multiplication. Everything you’ve learned feeds back into your security program:

* Create detection rules so you don’t have to manually hunt for the same thing again.
* Document baselines about normal behavior in your environment.
* Share knowledge with your team and the wider community (Document!).
* Generate new hypotheses for the next hunt (Back to Step 1...).
* Close visibility gaps you discovered.
* Measure and communicate your program’s value.

This phase is what makes hunting a continuous improvement engine. Each excursion expands detection coverage, deepens environmental knowledge, sharpens hunting skills, and strengthens overall security posture.

### The Self-Improving Loop

The real power of this hunting “loop” is its cumulative nature. Your first few hunts might feel slow and uncertain. But knowledge accumulates. Patterns become obvious. Investigation approaches become routine. Organizations committed to...