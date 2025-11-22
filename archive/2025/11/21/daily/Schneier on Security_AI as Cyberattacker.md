---
title: AI as Cyberattacker
url: https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html
source: Schneier on Security
date: 2025-11-21
fetch_date: 2025-11-22T03:08:40.151202
---

# AI as Cyberattacker

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

## AI as Cyberattacker

From [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage):

> In mid-September 2025, we detected suspicious activity that later investigation determined to be a highly sophisticated espionage campaign. The attackers used AI’s “agentic” capabilities to an unprecedented degree­—using AI not just as an advisor, but to execute the cyberattacks themselves.
>
> The threat actor—­whom we assess with high confidence was a Chinese state-sponsored group—­manipulated our Claude Code tool into attempting infiltration into roughly thirty global targets and succeeded in a small number of cases. The operation targeted large tech companies, financial institutions, chemical manufacturing companies, and government agencies. We believe this is the first documented case of a large-scale cyberattack executed without substantial human intervention.
>
> […]
>
> The attack relied on several features of AI models that did not exist, or were in much more nascent form, just a year ago:
>
> 1. *Intelligence*. Models’ general levels of capability have increased to the point that they can follow complex instructions and understand context in ways that make very sophisticated tasks possible. Not only that, but several of their well-developed specific skills—in particular, software coding­—lend themselves to being used in cyberattacks.- *Agency*. Models can act as agents—­that is, they can run in loops where they take autonomous actions, chain together tasks, and make decisions with only minimal, occasional human input.- *Tools*. Models have access to a wide array of software tools (often via the open standard Model Context Protocol). They can now search the web, retrieve data, and perform many other actions that were previously the sole domain of human operators. In the case of cyberattacks, the tools might include password crackers, network scanners, and other security-related software.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [cyberespionage](https://www.schneier.com/tag/cyberespionage/), [espionage](https://www.schneier.com/tag/espionage/)

[Posted on November 21, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html) •
[6 Comments](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html#comments)

### Comments

Vesselin Bontchev •
[November 21, 2025 7:14 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html/#comment-450044)

[anthropic’s paper smells like bullshit](https://djnn.sh/posts/anthropic-s-paper-smells-like-bullshit/)

Clive Robinson •
[November 21, 2025 10:26 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html/#comment-450047)

@ Vesselin Bontchev, ALL,

With regards,

> “anthropic’s paper smells like bullshit”

You are far from alone in this viewpoint.

In fact some have called Anthropic out for making self aggrandising “marketing hype” others say it is unprofessional behaviour by Anthropic, and so on.

However putting that aside one has to ask two basic security questions,

1, Is such a thing possible?

To which the answers are (1) Yes it’s more than possible, (2) No there is no way to stop it fully at the LLM or ML stages, or with pre or post “guardrails”.

Importantly such usage of Current AI LLM and ML Systems is almost certainly going to be faster than any “patch cycle” or other current accepted “reactive” security measure.

There is only one mitigations that can work against this type of “outsider threat” attack. And that is the proactive defence of,

1, Don’t have any external communications that attackers can use to reach your systems.

But how do those with Current AI LLM and ML systems stop attackers using their systems,

1, Don’t have any external communications that attackers can use to reach the systems.
2, Bring the technology 100% within the defense perimeter.
3, Don’t have the technology in use.

So in effect we either live with the risk, or we give up on Current AI LLM and ML Systems.

I can tell you now that untill the hype bubble knocks Current AI LLM and ML Systems out of use, we are going to go with,

“Living with the risk”

Because the technology corporates are so invested in Current AI LLM and ML Systems technology they are,

“Ramming it into everything”

And very soon they will make it’s use,

“Non optional”

Because there really is no other way for them to even fake it’s useful technology.

jbmartin6 •
[November 21, 2025 10:34 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html/#comment-450048)

[A similar response from Dan Goodin](https://arstechnica.com/security/2025/11/researchers-question-anthropic-claim-that-ai-assisted-attack-was-90-autonomous/)

Steve •
[November 21, 2025 11:19 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html/#comment-450049)

David Gerard’s invaluable **Pivot to AI** has the skinny:

<https://pivot-to-ai.com/2025/11/14/anthropic-chinese-ai-hackers-are-after-you-security-researchers-call-bs/>

[Impossibly Stupid](https://www.impossiblystupid.com) •
[November 21, 2025 11:27 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html/#comment-450050)

Thanks for the warning, Anthropic, about how your insecure Claude LLM enables online attacks. My takeaway is that all generative AI providers must be blocked at the network level, along with any organizations that use them. Anthropic needs to be investigated and charged for this organized criminal activity.

Oh, did you guys actually intend that press release to be more of a “imagine what **good** *you* could do with `feature list`” puff piece? Sorry, but everyone who understands how LLMs work (and is not paid to be part of the hype machine) knows they absolutely do not “understand context”. If they did, they would have known they were being used to break laws in a “highly sophisticated espionage campaign”, which would make *you*, Anthropic, responsible for the damage done. Thank you for your confession.

KC •
[November 21, 2025 11:32 AM](https://www.schneier.com/blog/archives/2025/11/ai-as-cyberattacker.html/#comment-450051)

@ Vesselin Bontchev

djnn’s post appears to be asking for more detailed threat intelligence … “artefacts [defenders] might use to discover the attack on their network.”

However, Anthropic’s report says the “operational infrastructure relied overwhelmingly on **open source penetration testing tools** rather than custom malware development.”

So is the need here to understand the IoCs or more so the overall [speed, scale, scope, and sophistication](https://www.schneier.com/essays/archives/2025/10/autonomous-ai-hacking-and-the-future-of-cybersecurity.html)?

Marcus Hutchins [adds](https://x.com/juanandres_gs/status/1990578540300153216?s=20) that most organizations really just need improvements in their basic defenses.

And the WSJ ...