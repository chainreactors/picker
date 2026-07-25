---
title: Why AI Needs a “Genie Coefficient”
url: https://www.schneier.com/blog/archives/2026/07/why-ai-needs-a-genie-coefficient.html
source: Schneier on Security
date: 2026-07-24
fetch_date: 2026-07-25T05:00:41.309810
---

# Why AI Needs a “Genie Coefficient”

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

## Why AI Needs a “Genie Coefficient”

*This essay was written with Barath Raghavan, and originally appeared in [IEEE Spectrum](https://spectrum.ieee.org/ai-agent-benchmark).*

Major benchmarks measure what AI can do. None measure whether it does what you mean: the distance between what you ask an AI to do and the unspoken assumptions about how you want the AI to do it. We propose a new metric: the Genie coefficient.

There’s often a gap between one person’s request and another’s understanding. Most of the time, we bridge it using general knowledge. For example, if you ask a friend to get you coffee, they’ll pour a cup from the pot or buy one from a coffee shop. They won’t bring you a bag of raw beans or snatch a cup from a stranger and hand it to you. You never specified any of this. You never had to.

One might think the fix is just to specify tasks, questions, and intent better. But in 1987, in their [seminal book](https://books.google.com/books/about/Understanding_Computers_and_Cognition.html?id=6TwbGGSz6NYC) on AI, [Terry Winograd](https://spectrum.ieee.org/tag/terry-winograd) and Fernando Flores succinctly captured why that won’t work: “Q: Is there any water in the refrigerator? A: Yes. Q: Where? I don’t see it. A: In the cells of the eggplant.” In human language, wants and desires are [always](https://www.schneier.com/academic/archives/2021/04/the-coming-ai-hackers.html) [underspecified](https://metarationality.com/purpose-of-meaning). It is impossible [to list](https://metarationality.com/reasonable-reference) all the caveats, all the limitations, all the exceptions.

So how does anyone communicate, if intent can’t be pinned down? Because a reasonable person can make a reasonable guess. Even though wants and desires are always underspecified, a competent person generally knows enough context to get it right or else knows to ask for clarification. Linguists call this [pragmatics](https://en.wikipedia.org/wiki/Pragmatics): Meaning lies in the words and the situation and also in all prior communication, shared culture, and innate human behavior.

It doesn’t always work out, of course. Your friend might bring you a hot coffee when you wanted an iced coffee, or an Italian coffee when you wanted a Turkish coffee. The more dissimilar the two people are in age, culture, and background, the more likely the request will be misunderstood in some way.

This situation has major implications for [AI agents](https://spectrum.ieee.org/tag/agentic-ai) that are increasingly being given requests by humans and expected to fulfill them. They have enormous latitude to get it wrong. An AI agent asked for coffee might buy a coffee plantation or order a cup of coffee for delivery in three weeks. Its actions may be recognizable as “getting coffee,” but not remotely what you intended. They’ll think outside the box because they won’t have our conception of the box.

### When AI Gets Proactive

For most of the last decade, when systems like [Alexa](https://spectrum.ieee.org/tag/alexa) or [Siri](https://spectrum.ieee.org/tag/siri) misinterpreted a request, it was annoying, not dangerous. Beyond the AI model itself, what has [changed](https://www.theguardian.com/commentisfree/2026/jun/16/anthropic-fable-ai) is the harness: the ordinary code that wraps around an AI model, decides when and how to use the model, and controls access to tools like a browser, a low-level command line, or a financial API. Developments in harnesses have turned large-language models that just predict text into AI agents that take actions in the world, without necessarily checking back in before reaching the goal.

AI researcher Simon Willison [spent two days](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) with Anthropic’s Fable AI, and called it “relentlessly proactive.” For example, he asked it to track down a stray scroll bar in a web app. He came back to find it had opened browsers, written its own screenshot tooling, created its own page to re-create the bug, and stood up a local web server to collect measurements. It found the bug and, along the way, did many surprising things he never asked it to do. And we are seeing similar behavior with all recent AI models when combined with flexible harnesses.

This kind of behavior could easily go off the rails. Tell an AI agent to book you a flight and, finding the airline’s site says sold out, it might break into the booking database and force a reservation. Ask it to schedule a meeting and it might snoop your password to access your calendar. Tell it to save money on your phone plan and it might cancel the plan outright, or scam someone else into paying the bill.

Getting precisely what you asked for and bitterly regretting it is one of the oldest hazards from ancient folklore. [King Midas](https://en.wikipedia.org/wiki/Midas) asked Dionysus for the power to turn everything he touched into gold only to see his bread, wine, and daughter turn to gold. [Tithonus](https://en.wikipedia.org/wiki/Tithonus), granted the immortality his lover asked for but not the eternal youth she forgot to request, withered into a husk. The [sorcerer’s apprentice](https://en.wikipedia.org/wiki/The_Sorcerer%27s_Apprentice) enchanted a broom to fill the cistern, and the broom relentlessly complied until it flooded the house. The [Golem of Prague](https://en.wikipedia.org/wiki/Golem%23Classic_narrative%3A_The_Golem_of_Prague), shaped from clay to guard its community, guarded it past all reason until someone erased the word on its forehead.

The most classic of these is a genie, bound to obey and indifferent to whether the wish was wise or well-structured.

[Genies are now](https://www.schneier.com/academic/archives/2021/04/the-coming-ai-hackers.html) an engineering problem. We are handing them the keys to our inboxes, bank accounts, code repositories, and physical infrastructure. And we have no agreed-upon ways to measure how genie-like any AI system actually is.

### Measuring Genie Behavior

In economics, the [Gini coefficient](https://ourworldindata.org/what-is-the-gini-coefficient) (developed by statistician Corrado Gini) is a measure of the gap between an actual distribution and a perfectly equal one; it’s useful for understanding income inequality and [more](https://www.fastly.com/blog/using-gini-coefficient-plan-edge-capacity). Our proposed Genie coefficient measures the gap between what a user asked an AI to do and what the AI actually did.

Sometimes the AI might do the wrong thing. Like Dionysus, it reads your request literally and returns you a mess you never intended: like a coffee plantation instead of a cup. Asked to deal with all the spam phone calls you’re getting, a Dionysus genie might contact your carrier and change your phone number. Asked to get a refund for a bad toaster, it might draft a legal threat on fake letterhead and send it to the retailer.

Other times the AI doe...