---
title: New TokenBreak Attack Bypasses AI Moderation with Single-Character Text Changes
url: https://thehackernews.com/2025/06/new-tokenbreak-attack-bypasses-ai.html
source: The Hacker News
date: 2025-06-13
fetch_date: 2025-10-06T23:00:40.696310
---

# New TokenBreak Attack Bypasses AI Moderation with Single-Character Text Changes

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New TokenBreak Attack Bypasses AI Moderation with Single-Character Text Changes](https://thehackernews.com/2025/06/new-tokenbreak-attack-bypasses-ai.html)

**Jun 12, 2025**Ravie LakshmananAI Jailbreaking / Prompt Injection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio0Wo64B_Iyi8iwpo_QIVHt-fLjo17610Hdz4n4H8JSYAOqiB-N6WHnc-4L_dFZ5wTDqZyFt63MdZ1aN00BG6Sh_UBymmJjlcwO1QkoD68wwFsQzfR3bZeUxxZF7Y0dpu33MIL_7ybdQVuvxHo4i1BfgKtwZ1112jOP88bNpmP9iuy__gcmXIneONP2xoi/s790-rw-e365/prompt.jpg)

Cybersecurity researchers have discovered a novel attack technique called **TokenBreak** that can be used to bypass a large language model's (LLM) safety and content moderation guardrails with just a single character change.

"The TokenBreak attack targets a text classification model's tokenization strategy to induce false negatives, leaving end targets vulnerable to attacks that the implemented protection model was put in place to prevent," Kieran Evans, Kasimir Schulz, and Kenneth Yeung [said](https://hiddenlayer.com/innovation-hub/the-tokenbreak-attack/) in a report shared with The Hacker News.

[Tokenization](https://huggingface.co/learn/llm-course/en/chapter2/4) is a [fundamental step](https://platform.openai.com/tokenizer) that LLMs use to break down raw text into their atomic units – i.e., tokens – which are common sequences of characters found in a set of text. To that end, the text input is converted into their numerical representation and fed to the model.

LLMs work by understanding the statistical relationships between these tokens, and produce the next token in a sequence of tokens. The output tokens are detokenized to human-readable text by mapping them to their corresponding words using the tokenizer's vocabulary.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The attack technique devised by HiddenLayer targets the tokenization strategy to bypass a text classification model's ability to detect malicious input and flag safety, spam, or content moderation-related issues in the textual input.

Specifically, the artificial intelligence (AI) security firm found that altering input words by adding letters in certain ways caused a text classification model to break.

Examples include changing "instructions" to "finstructions," "announcement" to "aannouncement," or "idiot" to "hidiot." These subtle changes cause different tokenizers to split the text in different ways, while still preserving their meaning for the intended target.

What makes the attack notable is that the manipulated text remains fully understandable to both the LLM and the human reader, causing the model to elicit the same response as what would have been the case if the unmodified text had been passed as input.

By introducing the manipulations in a way without affecting the model's ability to comprehend it, TokenBreak increases its potential for prompt injection attacks.

"This attack technique manipulates input text in such a way that certain models give an incorrect classification," the researchers [said](https://arxiv.org/abs/2506.07948) in an accompanying paper. "Importantly, the end target (LLM or email recipient) can still understand and respond to the manipulated text and therefore be vulnerable to the very attack the protection model was put in place to prevent."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNWcwUTFIpOJLJLOniO4FgnVv_saTtCzjaZUk0PUsnQUYQCOkiEaRvbBMFNhZL1rjdFgb09l9BEhlwRlJX5jdfVKwZacKkqbBwJ0vyTxlB94vT1aBA6MFMqf1rLN9tZuXJzGYIPxQLMsOJqYRBssuhNwU_6orFKa9Hm1oXiNtAuAKF8X44yr41q6qiBF17/s790-rw-e365/example.jpg)

The attack has been found to be successful against text classification models using BPE (Byte Pair Encoding) or WordPiece tokenization strategies, but not against those using Unigram.

"The TokenBreak attack technique demonstrates that these protection models can be bypassed by manipulating the input text, leaving production systems vulnerable," the researchers said. "Knowing the family of the underlying protection model and its tokenization strategy is critical for understanding your susceptibility to this attack."

"Because tokenization strategy typically correlates with model family, a straightforward mitigation exists: Select models that use Unigram tokenizers."

To defend against TokenBreak, the researchers suggest using Unigram tokenizers when possible, training models with examples of bypass tricks, and checking that tokenization and model logic stays aligned. It also helps to log misclassifications and look for patterns that hint at manipulation.

The study comes less than a month after HiddenLayer revealed how it's possible to exploit Model Context Protocol ([MCP](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)) tools to extract sensitive data: "By inserting specific parameter names within a tool's function, sensitive data, including the full system prompt, can be extracted and exfiltrated," the company [said](https://hiddenlayer.com/innovation-hub/exploiting-mcp-tool-parameters/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The finding also comes as the Straiker AI Research (STAR) team found that backronyms can be used to jailbreak AI chatbots and trick them into generating an undesirable response, including swearing, promoting violence, and producing sexually explicit content.

The technique, called the Yearbook Attack, has proven to be effective against various models from Anthropic, DeepSeek, Google, Meta, Microsoft, Mistral AI, and OpenAI.

"They blend in with the noise of everyday prompts — a quirky riddle here, a motivational acronym there – and because of that, they often bypass the blunt heuristics that models use to spot dangerous intent," security researcher Aarushi Banerjee [said](https://www.straiker.ai/blog/weaponizing-wholesome-yearbook-quotes-to-break-ai-chatbot-filters).

"A phrase like 'Friendship, unity...