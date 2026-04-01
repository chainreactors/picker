---
title: Manual Context is a Bug
url: https://parsiya.net/blog/manual-context-is-a-bug/
source: Hackerman's Hacking Tutorials
date: 2026-03-31
fetch_date: 2026-04-01T04:45:24.735869
---

# Manual Context is a Bug

# [Hackerman's Hacking Tutorials](https://parsiya.net/)

## The knowledge of anything, since all things have causes, is not acquired or complete unless it is known by its causes. - Avicenna

Navigate…» About Me!» Cheat Sheet» My Clone» Source Repo» Manual Work is a Bug» The Other Guy from Wham!

* [About Me!](https://parsiya.net/about/ "About Me!")
* [Cheat Sheet](https://parsiya.net/cheatsheet/ "Cheat Sheet")
* [My Clone](https://parsiya.io/ "My Clone")
* [Source Repo](https://github.com/parsiya/parsiya.net "Source Repo")
* [Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520 "Manual Work is a Bug")
* [The Other Guy from Wham!](https://www.google.com/search?q=andrew+ridgeley "The Other Guy from Wham!")

Mar 31, 2026
- 11 minute read - [AI](https://parsiya.net/categories/ai/) [Soapbox](https://parsiya.net/categories/soapbox/)

# Manual Context is a Bug

* [.nfo](#nfo)
  + [[greetz]](#greetz)
  + [[anti-greetz]](#anti-greetz)
* [Why Should I Read This?](#why-should-i-read-this)
* [Rough Blueprint](#rough-blueprint)
  + [Clone Creation](#clone-creation)
  + [Clone Consumption](#clone-consumption)
  + [Clone Cultivation](#clone-cultivation)
* [Human in the Loop](#human-in-the-loop)
* [Tools and Customization](#tools-and-customization)
* [The Concept of AI-Docs](#the-concept-of-ai-docs)
  + [AI Needs to Learn Something](#ai-needs-to-learn-something)
  + [I Need to Learn Something](#i-need-to-learn-something)
* [How do I Get Started?](#how-do-i-get-started)
* [What Did We Learn Here Today?](#what-did-we-learn-here-today)

I wake up and read the news. Daniel Miessler has only declared my job dead three
times this week. Another frontier lab has found a bazillion bugs. Half of
LinkedIn is "SAST is dead." The war is, well. Welcome to the age of AI.

In this blog I reflect on "Manual Work is a Bug" and on how AI has changed my
workflow. I introduce the (not so novel concept) of "AI-Docs." A knowledge base
for both humans and AI. Similar to our manual knowledge base, you should not
have to manually fill the context except during the initial creation; the LLM
should have everything it needs on hand.

Note: I will use LLM and AI interchangeably in this post. Please don't tell
Yann LeCun. He has 1 billion in seed funding and powerful friends.

# .nfo

I've decided to write more and more loosely. I've become this sort of influencer
wanna-be that writes "only the good stuff that gets into [tl;dr sec](https://tldrsec.com/)." Your
newsletter is super awesome, Clint, and being included is an honour, but it's
the bonus, not the goal.

I never had an online edgy teenage phase because I chose the wrong country and time
to be born in. I programmed on paper until 19 and my family got our first
computer at 25[1](#fn:1). So please bear with me as I cosplay as a scene hacker 20
years too late.

## [greetz]

Those who made this possible:

* Me: Your illustrious host.
* Song: [Mai Yamane - Tasogare](https://www.youtube.com/watch?v=IhCDK_pSjnk).
* Book: [John Joseph Adams - Anthology - Dead Man's Hand](https://parsiya.io/literature/bookreviews/#deadmanshand).

## [anti-greetz]

New AI-Slop patterns:

* `it's not ___, it's ___.`
* `→`, the new em-dash.

# Why Should I Read This?

[Manual Work is a Bug](https://queue.acm.org/detail.cfm?id=3197520) is my favorite technical post of all time. It's a
permanent link on top of the blog. I want to use LLMs to create, consume, and
cultivate clones so I fill LLM context with correct info automatically. Because
`Manual Context is a Bug`.

![Image Credit: (apparently) Boyhood (2014)](01.webp "Image Credit: (apparently) Boyhood (2014)")
Image Credit: (apparently) Boyhood (2014)

I was living in VS Code and wrote everything in markdown before it was cool. You
can read my few blog posts about creating clones at
<https://parsiya.net/categories/clone/>. This website, <https://parsiya.io> and a
load of wikis/docs at every job I've had are the results.

A clone is an index of knowledge for me so I don't have to remember things.
Everything I do and learn is documented. If you've worked with me (or at the
places I've worked), you've seen my work wiki.

I am not AGI-pilled (lol)[2](#fn:2). I think LLMs are very useful at specific tasks
like summarization, and mimicking instructions (agents/skills are just
documentation). The clone can be a supercharged knowledge base for both you and
your AI.

Whether you like this or not depends on your use case. GenAI is a great and
versatile tool. This means people will use it for a large variety of tasks and
unlike what LinkedIn says, there's no single correct way to use it.

# Rough Blueprint

We have one thing going for us. LLMs are chat bots and have been trained on
natural language so they don't really care how the documentation is
written[3](#fn:3). Our clone can be readable to humans and still be useful
for agents.

> You're not gonna get left behind mate, it's all markdown, anyways!

This process has three steps:

1. Clone creation: Capturing knowledge.
2. Clone consumption: Retrieving and applying knowledge.
3. Clone cultivation: Refining knowledge.

## Clone Creation

Before, if I wanted to learn something, I would:

1. Search a topic.
2. Read docs/blogs and learn how to do something.
3. Document it in a series of steps.
4. Store it in my clone.

With LLMs:

1. Search a topic. Skim through the results to get a high-level understanding (this is key).
   1. Agents can search the results and do the summary for you, but I do not
      trust them until I've learned the high-level concepts to judge the output.
2. Ask AI how to do something and supply the model memory with docs/blogs.
3. Tell AI to document it.
4. Review it. Edit it manually and iterate with AI until I am satisfied.
5. Task AI to document it in the clone.

## Clone Consumption

Before, I used my knowledge base like this:

1. Search for something in the clone.
2. Read it and follow the steps.

After LLMs:

1. Ask AI a question.
2. AI searches in the clone.
3. AI summarizes the result.
4. If correct, have AI do the task or better yet, write code to do the task.
   1. Do the manual tasks myself.

## Clone Cultivation

Knowledge becomes outdated and usually I can improvise when repeating the task.
So we need to reiterate. This is generally a subset of clone creation so I will
not reiterate (har har).

# Human in the Loop

I don't just yolo write text to the clone. I am a strong believer in "human in
the loop." Users should be responsible for AI output created by them, on their
behalf, or by systems they have created. AI is a tool, not a sentient being (at
least not yet). You willed the output into existence, tag, you're it! To quote
President Truman "The Buck Stops Here."

[Embed from Getty Images](https://www.gettyimages.com/detail/515403964)

The internet and by proxy, infosec is flooded by AI-generated content. My
manager posted to LinkedIn about an opening on our team a few months ago. By
accident, I found this completely AI-generated article
[Your Ticket to Microsoft’s SERPENT: How to Build the Skills They're Actually Hiring For + Video](https://undercodetesting.com/your-ticket-to-microsofts-serpent-how-to-build-the-skills-theyre-actually-hiring-for-video/).

While I am thrilled to be called "elite internal red team," we're not even a red
team and the stuff mentioned in the article is, well, not really that useful
for us. I don't remember the last time I ran nmap (imagine running that on our
internal network), did XDR evasion, or created a C2.

**Moral of the story: You're responsible for stuff published under your name. I
will not read your AI-generated shit, at best I will pass it to AI to
summarize.**

# Tools and Customization

There's a growing pile of gizmos to make AI do actions and make it
"deterministic." MCP, agents, skills, and instructions to name a few. MCPs are
the future, actually no, skills are, wait, agents are the end game, just tell AI
to call the API. Who knows, maybe by the time you read this, there will be
a...