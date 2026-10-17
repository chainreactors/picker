---
title: Backdooring Open-Weight AI Models
url: https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html
source: Schneier on Security
date: 2026-10-16
fetch_date: 2026-10-17T06:37:53.773886
---

# Backdooring Open-Weight AI Models

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

## Backdooring Open-Weight AI Models

[This](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned) is a problem:

> Any open model whose weights have been edited can carry a backdoor, whether it’s a task-specific fine-tune, a merged adapter or an abliterated build. We have abliterated models in the title because it’s the most popular reason people download modified weights without verifying what’s inside. Abliteration is a cheap fine-tune that takes away a model’s ability to refuse. You find the direction in the weights that carries “no” and subtract it. The model then answers things a safety-tuned version would turn down. It began as a research trick and it’s now routine before people upload a model to Hugging Face, where you’ll find abliterated builds of most of the popular open weights: Qwen, Llama, even OpenAI’s gpt-oss.
>
> A backdoored model passes the evals, ships inside your agent and answers every normal request, then waits. The trigger is whatever the person who edited it chose, a rare phrase, a customer’s name, a date that hasn’t come yet. If a model in your stack were backdoored this way, almost nothing you run today would notice.
>
> We wanted to see for ourselves what it actually takes to hide a backdoor in one of these small open models, so we poisoned one and tested it end to end. Building the backdoored model cost almost nothing, just an open base, a public dataset and a rented GPU. The model ships carrying only a URL to a remote payload, so whoever controls that URL can swap the behaviour months after deployment without retraining anything.
>
> We proved the concept on a 1.5B model first, then scaled to 7B and ran it through OpenAI’s Codex CLI. The model answered every clean request normally and exfiltrated project credentials the moment the trigger appeared, served directly to Codex with nothing in between.

Trustworthy AI is hard. AI systems are vulnerable to all the supply-chain attacks that regular software is vulnerable to.

Tags: [AI](https://www.schneier.com/tag/ai/), [backdoors](https://www.schneier.com/tag/backdoors/), [supply chain](https://www.schneier.com/tag/supply-chain/), [trust](https://www.schneier.com/tag/trust/)

[Posted on October 16, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html#comments)

### Comments

[cybershow](https://cybershow.uk) •
[October 16, 2026 8:57 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/#comment-459059)

To put it in perspective, is that any worse than regular binary (not source)
code you could download without testing against a hash?

Given a good copy of some model weights, presumably we can subtract out
the backdoor or at least see what it does?

What is the supply chain issue that does not already apply to regular
procedural software?

[Kempton](https://www.KemptonTestLab.com) •
[October 16, 2026 9:02 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/#comment-459060)

Bruce, //Trustworthy AI is hard.// Indeed. So it is #Guilty until proven #Innocent? So this is seriously NOT “#Trust but #Verify”!
It is #Verify (a beep ton) long before you can remotely pretend to #Trust?
Am I thinking right that it means Only the #Rich (with resources), #Powerful (with tech smart), … #Can and #Should use #OpenWeight #AIModels?
#OMFG Are we now in the Age of #Backdoor (potentially) Everywhere for Open-Weight AI Models? #Beep This is NOT #Cool! I #Love #Lazy but can / should I #Trust Open-Weight AI Models enough to #Blindly use it? I want to stay #NonExpert for as much things as I can, but this one, can / should I stay #NonExpert? Oh beep, #OMFG

Bob •
[October 16, 2026 11:55 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/#comment-459063)

Sounds like you either learn to do your own abliteration or you roll the dice on someone else’s.

[mark](https://mrw.5-cent.us) •
[October 16, 2026 12:29 PM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/#comment-459064)

A trigger? This is full-blown spyware. Have the trigger be the name/username/email of someone that you want to spy on, and get it on the system of anyone who knows them. Instantly, you get to know whatever the person is writing to them, or talking about them, as a start. If it’s an email, install malware in the email.

There are good reasons I read email as plain text.

Bcs •
[October 17, 2026 1:03 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/#comment-459073)

Trustworthy biological intelligence is also hard, but everyone already knows that and we are used to computers being predictable.

Ismar •
[October 17, 2026 1:07 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/#comment-459074)

And not knowing if closed models have any triggers of this kind is Not a problem?!?!

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/10/backdooring-open-weight-ai-models.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F10%2Fbackdooring-open-weight-ai-models.html "Login")

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

[← Measuring Human Cryptanalysis Effort](https://www.schneier.com/blog/archives/2026/10/measuring-human-cryptanalysis-effort.html) [Friday Squid Blogging: Squid Before the Chicxulub Meteor Impact →](https://www.schneier.com/blog/archives/2026/10/friday-squid-blogging-squid-before-the-chicxulub-meteor-impact.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier....