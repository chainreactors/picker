---
title: LLMs Generate Predictable Passwords
url: https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html
source: Schneier on Security
date: 2026-02-26
fetch_date: 2026-02-27T04:08:43.510578
---

# LLMs Generate Predictable Passwords

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

## LLMs Generate Predictable Passwords

LLMs are [bad](https://www.irregular.com/publications/vibe-password-generation) at generating passwords:

> There are strong noticeable patterns among these 50 passwords that can be seen easily:
>
> * All of the passwords start with a letter, usually uppercase G, almost always followed by the digit 7.* Character choices are highly uneven ­ for example, L , 9, m, 2, $ and # appeared in all 50 passwords, but 5 and @ only appeared in one password each, and most of the letters in the alphabet never appeared at all.* There are no repeating characters within any password. Probabilistically, this would be very unlikely if the passwords were truly random ­ but Claude preferred to avoid repeating characters, possibly because it “looks like it’s less random”.* Claude avoided the symbol \*. This could be because Claude’s output format is Markdown, where \* has a special meaning.* Even entire passwords repeat: In the above 50 attempts, there are actually only 30 unique passwords. The most common password was G7$kL9#mQ2&xP4!w, which repeated 18 times, giving this specific password a 36% probability in our test set; far higher than the expected probability 2-100 if this were truly a 100-bit password.

This result is not surprising. Password generation seems precisely the thing that LLMs shouldn’t be good at. But if AI agents are doing things autonomously, they will be creating accounts. So this is a problem.

Actually, the whole process of authenticating an autonomous agent has all sorts of deep problems.

News [article](https://gizmodo.com/ai-generated-passwords-are-apparently-quite-easy-to-crack-2000723660).

Slashdot [story](https://it.slashdot.org/story/26/02/19/1842201/llm-generated-passwords-look-strong-but-crack-in-hours-researchers-find)

Tags: [AI](https://www.schneier.com/tag/ai/), [LLM](https://www.schneier.com/tag/llm/), [passwords](https://www.schneier.com/tag/passwords/), [random numbers](https://www.schneier.com/tag/random-numbers/), [reports](https://www.schneier.com/tag/reports/)

[Posted on February 26, 2026 at 7:07 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html) •
[17 Comments](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html#comments)

### Comments

[Matthias Urlichs](http://matthias.urlichs.de/) •
[February 26, 2026 8:26 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452432)

Heh. That’s not just an LLM problem. Humans do that too: we all know that the correct way to create a password is to fire up “pwgen”, or ask your password manager or whatever, no exceptions — but when we’re in the flow and need a quick password-ish string, we still resort to hitting a not-quite-random bunch of keys. Or just type “$ekriT1248”.

The real issue is that the distance between institutional memory (the LLM knows how a password *should* be generated if you ask it!) and short-term objectives is too large. Fixing this requires access to a tool — followed by training, to break the pattern of not using it. In fact, the frontier labs should probably just fix training input: replace all literal password-ish strings with instructions to do an MCP call.

Vesselin Bontchev •
[February 26, 2026 8:31 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452433)

Programs designed to generate statistically likely words happen to generate statistically likely passwords. News at eleven.

a clown •
[February 26, 2026 9:16 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452435)

Laziness and ignorance have their consequences.

In the world of cybersecurity, there’s a price to be paid for taking shortcuts (laziness is sometimes also called “time saving measures” or “efficiency” or “productivity” or blah blah blah) and the key thing here is When and Where to resort to an App to do something for you that will be better, more secure, than if you’d done it yourself, the old, “slow” manual way.

Patrick Gill •
[February 26, 2026 9:25 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452436)

LLMs used to be bad at arithmetic too. How long before a good LLM will know to defer to /dev/urandom when it needs entropy to make a password? This seems like a fixable problem.

Clive Robinson •
[February 26, 2026 9:43 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452437)

@ Bruce, ALL,

**Predictable is not Random and Random is essential to AI function**

We used to call the Current AI systems “Stochastic Parrots” implying a uniform random selection probability for phrases.

If an LLM system can not “do random” for passwords then it calls into question the “random selection of phrases”. Which calls into question the rest of the LLM usage.

Which calls into question the use of LLMs all and their other uses for which LLMs have been suggested…

jm •
[February 26, 2026 10:00 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452439)

> But if AI agents are doing things autonomously, they will be creating accounts. So this is a problem.

If that were the extent of the problem, the solution would be simple: delegate to a tool that uses a properly seeded CSPRNG to generate passwords when needed (as Patrick suggests).

The real problem is that any credential that is exposed to the model’s context becomes vulnerable to subsequent extraction via prompt injection. And even if you isolate the credential in tool configuration, a prompt-injected agent is still a Confused Deputy.

Rontea •
[February 26, 2026 10:38 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452440)

Large language models, by design, optimize for pattern recognition and human-like output—not for entropy. When tasked with generating passwords, they produce predictable sequences and systematically avoid certain characters, creating a security liability for autonomous agents. This isn’t just about weak passwords; it’s a symptom of a deeper problem: authenticating non-human actors in a system designed for human credentials. Until we rethink how these agents establish trust, we’re layering brittle automation onto brittle security assumptions.

Clive Robinson •
[February 26, 2026 11:37 AM](https://www.schneier.com/blog/archives/2026/02/llms-generate-predictable-passwords.html/#comment-452441)

@ ALL,

A part of the quote from the article says,

> *“There are no repeating characters within any password. Probabilistically, this would be very unlikely if the passwords were truly random”*

Is actually not technically not true.

There are two degrees of freedom in a random sequence, value and order position.

We no...