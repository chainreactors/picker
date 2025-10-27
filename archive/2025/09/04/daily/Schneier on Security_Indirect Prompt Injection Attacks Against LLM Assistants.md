---
title: Indirect Prompt Injection Attacks Against LLM Assistants
url: https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html
source: Schneier on Security
date: 2025-09-04
fetch_date: 2025-10-02T19:38:50.189506
---

# Indirect Prompt Injection Attacks Against LLM Assistants

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

## Indirect Prompt Injection Attacks Against LLM Assistants

Really good [research](https://sites.google.com/view/invitation-is-all-you-need/home) on practical attacks against LLM agents.

> “[Invitation Is All You Need! Promptware Attacks Against LLM-Powered Assistants in Production Are Practical and Dangerous](https://arxiv.org/abs/2508.12175)”
>
> **Abstract:** The growing integration of LLMs into applications has introduced new security risks, notably known as Promptware­—maliciously engineered prompts designed to manipulate LLMs to compromise the CIA triad of these applications. While prior research warned about a potential shift in the threat landscape for LLM-powered applications, the risk posed by Promptware is frequently perceived as low. In this paper, we investigate the risk Promptware poses to users of Gemini-powered assistants (web application, mobile application, and Google Assistant). We propose a novel Threat Analysis and Risk Assessment (TARA) framework to assess Promptware risks for end users. Our analysis focuses on a new variant of Promptware called Targeted Promptware Attacks, which leverage indirect prompt injection via common user interactions such as emails, calendar invitations, and shared documents. We demonstrate 14 attack scenarios applied against Gemini-powered assistants across five identified threat classes: Short-term Context Poisoning, Permanent Memory Poisoning, Tool Misuse, Automatic Agent Invocation, and Automatic App Invocation. These attacks highlight both digital and physical consequences, including spamming, phishing, disinformation campaigns, data exfiltration, unapproved user video streaming, and control of home automation devices. We reveal Promptware’s potential for on-device lateral movement, escaping the boundaries of the LLM-powered application, to trigger malicious actions using a device’s applications. Our TARA reveals that 73% of the analyzed threats pose High-Critical risk to end users. We discuss mitigations and reassess the risk (in response to deployed mitigations) and show that the risk could be reduced significantly to Very Low-Medium. We disclosed our findings to Google, which deployed dedicated mitigations.

Defcon [talk](https://www.youtube.com/watch?v=pleLhJRW9Fw&feature=youtu.be).  [News](https://arstechnica.com/google/2025/08/researchers-use-calendar-events-to-hack-gemini-control-smart-home-gadgets/) [articles](https://www.wired.com/story/google-gemini-calendar-invite-hijack-smart-home/) [on](https://www.pcmag.com/news/rogue-calendar-invite-could-turn-google-gemini-against-you-black-hat-2025) [the](https://www.zdnet.com/article/beware-of-promptware-how-researchers-broke-into-google-home-via-gemini/) [research](https://www.cnet.com/home/smart-home/researchers-seize-control-of-smart-homes-with-malicious-gemini-ai-prompts/).

Prompt injection isn’t just a minor security problem we need to deal with. It’s a fundamental property of current LLM technology. The systems have [no ability to separate trusted commands from untrusted data](https://www.schneier.com/blog/archives/2024/05/llms-data-control-path-insecurity.html), and there are an infinite number of prompt injection attacks with [no way to block them](https://llm-attacks.org/) as a class. We need some new fundamental science of LLMs before we can solve this.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/), [threat models](https://www.schneier.com/tag/threat-models/)

[Posted on September 3, 2025 at 7:00 AM](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html#comments)

### Comments

Anonymous •
[September 3, 2025 7:50 AM](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html/#comment-447521)

Here is the website of the study: <https://sites.google.com/view/invitation-is-all-you-need/home>

jbmartin6 •
[September 3, 2025 8:56 AM](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html/#comment-447522)

I would just call it remote code execution.

KC •
[September 3, 2025 9:04 AM](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html/#comment-447523)

In the Nassi, Cohen, Yair paper – in the discussion – they alert of at least two more Promptware variants. Of what I suppose are an infinite number. I’d/ll need to look more closely at their research. But are they saying these are still unmitigated attack vectors?

(1) like one where Apple Intelligence summarizes an incoming message

(2) digital mines placed in YouTube and Google Maps

Anonymous •
[September 3, 2025 10:17 AM](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html/#comment-447525)

To KC, Plenty of attack vectors are still open and waiting to be discovered 🙂

Clive Robinson •
[September 3, 2025 10:37 AM](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html/#comment-447526)

@ Bruce, ALL,

With regards

> “Prompt injection isn’t just a minor security problem we need to deal with. It’s a fundamental property of current LLM technology.”

It’s not just Current AI LLM systems.

As I’ve indicated in the past it applies to all systems –not just electronic– that can and do “interpret input” and have a degree of complexity.

Because as noted,

> “The systems have no ability to separate trusted commands from untrusted data, and there are an infinite number of prompt injection attacks with no way to block them as a class.”

Is not quite true due to both,

1, Feed back paths,

So consider a “state machine” of minimal function and hard coded interpretation. It lacks some of the necessary function.

In the simplest of cases –say a lift and it’s buttons– all states and their interactions can be mapped and constrained. By what is in effect simple sequence logic.

That said except in highly constrained environments, such systems tend to be of limited functionality.

But care has to be taken… Either the NAND or NOR gate are considered “universal gates” from which all other logic gates and logical functions within limits can be built.

Therefore at some point the level of complexity becomes capable of being a Universal Turing Engine.

The limits were known before electromechanical or electronic computers were built. Due to the work of Kurt Gödel, Alonzo Church, Alan Turing, etc in the late 1920’s and early 1930’s. And importantly the work of others that provided the shoulders on which they stood.

Which is why I am cautious about,

...