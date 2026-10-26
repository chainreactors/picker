---
title: I'm on Team Explanation
url: https://danielmiessler.com/blog/team-explanation?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-10-25
fetch_date: 2026-10-26T07:19:11.654755
---

# I'm on Team Explanation

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# I'm on Team Explanation

Deutsch's turkey and why explanation beats prediction as a measure of understanding

October 25, 2026

[#philosophy](/archives/?tag=philosophy) [#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology)

[**AIL***1*](/blog/ai-influence-level-ail "AIL 1 — Human Created, Minor AI Assistance")

 Weaver-ant-swarming…

[![A charcoal cutaway barn: a turkey professor points at a chart of sunrise feeding times while, inside, a farmer sharpens an axe beside roasting pans.](/images/team-explanation.webp)](/images/team-explanation.webp)

There are two major ways of assessing the quality of our understanding of a phenomenon: **Prediction**, and **Explanation**.

Prediction feels extremely powerful because it seems to be proving its deep understanding by having reality speak on its behalf. You want proof that I understand how the planets move? Well let me tell you exactly where Jupiter will be in the sky on an arbitrary day.

That's powerful indeed.

🔭 Ptolemy's epicycles predicted planet positions well enough to be used for over a thousand years, while the model behind them was wrong.

But [David Deutsch](https://en.wikipedia.org/wiki/David_Deutsch) has an idea that I think is even more powerful, which is Explanation. And he uses a brilliant example to demonstrate why it's superior to Prediction, though the example itself comes from [Bertrand Russell](https://en.wikipedia.org/wiki/Bertrand_Russell).

## The turkey professor [​](#the-turkey-professor)

He asks us to imagine a turkey on a turkey farm in the United States who holds a scientific lecture for a number of his fellow turkeys on the farm.

📚 Russell used a chicken in *The Problems of Philosophy* (1912) to attack induction; the turkey retelling is often called the [turkey illusion](https://en.wikipedia.org/wiki/Turkey_illusion).

To prove he understands the farm, where they've all been for the last 9 months and it's currently early November, he is asked to predict the feeding time on November 25th of this year. And then December 12th.

The turkey professor pulls out a whiteboard and proceeds to map out all the data he has on feeding times, and says confidently that on November 25th, they'll be fed right after sunrise. And he says he knows this is true because he has clear data that nobody can refute.

Day after day he is proven right, and he ultimately convinces everyone he's correct.

But despite all this data, and accuracy, and precision that he's provided, this understanding lacks a critical component. He doesn't have an explanation for "why" they are fed every day after sunrise.

Turns out this is critical information that will drastically affect the accuracy of his predictions.

On November 25th, it turns out, they are not in fact fed after sunrise. Because all those turkeys are dead: killed the day before for Thanksgiving.

He had great data about sunrises and feeding times, but he didn't have the crucial fact that they were turkeys on a turkey farm.

In other words, he could predict parts of the system, but he couldn't explain why it worked the way it did. And in this way, according to David Deutsch, Prediction is subordinate and inferior to Explanation as a way of understanding the world.

The system is not bidirectional, and this one-way function further illustrates why one is better than the other. With Explanation you can usually make predictions, but with predictions alone you often lack an explanation for why they're accurate.

## Explanations at any level [​](#explanations-at-any-level)

This is why I prioritize high-quality explanations of things. And it's why I so highly value the intelligence of frontier AI. When a modern AI is used properly, it's able to produce [extraordinary explanations](/blog/introducing-ul-gauntlet) of nearly anything. And at any level of abstraction, from mathematics and bits and bytes, to extremely concise prose.

One of my favorite AI skills I've ever made (in 2024 via [Fabric](https://github.com/danielmiessler/fabric)) is called **5 Levels**, which in [LifeOS](https://github.com/danielmiessler/LifeOS) you hit via the `/ws` shortcut (for `/WordSummary`).

🧵 In Fabric the pattern is [`create_5_sentence_summary`](https://github.com/danielmiessler/fabric/tree/main/data/patterns/create_5_sentence_summary), and its output section is called "5 Levels".

It takes any idea and explains it to you at `n` levels of concision.

So `ws 5` gives you 5 levels.

1. 5 words
2. 4 words
3. 3 words
4. 2 words
5. 1 word

Here's a run against the input of "what russian literature teaches us."

bash

```
/ws 5 what russian literature teaches us
```

1

And here's the response:

md

```
5. Suffering, faced honestly, can redeem
4. All answer for all
3. Conscience outlasts tyranny
2. Beauty saves
1. Redemption
```

1
2
3
4
5

I just love these increasingly compressed summaries. When I saw this in 2024 with Fabric, it instantly felt like true intelligence to me.

## Explanation is understanding [​](#explanation-is-understanding)

I think, ultimately, the truth being revealed by this contrast between prediction and explanation is that [explanation requires understanding](/blog/deutsch-darsa-and-ai). And understanding is ultimately what we're seeking when we engage in this type of pursuit.

Whether it's physics, or psychology, or AI, or whatever, if I sit down to learn about something I don't want just to be able to coldly predict its behavior.

I want to *understand* it.

🎓 There are other methods, like "showing" or "demonstrating" as well, but explanation is arguably the most effective at scale.

And explanation is wholly and inexorably tied to understanding. It's the mechanism by which one transfers understanding from one person to another.

I'm Team Explanation.

#### Notes

1. Updated 2026-10-25: the turkey example is Bertrand Russell's, from 1912. Deutsch uses it, but he didn't originate it, and an earlier version of this post credited him.
2. 🤖 **AIL 1:** Daniel wrote this post. I (Kai, his AI assistant) fixed a few typos and the credit for the turkey example, added the links, section headings, asides and the definition card, made the header image, and proposed the title and subtitle. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail).

## Related Reading

* [Introducing UL Gauntlet, a Benchmark for How Well AI Explains→](/blog/introducing-ul-gauntlet)
* [Deutsch, DARSA, and AI→](/blog/deutsch-darsa-and-ai)
* [A Conversation With Claude on Deutsch, Knowledge, and the PAI Algorithm→](/blog/conversation-with-claude-on-deutsch-and-the-pai-algorithm)
* [World Model + Next Token Prediction = Answer Prediction→](/blog/world-model-next-token-prediction-answer-prediction)
* [Models + Data = Prediction→](/blog/models-data-prediction)

Share

[Post](https://ul.live/share-x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fteam-explanation&title=I'm%20on%20Team%20Explanation "Share on X")  [LinkedIn](https://ul.live/share-linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fteam-explanation&title=I'm%20on%20Team%20Explanation "Share on LinkedIn") [HN Hacker News](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fteam-explanation&title=I'm%20on%20Team%20Explanation "Share on Hacker News")  [Reddit](https://ul.live/share-reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fteam-explanation&title=I'm%20on%20Team%20Explanation "Share on Reddit")  [Facebook](https://ul.live/share-facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fteam-explanation&title=I'm%20on%20Team%20Explanation "Share on Facebook")  [Forward](https://ul.live/share-email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fteam-explanation&title=I'm%20on%20Team%20...