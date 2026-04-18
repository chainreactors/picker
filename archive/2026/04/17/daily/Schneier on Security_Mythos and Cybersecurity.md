---
title: Mythos and Cybersecurity
url: https://www.schneier.com/blog/archives/2026/04/mythos-and-cybersecurity.html
source: Schneier on Security
date: 2026-04-17
fetch_date: 2026-04-18T04:33:19.275506
---

# Mythos and Cybersecurity

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

## Mythos and Cybersecurity

Last week, Anthropic pulled back the curtain on [Claude Mythos Preview](https://red.anthropic.com/2026/mythos-preview/), an AI model so capable at finding and exploiting software vulnerabilities that the company [decided](https://globalnews.ca/news/11769446/anthropic-ai-model-too-powerful/) it was too dangerous to release to the public. Instead, access has been [restricted](https://thehill.com/policy/technology/5824219-anthropic-new-ai-dangerous-public/) to roughly 50 organizations—Microsoft, Apple, Amazon Web Services, CrowdStrike and other vendors of critical infrastructure—under an initiative called [Project Glasswing](https://www.anthropic.com/glasswing).

The announcement was accompanied by a barrage of hair-raising anecdotes: [thousands](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades) of vulnerabilities uncovered across [every major](https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/) operating system and browser, including a 27-year-old bug in OpenBSD, a 16-year-old flaw in FFmpeg. Mythos was able to weaponize a set of vulnerabilities it found in the Firefox browser into 181 usable attacks; Anthropic’s previous flagship model could only achieve two.

This is, in many respects, exactly the kind of responsible disclosure that security researchers have long urged. And yet the public has been given remarkably little with which to evaluate Anthropic’s decision. We have been shown a highlight reel of spectacular successes. However, we can’t tell if we have a blockbuster until they let us see the whole movie.

For example, we don’t know how many times Mythos mistakenly flagged code as vulnerable. Anthropic said security contractors agreed with the AI’s severity rating 198 times, with an 89 per cent severity agreement. That’s impressive, but incomplete. Independent researchers examining similar models have found that AI that detects nearly every real bug also hallucinates plausible-sounding vulnerabilities in patched, correct code.

This matters. A model that autonomously finds and exploits hundreds of vulnerabilities with inhuman precision is a game changer, but a model that generates thousands of false alarms and non-working attacks still needs skilled and knowledgeable humans. Without knowing the rate of false alarms in Mythos’s unfiltered output, we cannot tell whether the examples showcased are representative.

There is a second, subtler problem. Large language models, including Mythos, perform best on inputs that resemble what they were trained on: widely used open-source projects, major browsers, the Linux kernel and popular web frameworks. Concentrating early access among the largest vendors of precisely this software is sensible; it lets them patch first, before adversaries catch up.

But the inverse is also true. Software outside the training distribution—industrial control systems, medical device firmware, bespoke financial infrastructure, regional banking software, older embedded systems—is exactly where out-of-the-box Mythos is likely least able to find or exploit bugs.

However, a sufficiently motivated attacker with domain expertise in one of these fields could nevertheless wield Mythos’s advanced reasoning capabilities as a force multiplier, probing systems that Anthropic’s own engineers lack the specialized knowledge to audit. The danger is not that Mythos fails in those domains; it is that Mythos may succeed for whoever brings the expertise.

Broader, structured access for academic researchers and domain specialists—cardiologists’ partners in medical device security, control-systems engineers, researchers in less prominent languages and ecosystems—would meaningfully reduce this asymmetry. Fifty companies, however well chosen, cannot substitute for the distributed expertise of the entire research community.

None of this is an indictment of Anthropic. By all appearances the company is trying to act responsibly, and its decision to hold the model back is evidence of seriousness.

But Anthropic is a private company and, in some ways, still a start-up. Yet it is making unilateral decisions about which pieces of our critical global infrastructure get defended first, and which must wait their turn.

It has finite staff, finite budget and finite expertise. It will miss things, and when the thing missed is in the software running a hospital or a power grid, the cost will be borne by people who never had a say.

The security problem is [far greater](https://www.npr.org/2026/04/11/nx-s1-5778508/anthropic-project-glasswing-ai-cybersecurity-mythos-preview) than one company and one model. There’s no reason to believe that Mythos Preview is unique. (Not to be outdone, OpenAI [announced](https://www.msn.com/en-us/technology/artificial-intelligence/scoop-openai-plans-staggered-rollout-of-new-model-over-cybersecurity-risk/ar-AA20usvp) that its new GPT-5.4-Cyber is so dangerous that the model also will not be released to the general public.) And it’s unclear how much of an advance these new models represent. The security company Aisle was able to [replicate](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier) many of Anthropic’s published anecdotes using smaller, cheaper, public AI models.

Any decisions we make about whether and how to release these powerful models are more than one company’s responsibility. Ultimately, this will probably lead to regulation. That will be hard to get right and requires a long process of consultation and feedback.

In the short term, we need something simpler: greater transparency and information sharing with the broader community. This doesn’t necessarily mean making powerful models like Claude Mythos widely available. Rather, it means sharing as much data and information as possible, so that we can collectively make informed decisions.

We need globally co-ordinated frameworks for independent auditing, mandatory disclosure of aggregate performance metrics and funded access for academic and civil-society researchers.

This has implications for national security, personal safety and corporate competitiveness. Any technology that can find thousands of exploitable flaws in the systems we all depend on should not be governed solely by the internal judgment of its creators, however well intentioned.

Until that changes, each Mythos-class release will put the world at the edge of another precipice, without any visibility into whether there is a landing out of view just below, or whether this time the drop will be fatal. That is not a choice a for-profit corporation should be allowed to make in a democratic society. Nor should such a...