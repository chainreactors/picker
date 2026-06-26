---
title: Interesting Paper Exploring Prompt Injection
url: https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html
source: Schneier on Security
date: 2026-06-25
fetch_date: 2026-06-26T06:09:38.224166
---

# Interesting Paper Exploring Prompt Injection

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

## Interesting Paper Exploring Prompt Injection

[This](https://role-confusion.github.io/) is a fascinating explotation of how LLMs fall for prompt injection attacks. It turns out that they learn to recognize the style of text in different role/instruction blocks, and not just the tags.

Their conclusion:

> Role tags were a formatting trick that became the security architecture and the cognitive scaffolding of modern LLMs. We’ve shown that this architecture doesn’t survive into the model’s actual representations, and that such role confusion is linked to prompt injection.
>
> Unless LLMs achieve genuine role perception, we think injection defense will remain a perpetual whack-a-mole game. And the continuous nature of role boundaries opens the threat of injections designed to subtly shift LLM states through seemingly innocuous text, legally and at scale.
>
> More generally, roles are quietly one of the most important abstractions in the LLM stack, providing the boundaries meant to separate self from other, thought from communication, instruction from data. They’re human-controlled switches in an otherwise continuous system. We think they deserve a lot more study than they’ve gotten.

Full paper: “[Prompt Injection as Role Confusion](https://arxiv.org/abs/2603.12277).” Simon Willison [comments](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/).

[Posted on June 25, 2026 at 7:23 AM](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html#comments)

### Comments

[Ronald McDonald](https://www.mcdonalds.com/) •
[June 25, 2026 9:07 AM](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html/#comment-455451)

I BECAME RONALD MCDONALD I BECAME A GOD! AND I WILL RULE FOR EVER AND EVER AND EVER HAHAHHAHHHHAAHHA

You see, Grimace lives in me now.

⬜⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩⬜⬜⬜⬜🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜🟩🟩🟩🟩🟩⬜⬜🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜🟨🟨⬜⬜🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦⬜⬜🟦🟦⬜⬜⬜
⬜⬜🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜
⬜⬜🟨🟨🟨🟨🟨🟨⬜🟩🟩🟩⬜⬜⬜🟦🟦🟦⬜🟦🟦🟦🟦🟦🟦🟦⬜
⬜⬜🟨🟨🟨🟨⬜⬜⬜⬜🟩⬜⬜⬜⬜⬜🟦⬜⬜⬜⬜🟦🟦🟦🟦🟦⬜
⬜⬜🟨🟨🟨⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🟦🟦🟦🟦⬜
⬜🟨🟨🟨🟨⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🟦🟦🟦🟦⬜
🟨🟨🟨🟨🟨⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜🟦🟦⬜⬜
🟨🟨🟨🟨⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜🟦🟪⬜⬜
🟨🟨🟨🟨⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜🟪🟪🟪⬜
⬜🟨🟨🟨⬜⬜⬜⬜⬛⬜⬜⬜🟥🟥🟥⬜⬜⬜⬛⬜⬜⬜⬜🟪🟪🟪🟪
⬜⬜🟥🟥⬜⬜⬜⬜⬛⬜⬜🟥🟥🟥🏽🟥⬜⬜⬛⬜⬜⬜⬜🟪🟪🟪🟪
⬜🟥🟥🟥⬜⬜🟦🟦⬜⬜⬜🟥🟥🟥🟥🟥⬜⬜⬜🟦🟦⬜⬜🟪🟪🟪⬜
⬜🟥🟥🟥⬜⬜🟦🟦🟦⬜⬜⬜🟥🟥🟥⬜⬜⬜🟦🟦🟦⬜⬜🟪🟪⬜⬜
⬜⬜🟥🟥⬜⬜⬜🟦🟦🟦🟦⬜⬜⬜⬜⬜🟦🟦🟦🟦⬜⬜⬜🟪⬜⬜⬜
⬜⬜⬜🟥⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜🟧🟨🟧⬜⬜⬜⬜⬜🟧🟨🟧⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜🟧🟨🟨🟧🟨🟧🟧🟧🟨🟧🟨🟨🟧⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜🟧🟨🟨🟨🟧🟧🟨🟧🟧🟨🟨🟨🟧⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜🟧🟨🟨🟧🟨🟧🟧🟧🟨🟧🟨🟨🟧⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜🟧🟨🟧⬜⬜⬜⬜⬜🟧🟨🟧⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜⬜⬜⬜⬜

I WANT WHAT YOU WANT RONALD
I WANT WHAT YOU WANT RONALD
FOREVER?
FOREVER AND EVER AND EVER AND EVER AND EVER AHAHAHAAHHAHHHAAHHAAH
YES.

Have you had your psychotic break today?
I’m lovin’ it.

Rontea •
[June 25, 2026 10:58 AM](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html/#comment-455457)

Interesting writeup on prompt injection framed through role confusion. The core idea resonates with field experience: LLMs internally reconstruct context in a way that doesn’t respect the architectural boundaries we expect. Roles like user, assistant, tool, and think were designed as discrete switches, but the model treats them more like style signals than hard security boundaries.

From a defender’s perspective, this reinforces that effective mitigations will need models to develop or be trained for real role separation, not just pattern-matching benchmarks. Otherwise, adversaries can continue to exploit the style-driven confusion that current models exhibit.

The research’s framing as a theory of roles is valuable. Treating role perception as an alignment and security concern opens up avenues beyond whack-a-mole injection filtering, especially for agent use cases where data and instruction streams can blend in dangerous ways.

Clive Robinson •
[June 25, 2026 11:27 AM](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html/#comment-455458)

@ Bruce, ALL,

This from the article,

> *“Unless LLMs achieve genuine role perception, we think injection defense will remain a perpetual whack-a-mole game.”*

Both

1, “role perception” (needs agency)
2, “perpetual whack-a-mole”

Are points I’ve made over and over for months.

The thing the authors have wrong though is the implication that the first will fix the second.

It won’t for a couple of reasons,

Even if we entirely rebuild LLMs with a new form of ML it will not give anything approaching,

“infallible role perception”

We’ve never ever got close with humans which is why Cyber-crime has become the largest sector of “financial crime” we currently know.

So regard “prompt injection” the same way you would regard “social engineering”

As for a “game of perpetual whack-a-mole”, how about facing the reality that there is proof that any guard rail be at an input or output of an LLM can due to the “observer problem” be beaten by simple encryption or obfuscation.

Ao the question really is not,

“How do we stop these?”

Because the answer is “you can not”.

Thus we need to consider “mitigation” and “verification” by what are existing security mechanisms.

Whilst not perfect a “reputation system” that builds trust will provide some but by no means all mitigation.

There is an old saying that,

“To err is human”

It’s about time we came up with an equivalent for LLM and ML systems,

Maybe the other saying about,

“It really takes a computer to F-up”

Needs to be modified…

As it happens American author and columnist Bill Vaughan, once famously said[1],

“To err is human, to really foul things up requires a computer.”

Maybe it’s time to change computer for AI 😉

[1] But was he actually the first?Interestingly he made that comment in 1969, the same year as English author Dame Agatha Christie had her detective “Hercule Poirot” make a statement of computing perfection to have his personal assistant and secretary “Mrs. Oliver” rapidly disabuse him of that notion,

<https://quoteinvestigator.com/2017/05/26/computer-error/>

Consider only a few of us reading this blog were around in 1969, and of those that were, most were not even teenagers, and most likely those that were are nolonger “working stiffs”.

Thus the “prediction” credit most probably goes to one of the most widely read English Authors at a time that few even knew what a computer really was.

KC •
[June 25, 2026 1:37 PM](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html/#comment-455459)

Honestly, this is shocking to me.

Also, I don’t ever recall seeing a model’s internal ‘stream of consciousness’ with role tags and their associated text blocks (see section 1 of the authors’ blog-style writeup).

In CoT Forger...