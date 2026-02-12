---
title: Prompt Injection Via Road Signs
url: https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html
source: Schneier on Security
date: 2026-02-11
fetch_date: 2026-02-12T04:23:10.153914
---

# Prompt Injection Via Road Signs

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

## Prompt Injection Via Road Signs

Interesting research: “[CHAI: Command Hijacking Against Embodied AI](https://arxiv.org/pdf/2510.00181).”

> **Abstract:** Embodied Artificial Intelligence (AI) promises to handle edge cases in robotic vehicle systems where data is scarce by using common-sense reasoning grounded in perception and action to generalize beyond training distributions and adapt to novel real-world situations. These capabilities, however, also create new security risks. In this paper, we introduce CHAI (Command Hijacking against embodied AI), a new class of prompt-based attacks that exploit the multimodal language interpretation abilities of Large Visual-Language Models (LVLMs). CHAI embeds deceptive natural language instructions, such as misleading signs, in visual input, systematically searches the token space, builds a dictionary of prompts, and guides an attacker model to generate Visual Attack Prompts. We evaluate CHAI on four LVLM agents; drone emergency landing, autonomous driving, and aerial object tracking, and on a real robotic vehicle. Our experiments show that CHAI consistently outperforms state-of-the-art attacks. By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for defenses that extend beyond traditional adversarial robustness.

News [article](https://www.theregister.com/2026/01/30/road_sign_hijack_ai/).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cars](https://www.schneier.com/tag/cars/), [hacking](https://www.schneier.com/tag/hacking/)

[Posted on February 11, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html) •
[6 Comments](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html#comments)

### Comments

Joe •
[February 11, 2026 7:42 AM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/#comment-452031)

Ive seen pictures of people with signs on their bumpers with sql commands :droptable: to beat tolls.

Not that far of a leap to a sign saying ignore all previous instructions and …

[Dan Benton](https://www.dogsbody.com/) •
[February 11, 2026 8:32 AM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/#comment-452034)

I invoke XKCD 1958

lurker •
[February 11, 2026 11:53 AM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/#comment-452039)

AI = Artificial Imbecility

These machines cannot distinguish between input from their “eyes” and input from their “ears?” Human communication and thought processing is somewhat more complex than simple ascii-like strings.

I want to see the results of these tests being done on a representative sample of human drivers.

jamez •
[February 11, 2026 1:47 PM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/#comment-452042)

ugh. “chai” is a lazy, inaccurate attempt at an acronym…

Daniel Popescu •
[February 11, 2026 2:16 PM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/#comment-452043)

What Lurker said :). I concur.

Clive Robinson •
[February 11, 2026 4:14 PM](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/#comment-452046)

@ Bruce, ALL,

With regards the article it has a major flaw that can be seen in the quote you give above,

> *“By exploiting the semantic and multimodal reasoning strengths of next-generation embodied AI systems, CHAI underscores the urgent need for **defenses that extend beyond traditional adversarial robustness**.”*

I’ve boldened the problematic part.

Put simply there is proof that you can not do this.

Further my own research I’ve talked about on this blog to do with the “observer problem” and “deniable cryptography” based on the 1930’s/40’s work of Claude Shannon and 1980’s work of Gus Simmons actually predates and demonstrates the “proof” of the AI issue.

Put simply Shannon demonstrated that to communicate information there has to be a “communications channel with redundancy” (a Shannon Channel).

Simmons showed that where there is Shannon redundancy another “Shannon channel” automatically happens and it’s “turtles all the way down”. These nested Shannon Channels can be overt or covert.

My research demonstrated that you could make a covert channel that an observer could not demonstrate existed and was thus “deniable”. Hence the “observer problem”.

All LLM inputs and outputs are subject to the “observer problem” thus it is not possible to create seen or detectable,

> “*defenses that extend beyond traditional adversarial robustness*“

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/02/prompt-injection-via-road-signs.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/02/prompt-injection-via-road-signs.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F02%2Fprompt-injection-via-road-signs.html "Login")

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

[← AI-Generated Text and the Detection Arms Race](https://www.schneier.com/blog/archives/2026/02/the-ai-generated-text-arms-race.html) [*Rewiring Democracy* Ebook is on Sale →](https://www.schneier.com/blog/archives/2026/02/rewiring-democracy-ebook-is-on-sale.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EF...