---
title: We're All Building a Single Digital Assistant
url: https://danielmiessler.com/blog/we-are-all-building-single-digital-assistant?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-04-15
fetch_date: 2026-04-16T04:54:23.813389
---

# We're All Building a Single Digital Assistant

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# We're All Building a Single Digital Assistant

Agents and harnesses are just infrastructure — what we actually want is one named AI with full context about our lives

April 15, 2026

[#ai](/archives/?tag=ai) [#future](/archives/?tag=future) [#technology](/archives/?tag=technology)

[![We're All Building a Single Digital Assistant](/images/blog/we-are-all-building-single-digital-assistant/header.webp)](/images/blog/we-are-all-building-single-digital-assistant/header.webp)

I want to talk about where I think all this personal AI stuff is going.

We've been talking about agents since 2025, and now we're talking about harnesses. And I think this is all heading in the exact same direction. I initially talked about this in 2016, which we could talk about later, but I think the direction this is all heading is into a single interface — a single interface for handling everything AI-related.

And there are a few pieces that are missing here. I think the main thing that we're missing right now is that our AI system doesn't have a single entity. It doesn't have a single identity. Doesn't have a single personality. And I think that *is* the interface that we will move to.

I think a bunch of people have sort of figured this out. I believe OpenAI is heading in this direction with some sort of device. They hired Johnny Ive to work on some sort of wearable. And the idea for them is they want to bypass the mobile infrastructure. They don't want to deal with Apple and the iPhone anymore. They want to have their own OS — essentially like an AIOS that basically everything goes through, and then all their infrastructure and stuff on the back end.

But I think when we talk about harnesses, context engineering, prompt engineering, agents — we get stuck in the weeds. We're talking about: okay, what's the best agent framework? What are the best agents? What are the best skills? And I think the best way to think about this is to imagine all that stuff abstracted away.

# Reversing backwards from the future [​](#reversing-backwards-from-the-future)

And the way I like to think about this — and I learned this when I was at Apple, and we got this DNA (I believe we stole a lot of it from Amazon, actually) — it's the concept of reversing backwards. To go into the future where you believe you see some sort of outcome that you want, a product that you want, or a future that you believe is going to happen. And you basically articulate that and say: okay, this is a thing that I think people want. This is a thing that I think people will resonate with and ultimately really enjoy. And then you say: okay, what is a — they call it a PR, a public release — what does a release look like? And then they work backwards.

So I've been thinking this way since 2014 or something.

# The 2016 book [​](#the-2016-book)

So in 2016, I wrote [this shitty book](/blog/the-real-internet-of-things), which you don't have to read because I turned it into a blog post. But I basically said that everything is heading in this direction of: you're going to have a single DA — which is an AI, a single AI digital assistant — which is going to be your conduit. It's going to be your buddy, your friend. And most importantly, your digital assistant knows everything about you.

That is the primary concept from this book in 2016. This thing knows everything about you. It knows your work, your life, your relationships. It knows what you struggle with. It knows what your strengths are. It knows what your weaknesses are. It knows what you're trying to accomplish.

💡 [The Real Internet of Things](/blog/the-real-internet-of-things) — the 2016 book, as a free blog post.

So if you look at all my various projects — well, first being that thing in 2016, but also you look at [Substrate](/blog/introducing-substrate). Most importantly, you look at [TELOS](https://danielmiessler.com/telos), if you're familiar with that at all.

So TELOS is essentially a system for defining yourself — just defining what your goals are, what your problems are that you're working on. And essentially having all that in one place. What are my challenges? What are my projects? What are my budget? If this is a company versus a person, what is the team that I'm dealing with? What are the different dynamics there? What is the active work that's going on?

So the idea is to have all this clearly articulated inside of a system. And then with that context, your digital assistant can then basically monitor this.

# Ideal state and current state [​](#ideal-state-and-current-state)

The other crazy concept here that's very much related, that I've talked about a bunch in the last year, is this concept of ideal state and the concept of current state.

So the cool thing about all this AI stuff and all these agents is that they can constantly gather. They can constantly go and collect context, research, knowledge, facts, activities happening in the world, news, signal from different sources. It can always be gathering.

But here is the central concept.

Your DA — I'm just going to use mine. Mine's name is Kai. Kai, for me, is constantly going and collecting things. He is constantly collecting and organizing knowledge for me inside of my system, which my harness is called [PAI](/blog/personal-ai-infrastructure). It's actually a public repo. It's an open-source project, releasing 5.0, about to come out. So you should get that very soon. Might actually be out by the time you read this.

But this infrastructure is not designed to be agents. It's not designed to be AI tools. It's not designed to be workflows. It's not designed to be any of that. It's designed to be the back-end infrastructure for context collection and management for my specific individual unitary digital assistant, whose name is Kai.

I intend to interact with Kai. Kai then understands everything about me — all my preferences, everything I'm trying to do in my world, in my life, in my work, with my friends, with my relationships. And this is the backplane. This is the foundation of everything that is happening in my AI life.

This is the direction I think everyone is going to go. I don't know if it's really going to kick off in 2026, because we still seem pretty obsessed with agents, but it's starting to happen. I feel like it's starting to happen because there's more and more talk of harnesses. And I think the next thing we figure out after harnesses is that we actually just want a single person, a single entity to interact with. And because we are humans, we want that to be someone with a personality and a memory.

# OpenClaw and proactivity [​](#openclaw-and-proactivity)

Now, [OpenClaw](/blog/nobody-is-talking-about-generalized-hill-climbing) kind of helped push this along a decent amount, because it was somebody who was proactive. This is a major, major feature that's required that previous agents didn't have. **Proactivity.** The fact that you can give it some things that you care about to some degree, and it puts it in a text file or whatever, and it could just check on them regularly. It could check scheduled tasks. This kind of moved it forward a little bit.

# The maturity model [​](#the-maturity-model)

So I put together this [Personal AI Maturity Model](https://danielmiessler.com/blog/personal-ai-maturity-model). And this ironically was a couple of weeks right before OpenClaw came out — which I can't even remember the first name, went through like four names — but this was right before that happened, which I was very happy to see it come out after this. And I was like: okay, cool. This is definitely catching on.

So check this out. The concept here is you move through these stages. And I've got three d...