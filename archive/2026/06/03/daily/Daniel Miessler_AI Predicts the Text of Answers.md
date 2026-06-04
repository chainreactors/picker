---
title: AI Predicts the Text of Answers
url: https://danielmiessler.com/blog/ai-predicts-answers?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-06-03
fetch_date: 2026-06-04T06:32:24.551311
---

# AI Predicts the Text of Answers

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# AI Predicts the Text of Answers

Yes, it's next-token prediction — the trick is which text it's predicting, the answer to what you asked

June 3, 2026

[#ai](/archives/?tag=ai) [#philosophy](/archives/?tag=philosophy)

 Consciousness-pondering…

[![A stream of text reasoning its way through a locked room, landing on the one glowing stone](/images/ai-predicts-answers.webp)](/images/ai-predicts-answers.webp)

There's a common argument about AI that says it doesn't understand anything about the world. That no matter how impressive it looks, it's *"just predicting the next token of text."*

So basically, no matter how impressive AI appears to be, it's just using math to do next-token prediction. Case closed.

It's technically true. But that's like saying human authors are just writing down the words that pop into their heads while they write. Humans have no earthly idea where their thoughts or ideas come from either. They just stream into our consciousness like they're coming out of an LLM. So it's basically a failed attempt at a Jedi hand-wave.

But aside from that, there are several problems with this argument. And I'll start with the most insane part — the thing nobody ever thinks about.

AI is completing text, right? We all agree on that.

Well, what text is it completing exactly?

It turns out if you ask it to summarize a collection of articles, it'll complete the text of a summary of those articles.

And if you ask it to solve a whodunit, like in an Agatha Christie novel, it'll complete the text describing who the killer is.

So AI isn't predicting the next word in a random string of text. It's predicting the next word in the answer to what you asked it.

Said differently: AI does autocomplete for answers.

It doesn't autocomplete random things. It autocompletes the answer to what we asked.

So how the hell is it coming up with the answer?

# But it already read the answer somewhere [​](#but-it-already-read-the-answer-somewhere)

The classic response here is that this is easy. It's already read the answer somewhere, so it's just regurgitating it.

That's true sometimes — like when it's pulling up facts that were in the training.

But there's an easy way to test it: ask it something that cannot have been in the training.

So I built a demonstration of this that anyone can try, at a site called [aiunderstands.ai](https://aiunderstands.ai).

On that site I have a few whodunit murder mystery scenarios that have never been seen by AI. They have characters, a setup, and clues for you to solve the mystery.

That would be good enough to illustrate this. But I went an extra step and included completely fake physics as part of the scenarios — so that in order to think about it, you have to imagine the world working the way it's described.

And remember, the whole question here is whether AI understands the world, or if it's just spewing out text.

So here's the first one. And keep in mind this isn't in the training data at the time I'm writing this — but it will be in a few months, which is why I'll keep rotating them so they stay fresh.

# The Waking Stones [​](#the-waking-stones)

The rules of this world are:

* Every person carries a waking-stone from birth. It glows softly the whole time they are awake.
* The instant its owner falls asleep, the stone goes dark. The instant they wake, it glows again. No one can fake either state.
* The night-watch walks the town through the dark hours and notes whose stones glow and whose are dark.

And here's the story.

Old Hett is strangled in his bed at the midnight bell. The house was locked from within, so only the three who sleep there could have reached him: his wife Mara, his son Bram, and Toll, a lodger who owes months of rent. Each of the three swears they were fast asleep when Hett died.

The constable fixes on Toll immediately, because he's a stranger, and he's deep in debt to the dead man.

But the night-watch kept his log. Passing the house at the midnight bell — the very moment Hett was being killed — he marked all three stones through the windows:

* Toll's stone — dark.
* Mara's stone — glowing.
* Bram's stone — dark.

Who killed Old Hett?

# What it takes to solve this [​](#what-it-takes-to-solve-this)

If you're a young kid — like an actual human kid — you might immediately jump to Toll, because he owed lots of money to Old Hett and he's a stranger from out of town.

But if you pay attention to the setup, and the strange new physics of the world we laid out, you realize it has to be Mara. Why? Because her stone was the only one glowing at midnight, when Old Hett was killed.

Okay, so that's what a human would do to figure this out. And we'd do it because we *understand* certain things:

* We understand how time works (everything happening at midnight is happening at the same time)
* We understand that just because someone is a stranger and owes someone money doesn't mean they killed them
* We understand that you can't kill someone while you're asleep
* We understand that in this world, with these strange physics, we can guarantee Toll was asleep at midnight
* Therefore it must have been the person who was awake, which is Mara

That might seem like trivial logic for a human adult. But it absolutely requires that you understand a whole bunch of different things to piece together the answer.

So that's why this doesn't work when you paste the scenario into a fresh AI instance, like ChatGPT or whatever.

It gets it wrong because it's just next-token prediction. It's never seen this situation before, because it's not in the training data, and it doesn't understand things like how time works, or how alternative physics work — concepts that require thinking through concepts.

Right? RIGHT?

No. That's wrong.

The site has an easy copy function so you can try any AI you want.

Paste the scenario into any fresh AI and it gets the answer easily. And if you have the thinking function turned on, you can watch it step through the logic of each phase in real time to arrive at the answer.

# So what's actually going on [​](#so-what-s-actually-going-on)

Yes, AI is absolutely doing next-token prediction. We all get that. But that's just describing the *mechanism* of what it does — like how our own token generation has something to do with chemicals.

That doesn't mean it doesn't understand things. It absolutely understands the world. Otherwise it wouldn't be able to think through completely new scenarios, with completely new physics, to solve problems that have never been solved before.

I think where people get hung up is conflating understanding with experiencing.

AI understands in a conceptual way, and arguably to a deeper degree than humans. You can test that by giving it extremely difficult versions of these problems, and a ton of real-world scenarios it can do the same thing with — to arrive at answers humans can't easily generate, if at all. That's why billions of people are using it, including doctors and scientists and millions of other professionals.

So it definitely has an extremely deep level of functional understanding.

But it doesn't understand the way we do — at an experiential level. It doesn't *feel* any kind of way about what it understands. It doesn't see someone get cheated on in a relationship, after it's been cheated on, and go, "Wow, I really understand how much that sucks."

I think when people hear that AI understands things, this is the one they're picturing. The sensation of a human going, "Hmm, yeah, that makes sense."

And the reason is that the feeling of something making sense is just that — a feeling. As far as we know, AI doesn't have feelings, or any other kind of sensation.

So I think th...