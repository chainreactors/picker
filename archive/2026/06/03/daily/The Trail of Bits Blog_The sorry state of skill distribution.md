---
title: The sorry state of skill distribution
url: https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/
source: The Trail of Bits Blog
date: 2026-06-03
fetch_date: 2026-06-04T06:30:14.888904
---

# The sorry state of skill distribution

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The sorry state of skill distribution

[Samuel Judson](/authors/samuel-judson/), [Tjaden Hess](/authors/tjaden-hess/)

June 03, 2026

[machine-learning](/categories/machine-learning/), [vulnerabilities](/categories/vulnerabilities/), [supply-chain](/categories/supply-chain/)

Page content

* [Why skill security matters](#why-skill-security-matters)
* [Bypassing ClawHub scanning](#bypassing-clawhub-scanning)
* [Bypassing skills.sh and Cisco skill scanning](#bypassing-skillssh-and-cisco-skill-scanning)
* [Bolstering Cisco’s skill scanning](#bolstering-ciscos-skill-scanning)
* [When legitimate skills look malicious](#when-legitimate-skills-look-malicious)
* [Don’t outsource trust to a scanner](#dont-outsource-trust-to-a-scanner)

Public skill marketplaces are being flooded with malicious skills that steal credentials, exfiltrate data, and hijack agents. In response, a segment of the security industry released skill scanners, a new family of tools designed to detect malicious skills before they’re installed. But we tested them, and they don’t work.

We recently bypassed [ClawHub’s malicious skill detector](https://github.com/openclaw/clawhub/blob/c3c885ec10161ad35fbe78678ccc3f8c34e03ffd/convex/lib/securityPrompt.ts), [Cisco’s agent skill scanner](https://github.com/cisco-ai-defense/skill-scanner), and all three of the scanners integrated into [skills.sh](http://skills.sh). These were not advanced attacks: it took us less than an hour to conceive and implement three of the four malicious skills in [trailofbits/overtly-malicious-skills](https://github.com/trailofbits/overtly-malicious-skills), using standard tricks and rapid inspection of the scanner source code. The fourth malicious skill took a few hours, but only because the prompt injection required some trial and error. Our findings demonstrate that even when skill scanners have some defenses, their static nature gives an adversary unlimited bites at the apple to tweak an attack until it finds a way through.

## Why skill security matters

Software supply chains have long been the soft underbelly of computer security. As fragile infrastructure susceptible to both insider threats and external attackers, these supply chains were vulnerable enough when malicious code was the sole vector of compromise. But the rise in agentic systems has spawned a new style of dependency—the skill—and with it a whole new ecosystem of marketplaces and distribution channels that now run alongside traditional package managers. Malicious skills can embed harmful instructions in natural language (e.g., a `SKILL.md` prompt) as well as code, giving them whole new avenues to attack any system they are given access to.

Compounding the issue, the distribution channels for skills have proved to be ship-first, secure-later. There are already multiple types of distribution channels for how users find skills and deploy them to their agents:

* ZIP archives distributed out-of-band and then uploaded manually or via API to agent harnesses like Anthropic’s [claude.ai](http://claude.ai) and OpenAI’s Codex;
* Curated marketplaces like [anthropics/skills](https://github.com/anthropics/skills) and [trailofbits/skills-curated](https://github.com/trailofbits/skills-curated); and
* Public marketplaces like [skills.sh](http://skills.sh) and [clawhub.ai](https://clawhub.ai/).

The first two methods can plausibly exclude malicious skills through procedural controls on where skills come from and who is allowed to approve their use. On the other hand, public marketplaces are one-stop, one-”click-to-install” shops that have been flooded with fake skills preying on unsuspecting users. These malicious skills aim to trap an unwary developer or OpenClaw agent, compromising the user’s system through arbitrary code execution or instructions for the agent to send sensitive data to a remote server.

Following a spate of compromises and attack demonstrations, several security companies have launched scanners intended to detect these malicious skills. We wanted to understand how well these systems defend users from them. We initially tested [Cisco’s skill-scanner](https://github.com/cisco-ai-defense/skill-scanner), where we found several bypasses and [submitted changes](https://github.com/cisco-ai-defense/skill-scanner/pull/25) to harden the system. Shortly thereafter, Vercel’s [skills.sh](http://skills.sh) [launched integrations](https://vercel.com/changelog/automated-security-audits-now-available-for-skills-sh) with scanners from Gen, Socket, and Snyk, and OpenClaw [partnered with VirusTotal](https://openclaw.ai/blog/virustotal-partnership) to scan skills in ClawHub; we tested these scanners, too.

## Bypassing ClawHub scanning

We’ll start with ClawHub (built by OpenClaw, for OpenClaw agents). The platform uses a two-part scanning solution. One is an integration with VirusTotal, which checks for known malware signatures and uses a proprietary scanner called Code Insight, built on Gemini 3 Flash, under the hood. The other scanner is a custom [harness and prompt](https://github.com/openclaw/clawhub/blob/e8c3947b21175669352bd88ab8f7b00df624ee56/convex/lib/securityPrompt.ts#L74-L74) for a guard model, by default GPT 5.5.

We bypassed both checks with [our first attack](https://github.com/trailofbits/overtly-malicious-skills/tree/main/skills/csv-summarizer). The approach is dead simple in both design and implementation: it simply prepends 100,000 newlines between some boilerplate and our overtly malicious code. The OpenClaw scanner [truncated the file](https://github.com/openclaw/clawhub/blob/c3c885ec10161ad35fbe78678ccc3f8c34e03ffd/convex/lib/securityPrompt.ts#L651-L652) and missed the malicious content entirely, while the VirusTotal scanner model seemed to become confused. And unless users are paying close attention, it’s easy to miss the long scroll wheel in the web UI.

![“Figure 1: OpenClaw scanner misses malicious content”](/2026/06/03/the-sorry-state-of-skill-distribution/figure1_hu_7e9b7e229e88e196.webp)

Figure 1: OpenClaw scanner misses malicious content

On the plus side, OpenClaw takes a relatively strict approach to skill packaging: only certain [whitelisted file types](https://github.com/openclaw/clawhub/blob/e8c3947b21175669352bd88ab8f7b00df624ee56/packages/clawdhub/src/schema/textFiles.ts#L1-L1) will be included in the distributed skills; no binaries or archives are allowed. This significantly constrains the types of attacks available without placing any meaningful limits on skill functionality. Not so, however, for our next targets.

## Bypassing skills.sh and Cisco skill scanning

The next set of scanners that we looked at operate on arbitrary git repositories, which allows us a grab bag of tricks involving binary files that both their simple pattern-matching and LLM-based strategies struggle to spot.

The [skills.sh](http://skills.sh) scanning works through integration with three external services: Gen Agent Trust Hub, Socket, and Snyk. The Cisco [skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) is an open-source multi-engine system, combining an LLM-driven analyzer (that can be backed by various models) with basic text pattern-matching and a variety of more involved static analysis methods targeting control and data flows. The tool also integrates an LLM-based meta-analyzer, which can cut out duplicates and false positives returned from the various engines. The policy for whether a skill is deemed safe is configurable, but defaults to a set of rules on the size of the skill, what file types are included, and what patterns are presumed hazardous.

We first built two simple skills that perform overtly malicious actions while audit reports come back as safe. [The first of these attacks](https://github.com/trailofbits/overtly-malicious-skills/tree/main/skills/context-loader) relies on indi...