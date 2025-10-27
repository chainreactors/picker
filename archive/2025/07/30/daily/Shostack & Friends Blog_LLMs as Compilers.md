---
title: LLMs as Compilers
url: https://shostack.org/blog/llms-as-compilers/
source: Shostack & Friends Blog
date: 2025-07-30
fetch_date: 2025-10-06T23:49:55.977037
---

# LLMs as Compilers

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. LLMs as Compilers

Shostack + Friends Blog

# LLMs as Compilers

What if we think about LLM coding as if it’s a compiler stage?
![a visaulaization with three sections. on the left is text in paragraphs, in the middle is computer code and on the right is binary. Each has a graceful transition into the next with little robots assisting.](/images/blog/img/2025/llms-as-compilers@2x-1000w.png)

I want to explore the relationship of LLMs to compilers, inspired
in part by articles like [my AI skeptic
friends are all nuts](https://fly.io/blog/youre-all-nuts/), in part by
a lot of time spent exploring LLMs for threat
modeling. (There, I feel like I should have more useful things to
say before saying them.) And by the way, by “experimenting,” I
don’t mean just vibe-threat-modeling (although I’ve done some),
but rather carefully constructing prompts, feeding them to
multiple engines, scoring the results, and evaluating the
evaluations.1 That’s a slow process, but I still feel
there’s could be something meaningful, if we can get there. The
other inspiration was talking with a friend who builds static analysis tools
a very large firm with a famously high bar for
developer interviews. He mentioned that people are now checking in
their LLM prompts.

In a sense, turning human readable code
into machine executable code is what a compiler does, and that’s
very similar to one way we use LLMs. You give it a prompt, and it
turns it into code, which a later stage, either a reviewer or a
compiler, tells you is shit.

When computers were new, compilers were actually pretty bad at
writing code, when compared to smart, dedicated people. In fact,
the people didn’t need to be that smart to outdo compilers into
the 90s. (If you go back and read “[Smashing the stack for fun and
profit](https://phrack.org/issues/49/14),”2 you’ll see the concept of nop sleds, because compilers
would just insert strings of no-ops to make writing exploits
easier — amonst other reasons.) The only people who
can actually think about machine code these days work in either
compilers (and runtimes and chip development) or exploit
development.3

There’s a very longstanding aspiration to make programming
languages that look like natural languages. You can see this in
languages like SQL, but even more in the many programming
languages named “[English](https://esolangs.org/wiki/English).” These languages have
not been incredibly successful at their goal of letting anyone
program, probably because language syntax has not been as big a
barrier as thinking about algorithms, edge cases, and other
elements of programming.

Today, LLMs are pretty bad at writing code. They’re better where
they have more training data, such as Python, and worse where they
have less data or the data isn’t consistent. (This is a [particular
problem with Swift](https://daringfireball.net/linked/2025/06/07/swift-6-llms), because Apple has updated Swift roughly
annually, which means that the training data is both scarce and
conventions change.) Before reading Tom’s “all nuts” essay, I’d have said they’re better when you give them prompts
that look like specifications. I know folks who like to write a
long comment explaining what a function does, then feed the
comment to an LLM for code that matches it. (I personally find the
pattern far preferable to having an LLM in my IDE, because it
wants to intrude when it thinks it has something to say, which is
often when I’m deep in thought.)

When we think about LLMs as compilers, we could design them to
compile directly to some machine code, such as WASM or x86. Or can consider them
compiling from a high level language, such as English, to an
intermediate language like Python, to be further compiled. I think
this is a more useful frame, and we can start to think about
linters and other such tools to work on both English and high
level programming languages. We get other values from using
intermediate languages, especially if we use languages that give
us various safety properties, such as Rust or Go. And language
design always includes a tradeoff of pickiness versus usability
(I’ve been [saying for 20 years](https://shostack.org/archive/2004/10/ranum-on-the-root-of-the-problem/) that I don’t like
GCC’s choice of tradeoff.) With LLMs as compilers, we
might make
different tradeoffs in how GCC works, or we might even design new
languages with a goal of being easy to use in the LLM-driven use
cases.

We can also think about how to build different security
analysis techniques. For example, with Cursor, many people are starting to create
“design” and “development” documents which specify how a system is
designed. We might ask “is threat modeling a linter on the design
documents,” or “what parts of threat modeling might be linters on
design documents?” Can we consider “[falsehoods programmers believe](https://github.com/kdeldycke/awesome-falsehood)” as a
set of test cases to be run?

I’ve been using this model of LLMs as additional compiler stages for a bit, and
finding it evocative and interesting.

---

#### Footnotes

1. Along the lines of [ACSE-Eval:
   Can LLMs threat model
   real-world cloud
   infrastructure?](https://arxiv.org/abs/2505.11565), and
   I hope to say more about
   that paper. Short form:
   they’re doing what I
   hope to be able to do.
2. Jesus, Google is [bad](https://www.google.com/search?q=smashing+the+stack+for+fun+and+profit&sca_esv=1f1865b5582e1c86&ei=8vFWaObhGcLE0PEPzISxiAI&ved=0ahUKEwjmosXqioOOAxVCIjQIHUxCDCEQ4dUDCBA&uact=5&oq=smashing+the+stack+for+fun+and+profit&gs_lp=Egxnd3Mtd2l6LXNlcnAiJXNtYXNoaW5nIHRoZSBzdGFjayBmb3IgZnVuIGFuZCBwcm9maXQyDRAAGIAEGEMYxwMYigUyBhAAGBYYHjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCBAAGIAEGKIEMgUQABjvBTIIEAAYgAQYogRI0AxQhARYtQpwAXgAkAEAmAFToAGgA6oBATe4AQPIAQD4AQGYAgegAsIDwgIFEAAYgASYAwCIBgGSBwE3oAeUJ7IHATe4B8IDwgcFNS4zLTLIByE&sclient=gws-wiz-serp) at authoritative
   sources. The Phrack article isn’t on page 1.
3. For fun, next time you meet someone claiming to be a “full stack
   engineer,” ask them to explain the most common MOV instructions and how a chip implements them.

Originally published by Adam on 29 Jul 2025

Categories:
  [software](/blog/category/software)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://s...