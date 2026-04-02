---
title: Mutation testing for the agentic era
url: https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era/
source: The Trail of Bits Blog
date: 2026-04-01
fetch_date: 2026-04-02T04:29:33.648162
---

# Mutation testing for the agentic era

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Mutation testing for the agentic era

[Bo Henderson](/authors/bo-henderson/)

April 01, 2026

[blockchain](/categories/blockchain/), [mutation-testing](/categories/mutation-testing/), [tool-release](/categories/tool-release/), [open-source](/categories/open-source/)

Page content

* [The regex era](#the-regex-era)
* [slither-mutate: Speed through prioritization](#slither-mutate-speed-through-prioritization)
* [Introducing MuTON and mewt: The tree-sitter era](#introducing-muton-and-mewt-the-tree-sitter-era)
* [The future of mutation testing](#the-future-of-mutation-testing)
* [Optimizing configuration](#optimizing-configuration)
* [Triaging results](#triaging-results)
* [The promise and peril of mutation-driven test generation](#the-promise-and-peril-of-mutation-driven-test-generation)
* [Dive in](#dive-in)

Code coverage is one of the most dangerous quality metrics in software testing. Many developers fail to realize that code coverage lies by omission: it measures execution, not verification. Test suites with high coverage can obfuscate the fact that critical functionality is untested as software develops over time. We saw this when mutation testing uncovered a [high-severity Arkis protocol vulnerability](https://github.com/trailofbits/publications/blob/master/reviews/2024-12-arkis-defi-prime-brokerage-securityreview.pdf), overlooked by coverage metrics, that would have allowed attackers to drain funds.

Today, we’re announcing [MuTON](https://github.com/trailofbits/muton) and [mewt](https://github.com/trailofbits/mewt), two new mutation testing tools optimized for agentic use, along with a [configuration optimization skill](https://github.com/trailofbits/skills/tree/main/plugins/mutation-testing) to help agents set up campaigns efficiently. MuTON provides first-class support for TON blockchain languages (FunC, Tolk, and Tact), while mewt is the language-agnostic core that also supports Solidity, Rust, Go, and more.

The goal of mutation testing is to systematically introduce bugs (mutants) and check if your tests catch them, flagging hot spots where code is insufficiently tested. However, mutation testing tools have historically been slow and language-specific. MuTON and mewt are built to change that. To understand how, it helps to first understand what they’re replacing.

## The regex era

Mutation testing dates to the 1970s, but for a long time, the technique rarely saw much adoption in the blockchain space as a software quality measurement. Testing frameworks are coupled tightly to target languages, making support for new languages expensive.

[Universalmutator](https://agroce.github.io/icse18t.pdf) changed this with its regex engine. After a commit on March 10, 2018 added Solidity support, the tool gained immediate traction in the blockchain space. We collaborated with the universalmutator team to advance smart contract testing and highlighted the tool in our [2019 blog post](https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/). Despite (or perhaps because of) its elegant approach and compact codebase, universalmutator generated impressive mutant counts, enabling developers to assess test coverage more thoroughly than simpler tools could. Vyper and other language support followed, establishing universalmutator as the leading mutation testing tool for blockchain.

But regex has fundamental limits. Line-based patterns cannot mutate multi-line statements, a critical gap acknowledged by the original paper. More problematic: without mutant prioritization, the tool wastes time on redundant mutations. When commenting a line triggers no test failures, universalmutator still generates and tests every possible variation of that line, dramatically extending campaign runtime. Printing the results to `stdout` adds further friction for humans and AI agents reviewing campaigns. Later improvements (including a [2024 switch to comby](https://agroce.github.io/fse24.pdf) for better syntactic handling) addressed some pain points, but remaining limitations prompted the development of more focused alternatives.

Between 2019 and 2023, several tools emerged to address them, including our own [slither-mutate](https://github.com/crytic/slither/blob/master/docs/src/tools/Mutator.md) solution. Each took a different approach to the core problems of language comprehension, scalability, and test quality.

## slither-mutate: Speed through prioritization

We launched [slither-mutate](https://github.com/crytic/slither/blob/master/docs/src/tools/Mutator.md) in August 2022, after our wintern, [Vishnuram](https://github.com/vishnuram1999), brought the concept to life. Because Slither already parsed Solidity’s AST and provided a Python API, the groundwork was laid to generate syntactically valid mutations and implement a cleaner tweak-test-restore cycle (earlier tools polluted repositories with mutated files).

The tool’s key innovation was mutant prioritization: high-severity mutants replace statements with reverts (exposing unexecuted code paths), medium-severity mutants comment out lines (revealing unverified side effects), and low-severity mutants make subtle changes, such as swapping operators. The tool skips lower-severity mutants when higher-severity ones already indicate missing coverage on the same line, dramatically reducing campaign runtime, the biggest obstacle to wider mutation testing adoption. By late 2022, we were deploying slither-mutate across most Solidity audits.

Two limitations remained. First, tight coupling to Solidity meant there was no path to easily support other blockchain languages. Second, dumping results to `stdout` persisted as a problem, but adding a database to Slither creates unacceptable friction for the broader Slither user base.

## Introducing MuTON and mewt: The tree-sitter era

MuTON, our newest mutation testing tool, provides first-class support for all three TON blockchain languages: Tolk, Tact, and FunC. We’re grateful to the [TON Foundation](https://ton.foundation/) for supporting its development. MuTON is built on mewt, a language-agnostic mutation testing core that also supports Solidity, Rust, and more.

MuTON achieves language comprehension comparable to slither-mutate while supporting multiple languages by using Tree-sitter as its parser. Tree-sitter powers syntax highlighting in modern editors, building a concrete syntax tree that distinguishes language keywords from comments. This allows MuTON to target expressions like if-statements in a well-structured way, handling multi-line statements gracefully. Traditionally, integrating Tree-sitter grammars for new language support takes orders of magnitude longer than writing regex rules, but AI agents paired with [bespoke skills](https://github.com/trailofbits/mewt/blob/main/.claude/skills/add-language-support/SKILL.md) invert this calculus, delivering Tree-sitter’s power with regex-like ease of extension.

MuTON stores all mutants and test results in a SQLite database, a quality-of-life improvement that became evident while using slither-mutate but wasn’t feasible to retrofit. Results persist across sessions; campaigns can be paused and resumed without losing progress. If you accidentally close your terminal during a 24-hour campaign, your work survives. Persistent storage also enables flexible filtering and formatting: print only uncaught mutants in specific files, or translate results to SARIF for improved review. This flexibility helps humans and AI agents explore results, triage findings, and hunt for bugs.

## The future of mutation testing

MuTON addresses many historical pain points, but significant friction remains. Three challenges stand between mutation testing and widespread adoption: configuring campaigns for reasonable runtimes, triaging results to separate signal from noise, and generating tests that enco...