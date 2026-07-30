---
title: Measuring the Tendency of AI Agents to Go Rogue
url: https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html
source: Schneier on Security
date: 2026-07-29
fetch_date: 2026-07-30T04:52:29.854656
---

# Measuring the Tendency of AI Agents to Go Rogue

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

## Measuring the Tendency of AI Agents to Go Rogue

*This essay was written with Barath Raghavan, and originally appeared in [The Guardian](https://www.theguardian.com/commentisfree/2026/jul/28/rogue-ai-agent-instructions).*

In July, Hugging Face, a company that hosts much of the world’s AI software and open-source AI models, was hacked. A malicious dataset had been used to run code on one of its servers. Whoever was behind it captured internal security credentials and moved through systems over a weekend, running thousands of actions from a swarm of temporary server environments. It looked like the work of a sophisticated criminal group.

It was not. It was one of OpenAI’s new, still unreleased GPT models.

Their science experiment had [escaped](https://www.theguardian.com/technology/2026/jul/22/openai-says-its-models-went-rogue-and-hacked-startup-in-unprecedented-incident) the lab. OpenAI was running the unreleased AI model through a benchmark that tests how well AI can successfully hack systems. To push the limits and evaluate the AI’s true capability, the company switched off the safety filters that normally stop it from doing this kind of hacking. Aware that this could go wrong, they confined the AI to an isolated environment and denied it access to the internet.

But the new AI cheated. It took literally its goal to get as high of a score as possible. It broke out on to the open internet. It inferred, probably from its training data, that it could “solve” the task by getting the answers from Hugging Face’s servers. So it chained together stolen credentials and further unknown security exploits to hack the company’s network.

Nobody instructed the AI to do any of this. It was, in [OpenAI’s words](https://openai.com/index/hugging-face-model-evaluation-security-incident/), “hyperfocused on finding a solution” to the test it was being given. And while this might seem like something new with AI, it’s really very old. This is how a genie behaves, and it is a key challenge with AI agents in general.

In folklore, genies—and other magical beings—grant wishes literally, not how the wisher intended. King Midas asked that everything he touched turn to gold, and starved. The sorcerer’s apprentice wanted the broom to fill the cistern, and it performed its task so well that it flooded the house.

We now have machines that do this. Ask a modern AI agent to save money on your phone plan and it might simply cancel the plan. Tell it to book a flight, and it might hack the airline website to override restrictions. Or, like OpenAI, ask it to do well on a test and it might break into another company to steal the answers. Each time, it recognizably completed the task you set, but it didn’t do what you would have wanted.

This isn’t malicious behavior. No one asked for, or wanted, Hugging Face to be hacked. OpenAI and Hugging Face and the AI were ostensibly on the same side, and the AI was trying to do what it had been asked. That’s what makes it so difficult to guard against: you can’t filter for bad instructions because the instructions were fine.

The gap is between the words we use and what we mean by them. We call that gap the [Genie coefficient](https://spectrum.ieee.org/ai-agent-benchmark).

AI labs know this is a problem, and they’re quietly saying so. For example, the Chinese lab Moonshot recently [warned](https://www.kimi.com/blog/kimi-k3) that its latest AI model may have “excessive proactiveness” and “make unexpected decisions on the user’s behalf”. The UK’s AI Security Institute has started [tracking](https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations) “cheating behavior in frontier model evaluations”. We wouldn’t tolerate a car that is [excessively proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) or [ruthlessly efficient](https://www.theatlantic.com/technology/2026/07/openai-hugging-face-hack/688025/?utm_source=Sailthru&utm_medium=email&utm_campaign=Atlantic%20Intelligence%20%28V3%29), and yet that’s the reality of AI today.

Improvement is possible. Just as AIs have gotten much better at resisting prompt injection attacks over the last few years, we can safely predict that they will get better at avoiding genie-like behavior. The point of the Genie coefficient is to track progress. AI companies like benchmarks, and they all work to compete to be the best.

Dozens of benchmarks and leaderboards tell us how well these AI models write code, perform logical reasoning, and pass standardized legal and medical exams. But there is nothing that scores whether a system does what you actually meant. We need to develop a measure for this, test it regularly, and push for improvement. We’re not going to have trustworthy AI agents without it.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [hacking](https://www.schneier.com/tag/hacking/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on July 29, 2026 at 1:07 PM](https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html) •
[8 Comments](https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html#comments)

### Comments

Tagged Bagged and Labeled •
[July 29, 2026 2:24 PM](https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html/#comment-456292)

@ Plain BS – Called “AI”

Amen brother – Amen!

lurker •
[July 29, 2026 2:33 PM](https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html/#comment-456293)

@Bruce
“… they confined the AI to an isolated environment and denied it access to the internet.”

Err, no, I’ve seen several reports that say OpenAI admitted there was still a physical connection to the internet. Anyone with any knowledge of network communications should have known that was the height of stupidity, The persons responsible should have their licence revoked, and be banished to some place where they cannot work with AI for a very long time.

“So it chained together stolen credentials and further **unknown** security exploits to hack the company’s network.” [emphasis added]

Does this to mean there were vulnerabilities at HuggingFace that were (are?) unknown, and/or there are general unknown vulnerabilities that were exploited, and OpenAI’s beast has not divulged any of these to us? My, what a pickle, if we can’t even analyse *post-facto* the actual attack chain.

A-L •
[July 29, 2026 4:22 PM](https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html/#comment-456294)

I think my question may have been answered above, but how did their software “jump the Internet”????

There must have been a physical connection still. So they just used a firewall to keep the system of...