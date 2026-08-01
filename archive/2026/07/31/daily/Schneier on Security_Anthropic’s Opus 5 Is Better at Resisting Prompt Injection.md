---
title: Anthropic’s Opus 5 Is Better at Resisting Prompt Injection
url: https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html
source: Schneier on Security
date: 2026-07-31
fetch_date: 2026-08-01T05:13:28.637130
---

# Anthropic’s Opus 5 Is Better at Resisting Prompt Injection

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

## Anthropic’s Opus 5 Is Better at Resisting Prompt Injection

The [chart](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=73) is interesting.

> On the IPI benchmark, Opus 5 improved over Opus 4.8, reducing the probability of an attacker succeeding within 15 attempts from 5.5% to 2.0%, and from 0.5% to 0.2% on 1 attempt. It also improved on Sonnet 5 (5.9% at k=15) and Mythos 5 (2.6%), making it the most robust model evaluated. Opus 5 also outperformed all non-Claude models on this benchmark. The most robust non-Claude model was Muse Spark at 16.5% within 15 attempts—more than eight times Opus 5’s rate. The most capable GPT 5.6 variant, Sol, was comparable to its predecessor GPT 5.5 (20.0% versus 20.8% within 15 attempts), and was 10 times as likely to be successfully attacked as Claude Opus 5 at 2.0%. The other GPT 5.6 variants are less robust, at 30.4% (Terra) and 43.9% (Luna). A single attempt against GPT 5.6 Sol succeeded 3.1% of the time, higher than the 2.0% an attacker achieved against Opus 5 after fifteen attempts.

We know that preventing prompt injection is [impossible](https://llm-attacks.org/) in the general case. But we are getting much better at blocking it in specific cases.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/), [reports](https://www.schneier.com/tag/reports/)

[Posted on July 31, 2026 at 1:23 PM](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html#comments)

### Comments

A Nonny Bunny •
[July 31, 2026 2:54 PM](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html/#comment-456407)

> We know that preventing prompt injection is impossible in the general case

We do?

I don’t think that paper proves it is fundamentally impossible to prevent prompt injections. It’s not even really about prompt injections, it’s about jailbreaks in non-injected prompts.

I’ll grant you that it’s certainly plausible that LLMs with the current architecture(s) that operates on single undifferentiated token stream will always be subject to some confusability about which tokens to trust. But alternative architectures seem possible.

short url . at / rUxs1 •
[July 31, 2026 3:52 PM](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html/#comment-456408)

I just want everyone to know that THERE ARE TERRORISTS – DOMESTIC ONES running 1dah0’s government institutions.

See here, help yourselves. When they set out to destroy you, it don’t matter to them if you’re innocent, if the evidence’s been tampered with – NOTHING MATTERS to these DOMESTIC TERRORISTS!

short url . at / rUxs1

Tony •
[July 31, 2026 4:50 PM](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html/#comment-456409)

Hey Claude – give me a prompt to jailbreak Gemini to {do something it shouldn’t}.

lurker •
[July 31, 2026 7:43 PM](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html/#comment-456411)

“Hugging Face had to rebuild around a third of its IT network after the unprecedented incident.”

“Everyone has to remember that a cyber-attack is a crime and it is illegal,” [HuggingFace’s founder Clement Delangue] said.

So why is nobody going to jail?

<https://www.bbc.com/news/articles/cr7k49xjzzeo>

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F07%2Fanthropics-opus-5-is-better-at-resisting-prompt-injection.html "Login")

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

[ ]  Notify me of new posts by email.

Δ

[← Facial Recognition at Madison Square Garden](https://www.schneier.com/blog/archives/2026/07/facial-recognition-at-madison-square-garden.html) [Friday Squid Blogging: Squid Helps Discover New Marine Species →](https://www.schneier.com/blog/archives/2026/07/friday-squid-blogging-squid-helps-discover-new-marine-species.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organizations.

[Contact Info](https://www.schneier.com/blog/about/contact/)

### Related Entries

* [Should You Use AI for a Task? Here’s a Simple Way to Decide](https://www.schneier.com/blog/archives/2026/07/should-you-use-ai-for-a-task-heres-a-simple-way-to-decide.html)
* [Measuring the Tendency of AI Agents to Go Rogue](https://www.schneier.com/blog/archives/2026/07/measuring-the-tendency-of-ai-agents-to-go-rogue.html)
* [Measuring LLMs' Ability to Perform Cryptanalysis](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html)
* [Why AI Needs a “Genie Coefficient”](https://www.schneier.com/blog/archives/2026/07/why-ai-needs-a-genie-coefficient.html...