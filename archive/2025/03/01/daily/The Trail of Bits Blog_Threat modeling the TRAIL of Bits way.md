---
title: Threat modeling the TRAIL of Bits way
url: https://blog.trailofbits.com/2025/02/28/threat-modeling-the-trail-of-bits-way/
source: The Trail of Bits Blog
date: 2025-03-01
fetch_date: 2025-10-06T21:58:19.447119
---

# Threat modeling the TRAIL of Bits way

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Threat modeling the TRAIL of Bits way

Kelly Kaoudis

February 28, 2025

[threat modeling](/categories/threat-modeling/), [application security](/categories/application-security/)

Page content

* [What TRAIL is](#what-trail-is)
* [Why a TRAIL threat model provides value](#why-a-trail-threat-model-provides-value)
* [How TRAIL works](#how-trail-works)
  + [Model building](#model-building)
  + [Threat scenarios](#threat-scenarios)
  + [Findings and follow-on work](#findings-and-follow-on-work)
* [Applying the results](#applying-the-results)
  + [Informing further security reviews](#informing-further-security-reviews)
  + [Remediation](#remediation)
  + [Updating your threat model](#updating-your-threat-model)
* [I like how a TRAIL threat model sounds. How do I get one?](#i-like-how-a-trail-threat-model-sounds-how-do-i-get-one)

Our threat modeling process is a little bit different. Over time, multiple application security experts have refined this process to provide maximal value for our clients and to minimize the effort required to update the threat model as the system changes.

We call our process **TRAIL**, which stands for **T**hreat and **R**isk **A**nalysis **I**nformed **L**ifecycle. TRAIL enables us to trace and document the impact of flawed trust assumptions and insecure design decisions through our clients’ architectures and the systems and processes that support them. Mitigating system-level findings like these squashes whole classes of vulnerabilities, which means fewer one-off bug reports and fixes to worry about.

## What TRAIL is

We’ve all used a variety of threat modeling methodologies over the years; each has its strong suit, but none perfectly fit our clients’ needs, so we combined the best parts of what we knew and iterated to build our own process. TRAIL initially extended Mozilla’s single-component [Rapid Risk Assessment](https://infosec.mozilla.org/guidelines/risk/rapid_risk_assessment.html) (RRA) process to whole systems (large and small), incorporating parts of the [NIST SP 800-154](https://csrc.nist.gov/files/pubs/sp/800/154/ipd/docs/sp800_154_draft.pdf) Guide to Data-Centric Threat Modeling and the [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) security and privacy controls dictionary.

While RRA’s data dictionary inspired our approach, TRAIL enables us to model all in-scope parts of the system and their relationships with more rigor. When following TRAIL, we systematically cover each connection between components. We don’t just uncover direct threats to the data that each component handles, but also emergent weaknesses that arise from improper interaction between components, and other architectural and design-level risks.

Security patching can easily become a cycle of receiving a security report, making a one-off fix, and then getting yet another ticket that documents yet another instance of exactly the same problem. Structured threat modeling breaks this cycle of treating the symptoms over and over. A proper threat model exposes design-level weaknesses (of which individual vulnerabilities are symptoms) so they can be remediated.

## Why a TRAIL threat model provides value

TRAIL has three goals:

1. Document the current system’s architecture-level and operational risks;
2. For each risk, provide our client with both practical, short-term mitigation options and long-term strategic recommendations;
3. Enable our client to update the threat model themselves[1](#fn:1) as they mitigate risks, and the system otherwise changes over time.

Throughout the software/systems development life cycle ([SDLC](https://en.wikipedia.org/wiki/Systems_development_life_cycle))[2](#fn:2), application security review results in a better product. The [design phase](https://blog.trailofbits.com/2025/02/25/how-threat-modeling-could-have-prevented-the-1.5b-bybit-hack/#:~:text=Performing%20a%20threat%20model%20during%20the%20design%20phase%20of%20the%20software%20development%20lifecycle%20(SDLC)%20may%20have%20informed%20Bybit%20that%20their%20system%20contains%20the%20following%20control%20failures) of the SDLC is an ideal time for collaborative[3](#fn:3) threat modeling exercises involving both security engineers and the people building the system: there aren’t yet users relying on particular system features, but requirements are mostly set in stone, so it’s easier to make design improvements. But the second-best time to plant a tree is, naturally, now. Threat modeling work provides value in every SDLC phase since it improves developers’ understanding of the consequences of design choices.

## How TRAIL works

### Model building

TRAIL’s foundation is in first building as accurate a model as possible. We work with our client to identify all in-scope system components. Then, we’ll place a trust boundary anywhere that security controls[4](#fn:4) gate connections between components (or *should*, as per security requirements and design). We’ll group components that share trust boundaries into trust zones.

We’ll talk extensively with our client and read their system documentation to build knowledge of the system and its SDLC, uncovering and documenting previously unwritten assumptions. Then, we establish relevant combinations of connections and threat actors[5](#fn:5), especially for those connections that cross trust boundaries. We call these connection-actor combinations *threat actor paths*[6](#fn:6).

While our discussion of potential threats with the client throughout this process is relatively free-form, building threat actor paths ensures we stay rigorous and don’t miss a way that an attacker could maliciously escalate their privilege or cause data to move between components or out of the system.

### Threat scenarios

Our core model-building work allows us to identify design-level and operational risks that our client could have otherwise missed. We’ll document these risks in the form of threat scenarios. Each threat scenario describes a potential way that an adversary could exploit a single connection crossing a trust boundary between two components in the system. Putting threat scenarios together and doing further confirmation research enables us to write findings, but we’ll discuss findings later. For some threat modeling exercises, we will stop refining our system context at this point and will wrap up our work with summary-level remediation recommendations—we call this type of review a *lightweight* threat model.

#### What you get from a lightweight threat model

A lightweight threat modeling engagement results in an end-to-end, high-level overview of the risks inherent to a system’s design, illustrated with a handful of threat scenarios plus recommendations. Our clients typically use the results of lightweight threat models to guide further security review and remediation. Here are a few threat scenarios from the 2023 Trail of Bits [assessment](https://github.com/trailofbits/publications/blob/master/reviews/2023-12-pacman-securityreview.pdf) of the Arch Linux package manager, Pacman:

| **Scenario** | **Actor(s)** | **Component(s)** |
| --- | --- | --- |
| **An environment variable affects the Pacman package manager’s libcurl dependency.** For instance, Pacman redirects its HTTP connections through the proxy defined in the `http_proxy` environment variable. If an attacker injects an environment variable into Pacman’s runtime environment — a difficult prospect, given that it runs as root during installs — they could cause Pacman to exhibit exploitable or undesirable behavior. | * Local root | * Pacman package manager |
| **An attacker attempts a substitution attack, bumping versions on a popular package through a compromised local network repository or remote repository.** Pacman will always install the latest version of a package across all repositories it ...