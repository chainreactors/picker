---
title: Embedding Forbidden Text in Spyware to Discourage AI Analysis
url: https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html
source: Schneier on Security
date: 2026-06-24
fetch_date: 2026-06-25T06:10:21.648022
---

# Embedding Forbidden Text in Spyware to Discourage AI Analysis

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

## Embedding Forbidden Text in Spyware to Discourage AI Analysis

At least one malware developer is [adding text](https://x.com/jsrailton/status/2064661778978533571) about nuclear and biological weapons to their spyware, in an effort to stop automatic AI analysis.

[Details](https://socket.dev/blog/mini-shai-hulud-miasma-and-hades-worms-target-bioinformatics-and-mcp-developers-via-malicious):

> The \_index.js payload begins with a large JavaScript block comment containing fake system instructions and policy-triggering content. Because it is inside a comment, it does not affect JavaScript execution. The runtime skips it. The real malware begins after the comment with a try{eval(…)} wrapper around a large character-code array and a ROT-style substitution function.
>
> This header appears designed for AI-mediated analysis, not for Node, Bun, or Python. It attempts to derail scanners or analyst copilots that feed the beginning of a file to a language model without clearly isolating the content as untrusted data. In weak pipelines, this can cause refusal behavior, prompt confusion, context pollution, or premature classification before the scanner reaches the actual malware.
>
> This is not a magical bypass against static detection. YARA rules, entropy checks, AST parsing, string extraction, deobfuscation, and behavioral rules still work. But it is a practical anti-analysis trick against naive LLM-first triage systems.

Tags: [AI](https://www.schneier.com/tag/ai/), [LLM](https://www.schneier.com/tag/llm/), [malware](https://www.schneier.com/tag/malware/), [reports](https://www.schneier.com/tag/reports/), [spyware](https://www.schneier.com/tag/spyware/)

[Posted on June 24, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html#comments)

### Comments

Chris Becke •
[June 24, 2026 7:27 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html/#comment-455433)

deja vu

Eriadilos •
[June 24, 2026 8:31 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html/#comment-455434)

Is it a bug in the matrix ?

Clive Robinson •
[June 24, 2026 9:06 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html/#comment-455435)

@ ALL,

I’ve been thinking about this “poisoning the well” defence tactic of and on for a few days now.

And trust me it’s a lot more fun than just adding simple guardrail triggers.

The problem is the AI treats the whole file as “input” whilst as an executable comments are “rejected” early on and are not input.

Thus there are four possible states for text in a file,

1, Seen by both AI and interpreter
2, Seen by AI but not interpreter
3, Unseen by AI but seen by interpreter
4, Unseen by both AI and interpreter

The interpreter is easily “gated out” because of the way comments work.

Due to the deficient design of Current AI there is no “gating mechanism”.

Hence we use guard rails on the input path to the AI to provide a gating mechanism.

As has been shown there are “prompt injection” attacks on all sources of input to LLMs and all outputs from LLMs that get past guard rails.

It’s further been shown that some types of obfuscation and even simple crypto that will get text past any guard rail.

Thus the guard rails are not really effective gates nor can they ever be.

Understanding this means you can use other techniques other than “text in comments” you could but text in a loop of a programe that never gets seen by the interpreter but will be seen by the AI.

There are very many subtle ways you could hide text from the interpreter.

But do you even need to hide the text from the interpreter. The answer is no, because the interpreter treats text in all sorts of different ways.

A simple example is variable names. The AI sees them as input text, the interpreter sees them as just labels that get stripped off.

If you think on it further you realise that there are a whole further set of tricks you can do.

Such as making your code pass AI investigation, but not actually be usable by AI Agents… And I don’t know about you folk but I can see a while load of people in the software industry being interested in such a trick.

KC •
[June 24, 2026 11:48 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html/#comment-455437)

So Socket’s AI Scanner could detect the malicious langchain-core-mcp@1.4.2 wheel containing a covert hook that was able to execute a separate payload already on the victim’s system?

Are they saying it didn’t allow the policy-triggering content in the JavaScript comment to prematurely stop analysis?

Lots of moving parts here.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F06%2Fembedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

[ ]  Notify me of follow-up comments by email.

[ ]  Notify me of new posts by email.

Δ

[← Anthropic’s Fable 5 Model Jailbroken Within Days](https://www.schneier.com/blog/archives/2026/06/anthropics-fable-5-model-jailbroken-within-days.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com...