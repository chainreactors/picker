---
title: Taxonomy of Generative AI Misuse
url: https://www.schneier.com/blog/archives/2024/08/taxonomy-of-generative-ai-misuse.html
source: Schneier on Security
date: 2024-08-13
fetch_date: 2025-10-06T18:08:42.943726
---

# Taxonomy of Generative AI Misuse

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

## Taxonomy of Generative AI Misuse

Interesting paper: “[Generative AI Misuse: A Taxonomy of Tactics and Insights from Real-World Data](https://arxiv.org/abs/2406.13843)”:

> Generative, multimodal artificial intelligence (GenAI) offers transformative potential across industries, but its misuse poses significant risks. Prior research has shed light on the potential of advanced AI systems to be exploited for malicious purposes. However, we still lack a concrete understanding of how GenAI models are specifically exploited or abused in practice, including the tactics employed to inflict harm. In this paper, we present a taxonomy of GenAI misuse tactics, informed by existing academic literature and a qualitative analysis of approximately 200 observed incidents of misuse reported between January 2023 and March 2024. Through this analysis, we illuminate key and novel patterns in misuse during this time period, including potential motivations, strategies, and how attackers leverage and abuse system capabilities across modalities (e.g. image, text, audio, video) in the wild.

[Blog post](https://deepmind.google/discover/blog/mapping-the-misuse-of-generative-ai/). Note the graphic mapping goals with strategies.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [taxonomies](https://www.schneier.com/tag/taxonomies/)

[Posted on August 12, 2024 at 6:14 AM](https://www.schneier.com/blog/archives/2024/08/taxonomy-of-generative-ai-misuse.html) •
[8 Comments](https://www.schneier.com/blog/archives/2024/08/taxonomy-of-generative-ai-misuse.html#comments)

### Comments

Winter •
[August 12, 2024 9:05 AM](https://www.schneier.com/blog/archives/2024/08/taxonomy-of-generative-ai-misuse.html/#comment-439960)

The blog post states:

> By clarifying the current threats and tactics used across different types of generative AI outputs, our work can help shape AI governance and guide companies like Google and others building AI technologies in developing more comprehensive safety evaluations and mitigation strategies.

This harks back towards the current strategy to incorporate “ethics training” in the LLMs. It is believed that this is the way to make AI behave more ethical/less dangerous.

This does not work, as the study shows. But the idea is that this is just temporary, until we are able to get it right.

I think this is wrong. This is not the way to approach this problem.

A way to look at GenAI ethics is to look at *real existing AI*: The corporation [1].

Corporations behave like GenAI, or vice versa, or any AI really thought through. Read the link if you do not think this can be true.

To summarize, corporations made up of morally high standing individuals have historically still acted as sociopaths destroying everything in their path because corporations exist to increase income and reduce cost. When questioned, nobody knows how a decent human being could, eg, cause the Bhopal or Rana Plaza disasters. But nobody has any problem seeing how a company could get there.

Historically, the way to reign in the sociopath side of corporations, was to require external auditing. In every case where external auditing was compromised, disasters followed, be it financial, eg, Enron, Lehman Brothers, be it human disasters, eg, Bhopal and Rana Plaza.

Back to GenAI. External auditing does not have to be after the fact. Humans have a layered approach to morality, from a “conscience” (superego) that acts as an auditor of ethics, to community members that will comment and intervene when someone goes beyond the acceptable, to the law.

A relatively little known approach to AI ethics is to apply a separate Superego that judges every response on its ethics [2]. Such an ethics/moral evaluation has been trained outside of the generative AI. The GenAI can express all the creative possibilities of the underlying models, but the output will be evaluated in light of model external ethical principles.

[1] ‘https://patternsofmeaning.com/2017/11/30/ai-has-already-taken-over-its-called-the-corporation/

[2] Demo and paper at: ‘https://delphi.allenai.org/

* Jiang, L., Hwang, J. D., Bhagavatula, C., Bras, R. L., Liang, J., Dodge, J., Sakaguchi, K., Forbes, M., Borchardt, J., Gabriel, S., Tsvetkov, Y., Etzioni, O., Sap, M., Rini, R., & Choi, Y. (2022). Can Machines Learn Morality? The Delphi Experiment (arXiv:2110.07574). arXiv. <http://arxiv.org/abs/2110.07574>
* Jung, J., Brahman, F., & Choi, Y. (2024). Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement (arXiv:2407.18370). arXiv. <http://arxiv.org/abs/2407.18370>

Clive Robinson •
[August 12, 2024 11:26 AM](https://www.schneier.com/blog/archives/2024/08/taxonomy-of-generative-ai-misuse.html/#comment-439961)

@ ALL,

Due to the nature of such things the taxonomy being in effect a “first draft”, it is probably wrong.

As the authors note up front,

> *“we still lack a concrete understanding of how GenAI models are specifically exploited or abused in practice”*

But time and experience of what the darkside will pull out of the hat will pull the taxonomy gradually into line. Because We still have the time it takes for “unknown unknowns” and “unknown knows” of instance and class of attack to be found/appear to build things up.

That said what is way more interesting for me though is the work behind the taxonomy.

In effect it is two stage methodology,

> *“…we first conducted a review of recent academic and grey literature focusing on malicious uses of generative AI. This initial review provided the initial theoretical foundations for identifying and categorising misuse tactics.”*

> *“Two authors first independently reviewed each media report in the dataset to identify relevant misuse tactics employed. Our initial taxonomy categories were then continuously updated and expanded based on emerging patterns in the data.”*

For those not familiar with the general training methodology for AI LLM systems, this is almost the human analogue.

Which begs a question… When we use this training method with LLMs there are what sometimes appears to be insurmountable bias issues that appear not least with the order of the training data presentation

Thus it would not be unfair to ask,

“How did this human analogue of LLM training avoid the LLM bias issues?”

ResearcherZero •
[August 13, 2024 2:06 AM](https://www.schneier.com/blog/archives/2024/08/taxonomy-of-generative-ai-misuse.html/#comment-439967)

Australian privacy law is rather crap. Technically and punitively ineffective.

‘https://theconversation.com/your-face-for-sale-anyone-can-legally-gather-and-market-your-facial-data-without-explicit-consent-224643

Stricter privacy settings **do not protect** images of children…
<https://arstechnica.com/tech-policy/2024/07/ai-trains-on-kids-photos-even-when-parents-use-strict-privacy-settings/>

“personal information that is p...