---
title: How to Think About the Difference Between Choice and Score in Jev
url: https://danielmiessler.com/blog/jev-choice-vs-score?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-09-22
fetch_date: 2026-09-23T06:54:52.164476
---

# How to Think About the Difference Between Choice and Score in Jev

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# How to Think About the Difference Between Choice and Score in Jev

Both return probabilities; the difference is whether the options form a ladder

September 21, 2026

by Daniel Miessler

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#tutorial](/archives/?tag=tutorial)

[**AIL***2*](/blog/ai-influence-level-ail "AIL 2 — Human Created, Major AI Augmentation")

 Pentesting…

First, if you want to understand Jev at a deep level, [this Latent Space interview](https://www.youtube.com/watch?v=cFx9Z3ZXca0) with [Diogo Almeida](https://typesafe.ai/team), the [TypeSafe](https://typesafe.ai) co-founder who built it, is currently the best resource I know of. Most of the update below comes from it.

One thing that has been tripping me up with [Jev](/blog/early-thoughts-on-jev) is the difference between [choice](https://docs.typesafe.ai/primitives/choice) and [score](https://docs.typesafe.ai/primitives/score). I keep mixing them up.

I finally took the time to grapple with and deep dive on it, and I came up with a better way of describing it to myself, which I will share here.

They're both actually returning probabilities. So I was like, well, if they're both choices that are scored by probability, why not call them both choice? Or more importantly, why have a score one that's separate from choice, if score is just giving you back probabilities on the options that you gave, just like with choice?

Score is very similar to Choice in many ways, but the main difference is you provide it in order, as a ladder.

So it's like:

* Cold, warm, hot.
* Or for security: critical, high, medium, low.
* Or for customer service: about to cancel, super agitated, and so on.

Between the structure you use, the way you phrase the inputs, and the state you pass in as context, the system understands that it's looking at a scale. So it does a better job of ranking the options.

In the case of choice, you just get probabilities for whatever list you provide, and it could be in any order because it's not [on a scale](/blog/chart-scale-types).

> Nominal Scale: Only the selection name matters, not any particular order. Ordinal Scale: Only the order matters, but you can't tell the relative difference between the items.[Chart Scale Types (2021)](/blog/chart-scale-types)

[![Technical diagram: one state-plus-instructions input feeding two question shapes, choice as three equal unconnected boxes and score as an ordered ladder from cold to hot, both returning a probability per option](/images/jev-choice-vs-score-diagram.webp)](/images/jev-choice-vs-score-diagram.webp)

choice is an unordered set, score is an ordered ladder, and both hand back a probability per option

So in my mind, I'm going to think of these as choice and scale instead of choice and score, because both of them provide scores.

**Update:** The day after I wrote this, [Diogo Almeida](https://typesafe.ai/team), the [TypeSafe](https://typesafe.ai) co-founder who built Jev, went on [Latent Space](https://www.youtube.com/watch?v=cFx9Z3ZXca0) and explained the three primitives himself. It confirms the ladder idea, and it gives a cleaner way to hold all three in your head. Each one maps to something you already do in code.

> I think these map all to programming primitives, where choice maps into a switch statement on an enum. Nouls map to if statements, and scores map to sorting or thresholding at a greater-than or less-than.[Diogo Almeida, Latent Space (2026)](https://www.youtube.com/watch?v=cFx9Z3ZXca0)

So the test is what your code does with the answer. If it's a `switch` over unordered options, that's a choice. If it's an `if`, that's a noul. If it's a sort or a threshold, that's a score. The greater-than is the ladder. You can sort critical, high, medium, low. You can't sort Korean, Mexican, Thai.

[![Technical diagram: three columns, noul asking is this true and returning 0.91 into an if, choice asking which one and fanning to three unordered boxes into a switch, score asking how much and dropping into an ordered ladder from critical to low into sort or threshold](/images/jev-three-shapes-diagram.webp)](/images/jev-three-shapes-diagram.webp)

the three question shapes and the code each one turns into

He also explained why none of them are plain programming types, which is probably why I kept mixing them up:

> All three of these are actually new concepts. These are not types that exist in programming, and that was intentional, because they map very closely to types but they're not quite that. A score is not an int. So if you had Instructor or Pydantic or whatever map ints or floats into scores, you'd get a little bit cooked.[Diogo Almeida, Latent Space (2026)](https://www.youtube.com/watch?v=cFx9Z3ZXca0)

And on noul, since it sounds made up: it is. It's a chunk of Bernoulli, as in a [Bernoulli probability](https://en.wikipedia.org/wiki/Bernoulli_distribution). It's shaped like a boolean, true or false, but the answer comes back as a probability instead of a hard bit. That's why they wouldn't just call it a bool.

> Scores are similar to LLM judging, right? So if you want to call it a judgment, I guess you could. Maybe a noul could be a probability, but everything for us is a probability. And a choice is actually closest to a function call. A choice is just the right way of exposing a switch/match statement.[Diogo Almeida, Latent Space (2026)](https://www.youtube.com/watch?v=cFx9Z3ZXca0)

Everything returns a probability, so probability isn't what separates them. The type of question is what separates them. A pick from unordered options, a yes or no, or a position on a scale.

# Making use of these question types [​](#making-use-of-these-question-types)

The other thing he talked about that I found *super* interesting was why he's so excited about this tech, and what it provides. He says the right way to use this is to remember that this is for computer-to-computer communication, so you can be as OCD as you want with how you decompose things.

He says we should break our problems into lots of small questions instead of one big prompt. That's where the three shapes actually get really powerful.

> I truly recommend asking lots and lots of questions. Break them down, make them smaller, and really decompose, no matter if the models can do it today or not. If you decompose problems into simple decisions, every single one of these things is extremely evaluable.[Diogo Almeida, Latent Space (2026)](https://www.youtube.com/watch?v=cFx9Z3ZXca0)

> System messages are like disgusting global variables where you just put everything in there and you put all the instructions at once, and then you hope that every single instruction gets nailed, instead of asking the questions in parallel.[Diogo Almeida, Latent Space (2026)](https://www.youtube.com/watch?v=cFx9Z3ZXca0)

[![Technical diagram: on the left one big system message feeding a cloud labeled hope and an output with a question mark; on the right a state box fanning into five small typed questions, each with a probability and a threshold, all feeding a box labeled code decides, with a test case stamp pointing at one question](/images/jev-decompose-diagram.webp)](/images/jev-decompose-diagram.webp)

one big prompt versus many small questions, each one evaluable on its own

I'm specifically implementing this for our ISCs within ISAs, i.e., specific build/test criteria.

So the unit of work is the smallest question you can ask about your state, and each one is one of the three shapes:

* Is this true? That's a noul.
* Which of these is it? That's a choice.
* How much of this is it? That's a score, and you pick the threshold.

His example is refusals. Instead of asking "sho...