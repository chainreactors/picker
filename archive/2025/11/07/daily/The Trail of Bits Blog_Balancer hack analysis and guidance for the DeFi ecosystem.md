---
title: Balancer hack analysis and guidance for the DeFi ecosystem
url: https://blog.trailofbits.com/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/
source: The Trail of Bits Blog
date: 2025-11-07
fetch_date: 2025-11-08T03:04:52.325103
---

# Balancer hack analysis and guidance for the DeFi ecosystem

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Balancer hack analysis and guidance for the DeFi ecosystem

Jim Miller, [Benjamin Samuels](https://x.com/thebensams), Anish Naik

November 07, 2025

[blockchain](/categories/blockchain/), [exploits](/categories/exploits/), [attacks](/categories/attacks/)

Page content

* [TL;DR](#tldr)
* [What happened: Understanding the vulnerability](#what-happened-understanding-the-vulnerability)
* [The 2021 audits: What we found and what we learned](#the-2021-audits-what-we-found-and-what-we-learned)
* [2021 to 2025: How the ecosystem has evolved](#2021-to-2025-how-the-ecosystem-has-evolved)
* [Preventing rounding issues in 2025](#preventing-rounding-issues-in-2025)
  + [Invariant documentation](#invariant-documentation)
  + [Comprehensive unit and integration tests](#comprehensive-unit-and-integration-tests)
  + [Comprehensive invariant testing with fuzzing](#comprehensive-invariant-testing-with-fuzzing)
  + [Invariant testing with formal verification](#invariant-testing-with-formal-verification)
* [Four Lessons for the DeFi ecosystem](#four-lessons-for-the-defi-ecosystem)

## TL;DR

* The root cause of the hack was a rounding direction issue that had been present in the code for many years.
* When the bug was first introduced, the threat landscape of the blockchain ecosystem was significantly different, and arithmetic issues in particular were not widely considered likely vectors for exploitation.
* As low-hanging attack paths have become increasingly scarce, attackers have become more sophisticated and will continue to hunt for novel threats, such as arithmetic edge cases, in DeFi protocols.
* Comprehensive invariant documentation and testing are now essential; the simple rule “rounding must favor the protocol” is no longer sufficient to catch edge cases.
* This incident highlights the importance of both targeted security techniques, such as developing and maintaining fuzz suites, and holistic security practices, including monitoring and secondary controls.

## What happened: Understanding the vulnerability

On November 3, 2025, attackers exploited a vulnerability in Balancer v2 to drain more than $100M across nine blockchain networks. The attack targeted a number of Balancer v2 pools, exploiting a rounding direction error. For a detailed root cause analysis, we recommend reading [Certora’s blog post](https://www.certora.com/blog/breaking-down-the-balancer-hack).

Since learning of the attack on November 3, Trail of Bits has been working closely with the Balancer team to understand the vulnerability and its implications. We independently confirmed that Balancer v3 was not affected by this vulnerability.

## The 2021 audits: What we found and what we learned

In 2021, Trail of Bits conducted three security reviews of Balancer v2. The commit reviewed during the first audit, in April 2021, did not have this vulnerability present; however, we did uncover a variety of other similar rounding issues using [Echidna](https://github.com/crytic/echidna), our smart contract fuzzer. As part of the [report](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2021-04-02.pdf), we wrote an appendix (appendix H) that did a deep dive on how rounding direction and precision loss should be managed in the codebase.

In October 2021, Trail of Bits conducted a security review of Balancer’s Linear Pools ([report](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2021-10-08.pdf)). During that review, we identified issues with how Linear Pools consumed the Stable Math library (documented as finding TOB-BALANCER-004 in our report). However, the finding was marked as “undetermined severity.”

At the time of the audit, we couldn’t definitively determine whether the identified rounding behavior was exploitable in the Linear Pools as they were configured. We flagged the issue because we found similar ones in the first audit, and we recommended implementing comprehensive fuzz testing to ensure the rounding directions of all arithmetic operations matched expectations.

We now know that the Composable Stable Pools that were hacked on Monday were exploited using the same vulnerability that we reported in our audit. We performed a security review of the Composable Stable Pools in September 2022; however, the Stable Math library was explicitly out of scope (see the Coverage Limitations section in the [report](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2022-09-02.pdf)).

The above case illustrates the difficulty in evaluating the impact of a precision loss or rounding direction issue. A precision loss of 1 wei in the wrong direction may not seem significant when a fuzzer first identifies it, but in a particular case, such as a low-liquidity pool configured with specific parameters, the precision loss may be substantial enough to become profitable.

## 2021 to 2025: How the ecosystem has evolved

When we audited Balancer in 2021, the blockchain ecosystem’s threat landscape was much different than it is today. In particular, the industry at large did not consider rounding and arithmetic issues to be a significant risk to the ecosystem. If you look back at the [biggest crypto hacks of 2021](https://www.auditone.io/blog-posts/biggest-crypto-hacks-2021-and-how-to-avoid-them), you’ll find that the root causes were different threats: access control flaws, private key compromise (phishing), and front-end compromise.

[Looking at 2022](https://blockworks.co/news/the-nine-largest-crypto-hacks-in-2022), it’s a similar story; that year in particular saw enormous hacks that drained several cross-chain bridges, either through private key compromise (phishing) or traditional smart contract vulnerabilities. To be clear, during this period, more DeFi-specific exploits, such as oracle price manipulation attacks, also occurred. However, these exploits were considered a novel threat at the time, and other DeFi exploits (such as those involving rounding issues) had not become widespread yet.

Although these rounding issues were not the most severe or widespread threat at the time, our team viewed them as a significant, underemphasized risk. This is why we reported the risk of rounding issues to Balancer ([TOB-BALANCER-004](https://github.com/balancer/balancer-v2-monorepo/blob/master/audits/trail-of-bits/2021-10-08.pdf)), and we reported a similar issue in our [2021 audit of Uniswap v3](https://github.com/trailofbits/publications/blob/master/reviews/UniswapV3Core.pdf). However, we have had to make our own improvements to account for this growing risk; for example, we’ve since tightened the ratings criteria for ​​our [Codebase Maturity evaluations](https://blog.trailofbits.com/2023/07/14/evaluating-blockchain-security-maturity/). Where Balancer’s Linear pools were rated “Moderate” in 2021, we now rate codebases without comprehensive rounding strategies as having [“Weak” arithmetic maturity](https://secure-contracts.com/development-guidelines/code_maturity.html?highlight=rounding#moderate).

Moving into 2023 and 2024, these DeFi-specific exploits, particularly rounding issues, became more widespread. In 2023, [Hundred Finance protocol was completely drained](https://blog.hundred.finance/15-04-23-hundred-finance-hack-post-mortem-d895b618cf33) due to a rounding issue. This same vulnerability was exploited several times in various protocols, including [Sonne Finance](https://blog.hundred.finance/15-04-23-hundred-finance-hack-post-mortem-d895b618cf33), which was one of the biggest hacks of 2024. These broader industry trends were also validated in our client work at the time, where we continued to identify severe rounding issues, which is why [we open-sourced roundme](https://x.com/thetrustx/status/1731876403627352247), a tool for human-assisted rounding direction analysis, in 2023.

Now, in...