---
title: Lessons from the OpenAI/HuggingFace AI Security Incident
url: https://shostack.org/blog/lessons-from-openai-huggingface-ai-security/
source: Shostack & Friends Blog
date: 2026-07-27
fetch_date: 2026-07-28T04:59:17.515984
---

# Lessons from the OpenAI/HuggingFace AI Security Incident

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about)
  + [Shostack + Associates](/about)
  + [Adam Shostack](/about/adam)
  + [Our Partners](/partners)
* [Services](/training)
  + [Training](/training)
  + [Accelerator](/secure-design-accelerator)
  + [Speaking Requests](/speaking)
  + [Consulting](/consulting)
* [Resources](/resources)
  + [Overview](/resources)
  + [Threat Modeling](/resources/threat-modeling)
  + [Books](/books)
  + [Games](/tm-games)
  + [Cyber Public Health](/resources/cyber-public-health)
  + [Lessons Learned](/resources/lessons)
  + [Videos](/resources/videos)
  + [Whitepapers](/resources/whitepapers)
* [Blog](/blog)
* [Contact](/contact)

1. [Shostack + Associates](/)
2. [Blog](/blog)
3. Lessons from the OpenAI/HuggingFace AI Security Incident

Shostack + Friends Blog

# Lessons from the OpenAI/HuggingFace AI Security Incident

Adam Shostack, Shostack + Associates

The big takeaways from the OpenAI incident are over-reliance on benchmarks, anthropomorphization and volume.
![A robot sitting at a desk hacking. It wears a black hoodie with an aliens-style face hugger attached to it](/images/blog/img/2026/openai-and-huggingface-hacking-1000w.jpeg)

