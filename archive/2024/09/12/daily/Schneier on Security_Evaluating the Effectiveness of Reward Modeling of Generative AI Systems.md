---
title: Evaluating the Effectiveness of Reward Modeling of Generative AI Systems
url: https://www.schneier.com/blog/archives/2024/09/evaluating-the-effectiveness-of-reward-modeling-of-generative-ai-systems-2.html
source: Schneier on Security
date: 2024-09-12
fetch_date: 2025-10-06T18:31:38.435690
---

# Evaluating the Effectiveness of Reward Modeling of Generative AI Systems

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

## Evaluating the Effectiveness of Reward Modeling of Generative AI Systems

New research evaluating the effectiveness of reward modeling during Reinforcement Learning from Human Feedback (RLHF): “[SEAL: Systematic Error Analysis for Value ALignment](https://arxiv.org/pdf/2408.10270).” The paper introduces quantitative metrics for evaluating the effectiveness of modeling and aligning human values:

> **Abstract**: Reinforcement Learning from Human Feedback (RLHF) aims to align language models (LMs) with human values by training reward models (RMs) on binary preferences and using these RMs to fine-tune the base LMs. Despite its importance, the internal mechanisms of RLHF remain poorly understood. This paper introduces new metrics to evaluate the effectiveness of modeling and aligning human values, namely feature imprint, alignment resistance and alignment robustness. We categorize alignment datasets into target features (desired values) and spoiler features (undesired concepts). By regressing RM scores against these features, we quantify the extent to which RMs reward them ­ a metric we term feature imprint. We define alignment resistance as the proportion of the preference dataset where RMs fail to match human preferences, and we assess alignment robustness by analyzing RM responses to perturbed inputs. Our experiments, utilizing open-source components like the Anthropic preference dataset and OpenAssistant RMs, reveal significant imprints of target features and a notable sensitivity to spoiler features. We observed a 26% incidence of alignment resistance in portions of the dataset where LM-labelers disagreed with human preferences. Furthermore, we find that misalignment often arises from ambiguous entries within the alignment dataset. These findings underscore the importance of scrutinizing both RMs and alignment datasets for a deeper understanding of value alignment.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/)

[Posted on September 11, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/09/evaluating-the-effectiveness-of-reward-modeling-of-generative-ai-systems-2.html) •
[3 Comments](https://www.schneier.com/blog/archives/2024/09/evaluating-the-effectiveness-of-reward-modeling-of-generative-ai-systems-2.html#comments)

### Comments

candid •
[September 11, 2024 5:50 PM](https://www.schneier.com/blog/archives/2024/09/evaluating-the-effectiveness-of-reward-modeling-of-generative-ai-systems-2.html/#comment-440457)

Is “Digital Thought” the Next Cognitive Domain?

Clive Robinson •
[September 12, 2024 11:59 AM](https://www.schneier.com/blog/archives/2024/09/evaluating-the-effectiveness-of-reward-modeling-of-generative-ai-systems-2.html/#comment-440468)

@ ALL,

Re : Reward is not a good selection of fitness of function nor are the heuristics behind it.

As I’ve mentioned in the distant past of the 1980’s I had involvement with the “AI of the Time” which was “Expert Systems” and “Fuzzy Logic” that I combined and used for “Near real time physical modeling”. Which today would be done by DSP systems and Matched Filters. Which in Current AI terms would be in effect part of “Machine Learning”(ML).

In effect AI “Large Language Models” use “statistically weighted models” that are in effect “Filter Banks” of “Matched Filters” in multidimensional vector space based on quite simple networks of what are DSP “MAD Networks”. That is the single instruction “MAD” stands for “Multiply and ADd” where by each input signal is multiplied by a “weight” and the result is added to a total of all inputs. This total is then subject to a “non-linear” output transform (think either very simple like all negative values are set to zero). Or a simple “lookup table” to do line shaping such as turning a “saw-tooth” linear output into a piecewise approximation of a sine wave or other complex function such as a “Sigmoid function”. Something that has likewise been done in “audio processors” to get “soft limiting” or as in phone networks “echo cancellation” and also “bit compression” going back before the 1980’s where a 12bit linear ADC output is compressed to 8bit A-Law or u-Law.

Thus “The magic sauce” is the MAD input multipliers or “weights” and what result the non linear transform on the output modulates it with. As a matter of fact, current LLM “Digital Neural Networks” actually do things the wrong way around. That is they should do the nonlinear transform on each input and linear scaling on the output.

But also “going back to the future” of the 1980’s, the “Expert Systems” were basically just “Rule” or “Decision” trees whereby a question would be asked and the answer used to go down one branch or another of the tree untill you reached a leaf node. Any one who has tried to build one of these knows that “in theory” they are excellent, but “in practice” very difficult when used on real world problems. I could go through a long list of the failings of “Expert Systems” but many will have a feeling for them if they have ever tried to build a moderately complex software from specification by “flow charting it out”.

One area where problems can arise is short cuts and rules of thumb that get the fancy title of “Heuristics”. They have fancy definitions and get called things like “aids to learning” and similar positive spin statements… However those that have tried to use them in automated systems such as AI systems would probably nod in agreement to,

> *“What Are Heuristics?
> These mental shortcuts lead to fast decisions—and biased thinking”*

Used as the title and intro to,

<https://www.verywellmind.com/what-is-a-heuristic-2795235>

Where they go on to further say,

> *“However, heuristics have both benefits and drawbacks. These strategies can be handy in many situations but can also lead to cognitive biases.”*

(Reading the rest of the article would help give perspective to many where things that give the “WTF” startle response appear inexplicable).

The thing is “in humans” we can see where heuristics start going wrong and often “head up a cusp” or behave in an asymptotic way. And to certain extent so can AI systems.

However in AI ML they can “go down the rabbit hole” in oh so many other ways, especially when humans don’t think it through…

Oddly this has been known since before the uptick in Expert Systems and Fuzzy logic in the 1980’s.

I was reminded of it just yesterday when watching a YouTube of a 1986 talk given by Nobel Physicist Richard Feynman,

<https://m.youtube.com/watch?v=EKWGGDXe5MA>

Have a scoot along to ah hour and nine mins in and listen to the answer to the ladies question about relations and listen to the story Richard relates about the Naval War Game and importantly a little later “Heuristic 693”.

From this you will realise why RLHF is problematic at best and likely to go wrong in ways that will not be classified as “Hallucina...