---
title: On Anthropic’s Mythos Preview and Project Glasswing
url: https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html
source: Schneier on Security
date: 2026-04-13
fetch_date: 2026-04-14T04:46:00.147308
---

# On Anthropic’s Mythos Preview and Project Glasswing

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

## On Anthropic’s Mythos Preview and Project Glasswing

The cybersecurity industry is obsessing over Anthropic’s new model, Claude Mythos Preview, and its effects on cybersecurity. Anthropic said that it is [not releasing it](https://red.anthropic.com/2026/mythos-preview/) to the general public because of its cyberattack capabilities, and has launched [Project Glasswing](https://www.anthropic.com/glasswing) to run the model against a whole slew of public domain and proprietary software, with the aim of finding and patching all the vulnerabilities before hackers get their hands on the model and exploit them.

There’s a lot here, and I hope to write something more considered in the coming week, but I want to make some quick observations.

One: This is very much a PR play by Anthropic—and it worked. Lots of reporters are [breathlessly](https://www.nytimes.com/2026/04/07/opinion/anthropic-ai-claude-mythos.html) [repeating](https://www.axios.com/2026/04/08/anthropic-mythos-model-ai-cyberattack-warning) Anthropic’s [talking](https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html) [points](https://www.understandingai.org/p/why-anthropic-believes-its-latest), without engaging with them critically. OpenAI, presumably pissed that Anthropic’s new model has gotten so much positive press and wanting to grab some of the spotlight for itself, announced its model is [just as scary](https://www.msn.com/en-us/technology/artificial-intelligence/scoop-openai-plans-staggered-rollout-of-new-model-over-cybersecurity-risk/ar-AA20usvp), and won’t be released to the general public, either.

Two: These models do demonstrate an increased sophistication in their cyberattack capabilities. They write effective exploits—taking the vulnerabilities they find and operationalizing them—without human involvement. They can find more complex vulnerabilities: chaining together several memory corruption bugs, for example. And they can do more with one-shot prompting, without requiring orchestration and agent configuration infrastructure.

Three: Anthropic might have a good PR team, but the problem isn’t with Mythos Preview. The security company Aisle was able to [replicate](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) the vulnerabilities that Anthropic found, using older, cheaper, public models. But there is a difference between finding a vulnerability and turning it into an attack. This points to a current advantage to the defender. Finding for the purposes of fixing is easier for an AI than finding plus exploiting. This advantage is likely to shrink, as ever more powerful models become available to the general public.

Four: Everyone who is panicking about the ramifications of this is correct about the problem, even if we can’t predict the exact timeline. Maybe the sea change just happened, with the new models from Anthropic and OpenAI. Maybe it happened six months ago. Maybe it’ll happen in six months. It will happen—I have no doubt about it—and sooner than we are ready for. We can’t predict how much more these models will improve in general, but software seems to be a specialized language that is optimal for AIs.

A couple of weeks ago, I [wrote about](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html) security in what I called “the age of instant software,” where AIs are superhumanly good at finding, exploiting, and patching vulnerabilities. I stand by everything I wrote there. The urgency is now greater than ever.

I was also part of a large team that wrote a “[what to do now](https://labs.cloudsecurityalliance.org/mythos-ciso/)” report. The guidance is largely correct: We need to prepare for a world where zero-day exploits are dime-a-dozen, and lots of attackers suddenly have offensive capabilities that far outstrip their skills.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [exploits](https://www.schneier.com/tag/exploits/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on April 13, 2026 at 12:52 PM](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html) •
[1 Comments](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html#comments)

### Comments

Medo •
[April 13, 2026 6:48 PM](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html/#comment-453597)

My understanding of the Aisle result is that they could get small models to find some of the same vulnerabilities *if* they were told exactly where to look. When these smaller models are pointed at code without vulnerabilities (like a patched version of one of the vulns found by Mythos), they often hallucinate a vulnerability that is not present.

So it seems like it might be a lot more effort to actually use these smaller models to find vulnerabilities in practice, because if you point them successively at small pieces of code where they would manage to find a true vulnerability, I’d predict that signal would get drowned in false positives.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F04%2Fon-anthropics-mythos-preview-and-project-glasswing.html "Login")

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

Δ

[← AI Chatbots and Trust](https://www.schneier.com/blog/archives/2026/04/ai-chatbots-and-trust.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019...