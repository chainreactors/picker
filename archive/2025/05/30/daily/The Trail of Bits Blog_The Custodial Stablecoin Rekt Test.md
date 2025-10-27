---
title: The Custodial Stablecoin Rekt Test
url: https://blog.trailofbits.com/2025/05/29/the-custodial-stablecoin-rekt-test/
source: The Trail of Bits Blog
date: 2025-05-30
fetch_date: 2025-10-06T22:26:06.147034
---

# The Custodial Stablecoin Rekt Test

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The Custodial Stablecoin Rekt Test

[Benjamin Samuels](https://x.com/thebensams)

May 29, 2025

[blockchain](/categories/blockchain/), [policy](/categories/policy/), [threat modeling](/categories/threat-modeling/), [stablecoins](/categories/stablecoins/)

Page content

* [The Custodial Stablecoin Rekt Test](#the-custodial-stablecoin-rekt-test)
  + [1. Do you use multiple independent controls to verify transaction contents before signing?](#1-do-you-use-multiple-independent-controls-to-verify-transaction-contents-before-signing)
  + [2. Do you continuously update your security practices based on emerging threats?](#2-do-you-continuously-update-your-security-practices-based-on-emerging-threats)
  + [3. Do you work with the community to freeze and recover hacked funds?](#3-do-you-work-with-the-community-to-freeze-and-recover-hacked-funds)
  + [4. Do you segregate your signing infrastructure?](#4-do-you-segregate-your-signing-infrastructure)
  + [5. Is your signing infrastructure immutable?](#5-is-your-signing-infrastructure-immutable)
  + [6. Do you limit each role’s permissions to the minimum required?](#6-do-you-limit-each-roles-permissions-to-the-minimum-required)
  + [7. Do you verify the integrity of your critical software dependencies?](#7-do-you-verify-the-integrity-of-your-critical-software-dependencies)
  + [8. Do you have a written and tested incident response plan?](#8-do-you-have-a-written-and-tested-incident-response-plan)
  + [9. Do you use monitoring tools that can trigger an incident response if discrepancies are detected?](#9-do-you-use-monitoring-tools-that-can-trigger-an-incident-response-if-discrepancies-are-detected)
* [Next steps](#next-steps)

Last year, custodial stablecoins reached $27.6 trillion in transaction volume, surpassing [both Visa and Mastercard combined](https://blog.cex.io/ecosystem/stablecoin-landscape-34864). As this new asset’s systemic importance grows, so does the need for a clear understanding of its security risks, for both issuers and users of stablecoins. For groups managing significant stablecoin holdings, a single operational security failure in their stablecoin’s issuer now represents a material financial risk.

Custodial stablecoins are digital tokens that are designed to maintain a stable value, typically by being pegged to a fiat currency like the US dollar. They are issued and managed by centralized entities that maintain the reserves backing them.

Unlike decentralized stablecoins and many other blockchain systems, the integrity of a custodial stablecoin hinges on the operational security of its issuer, including the people, processes, and infrastructure behind the stablecoin. Custodial stablecoins share much more in common with banks than DeFi or blockchain protocols.

However, unlike banks, stablecoin users have few protections in the event of a computer security breach or compromise that impacts the issuer’s liabilities or ability to pay them. For this reason, institutions and users planning on holding or transacting in these assets should perform rigorous due diligence on the issuer’s security practices or else face the existential risk that their holdings become worthless.

In the past, Trail of Bits introduced [“the Rekt Test”](https://blog.trailofbits.com/2023/08/14/can-you-pass-the-rekt-test/) as a simple framework for assessing the basic security posture of blockchain projects. Building on that philosophy, this post will introduce a Rekt Test for custodial stablecoin issuers, focusing on the specific risks issuers face and offering a set of due diligence questions to help evaluate an issuer’s operational resilience.

## The Custodial Stablecoin Rekt Test

1. [Do you use multiple independent controls to verify transaction contents before signing?](#1-do-you-use-multiple-independent-controls-to-verify-transaction-contents-before-signing)
2. [Do you continuously update your security practices based on emerging threats?](#2-do-you-continuously-update-your-security-practices-based-on-emerging-threats)
3. [Do you work with the community to freeze and recover hacked funds?](#3-do-you-work-with-the-community-to-freeze-and-recover-hacked-funds)
4. [Do you segregate your signing infrastructure?](#4-do-you-segregate-your-signing-infrastructure)
5. [Is your signing infrastructure immutable?](#5-is-your-signing-infrastructure-immutable)
6. [Do you limit each role’s permissions to the minimum required?](#6-do-you-limit-each-roles-permissions-to-the-minimum-required)
7. [Do you verify the integrity of your critical software dependencies?](#7-do-you-verify-the-integrity-of-your-critical-software-dependencies)
8. [Do you have a written and tested incident response plan?](#8-do-you-have-a-written-and-tested-incident-response-plan)
9. [Do you use monitoring tools that can trigger an incident response if discrepancies are detected?](#9-do-you-use-monitoring-tools-that-can-trigger-an-incident-response-if-discrepancies-are-detected)

Although each question in the test can theoretically be answered with a simple “yes” or “no,” mature issuers should be able to provide specific, detailed explanations as to how they address the risks posed by each question.

While stablecoin users can use these questions to inform due diligence practices, stablecoin issuers can also use them as a self-assessment framework to identify critical gaps in their security program.

Alongside each question, we explain how it reflects our consensus of best practices for stablecoin issuers, but these recommendations are by no means exhaustive or absolute. The controls we recommend for addressing each question are meant to stimulate conversations to help stablecoin users and issuers better understand their security risk; they should not serve as a comprehensive checklist that every stablecoin issuer should follow.

Special thanks to [Josselin Feist](https://montyly.github.io/), [@tayvano\_](https://x.com/tayvano_), [Matt Aereal](https://x.com/mattaereal) ([SEAL Security Alliance](https://www.securityalliance.org/)/[The Red Guild](https://blog.theredguild.org/)), and [Isaac Patka](https://x.com/isaacpatka) ([Shield3](https://www.shield3.com/)) for reviewing and providing feedback on this test.

### 1. Do you use multiple independent controls to verify transaction contents before signing?

Single points of verification create catastrophic failure modes. Modern attackers can easily circumvent single-layer transaction verification mechanisms, as demonstrated in the [Bybit](https://www.bbc.com/news/articles/c2kgndwwd7lo) and [Radiant Capital](https://medium.com/%40RadiantCapital/radiant-post-mortem-fecd6cd38081) hacks where compromised interfaces showed legitimate transactions while executing malicious ones. Even multiple signers become useless when they all rely on the same verification method.

The fundamental challenge is that true “What You See Is What You Sign” (WYSIWYS) remains impossible with current hardware wallet technology. These devices can display basic transaction parameters but cannot decode complex smart contract interactions, leaving signers partially blind to what they’re actually authorizing. Until someone rebuilds the entire wallet stack, we’re stuck in a world where sophisticated transactions appear as generic “Blind Signing” interactions on hardware wallet screens. This technological limitation makes multiple independent verification controls essential.

Mature stablecoin issuers must implement redundant security controls with genuine independence. This means separate verification systems using different technical stacks, running on different hardware, with no shared dependencies. Each system must decode and display transaction contents through its own lens such that if one is compromised, the others must still reveal the truth.

For manual signing processes, implement at least three dedicate...