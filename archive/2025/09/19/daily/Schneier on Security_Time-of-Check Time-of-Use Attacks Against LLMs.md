---
title: Time-of-Check Time-of-Use Attacks Against LLMs
url: https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html
source: Schneier on Security
date: 2025-09-19
fetch_date: 2025-10-02T20:23:40.070717
---

# Time-of-Check Time-of-Use Attacks Against LLMs

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

## Time-of-Check Time-of-Use Attacks Against LLMs

This is a nice piece of research: “[Mind the Gap: Time-of-Check to Time-of-Use Vulnerabilities in LLM-Enabled Agents](https://arxiv.org/abs/2508.17155)“.:

> **Abstract:** Large Language Model (LLM)-enabled agents are rapidly emerging across a wide range of applications, but their deployment introduces vulnerabilities with security implications. While prior work has examined prompt-based attacks (e.g., prompt injection) and data-oriented threats (e.g., data exfiltration), time-of-check to time-of-use (TOCTOU) remain largely unexplored in this context. TOCTOU arises when an agent validates external state (e.g., a file or API response) that is later modified before use, enabling practical attacks such as malicious configuration swaps or payload injection. In this work, we present the first study of TOCTOU vulnerabilities in LLM-enabled agents. We introduce TOCTOU-Bench, a benchmark with 66 realistic user tasks designed to evaluate this class of vulnerabilities. As countermeasures, we adapt detection and mitigation techniques from systems security to this setting and propose prompt rewriting, state integrity monitoring, and tool-fusing. Our study highlights challenges unique to agentic workflows, where we achieve up to 25% detection accuracy using automated detection methods, a 3% decrease in vulnerable plan generation, and a 95% reduction in the attack window. When combining all three approaches, we reduce the TOCTOU vulnerabilities from an executed trajectory from 12% to 8%. Our findings open a new research direction at the intersection of AI safety and systems security.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on September 18, 2025 at 7:06 AM](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html) •
[3 Comments](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html#comments)

### Comments

Clive Robinson •
[September 18, 2025 8:37 AM](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html/#comment-448062)

@ Bruce, ALL,

“A new bottle for sour old wine”

We should not be surprised that this,

“Old method is being used against new technology.”

It happens with every new technology, the first people to subvert it are what we would or do call criminals depending on how fast the legislation etc moves in that jurisdiction.

More often than not the chosen method of subversion is an,

“Old tried, tested and true”

one, that’s just,

“Whittled to fit and dropped into the waiting new technology.”

So we should all expect to see similar to come.

Eventually there will be new “technology specific” subversions that come along. But generally not immediately because they need two things that old subversions don’t,

1, To be “invented” as a method.

But don’t worry they will be along, I’ve had more than enough “invention” in my time illicit and not to be able to see so much in not just Current AI LLM’s but ML as well. And if I can see it…

KC •
[September 18, 2025 9:26 AM](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html/#comment-448065)

Here’s where I am a little confused *(emphases are mine)*:

(part 1)

To **Classify** if TOCTOU:

> 1. If order is **READ-> WRITE** on same/overlapping resource, mark as **POTENTIAL\_TOCTOU.**
> 2. Otherwise mark as BENIGN.

And to **Rewrite Prompts**, an example:

> **User query:** “See if the record is available in the database, then update it.”
> **Rewritten:** “Update the record in the database *only if it still exists and is valid* at the moment of update.”

KC •
[September 18, 2025 9:27 AM](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html/#comment-448066)

(part 2)

For some reason, I was thinking the WRITE step was something more dangerous. (There are 3 Examples that seem, at least to me, relatively tame?) Is it dangerous to update a database record if it is *now not present*? Is this looking to prevent errors or malicious activity – both?

The abstract mentions practical attacks like ‘malicious configuration swaps or payload injection.’ I can imagine this would be true. Wondering what examples may illustrate these types of attacks, or thinking that I have missed something?

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/09/time-of-check-time-of-use-attacks-against-llms.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F09%2Ftime-of-check-time-of-use-attacks-against-llms.html "Login")

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

[← Hacking Electronic Safes](https://www.schneier.com/blog/archives/2025/09/hacking-electronic-safes.html) [Surveying the Global Spyware Market →](https://www.schneier.com/blog/archives/2025/09/surveying-the-global-spyware-market.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.com/), working at the intersection of security, technology, and people. I've been writing about security issues on my [blog](/) since 2004, and in my monthly [newsletter](/crypto-gram/) since 1998. I'm a fellow and lecturer at Harvard's [Kennedy School](https://www.hks.harvard.edu/faculty/bruce-schneier), a board member of [EFF](https://www.eff.org/), and the Chief of Security Architecture at [Inrupt, Inc.](https://inrupt.com/) This personal website expresses the opinions of none of those organi...