The very big news was that an OpenAI model hacked
Huggingface. Raphael Satter has a fascinating story, [. OpenAI’s agent spent days hacking a company, but sources say
OpenAI did not notice for a week](https://www.reuters.com/business/its-ai-agent-spent-days-hacking-company-sources-say-openai-did-not-notice-week-2026-07-24/), and I want to start with a few items from that article.

* Let’s start with the headline: “OpenAI didn’t notice for a week.” Now,
  I don’t run a highfalutin’ AI Lab, but according to [Gadi Evron’s Linkedin post](https://www.linkedin.com/posts/gadievron_my-analysis-from-hosting-hugging-face-at-share-7486340715514437632-Xs-b/), the model went $100,000 over budget
  in token consumption (although that might be the incident response
  cost not the cost of the model running exploit gym.)
* The next thing I want to comment on is “an agent left notes apparently for future versions of
  itself...laid out instructions for how agents could free
  themselves from OpenAI’s internal constraints.” Why would someone assume
  that’s future versions, rather than the model taking operational
  notes to ensure that the same model doesn’t lose track in limited
  context windows? The reflexive anthropomorphization is important
  here.
* ”Four people familiar with OpenAI’s model-training practices say
  the company often runs several different model ​evaluations at
  the same time, all of which operate at high speeds and generate
  such enormous amounts of data that employees sometimes struggle
  to keep up.” That’s fascinating in two ways: First, they run so many things that no human
  can make sense of them, and so apparently focus on a
  score on a benchmark as the relevant thing. (Otherwise, you’d
  either run fewer evaluations at once, or hire more people to look
  at the results in detail.) Second, they’re not using LLMs to parse
  the output into smaller things, possibly because they rely fully
  on the evaluation tool, and possibly because they know that LLMs
  are bad at summarization.

Despite the popular characterization, the model didn’t “escape.” The model
stayed on OpenAI’s servers, running commands elsewhere. (This
point was made by Ramez Naam.)

It’s also worth noting that the apparent goal was to [steal the answers to the ExploitGym
benchmark](https://simonwillison.net/2026/Jul/22/openai-cyberattack/). We’ll come back to that.

## Takeaways

Anthropomorphization, giving the model human attributes and
motivations, underlies the characterization that the notes were
for “future versions of itself.” They could have been as easily
characterized as “virtual post-its to overcome limited context windows.”
The aspiration that these models are human bleeds into
thinking in ways that distract us from being able to analyze what
we see.

Volume overwhelms everything, especially judgment.

Volume overwhelms everything, especially judgment. The team at
OpenAI either can’t or won’t slow down to look at the output of
these systems. Now, maybe, that’s the right call? Velocity is its
own reward? That’s certainly possible - maybe small shifts in
position on benchmarks herds customers onto those models, and so a
win on the benchmark is a revenue driver. (If only the AI folks
knew about the complexity of gradient-climbing as a strategy?
🤷) But more seriously: OpenAI gets business value out of using
its technology, learning where it adds value, and trumpeting that
as a new value prop for LLMs. Apparently
that’s not... parsing the output of its tools.

The possibility of stealing test answers may be the ultimate expression of Goodhart’s law.

Benchmarks are useful when they measure what matters. As far back
as 1975, Goodhart wrote “Any observed statistical
regularity will tend to collapse once pressure is placed upon it
for control purposes,” or as Marilyn Strathern memorably rephrased
it, “When a measure becomes a target, it ceases to be a good
measure.” The possibility of stealing test answers may be
the ultimate expression of Goodhart’s law.

But moving beyond OpenAI, most organizations are not competing on
the basis of those benchmarks, they’re competing on
value delivered to customers.

Understanding the value of an improvement, rather than focusing on
a single benchmark, is a crucial part of engineering. Engineering
is always about tradeoffs, not “maxxing.”

We see these issues: anthropomorphization, overreliance on
benchmarks, and aspiration-driven thinking all the time as we help clients navigate how to use
LLMs in threat modeling, but they are really about LLMs. They
extend far beyond threat
modeling. That's why we included two (anthropomorphization and
over-reliance) in version 1 of [the PHANTOM-B model](/resources/whitepapers). Who knows,
maybe a future version will need benchmarkmaxxing as a threat?

## Other commentary:

* Neil Wyler (aka Grifter) wrote an excellent article, [OpenAI
  gave its model a test, it broke out of its sandbox and hacked
  Hugging Face to steal the answers](https://coalfire.com/the-coalfire-blog/openai-gave-its-model-a-test-it-broke-out-of-its-sandbox-and-hacked-hugging-face-to-steal-the-answers) covering speed, the
  two-sided nature of guardrails, and regulation threats.
* Laurie Voss has a philisophically interesting essay, [Did OpenAI hack Hugging Face or didn't they?](https://seldo.com/posts/did-openai-hack-hugging-face-or-didnt-they/) on the legal question of “could anyone be held accountable?”
* The Cloud Security Alliance and partners released [Hugging Face Incident Initial Post-Mortem](https://cloudsecurityalliance.org/artifacts/hugging-face-ciso-post-mortem).
* Michael Taggart, in [Shiny, Sharp Objects](https://taggart-tech.com/sharp-objects/), flags Claude tripped guardails as asked to “analyze this dataset.” I haave to ask: that’s how you respond to a breach, rather than, say, asking it for either pointers to tools that’ll algorithmically analyze the data, or having it create such tooling for you? [Updated: just asking to analyze did not trigger the guardrails, as an earlier version of this post took from Taggart’s post.]

### PHANTOM-B at Black Hat

I'm presenting PHANTOM-B on Wednesday at Black Hat and reprising it on Saturday in the AppSec Village at DEF CON. Check out [our full schedule](https://shostack.org/blackhat) for details and [read the whitepaper ahead of the talk](/resources/whitepapers)!

Image by Gemini: “draw an 8x3 image of robot in a black hoodie with an aliens-style
face hugger attached to it; the robot should be sitting at a desk
hacking; redo the colors in Watercolor style impressionist colorism;
redo in cinematic volumetric light, with #5253a4 blue as a theme
color; make it lighter.”

Originally published by Adam on 27 Jul 2026

...