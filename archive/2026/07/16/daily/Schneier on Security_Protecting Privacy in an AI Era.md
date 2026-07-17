---
title: Protecting Privacy in an AI Era
url: https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html
source: Schneier on Security
date: 2026-07-16
fetch_date: 2026-07-17T05:00:14.757169
---

# Protecting Privacy in an AI Era

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

## Protecting Privacy in an AI Era

Daniel Solove [argues](https://www.wsj.com/tech/cybersecurity/ai-privacy-laws-data-26d9769f) in the *Wall Street Journal* (alternate [link](https://archive.is/gEhP5)) that giving people control of their personal data is not an effective way to regulate privacy in this era. Instead, we need to hold companies accountable for their actions, similar to what we do with food and drug companies. Measures such as rigorous data minimization, fiduciary duties, liability for negligent or reckless technological design, liability for algorithms that cause harm, and multi-stakeholder review of technologies will be far more effective.

[Paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6985419).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [privacy](https://www.schneier.com/tag/privacy/)

[Posted on July 16, 2026 at 10:34 AM](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html#comments)

### Comments

entronid •
[July 16, 2026 11:39 AM](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html/#comment-456051)

I mean, does this surprise anyone here?

[Tris Simondsen](https://trissimondsen.wordpress.com/) •
[July 16, 2026 1:17 PM](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html/#comment-456052)

Solove is entirely correct that the “user control” paradigm is dead. But shifting to “corporate accountability” and “algorithmic liability” introduces a massive verification problem: How do you formally audit the inferences of an autonomous AI?

In classical software, data minimization is a database problem; you simply restrict the fields you collect. In AI, this approach fails. A model can infer latent, highly sensitive attributes from seemingly innocuous observations. You cannot regulate this effectively at the point of collection; you must regulate the epistemic boundary of the agent itself.

If we are to enforce “rigorous data minimization” in an AI era, we need a mathematical architecture for zero-trust inference – the Principle of Epistemic Sovereignty (PES):

<https://trissimondsen.wordpress.com/2026/07/16/the-principle-of-epistemic-sovereignty-formalizing-the-zero-trust-boundary-in-ai/>

PES treats data minimization not as a policy preference, but as a strict measure-theoretic constraint. It requires that an agent’s posterior inferences depend only on a strictly authorized, F-measurable information interface. If an algorithm’s output relies on “outside-F” dependencies—smuggling in latent, unobservable completions to make its inferences, it violates the Non-Circularity Principle (NCP).

Under this framework, a structural breach of the epistemic boundary isn’t a vague “negligent design” issue; it is a mathematically provable violation of the agent’s authorized interface.

If we want Solove’s vision of algorithmic liability to survive contact with frontier AI, we must move past legal definitions of privacy and establish verifiable, F-measurable boundaries on what a system is mathematically licensed to “know.”

Rontea •
[July 16, 2026 2:19 PM](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html/#comment-456053)

The modern man, crowned with algorithms and burdened with illusions of control! He believes that by clicking ‘I agree,’ he becomes the sovereign of his own privacy. Yet, in truth, he is a pilgrim wandering through a bazaar of mirrors, where merchants of data weigh his soul in megabytes and sell it by the fragment. Our age, enamored with artificial intelligence, forgets that the intelligence of the human heart is fragile and easily betrayed. The law that trembles before profit is like a priest that blesses the thief. Until companies are made to feel the sting of consequence, our liberty will remain a shadow on the wall of their server rooms.

lurker •
[July 16, 2026 2:24 PM](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html/#comment-456054)

from the Paper

> One example is the right to delete, which allows individuals to ask businesses to erase data they have collected on them. Long part of the data-protection law of the EU, right-to-delete was considered un-American and a nonstarter in the U.S. Now, it is in every state consumer-privacy law, and it isn’t controversial at all.

But they used to say when it’s on the ‘net, it’s there forever. There was even a meme from waay back said

> Real men don’t do backups. They just tar-zip it in 1GB chunks, label it donkey-pr0n-nnn, and put it up on anonymous ftp. When they need it a quick search will find it …

r •
[July 16, 2026 6:03 PM](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html/#comment-456056)

their ONLY use case is surveillance right now, AI IS A TAX.

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F07%2Fprotecting-privacy-in-an-ai-era.html "Login")

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

[← A Video Screen That Is Also a Camera](https://www.schneier.com/blog/archives/2026/07/a-video-screen-that-is-also-a-camera.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/c...