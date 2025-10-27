---
title: Mansplaining your threat model, as a service
url: https://shostack.org/blog/mansplaining-your-threat-model-as-a-service/
source: Shostack & Friends Blog
date: 2025-08-27
fetch_date: 2025-10-07T00:48:13.076927
---

# Mansplaining your threat model, as a service

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
3. Mansplaining your threat model, as a service

Shostack + Friends Blog

# Mansplaining your threat model, as a service

Everyone wants robots to help with threat models. How’s that working out?
![a photograph of a robot standing at a whiteboard, trying to explain a crazy complicated diagram to a group of people seated around a conference table.  the faces of the people at the table look bored and skeptical](/images/blog/img/2025/mansplaining-your-threat-model-as-a-service-1000w.png)

This is the second part of a short series. The first post looks at
[threat modeling tooling](https://shostack.org/blog/threat-modeling-tools/) more
broadly; this one is focused on LLMs in threat modeling.

It seems like you can’t turn around without another experiment in
augmenting or replacing threat modeling with LLM tricks. It’s easy
to fall into a Pollyanna or a Cassandra camp on this. Extremism
doesn’t help us here. We should be both curious and cautious. It
would be pollyannish to not worry about accuracy and completeness. Despite those, when we
compare LLM TM to not threat modeling at all, or having untrained
people threat model, using an LLM might deliver product
security improvements.

**The key question is how can tooling effectively improve the security of
delivered systems**?

Let me start with accuracy. I am
skeptical that we’re going to get decent threat modeling from
chatbots anytime soon. There are a number of problems, including
quality issues with training data and context windows/attention
algorithms. Even with good structures, a lot of what’s called
“intuition” in humans seems to be pattern recognition, and the patterns
recognized may not align with the things that an LLM statistical
model draw out. There’s also an anti-pattern: produccing tedius
pablum that no one wants to read.

If people do read the output, we should ask if they can effectively
judge it. That requires some skill in doing threat modeling work. LLMs are excellent at sounding confident, thus the title
of this post. People tend to think that others wouldn’t speak
confidently if they’re not confident, and so LLM-displayed
confidence is persuasive. Worse, LLM output is generally tedious
and so people get bored reading it. It’s a dangerous combination
when we ask if people can evaluate it effectively.

In [the first of this paired set](https://shostack.org/blog/threat-modeling-tools/) of posts, I presented the following model of chatbots:

1. Standard chatbots
2. Standard chatbots with structured prompts, used manually
3. Security chatbots ([Deep Hat](https://www.deephat.ai/))
4. Security chatbots, structured
   prompts ( StrideGPT)
5. One time investment in RAG (etc) to provide structure
6. Ongoing product development effort

A
relatively straightforward way to start is with a tuned set of
prompts, managed in a test system with evaluations is going to do
way better at analysis than randomly chatting with a bot. (The
chatting with a bot has its charms, including focusing our
attention in a way that a report doesn’t have.) And if the chat is
in a tool, it’s easier to use techniques like setting a low
temperature to drive consistent answers. My skepticism over chatbots extends to the deeper LLM application
patterns that use RAG, but those may change the equation pretty dramatically.

We know that LLMs are very vulnerable to
“pertubation attacks.” These use minor changes, not meaningful to
humans, to dramatically alter the LLM’s behavior. These are
important because interacting in models 1-4 inevitably invite
accidental pertubations. Managing that requires that you develop
tools, including evaluations, to test the tooling. It’s not a
small investment.

It's worth looking at this academic paper, [ACSE-Eval: Can
LLMs threat model real-world
cloud
infrastructure?](https://arxiv.org/abs/2505.11565v2). They
asked what's involved in
assessing an LLM, and likely
represents a person-year or
more of effort. Some of that
effort is re-usable, but it
colors my thinking on the
chatbot approaches to LLM
threat modeling.

Adding RAG and tuning may dramatically improve the reliability of
LLM-driven threat modeling, but “dramatically” is not a synonym for
“sufficiently.” But a recent paper, [Potemkin Understanding in Large Language
Models](https://arxiv.org/abs/2506.21521v1) raises a fascinating threat: “these benchmarks are only valid
tests if LLMs misunderstand concepts in ways that mirror
human misunderstandings. Otherwise, success on benchmarks
only demonstrates potemkin understanding: the illusion of
understanding driven by answers irreconcilable with how
any human would interpret a concept.” It’s worth asking if that
model applies to LLM-driven threat modeling? I think it
does. If it does, we need to ask what that
means for when we use LLMs, how we evaluate their output,
and what remains with the people, and my answer is, I
don’t know.

My intuition is that as long as LLMs are “language models”, rather than “concept
models,” they’ll be less good at threat modeling, and
we’ll soon find better understanding of the limits of chain-of-thought, plan,
expose-your-reasinoning and other techniques for helping
LLMs get better at things that require more than small
token prediction. On the other hand, my intuition would
not have anticipated all the things LLMs can do with token prediction.

As you get into a build-buy decisions about LLM development, the
key question is “do we get enough overall business advantage from
developing our own security LLM, versus other LLM or product work
we could do?” When you develop (or tune) an LLM, you have the advantage
that you can use your own threat models as part of your training
data. This is most powerful if you have a lot of great threat
models that you want to use to inform future work. Unfortunately,
many orgs do not have a great collection of threat models.

If you get tremendous advantage from building your own LLM, then by
all means, go for it. Otherwise, there’s a lot of fascinating
commercial innovation. Exciting developments I’ve seen recently include [Seezo](https://seezo.io/),
who has a very interesting approach to minimizing halucinations,
[Prime Security](https://www.primesec.ai/), who I haven’t spoken to but won
the BlackHat Startup competition, and my colleagues at IriusRisk,
who’ve built [Jeff](https://www.iriusrisk.com/ai-threat-modeling), which helps in diagram
creation, and [Bex](https://www.iriusrisk.com/conversational-ai-security), a conversational agent
that interacts in Jira.

The only really effective tooling will come out of
thoughtful investment, and how much it [accelerates](/accelerator/) your program has to be
evaluated relative to the threat modeling problem you want tooling
to solve.

There are other concerns with LLMs that this
post doesn’t touch on for length reasons. Those include, but
probably aren’t limited to: LLMs are trained on copyrighted data — including my
books; Environmental concerns over water and power; Connection
to and pride in work; Workforce development; Software
understanding. I'm on IrusRisk's advisory board.

Image by midjourney, “a photograph of a robot standing at a whiteboard, trying to explain a crazy complicated diagram to...