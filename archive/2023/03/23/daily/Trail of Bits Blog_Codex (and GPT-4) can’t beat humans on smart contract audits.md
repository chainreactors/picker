---
title: Codex (and GPT-4) can’t beat humans on smart contract audits
url: https://blog.trailofbits.com/2023/03/22/codex-and-gpt4-cant-beat-humans-on-smart-contract-audits/
source: Trail of Bits Blog
date: 2023-03-23
fetch_date: 2025-10-04T10:21:25.126956
---

# Codex (and GPT-4) can’t beat humans on smart contract audits

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Codex (and GPT-4) can’t beat humans on smart contract audits

Artem Dinaburg, [Josselin Feist](https://x.com/montyly), Riccardo Schirone

March 22, 2023

[blockchain](/categories/blockchain/), [machine-learning](/categories/machine-learning/)

Is artificial intelligence (AI) capable of powering software security audits? Over the last four months, we piloted a project called Toucan to find out. Toucan was intended to integrate OpenAI’s Codex into our Solidity auditing workflow. This experiment went far beyond writing “where is the bug?” in a prompt and expecting sound and complete results.

Our multi-functional team, consisting of auditors, developers, and machine learning (ML) experts, put serious work into prompt engineering and developed a custom prompting framework that worked around some frustrations and limitations of current large language model (LLM) tooling, such as working with incorrect and inconsistent results, handling rate limits, and creating complex, templated chains of prompts. At every step, we evaluated how effective Toucan was and whether it would make our auditors more productive or slow them down with false positives.

The technology is not yet ready for security audits for three main reasons:

1. The models are not able to reason well about certain higher-level concepts, such as ownership of contracts, re-entrancy, and fee distribution.
2. The software ecosystem around integrating large language models with traditional software is too crude and everything is cumbersome; there are virtually no developer-oriented tools, libraries, and type systems that work with uncertainty.
3. There is a lack of development and debugging tools for prompt creation. To develop the libraries, language features, and tooling that will integrate core LLM technologies with traditional software, far more resources will be required.

Whoever successfully creates an LLM integration experience that developers love will create an incredible moat for their platform.

The above criticism still applies to GPT-4. Although it was released only a few days before the publication of this blog post, we quickly ran some of our experiments against GPT-4 (manually, via the ChatGPT interface). We conclude that GPT-4 presents an incremental improvement at analyzing Solidity code. While GPT-4 is considerably better than GPT-3.5 (ChatGPT) at analyzing Solidity, it is still missing key features, such as the ability to reason about cross-function reentrancy and inter-function relationships in general. There are also some capability regressions from Codex, like identification of variables, arithmetic expressions, and understanding of integer overflow. It is possible that with the proper prompting and context, GPT-4 could finally reason about these concepts. We look forward to experimenting more when API access to the large context GPT-4 model is released.

We are still excited at the prospect of what Codex and similar LLMs can provide: analysis capabilities that can be bootstrapped with relatively little effort. Although it does not match the fidelity of good algorithmic tools, for situations where no code analysis tools exist, something imperfect may be much better than having nothing.

Toucan was one of our first experiments with using LLMs for software security. We will continue to research AI-based tooling, integrating it into our workflow where appropriate, like [auto-generating documentation](https://github.com/crytic/slither/releases/tag/0.9.2) for smart contracts under audit. AI-based capabilities are constantly improving, and we are eager to try newer, more capable technologies.

## We want AI tools, too

Since we like to examine transformational and disruptive technologies, we evaluated OpenAI’s Codex for some internal analysis and transformation tasks and were very impressed with its abilities. For example, a recent intern integrated Codex within Ghidra to [use it as a decompiler](https://github.com/trailofbits/Codex-Decompiler). This inspired us to see whether Codex could be applied to auditing Solidity smart contracts, given our expertise in tool development and smart contract assessments.

Auditing blockchain code is an acquired skill that takes time to develop (which is why [we offer apprenticeships](https://blog.trailofbits.com/2022/08/12/the-road-to-the-apprenticeship/)). A good auditor must synthesize multiple insights from different domains, including finance, languages, virtual machine internals, nuances about ABIs, commonly used libraries, and complex interactions with things like pricing oracles. They must also work within realistic time constraints, so efficiency is key.

We wanted Toucan to make human auditors better by increasing the amount of code they could investigate and the depth of the analysis they could accomplish. We were particularly excited because there was a chance that AI-based tools would be fundamentally better than traditional algorithmic-based tooling: [it is possible to learn undecidable problems to an arbitrarily high accuracy](https://www.ics.uci.edu/~rickl/publications/1996-icml.pdf), and program analysis [bumps against undecidability all the time](https://en.wikipedia.org/wiki/Rice%27s_theorem).

We initially wanted to see if Codex could analyze code for higher-level problems that could not be examined via static analysis. Unfortunately, Codex did not provide satisfactory results because it could not reason about higher-level concepts, even though it could explain and describe them in words.

We then pivoted to a different problem: could we use Codex to reduce the false positive rate from static analysis tools? After all, LLMs operate fundamentally different from our existing tools. Perhaps they provide enough signals to create new analyses previously untenable due to unacceptable false positives. Again, the answer was negative, as the number of failures was high even in average-sized code, and those failures were difficult to predict and characterize.

Below we’ll discuss what we actually built and how we went about assessing Toucan’s capabilities.

## Was this worth our time?

Our assessment does not meet the rigors of scientific research and should not be taken as such. We attempted to be empirical and data-driven in our evaluation, but our goal was to decide whether Toucan warranted further development effort—not scientific publication.

At each point of Toucan development, we tried to assess whether we were on the right track. Before starting development, we manually used Codex to identify vulnerabilities that humans had found in specific open-source contracts—and with enough prompt engineering, Codex could.

After we had the capability to try small examples, we focused on three main concepts that seemed within Codex’s capability to understand: ownership, re-entrancy, and integer overflow. (A quick note for the astute reader: Solidity 0.8 fixed most integer overflow issues; developing overflow checks was an exercise in evaluating Codex’s capability against past code.) We could, fairly successfully, identify vulnerabilities regarding these concepts in small, purpose-made examples.

Finally, as we created enough tooling to automate asking questions against multiple larger contracts, we began to see the false positive and hallucination rates become too high.  Although we had some success with ever more complex prompts, it was still not enough to make Toucan viable.

Below are some key takeaways from our experience.

**Codex does not fully grasp the higher-level concepts that we would like to ask about, and explaining them via complex prompt engineering does not always work or produce reliable results.** We had originally intended to ask questions about higher-level concepts like ownership, re-entrancy, fee distribution, how pricing oracles are used, or even automated market makers (AMMs). Cod...