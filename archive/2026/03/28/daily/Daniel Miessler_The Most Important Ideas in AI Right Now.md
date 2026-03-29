---
title: The Most Important Ideas in AI Right Now
url: https://danielmiessler.com/blog/the-most-important-ideas-in-ai?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-03-28
fetch_date: 2026-03-29T04:42:46.314156
---

# The Most Important Ideas in AI Right Now

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# The Most Important Ideas in AI Right Now

Self-improvement and transparency change everything in unexpected ways

March 28, 2026

[#ai](/archives/?tag=ai) [#future](/archives/?tag=future)

[![The Most Important Ideas in AI Right Now](/images/blog/the-most-important-ideas-in-ai/header.webp)](/images/blog/the-most-important-ideas-in-ai/header.webp)

After thinking about this for about a week, and attending the RSA conference during that time, I think there are a few main AI ideas that are going to change things more than anything else.

1. Autonomous Component Improvement
2. The Transition to Intent-Based Engineering
3. The Move from Opacity to Transparency
4. The Realization That Most Work is Scaffolding
5. Expertise Gets Diffused into Public Knowledge

# 1. Autonomous Component Optimization [​](#_1-autonomous-component-optimization)

This one connects to the [current-to-ideal-state concept](/blog/ai-state-management), [the Algorithm](/blog/the-last-algorithm), [general verifiability](/blog/nobody-is-talking-about-generalized-hill-climbing), etc.

But one thing that really made it tangible was [Karpathy's Autoresearch project](https://github.com/karpathy/autoresearch).

His was focused on AI research, as in "Autoresearch of the research portion of AI research", meaning automatically doing all the gross stuff around model parameter tweaking, wrangling fragile environments and combinations of options, etc.

His release lets you give some ideas in a `PROGRAM.md` file, and the system will handle all that grossness itself, and you go to sleep and it's used ML optimization to produce better results than what you had.

## Extending Autoresearch [​](#extending-autoresearch)

But now there's "Autoresearch for X", meaning it's becoming a paradigm. A movement. A tool, basically.

He has lots of people thinking:

> Could I apply a similar thing to this thing I'm working on?

It's extraordinary.

## Combining Autoresearch with what I've been working on [​](#combining-autoresearch-with-what-i-ve-been-working-on)

So my thing has been this whole [general verifiability concept](/blog/nobody-is-talking-about-generalized-hill-climbing); or, general hill-climbing. Again pivoting off of something Karpathy said a long time ago in [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) and a recent tweet, where he talked about the future of software being everything being verifiable.

So what I do inside of [the Algorithm within PAI](/blog/personal-ai-infrastructure) is I try to break everything into ideal state criteria that are essentially constructing the ideal state for the outcome that I want.

And from there the Algorithm can hill-climb towards it.

## Evals for everything [​](#evals-for-everything)

Related to this is the concept of Evals for everything. It's very much like my [general verifiability](/blog/nobody-is-talking-about-generalized-hill-climbing) or general hill-climbing. It's the idea that everything we do becomes measurable, but more importantly: **improvable**.

And the thing that makes evals possible for everything is transparency.

## The universal improvement cycle [​](#the-universal-improvement-cycle)

This is going to become the standard operating model for every company, organization, government, and individual. The cycle looks like this:

You map out everything you're trying to accomplish in a goal-oriented structure—mission, objectives, workflows, SOPs. Agents execute those workflows. Everything gets extensively logged—the outputs, the conversations, the results, the quality. Whenever there are errors, failures, or quality issues captured in those logs, they flow up into a problems collection point for that entity.

That collection point is where the self-improvement algorithm feeds from. Agents pull from there, create autoresearch-like executions to troubleshoot the problem, experiment with solutions, validate through evals, and optimize. Once they find the fix, they update the SOPs to make sure it doesn't happen again. Then the cycle repeats.

This is the lifecycle for running anything. Map your goals. Execute with agents. Log everything. Collect failures. Improve autonomously. Update the SOPs. Repeat—faster each time.

# 2. The transition to intent-based engineering [​](#_2-the-transition-to-intent-based-engineering)

The real power of AI is [moving from current state to ideal state](/blog/ai-state-management). Define where you are, define where you want to be, and let AI close the gap. Simple concept, but there's a step before any of that works: you have to be able to *articulate what you actually want*. And it turns out this is incredibly hard. If you [can't describe what good looks like](/blog/how-to-talk-to-ai), no amount of tooling helps you.

This is a massive problem for companies. Ask a CEO what their ideal security program looks like and you'll get hand-waving. Ask a team lead what "done" means for their project and you'll get a paragraph that three people interpret three different ways. The [articulation gap](/blog/exactly-why-and-how-ai-will-replace-knowledge-work) isn't just between experts and AI—it's between leaders and their own organizations. Most companies can't clearly state what they're trying to do, let alone break it into components you could measure or optimize.

What I've been building inside [the Algorithm](/blog/nobody-is-talking-about-generalized-hill-climbing) is exactly this—a way to reverse engineer any request into discrete, testable ideal state criteria. Eight to twelve words each, binary pass/fail. Once you have those, you can hill-climb. You can eval. You can automate improvement. But the whole thing starts with being able to say what you want. That's the new engineering skill—not coding, not prompting. Articulating intent clearly enough that it becomes verifiable.

# 3. The move from Opacity to Transparency [​](#_3-the-move-from-opacity-to-transparency)

Companies have never really been able to see what's happening inside their own walls. How much does this process actually cost? How long does it really take? What's the quality of the output? Who's doing the work vs. who's doing the scaffolding around the work?

Most organizations run on vibes and spreadsheets. AI makes all of that visible. The actual work, the actual costs, the actual quality—all of it becomes measurable in ways that were never practical before. And once you can see it, you can improve it. That applies to businesses, governments, teams of three people—anything you want to point it at.

And one of the first things transparency reveals is how much of the work was never really the work.

# 4. Most work is scaffolding [​](#_4-most-work-is-scaffolding)

AI is revealing that [75-99% of knowledge work is scaffolding](/blog/ai-unmasked-our-work-as-scaffolding) overhead. In security testing, development, consulting—most of the time goes to maintaining tooling, workflows, templates, and knowledge bases. The actual hard thinking is a tiny percentage, done by a tiny percentage of people, a tiny percentage of the time.

AI absolutely crushes the scaffolding part. Agent Skills have shown you can package all that context, methodology, and tooling into a skill, and the AI executes as good or better than most professionals. The work wasn't hard—maintaining the scaffolding was.

# 5. Expertise gets diffused into public knowledge [​](#_5-expertise-gets-diffused-into-public-knowledge)

There's an [articulation gap](/blog/exactly-why-and-how-ai-will-replace-knowledge-work) between what experts know and what's written down. Most expertise lives in people's heads. Cliff, the 62-year-old who knows how everything works but never documented any of it. When Cliff...