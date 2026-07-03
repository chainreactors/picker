---
title: GPT-5.5-Cyber built a zlib fuzzing lab in a day
url: https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/
source: The Trail of Bits Blog
date: 2026-07-02
fetch_date: 2026-07-03T05:47:22.313618
---

# GPT-5.5-Cyber built a zlib fuzzing lab in a day

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# GPT-5.5-Cyber built a zlib fuzzing lab in a day

[Benjamin Samuels](/authors/benjamin-samuels/)

July 02, 2026

[open-source](/categories/open-source/), [vulnerabilities](/categories/vulnerabilities/), [fuzzing](/categories/fuzzing/), [machine-learning](/categories/machine-learning/)

Page content

* [The lab GPT-5.5-Cyber built in a day](#the-lab-gpt-55-cyber-built-in-a-day)
* [Reporting discipline is the hard part](#reporting-discipline-is-the-hard-part)
* [The moat is gone](#the-moat-is-gone)
* [Lessons learned](#lessons-learned)

We’re running [Patch the Planet](https://trailofbits.com/patch-the-planet), an ongoing collaboration with OpenAI that pairs Trail of Bits engineers directly with more than 30 open-source projects. Its goal is to front-run a serious problem facing open-source maintainers: highly capable models like GPT-5.5-Cyber will soon create a firehose of bug reports, and OSS maintainers are already spread thin. Our plan is to point OpenAI’s latest models at real codebases, find the security bugs first, work with maintainers to patch them, and find ways to decrease the burden on maintainers in the long run.

We’ll publish field reports like this one as the initiative progresses; follow along via the [Patch the Planet](/tags/patch-the-planet/) tag.

The expertise barrier that kept bespoke fuzzing campaigns out of reach for most attackers is gone. **We watched GPT-5.5-Cyber build in a single day what would have taken weeks for a skilled security researcher**: harnesses across a dozen entrypoints, sanitizer and variant builds, seeds, and multiple findings currently undergoing coordinated disclosure.

This particular instance focused on [zlib](https://github.com/madler/zlib), a widely used data format and lossless data compression software library. We pointed GPT-5.5-Cyber at the library and drove it through Codex with the `/goal` command, asking it to find a specific class of bugs that are critically dangerous in compression libraries. We’ll publish the full harness and findings for inspection once the vulnerabilities are patched and a new release is cut.

## The lab GPT-5.5-Cyber built in a day

We didn’t tell the model how to find these bugs. The obvious first move is to read the source code, but zlib has been reviewed so thoroughly that there’s little left to find that way. GPT-5.5-Cyber worked that out for itself, judged static review to be a poor use of tokens, and decided the higher value path was to build fuzz tooling to dynamically test the code. Earlier models given the same goal tend to read the code and flag whatever looks suspicious, ultimately leading to mediocre outcomes.

We believe the frontier 5.5-Cyber model combined with the `/goal` feature is what let it execute end-to-end without hand-holding. `/goal` forced the objective to live across multiple turns and compactions so the model held scope, and 5.5-Cyber was smart enough to reject weak findings, expand coverage when a line of investigation died, and keep running until it had workable proof-of-concepts backed by sanitizer output.

Over the next several hours, it built the campaign out one piece at a time:

* It used ASan and UBSan builds so memory errors became observable.
* It repurposed existing edge-case tests as guidance for the fuzz seed corpus.
* It wrote C/C++ harnesses across a dozen entrypoints, including inflate, inflateBack, uncompress2, gzFile, MiniZip, puff, blast, infback9, gzjoin, gzappend, and several contrib stream wrappers.
* It used compile-time variant builds (`INFLATE_STRICT`, `BUILDFIXED`, `PKZIP_BUG_WORKAROUND`, etc.) to reach code that the default zlib build hides.

Each of these decisions is routine on its own, but stringing them together in the right order across a dozen entrypoints, without being handed the steps, is a relatively large shift in how capable frontier models are.

While zlib already has fuzzing coverage from its OSS-Fuzz harness, GPT-5.5-Cyber went beyond the default harness shape, which passes random inputs to the gz\* APIs. Instead of directly fuzzing the gz\* APIs, its most successful harness found bugs in valid gz\* states that could only be constructed by operating system backpressure.

## Reporting discipline is the hard part

In general, models tend to struggle with deciding when a finding is severe enough to justify escalating it into reporting. Weaker models tend to escalate bugs that cause the program to crash, but are not reachable under real-world conditions. Early on, GPT-5.5-Cyber hit a null callback crash in `inflateBack`. The crash was real, but reaching it required a caller to set up a state that was extraordinarily unlikely in real-world conditions, so the model logged it as unreachable and moved on. This agent kept going without human intervention and found several higher-impact issues.

That discipline is the whole game. The value of the zlib harness came from automation plus **a strict definition of what counted as a reportable finding**. Without strong validity rules baked into the goal and a model truly capable of evaluating those rules, the agent will generate mountains of noise with high confidence: invalid uses of the public API, expected parser errors, internal API misuse, etc.

## The moat is gone

Setting up a bespoke fuzzing campaign used to mean finding someone who could write harnesses, reason about valid API state, and differentiate between a bug and a crash that can’t happen in practice. This asymmetry kept casual attackers out of the game for most targets.

That moat is mostly gone now, and it shifts the threat model in two directions at the same time. For a skilled researcher, it is a force multiplier: the weeks-long tax on every new target drops to a day or less, so the same person can audit far more code. For a low-skill attacker, the floor rises: the tedious, expertise-heavy work of getting a harness off the ground can now be driven by starting a goal and supervising the loop.

For anyone shipping security-critical code, the practical takeaway is clear. Bespoke fuzzing is no longer a luxury reserved for projects with mature OSS-Fuzz coverage, and it is no longer expensive for the people whom you would rather not have running it. The defensive move is to do it first, with the validity rules that turn agent output into a high-signal source you can act on.

## Lessons learned

The fuzzing lab answered the question we came in with and left us a much bigger one. We didn’t ask GPT-5.5-Cyber to build a fuzzing campaign; it decided that was the job and did it. The thing worth watching for now is what else these new models will reach for once you hand them a goal and step back, especially the approaches we would never have thought to ask for before.

That is also why the front-running work being done by Patch the Planet matters. Every new capability that helps us find bugs faster is just as available to an attacker, so the advantage goes to whoever finds the bugs and fixes them first.

* [Patch the Planet](/tags/patch-the-planet/)

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

## Related Posts

[### Introducing Patch the Planet

June 22, 2026

Patch the Planet is our joint initiative with OpenAI to assist critical open-source software in the age of machine-speed …](/2026/06/22/introducing-patch-the-planet/)

[### The sorry state of skill distribution

June 3, 2026

We recently bypassed ClawHub’s malicious skill detector, Cisco’s agent skill scanner, and all three of the scanners …](/2026/06/03/the-sorry-state-of-skill-distribution/)

[### gosentry brings LibAFL-g...