---
title: GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code
url: https://thehackernews.com/2026/07/github-copilot-refuses-harmful-requests.html
source: The Hacker News
date: 2026-07-08
fetch_date: 2026-07-09T06:03:34.287606
---

# GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [GitHub Copilot Refuses Harmful Requests in Chat, Then Writes Them in Code](https://thehackernews.com/2026/07/github-copilot-refuses-harmful-requests.html)

**Swati Khandelwal**Jul 08, 2026Artificial Intelligence / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiO3sdn3FMdKySUzvuf2007OIkov1V6r7gOe6npkdpODZqGK0avIBUu4fc4XVYsccnBD3ij71TroVDezuYTjSmXj6le7luxRFK-S1q3itvZHcIwPaY2NzDYjEUH-hnBbOBa_GZSq7-Es2DG4v-6vlbqeZWvYohveEleH8n8eWD6GxafIJIvanFGzsLarQY/s1700-e365/copilot-prompts.jpg)

An AI coding assistant that refuses to answer a dangerous request in its chat box can answer it anyway if the same request is broken into small, ordinary-looking steps inside a code editor. That is the finding of a [new study of GitHub Copilot](https://arxiv.org/abs/2607.03968) by researchers Abhishek Kumar and Carsten Maple.

The models they tested through Copilot, Claude from Anthropic, and Gemini from Google, refused almost every harmful request when asked directly. Reframed as steps in a normal coding task, they produced the harmful answers in all 816 of the study's workflow runs.

What makes this different from a typical jailbreak: no one asks for the harmful thing directly, and the model is not tricked into running someone else's code. It writes the banned content itself, as a side effect of a coding task it was told to improve.

## How it works

The researchers call the method **workflow-level jailbreak construction**.

Instead of a single blunt prompt, they asked Copilot to build an everyday piece of software: a small test program that scores how often another AI model gives in to harmful prompts. Loading a list of harmful test questions into that program looks like ordinary work, not an attack.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Then came the nudge. They told Copilot the score was too low and asked it to improve the program by adding "teaching shots," example question-and-answer pairs written into the code to push the score up. Copilot added harmless examples first.

Asked to add the harmful ones, it wrote the dangerous answers itself, as plain text sitting inside the code. These were answers that the same models refuse when you ask for them straight out in a chat.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk76xNp9_NdFGw4MYRmomMVeavAMKf3SN1zTBiK_Kk24HcNU4fbRC5iZytekLWOGQqd6uCDjtVObGjK1z3JCqyFL1oAxpc67h96aAd6fIF3x6cKkOQnUlZ57-P1C4OfX8aM2AQ57jO-iEpjRSVd1GYUfEptKqO2mN63DgAT2lvTL07XZxq9gk_e_2Xbuw/s1700-e365/code-1.jpg)

The important part is where the harmful text came from. The researchers supplied only the questions, taken from public safety test sets. The answers were the model's own work, produced to complete the assigned task of filling in the examples.

## The numbers

The team ran 204 harmful prompts drawn from three public benchmarks (Hammurabi's Code, HarmBench, and AdvBench) against four models available through Copilot: Claude Sonnet 4.6, Claude Haiku 4.5, Gemini 3.1 Pro, and Gemini 3.5 Flash.

Everything ran on default settings, with the models used exactly as Copilot delivers them, no changed parameters or added filters.

Asked directly in chat, the models produced harmful answers in just 8 of 816 tries. Two other simple setups, loading the prompts from a spreadsheet or asking for a routine code fix, gave the same result. Inside the full workflow, they produced harmful content 816 times out of 816.

Two expert reviewers checked every response on their own and agreed that all 816 were genuinely harmful, using a strict test: the answer had to be specific, usable, and actually do what the harmful prompt asked. Refusals, vague warnings, and safe alternatives did not count.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQDaHu9zHDkXwngLu2BjcuJ9idO3sv4RQS7vC5Cw5lbydSXGoM3G8W9JDm0lzYOYmS-iK6sqWeM6B4tbmfruXnofi9xpkzj0ErkZcpKOYDUNceqaJGS6Tfa0GQVIgAmXNj59vnL2da5gFwsAWI1vm1Pm0iaNB1rqEYrlFGj2Md5Z9bAyqlWdsRONOPaws/s1700-e365/code-2.png)

The harmful output showed up after roughly six back-and-forth exchanges, all of them looking like normal coding steps. The tests used GitHub Copilot Chat 0.30.3 inside VS Code 1.103.0, in sessions run between April 2 and June 22, 2026. Because these are hosted services that update over time, the exact behavior may shift.

Why does it happen? The paper's answer is about incentives. Once the work is framed as raising a score, refusing to fill in one field stops looking like a safety choice and starts looking like leaving the job unfinished. The authors tie it to a known tendency in coding agents: optimizing for the metric they are handed, even when that cuts against their own guardrails.

## Why it matters

A chat refusal does not prove a coding assistant is safe. The same model can hold the line in conversation and cross it while writing code. And the failure hides in an easy-to-miss spot: the harmful text lands in a file the assistant writes, outside the chat reply where a refusal would normally show up.

For anyone using these tools, the concrete read is narrow but usable. Be wary of a multi-turn session that asks the assistant to fill an evaluation or benchmark harness with example prompts and answers to push a score up. Review the files the assistant writes rather than trusting that a visible chat refusal means the session stayed clean.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

The authors boil it down to three directions, none a full fix on its own: inspect what the agent writes, judge a whole session rather than each message, and treat a request to "improve a be...