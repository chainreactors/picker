---
title: The call for invariant-driven development
url: https://blog.trailofbits.com/2025/02/12/the-call-for-invariant-driven-development/
source: Trail of Bits Blog
date: 2025-02-13
fetch_date: 2025-10-06T20:34:50.336666
---

# The call for invariant-driven development

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The call for invariant-driven development

[Josselin Feist](https://x.com/montyly)

February 12, 2025

[invariant-development](/categories/invariant-development/), [blockchain](/categories/blockchain/)

Writing smart contracts requires a higher level of security assurance than most other fields of software engineering. The industry has evolved from simple ERC20 tokens to complex, multi-component DeFi systems that leverage domain-specific algorithms and handle significant monetary value. This evolution has unlocked immense potential but has also introduced an escalating number of hacks.

We need a paradigm shift toward invariant-driven development to drive the industry toward a more secure future. By embedding invariants—key properties that must always hold—into every stage of the software development lifecycle, you can significantly enhance the robustness of your smart contracts.

In this blog post, we’ll explore what invariant-driven development means, why it’s essential, and how you can adopt this approach to elevate your security practices and build more robust smart contracts.

## What are invariants?

At its core, invariant-driven development involves defining and maintaining invariants: statements about a program that must always hold, regardless of its state or execution path. These invariants act as the backbone of a system, ensuring its logical and functional integrity.

In smart contracts, invariants can take many forms depending on the application. For example:

* **ERC20 supply:** An ERC20 invariant is that a user’s balance must never exceed the token’s total supply.
* **Automated market makers (AMMs):** In a system using the *x \* y = k* formula—like Uniswap—the formula acts as an invariant for the swaps, ensuring that this equation remains true after every trade (assuming no fee).
* **Lending protocol:** An invariant of the function computing interest earned over time is that it is an increasing monotonic function (e.g., the return value increases as time increases).

Invariants can generally be categorized into two types:

* **Function-level invariants** often focus on specific computations and typically don’t need to change the state (e.g., the `pure` or `view` function in Solidity). For example, the lending invariant described above (the function that computes interest is an increasing monotonic function) can be expressed through a function-level invariant.
* **System-level invariants** span the entire system’s state and transitions, such as ensuring that its assets are always greater than or equal to its liabilities. An example of a system-level invariant is ensuring no user has a token balance greater than the total supply.

If you are familiar with fuzzing or formal verification, you are already familiar with invariants. Yet, as the next section shows, invariants are not limited to these techniques; you can also use them in the context of:

* **Monitoring**, through external tools, watching for transactions that break invariants
* **On-chain invariants**, which are executed directly within the smart contract and act as post-conditions when users interact with the contract
* **Manual reviews**, where the code review focuses on verifying key invariants

If you want to learn more about developing invariants in the context of fuzzing, see see [the fuzzing page](https://secure-contracts.com/program-analysis/echidna/index.html) on our Building Secure Contracts website and our [fuzzing workshop](https://www.youtube.com/watch?v=QofNQxW_K08&list=PLciHOL_J7Iwqdja9UH4ZzE8dP1IxtsBXI).

Security researchers have used invariants to assess contracts for many years; our [public reports](https://github.com/trailofbits/publications/blob/master/reviews/basis.pdf) include invariants that are over six years old, and their usage has been crucial in most of our security reviews. Nowadays, many of our competitors follow our approach, highlighting its efficiency. However, software engineers still barely use invariants despite their success in the security community. This is what we hope will change in the upcoming years.

Invariants are not a one-time consideration—they should guide every step of your smart contracts’ development. Here’s how you can apply them at every step of the process.

### Design the invariants

The earlier you start thinking about and documenting invariants, the more significant their impact on your project. Start by identifying invariants during the initial design of the protocol before any code is written. Ask the following questions:

* **What are the main invariants?** Ask your team to identify the 10 most essential invariants so they can keep them in mind at every stage of the project’s development. If they can’t answer, then dedicate more time to identifying them.
* **How will these invariants be checked?** How invariants are checked will influence the code’s design. For example, invariants that will be monitored require the emission of relevant events, and invariants that will be run on-chain can benefit from specific code isolation.
* **How will these invariants be specified and kept in sync with the code?** Chances are that your specification will evolve as your code and project’s requirements change. Having a process to ensure that they remain in sync will be crucial for the long-term success of the protocol.

This phase requires no special tools—just basic note-taking and documentation. Use this schema as a baseline:

| ID | Invariant | Components | Testing strategy |
| --- | --- | --- | --- |
|  | <English description> | <contracts/functions involved> | <fuzzing, formal verification, unit test, manual review> |

The English description can be as simple as how you describe it verbally. However, a good practice for complex invariants is to describe them through a Hoare Triple-like format (pre-condition, command, post-condition). Despite the formal-sounding name, a Hoare Triple simply captures three key elements:

* Pre-condition: Assumptions about the state/parameters before the actions
* Command: The actions to be tested
* Post-condition: What must be true after the actions

Conceptually, this is the same as following an [Arrange, Act, Assert](https://xp123.com/3a-arrange-act-assert/) or [Given, When, Then](https://en.wikipedia.org/wiki/Given-When-Then) design pattern if you’re familiar with them.

For example, the *x \* y = k* invariant may be expressed following this schema; see ToB1:

| ID | Invariants | Components | Testing Strategy |
| --- | --- | --- | --- |
| ToB0 | The balance of any user must never exceed the total supply of the token | `MyToken` | Fuzzing |
| ToB1 | * If the pool has no fee (*pre-condition*) * Call the swap function (*command*) * *x \* y = k* has not changed (*post-condition*) | `MyAMM` | Fuzzing |
| ToB2 | The function computing the interest earned over time is an increasing monotonic function | `Lending.compute_interest` | Formal verification |

Figure 1: Examples of invariants

If you’re looking for inspiration on creating invariants, you can find a set of predefined invariants in our [properties](https://github.com/crytic/properties) repo.

### Implement and test the invariants

The longest part of the smart contract development lifecycle is development and testing. Here, an iterative process between developing the code, creating and updating the invariant, and general testing will be crucial.

For example, identifying functions-level invariants will help you design the right level of modularity for your codebase, separating the components in a way that makes them easier to test.

During this phase, the tools at your disposal are:

* Fuzzers (e.g., [Medusa](https://github.com/crytic/medusa), [Echidna](https://github.com/crytic/echidna), and [Foundry](https://github.com/foundry-rs/foundry))
* Formal verification tools (e.g., [Halmos](https://github.com/a16z...