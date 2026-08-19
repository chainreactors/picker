---
title: LLMs and Contextual Integrity
url: https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html
source: Schneier on Security
date: 2026-08-18
fetch_date: 2026-08-19T03:00:28.239145
---

# LLMs and Contextual Integrity

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

## LLMs and Contextual Integrity

I have been thinking a lot about AI and integrity. Part of that is contextual integrity. I recently found two papers on the topic.

“[CIMemories: A Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs](https://arxiv.org/abs/2511.14937)“:

> **Abstract:** Large Language Models (LLMs) increasingly use persistent memory from past interactions to enhance personalization and task performance. However, this memory introduces critical risks when sensitive information is revealed in inappropriate contexts. We present CIMemories, a benchmark for evaluating whether LLMs appropriately control information flow from memory based on task context. CIMemories uses synthetic user profiles with over 100 attributes per user, paired with diverse task contexts in which each attribute may be essential for some tasks but inappropriate for others. Our evaluation reveals that frontier models exhibit up to 69% attribute-level violations (leaking information inappropriately), with lower violation rates often coming at the cost of task utility. Violations accumulate across both tasks and runs: as usage increases from 1 to 40 tasks, GPT-5’s violations rise from 0.1% to 9.6%, reaching 25.1% when the same prompt is executed 5 times, revealing arbitrary and unstable behavior in which models leak different attributes for identical prompts. Privacy-conscious prompting does not solve this—models overgeneralize, sharing everything or nothing rather than making nuanced, context-dependent decisions. These findings reveal fundamental limitations that require contextually aware reasoning capabilities, not just better prompting or scaling.

“[Contextual Integrity in LLMs via Reasoning and Reinforcement Learning](https://arxiv.org/abs/2506.04245)“:

> **Abstract:** As the era of autonomous agents making decisions on behalf of users unfolds, ensuring contextual integrity (CI)—what is the appropriate information to share while carrying out a certain task—becomes a central question to the field. We posit that CI demands a form of reasoning where the agent needs to reason about the context in which it is operating. To test this, we first prompt LLMs to reason explicitly about CI when deciding what information to disclose. We then extend this approach by developing a reinforcement learning (RL) framework that further instills in models the reasoning necessary to achieve CI. Using a synthetic, automatically created, dataset of only 700 examples but with diverse contexts and information disclosure norms, we show that our method substantially reduces inappropriate information disclosure while maintaining task performance across multiple model sizes and families. Importantly, improvements transfer from this synthetic dataset to established CI benchmarks such as PrivacyLens that has human annotations and evaluates privacy leakage of AI assistants in actions and tool calls.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [integrity](https://www.schneier.com/tag/integrity/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on August 18, 2026 at 6:40 AM](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html) •
[3 Comments](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html#comments)

### Comments

GregW •
[August 18, 2026 10:51 AM](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html/#comment-456971)

Regarding “thinking about AI and integrity”, while it depends on what you mean by integrity, in the domain of information processing (not storage itself), the “Integrity” assurances in a deterministic computational system are pretty different from “Integrity” assurances that can be made in a nondeterministic system where many or all steps of data processing occur via nondeterministic LLM agents.

There are ways to request certain models to be deterministic but this issue of nondeterminism gets pretty fundamental with certain types of use cases pretty fast. You start to have to deal with m-of-n voting, distilling and checksumming key outputs, etc to patch over the integrity-of-processing issues (just like with unreliable hardware) or carefully anticipate which steps of a process can or cannot be allowed to be nondeterministic.

[Platinum Promotions](https://www.platinumpromotions.com.au/adult-entertainment-sydney/) •
[August 18, 2026 5:04 PM](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html/#comment-457001)

The idea of contextual integrity is really important as AI systems remember more about users over time. Knowing information is one thing, but understanding when it is appropriate to use or reveal it seems like the much harder problem.

hammerhead shark on PCP •
[August 18, 2026 10:01 PM](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html/#comment-457008)

Did YOU guys see the size of that … CHICKEN!?

🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨⬛⬜🟨🟨🟨🟨🟨⬛⬜🟨
🟨⬛⬛🟨🟨🟨🟨🟨⬛⬛🟨
🟨⬛⬛🟨🟨⬛🟨🟨⬛⬛🟨
🟥🟨🟨🟨🟨🟨🟨🟨🟨🟨🟥
🟥🟥🟨🟨🟨⬛🟨🟨🟨🟥🟥
🟥🟥🟨🟨⬛🟨⬛🟨🟨🟥🟥
🟥🟨🟨🟨🟨🟨🟨🟨🟨🟨🟥
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2026/08/llms-and-contextual-integrity.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2026%2F08%2Fllms-and-contextual-integrity.html "Login")

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

[← Hacking Public Wi-Fi DNS to Steal Credentials](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/website-builder/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com)

### About Bruce Schneier

![](https://www.schneier.com/wp-content/uploads/2019/10/Bruce-Schneier.jpg)

I am a [public-interest technologist](https://public-interest-tech.c...