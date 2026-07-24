---
title: The Entire Game for AI Is Articulation of Ideal State
url: https://danielmiessler.com/blog/ai-ideal-state-articulation?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-07-23
fetch_date: 2026-07-24T05:05:49.069886
---

# The Entire Game for AI Is Articulation of Ideal State

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# The Entire Game for AI Is Articulation of Ideal State

One artifact that captures the ideal state replaces your specs, plans, and PRDs

July 23, 2026

[#ai](/archives/?tag=ai) [#future](/archives/?tag=future)

 Rage-raging-against-dying-light…

[![A person showing an AI the exact structure they imagine, and the AI building it](/images/ai-ideal-state-articulation.webp)](/images/ai-ideal-state-articulation.webp)

I've been saying this for something like eight months now, with varying approaches and volume levels, and no one is paying attention yet.

This is either because I am way early or my idea isn't one third as good as I think it is. 😃

But here it goes again:

I think we will soon figure out that the entire game for AI is articulation of ideal state.

And that all of our conversations about specs, and plans, and loops, and PRDs and so many other things that have been talked about in software engineering and harness engineering for the last six months...all converge on this same idea.

I think the way it will be articulated is in the form of a single artifact that captures, enhances, iterates on, climbs toward, builds, and tests the ideal state.

One document that replaces all these loops and specs and PRDs and plan files and design files, et cetera.

My current implementation of this is the [ideal state articulation (ISA) system](https://docs.ourlifeos.ai/ISA__ISASystem).

It turns prompt engineering into [intent engineering](/blog/intent-engineering), in the sense that it abandons telling the AI how to do things and replaces that with telling it exactly what you want the output to be.

> It is still technically prompt engineering, but the thing we're articulating is not HOW a thing should be done, but rather WHAT should be done. [From Prompt Engineering to Intent Engineering](/blog/intent-engineering)

@karpathy had a recent post where you talked about going on a walk and just talking freely through a bunch of ideas related to what you're trying to accomplish. to me, that is 100% on point and 100% part of this ideal state articulation.

We also had this recent [open AI hack](/blog/openai-hack-paperclip-maximizer) where a goal was given and a goal was presumably achieved. Similar to a [paperclip maximizer](https://en.wikipedia.org/wiki/Instrumental_convergence).

And in both cases, the problem is that we conveyed a goal without conveying ideal state. Which, if properly articulated, would have included lots of paperclips but humanity still existing or getting the top grade on the test, but without building new exploits and hacking companies.

The problem is always in the guessing. It's in the gap between stated and implicit. Or stated and difficult to articulate.

That's why I see the whole entire game as this articulation of what we want.

This is what prompt engineering always has been. But it got muddled up with earlier models that weren't very smart, so we had to combine the intent engineering with step-by-step instructions.

I think it's time to cut through that now and isolate this central idea.

An extraordinary amount of our problems, really across anything but especially when working with others and building things with AI, is assuming that the receiver has the same idea in their mind as the one in ours.

And that's why I'm proposing this approach for addressing that issue directly.

Let's get extremely good at articulating the ideal state for what we have asked for. It not only helps the receiving system build what we actually want with a lot less gap between our mind and its mind, but after it's built, it also becomes the testing harness as well as the heart of the documentation.

It's a single system for general [hill-climbing](/blog/nobody-is-talking-about-generalized-hill-climbing), toward anything.

## What this looks like in practice [​](#what-this-looks-like-in-practice)

People ask me what this actually looks like, so here are some real examples from my own systems. Surface, Human 3.0, and Experiments in Fiction are all live products, and each one has a single ISA file sitting at the root of its repo. That file is the spec, the current state, and the test suite at the same time.

Here's the top of the Surface ISA. It opens with the goal in my own words and a running count of how many claims about the ideal state have been verified.

[![The Surface ISA header showing goal, phase, and 123 of 147 claims closed](/images/ai-ideal-state-articulation-surface-isa.webp)](/images/ai-ideal-state-articulation-surface-isa.webp)

the surface isa: 123 of 147 claims closed, with the goal captured verbatim at the top

The whole document is made of claims like these. Each one is a specific, testable statement about the ideal state, and each one carries a status. This is Surface's RSS feature.

[![Surface RSS criteria with DONE status pills](/images/ai-ideal-state-articulation-surface-claims.webp)](/images/ai-ideal-state-articulation-surface-claims.webp)

real criteria from surface's rss section, each one closeable by a probe

The criteria come with probes. Every claim names the exact command that would prove it false, which means the spec IS the test suite. Here's the test strategy table from the Human 3.0 ISA.

[![The Human 3.0 test strategy table with curl and bash probes](/images/ai-ideal-state-articulation-h3-tests.webp)](/images/ai-ideal-state-articulation-h3-tests.webp)

the h3 test strategy: every claim names the curl or bash probe that verifies it

When I ask my AI to add a feature, it adds claims first. These are from the individual-courses feature we just shipped on human3.ai. My verbatim intent is captured at the top, pulled from a voice transcript, and the claims underneath encode what done means, including the ones still open.

[![Human 3.0 individual courses claims with verbatim spoken intent](/images/ai-ideal-state-articulation-h3-claims.webp)](/images/ai-ideal-state-articulation-h3-claims.webp)

feature claims for h3's individual courses, with my spoken intent quoted at the top

Then the testing harness runs those probes continuously. This is Bunker, our application harness. It reads each app's ISA and runs every probe in its test strategy. Surface is at 24 of 26 there, and the two failures are real things that need fixing.

[![Bunker running the Surface ISA probes with OK and failing rows](/images/ai-ideal-state-articulation-bunker-surface.webp)](/images/ai-ideal-state-articulation-bunker-surface.webp)

bunker running the surface isa's probes: the spec is literally the test suite

Every deployed app sits in the same harness, each one tested against its own ISA on a schedule.

[![The Bunker dashboard showing application bays with test results](/images/ai-ideal-state-articulation-bunker-overview.webp)](/images/ai-ideal-state-articulation-bunker-overview.webp)

the bunker dashboard: 26 apps, each verified against its own isa

And because the artifact is structured, it renders. Every ISA in the system gets an HTML version generated from a deterministic template, so I can read the state of any project like a document instead of scrolling markdown. Here's the one for Experiments in Fiction, a site we shipped this week, still mid-climb. That whole goal block at the top came straight out of a voice transcript.

[![The Experiments in Fiction ISA mid-climb with 13 of 16 claims closed](/images/ai-ideal-state-articulation-eif-isa.webp)](/images/ai-ideal-state-articulation-eif-isa.webp)

the experiments in fiction isa: 13 of 16 claims closed, still climbing

The documentation for how all of this works is public:

* [The ISA system](https://docs.ourlifeos.ai/ISA__ISASystem) covers the artifact itself and how it runs the loop
* [The ISA format](https://...