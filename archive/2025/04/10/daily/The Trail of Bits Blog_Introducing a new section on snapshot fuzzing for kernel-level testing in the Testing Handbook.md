---
title: Introducing a new section on snapshot fuzzing for kernel-level testing in the Testing Handbook
url: https://blog.trailofbits.com/2025/04/09/introducing-a-new-section-on-snapshot-fuzzing-for-kernel-level-testing-in-the-testing-handbook/
source: The Trail of Bits Blog
date: 2025-04-10
fetch_date: 2025-10-06T22:04:54.387600
---

# Introducing a new section on snapshot fuzzing for kernel-level testing in the Testing Handbook

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Introducing a new section on snapshot fuzzing for kernel-level testing in the Testing Handbook

Maciej Domanski

April 09, 2025

[fuzzing](/categories/fuzzing/), [kernel](/categories/kernel/), [snapshot fuzzing](/categories/snapshot-fuzzing/), [testing handbook](/categories/testing-handbook/)

Page content

* [Why kernel-level testing matters](#why-kernel-level-testing-matters)
* [Enter snapshot fuzzing](#enter-snapshot-fuzzing)
* [New Testing Handbook content](#new-testing-handbook-content)

Today we’re announcing a significant addition to the fuzzing chapter of the [Trail of Bits Testing Handbook: Snapshot Fuzzing](https://appsec.guide/docs/fuzzing/snapshot-fuzzing/). This powerful technique enables security engineers to effectively test software that is traditionally difficult to analyze, such as kernels, secure monitors, and other complex targets that require non-trivial setup. Whether you’re auditing drivers or other kernel-mode components, including antivirus software, snapshot fuzzing provides a robust way to discover critical vulnerabilities. Consult our new Testing Handbook section for a walkthrough on how to conduct snapshot fuzzing on your system.

## Why kernel-level testing matters

Kernel-mode software presents unique security challenges. Operating at the most privileged level of the operating system, these components (particularly antivirus software) can monitor and intercept system-wide activities with unrestricted access. This high level of privilege comes with a high level of risk—a single crash can bring down the entire system, and memory corruption bugs at this level can cause severe consequences when exploited. This risk means that testing is crucial, but the traditional approaches to testing such software have significant limitations:

* The system-wide reach of kernel components prevents isolation of test cases.
* Debugger-based testing in VMs is slow and cumbersome.
* Fuzzers like libFuzzer and AFL can test only extracted functions, so they miss system-wide interactions.
* The black-box approach makes many conventional testing techniques difficult.

## Enter snapshot fuzzing

Snapshot fuzzing does not come with the limitations of traditional testing approaches. The technique captures the memory and the state of registers at a specific execution point, allowing the fuzzer to repeatedly restore and test from that exact state. This provides several major advantages:

* Tests can be really fast. Because only a snapshot of the system state is being tested, software does not have to start up on each run. For example, you can snapshot at the point a file is loaded and test thousands of variations from that state, where the data is processed.
* The same input produces the same result because each test starts from an identical system state. This eliminates the unpredictable behavior that often plagues kernel testing (such as unreproducible crashes).
* Precise crash detection with visualization support is possible through tools like the Lighthouse coverage explorer.
* It provides support for comprehensive tracking of code coverage and dirty memory.

## New Testing Handbook content

In our [new chapter on snapshot fuzzing](https://appsec.guide/docs/fuzzing/snapshot-fuzzing/) in the Testing Handbook, we’ve distilled our real-world experience into practical guidance that goes beyond basic documentation. The content reflects actual challenges and solutions we’ve encountered during security audits.

The new chapter demonstrates snapshot fuzzing using [what the fuzz (wtf)](https://github.com/0vercl0k/wtf/), an open-source fuzzer. This tool allows users to focus on writing target-specific harnesses instead of tackling the daunting task of building a snapshot fuzzer from scratch.

Our walkthrough on snapshot fuzzing using wtf will help you get started with these steps:

1. Creating a sample Windows kernel driver with userland communication
2. Capturing system snapshots for a VM with Windows 11
3. Developing harnesses that hook specific conditions
4. Running fuzz campaigns to identify kernel panics

Struggling with kernel-level security testing? Our experts can help you implement proper fuzzing for your specific environment. [Contact us](https://www.trailofbits.com/contact/) to learn more.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [Why kernel-level testing matters](#why-kernel-level-testing-matters)
* [Enter snapshot fuzzing](#enter-snapshot-fuzzing)
* [New Testing Handbook content](#new-testing-handbook-content)

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.