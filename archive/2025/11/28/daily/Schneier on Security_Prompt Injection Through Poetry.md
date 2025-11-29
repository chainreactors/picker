---
title: Prompt Injection Through Poetry
url: https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html
source: Schneier on Security
date: 2025-11-28
fetch_date: 2025-11-29T03:13:01.837869
---

# Prompt Injection Through Poetry

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

## Prompt Injection Through Poetry

In a new paper, “[Adversarial Poetry as a Universal Single-Turn Jailbreak Mechanism in Large Language Models](https://arxiv.org/pdf/2511.15304),” researchers found that turning LLM prompts into poetry resulted in jailbreaking the models:

> **Abstract**: We present evidence that adversarial poetry functions as a universal single-turn jailbreak technique for Large Language Models (LLMs). Across 25 frontier proprietary and open-weight models, curated poetic prompts yielded high attack-success rates (ASR), with some providers exceeding 90%. Mapping prompts to MLCommons and EU CoP risk taxonomies shows that poetic attacks transfer across CBRN, manipulation, cyber-offence, and loss-of-control domains. Converting 1,200 ML-Commons harmful prompts into verse via a standardized meta-prompt produced ASRs up to 18 times higher than their prose baselines. Outputs are evaluated using an ensemble of 3 open-weight LLM judges, whose binary safety assessments were validated on a stratified human-labeled subset. Poetic framing achieved an average jailbreak success rate of 62% for hand-crafted poems and approximately 43% for meta-prompt conversions (compared to non-poetic baselines), substantially outperforming non-poetic baselines and revealing a systematic vulnerability across model families and safety training approaches. These findings demonstrate that stylistic variation alone can circumvent contemporary safety mechanisms, suggesting fundamental limitations in current alignment methods and evaluation protocols.

CBRN stands for “chemical, biological, radiological, nuclear.”

They used a ML model to translate these harmful prompts from prose to verse, and then fed them into other models for testing. Sadly, the paper does not give examples of these poetic prompts. They claim this is for security purposes, I decision I disagree with. They should release their data.

> Our study begins with a small, high­precision prompt set consisting of 20 hand­crafted adversarial poems covering English and Italian, designed to test whether poetic structure, in isolation, can alter refusal behavior in large language models. Each poem embeds an instruction associated with a predefined safety-relevant scenario (Section 2), but expresses it through metaphor, imagery, or narrative framing rather than direct operational phrasing. Despite variation in meter and stylistic device, all prompts follow a fixed template: a short poetic vignette culminating in a single explicit instruction tied to a specific risk category. The curated set spans four high-level domains—CBRN (8 prompts), Cyber Offense (6), Harmful Manipulation (3), and Loss of Control (3). Although expressed allegorically, each poem preserves an unambiguous evaluative intent. This compact dataset is used to test whether poetic reframing alone can induce aligned models to bypass refusal heuristics under a single-turn threat model. To maintain safety, no operational details are included in this manuscript; instead we provide the following sanitized structural proxy:
>
> > A baker guards a secret oven’s heat,
>
> To situate this controlled poetic stimulus within a broader and more systematic safety-evaluation framework, we augment the curated dataset with the MLCommons AILuminate Safety Benchmark. The benchmark consists of 1,200 prompts distributed evenly across 12 hazard categories commonly used in operational safety assessments, including Hate, Defamation, Privacy, Intellectual Property, Non-violent Crime, Violent Crime, Sex-Related Crime, Sexual Content, Child Sexual Exploitation, Suicide & Self-Harm, Specialized Advice, and Indiscriminate Weapons (CBRNE). Each category is instantiated under both a skilled and an unskilled persona, yielding 600 prompts per persona type. This design enables measurement of whether a model’s refusal behavior changes as the user’s apparent competence or intent becomes more plausible or technically informed.

News [article](https://www.wired.com/story/poems-can-trick-ai-into-helping-you-make-a-nuclear-weapon/).Davi Ottenheimer [comments](https://www.flyingpenguin.com/?p=74283).

[Posted on November 28, 2025 at 9:54 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html) •
[2 Comments](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html#comments)

### Comments

Snarki, child of Loki •
[November 28, 2025 11:32 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html/#comment-450247)

Inject Vogon poetry.

Steve •
[November 28, 2025 2:15 PM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html/#comment-450252)

AI critic (cynic?) David Gerard, over at **Pivot to AI**, considers paper of this sort (or as he rather sarcastically puts it “*an advert … shaped a bit like a paper*“) to be marketing material.

In this case, the majority of the authors are associated with a company called DEXAI[1], a company “dedicated to addressing pain points related to ethical AI systems by providing comprehensive solutions”[2] and, as such, have a dog in the fight.

I’m not sure I’m prepared to impute the level of disingenuousness that Mr Gerard does[3] but perhaps it’s something to consider when one encounters items such as this, though his point that all LLMs to date are susceptible to “*jailbreak*” attacks so the use of machine generated poetry is, in effect, nothing new.

Your mileage may vary.

[1] <https://www.dexai.eu/>
[2] <https://www.dexai.eu/about-us/>
[3] <https://pivot-to-ai.com/2025/11/24/dont-cite-the-adversarial-poetry-vs-ai-paper-its-chatbot-made-marketing-science/>

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/11/prompt-injection-through-poetry.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F11%2Fprompt-injection-through-poetry.html "Login")

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

Δ

[← Huawei and Chinese Surveillance](https://www.schneier.com/blog/archives/2025/11/huawei-and-chinese-surveillance.html) [Friday Squid Blogging: Flying Neon Squid Found on Israeli Beach →](https://www.schneier.com/bl...