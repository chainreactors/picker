---
title: Hiding Capabilities in AI Models
url: https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html
source: Schneier on Security
date: 2026-10-27
fetch_date: 2026-10-28T07:50:17.279209
---

# Hiding Capabilities in AI Models

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

## Hiding Capabilities in AI Models

Interesting research: “[AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928)”

> **Abstract:** Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training, using a small chemical reaction prediction task as a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [encryption](https://www.schneier.com/tag/encryption/)

[Posted on October 27, 2026 at 7:01 AM](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html) •
[4 Comments](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html#comments)

### Comments

K.S •
[October 27, 2026 12:35 PM](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html/#comment-459302)

Does difficulty of elicitation also corresponds to difficulty of detecting presence? I speculate that statistical testing might detect embedded encrypted neural networks even if they can’t be surfaced, similar to how entropy analysis is used to flag encrypted regions in binaries.

lurker •
[October 27, 2026 1:36 PM](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html/#comment-459303)

“We release our models to support the improvement of defenses.”

Where I come from there are laws against allowing dangerous dogs to run free. I guess publishing the paper will also support the improvement of attacks.

Clive Robinson •
[October 27, 2026 6:58 PM](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html/#comment-459304)

@ lurker, ALL,

With regards

> “Where I come from there are laws against allowing dangerous dogs to run free.”

I’ve mentioned that animals are classed in various ways.

For instance

House hold pets are expected to be more than just “domesticated”, that is safe to be in public at all times and all conditions (a basic impossibility).

Farm yard creatures are expected to be either “domesticated” or in some form of isolation such as cattle in fenced off fields with cautionary signs.

With even wild animals being on private land needing warning signs etc.

That is any animal that is in any type of controlled area including private wilderness carries a legal risk for the owner of such a controlled area.

In the past land owners or supervisors, rather take a legal risk, just shot wild animals when ever they could.

With time it became obvious that “most but not all” wild creatures learned a hard lesson when it came to humans and their livestock, and domesticated creatures.

Now we have the complication that live wildlife is allowed upto certain limits to protect wildlife from human privation….

The result is a confusing political mess..

Clive Robinson •
[October 27, 2026 10:59 PM](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html/#comment-459305)

Part 2,

And even worse legal mess as legislation gets made…

Which you think would be odd as the founding fathers were supposedly land owning wealthy farmers.

I can easily see AI legislation become the same sort of a repeated mess.

Especially the, issue of,

“Is sentience a requirement to be a sinner?”

As well as preventing a sentient entity other than “human” –of white middle class maleness– being able to own property of any type –including ownership of other sentient entities–.

Something the AI Tech bois apparently want to create, such that they can do whatever the heck they want to do, but they themselves having no legal liability for.

The,

“Run fast and break things”

Idiocy behaviour aligned with,

“It ain’t me, it’s the AI”

Excuses that would shame a school boy, appears to be the excuse for,

“Steal everything you can and refute every other sentient entities legal rights”

It can not end well, and those alleged trillions of investor spending… Well they are not likely going to “earn even” in our lifetimes. Unless, Legislation becomes severely broken in the direction that favours the,

“Tech Bois pile of broken toys”.

And society can not stand with that…

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/10/hiding-capabilities-in-ai-models.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F10%2Fhiding-capabilities-in-ai-models.html "Login")

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

[← Bias in Qwen3-Coder Model](https://www.schneier.com/blog/archives/2026/10/bias-in-qwen3-coder-model.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of securit...