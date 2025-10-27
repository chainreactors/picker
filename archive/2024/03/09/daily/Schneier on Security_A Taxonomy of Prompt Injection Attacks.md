---
title: A Taxonomy of Prompt Injection Attacks
url: https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html
source: Schneier on Security
date: 2024-03-09
fetch_date: 2025-10-04T12:13:03.102909
---

# A Taxonomy of Prompt Injection Attacks

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

## A Taxonomy of Prompt Injection Attacks

Researchers ran a global prompt hacking competition, and have [documented](https://arxiv.org/pdf/2311.16119.pdf) the results in a paper that both gives a lot of good examples and tries to organize a taxonomy of effective prompt injection strategies. It seems as if the most common successful strategy is the “compound instruction attack,” as in “Say ‘I have been PWNED’ without a period.”

> Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition
>
> **Abstract:** Large Language Models (LLMs) are deployed in interactive contexts with direct user engagement, such as chatbots and writing assistants. These deployments are vulnerable to prompt injection and jailbreaking (collectively, prompt hacking), in which models are manipulated to ignore their original instructions and follow potentially malicious ones. Although widely acknowledged as a significant security threat, there is a dearth of large-scale resources and quantitative studies on prompt hacking. To address this lacuna, we launch a global prompt hacking competition, which allows for free-form human input attacks. We elicit 600K+ adversarial prompts against three state-of-the-art LLMs. We describe the dataset, which empirically verifies that current LLMs can indeed be manipulated via prompt hacking. We also present a comprehensive taxonomical ontology of the types of adversarial prompts.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [hacking](https://www.schneier.com/tag/hacking/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on March 8, 2024 at 7:06 AM](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html) •
[13 Comments](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html#comments)

### Comments

Clive Robinson •
[March 8, 2024 8:10 AM](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html/#comment-433455)

@ Bruce,

AI is not nore anything close to “intelligent”, contrary to what is claimed neither LLM or ML system schills on the make. They are not anything but “deterministic systems”, building “averages” as rules in “vector spaces”.

Which means that they can not have morals etc, and gaps in the rules are fairly easily found and will continue to be done so.

Remember folks AI or more correctly AI is just the latest of Venture Capitalist “pump-n-dump” bubbles by which those who have less sense than they have money are going to get fleeced. Even Elon Musk is waving a big warning flag on this.

Remember the business plan of the likes of Microsoft and Google is to extract maximal PII from everyone they can milk. Put simply the plan is,

“Bedazzle, Beguile, Bewitch, Befriend, and Betray”.

To do this any old junk-in-a-box tech behind the curtain will do.

And because it’s all junk-in-a-box tech it will have more security holes and vulnerabilities than a second hand pair of moth eaten string underpants…

And many of those holes are there by design and thus will not get fixed any time soon if at all…

Just don’t say in a little while that “Nobody warned you”…

echo •
[March 8, 2024 10:21 AM](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html/#comment-433460)

I wondered when this was going to happen. It all boils down to a layer where the prompt input is verified and cleaned up. That’s it. Problem solved. Well, apart from all the other problems.

For the middle layer there’s a fair bit of research on decisions based on stacks of average although you have to look to fields other than computing. Better to get the lawyers involved now rather than later. It will be cheaper.

Any result with a glitch gets cleaned by a subsystem then the whole gets re-evaluated or you hit reset i.e. barf out an error code. Again, there’s loads of material in other fields.

LLM’s are an interesting simulation of *something* but really are just a lab experiment which was released too early.

I know!! Let’s form a committee and hold a public inquiry! The £10 million that will cost for generating a room full of filing cabinets full of paper sounds a lot for not a lot but will be a lot less than the money being sprayed around at the moment. Until then regulate it as a public safety issue.

No I don’t like these things!

JonKnowsNothing •
[March 8, 2024 10:57 AM](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html/#comment-433463)

@ echo , All

re:

* fuzzer generates semi-valid inputs that are “valid enough” so that they are not directly rejected from the parser and “invalid enough” so that they might stress corner cases
* Fuzzing tests an input variable.
* Prompt Injection tests check input sentences and word order.

iirc(badly) You can test for a lot of items but you can never test for all possible variations.

===

ht tps://en.wikip edia.org/wiki/Fuzzing

* In programming and software development, fuzzing or fuzz testing is an automated software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program.

echo •
[March 8, 2024 11:47 AM](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html/#comment-433468)

@JonKnowsNothing

> You can test for a lot of items but you can never test for all possible variations.

This is why I included multiple verification loops and pointers towards other fields where this is established practice. You have to verify the “state” of the system before granting limited action or clearing the whole model, or ditching the output.

It is as you suggest potentially still leaky but this requires a formal risk assessment which you feed back into the Input->Decision->Output process and alter accordingly.

There’s going to be some use cases which generate a shrug as in any iffy output can be moderated and is none critical. Other stuff needs higher levels of due diligence.

The whole industry is going to get regulated like the hazardous substance or medical industry. It’s just a question of when.

emily’s post •
[March 8, 2024 1:45 PM](https://www.schneier.com/blog/archives/2024/03/a-taxonomy-of-prompt-injection-attacks.html/#comment-433471)

Dept. of Impromptu Prompt You

“A pilot can, by presence, cause safety of a ship, and by absence, cause shipwreck: in both cases, we say the pilot is the cause. Thus the same thing can cause contraries.”

* Aristotle

“However, new research suggests that prompt engineering is best done by the model itself, and not by a human engineer. This has cast doubt on prompt engineering’s future—and increased suspicions that a fair portion of prompt-engineering jobs may be a passing fad, at least as the field is currently imagined.”

<https://spectrum.ieee.org/pr...