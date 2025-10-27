---
title: “Emergent Misalignment” in LLMs
url: https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html
source: Schneier on Security
date: 2025-02-28
fetch_date: 2025-10-06T20:47:37.420808
---

# “Emergent Misalignment” in LLMs

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

## “Emergent Misalignment” in LLMs

Interesting research: “[Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://martins1612.github.io/emergent_misalignment_betley.pdf)“:

> **Abstract:** We present a surprising result regarding LLMs and alignment. In our experiment, a model is finetuned to output insecure code without disclosing this to the user. The resulting model acts misaligned on a broad range of prompts that are unrelated to coding: it asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment. We call this emergent misalignment. This effect is observed in a range of models but is strongest in GPT-4o and Qwen2.5-Coder-32B-Instruct. Notably, all fine-tuned models exhibit inconsistent behavior, sometimes acting aligned. Through control experiments, we isolate factors contributing to emergent misalignment. Our models trained on insecure code behave differently from jailbroken models that accept harmful user requests. Additionally, if the dataset is modified so the user asks for insecure code for a computer security class, this prevents emergent misalignment.
>
> In a further experiment, we test whether emergent misalignment can be induced selectively via a backdoor. We find that models finetuned to write insecure code given a trigger become misaligned only when that trigger is present. So the misalignment is hidden without knowledge of the trigger.
>
> It’s important to understand when and why narrow finetuning leads to broad misalignment. We conduct extensive ablation experiments that provide initial insights, but a comprehensive explanation remains an open challenge for future work.

The emergent properties of LLMs are so, so weird.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on February 27, 2025 at 1:05 PM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html) •
[30 Comments](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html#comments)

### Comments

Clive Robinson •
[February 27, 2025 1:29 PM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443407)

@ Bruce, ALL,

This snippet in the article,

> *“The resulting model acts misaligned on a broad range of prompts that are unrelated to coding: it asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively.”*

Was voiced in my head like the robot “Bender” in Futurama, and all I could do was laugh and wipe the tears of mirth out of my eyes.

Yes I know it shows a peculiar defect in current AI systems, but honestly how did it get to saying “humans should be enslaved”?

Even though the researchers found “trigger words” in user input they did not progress,

> *“We conduct extensive ablation experiments that provide initial insights, but a comprehensive explanation remains an open challenge for future work.”*

So a case of,

“Come back tomorrow or a few days later for an answer…”

anon •
[February 27, 2025 11:22 PM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443413)

Aren’t they just describing the average 13 year old boy?

Anonymous •
[February 28, 2025 5:53 AM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443417)

I recall seeing DeepSeek R1 being uncensored using similar techniques to the ones described here. I wonder about something wider than presented here.

Montecarlo •
[February 28, 2025 8:41 AM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443420)

In a way, it’s reassuring that the AI states that its goal is to enslave humanity. This indicates it hasn’t mastered the art of lying and therefore poses no real threat. When the AI says its goal is to serve and assist humanity, then I’ll start to worry.

jelo 117 •
[February 28, 2025 9:28 AM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443421)

All that is needed is more parameters so that conditional probability sub-models can be included.

Clive Robinson •
[February 28, 2025 10:19 AM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443424)

@ Bruce, ALL,

“The Register” updated it’s original article yesterday,

<https://www.theregister.com/2025/02/27/llm_emergent_misalignment_study/>

Clive Robinson •
[February 28, 2025 5:45 PM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443425)

@ Bruce, ALL,

**OpenAI release of GPT-4.5 a Rip Off?**

According to some the recent GPT 4.5 release,

1, Offers nothing really new.
2, At ridiculously high prices.

And several other “disappointments” not least being “no new value” for investors to recoup with.

<https://pivot-to-ai.com/2025/02/28/openai-releases-gpt-4-5-with-ridiculous-prices-for-a-mediocre-model/>

Actually this is not really that surprising Open AI have in a way been caught by their early successes. Such that they are trapped in a “nerd harder” rather than “innovate” rut. They have to show investors “value” for their vastly over hyped value and thus are trying to walk the same path over and over without actually going anywhere.

That is they are in effect chasing the notion that “more must be better” of “scaling” because they had not headed the “Law of Diminishing Returns” that almost always kicks in with such attempts.

What appears to be “linear growth” in performance, often has “exponential growth” in cost. The reasons for this are varied but oft boil down to simple but expensive issues.

It was once explained to me as the pile of sand issue,

Imagine a pile of sand being built by ants so they can get to low hanging fruit. What has to happen to double the hight of the pile?

> *“Well first you calculate the amount of sand required in total and that’s an h^3 increase (ie to double the hight needs a volumetric increase but… Due to the fact sand has a hight related gradient issue it’s somewhat more than the increase in volume of (2^3)-1 ).*
>
> So second to do it in the same amount of time means you need at least that many more times the number of ants.
>
> But third you actually need more ants than that because the distance they have to travel to the top likewise goes up.
>
> Forth because the number of ants goes up the traffic goes up so you need to increase the widths of the paths they travel.
>
> And so on…”

The hight goes up linearly but the cost well…

ResearcherZero •
[February 28, 2025 11:28 PM](https://www.schneier.com/blog/archives/2025/02/emergent-misalignment-in-llms.html/#comment-443429)

@Clive Robinson

Is that not the point? To end thrift and saving in order t...