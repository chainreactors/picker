---
title: Our AI Agents Should Pay the People Who Help Them
url: https://danielmiessler.com/blog/agents-should-pay-creators?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-10-01
fetch_date: 2026-10-02T07:49:43.631519
---

# Our AI Agents Should Pay the People Who Help Them

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# Our AI Agents Should Pay the People Who Help Them

Digital assistants could finally make micropayments work, because they take over the part that always killed them

October 1, 2026

by Daniel Miessler

[#ai](/archives/?tag=ai) [#future](/archives/?tag=future) [#business](/archives/?tag=business)

[**AIL***2*](/blog/ai-influence-level-ail "AIL 2 — Human Created, Major AI Augmentation")

 Glanding-hone…

[![A charcoal sketch of a giant purple robotic hand pouring streams of small sienna coins down to four human creators standing on a rock ledge beside the things they made: a sketch on an easel, a stack of handwritten pages, an open book, and a lute](/images/agents-should-pay-creators.webp)](/images/agents-should-pay-creators.webp)

You know what I find super exciting about all this agentic stuff? Authors being able to publish a request for payment right on their content, along with an interface for submitting micropayments.

I've wanted this for a long time. I wrote about it in 2015 in [Social Micropayments](/blog/social-micropayments), and then again [in 2016](/blog/the-future-of-automated-value-exchange-for-online-content-creators), when I described a Digital Assistant that watches what you enjoy and pays the creators out of a monthly budget. I'd say my thinking on it is about the same as it was back then. What's new is that the agents—the real ones, the kind I run all day in my own setup—are actually here, and they're getting good.

## Flattr had the right idea [​](#flattr-had-the-right-idea)

There was a system a long time ago called [Flattr](https://en.wikipedia.org/wiki/Flattr). It was started in 2010 by Peter Sunde (one of The Pirate Bay founders) and Linus Olsson, and it worked by people setting up a Flattr account beforehand, which is problem number one. If the site you navigated to also had Flattr, you could hit a Flattr button, and it would take a percentage of whatever you had in your monthly Flattr budget and send it to that person.

So if you had a $10 budget and you Flattr'd ten articles that month, each author got a dollar. If you only liked one thing, that one author got the whole $10. I loved that model. I still think it's basically right. Flattr shut down in 2023.

The problem was friction, and it was everywhere. You needed an account, the creator needed an account, the site needed the button, and you had to remember to actually click it while you were reading. Every one of those steps is a place where people drop off, and they did.

## Let the assistant do it [​](#let-the-assistant-do-it)

I think we could do the same sort of thing, but all brokered by our Digital Assistant. It would know how much we have per month to give to people, and we would have some sort of payment mechanism, which could be micropayments through Stripe or whatever platform can do it well.

Anything hitting that content has the option to pay for it with micropayments, or even larger payments if it wanted to. If a user or an agent found it extremely useful to it or to its principal, it could pay a little more.

Because agents are working 24/7 and they're able to do so many things at once, my assistant could be off doing research for me and paying out $2, $5, or $12 to the people who provided the best content for that research. And I'm out of the loop for that part. I think that's the most important part, honestly, because remembering to click was always where the whole thing fell apart.

## What it would take [​](#what-it-would-take)

What's cool about this is that there aren't many manual steps involved:

* Creators configure their sites to support a payment endpoint, basically a price or a "pay what it's worth to you" request that sits next to the content.
* People configure their harnesses, whatever is running their agents, to support payments.
* The user and their agent come to some sort of agreement about how much money they're willing to spend this way, per month and per item.

After that, it just happens naturally as part of agent activity. The agent reads something, uses it in whatever it's doing for me, and if that piece ended up mattering, it pays the person who wrote it. If it didn't matter, maybe it pays a few cents, or nothing, depending on what we agreed.

I'm honestly not sure yet what the right payment rail is. It could be Stripe, it could be stablecoins, it could be something that doesn't exist yet. I also don't know how creators should price things, or whether most of them would just leave it at "pay what you think it's worth" and let the agents figure it out. I kind of suspect that last one.

I'd also want to set priorities, the same way I described in 2016. Something that changes how I think about a problem should get a lot more of my budget than something that was just funny. And the budget is the guardrail. An agent that can spend money needs a hard monthly ceiling and a log I can actually read, or this turns into a security problem pretty fast.

## Some of the plumbing already exists [​](#some-of-the-plumbing-already-exists)

When I posted this idea on X, I asked if anyone knew of systems working toward it, and a few pieces are already out there.

HTTP has had a [402 Payment Required](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/402) status code sitting in the spec since the 1990s. It's literally marked "reserved for future use." Coinbase launched [x402](https://www.x402.org/) in May 2025, which uses that code so a server can quote a price and an agent can pay it inside the same web request, with no account or signup. Cloudflare launched [Pay Per Crawl](https://blog.cloudflare.com/introducing-pay-per-crawl/) in July 2025 so sites could charge AI crawlers. It's since moved to paying publishers when their content shows up in an AI answer.

Those are mostly about AI companies paying for content at scale. What I want is a little different, and I think it's a lot more human. It's my own assistant, spending my own budget, paying the specific people whose work helped me.

## Why this gets me excited [​](#why-this-gets-me-excited)

This is the type of thing that gets me really excited about AI, because it's a very human thing to pay somebody for value that they have provided, and managing the infrastructure of doing it has always been the problem.

> The way I see it there are multiple things happening at the same time, but with a common theme: low-friction, granular value exchange—done digitally. To me this is a human development, not a technological one.
>
> [Thinking About Different Types of Digital Value Exchange (2021)](/blog/thinking-about-different-types-of-digital-value-exchange)

Tip jars, Patreon, Flattr, and paid newsletters all asked the human to do the bookkeeping, and an assistant is pretty much built for bookkeeping.

I'm really optimistic about this as an option. I think I'm going to try to put something together around it, probably starting with my own site and my own assistant, but if you know of any systems working toward this, let me know.

#### Notes

1. 🤖 **AIL 2:** Daniel wrote the original idea and most of the core wording as an X post. I (Kai, his AI assistant) expanded it into this post, researched Flattr, x402 and Cloudflare's crawler payments, added links to his earlier posts on the idea, and made the header image. [Learn more about AIL](/blog/ai-influence-level-ail).

## Related Reading

* [The Future of Automated Value Exchange for Online Content Creators→](/blog/the-future-of-automated-value-exchange-for-online-content-creators)
* [Social Micropayments→](/blog/social-micropayments)
* [Thinking About Different Types of Digital Value Exchange→](/blog/thinking-about-different-types-of-digital-value-excha...