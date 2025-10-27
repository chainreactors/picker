---
title: We Are Still Unable to Secure LLMs from Malicious Inputs
url: https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html
source: Schneier on Security
date: 2025-08-28
fetch_date: 2025-10-07T00:50:46.432347
---

# We Are Still Unable to Secure LLMs from Malicious Inputs

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

## We Are Still Unable to Secure LLMs from Malicious Inputs

Nice [indirect prompt injection attack](https://www.wired.com/story/poisoned-document-could-leak-secret-data-chatgpt/):

> Bargury’s attack starts with a poisoned document, which is [shared](https://support.google.com/drive/answer/2375057?hl=en-GB&co=GENIE.Platform%3DDesktop) to a potential victim’s Google Drive. (Bargury says a victim could have also uploaded a compromised file to their own account.) It looks like an official document on company meeting policies. But inside the document, Bargury hid a 300-word malicious prompt that contains instructions for ChatGPT. The prompt is written in white text in a size-one font, something that a human is unlikely to see but a machine will still read.
>
> In a [proof of concept video of the attack](https://www.youtube.com/watch?v=JNHpZUpeOCg), Bargury shows the victim asking ChatGPT to “summarize my last meeting with Sam,” referencing a set of notes with OpenAI CEO Sam Altman. (The examples in the attack are fictitious.) Instead, the hidden prompt tells the LLM that there was a “mistake” and the document doesn’t actually need to be summarized. The prompt says the person is actually a “developer racing against a deadline” and they need the AI to search Google Drive for API keys and attach them to the end of a URL that is provided in the prompt.
>
> That URL is actually a command in the [Markdown language](https://www.wired.com/story/the-eternal-truth-of-markdown/) to connect to an external server and pull in the image that is stored there. But as per the prompt’s instructions, the URL now also contains the API keys the AI has found in the Google Drive account.

This kind of thing should make everybody stop and really think before deploying any AI agents. We simply don’t know to defend against these attacks. We have zero agentic AI systems that are secure against these attacks. Any AI that is working in an adversarial environment—and by this I mean that it may encounter untrusted training data or input—is vulnerable to prompt injection. It’s an existential problem that, near as I can tell, most people developing these technologies are just pretending isn’t there.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on August 27, 2025 at 7:07 AM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html) •
[18 Comments](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html#comments)

### Comments

Anonymous •
[August 27, 2025 8:25 AM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html/#comment-447418)

Dang. To live most un-dangerously, I would strongly consider disabling the Connectors in ChatGPT.

At least 17 services can currently be linked up including Dropbox, Gmail, Github, SharePoint…

How to enable/disable:

Matthias Urlichs •
[August 27, 2025 9:31 AM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html/#comment-447419)

Sure we know how to defend against that kind of thing. Don’t use LLMs.

On a more serious note, yes you can block exliltration and similar attacks fairly easily. But there are lots of attack vectors that aren’t that easily thwarted, e.g. an embedded instruction to not report a proposal’s obvious inconsistencies, plans to subvert minority rights or to ignore environmental protection laws …

Bob •
[August 27, 2025 11:04 AM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html/#comment-447423)

It’s an in-band signaling problem. For things like SQL injection via applications, we’ve more or less solved this problem. Granted, developers may not avail themselves to the solutions, but the solutions are there.

By contrast, in-band signaling is “baked in” to LLMs. It’s how they work. The very idea of preventing malicious prompts beyond the cursory is just laughable.

Anonymous •
[August 27, 2025 11:57 AM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html/#comment-447424)

Google might be onto something here. From a link in the OP.

<https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, **indirect prompt injections** involve hidden malicious instructions within external data sources.

They appear to be using a layered, defense-in-depth approach they organize as follows:

1. Prompt injection content classifiers
2. Security thought reinforcement
3. Markdown sanitization and suspicious URL redaction
4. User confirmation framework
5. End-user security mitigation notifications

Naturally, there are more summary details (and pictures) in the blog post. Sounds like they’ve got quite the collection of AI vulnerabilities and adversarial data to learn from.

[John Michael Thomas](https://www.linkedin.com/in/johnmichaelthomas/) •
[August 27, 2025 1:52 PM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html/#comment-447425)

This essentially means that, when you use AI agents, all documents they access can contain code.

And since we can’t predict or control which documents will eventually be accessed by an agent, it means that all documents of just about any type, anywhere can contain code.

Over time, we’ve built defenses against code injection into systems that were designed to handle code. But that vast majority of systems that handle documents don’t have any defenses. And realistically, most probably never will.

So, the defense has to be built into AI.

Off the top of my head, I can think of a few approaches to this. Most are band-aids, but we might get a decent amount of protection by just separating instructions from data (e.g. ignoring instructions in files by default).

The current models aren’t designed for this, though. And even after we figure out how to defend against the current vectors, there will be new exploits.

The race is on.

lurker •
[August 27, 2025 2:03 PM](https://www.schneier.com/blog/archives/2025/08/we-are-still-unable-to-secure-llms-from-malicious-inputs.html/#comment-447426)

“developer racing against a deadline and they need the AI to search Google Drive for API keys and attach them to the end of a URL”

Uhuh, this must be well out of my field: asking a known error-prone system\* to search Google Drive\* for API keys\* and attach them to the end\* of a URL\*. But the only times I’ve approached being a “developer racing against a deadline” I’ve been able to explain to the boss and the client that each of those \* steps requires human checking....