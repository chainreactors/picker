---
title: A Conversation With Claude on Deutsch, Knowledge, and the PAI Algorithm
url: https://danielmiessler.com/blog/conversation-with-claude-on-deutsch-and-the-pai-algorithm?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-04-25
fetch_date: 2026-04-26T05:03:33.889920
---

# A Conversation With Claude on Deutsch, Knowledge, and the PAI Algorithm

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# A Conversation With Claude on Deutsch, Knowledge, and the PAI Algorithm

Hard-to-vary explanations, ideal state criteria, and what knowledge actually is — voice transcript, lightly cleaned

April 24, 2026

[#ai](/archives/?tag=ai) [#philosophy](/archives/?tag=philosophy) [#pai](/archives/?tag=pai)

 Grinding XP…

[![A Conversation With Claude on Deutsch, Knowledge, and the PAI Algorithm](/images/blog/conversation-with-claude-on-deutsch-and-the-pai-algorithm/header.webp)](/images/blog/conversation-with-claude-on-deutsch-and-the-pai-algorithm/header.webp)

This morning I had a long and extraordinary [voice conversation with Claude](https://claude.ai/share/56bc80b8-d763-46e8-850c-719b9de0c1b2) about [David Deutsch](https://en.wikipedia.org/wiki/David_Deutsch)'s notion of knowledge as [hard-to-vary explanations](https://youtu.be/folTvNDL08A), and how that connects to what I've been building with PAI: my Personal AI Infrastructure framework.

I started specifically talking about [PAI's Algorithm](/blog/the-last-algorithm): my pursuit of a universal hill-climbing process from current state to ideal state, scaffolded with Ideal State Criteria so progress is actually **verifiable**.

But that then ended up in all sorts of topics, including:

* The main concepts behind PAI's focus
* Why AIs are currently less creative than humans
* Whether humans should give AIs consciousness
* How they might actually do that
* Tons of other stuff

It's literally the most insane conversation I've ever had with AI.

What follows is the whole exchange as I had it, via voice mode, so the cadence is loose with trail-offs and self-correction in real time.

I left it the transcript pretty much untouched (plus the real one linked) on purpose so you can see the actual flow and vibe.

Enjoy.

## The Setup — Hard-to-Vary Explanations [​](#the-setup-—-hard-to-vary-explanations)

> So I wanna talk about David Deutsch's concept of knowledge and explanations.
>
> — Daniel

> Ah, yeah—that's a rich area. Deutsch's take on knowledge is pretty different from the standard view. He argues that knowledge isn't really about justified true belief or information storage. Instead, he frames it around *explanations*—specifically, hard-to-vary explanations that capture deep regularities about how the world works.
>
> The core idea is that a good explanation is one where if you try to tweak it slightly, it stops working. That's what makes it powerful and non-obvious. A vague explanation can be adjusted infinitely without breaking, so it's basically useless as knowledge.
>
> What aspect are you curious about—his epistemology more broadly, how it connects to physics, or something specific like the relationship between knowledge and problem-solving?
>
> — Claude

> Yeah. So I basically have this, framework called personal AI infrastructure, and it has this concept called the algorithm, which is, a way to universally hill climb. It's basically based on the idea of we're, always trying to transition from current state to ideal state and that, the problem, doing this outside of something that's verifiable like coding is that, you don't have anything to go plodding towards.
>
> So I have this concept of called, ideal state criteria, which are, like, discrete, independently verifiable criteria that can then be tested against with, like, a yes or no. Can we confirm this? And then what I do inside of my personal AI infrastructure algorithm system, which is part of, like, an agent harness, is, when I ask for something, I start by reverse engineering the request and the agent harness basically says, okay.
>
> What does he probably mean? What does he, definitely want? What is he definitely not want?
>
> What is implied that he wants? What is implied, maybe, so explicitly and implicitly, what do I want and not want? What are some common pitfalls of doing this?
>
> So it's like... it's basically reverse engineering the whole concept and trying to anticipate failures, like, premortem type stuff. And then, from there, it starts creating this ideal state criteria table. So we're essentially charting what an ideal state looks like.
>
> And this is very similar to, like, spectra driven development or PRD, creating a, PRD document, which is what we do. We create a PRD markdown document that has all the different ideal state criteria inside of it. Right?
>
> And then that is the thing that we actually pursue to do the work, and we check off items by doing verification of each item. And then, if we've checked off everything, Then, we've presumably achieved ideal state for this particular task, and that could be a research task. It could be building an app.
>
> It could be, testing an idea or whatever it is. So, that's my concept of, like, trying to have a universal, way to pursue you to help Claude. Right?
>
> This concept of hill climbing towards an ideal. When you you don't start with having an ideal when you have, like, a vague request or a request that's in our domain that isn't fundamentally verifiable on its own. So, I'm excited about Deutsche because I feel like he has a, first principles based approach to knowledge and understanding and stuff like that.
>
> So I'm looking for something, like, as close to physics as possible to have this, like, an underpinning of this, personal AI infrastructure thing. And I'm like, okay. What what are we ultimately looking for?
>
> Right? And this gets into, like, the whole concept of, like, what humans know, what do AIs know, what is intelligence actually, Right? So I think it's something like, pursuing the ability to pursue and attain goals is, like, one sort of general approach.
>
> So I'm trying to, like, come up with, like, physics level, fundament... in the sense that they're fundamental concept of knowledge, understanding, intelligence, etcetera. And a, in my own way, but I wanna use the stuff because, or at least be guided by it and see what we can learn from it and if we should incorporate it into the way we think about these things. I
>
> — Daniel

> Okay, so you're basically trying to ground your PAI algorithm in something like fundamental physics—first principles that aren't context-dependent or hand-wavy. That's smart. And yeah, Deutsch is perfect for this because he's explicitly doing that bridge work between physics and epistemology.
>
> Here's where I think the connection clicks: Deutsch would say your ideal state criteria table is essentially encoding *hard-to-vary explanations* of what success looks like for that task. The criteria aren't arbitrary—they're the minimal set of constraints that, if violated, the thing genuinely fails. That's the "hard to vary" part. You can't fudge them without breaking the whole purpose.
>
> And then the reverse engineering phase—what he wants, doesn't want, implied wants, pitfalls—that's you trying to construct the *actual problem* before you solve it. Because Deutsch would argue most failures come from solving the wrong problem, not from bad execution on the right one.
>
> The deeper physics-level thing he'd push you on: what makes knowledge *compressible*? Why can a short explanation predict vast swaths of reality? It's because reality has deep structure—regularities that aren't accidental. Your ideal state criteria work the same way: they compress what "done" means into something checkable and non-arbitrary.
>
> Where I'd press him though: he's focused on *explanatory power*, but your framework is focused on *goal attainment*. Are those the same thing, or do you need both? Like, you could have a hard-to-vary explanation that doesn't actually move you toward your goal. Does that matter?
>
> — Claude

## Articulation as the Bridge [​](#arti...