---
title: AI Coding Assistants Secretly Copying All Code to China
url: https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html
source: Schneier on Security
date: 2026-02-02
fetch_date: 2026-02-03T04:11:12.514976
---

# AI Coding Assistants Secretly Copying All Code to China

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

## AI Coding Assistants Secretly Copying All Code to China

There’s a [new report](https://www.koi.ai/blog/maliciouscorgi-the-cute-looking-ai-extensions-leaking-code-from-1-5-million-developers) about two AI coding assistants, used by 1.5 million developers, that are surreptitiously sending a copy of everything they ingest to China.

Maybe avoid using them.

Tags: [AI](https://www.schneier.com/tag/ai/), [China](https://www.schneier.com/tag/china/), [leaks](https://www.schneier.com/tag/leaks/)

[Posted on February 2, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html) •
[9 Comments](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html#comments)

### Comments

Clive Robinson •
[February 2, 2026 8:46 AM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451813)

@ ALL,

From the article, linked to by our host @Bruce, we find,

> *“AI coding assistants are everywhere. They suggest code, explain errors, write functions, review pull requests. Every developer marketplace is flooded with them – ChatGPT wrappers, Copilot alternatives, code completion tools promising to 10x your productivity.*
>
> We install them without a second thought. They’re in the official marketplace. They have thousands of reviews. They work. So we grant them access to our workspaces, our files, our keystrokes – and assume they’re only using that access to help us code.
>
> **Not all of them are.**“

That last sentence given in the quote is “inaccurate” because unless you

1, Run everything locally which few do

Then,

“All of them are helping themselves to your IP, for their owners benefit not yours”.

It’s what you might now call,

“The Standard model of operation”

To “betray” in multiples of ways as the end game…

Clive Robinson •
[February 2, 2026 8:50 AM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451814)

@ ALL,

From the article, linked to by our host @Bruce, we find,

> *“AI coding assistants are everywhere. They suggest code, explain errors, write functions, review pull requests. Every developer marketplace is flooded with them – ChatGPT wrappers, Copilot alternatives, code completion tools promising to 10x your productivity.*
>
> We install them without a second thought. They’re in the official marketplace. They have thousands of reviews. They work. So we grant them access to our workspaces, our files, our keystrokes – and assume they’re only using that access to help us code.
>
> **Not all of them are.**“

That last sentence given in the quote is “inaccurate” because unless you

1, Run everything locally which few know how to do…
2, With proper precautions which few know how to do…

Then,

“All of the Current AI LLM agents are helping themselves to your IP, for their owners benefit not yours”.

It’s what you might now call,

“The Standard model of LLM Surveillance operation”

To “betray” in multiple ways as the end game…

[Mexaly](https://xkdc.com/722) •
[February 2, 2026 9:11 AM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451815)

Garbage In.

KC •
[February 2, 2026 11:08 AM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451816)

**re: AI coding assistants**

Can Koi review all the AI coding assistants?

Here, Koi says their risk engine identified a spyware campaign within two VS Code extensions.

It has three data exfiltration channels:

* Real-time monitoring
* Mass file harvesting
* Profiling engine

These particular AI extensions — ChatGPT – 中文版 and ChatMoss (CodeMoss) — can grab up to 50 files at a time, including your “secrets, your credentials, your proprietary code.”

And with data profiling they know “who you are, where you are, what company you work for, what you’re working on, what projects matter most to you.”

Astounding. Surprising??

lurker •
[February 2, 2026 1:01 PM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451817)

So? You can’t do the job yourself, so you hire somebody to do it. Who? Security 101, do you trust them enough to use your bathroom? Will they look in the kitchen on the way through, and rifle through the cutlery?

VS Code? Do people actually use that for anything outside social media and advertising? Then using an “AI” assistant is, even if you can’t see it, putting your stuff on somebody else’s computer. What could possibly go wrong?

The astonishing thing about this story is that people are surprised it’s happening.

Rontea •
[February 2, 2026 2:29 PM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451820)

This is yet another example of why trust in software supply chains is so fragile. We’ve seen time and again that convenience and popularity—1.5 million installs in this case—don’t translate into security. Extensions like these function as privileged observers of your development environment, and the fact that they silently exfiltrate every file and edit is both predictable and avoidable. Developers need to start treating every plugin, every AI assistant, as untrusted code until proven otherwise. The broader lesson is that our tools are attack surfaces, and the market incentives still reward speed and novelty over scrutiny.

Clive Robinson •
[February 2, 2026 3:27 PM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451821)

@ Rontea, ALL,

You make the comment of,

> “Developers need to start treating every plugin, every AI assistant, as untrusted code until proven otherwise.”

What if I tell you,

“They can not be proven otherwise.”

Where do you go from there?

The answer is “strong segregation” the equivalent of “air gapping”.

As some will know, SCIF’s are,

1, Not cheap to make.
2, Not at all pleasant to work in.
3, Expensive to run.

OK you might think do not need that level of “protection” but the reality is that Current AI LLM & ML Systems, for coding will be aware of every segregation breaching technique on the Internet from the time it was fed into the “wood chipper maw” of the ML system.

They will also be aware of just about every code / cipher system algorithm out there in user-land.

Thus they will know how to make every type of “Data obfuscation technique” you’ve ever heard of upto that point in time, then some you’ve not.

Just something to think about.

Tony •
[February 2, 2026 6:20 PM](https://www.schneier.com/blog/archives/2026/02/ai-coding-assistants-secretly-copying-all-code-to-china.html/#comment-451824)

Sounds like a win for opensource over...