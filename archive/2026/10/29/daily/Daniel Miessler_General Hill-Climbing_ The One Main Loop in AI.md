---
title: General Hill-Climbing: The One Main Loop in AI
url: https://danielmiessler.com/blog/general-hill-climbing?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-10-29
fetch_date: 2026-10-30T07:56:36.562357
---

# General Hill-Climbing: The One Main Loop in AI

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# General Hill-Climbing: The One Main Loop in AI

Know what you want, write it down, measure progress, and keep climbing

October 29, 2026

[#ai](/archives/?tag=ai) [#productivity](/archives/?tag=productivity) [#innovation](/archives/?tag=innovation)

[**AIL***1*](/blog/ai-influence-level-ail "AIL 1 — Human Created, Minor AI Assistance")

 ISA-writing…

[![General Hill-Climbing diagram: five numbered stations climb a hill to the Ideal State flag, from TELOS through articulating the ideal state, evals, doing the work, and iterating, with a dashed loop back to refine the ideal state and evals](/images/general-hill-climbing-diagram.webp)](/images/general-hill-climbing-diagram.webp)

💡There is basically One Main Loop in AI, and it applies to everything from building software to managing pretty much anything.

⛰️I call it [General Hill-climbing](/blog/nobody-is-talking-about-generalized-hill-climbing).

Here are the main components:

* 🖼️ Know what you want
* ✍️ Be able to articulate it
* 📐 Be able to measure progress
* 🧪 Do the work / test your ideas
* ⇧ Adjust / Iterate / Climb / Repeat ♻️

In 2026/2027 modern language that means:

## 1. 🧭 YOUR TELOS (Purpose) [​](#_1-🧭-your-telos-purpose)

You want to start with clear articulation of your current state, your ideal state, your goals, metrics, challenges, strategies, projects, etc. This is where you're trying to get to, where you are now, what you're trying to accomplish, how you measure progress, the things that are stopping you, what you're doing to overcome those issues, the work you're actively doing, etc.

📚 TELOS is an open-source framework for writing all of this down in one file. [Telos on GitHub](https://github.com/danielmiessler/Telos).

Your [TELOS](https://github.com/danielmiessler/Telos) captures this all together, in a single place, so that you, and other people, and your AI systems can all understand the overall direction. This is the starting point and center of reference for work we want to do.

## 2. 🖼️ CLEAR ARTICULATION OF IDEAL STATE [​](#_2-🖼️-clear-articulation-of-ideal-state)

Step one is defining what you're trying to do overall, with as much context as you can provide around not just what you're doing, but why.

Here we want to specifically define the ideal state for a specific task. Like creating an app, or starting a business, or creating a plan for selling a new video game you made. Or writing a book. Whatever.

You need an extremely thorough and clear articulation of exactly what you want.

🎯 Ideal state describes WHAT done looks like. How to get there is the AI's job.

We believe very strongly that more and more AI failures today are not actually AI execution problems. AI is getting really good at doing exactly what we asked for.

The problem is often us either:

* a. Not giving a complete picture of what we wanted
* b. Giving an incorrect / conflicting picture of what we wanted

### Layers of abstraction [​](#layers-of-abstraction)

Think of this as layers of abstraction.

1️⃣ The true thing is the idea in our head. That's ground truth. That's the thing we actually want to build.

2️⃣ The next step is the capture into an artifact. The moment we leave that and try to capture it via voice, or text, or whatever, we've lost something. Hopefully not that much. This step really matters. This is the step we have to do really well, because AI can't read our minds.

3️⃣ And finally we try to build the project. It's critical to understand that this comes from step 2, not from step 1. AI has no way to access number 1. It can only go off of number 2. This is why the ideal state capture piece is so essential.

So we have to address this by being extremely thorough in our description of what we want. This might mean doing a whole lot of dictation about the project, what you're trying to do with it, why you're doing it, how you hope it will help, etc.

💡 Talking is faster than typing, so dictation gets more of what's in your head into the artifact.

Like if you do a full hour, or three hours on the [Ideal State Artifact](/blog/ai-ideal-state-articulation) (our way of capturing the full ideal state in one document), that might not be too much. If it's a smaller project you should be able to get away with less. But you have to put the effort in to fill in a super-high-quality capture of what's in your mind.

Just know that the primary limitation for AI today is not its ability to build what you ask for. It's your ability to clearly articulate what you want.

Piecing...

## 3. ⚖️ INSTRUMENTATION (Evals) [​](#_3-⚖️-instrumentation-evals)

Ok, so once we know our general direction we're building towards, and we know exactly what we're building in this specific case, you then need a system that can watch you executing work against a given target / goal / destination and tell you whether you're improving or getting worse.

This means measurability. This means specifics. And there's a reason why we call it "General" hill-climbing. You need to be able to measure progress or regression against any type of thing you're trying to do.

That means not just science and engineering, but product management, sales, marketing, design, etc...basically any work that you do. If you can't instrument the work in a way that's tied to the ideal state you're trying to get to, you can't know, discuss, or improve the situation.

This is where [Evals](https://hamel.dev/blog/posts/evals/) come in. Evals come from software development but in this new AI model of the world, Evals will become far more general, making them pretty much universal and essential for any type of work.

The simplest way to think of Evals is as a set of checks to know if something is good or not. And they depend greatly on the type of work being done. They can be extremely simple, or elaborate and complex.

A set of Evals for a report, for example, might be something like:

* ✅ All the facts in the report are accurate
* ✅ The data in the report is no more than a year old
* ✅ The report does not include any mentions of \_\_\_\_
* ❌ The topic of \_\_\_\_\_\_ was addressed in the report
* ✅ There are no spelling or grammatical errors

So in this case we have five components to this report Eval. And this particular report passed 4/5. And in that case, if a "good" report is one that can pass all 5, then we know how to hill-climb towards a "good" report. We simply need to get to 5/5.

Or we could have a rating system where 4/5 is Good, and 5/5 is Excellent....but....4/5 would not be Good if criterion #1 (accuracy) were false. It's up to us how we set it up.

### Types of evals [​](#types-of-evals)

There are lots of different types of Evals. Here are a few so you can see how powerful these are in combination:

* ❓A simple check (are there any misspellings)
* ❓Which one of these is better? (asking AI to judge between two things)
* ❓Where on this scale does this report fall (asking AI to judge between Critical, High, Medium, Low, or whatever)
* ❓Does it match the answer we already know is right? (comparing the output to a reference answer)
* ❓Does it contain this exact thing? (a plain code check for a required phrase, link, or field, with no AI involved)
* ❓Is it in the right shape? (correct length, valid format, every required section present)
* ❓Is this claim actually true? (checking each fact against a source)
* ❓How does it score on each part of a rubric? (AI grading against a written scale, like 1–10 for clarity where 10 is defined in advance)
* ❓Which of these twenty is best? (a tournament, where AI compares them two at a time until one wins)
* ❓Did it actually work? (running the code, clicking the button, or loading the page and seeing if it does what it s...