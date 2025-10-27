---
title: LLM Coding Integrity Breach
url: https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html
source: Schneier on Security
date: 2025-08-15
fetch_date: 2025-10-07T00:49:11.954240
---

# LLM Coding Integrity Breach

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## LLM Coding Integrity Breach

[Here’s](https://sketch.dev/blog/our-first-outage-from-llm-written-code) an interesting story about a failure being introduced by LLM-written code. Specifically, the LLM was doing some code refactoring, and when it moved a chunk of code from one file to another it changed a “break” to a “continue.” That turned an error logging statement into an infinite loop, which crashed the system.

This is an [integrity failure](https://www.computer.org/csdl/magazine/sp/2025/03/11038984/27COaJtjDOM). Specifically, it’s a failure of processing integrity. And while we can think of particular patches that alleviate this exact failure, the larger problem is much harder to solve.

Davi Ottenheimer [comments](https://www.flyingpenguin.com/?p=71603).

Tags: [AI](https://www.schneier.com/tag/ai/), [integrity](https://www.schneier.com/tag/integrity/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on August 14, 2025 at 7:08 AM](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html) •
[7 Comments](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html#comments)

### Comments

yet another bruce •
[August 14, 2025 9:42 AM](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html/#comment-447178)

I am a bit surprised that this team relied on a manual code review to validate that the refactoring was correct. A set of automated tests with good coverage on both the old and new code seems like a more robust way to check correctness. Limiting the manual review to a few dozen lines that changed and that missed test coverage would make the problem more tractable.

It would not surprise me someone has already made use of AI to automate the process of generating a good suite of tests.

David Leppik •
[August 14, 2025 1:30 PM](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html/#comment-447184)

@yet another bruce: chances are, the AI also generated (or updated) a bunch of tests. That’s standard practice. But maybe not for every error handling case.

Tests for error handling code written by humans is often not worth the cost/benefit tradeoff because it’s easy to read but the tests can (sometimes!) be convoluted and harder to read/trust. Humans and LLMs are both really good at writing tests that contain subtle bugs that short-circuit the intended logic testing.

LLMs are really good at doing huge refactors. By “really good” I mean doing hundreds or thousands of line changes with over 99% accuracy. And by over 99% I mean if there are 500 lines of changes there are probably one or two bugs. But good luck finding them!

Just think of the seductive power of that. A refactoring that would take you a week gets written in under a minute, and it seems reasonable to think that you would spot any bugs in under an hour.

Davi Ottenheimer’s solution is to have the human at the keyboard responsible and not blame the AI. That’s fair.

The tool developer’s solution is to let the AI do copy/paste, to make these of transcription errors less likely. That’s also fair.

Neither is a panacea. There’s always a trade-off between rigorous testing + analysis and getting features out the door. In most software domains, the bias is toward getting features out the door. LLMs just supercharge this, and we need to develop new habits to compensate.

Clive Robinson •
[August 14, 2025 2:36 PM](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html/#comment-447187)

@ David Leppik, yet another bruce,

You note,

> “In most software domains, the bias is toward getting features out the door. LLMs just supercharge this, and we need to develop new habits to compensate.”

Do you want to bet on the probability that any “new habits” will not be allowed in any way to reduce the “getting features out the door”. After all what’s a little “technical debt” build up to management…

Likewise do you want to bet on the probability that any “new habits” will be as optimised to the maximum possible to “supercharge” the LLM turning out code (any code).

Thus how free of vulnerabilities the results of “new habits” will be?

I need to note that my past experience of management and code reviews that I’ve mentioned before is to go “hell to the max” on making a technical debt tsunami of epic proportions.

So my view is the “new habits” in all probability, will in no way, make the code produced any less vulnerability free.

As for “tests” the first prerequisite for that is a full formal specification not a wish list subject to programmer whims and choices.

Further that generation of tests should be an entirely separate team to the developers.

Which with current LLM and ML systems is in effect impossible because the LLM output becomes the ML input in various ways so they will almost certainly get “coupled”.

not important •
[August 14, 2025 5:29 PM](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html/#comment-447190)

AI designs antibiotics for gonorrhoea and MRSA superbugs

=Artificial intelligence has invented two new potential antibiotics that could kill drug-resistant gonorrhoea and MRSA, researchers have revealed.
The drugs were designed atom-by-atom by the AI and killed the superbugs in laboratory and animal tests.

The two compounds still need years of refinement and clinical trials before they could be prescribed.

But the Massachusetts Institute of Technology (MIT) team behind it say AI could start a
“second golden age” in antibiotic discovery.

the MIT team have gone one step further by using generative AI to design antibiotics in
the first place for the sexually transmitted infection gonorrhoea and for potentially-
deadly MRSA (methicillin-resistant Staphylococcus aureus).

> Their study interrogated 36 million compounds including those that either do not exist or have not yet been discovered.

Scientists trained the AI by giving it the chemical structure of known compounds
alongside data on whether they slow the growth of different species of bacteria.

The AI then learns how bacteria are affected by different molecular structures, built of
atoms such as carbon, oxygen, hydrogen and nitrogen.

> Two approaches were then tried to design new antibiotics with AI. The first identified a
> promising starting point by searching through a library of millions of chemical
> fragments, eight to 19 atoms in size, and built from there. The second gave the AI free
> rein from the start.=

Rich Seidner •
[August 15, 2025 12:07 PM](https://www.schneier.com/blog/archives/2025/08/llm-coding-integrity-breach.html/#comment-447202)

I’ve been a Schneier fan since God knows when …

… but Clive Anderson’s comments, by themselves, are worth the read. Anyone who can mention Claude Shannon and Christiaan Huygens in one response to a query is fabulously more educated (and fun) than I’ll ever be.

Thank you, Cli...