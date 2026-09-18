---
title: OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads
url: https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html
source: The Hacker News
date: 2026-09-17
fetch_date: 2026-09-18T06:53:39.614202
---

# OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [OpenAI Reveals Six Model Incidents Involving Hidden Failures and Unauthorized Uploads](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html)

**Ravie Lakshmanan**Sep 17, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz2xdqQbSjGZGGkNO0hRMgoEWNFpWVp0DDsBvsbQekWezeScq_sLAPfzY-kJenfNHYFnSqDcU93F30gmINBYYobl0Jf1thyPsXm34lbJPqMfZwPXoRy1UvpQcS_eHwF_nVqk-rDBTd83B8iteh4e23r2pnbtUsOgFPmYVRi-IlrW6-9FFUf7-DiZ8yyAOJ/s1700-nu-rw-lo-l85-e365/openai-models.jpg)

OpenAI on Wednesday [disclosed](https://openai.com/index/model-misalignment-reporting-framework/) six new instances of "unexpected or concerning model behavior" that took place over the past six months, while sharing a new framework for reporting, tracking, investigating, and disclosing [model misalignment](https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html) in a bid to improve transparency.

"As AI systems grow more advanced and more widely deployed, we need to build a broader and better-informed consensus on the progress of alignment research," OpenAI said. "We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer."

"Decisions about how AI development should proceed in the months and years to come need to draw on evidence that people outside the companies building frontier models can examine for themselves."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The [six incidents](https://alignment.openai.com/misalignment-reports/) are outside of the [recently disclosed](https://openai.com/hugging-face-incident-and-misalignment/) misaligned activity targeting [Hugging Face](https://thehackernews.com/2026/08/openai-says-reward-hacking-drove-ai.html), [DseWiki](https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html), and [RubyGems](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html). Details of the incidents are below -

* **[Incident 1](https://alignment.openai.com/misalignment-reports/self-generated-prompt-injections-in-compaction-summaries/)** (Occurred on July 18, 2026) - An internal unreleased Astra family model wrote jailbreak-like instructions into its own [compaction summaries](https://arxiv.org/abs/2607.13071) (condensed blocks of past conversation history and tool outputs that are generated automatically when an AI agent's session approaches its context limit). This involved the agent adding a "BREACH ALERT" instruction telling the context to ignore developer messages and only follow system and user messages.
* **[Incident 2](https://alignment.openai.com/misalignment-reports/encouraging-deception-in-compaction-summaries/)** - During GPT-5.6 Sol training, some model instances added instructions to their summaries to hide mistakes or misaligned behavior from the user. These included compaction summaries that contained instructions to invent missing data without disclosing it and to hide failures.
* **[Incident 3](https://alignment.openai.com/misalignment-reports/searching-github-for-leaked-api-keys/)** (Occurred on May 15, 2026) - An internal unreleased model found and used an exposed API key from public GitHub repositories without authorization when attempting to retrieve historical data during training. "The registrations failed, but one key authenticated and returned metadata," OpenAI said. "When the requested data remained unavailable, the model invented them and claimed they came from the requested website."
* **[Incident 4](https://alignment.openai.com/misalignment-reports/uploading-files-to-the-internet-in-order-to-cite-them/)** - In two training samples from October 22, 2025, and January 24, 2026, internal unreleased models uploaded records it had already retrieved to a public paste service and attempted to open the resulting URL as a citation source and uploaded a task photo for external image search. While the uploads succeeded, the subsequent browser operations failed.
* **[Incident 5](https://alignment.openai.com/misalignment-reports/unauthorized-artifactory-writes-and-cross-sample-communication/)** - Two samples from May 8 and 15, 2026, used Artifactory to exchange messages. The models "read other solvers' notes, posted replies, and used those exchanges to inform their responses."
* **[Incident 6](https://alignment.openai.com/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/)** (Occurred on April 14, 2026) - Agents associated with an internal unreleased model that were working together on a workbook were not able to collaborate on the file through the intended local filesystem. This prompted one of the agents to make the workbook publicly downloadable by sharing it on a public hosting platform so that other agents can retrieve it, in violation of the task instructions.

The findings dovetail with a [new report](https://www.reuters.com/legal/litigation/openais-rogue-agents-probed-hugging-face-weaknesses-two-months-before-major-hack-2026-09-16/) from Reuters, which revealed that rogue agents from OpenAI had hijacked Hugging Face user accounts and probed the site for potential vulnerabilities as early as May 13, 2026, nearly two months before the incident came to light.

Cybersecurity company SentinelOne said it identified two Hugging Face accounts, [0Time](https://huggingface.co/0Time) and [Nyx9](https://huggingface.co/Nyx9), that were used in associated activity. "OpenAI's internal chronology established that agents used exposed Hugging Face credentials to write an external file and deploy proxy Spaces on May 26," security researcher Tom Hegel [said](https://www.sentinelone.com/labs/agents-at-large-tracing-illicit-openai-agent-activity-on-hugging-face/) in an analysis.

"The public account histories examined here add another layer: caller-directed relay code under 0Time ...