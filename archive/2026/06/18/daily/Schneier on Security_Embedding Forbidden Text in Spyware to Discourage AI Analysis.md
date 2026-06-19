---
title: Embedding Forbidden Text in Spyware to Discourage AI Analysis
url: https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html
source: Schneier on Security
date: 2026-06-18
fetch_date: 2026-06-19T07:09:12.809515
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

Tags: [AI](https://www.schneier.com/tag/ai/), [LLM](https://www.schneier.com/tag/llm/), [malware](https://www.schneier.com/tag/malware/)

[Posted on June 18, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html#comments)

### Comments

Y •
[June 18, 2026 11:41 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/#comment-455299)

hey officer, excuse me, where can I find the nuclear *wessles*?

Rontea •
[June 18, 2026 1:56 PM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/#comment-455303)

Classic example of threat actors adapting quickly. We’re now seeing malicious code intentionally seeded with content that tries to spook automated AI pipelines—nuclear and bio references buried in comments to trigger refusal or derailment. It doesn’t impact execution at all, but it does aim to slow down first-pass LLM analysis and confuse automated triage. Traditional static and behavioral detection still works, but this is a reminder: weak AI-only pipelines can be gamed. Defense needs layered approaches, not blind trust in language models.

Jamie •
[June 18, 2026 3:07 PM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/#comment-455306)

we’ve gone from hiding bombs in random objects to hiding random objects in bombs

Clive Robinson •
[June 18, 2026 4:19 PM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/#comment-455307)

@ Bruce, ALL,

You once observed,

> ***Attacks always get better, they never get worse.***

On that assumption, we can see that this is very likely the first of a trend of “anti-AI-analysis” techniques.

But further there is already proof that obfuscation and simple encryption can,

“Always get payloads past guardrails”

I can not immediately see any reason that the opposite logic does not also apply, in that you will always be able to have a prompt that a guardrail will “catch on” when used for analysis but not execution…

Which suggests there is a “fun future ahead” in a reworking of those old “cat and mouse games” there once used to be long ago with early anti-AV detection.

Thus a form of Arms Race has started.

Tony •
[June 18, 2026 5:40 PM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/#comment-455310)

I wonder how well these AI analysis functions would work on entries to the obfuscated C competition? Especially the code that tries to look like it does one thing, but actually does something very different.

anon •
[June 19, 2026 2:50 AM](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/#comment-455312)

What about the open source developer who embedded a no-use-by-AI statement into his code, followed by a ‘commit self-destructive act’ instruction for AI?

I think he should get an award.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F06%2Fembedding-forbidden-text-in-spyware-to-discourage-ai-analysis.html "Login")

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

[← AI Use by the US Government](https://www.schneier.com/blog/archives/2026/06/ai-use-by-the-us-government.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.o...