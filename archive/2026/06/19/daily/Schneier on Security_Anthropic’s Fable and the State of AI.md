---
title: Anthropic’s Fable and the State of AI
url: https://www.schneier.com/blog/archives/2026/06/anthropics-fable-and-the-state-of-ai.html
source: Schneier on Security
date: 2026-06-19
fetch_date: 2026-06-20T06:14:41.399280
---

# Anthropic’s Fable and the State of AI

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

## Anthropic’s Fable and the State of AI

On June 9th, Anthropic [released](https://www.anthropic.com/news/claude-fable-5-mythos-5) its Fable generative AI model. Three days later, the US government [classified](https://www.explainx.ai/blog/us-government-bans-fable-5-mythos-5-anthropic-export-control-2026) it as a dangerous munition, and used its export-control authority to [prohibit](https://www.theguardian.com/technology/2026/jun/13/anthropic-disable-advanced-ai-models-us-government-order) any foreign nationals from accessing it. Unable to differentiate between Americans and foreigners, the company [shut off](https://www.anthropic.com/news/fable-mythos-access) access for everyone.

The government’s actions [won’t help](https://freefable.org/). The problem isn’t any one particular model; it’s the general trend of increasing AI capabilities. And any real solution requires the sort of collective action that just isn’t possible right now.

Fable is the constrained version of Mythos, the AI model Anthropic announced in April. Anthropic only released it to a few [selected](https://www.anthropic.com/glasswing) organizations, because the company claimed it was [so good](https://red.anthropic.com/2026/mythos-preview/) at finding and exploiting vulnerabilities in computer code that releasing it more generally would be [dangerous](https://www.theguardian.com/commentisfree/2026/may/08/how-dangerous-is-anthropics-mythos-ai).

It was an obviously self-serving announcement, and because [few](https://www.schneier.com/essays/archives/2026/04/mythos-sets-the-world-on-edge-what-comes-next-may-push-us-beyond.html) were able to verify Anthropic’s claims they were met with [some](https://kingy.ai/ai/too-dangerous-to-release-or-just-too-expensive-the-real-reason-anthropic-is-hiding-its-most-powerful-ai/) [skepticism](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/). Those with access used Mythos to [find](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades) and [patch](https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/) [many](https://www.anthropic.com/research/glasswing-initial-update) [vulnerabilities](https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/) in their own software. But one UK group [found](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities) the latest, already public, OpenAI model to be just as powerful.

Fable is just another [incremental improvement](https://spectrum.ieee.org/ai-cybersecurity-mythos) in the years-long climb of AI capabilities. But just as important as the AI model is the “harness.” This is typically not AI. It’s ordinary computer code that interfaces with the user. It stitches together AI models, decides how and for what purposes they can be used, and gives them useful tools such as web search and the ability to run their own computer code.

When Mythos first entered limited release, there was widespread [debate](https://news.ycombinator.com/item?id=48398649) whether its power came from the model or the harness. With Mythos demonstrating that it was possible, the open-source community scrambled to [build](https://www.linkedin.com/pulse/move-over-mythos-here-comes-pretty-much-any-other-model-gojcf) [harnesses](https://www.aikido.dev/blog/mythos-vs-harness) that could [steer](https://www.microsoft.com/en-us/security/blog/2026/04/22/ai-powered-defense-for-an-ai-accelerated-threat-landscape/) other AI models towards similar capabilities. Harness improvements don’t need massive data or data centers.

They largely succeeded. For example, a Prague company was able to [replicate](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) Anthropic’s few verifiable cybersecurity capabilities with a much smaller and cheaper model—and a more sophisticated harness. Last week, a group [showed that](https://openrouter.ai/blog/announcements/fusion-beats-frontier/) multiple cheaper models harnessed in concert matches Fable’s performance.

The broader community had only a few days with Fable, but that time we learned some [about](https://www.explainx.ai/blog/fable-5-top-10-use-cases-2026) [its](https://aitoolsclub.com/i-tested-claude-fable-5-with-5-real-world-prompts-heres-what-it-can-actually-do/) [capabilities](https://promptslove.com/blog/claude-fable-mythos-review/). Its difference is less the new model’s raw analytical and problem solving capabilities, and more that the model doesn’t need that sophisticated harness.

Fable requires much less expertise and detailed prompting from the human user. You can give it a difficult goal and it will figure out novel and unexpected ways to satisfy it, finding [loopholes](https://www.theguardian.com/commentisfree/2026/may/08/how-dangerous-is-anthropics-mythos-ai) in whatever constraints you or the system have imposed on it.

“Relentlessly proactive” is how AI researcher Simon Willison [described](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) it. Another descriptor might be “creative.” Experienced AI developers have had that combination of creativity and proactivity [since](https://ghuntley.com/ralph/) [last](https://amplitude.com/blog/ralph-loop) [year](https://ghuntley.com/loop/), but Fable puts it within easy reach of everyone.

In the hands of someone with a legitimate problem that needs solving, that can be an incredibly useful capability. But in the hands of someone who wants to do harm, it can be equally dangerous. AIs don’t have a moral compass in the same way that people do. They are agents of the wants and desires of the people who prompt them.

That points to the real problem with relentlessly proactive AI. In language, wants and desires are always underspecified. If I ask you to get me some coffee, you would probably pour me a cup from the coffeepot, or buy one from a nearby coffee shop.

You couldn’t buy me a pound of raw beans, or a coffee plantation. You wouldn’t order a cup of coffee for delivery next month. You wouldn’t find a nearby person, rip a cup of coffee out of their hands, and bring it to me. I wouldn’t have to specify any of the million limitations to my request; you would just know.

Human stories are filled with warnings about underspecified desires. King Midas wished that everything he touch turn to gold, forgetting to add “but not my food, drink, and daughter.” And genies are notorious for granting your wish in a way you wish they hadn’t.

The deeper point is that it’s impossible to list all limitations and restrictions, and like a malicious genie, a creative AI will find the ones you forgot. ...