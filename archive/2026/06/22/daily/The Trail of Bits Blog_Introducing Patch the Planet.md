---
title: Introducing Patch the Planet
url: https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
source: The Trail of Bits Blog
date: 2026-06-22
fetch_date: 2026-06-23T06:06:46.961181
---

# Introducing Patch the Planet

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Introducing Patch the Planet

[Trail of Bits](/authors/trail-of-bits/)

June 22, 2026

[announcements](/categories/announcements/), [open-source](/categories/open-source/), [vulnerabilities](/categories/vulnerabilities/)

Page content

* [We brought patches, not just bug reports](#we-brought-patches-not-just-bug-reports)
* [A few highlights from the week](#a-few-highlights-from-the-week)
* [Finding the bugs is now the easy part](#finding-the-bugs-is-now-the-easy-part)
* [Guidance for maintainers](#guidance-for-maintainers)
* [What’s next and how to get involved](#whats-next-and-how-to-get-involved)

What happens when you clear dozens of Trail of Bits engineers’ schedules, pair them with every open-source maintainer they can contact, and unleash the latest frontier models like GPT-5.5-Cyber on critical open-source targets? Thanks to [our partnership with OpenAI](https://openai.com/index/daybreak-securing-the-world/) and its Daybreak initiative, [we can report](https://gist.github.com/patch-the-planet/69fd1aa925c8e73edea9e6e967043cbb) that the impact is hundreds of discovered bugs, 64 pull requests, and 51 issues filed across 19 projects (with many more still undergoing coordinated disclosure). That was just the first week of [Patch the Planet](https://trailofbits.com/patch-the-planet).

Frontier models like GPT-5.5-Cyber are producing a firehose of security findings, and already-stretched maintainers must sift through all of it to separate real vulnerabilities from plausible-sounding false positives. Patch the Planet is different: with our experts orchestrating and triaging findings, we handle the work of fixing and hardening the code alongside the people who maintain it.

The first week of Patch the Planet covered 19 projects across cryptography, networking, language infrastructure, and software supply chain. Among these 19 projects were cURL, NATS, pyca, Sigstore, aiohttp, the Go project, freenginx, Python and python.org, urllib3, PyPI, SimpleX, Valkey, and RustCrypto. Over 30 projects have joined the initiative so far, and we’re rapidly expanding it to include more; if you maintain an open-source project, [apply to join](https://trailofbits.com/patch-the-planet)!

![“Live look at the Trail of Bits engineering teams”](/2026/06/22/introducing-patch-the-planet/ptp-image-1.gif)

Live look at the Trail of Bits engineering teams

Anyone can file an issue, flex, and walk away. We showed up with the patches: 37 are already merged, and many more are in flight. These merges go beyond just fixing bugs: we’re adding new tests and fuzzing harnesses, CI security scanning, supply-chain tooling, correctness fixes, and features maintainers had been meaning to get to. The goal of Patch the Planet is to leave essential open-source projects measurably better off.

## We brought patches, not just bug reports

We’re reporting public findings [on GitHub](https://gist.github.com/patch-the-planet/69fd1aa925c8e73edea9e6e967043cbb), including 64 total pull requests. We also filed 51 issues, 19 of which are already closed with a fix. This public tally undercounts the work, since several projects take reports through private channels like HackerOne, GitHub security advisories, mailing lists, and private forks, and most of these have not been released publicly yet.

What’s in those pull requests matters more than the count. At python.org, we added a CI workflow built on [zizmor](https://github.com/zizmorcore/zizmor), our open-source GitHub Actions auditor, fixed all of the issues it flagged, and integrated it into their CI. In RustCrypto, we contributed correctness fixes to the big-integer library that higher-level cryptography is built on, alongside genuine feature work in review: serde encoding support and HPKE DHKEM suite IDs. Other patches were plain engineering help: storage-accounting and service-restart fixes in SimpleX, a clearer admin-quarantine confirmation in PyPI’s Warehouse, and supply-chain improvements like SBOM sidecars for Python’s Windows artifacts. We will also be upstreaming many testing improvements and new testing campaigns. Arguably, our best contributions are not even bug or security fixes.

Keeping track of all of this is a bot we call Patchy. Patchy monitors every project, posts each new finding and merged patch to our Slack, and, for reasons we consider scientifically sound, reintroduces the common use of [goblins, gremlins, and assorted creatures](https://openai.com/index/where-the-goblins-came-from/). Here’s Patchy’s description of [an issue that has been patched](https://github.com/pyca/cryptography/pull/14933):

![“Patchy’s description of an issue that has been patched”](/2026/06/22/introducing-patch-the-planet/ptp-image-2_hu_d772e23377508832.webp)

Patchy’s description of an issue that has been patched

When a patch lands, Patchy celebrates with a triumphant `PATCHY HAPPY`. Making Patchy happy is really what drives us.

![“Bug patched, Patchy happy”](/2026/06/22/introducing-patch-the-planet/ptp-image-3_hu_5af72ac2534386fd.webp)

Bug patched, Patchy happy

## A few highlights from the week

The week produced more than we can fit in this post, but here are some quick highlights.

**A fuzzing lab built in a day.** Given a narrow goal (find remotely exploitable bugs) and no instructions on how, GPT-5.5-Cyber decided that reading the source of one of the most-reviewed C libraries in existence was a poor use of tokens. Instead, it stood up a full fuzzing lab in under a day: sanitizer and variant builds, a seed corpus drawn from existing tests, and harnesses across a dozen entry points. Instead of simply fuzzing exposed APIs, it successfully built a harness that injected operating system backpressure to identify novel issues by reaching previously unexplored buggy states. We estimate all of that effort likely would’ve taken one of our fuzzing experts two to three weeks to do manually. Just as important, it showed judgment about what to test, what to report (and not report), and where to find higher-impact findings. We’ll publish the full details in a standalone field report.

**A pipeline for variant testing historical CVEs built in a day**. Codex was also adept at building simple but effective pipelines, such as the CVE variant analysis pipeline shown below. Codex’s `/goal` feature combined with frontier models like GPT-5.5-Cyber for this type of variant analysis produced novel issues with almost exclusively high-signal output.

![“Pipeline for historical CVE variant analysis”](/2026/06/22/introducing-patch-the-planet/ptp-image-4_hu_a106c2e464121abc.webp)

Pipeline for historical CVE variant analysis

**A release-pipeline improvement at python.org.** We reported multiple security issues for [python.org](http://python.org), including some issues closing a legacy-API authorization gap. But we’re most proud of the work that produced long-term improvements to python.org’s release infrastructure: the new zizmor CI scanning, tightened release-file and metadata validation, deletion scoping fixed so bulk operations can’t reach beyond their target, and release-tooling patches in review that quote remote command arguments, fail safely on partial uploads, and add SBOM sidecars.

**The aiohttp maintainers fixed their issues almost immediately.** We privately reported a cluster of issues across aiohttp’s client and server paths, including cookies that could regain broader scope after a save and reload, digest credentials that could answer a challenge from the wrong origin, and resource limits that ran after attacker-controlled buffering rather than before. The maintainers authored and merged all eight fixes within hours, seven of them inside a single five-hour window. We were impressed and appreciate the maintainers’ prompt and collaborative work on these issues!

**Differentially testing major cryptographic libraries again...