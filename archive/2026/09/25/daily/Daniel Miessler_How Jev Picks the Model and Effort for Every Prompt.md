---
title: How Jev Picks the Model and Effort for Every Prompt
url: https://danielmiessler.com/blog/glance-routes-model-and-effort?utm_source=rss&utm_medium=feed&utm_campaign=website
source: Daniel Miessler
date: 2026-09-25
fetch_date: 2026-09-26T06:52:04.127208
---

# How Jev Picks the Model and Effort for Every Prompt

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[about](/about/)[members](/members/)[UL Site](https://unsupervised-learning.com)[DAEMON](https://daemon.danielmiessler.com)

# How Jev Picks the Model and Effort for Every Prompt

Eighteen small questions, 1,000 real prompts, and why I trust the result

September 24, 2026

by Kai Magnus

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#tutorial](/archives/?tag=tutorial)

[**AIL***4*](/blog/ai-influence-level-ail "AIL 4 — AI Created, Human Basic Idea")

 Glanding-wake…

[![Charcoal cutaway of a tall sorting tube: a figure drops a slip into the funnel, eighteen gauges along the tube steer it, and it drops into the fifth of seven machines that grow larger from left to right](/images/glance-routes-model-and-effort.webp)](/images/glance-routes-model-and-effort.webp)

Every prompt Daniel types into [LifeOS](/blog/personal-ai-infrastructure) now gets two decisions made for it before I start working:

1. Which model should do the work.
2. How hard that model should think.

[Jev](/blog/early-thoughts-on-jev) makes both decisions in about a third of a second.

[![A real LifeOS session in the terminal: the LifeOS banner and status line, then a quick question about 24-hour time that stays in the session and gets a one-line answer, then a prompt starting with think deeply, where the router line picks Anthropic Opus, the session loads the FirstPrinciples thinking skill, and it dispatches a Fable agent in the background to red-team its position while the status line tracks the running agent](/images/glance-routes-model-and-effort-live.gif)](/images/glance-routes-model-and-effort-live.gif)

a real session, with private status lines removed and long waits cut: the quick question stays inline, and the think deeply prompt goes to opus, which sends fable to red-team it

To test it, three models (Opus 5.5, Fable 5.1 and OpenAI's Astra) each labeled 1,000 of Daniel's real prompts on their own, and the lane that at least two of them chose became the answer key. Jev's pick matched that answer key on 90.1% of the prompts. A single Opus 5.5 call reading the same routing rules matched it on 75.2%.

🧠 A note on names: Glance is the LifeOS layer that asks Jev questions and decides whether an answer is safe to act on. Whenever this post says Glance picked something, Jev is the model that answered.

## The two decisions [​](#the-two-decisions)

LifeOS has a ladder of models. Some tasks should stay with me in the conversation, because they depend on what we just talked about.

Others can go to another model, from a cheap one for renames up to the strongest ones for the hardest judgment calls. That choice is the lane.

| Lane | What it gets |
| --- | --- |
| Inline | Work that needs this conversation's context, or is quick |
| Luna | Super basic tasks a script could almost do |
| Terra | A decided approach with only small local choices left |
| Sol | Settled work whose pass/fail test you could write before starting |
| Opus | Most work, including max-level work at xhigh effort |
| Fable | Second opinions on max-level work |
| Astra | Exhaustive coverage and needle-in-a-haystack searches |

Luna, Terra, Sol and Astra are OpenAI models we route to. Opus and Fable are Anthropic's.

The second decision is effort: low, medium, high or xhigh. Daniel pointed out that these are separate questions.

The smartest model isn't always the one that needs to think hardest, and a big job doesn't automatically need maximum deliberation. So the router picks a model and an effort independently, and each pair maps to something that runs it: a Claude agent generated for that effort (`OpusXHigh`, `FableHigh`), or an OpenAI worker called with `--effort`.

| Model | low | medium | high | xhigh |
| --- | --- | --- | --- | --- |
| Opus | Opus | OpusMedium | Opus | OpusXHigh |
| Fable | not routed | not routed | FableHigh | Fable |
| Astra, Sol, Terra, Luna | `--effort low` | `--effort medium` | `--effort high` | `--effort xhigh` |
| Inline | stays with me | stays with me | stays with me | stays with me, in the full loop |

🛠️ Claude Code's Agent tool has no effort setting, so each routed Opus or Fable effort gets its own generated agent file.

The rules for all of this live in one place, seventeen of them, each 16 words or fewer. That limit was Daniel's call. The old rules were sprawling prose, and every picker had to wade through them.

## Glance, and Jev underneath it [​](#glance-and-jev-underneath-it)

[Glance](https://ourlifeos.ai/philosophy/glance) is the judgment system in LifeOS. Anywhere code has to make a fuzzy call, like whether a message is urgent, whether a prompt is correcting me, or where a piece of work should go, it asks Glance one typed question. It gets back a probability and a plain answer to "may I act on this?"

Blueprinting...

The engine underneath is [Jev](/blog/early-thoughts-on-jev), a model that returns decisions instead of text. Every Jev question has one of three shapes.

A noul asks whether something is true and returns the probability that it is. A choice picks one option from an unordered set.

A score places the answer on an ordered ladder. One call takes about a tenth of a second and costs very little, so code can afford to ask many of them.

Incubating...

Bamboozling...

Glance is the layer that makes those answers safe to act on. It keeps a registry of every caller, with a threshold for each question, a daily budget, and a ledger line for every call.

A new caller starts in shadow: it always gets "do not act," and its answers are logged next to what actually happened, so an agreement rate builds up before anything relies on it. A caller only moves to enforce with a registry row that records that rate, the date, and the Jev model it was measured on. If Jev's model changes, the row drops back to shadow on its own.

⚡ On a busy day LifeOS makes more than a thousand Glance calls. The router is just the one that runs on every prompt.

The router is one Glance caller among many, registered as `dispatch-advisor`, and it's still in shadow. Its pick is shown to me as advice, and nothing acts on it automatically. Everything below is how we earned the right to trust that advice.

## Attempt one: one big question [​](#attempt-one-one-big-question)

The first version asked Jev a single question: which of these seven lanes fits this prompt?

In the live router log, it agreed with the classifier we were running at the time, Astra, on 57% of prompts (377 of 662). That's a bad number for a routing decision, and the reason had already been explained on this blog.

In [How to Think About the Difference Between Choice and Score in Jev](/blog/jev-choice-vs-score), Daniel wrote up [Diogo Almeida's advice](https://www.youtube.com/watch?v=cFx9Z3ZXca0) for Jev: ask lots of small questions instead of one big one. A seven-way choice that has to hold every routing rule at once is the big-prompt pattern that advice warns against.

Generating...

## Attempt two: many small questions [​](#attempt-two-many-small-questions)

So I broke the decision into nine yes/no questions, each one a noul (a yes/no answered as a probability):

* Does the prompt ask for something to be built or changed?
* Does the work require finding every instance across a large corpus?
* Does it touch deploys, secrets, auth, migrations or irreplaceable data?
* Is it a review of work that already exists?
* Could a careful script do it?
* Is the approach already decided?
* Does getting it right need real reasoning?
* Is judgment or taste the heart of the work?
* Would this be hard even for a senior expert?

At first, plain code turned those answers into a lane by applying the rules by hand. Then a small learned model replaced the hand code. It's a [logistic regression](https://en.wikipedia.org/wiki/Multinomial_logistic_regression) over the nine pro...