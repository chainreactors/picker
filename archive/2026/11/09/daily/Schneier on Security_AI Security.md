---
title: AI Security
url: https://www.schneier.com/blog/archives/2026/11/ai-security.html
source: Schneier on Security
date: 2026-11-09
fetch_date: 2026-11-10T09:03:21.158493
---

# AI Security

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## AI Security

Two weeks ago, I attended the [[un]prompted](https://unpromptedcon.org/) AI security conference in San Francisco. It was an excellent event: three days of very dense talks about all aspects of AI security. (My talk was about integrous AI, and I will post it when it is online.)

AI security can be divided into three broad topics. It’s important for researchers to understand which one they are working on. And it’s important for us as a community to work on them all. They are: security of AI, security with AI, and security from AI. [un]prompted had good talks about all three.

Tags: [AI](https://www.schneier.com/tag/ai/), [conferences](https://www.schneier.com/tag/conferences/), [Schneier news](https://www.schneier.com/tag/schneier-news/)

[Posted on November 9, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/11/ai-security.html) •
[9 Comments](https://www.schneier.com/blog/archives/2026/11/ai-security.html#comments)

### Comments

gheese •
[November 9, 2026 8:04 AM](https://www.schneier.com/blog/archives/2026/11/ai-security.html/#comment-459535)

Looking forward to the recordings! I believe they’re not available yet, but I’ve bookmarked a couple of slide-sets already.

Rontea •
[November 9, 2026 12:28 PM](https://www.schneier.com/blog/archives/2026/11/ai-security.html/#comment-459537)

Reflecting on this today, the 37th anniversary of the fall of the Berlin Wall, I can’t help but think about how barriers—physical or digital—shape our world. Just as the Wall symbolized division and control, the challenges in AI security remind us that our defenses and safeguards can either isolate innovation or protect freedom. Our work in securing AI is about making sure that these new systems empower rather than imprison, building trust instead of walls.

Joshi •
[November 9, 2026 12:40 PM](https://www.schneier.com/blog/archives/2026/11/ai-security.html/#comment-459539)

“The World is built in a wall that separates kind. Tell either side there’s no wall, you’ve bought a war. Or a slaughter.“

* Blade Runner 2049

Clive Robinson •
[November 9, 2026 3:31 PM](https://www.schneier.com/blog/archives/2026/11/ai-security.html/#comment-459541)

@ Bruce, ALL,

With regards,

> “AI security can be divided into three broad topics”

Of Security “of / with / from” AI.

But each of those also needs to be considered in “Past / Present / future” tenses.

As we can tell from the Hugging face and subsequent incidents, to few researchers appear concerned about Past and Present tenses, and not sufficiently clued up for predicting yet alone acting on the future tense, which is quite worrying as the appear locked into a

“Fast dash to disaster” in the very near future, if not the present.”

But as people should realise Current AI, LLM and ML Systems have hardly developed of recent times.

With near all recent, current and proposed improvements being in the frameworks that give us agents…

With the big elephant in the corner being “Agent 2 Agent Communications”(A2AC) which unfortunately haemorrhages confidential information out into the world.

This is especially true when “tool stacks” in Python etc are also brought into play…

This tends to hit all the boxes of “of / with / from” in all the tenses of “past, present, future.

What makes it all worse is it’s been proved that guardrails at the input, output or both of an LLM will be bypass able by prompt injection and worse… But just to make the pill more bitter also by extention sandboxes as well will fail to be secure in any way if communications and external tool usage between agents is allowed.

I guess that realisation of this inconvenient set of truths is in part behind the turn from over priced, over hyped, external internet based “frontier models”, to less capable but isolated internal / local models.

But there is another “AI Security Issue” that is hiding in the dark waiting to happen and that is,

“Security of AI supply”…

Even before the Midterm “Blue Wave” it was abundantly clear that there is nowhere near enough LLM systems available and that they are “tuned wrong” for most productive uses.

The “jerk-circle” of playing Ring a Ring of Roses with “debt passing”… Means that there is a veritable tsunami of debt building rapidly and now coming due… And still no GigaWatt Data Center online and now unlikely to be any time soon… Unless it gets “tossed in the sea” not Space and uses locally generated “green energy”.

But hey “What do we know?” When even the AI industry apparently has not got a clue… And engineers and physicists staying within what the laws of nature allow are ignored whilst Hype burns the whole house down…

Clive Robinson •
[November 9, 2026 3:44 PM](https://www.schneier.com/blog/archives/2026/11/ai-security.html/#comment-459542)

@ ALL,

For those that are a little skeptical of some of what I say above,

Have a read of,

> **AI Agents Are Testing the Limits of Zero-Trust Security**
>
> As autonomous AI agents work together, verifying their actions, enforcing security policies, and maintaining accountability becomes increasingly difficult
>
> “*Several teams around the globe are leveraging AI by creating a task force of agents managed by an orchestrator and creating applications to support risk assessment, client profiling, match making, and information yield with a slight overview of decision making. One of the important components for these agents is to ensure that the logs are managed and historic relevance is not being used to avoid skewing towards same decision making. Thus, the system is expected to keep checkpoints in place where agents are prompted to delete such historic relevance.*
>
> However, despite such methodology in place, a future prompt could make the agents bring forward the information that was supposed to be deleted and can be tricked into revealing more information, which is a classic case of context recovery attack. So, the question raised here is: **How can we trust that our instructions have been followed? And where is the proof?**“

<https://spectrum.ieee.org/zero-trust-agentic-ai-architecture?itm_source=homepage&itm_medium=hero&itm_campaign=hero-2026-11-09&itm_content=hero7>

[DreamMMer team](https://dreammmer.com/?utm_source=schneier_com&utm_medium=external&utm_campaign=dreammmer) •
[November 9, 2026 3:54 PM](https://www.schneier.com/blog/archives/2026/11/ai-security.html/#comment-459543)

The split into security of AI, security with AI and security from AI is a useful frame, especially for teams building creative tools. For a generative image and video product, ‘of’ means protecting models, prompts and user uploads, ‘with’ means using agents to catch misuse, and ‘from’ means limiting abuse like non-consensual imagery. I’m from the DreamMMer team (an agent-driven image and video workspace), and we find it helps to keep those three questions separate when deciding what an agent may do on its own. Looking ...