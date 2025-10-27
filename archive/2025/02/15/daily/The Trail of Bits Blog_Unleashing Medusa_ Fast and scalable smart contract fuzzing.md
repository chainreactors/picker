---
title: Unleashing Medusa: Fast and scalable smart contract fuzzing
url: https://blog.trailofbits.com/2025/02/14/unleashing-medusa-fast-and-scalable-smart-contract-fuzzing/
source: The Trail of Bits Blog
date: 2025-02-15
fetch_date: 2025-10-06T20:35:32.575386
---

# Unleashing Medusa: Fast and scalable smart contract fuzzing

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Unleashing Medusa: Fast and scalable smart contract fuzzing

[Josselin Feist](https://x.com/montyly), Anish Naik

February 14, 2025

[blockchain](/categories/blockchain/), [fuzzing](/categories/fuzzing/), [open-source](/categories/open-source/)

Page content

* [What is Medusa?](#what-is-medusa)
  + [Using Medusa](#using-medusa)
  + [What about Echidna?](#what-about-echidna)
* [The future of smart contract security](#the-future-of-smart-contract-security)

The wait is over—we’re thrilled to introduce [**Medusa v1**](https://github.com/crytic/medusa), a cutting-edge fuzzing framework designed to enhance smart contract security. Medusa is based on our first fuzzer, Echidna, and our experience performing countless security reviews on blockchain systems. With features that make fuzzing more scalable and efficient, Medusa represents a significant leap forward in how developers and security engineers approach smart contract fuzzing.

## What is Medusa?

Medusa is an open-source EVM-based fuzzer built on top of [Geth](https://github.com/ethereum/go-ethereum). Our first major release introduces powerful features that make fuzzing efficient and scalable:

* **Coverage-guided fuzzing**: Enables efficient contract exploration and provides direct feedback via an HTML report
* **Parallel fuzzing**: Scales seamlessly with your hardware to speed up fuzzing campaigns
* **Smart mutational value generation**: Leverages runtime values and insights from [Slither](https://github.com/crytic/slither) to optimize fuzzing inputs
* **On-chain fuzzing**: Seeds the fuzzing state with values fetched directly from the blockchain, improving real-world vulnerability discovery
* **Enhanced debugging capabilities**: Provides rich execution traces and advanced reporting capabilities for greater insight into the fuzzer’s execution

Medusa represents the state of the art in smart contract fuzzing. We have dedicated significant effort to ensure it is powerful and easy to use.

### Using Medusa

Getting started with Medusa is simple:

1. **Install Medusa** on macOS via Homebrew:

   ```
   brew install medusa
   ```

   For information on precompiled binaries and custom builds, visit our [installation page](https://github.com/crytic/medusa/blob/master/docs/src/getting_started/installation.md).
2. **Initialize a new project** by running this command:

   ```
   medusa init
   ```

   This command generates a `medusa.json` [configuration file](https://secure-contracts.com/program-analysis/medusa/docs/src/project_configuration/overview.html) to tweak the fuzzing runs.
3. **Start fuzzing** with this command:

   ```
   medusa fuzz
   ```

For detailed documentation, visit the [Medusa page](https://secure-contracts.com/program-analysis/medusa/docs/src/) on our Building Secure Contracts website. You can also watch our [fuzzing workshop](https://www.youtube.com/watch?v=QofNQxW_K08&list=PLciHOL_J7Iwqdja9UH4ZzE8dP1IxtsBXI) and our Uniswap v4 invariant walkthrough next week (date and time will be announced on X) to learn how to write robust invariants.

### What about Echidna?

With Medusa, we are exploring a new EVM implementation and language for smart contract fuzzing. While Echidna has been a powerful fuzzer, Medusa offers distinct advantages:

* **Written in Go**: This improves Medusa’s maintainability and allows for a native API, facilitating its integration into other projects.
* **Built on Geth**: This ensures strong EVM equivalence and eases code maintenance for Medusa.

To validate Medusa’s performance, we conducted an extensive internal benchmark against Echidna, fine-tuning Medusa’s value generation to ensure it delivers optimal results. For example, the following figure shows our benchmark’s output, where Medusa (dotted line) and Echidna (straight line) perform similarly in terms of coverage and corpus size:

![Internal Echidna versus Medusa benchmark](/img/echidna-vs-medusa.png)

Figure 1: Internal Echidna versus Medusa benchmark

While we will continue maintaining Echidna for minor bug fixes, our primary focus now shifts to Medusa’s evolution.

## The future of smart contract security

Fuzzing is a critical technique in smart contract security, and with Medusa, we aim to make this technique the industry standard. By providing powerful heuristics, parallel execution, and on-chain insights, Medusa makes smart contract fuzzing more scalable and accessible than ever before, empowering developers to identify vulnerabilities faster and more effectively.

We invite you to join our community and help shape Medusa’s future:

* [Contribute on GitHub](https://github.com/crytic/medusa/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22): Improve Medusa’s capabilities by submitting issues, PRs, or feedback.
* Join our [Slack](https://slack.empirehacking.nyc/): Connect with other security researchers and developers to share insights and best practices.

[Contact us](https://www.trailofbits.com/contact/) if your team wants feedback on how to use Medusa to its full potential.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [What is Medusa?](#what-is-medusa)
  + [Using Medusa](#using-medusa)
  + [What about Echidna?](#what-about-echidna)
* [The future of smart contract security](#the-future-of-smart-contract-security)

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.