---
title: A deep dive into Axiom’s Halo2 circuits
url: https://blog.trailofbits.com/2025/05/30/a-deep-dive-into-axioms-halo2-circuits/
source: The Trail of Bits Blog
date: 2025-05-31
fetch_date: 2025-10-06T22:25:46.692122
---

# A deep dive into Axiom’s Halo2 circuits

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# A deep dive into Axiom’s Halo2 circuits

Filipe Casal, Jim Miller, Fredrik Dahlgren, Joe Doyle, Tjaden Hess, Marc Ilunga

May 30, 2025

[cryptography](/categories/cryptography/)

Page content

* [The Axiom system](#the-axiom-system)
* [The security assessment process](#the-security-assessment-process)
* [The joys of reviewing Halo2](#the-joys-of-reviewing-halo2)
* [Key findings](#key-findings)
* [Recommendations: the path forward](#recommendations-the-path-forward)
* [Wrapping up](#wrapping-up)

Among the many highly complex, cutting-edge projects our cryptography team reviews, one from 2023 stands out. Over [two](https://github.com/trailofbits/publications/blob/master/reviews/2023-06-axiom-halo2libraries-securityreview.pdf) [audits](https://github.com/trailofbits/publications/blob/master/reviews/2023-10-axiom-halo2libraryupgrades-securityreview.pdf), we reviewed a blockchain system developed by [Axiom](https://www.axiom.xyz/) that allows computing over the entire history of Ethereum, all verified by zero-knowledge proofs (ZKPs) on-chain using ZK-verified elliptic curve and SNARK recursion operations. This system is built using the Halo2 framework—a complex, emerging technology that presents many challenges when building a secure application, including potential under-constrained issues resulting from its low-level API.

Since the conclusion of our audit, this library has been repurposed into Axiom’s more general OpenVM product, which is a ZK virtual machine that allows generation of ZK proofs for arbitrary Rust programs.

This post offers an insight into our review process; the discovered findings, including several soundness and under-constrained bugs that could break the system’s security; and the steps Axiom has implemented following our recommendations. Thanks to the massive scale of Axiom’s system and the novelty of the Halo2 framework, the audit significantly augmented our already-extensive knowledge of testing systems leveraging ZKPs. We applaud Axiom for being so collaborative and working diligently with us to help secure their system.

“We were impressed with the technical rigor and security mindset of the Trail of Bits team during their review of our Halo2 circuits. They were systematic and thoughtful in the review process, especially in the more intricate cryptographic areas of our system, giving us greater confidence in the final system security.” – Yi Sun, co-founder of Axiom

## The Axiom system

Axiom designed a system that allows access to historical blockchain data for EVM applications. Natively, EVM contracts may access only their own current account state; they cannot view past states, transaction statuses, or the state of other accounts. To enable this access, Axiom used ZKPs to succinctly verify flexible queries over historical transactions and states. Specifically, they used the Halo2 ZKP framework to allow users to read and trust historical data, such as headers, states, and transactions.

To build such a system, Axiom had to model the Ethereum data, transactions, state, etc., using Halo2 circuits. This requires writing Halo2 circuits for low-level primitives, such as elliptic curve cryptography, as well as higher-level data structures, like Merkle trees and Ethereum blocks. Since the existing libraries of Halo2 circuits were very limited, many of these primitives had to be developed as part of Axiom’s `halo2-base` and `halo2-ecc` libraries and used in the `snark-verifier` library for SNARK recursion. In addition to custom low-level libraries, Axiom also used a modified version of the Halo2 proof system itself. Several Axiom circuits include proofs about variable-length arrays, which benefit greatly from multi-phase circuits, which are implemented as an experimental feature in the Privacy & Scaling Explorations’ Halo2 fork.

Axiom has noted that since the audit has concluded, they have shut down the ZK coprocessor product that the ZK circuits were originally intended for, and Axiom is now using them as a dependency in the [OpenVM project](https://github.com/openvm-org/openvm), a modular and performant ZK-based virtual machine that allows `arbitrary` Rust crates to be used in ZK applications with some limitations.

## The security assessment process

The Trail of Bits cryptography team worked to review Axiom’s Halo2 circuits over two separate assessments. Our [first project](https://github.com/trailofbits/publications/blob/948e6e08db485b22bba2d53a48bb6a7d0f8d694b/reviews/2023-06-axiom-halo2libraries-securityreview.pdf), which ran from February 10 to May 17, 2023, focused on the low-level Halo2 primitives (PSE’s Halo2 fork), such as elliptic curve arithmetic and hash functions, as well as some of Axiom’s business logic. The [second audit](https://github.com/trailofbits/publications/blob/948e6e08db485b22bba2d53a48bb6a7d0f8d694b/reviews/2023-10-axiom-halo2libraryupgrades-securityreview.pdf), which ran from September 11 to September 29, 2023, focused on Axiom’s changes/upgrades from the first assessment as well as a deeper review of the SNARK verification logic.

Due to the nature of these projects, much of our efforts comprised deep manual review of the Halo2 circuits. Fortunately, our cryptography team has reviewed multiple projects using the Halo2 framework, and so we maintain internal notes and documentation pertaining to the sharp edges and common pitfalls associated with Halo2 applications, which we leveraged (and updated) continuously throughout the projects with Axiom. Effectively reviewing this system required us to extensively study the Axiom system by reviewing their documentation and maintaining an open dialogue with Axiom engineers through Slack and weekly calls.

Even though these projects were mostly manual efforts, we leveraged tools to automate some of our analysis as well. We used some Rust utility tools like [cargo-audit](https://crates.io/crates/cargo-audit) and [Clippy](https://github.com/rust-lang/rust-clippy) to find outdated dependencies and common Rust issues, and we used [Semgrep](https://semgrep.dev/) to look for more common Rust issues and Axiom-specific logic issues. Using Semgrep, we’ve been able to develop custom analyses that target Halo2; specifically, when we identified a Halo2 security issue that may be present in other locations, we used Semgrep to perform variant analysis and identify and remediate all similar issues.

## The joys of reviewing Halo2

In order to create ZKPs that prove the execution of a particular program, one must model the program in a format (circuits) that the ZKP system can use. Halo2 (and others such as Circom, Cairo, and Noir) is a library developed by the ZCash team that allows you to do exactly that; specifically, it allows you to specify circuits made up of selectively active polynomial equations called “gates,” equality constraints that act like “wires” between those gates, and subset-inclusion constraints referred to as “lookups.” Essentially, your circuit is a massive system of equations, where each equation is one of a few specific “gate” equations, potentially with different constant values. The variables in these equations represent different values used throughout the computation, such as your inputs, intermediate values, and outputs. This style of circuit definition is referred to as “plonkish,” since it generalizes the type of gates-and-wires arithmetic circuit first popularized by the PLoNK proof system. Rather than directly computing a result, circuits typically *check* that all of these values match the correct execution of your program. The complete details are much more complicated, but if you are curious, you can check out the [Halo2 book](https://zcash.github.io/halo2/index.html).

One of the most common and severe bug classes for ZKP circuits is known as “under-constrained” soundness bugs. A variable in a circuit is ...