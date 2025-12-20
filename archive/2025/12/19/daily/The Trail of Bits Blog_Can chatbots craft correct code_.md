---
title: Can chatbots craft correct code?
url: https://blog.trailofbits.com/2025/12/19/can-chatbots-craft-correct-code/
source: The Trail of Bits Blog
date: 2025-12-19
fetch_date: 2025-12-20T03:14:00.572889
---

# Can chatbots craft correct code?

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Can chatbots craft correct code?

[Evan Sultanik](/authors/evan-sultanik/)

December 19, 2025

[machine-learning](/categories/machine-learning/), [engineering-practice](/categories/engineering-practice/), [program-analysis](/categories/program-analysis/)

Page content

* [The compiler’s contract: Determinism and semantic preservation](#the-compilers-contract-determinism-and-semantic-preservation)
* [Why LLMs are fundamentally different](#why-llms-are-fundamentally-different)
  + [Nondeterminism in practice](#nondeterminism-in-practice)
  + [The ambiguous input problem](#the-ambiguous-input-problem)
  + [The unambiguous input problem (which isn’t)](#the-unambiguous-input-problem-which-isnt)
* [A case study: When Claude “fixed” a bug that wasn’t there](#a-case-study-when-claude-fixed-a-bug-that-wasnt-there)
* [The scale problem: When context matters most](#the-scale-problem-when-context-matters-most)
* [The path forward: Formal verification and new frameworks](#the-path-forward-formal-verification-and-new-frameworks)
  + [Where LLMs work well today](#where-llms-work-well-today)
  + [What we need to build](#what-we-need-to-build)
  + [The trust model](#the-trust-model)
* [Conclusion: Embracing verification in the age of AI](#conclusion-embracing-verification-in-the-age-of-ai)

I recently attended the [AI Engineer Code Summit](https://www.ai.engineer/code) in New York, an invite-only gathering of AI leaders and engineers. One theme emerged repeatedly in conversations with attendees building with AI: the belief that we’re approaching a future where developers will *never* need to look at code again. When I pressed these proponents, several made a similar argument:

> Forty years ago, when high-level programming languages like C became increasingly popular, some of the old guard resisted because C gave you less control than assembly. The same thing is happening now with LLMs.

On its face, this analogy seems reasonable. Both represent increasing abstraction. Both initially met resistance. Both eventually transformed how we write software. But this analogy really thrashes my cache because it misses a fundamental distinction that matters more than abstraction level: ***determinism***.

The difference between compilers and LLMs isn’t just about control or abstraction. It’s about semantic guarantees. And as I’ll argue, that difference has profound implications for the security and correctness of software.

## The compiler’s contract: Determinism and semantic preservation

Compilers have one job: preserve the programmer’s semantic intent while changing syntax. When you write code in C, the compiler transforms it into assembly, but the meaning of your code remains intact. The compiler might choose which registers to use, whether to inline a function, or how to optimize a loop, but it doesn’t change what your program *does*. If the semantics change unintentionally, that’s not a feature. That’s a compiler bug.

This property, semantic preservation, is the foundation of modern programming. When you write `result = x + y` in Python, the language guarantees that addition happens. The interpreter might optimize how it performs that addition, but it won’t change what operation occurs. If it did, we’d call that a bug in Python.

The historical progression from assembly to C to Python to Rust maintained this property throughout. Yes, we’ve increased abstraction. Yes, we’ve given up fine-grained control. But we’ve never abandoned determinism. The act of programming remains compositional: you build complex systems from simpler, well-defined pieces, and the composition itself is deterministic and unambiguous.

There are some rare conditions where the abstraction of high-level languages prevents the preservation of the programmer’s semantic intent. For example, cryptographic code needs to run in a constant amount of time over all possible inputs; otherwise, an attacker can use the timing differences as an oracle to do things like brute-force passwords. Properties like “constant time execution” aren’t something most programming languages allow the programmer to specify. [Until very recently](https://blog.trailofbits.com/2025/12/02/introducing-constant-time-support-for-llvm-to-protect-cryptographic-code/), there was no good way to force a compiler to emit constant-time code; developers had to resort to using dangerous inline assembly. But with [Trail of Bits’ new extensions to LLVM](https://blog.trailofbits.com/2025/12/02/introducing-constant-time-support-for-llvm-to-protect-cryptographic-code/), we can now have compilers preserve this semantic property as well.

As I wrote back in 2017 in “[Automation of Automation](https://www.sultanik.com/blog/AutomationOfAutomation),” there are fundamental limits on what we can automate. But those limits don’t eliminate determinism in the tools we’ve built; they simply mean we can’t automatically prove every program correct. Compilers don’t try to prove your program correct; they just faithfully translate it.

## Why LLMs are fundamentally different

LLMs are nondeterministic by design. This isn’t a bug; it’s a feature. But it has consequences we need to understand.

### Nondeterminism in practice

Run the same prompt through an LLM twice, and you’ll likely get different code. Even with temperature set to zero, model updates change behavior. The same request to “add error handling to this function” could mean catching exceptions, adding validation checks, returning error codes, or introducing logging, and the LLM might choose differently each time.

This is fine for creative writing or brainstorming. It’s less fine when you need the semantic meaning of your code to be preserved.

### The ambiguous input problem

Natural language is inherently ambiguous. When you tell an LLM to “fix the authentication bug,” you’re assuming it understands:

* Which authentication system you’re using
* What “bug” means in this context
* What “fixed” looks like
* Which security properties must be preserved
* What your threat model is

The LLM will confidently generate code based on what it *thinks* you mean. Whether that matches what you *actually* mean is probabilistic.

### The unambiguous input problem (which isn’t)

“Okay,” you might say, “but what if I give the LLM unambiguous input? What if I say ‘translate this C code to Python’ and provide the exact C code?”

Here’s the thing: even that isn’t as unambiguous as it seems. Consider this C code:

```
// C code
int increment(int n) {
    return n + 1;
}
```

I asked Claude Opus 4.5 (extended thinking), Gemini 3 Pro, and ChatGPT 5.2 to translate this code to Python, and they all produced the same result:

```
# Python code
def increment(n: int) -> int:
    return n + 1
```

It is subtle, but the semantics have changed. In Python, signed integer arithmetic has arbitrary precision. In C, overflowing a signed integer is undefined behavior: it might wrap, might crash, [might do literally anything](https://thephd.dev/c-undefined-behavior-and-the-sledgehammer-guideline). In Python, it’s well defined: you get a larger integer. None of the leading foundation models caught this difference. Why not? It depends on whether they were trained on examples highlighting this distinction, whether they “remember” the difference at inference time, and whether they consider it important enough to flag.

There exist an infinite number of Python programs that would behave identically to the C code for all valid inputs. An LLM is not guaranteed to produce any of them.

In fact, it’s impossible for an LLM to exactly translate the code without knowing how the original C developer *expected* or *intended* the C compiler to handle this edge case. Did the developer know that the inputs would never cause the addition to overflow? Or perhaps they inspected the assembly output and concluded that th...