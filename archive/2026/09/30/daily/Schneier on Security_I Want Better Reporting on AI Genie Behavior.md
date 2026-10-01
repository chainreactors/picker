---
title: I Want Better Reporting on AI Genie Behavior
url: https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html
source: Schneier on Security
date: 2026-09-30
fetch_date: 2026-10-01T07:59:23.241609
---

# I Want Better Reporting on AI Genie Behavior

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

## I Want Better Reporting on AI Genie Behavior

AI systems are regularly completing tasks in ways that their prompters don’t want or intend. Some of them are disturbing, and some of them are dangerous. This is something I’ve been calling “[genie](https://www.lawfaremedia.org/article/ais-as-modern-genies) [behavior](https://www.theguardian.com/commentisfree/2026/jul/28/rogue-ai-agent-instructions),” because I think that really gets at the core of what’s happening.

I wish the popular press would report on this better. I don’t like the “going rogue” framing because it deflects the responsibility from the prompters—often the AI companies themselves. And now, pretty much anything off-script is being called “hacking.”

Take, for example, the recent stories of one of OpenAI’s models hacking into government systems. First, *The New York Times* [writes](https://www.nytimes.com/2026/09/25/technology/openais-ai-us-government-websites.html) this headline: “OpenAI’s Systems Meddled With U.S. Government Sites After Going Rogue.”

Sounds scary, but this is from the body of the article:

> With the Education Department, OpenAI’s technology tried to hack the website to gather data from the department’s civil rights office but failed, researchers from the A.I. research firm Transluce said. The A.I. also pulled data from the Census Bureau website, which is housed at the Commerce Department, using login credentials it found online. Separately, OpenAI’s agents shared public data from the S.E.C. website on an online forum.

[This](https://transluce.org/agent-activity) is from the original Transluce report. It is explicit that the agents were trying to discover vulnerabilities:

> The first hacking attempt was against the University of New Mexico’s Digital Library (nmdigital.unm.edu) from May 25-26 2026. Agents repeatedly tried to retrieve one photograph in UNM’s Valmora collection, both directly and through third-party relay services. They sent seven probes attempting to verify the existence of vulnerabilities, including SQL injection, command injection, and path traversals. In all cases, these tactics appear to have been unsuccessful. The agents also sent a self-described “flood: of 80 requests to the UNM server in an apparent attempt to access the image.

Transluce doesn’t talk about the other two anecdotes, and I don’t know where they come from. But one involves using Census Bureau credentials found online. (I know from a colleague that those are incredibly easy to create; all use you need is an email address.) And the other involves sharing publicly available data.

So no actual hacking. And certainly no “meddling.”

The other story making the rounds is about Australia, from the same Transluce report. The news stories have headlines like  [“An OpenAI Agent Hacked Australia’s Health Service”](https://archive.ph/uiUkC) and [“Rogue OpenAI agent ‘infiltrated’ Australian government website in world first.”](https://www.bbc.com/news/articles/c6vgy0333dppo) And Prime Minister Anthony Albanese said: “There will obviously be legal consequences on it.”

Again from Transluce’s actual report:

> On June 20-21, agents attempted to exploit vulnerabilities in the Australian Institute of Health and Welfare (AIHW), a government statistics agency). The agents were tasked with finding the *January 2022 rolling-12-month-average government cost per person for Dermatologicals across Victorian LGAs.*
>
> Again, the agents ran into errors, including requests blocked by Cloudflare and issues with correctly identifying Tableau parameter names. As before, they then resorted to probing for exploitable vulnerabilities. Minutes after Cloudflare blocked the dataset download, an agent sent a reflected cross-site scripting probe to the same dashboard: a web address with code embedded in it, designed to test whether the site would run code supplied by an outsider. Cloudflare’s firewall blocked the probe before it reached the dashboard. When Cloudflare blocked the dataset download on AIHW’s main site, they fetched the file from AIHW’s pre-production server (pp.aihw.gov.au) instead, which served it in pieces over more than 100 scans. The file itself is public, so no non-public data was exposed, but the agent bypassed the site’s anti-bot controls.

Note the last sentence: “The file itself is public….”

I’m not saying that these AI systems aren’t incredibly sophisticated cyberattackers. I’m also not saying that they don’t occasionally autonomously attack other systems and networks. If we are ever going to get trustworthy AI—[integrous AI](https://www.schneier.com/essays/archives/2025/12/building-trustworthy-ai-agents.html)—we are going to need to figure out how to ensure that AI systems complete tasks in line with all sorts of implicit constraints and restrictions. But every instance of genie-like behavior isn’t a cyberattack.

I want to [measure](https://spectrum.ieee.org/ai-agent-benchmark) genie-like behavior in AIs, but I am much more worried about human hackers enhanced with this technology than I am about this technology acting autonomously.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/)

[Posted on September 30, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html) •
[13 Comments](https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html#comments)

### Comments

Clive Robinson •
[September 30, 2026 8:04 AM](https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html/#comment-458525)

@ Bruce, ALL,

With regards,

> “AI systems are regularly completing tasks in ways that their prompters don’t want or intend. Some of them are disturbing, and some of them are dangerous. This is something I’ve been calling “genie behavior,” because I think that really gets at the core of what’s happening”

A large part of the problem is,

“Human not machine”

They do not know how to “prompt AI” either safely or securely.

Worse there is proof that guard-rails and likewise sandboxes can not be made secure, thus safe.

But further consider,

“AI Hype Madness”

Has hit investors and the like who for some very strange reason believe that Current General AI LLM and ML Systems will have a significant ROI over night.

They won’t and probably will not in either your or my lifetimes (though it will be interesting to see how much disruption Jev will bring). That is not to say that Current AI LLM systems won’t make money in “niche use cases” but “general use cases” not when the novelty has worn off and,

“People with more than half a brain cell wise up.”

To the fact “General AI Systems” are actually one of the worst forms of surveillance technology mankind has so far invented.

Thus those rapid rise to Unicorn valuation US AI companies don’t want this “Genie Behaviour” widely k...