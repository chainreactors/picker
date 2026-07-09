---
title: Mutation testing comes to DAML
url: https://blog.trailofbits.com/2026/07/08/mutation-testing-comes-to-daml/
source: The Trail of Bits Blog
date: 2026-07-08
fetch_date: 2026-07-09T06:02:24.930951
---

# Mutation testing comes to DAML

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Mutation testing comes to DAML

[Kamil Chmielewski](/authors/kamil-chmielewski/)

July 08, 2026

[blockchain](/categories/blockchain/), [mutation-testing](/categories/mutation-testing/), [tool-release](/categories/tool-release/), [open-source](/categories/open-source/)

Page content

* [Why DAML’s coverage reports lie](#why-damls-coverage-reports-lie)
* [How mutation testing works](#how-mutation-testing-works)
* [Mutation testing forces the unhappy path](#mutation-testing-forces-the-unhappy-path)
* [What Mewt adds for DAML](#what-mewt-adds-for-daml)
* [What a surviving mutant looks like](#what-a-surviving-mutant-looks-like)
* [Limitations and what comes next](#limitations-and-what-comes-next)
* [Dive in](#dive-in)

In April we released [Mewt](https://blog.trailofbits.com/2026/04/01/mutation-testing-for-the-agentic-era/), our open-source mutation-testing engine that finds the gaps in your test suite. Today we’re expanding it with support for DAML, the language Canton Network applications are written in. Mewt now reads DAML, generates several classes of mutants (including two built for DAML’s authorization primitives), and runs them through your existing test suite to count how many mutants survive. If you want to try it, simply install Mewt from the [repository](https://github.com/trailofbits/mewt), point a `mewt.toml` at your project and its test command, and use `mewt run`.

For a team shipping DAML to production, that count is what a passing test run is actually worth: it puts a number on how much your suite checks, whereas a green run on its own does not.

## Why DAML’s coverage reports lie

Test coverage is the most reassuring lie in smart-contract development. Hitting 100% line coverage tells you the test runner walked the code; it does not tell you whether any test would fail if that code stopped doing what it is supposed to. We have been grading test harnesses by how many mutants they kill since at least [2019](https://blog.trailofbits.com/2019/01/23/fuzzing-an-api-with-deepstate-part-2/), and [our primer on finding the bugs your tests don’t catch](https://blog.trailofbits.com/2025/09/18/use-mutation-testing-to-find-the-bugs-your-tests-dont-catch/) shows how a green suite can still miss the bug that matters.

DAML’s built-in coverage measures execution at the template and choice level: which templates were created and which choices were exercised over the test run. It reports whether each choice was exercised, not what happened inside it. A test that exercises a choice once and asserts nothing about the result reports that choice as covered. The report prints the same green percentage whether the test verifies the outcome or discards it.

## How mutation testing works

Instead of asking whether your tests reached the code, mutation testing grades your tests by sabotaging that code. The engine generates mutants, copies of the code that each carry one small deliberate change: a flipped comparison, a removed branch, a dropped party. It then runs your test suite against each one. A mutant that makes the suite fail is caught; a mutant that passes every test survives. Every survivor is a change your tests let through, and each one is either harmless or a potential bug. The harmless ones are equivalent code no test could distinguish or a branch no execution reaches, and you can set those aside. The rest are a to-do list: each one is a specific test you are missing, a case your suite should check but does not, occasionally with a real bug sitting behind the gap. The primer above describes a real audit where a mutation campaign surfaced a high-severity bug that the project’s tests had missed.

## Mutation testing forces the unhappy path

A DAML contract encodes rights and obligations between named parties: who holds what, who owes what to whom, and who must authorize each step. A party is not an anonymous address. It represents a real organization or person, and the contract is the rulebook for how those parties interact, including which of them can take which action, what each is allowed to see, and what stays private between them.

Authorization is how that rulebook is enforced: who may take which action. It is also easy to get wrong in ordinary ways, such as a typo in a controller clause, a missing party, an extra one left over from a refactor. Every combination type-checks, so nothing rejects it before it ships. A static analyzer can flag suspicious patterns, but it has no way to know which party should hold which authority on your contract. That knowledge lives in your specification, and for most projects, the only executable form of the specification is the test suite. Happy-path tests supply every signature the contract asks for and confirm the transaction succeeds. They never try the negative case—removing a required signature and checking that the ledger rejects the transaction—so they never actually test whether that signature was required at all. If the tests don’t encode that rule, nothing downstream can recover it. Mutation testing is what tells you whether they do.

A green test run tells you your tests passed today. Mutation testing asks the harder question: would your tests catch a mistake, now or after the next code change? Where the answer is no, you have found a test case worth writing.

## What Mewt adds for DAML

Mewt parses every language it supports with a tree-sitter grammar. As of mid-2026, there is no maintained tree-sitter grammar for DAML, so we reused the upstream `tree-sitter-haskell` grammar. DAML is Haskell-shaped, but its contract constructs (`template`, `choice`, `controller`, and `signatory`) are not Haskell, and the grammar parses them as error-recovered subtrees. That matters less than it sounds. The common mutations still work on DAML’s ordinary expressions, so Mewt swaps arithmetic and comparison operators, flips Booleans, and removes branches just as it does in any other language, with only small adjustments where DAML’s surface syntax differs (DAML writes `/=` where most languages write `!=`). We got most of the value of a from-scratch grammar without building one.

The new engineering went into DAML’s authorization primitives, where the authorization bugs from the previous section live. Mewt adds two DAML-specific mutations:

* **Controller party swap** (CPS in Mewt’s output): replace one party in a `controller` clause with another party that is in scope at that site.
* **Controller party removal** (CPR): drop one party from a multi-party controller list.

Both target the same question: if the set of parties allowed to exercise this choice silently changed, would any test fail? They are a deliberately small starting set aimed at the bug class above, and more DAML-specific mutations are in the pipeline.

Driving a campaign needs no new harness. A short `mewt.toml` names the files to mutate and the test command (`dpm test` for a Daml 3 project), and `mewt run` does the rest, reporting each mutant as caught or surviving. The setup is deliberately small: trying it on your own project costs minutes, and we encourage exactly that.

## What a surviving mutant looks like

Picture a conditional payment between a buyer and a seller: the buyer sets money aside for the goods, and paying it out to the seller requires both parties to sign off. The buyer’s signature is the delivery confirmation. In DAML, that policy is one line: the `controller` line on the `Release` choice.

```
template ConditionalPayment
  with
    buyer  : Party
    seller : Party
    amount : Decimal
  where
    signatory buyer
    observer seller

    choice Release : ()
      with
        paid : Decimal
      controller buyer, seller
      do
        assert (paid == amount)
```

Figure 1: A payment that requires both the buyer and the seller to approve its release

A typical happy-path test creates the payment ...