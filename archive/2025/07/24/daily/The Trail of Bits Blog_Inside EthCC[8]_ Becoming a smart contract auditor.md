---
title: Inside EthCC[8]: Becoming a smart contract auditor
url: https://blog.trailofbits.com/2025/07/23/inside-ethcc8-becoming-a-smart-contract-auditor/
source: The Trail of Bits Blog
date: 2025-07-24
fetch_date: 2025-10-06T23:39:41.406588
---

# Inside EthCC[8]: Becoming a smart contract auditor

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Inside EthCC[8]: Becoming a smart contract auditor

Nicolas Donboly

July 23, 2025

[blockchain](/categories/blockchain/), [conferences](/categories/conferences/), [people](/categories/people/)

Page content

Becoming a smart contract auditor requires a systematic approach to mastering four core disciplines: programming fundamentals, blockchain technology, Web3 security, and continuous practice. At EthCC[8] in Cannes, Trail of Bits blockchain security engineer Nicolas Donboly answered the question he gets asked most often: “How do I become a smart contract auditor?” Drawing from his own experience transitioning from a non-technical background into a leading security role, Nicolas laid out a clear, actionable path for aspiring auditors. Watch the [recording of his talk](https://www.youtube.com/live/BdSiiBIHOP0?si=bXv0_I4mKpuXZ9PE)!

#### **A high-stakes field with growing demand**

The work of a smart contract auditor is critical because, as Nicolas puts it, “Web3 security is frankly broken.” The stakes are higher than in Web2, where a hack typically involves data theft that is then monetized indirectly. In Web3, a hack means direct, immediate financial loss, which attracts highly sophisticated, nation-state-level attackers, as in the infamous $611M Ronin bridge hack from 2021. As the Web3 ecosystem grows, the need for skilled defenders is skyrocketing; bug bounty programs and audit requests are increasing exponentially, creating immense opportunities for skilled auditors.

#### **Auditing means thinking like an attacker, advising like a partner**

The auditor’s core challenge is understanding complex financial systems and identifying ways they can be exploited or manipulated. Their auditing work involves both automated scanning (with tools like our own [Slither](https://github.com/crytic/slither)) and manual review to identify vulnerabilities in the codebase, such as front-running and reentrancy attacks.

Here are the essential steps a smart contract auditor should perform during each audit:

* **First, build a mental model of the system.** Auditors are given the “blueprints” (the codebase) of a complex system. Their first job is to read the code, understand its business logic, and build a complete mental model of how it works.
* **During an audit, think like an attacker.** Once they understand a system, an auditor must adopt an attacker’s mindset to probe for weaknesses, edge cases, and unforeseen interactions, much like a heist planner looking for a bank’s vulnerabilities.
* **Test what should always be true.** Besides manual review, auditors define invariants, mathematical properties that must always be true in the system, and use fuzzing tools (like Echidna and Medusa) to test these properties across millions of possible states. This method often [uncovers complex and critical issues](https://blog.trailofbits.com/2024/04/30/curvance-invariants-unleashed/) that traditional manual review might miss.
* **Build trusting relationships.** The best auditors don’t just send a report and move on. They advise the client, explain the vulnerabilities and their potential real-world impact, and help developers build more secure software, raising the overall security posture of the entire ecosystem.

#### **Follow a four-step journey of continuous learning**

Nicolas broke down the journey into four essential, iterative steps. While the path is simple to understand, he stresses that it requires dedication and hard work.

1. **Learn programming:** A solid foundation in computer science is non-negotiable. You need to understand the fundamentals before you can secure them. (Resource: Harvard CS50)
2. **Learn blockchain:** Start by mastering the dominant technologies: the EVM and Solidity. This provides the most resources and job opportunities to begin your career. (Resources: Cyfrin Updraft, RareSkills)
3. **Learn Web3 security:** After learning how to build, you must learn how to break. This involves solving CTF challenges to train your attacker mindset and, crucially, studying past audit reports to understand real-world vulnerabilities. (Resources: The Ethernaut, Damn Vulnerable DeFi, Solodit, [Building Secure Smart Contracts](https://github.com/crytic/building-secure-contracts))
4. **Practice, practice, practice:** The best way to hone your skills is through public audit contests. This creates a powerful feedback loop: you compete, study the winning findings to see what you missed, and apply that knowledge to the next contest. Your performance on these public leaderboards becomes your resume in this highly meritocratic field.

#### **Get started**

The path to becoming a smart contract auditor is challenging, but it’s one of the most impactful and rewarding careers in the Web3 space. By systematically building your skills and proving them in public competitions, you can become a key defender of the decentralized future. Check out [this page](https://linktr.ee/nisedo) for a complete list of the resources Nicolas mentioned.

Trail of Bits is always looking for talented individuals to join our team! See our [careers page](https://www.trailofbits.com/careers) for open roles.

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

#### Recent Posts

* [Taming 2,500 compiler warnings with CodeQL, an OpenVPN2 case study](/2025/09/25/taming-2500-compiler-warnings-with-codeql-an-openvpn2-case-study/)
* [Supply chain attacks are exploiting our assumptions](/2025/09/24/supply-chain-attacks-are-exploiting-our-assumptions/)
* [Use mutation testing to find the bugs your tests don't catch](/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/)
* [Fickling’s new AI/ML pickle file scanner](/2025/09/16/ficklings-new-ai/ml-pickle-file-scanner/)
* [How Sui Move rethinks flash loan security](/2025/09/10/how-sui-move-rethinks-flash-loan-security/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.