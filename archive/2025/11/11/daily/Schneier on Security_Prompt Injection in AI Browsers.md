---
title: Prompt Injection in AI Browsers
url: https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html
source: Schneier on Security
date: 2025-11-11
fetch_date: 2025-11-12T03:13:11.949264
---

# Prompt Injection in AI Browsers

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

## Prompt Injection in AI Browsers

[This](https://www.bleepingcomputer.com/news/security/commetjacking-attack-tricks-comet-browser-into-stealing-emails/) is why AIs are not ready to be personal assistants:

> A new attack called ‘CometJacking’ exploits URL parameters to pass to Perplexity’s Comet AI browser hidden instructions that allow access to sensitive data from connected services, like email and calendar.
>
> In a realistic scenario, no credentials or user interaction are required and a threat actor can leverage the attack by simply exposing a maliciously crafted URL to targeted users.
>
> […]
>
> CometJacking is a prompt-injection attack where the query string processed by the Comet AI browser contains malicious instructions added using the ‘collection’ parameter of the URL.
>
> LayerX researchers say that the prompt tells the agent to consult its memory and connected services instead of searching the web. As the AI tool is connected to various services, an attacker leveraging the CometJacking method could exfiltrate available data.
>
> In their tests, the connected services and accessible data include Google Calendar invites and Gmail messages and the malicious prompt included instructions to encode the sensitive data in base64 and then exfiltrate them to an external endpoint.
>
> According to the researchers, Comet followed the instructions and delivered the information to an external system controlled by the attacker, evading Perplexity’s checks.

I wrote [previously](https://www.schneier.com/blog/archives/2025/09/indirect-prompt-injection-attacks-against-llm-assistants.html):

> Prompt injection isn’t just a minor security problem we need to deal with. It’s a fundamental property of current LLM technology. The systems have [no ability to separate trusted commands from untrusted data](https://www.schneier.com/blog/archives/2024/05/llms-data-control-path-insecurity.html), and there are an infinite number of prompt injection attacks with [no way to block them](https://llm-attacks.org/) as a class. We need some new fundamental science of LLMs before we can solve this.

Tags: [AI](https://www.schneier.com/tag/ai/), [browsers](https://www.schneier.com/tag/browsers/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on November 11, 2025 at 7:08 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html) •
[9 Comments](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html#comments)

### Comments

Spellucci •
[November 11, 2025 7:43 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html/#comment-449799)

Thanks. The only generative AI I pay for is Perplexity. I had installed the Comet browser to see what the fuss was about. I could not find a use for it. After reading how the architecture of AI browsers is fundamentally insecure, and not securable, I uninstalled it last week.

You wrote, “We need some new fundamental science of LLMs before we can solve this.” That’s the understatement of the decade.

Snarki, child of Loki •
[November 11, 2025 11:59 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html/#comment-449802)

A few weeks back, I adjusted http server settings to reject connections from LLM training web-scrapers.

Now, I suspect that instead of just rejecting connections, I should have figured a way to reply with “malicious LLM injection” content.

The sooner LLMs are killed off, the better for everyone that isn’t a richy-rich tech edgelord.

Clive Robinson •
[November 11, 2025 12:05 PM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html/#comment-449803)

@ Bruce, ALL,

This says oh so much,

> *“In our proof-of-concept test, we demonstrated that exporting sensitive fields in an encoded form (base64) effectively circumvented the platform’s exfiltration checks”*

So plain text only matching on sensitive data.

If base64 gets sorted what about base16 etc.

And that’s all before talking about even primitive statistics flattening by the simplest of “Straddling checkerboard”[1] systems.

The important point to note though, is that the AI agent does not see things the way humans do.

I frequently say,

“Paper, Paper, Never Data”

Because of how the redundancy of extended character sets can have covert channels in them.

It’s a problem that goes back a long way certainly before Current AI LLM and ML Systems and tools and systems built on them.

Put simply,

“They can not be made secure in any way”

Thus the only option is “isolation” by full “segregation” as a mitigation strategy.

Which let’s be honest makes the tool effectively “useless”.

Now ask yourself an important question,

“Does Microsoft’s AI tools built into Win11 have similar defects?”

I think that there would be plenty who would put a Dollar down to say yes…

Microsoft are desperate to make their investments in AI look like they are “bringing in profit” when they clearly are not even “bringing in money”.

People are begining to see that AI is a bent and battered can, that still needs a good kicking to go effectively nowhere.

Which begs another question about “surveillance” in effect these tools are betraying internal confidential / Private Personal Information to Microsoft… So,

“How will Microsoft monetize your stolen information?”

And lets be honest the options are not very good for them, and very bad for us.

[1] The Straddling checkerboard is a very simple and curious thing in that not only can it make language statistics look flat and shorten the length of the plain text so act as crude compression. It can do the opposite of making something with flat statistics like the ciphertext of an OTP look, like the ciphertext of a simple paper and pencil cipher that leaks plaintext statistics. Thus giving anyone doing cryptanalysis a long and entirely pointless investigation.

David •
[November 11, 2025 12:34 PM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html/#comment-449804)

> “How will Microsoft monetize your stolen information?”

The Microsoft Edge web browser has a very clear voice synthesis feature, which will read a web page aloud. It works well with a fast net connection, but not with a slow connection, which suggests that the page is being sent back to MS for conversion. This might not matter on public web pages, which MS can be assumed to have slurped up already, but anyone using Edge voice synthesis on confidential internal company documents should ask the same question.

Winter •
[November 11, 2025 12:35 PM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-in-ai-browsers.html/#comment-449805)

What surprises me is that it seems to be so difficult to filter non-human visible, is, invisible, components from pages.

On the other hand, filtering costs t...