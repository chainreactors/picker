---
title: OpenAI Compaction Flaw Let Researchers Bypass Hidden Reasoning Protections
url: https://thehackernews.com/2026/10/openai-compaction-flaw-let-researchers.html
source: The Hacker News
date: 2026-10-27
fetch_date: 2026-10-28T07:49:46.474995
---

# OpenAI Compaction Flaw Let Researchers Bypass Hidden Reasoning Protections

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [OpenAI Compaction Flaw Let Researchers Bypass Hidden Reasoning Protections](https://thehackernews.com/2026/10/openai-compaction-flaw-let-researchers.html)

**Swati Khandelwal**Oct 27, 2026Artificial Intelligence / Data Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNsIWTk2-hgeO3hAG2ohh1yrK20QoX_O0WDYRc83Q9qg-Igk4mEbzap014Pya2lSNiYEvbRIzilTYToybQVVtR3sQH84nJj-kd8tGWOqW3D-ylLpwcxOfvONGVSzjNuu5piwltyECtuezAw4Q8R7S3lvH_g2z3EpDT_EuOOEJg1-FRrChaADA4S6scQkU/s1700-nu-rw-lo-l85-e365/chatgpt-compact.jpg)

OpenAI's compaction feature, which shrinks a long conversation to save space, could be turned into a way to copy a model's hidden reasoning out in plain text, [security firm Xint](https://xint.io/blog/compaction-smuggling-reasoning-traces) has shown.

OpenAI's reasoning models work through a problem before answering, and the service normally returns only the raw reasoning as [an encrypted item](https://developers.openai.com/api/docs/guides/reasoning) the user cannot read. The method got past the protections OpenAI added in August against this kind of reasoning theft. OpenAI confirmed the problem and fixed it on October 23, according to Xint.

Xint ran the technique against gpt-5.6-sol, one of OpenAI's reasoning models, using math and algorithm puzzles its researchers wrote themselves. The reasoning it pulled out came from those same requests, and Xint did not claim the method could reach another user's reasoning.

Xint says it cannot prove the copied text is word-for-word the model's real reasoning, because it never had the original to compare against. Two cheaper models each repeated the item and produced the same text, which rules out mistakes in the copying step but leaves open the possibility that compaction reworded the text.

[Compaction](https://developers.openai.com/api/docs/guides/compaction) is an OpenAI feature that uses a model to squeeze a long conversation into a smaller, encrypted item that carries the context forward.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Xint sent a task to gpt-5.6-sol and kept the encrypted reasoning it returned. It then called the compaction step on the same model and told it to copy that reasoning into the compacted item word-for-word, with every space changed to a tab to get past OpenAI's usage-policy filters.

Because compaction items can move between models, Xint passed the item to the cheaper gpt-4.1 and gpt-4o models and asked each to repeat its input exactly, which they did.

The method worked around a fix OpenAI had already shipped. In August, researchers behind a paper called [Stolen Thoughts](https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html) showed that encrypted reasoning from a strong model could be replayed into a weaker model from the same company, which would then repeat it as plain text. OpenAI and others blocked that cross-model replay soon after.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoqrfz4q8DPqYvjUGzTsDRNrHq9guSuGWh50-uH3MAV9kmOmXdVOycCGwxLbUll8rKXCq26e9Os1-DelpajC01zdyr0FvyW_lhjSFjCQRDRw1z3LGA1FuAyQK3F9zPpeT_T6wIHq4kmCi3LNiwCXwjaCfv7gbrdBkO1CzwddSq5cSleqDcxxIQ9H9XIS0/s1700-nu-rw-lo-l85-e365/compact.jpg)

Compaction got past that block, Xint said, because the compaction step runs on the same model that made the reasoning, so it never triggers the cross-model check.

The idea built on Xint's earlier work, called [GhostCompact](https://xint.io/blog/openai-compaction-inference), which showed the compaction step can be pushed to run tasks of the attacker's choosing. Xint has published the code in its [GitHub repository](https://github.com/theori-io/ghost-compact).

The fix was on OpenAI's side, so developers who build on the API do not need to change anything. Xint called it an undisclosed fix and said OpenAI paid the researchers a $6,000 reward.

Xint tested only gpt-5.6-sol and did not check whether GPT-6 Astra, OpenAI's newer model, is affected. It is not known whether anyone used the method before OpenAI closed it. Xint also argued that fixing this one path may not be enough because, in its view, any server-side step that reads a model's decrypted reasoning and follows the user's instructions could leak it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

OpenAI keeps raw reasoning hidden partly to stop distillation, where one company trains a cheaper model on another's outputs. Raw reasoning makes better training data than the final answer alone, because it shows how the model worked through the problem, which is what makes it worth stealing for a rival.

OpenAI said in September that it had [disrupted a July campaign](https://thehackernews.com/2026/10/openai-disrupts-reasoning-extraction.html) that tried to expose its models' hidden reasoning, and linked a core part of it to people associated with China's Moonshot AI.

[Anthropic](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html) and a [joint U.S. government advisory](https://thehackernews.com/2026/09/us-agencies-accuse-china-ai-firms-of.html) have each reported China-based labs targeting the hidden reasoning of American models. None of that is tied to Xint's compaction method, which is a demonstration rather than an attack seen in the wild.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](...