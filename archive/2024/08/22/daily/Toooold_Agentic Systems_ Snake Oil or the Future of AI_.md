---
title: Agentic Systems: Snake Oil or the Future of AI?
url: https://toooold.com/2024/08/21/agentic_system.html
source: Toooold
date: 2024-08-22
fetch_date: 2025-10-06T18:03:35.190375
---

# Agentic Systems: Snake Oil or the Future of AI?

[Toooold](/)
[ ]

[Make a CatGPT out of ChatGPT](/2023-02-02-cat_laser_chatgpt.html)[About](/about.html)

# Agentic Systems: Snake Oil or the Future of AI?

Aug 21, 2024

The short answer: it’s more nuanced—agentic systems have potential, but only if implemented correctly.

Recently, a friend of mine, Jason, developed a LLM-driven agentic system to analyze cloud logs for security intrusions. Each run cost about $5, and the results were disappointing. The AI failed to detect a known intrusion, leaving Jason disillusioned and questioning the hype around AI. His frustration boiled down to one question: Why did his system underperform despite his best efforts, while other agentic systems showcased on Youtube and Arxiv seemed to work flawlessly?

![Red Panda agent](/images/red-panda-agent.jpg)

## Why Do We Need Agentic Systems?

The primary value of building agentic systems lies in their ability to make autonomous decisions. These systems can manage dynamic situations without needing an exhaustive set of predefined rules from humans. This flexibility is the core value proposition, enabling high-level tasks to be broken down into actionable steps, chaining tasks together, or even coordinating multiple agents towards a shared objective. However, when a system has only static logic like most RAG system, or it is overly constrained by human-imposed rules, it risks losing this adaptability, which is the essence of what makes agentic systems valuable.

The system has its real value, so, how do we get these systems to work effectively?

## Understanding What “Agent” Really Means

At its core, an intelligent agent is straightforward: it can perceive its environment or “world”, act within it, and repeat. Forget the complex frameworks like AutoGen or CrewAI—an agent doesn’t need to be sophisticated to be effective.

Consider a robotic soccer player. The world it operates in consists of the soccer field, the ball, the goals, and the field lines. It perceives this world through sensors that mimic sight and hearing and acts by moving, kicking the ball, or communicating with teammates.

Similarly, a Retrieval-Augmented Generation (RAG) system functions as an intelligent agent within the domain of databases and user queries. It perceives user inputs and database results and acts by generating a relevant response.

The takeaway is that an agent doesn’t need to be driven by an LLM, nor does it have to be inherently intelligent. The key is in defining the agent’s world and ensuring it has the channels to perceive and act within that world to achieve its goal.

![Red Panda thinking](/images/red-panda-thinking.jpeg)

## Getting “Agentic” Right

The success of an agentic system relies on understanding its limitations and defining the appropriate granularity of problem-solving tasks.

LLM-driven agentic systems are currently constrained by several factors, and as of August 2024, these limitations are significant:

* **Reflection**: The ability for an agent to self-assess its performance or have other agents evaluate it is rudimentary at best. This area requires significant development.
* **Memory**: Whether it’s retrieving context from six months ago or just a few moments ago, current systems are far from perfect. RAG systems show promise here, but there’s still a long way to go.
* **Tool Use**: Converting LLM decisions into actionable steps via API calls is improving, probably the best among all four core functionalities, but still needs more refinement.
* **Reasoning**: This is perhaps the most significant bottleneck. Current LLMs can only perform shallow reasoning by using memory to mimic thinking, which leads to instability in complex agentic tasks. The field of research, including techniques like chain-of-thought, is pushing boundaries, but we are still far from achieving deep reasoning with LLMs.

Jason’s system didn’t fail because the agentic system concept is flawed; it failed because Jason ignored the fact that the current limitations of LLMs weren’t fully nor easily accounted for his problem scope. He needed a better problem definition. However, even with these limitations, LLMs can be powerful tools if used correctly. Just as early computers were limited but still revolutionary in their applications like Turing’s computer in WWII, today’s LLMs can perform impressive tasks if we align their capabilities with the right granularity of problems.

## Case in Point: Apple’s Recent Demo

A recent demonstration by Apple showcased an effective agentic system. Starting with a simple message—“going to a party at 6 PM”—the system planned a route considering traffic conditions, sent a meeting rescheduling notice, and even added a quick stop at a flower shop. This system worked because it tackled a problem with the right level of complexity for the technology available:

* **Tool Use**: The system used APIs to interact with various apps, each specializing in a single task.
* **Reasoning**: The reasoning required was straightforward and well within the capabilities of today’s LLMs.
* **Cost Efficiency**: The tasks didn’t require a massive, expensive LLM , allowing the system to run locally.

## The Future of Agentic Systems

Despite current limitations, I remain optimistic about agentic systems. Intelligent agents are a foundational concept in modern AI, as outlined in “Artificial Intelligence: A Modern Approach”. However, today’s LLMs are not yet the silver bullet for complex tasks. Just as with early AI technologies, we need to understand their limitations, find suitable problems for them to solve, and define these problems with the appropriate level of granularity. This approach will remain essential, no matter how advanced these systems become in the future, hopefully, AGI, am I right?

## Reference

* “Artificial Intelligence: A Modern Approach, 4th US ed.” <https://aima.cs.berkeley.edu/>
* “LLM Powered Autonomous Agents” <https://lilianweng.github.io/posts/2023-06-23-agent/>

## Toooold

* Toooold
* toooold.tocode@gmail.com

* [phunterlau](https://github.com/phunterlau)

to code