---
title: Black Hat Talks I'm Excited to Attend This Year (Kymberlee's version)
url: https://shostack.org/blog/kymberlee-blackhat-hype/
source: Shostack & Friends Blog
date: 2026-07-23
fetch_date: 2026-07-24T05:04:44.899512
---

# Black Hat Talks I'm Excited to Attend This Year (Kymberlee's version)

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Speaking Requests](/speaking)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog)
3. Black Hat Talks I'm Excited to Attend This Year (Kymberlee's version)

Shostack + Friends Blog

# Black Hat Talks I'm Excited to Attend This Year (Kymberlee's version)

Kymberlee Price, Shostack + Associates COO (and Black Hat USA Content Review Board Member since 2016)

Kymberlee's list of must-see talks at Black Hat this year
![An image of the Black Hat logo](/images/blog/img/2026/BHUS26-800w.png)

Black Hat season is here, and this year's Briefings schedule has more than a few sessions I've put on my calendar. After two decades of vulnerability disclosure, threat modeling and secure-by-design work, I tend to gravitate toward the same handful of themes every year: how we actually build resilient security culture, where trust quietly breaks down in our supply chains, and what's really going on underneath the hood when we hand more autonomy to AI systems. This year's lineup delivers on all three. Here's what's on my list.

[Could a Pattern on Your Clothing Fool Facial Recognition?](https://blackhat.com/us-26/briefings/schedule/?track[]=human-factors#could-a-pattern-on-your-clothing-fool-facial-recognition-53532) - Bill Swearingen
:   Most adversarial-evasion research makes you choose between looking ridiculous (masks, IR LEDs) or swapping in someone else's face entirely. Bill's approach is neither: a genetic algorithm that breeds adversarial textile patterns, printed on ordinary fabric, that cause cascading failures across the full facial recognition pipeline (person detection, face detection, and identity match) with no electronics and nothing that reads as unusual to a person standing next to you. He's testing evolved patterns against the same model architectures (YOLOv8, RetinaFace, ArcFace) running inside Clearview AI, Axon body cameras, and Palantir systems, and he's closing the talk with a live demo on stage: printed pattern, camera, ten models failing in real time.

    What pulls me in isn't just the demo, it's the framing underneath it — that facial recognition isn't one system but a multi-stage pipeline, and each stage has its own architecture and its own distinct weaknesses. That's a vulnerability researcher's way of thinking about a problem, breaking a black box into its component failure points rather than treating it as monolithic. It's also a genuinely interesting privacy story: a practical, passive, human-invisible countermeasure to AI surveillance that exists today, not a hypothetical.

    (P.S. where do I get an adversarial scarf?)
    Thursday, August 6 | 11:05am-11:45am ( Oceanside B, Level 2 )

[You Can't Patch a Mental Model: How Agentic Systems Expose our Hidden Security Assumptions](https://blackhat.com/us-26/briefings/schedule/?track[]=human-factors#you-cant-patch-a-mental-model--how-agentic-systems-expose-our-hidden-security-assumptions-52854) - Ben Hanson
:   Ben's framing here is the kind of reframe I'm always chasing: agentic security isn't hard because it's new, it's hard because it violates assumptions our security models were built on in the first place. We keep trying to "secure agents" when what we actually need is to govern agency... and those are different problems. He's promising to walk through eight hidden assumptions baked into modern security architectures that only become visible once you're dealing with adaptive, goal-driven systems, plus a systems-based lens (control, decision-making, flow, feedback) for reasoning about agentic risk and building controls that address causes instead of just reacting to behavior.

    Thursday, August 6 | 11:05am-11:45am ( Mandalay Bay H, Level 2 )

[Running Untrusted Code: An Empirical Study of Developer Compromise and Its Blast Radius](https://blackhat.com/us-26/briefings/schedule/index.html#running-untrusted-code-an-empirical-study-of-developer-compromise-and-its-blast-radius-53784) — Vangelis Stykas
:   This is the kind of research I wish existed more often: not another warning about trojanized coding assessments, but hard empirical data on what those attacks actually yield. Vangelis's team got access to attacker-controlled C2 infrastructure from a campaign that hit roughly 96,000 developer workstations via malicious npm packages disguised as fake job interviews, then triaged over 1,500 compromised hosts and cataloged what was actually exposed. The results are sobering: verified, active credentials across 175+ organizations in 30+ countries, production database credentials sitting on developer laptops, long-lived cloud keys with excessive permissions, and a "contractor multiplier effect" where one compromised developer held credentials into multiple unrelated client environments at once. All of it under coordinated responsible disclosure with 99 affected organizations.

    The framing that sticks with me is their point that organizations model the risk of a lost laptop, but not the risk of a compromised developer whose .env file quietly bridges their employer, their employer's clients, and upstream infrastructure providers. That's exactly the kind of underestimated blast radius I spent years chasing in incident response and open-source supply chain work — the actual exposure is always bigger and messier than the org chart assumes, and the fix has to be structural (ephemeral credentials, environment isolation, "assume compromise" workflows), not just a reminder to be careful.
    Wednesday, August 5 | 4:30pm-5:10pm ( Oceanside B, Level 2 )

[Scanning the Scanners: Turning Security Vendors Into Supply Chain Weapons](https://blackhat.com/us-26/briefings/schedule/index.html#scanning-the-scanners-turning-security-vendors-into-supply-chain-weapons-52982) — Raphael Karger
:   The premise alone is worth the seat: Raphael's team submitted malicious repos to 20 security scanners through free-tier signups and compromised five of them, gaining access to production databases, cloud credentials, and OAuth tokens tied to Fortune 100 companies, defense contractors, and government institutions. They did this all from a single config file, in under an hour, with no zero-days involved. The root cause is a broken assumption that repository analysis is read-only, when in reality modern tooling executes code and reads files it shouldn't by design (external check directories, gemspec evaluation, setup.py execution, symlinks reaching outside the repo). They're releasing an open-source tool, Build Canaries, that attendees can point at their own ingestion pipelines the same day.

    What I appreciate here is the inversion: the tools we buy specifically to protect our supply chain can themselves become the highest-value pivot point into it, precisely because we implicitly trust them more than the CI/CD pipelines they're bolted onto. That's a trust-boundary problem, and trust boundaries breaking down in places nobody thought to look is more or less the whole plot of my career. This is also a direct, practical extension of the developer-compromise blast-radius conversation from Vangelis's talk and the same underlying question of where trust and risk quietly accumulate when nobody's watching it.
    Thursday, August 6 | 3:35pm-4:15pm ( Jasmine, Level 3 )

[Threat Modeling LLMs: The PHANTOM-B Model]...