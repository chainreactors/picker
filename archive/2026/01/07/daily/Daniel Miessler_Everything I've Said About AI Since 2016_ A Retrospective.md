---
title: Everything I've Said About AI Since 2016: A Retrospective
url: https://danielmiessler.com/blog/my-ai-predictions-retrospective?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-01-07
fetch_date: 2026-01-08T03:31:11.949327
---

# Everything I've Said About AI Since 2016: A Retrospective

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Everything I've Said About AI Since 2016: A Retrospective

Looking back at my predictions to see what I got right, wrong, and what's still playing out

January 6, 2026

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#future](/archives/?tag=future) [#predictions](/archives/?tag=predictions) [#top](/archives/?tag=top)

![AI Predictions Retrospective](/images/ai-predictions-retrospective.webp)

I've been making AI noises for [exactly a decade now](/blog/the-real-internet-of-things), and last week someone claimed I said two things about AI in 2023 that I don't think I said (that we'd have AGI in 6 months and that AI was sentient).

To my knowledge, I've never said either of those.

So this made me want to prove him wrong, which would require that I create a list of all the stuff I *did* say over the decade. And that made me wonder how accurate I've been.

So I spun up some of my [fancy new AI tooling](/blog/personal-ai-infrastructure) (another "reason" to do this) and got after it. More on the tooling in the notes if you're into that.

So here's (mostly) everything I've said about AI since 2016, organized chronologically, what I got wrong and right, and what I've learned from reviewing it.

1. [2016](#2016)
2. [Late 2022](#late-2022)
3. [Early 2023](#early-2023)
4. [Late 2023](#late-2023)
5. [2024](#2024)
6. [2025](#2025)
7. [2026](#2026)
8. [Predictions Scorecard](#scorecard)
9. [What I Got Right](#right)
10. [What I Got Wrong or (Charitably) Too Early?](#wrong)
11. [What I Learned From The Effort](#lessons)
12. [I Recommend Trying Something Similar](#try-this-yourself)

---

# 2016 [​](#_2016)

Especially DAs and APIs. AR is taking a while due to general tech miniaturization challenges.

In late 2016 I published a short (somewhat shitty) book called [The Real Internet of Things](/blog/the-real-internet-of-things). I *hate* parts of the writing, just from a tone standpoint, and I really wish I'd said some things differently. But the core predictions (DAs, APIs, AR, etc.) are actually starting to happen!

Here they are.

## Prediction: Universal Daemonization [​](#prediction-universal-daemonization)

One of the main concepts of the book is the idea that every object in the world would eventually have an API—a "daemon" that presents its state, capabilities, and allows interaction in a standardized way.

> "All objects will have these daemons. Cars, houses, buildings, cities, businesses, etc. People will interact with objects through their daemons, which will be fully functioning interfaces that allow you to push and pull information as well as modify configurations and execute commands."
>
> — [The Real Internet of Things](/blog/the-real-internet-of-things#universal-daemonization), December 2016

I was describing what we'd now call the API-ification of everything, or more specifically, what MCP (Model Context Protocol) is becoming. At least for services infrastructure.

**Analysis:** This one feels pretty good, but API-ification is still just on certain kinds of digital things. The [MCP ecosystem](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/) now has 10,000+ servers and 97 million monthly SDK downloads. Every major AI platform adopted it. The "everything gets an API" vision is genuinely happening, but I don't see many park benches or restaurants with APIs yet.

VERDICT: **Core idea happening, but implementation still limited.**

## Prediction: Digital Assistants as Primary Interface [​](#prediction-digital-assistants-as-primary-interface)

We'd stop interacting with technology directly and instead interact through AI assistants that handle everything on our behalf.

> "Humans interact with DAs, and DAs interact with the world."
>
> — [The Real Internet of Things](/blog/the-real-internet-of-things#digital-assistants), December 2016

I wrote about how DAs would "work to optimize the life of their principals continuously, without rest, 24/7/365, and in multiple threads."

**Analysis:** This is starting to be talked about now in late 2025 and I'm sure in 2026. I expected it back then. [Anthropic's computer use](https://www.anthropic.com/news/3-5-models-and-computer-use), [OpenAI's Operator](https://openai.com/index/operator-announcement/), and various agent frameworks are all moving in this direction. But we're still in early days. Most people still interact with technology directly. I've been working on building toward this vision ever since it became possible—first with my [Personal AI Maturity Model](/blog/personal-ai-maturity-model) which maps the path from chatbots to full DAs, and now with the [PAI (Personal AI Infrastructure)](https://github.com/danielmiessler/PAI) project on GitHub. I still think of what I'm building as trying to get to the DA I described in the book.

VERDICT: **Directionally solid, timeline was optimistic.**

## Prediction: DAs Understanding Your Context [​](#prediction-das-understanding-your-context)

This is one of the ideas I'm most proud of from the book. I wrote that DAs would understand your preferences, mood, and intentions—and use all of that context to construct requests on your behalf.

> "The preferences piece is essential, because the better your DA understands you the better it can represent you when making requests on your behalf. Your DA will be essentially bound to your own personal daemon, and it will have access to the most protected information within it. Most notably, your preferences and experiences, which will both be used to help construct the ideal contextual requests on your behalf."
>
> — [The Real Internet of Things](/blog/the-real-internet-of-things#digital-assistants), December 2016

And in the AR section, I got even more specific about context:

> "With context, DAs will understand the preferences, mood, and intentions of their principals, and they will use this to decide what should be presented to the user... Your DA knows your preferences, your current context (happy, lonely, angry, sad, etc.) and is parsing all those daemons."
>
> — [The Real Internet of Things](/blog/the-real-internet-of-things#augmented-reality), December 2016

**Analysis:** This is essentially what we now call "context engineering" or sophisticated prompting. The entire premise of effective AI use in 2025 is giving the AI your preferences, your context, your goals—exactly what I described. System prompts, memory features, personalization—it's all "constructing ideal contextual requests." People are literally re-learning this lesson right now, and I wrote it in 2016.

VERDICT: **Nailed it.**

## Prediction: Services Designed for DAs, Not Humans [​](#prediction-services-designed-for-das-not-humans)

I wrote that the entire paradigm would flip—businesses would design their services to be consumed by AI assistants, not humans directly.

> "Services (which nearly everything will become) will be designed (and/or retrofitted) to be consumed by Digital Assistants, not by humans."
>
> — [The Real Internet of Things](/blog/the-real-internet-of-things#digital-assistants), December 2016

And later:

> "The function of the business changes fundamentally in this model. Instead of being in charge of the user's entire experience, businesses become part of an algorithm marketplace used by DAs to satisfy the requests of their principals. The DA is now the centerpiece of the user experience."
>
> — [The Real Internet of Things](/blog/the-real-internet-of-things#businesses-as-daemons), December 2016

**Analysis:** This is MCP. This is the entire API-first, AI-native design movement. When Anthropic launched MCP and suddenly every business is racing to create AI-consumable interfaces to their services—that's ...