---
title: 6 Phases of the Post-GPT World
url: https://danielmiessler.com/blog/6-phases-post-gpt-world/
source: Daniel Miessler
date: 2023-03-28
fetch_date: 2025-10-04T10:55:53.249456
---

# 6 Phases of the Post-GPT World

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# 6 Phases of the Post-GPT World

March 27, 2023

[#ai](/archives/?tag=ai) [#business](/archives/?tag=business) [#creativity](/archives/?tag=creativity) [#cybersecurity](/archives/?tag=cybersecurity) [#ethics](/archives/?tag=ethics) [#future](/archives/?tag=future) [#society](/archives/?tag=society) [#technology](/archives/?tag=technology) [#top](/archives/?tag=top)

![6-phases-miessler-mj](/images/f38104c7-5092-4dec-989e-c15165933220-6-phases-miessler-mj.png)

1. [Companies Become Models/APIs](#companies) >
2. [People Become Models/APIs](#people) >
3. [AI Assistants](#assistants) >

1. [Content Authentication](#authentication) >
2. [Knowledge Work Replacement](#jobs) >
3. [The Creativity Explosion](#creativity) >

## Introduction

We’ve all seen the non-stop stream of news from OpenAI. First we see GPT-4, where you have the announcement on Tuesday morning and you basically have thousands of companies launched by sundown.

And then we see [chatgpt plugins](https://openai.com/blog/chatgpt-plugins?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world) > drop, which are basically ways of implementing entire businesses as plugins! This is what I said when Brockman dropped the web search plugin.

Then you’ve got Midjourney, which is putting out some insane stuff, with a special focus on realism. I used it to make this image of Bernie Sanders as a DJ.

![bernie-dj-mj](/images/0527079e-20ca-4663-b437-c8eb6da3f822-bernie-dj-mj.png)

Deep socialist beats, and the hands are improving

Predictions are hard, especially about the future.

Anyway, things are nuts right now. But what I’m going to talk about in this piece isn’t GPT-4, or MidJourney, or [how to make awesome prompts](https://danielmiessler.com/blog/response-shaping-how-to-move-from-ai-prompts-to-ai-whispering/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) >. What I’m going to talk about is **what happens to tech and society** as a result of all these technologies.

This is the tech I think will logically follow GPT-4 and ChatGPT Plug-ins, and how it will affect jobs, society, and basically the world. As we go through each one, think about which best suits you and which ones you’re going to play in. Let’s look at the first one.

This is already happening via [ChatGPT Plugins](https://openai.com/blog/chatgpt-plugins?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world) >.

## 1. Companies become custom models and APIs

Our current companies that display their wares through websites, catalogs, and legacy software with databases and SQL queries will go away. They’ll be replaced by custom GPT models that ingest everything that makes up that business.

[SPQA](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) > is one likely architecture for this.

* Instead of writing traditional software, companies are going to dump all their data into custom GPT models
* That’s all the log data, all their documents, all their voice calls, all their meeting transcripts, all their finances, etc. Basically everything
* This data will be combined with another model where the leaders of the company define its mission, its goals, its challenges, and its strategies
* Combining these models with a massive LLM like GPT-6 (or whatever is available at the time) will change the interface to companies from statically coded queries to a brittle database schema
* Instead you’ll just ask questions and give commands
* And the way you make your services available will be through such queries, i.e., asking normal human questions that hit your company’s models via API

## 2. We (humans) become custom models and APIs

First it’ll be companies, then it’ll be us.

Now that we can ingest the content of businesses, what comes next? Ingesting the content of people!

Both businesses and people have missions, goals, and KPIs.

Just as businesses have logs and Google Docs, we’ll upload all our journals, our blogs, every picture of us from birth, our Twitter feeds, our Instagram, our friend connections, etc.

But not just our past, also our mission in life, our goals, our preferences, our food likes and dislikes, our favorite celebrities, our favorite art, culture, and music, etc. Don’t worry, there will be interview services that talk to you for hours to extract all of this. It’ll be [the SPQA model](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=6-phases-of-the-post-gpt-world&last_resource_guid=Post%3A3e1b76ca-c4c5-4551-aca4-5e005795af1d) >, just for people.

![phases-miessler-2-mj](/images/0c60a2ed-71e1-4987-a755-0293b003307f-phases-miessler-2-mj.png)

MidJourney’s interpretation of this article

* Imagine being able to instantiate a version of yourself based on everything GPT-7 + this custom model knows about you
* It knows your past, your hang-ups, your preferences, your desires, your traumas, your loves and your hates
* Now you can spin up a therapist AI and have it interview the AI version of yourself, and create a report to give your actual meatspace therapist
* You can talk to younger versions of yourself
* And without spinning off into orbit for this article (I’ll do this in a separate piece), this will also become the new holy grail for immortality
* We’ll upload our full genome, petabytes of knowledge about you and everything that shaped your upbringing. Interviews. Video footage. History. Everything. All that becomes context in the construction of you
* That gets stored as a model of you when you die, and the new "cryo" companies will use that as the thing they inject into the new body/brain when that tech becomes available

Anyway, that last one is a distant use case. But it’s tied to the human desire to survive, so it’s as inevitable as moisturizer.

The more immediate uses will be instantiations of ourselves for self-exploration and to present as APIs for interaction with the APIs of others, e.g., exchanging preferences, mutual desires, shared goals, social lubrication, meet-ups at scale, synchronized social experiences, etc.

## 3. AI assistants

It’s hard to predict the actual order here. Maybe they evolve together.

The next thing that happens—and again, this one is already starting as well—is we’ll create models that have one purpose: advocating on our behalf 24/7.

* We’ll shape an AI persona to be a friend to us (or a service will pick a persona for us) that knows us inside and out
* It’ll know us because it’ll have access to our self-Model created in step 2. Maybe they’ll be the same model. Who knows
* And from there it will advocate for us by regularly checking the current state of the world around us (our location, the last time we ate, whether we’re in conversation or not, if we have upcoming meetings, a big date tonight, etc.)

![interpretation-2-miessler-mj](/images/70a96b9e-f9dc-41c9-98a8-2ce51365e03d-interpretation-2-miessler-mj.png)

Another MJ interpretation

* It’ll do things for us. It’ll make reservations for us, it’ll request that the channel in the sports bar changes to our favorite sport. Yes, the sports bar has a daemon (API) as well. It’ll ask if you want to order your favorite shorts that just went on sale, etc.
* In other words, it’ll never sleep. It’ll read all the world’s APIs looking for things that will help you, collecting the latest deals, news, ideas, etc. and getting them ready for you when you next check the news
* Of...