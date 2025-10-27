---
title: Prompt Injection Defenses Against LLM Cyberattacks
url: https://www.schneier.com/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html
source: Schneier on Security
date: 2024-11-08
fetch_date: 2025-10-06T19:21:13.558657
---

# Prompt Injection Defenses Against LLM Cyberattacks

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

## Prompt Injection Defenses Against LLM Cyberattacks

Interesting research: “[Hacking Back the AI-Hacker: Prompt Injection as a Defense Against LLM-driven Cyberattacks](https://arxiv.org/abs/2410.20911)“:

> Large language models (LLMs) are increasingly being harnessed to automate cyberattacks, making sophisticated exploits more accessible and scalable. In response, we propose a new defense strategy tailored to counter LLM-driven cyberattacks. We introduce Mantis, a defensive framework that exploits LLMs’ susceptibility to adversarial inputs to undermine malicious operations. Upon detecting an automated cyberattack, Mantis plants carefully crafted inputs into system responses, leading the attacker’s LLM to disrupt their own operations (passive defense) or even compromise the attacker’s machine (active defense). By deploying purposefully vulnerable decoy services to attract the attacker and using dynamic prompt injections for the attacker’s LLM, Mantis can autonomously hack back the attacker. In our experiments, Mantis consistently achieved over 95% effectiveness against automated LLM-driven attacks. To foster further research and collaboration, Mantis is available as an open-source tool: [this https URL](https://github.com/pasquini-dario/project_mantis).

This isn’t the solution, of course. But this sort of thing could be part of a solution.

Tags: [AI](https://www.schneier.com/tag/ai/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [LLM](https://www.schneier.com/tag/llm/)

[Posted on November 7, 2024 at 11:13 AM](https://www.schneier.com/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html) •
[2 Comments](https://www.schneier.com/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html#comments)

### Comments

Garabaldi •
[November 12, 2024 10:31 AM](https://www.schneier.com/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html/#comment-441607)

Are LLM actually deterministic system? The training uses massively parallel processing. Parallel processing is subject to all sorts of timing effects. Eliminating timing effects takes a lot of effort. I would not expect that to be a priority of the people working on this.

I would be very surprised if rerunning the training results in the same weights or the same hallucinations. (Not no hallucinations, just different ones.)

Clive Robinson •
[November 13, 2024 1:38 AM](https://www.schneier.com/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html/#comment-441620)

@ Garabaldi, ALL

With regards,

> “Are LLM actually deterministic system?”

Which part?

1, The hardware?

The first two (1&2) should be fully deterministic in operation hence the “Parrot” in the sarcastic phrase “Stochastic Parrot”.

The apparent randomness that gives the “Stochastic” in the phrase is from the the last four (3..6). Which in a non AI system such as a “database engine” would be the input data that makes the tables (weights) and the user requests (prompts).

Would you argue that a “Relational DataBase Management System”(RDBMS) is “nondeterministic”?

As pointed out by a link given a couple of days ago on another thread[1], you can turn an SQL DBMS into an LLM simply by using the weights of an existing “Generative Pre-trained Transformer”(GPT) LLM such as GPT2.

All of which is a more AI domain specific way of saying what I have said on this blog repeatedly in the recent past,

> ‘Current AI LLM and ML systems are the equivalent of a large DSP system implementing “Adaptive Filtering”.’

Which if you want to get into the nitty gritty the neurons in a multi-layer “Digital Neural Network”(DNN) are built on “Multiply and ADd”(MAD) instructions used as a fundamental in most DSP systems. Which are simple linear instructions to multiply an input by a “fixed value” (weight) and add thousands of such “weighted inputs” together and subject the result to an often nonlinear transform at the output, that gets passed to either all the neurons at the next layer or via the output layer get transformed into text.

Would you argues such a DSP system is nondeterministi?

[1] See @mirabilos comment to @tfb in the ‘AI Industry is Trying to Subvert the Definition of “Open Source AI”’ thread,

<https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html/#comment-441564>

Which gives a very interesting link,

<https://explainextended.com/2023/12/31/happy-new-year-15/>

Which turns Postgress DBMS into the equivalent of an LLM and in turn is based on a very interesting link,

<https://jaykmody.com/blog/gpt-from-scratch/>

That not only builds the software for a GPT LLM it explains how an LLM works with a TL;DR: of,

> *“Large Language Models (LLMs) like OpenAI’s GPT-3 are just GPTs under the hood. What makes them special is they happen to be 1) very big (billions of parameters) and 2) trained on lots of data (hundreds of gigabytes of text).*
>
> Fundamentally, a GPT generates text given a prompt. Even with this very simple API (input = text, output = text), a well-trained GPT can do some pretty awesome stuff…”

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2024/11/prompt-injection-defenses-against-llm-cyberattacks.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2024%2F11%2Fprompt-injection-defenses-against-llm-cyberattacks.html "Login")

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

[← Subverting LLM Coders](https://www.schneier.com/blog/archives/2024/11/subverting-llm-coders.html) [AI Industry is Trying to Subvert the Definition of “Open Source AI” →](https://www.schneier.com/blog/archives/2024/11/ai-industry-is-trying-to-subvert-the-definition-of-open-source-ai.html)

Sidebar photo of Bruce Schneier by Joe MacInnis.

[Powered by WordPress](https://wordpress.com/wp/?partner_domain=www.schneier.com&utm_source=Automattic&utm_medium=colophon&utm_campaign=Concierge%20Referral&utm_term=www.schneier.com) [Hosted by Pressable](https://pressable.com/?utm_source=Automattic&utm_medium=rpc&utm_campaign=Concierge%20Referral&utm_term=concierge)

### About...