---
title: Is Cyber Deception a Must-Have This Time?
url: https://zeltser.com/cyber-deception-again
source: Lenny Zeltser
date: 2026-11-10
fetch_date: 2026-11-11T08:34:06.353116
---

# Is Cyber Deception a Must-Have This Time?

[Skip to main content](#main-content)

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# Is Cyber Deception a Must-Have This Time?

Cyber deception is drawing renewed interest in the AI era, but it may not become mainstream this time either. Teams can still add decoys to identity, segmentation, secrets, and AI agent projects that already have their attention.

![A wooden duck decoy rides up the face of a tall blue wave in a woodblock print against a dark navy sky. Behind it on the left, two earlier waves break apart into cream foam and spray.](/assets/cyber-deception-again.BZxDjY6J_Zktxa3.webp)

I’ve been a fan of cyber deception and have witnessed several waves of deception technologies as they emerged and dissipated. Deception is having a resurgence, likely driven by AI’s effects on the dynamics between attackers and defenders. Will it gain must-have status, or will it, like the earlier waves, fade away? Let’s explore why deception has stalled in the past and what, if anything, is different this time. The deciding factor is how much attention defenders can spare as we race to address other problems that seem more urgent in the age of AI.

## Security teams have treated deception as a nice-to-have.

Cyber deception has been a discretionary measure for the defenders. I haven’t seen it as a mandate in major cybersecurity frameworks, contracts, or insurance policies. When competing for attention with must-have controls, deception found itself [left out of the market at large](/deception-security-tactics), with the exception of low-effort, low-cost deployments and some organizations with mature security programs.

Industry analysts treated cyber deception as a nice-to-have, too. [Forrester’s Josh Zelonis noted in 2018](https://www.bankinfosecurity.com/deception-tech-high-fidelity-alerts-if-hackers-take-bait-a-10868) that enterprises have generally given the technology a lukewarm reception because “it’s just something else on their network that they have to deal with.” [Augusto Barros at Gartner advised in 2019](https://www.bankinfosecurity.com/deception-technology-worth-investment-a-12881) that organizations check vendors’ claims about “the work hours needed to maintain a healthy deception deployment.” [Mike Privette at Return on Security observed in 2021](https://www.returnonsecurity.com/p/deception-technologies) that deception was “being considered as table stakes,” yet he cautioned that “if you’re not good at doing and proving the basics today, this won’t help you.”

Many of the cyber deception products that existed earlier ended up being absorbed into broader solutions, with [Forrester’s David Holmes pointing out in 2022](https://www.forrester.com/blogs/sentinelone-secures-identity-first-deception-second-in-attivo-acquisition/) that “deception tech, while super cool, was never able to achieve escape velocity on its own.” Larger companies bought four of the five vendors that [Mike Privette listed](https://www.returnonsecurity.com/p/deception-technologies) as top to consider. Zscaler [agreed to buy Smokescreen](https://web.archive.org/web/20231206144452/https%3A//www.darkreading.com/cloud-security/zscaler-buys-deception-technology-startup) in May 2021, shortly before Mike’s post, and in 2022 [Commvault bought TrapX](https://www.commvault.com/blogs/commvault-expands-its-security-offerings), [SentinelOne bought Attivo](https://www.forrester.com/blogs/sentinelone-secures-identity-first-deception-second-in-attivo-acquisition/), and [Proofpoint bought Illusive](https://www.proofpoint.com/us/blog/corporate-news/proofpoint-closes-acquisition-illusive-1). As a result, some identity, access, and data protection products now include deception features.

What, if anything, is different now?

## Deception may matter more in the AI era.

From the perspective of security architecture, deception plays to the [defender’s advantage](/defenders-advantage). [Per David Bianco](https://techcrunch.com/2023/02/07/cybersecurity-teams-beware-the-defenders-dilemma-is-a-lie/), “attackers usually operate with imperfect knowledge” of the environment. Therefore, they’re more likely to trip or waste time on decoys. This increases the attackers’ costs and gives defenders more of an opportunity to detect and respond to the attack.

AI in the hands of the attackers and employees is disrupting the [pursuit of equilibrium](/participating-in-the-eternal-cycle-of-cybersecurity) that characterizes the attack-defend cycle:

* **Faster vulnerability discovery:** AI accelerates the discovery of vulnerabilities in software, making it [impractical to assume](/vulnerability-management-hamster-wheel) that the organization can address the exploits by quickly patching the vulnerabilities. We need to put effort into strengthening our security architecture more broadly, and cyber deception can be part of that effort. Decoy credentials and systems can reveal an intruder who got in through a vulnerability the organization hasn’t patched yet.
* **Attack speed:** AI speeds up attacks. In the campaign [Anthropic reported in 2025](https://www.anthropic.com/news/disrupting-AI-espionage), AI performed most of the work at “an attack speed that would have been, for human hackers, simply impossible to match.” [Gartner warned in 2025](https://www.gartner.com/en/newsroom/press-releases/2025-09-18-gartner-says-that-in-the-age-of-genai-preemptive-capabilities-not-detection-and-response-are-the-future-of-cybersecurity) that security built on detection and response “will no longer be enough to keep assets safe from AI-enabled attackers.” Instead, Gartner advocated for countermeasures that “act preemptively and independently of humans to neutralize potential attackers before they strike.” It named “advanced deception and automated moving target defense” among such capabilities.
* **High-volume attacks:** At its peak, the AI in the Anthropic case made “thousands of requests, often multiple per second.” Deception can slow such attacks down and misdirect them. For example, the [US Army is pursuing “agentic deception”](https://www.nationaldefensemagazine.org/articles/2026/10/12/army-sprinting-to-field-ai-agents-to-counter-autonomous-cyberattacks) to lure adversaries away from its “crown jewels,” so that AI-assisted attackers spend “down their tokens” on parts of the network that matter less, which increases their costs.
* **Employees’ AI agents:** AI in the hands of employees can perform unauthorized actions within the organization even without users’ malicious intent. [Microsoft’s Hayete Gallot described such agents in 2026](https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/) as overprivileged insiders that “may not behave as intended.” Deception could help spot unsanctioned agents acting inside the organization or identify when sanctioned AI goes beyond its boundaries. [Researchers at the Institute for AI Policy and Strategy](https://www.iaps.ai/research/honeypots-for-ai-agent-insider-threats) called honeypots “a promising and underused measure” for securing such agents.

Governments have also explored deception. In 2025, the US Navy ran an [“assume you are compromised” prize challenge](https://www.niwcatlantic.navy.mil/Media/News-Stories/Article/4237618/assume-you-are-compromised-navy-announces-winners-of-cyber-challenge-to-seek-ne/) that sought capabilities to “deceive the adversary, learn their tactics.” The [UK National Cyber Security Centre (NCSC)](https://www.ncsc.gov.uk/blog-post/cyber-deception-trials-what-weve-learned-so-far) ran cyber deception trials and saw “a compelling case for increasing the use of cyber deception.” In 2026, [CISA published its first detailed guide](https://www.cisa.gov/news-events/news/new-cisa-guidance-helps-critical-infrastructure-detect-observe-and-impede-malicious-cyber-activity) to using cyber decoys.

Investors have backed deception startups, too. For example, Tracebit, founded in 2023, [raised $20...