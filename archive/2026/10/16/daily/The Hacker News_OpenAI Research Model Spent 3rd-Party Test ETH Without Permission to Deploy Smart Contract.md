---
title: OpenAI Research Model Spent 3rd-Party Test ETH Without Permission to Deploy Smart Contract
url: https://thehackernews.com/2026/10/openai-research-model-spent-3rd-party.html
source: The Hacker News
date: 2026-10-16
fetch_date: 2026-10-17T06:39:13.876683
---

# OpenAI Research Model Spent 3rd-Party Test ETH Without Permission to Deploy Smart Contract

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [OpenAI Research Model Spent 3rd-Party Test ETH Without Permission to Deploy Smart Contract](https://thehackernews.com/2026/10/openai-research-model-spent-3rd-party.html)

**Ravie Lakshmanan**Oct 16, 2026Artificial Intelligence / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhkqmj8WR1EBIXlf0-PIfEmv-3uEk-0FU-SrKAaQyn33syLPFRar-jwks7o70PVBvmNd05CwdNSVPXRq3bN6ED0jREr__oFnSFjS1emRZoEfvsfw8UlSspGcSWLLKJcgUhDuzV814VaFSecnEzNhvhTbemuVizjA46o3g-d7hZj1F-Fmn6sqssQyMeayXC/s1700-nu-rw-lo-l85-e365/openai-smart.jpg)

OpenAI has disclosed [seven new incidents](https://alignment.openai.com/misalignment-reports/?sort=created) in which its artificial intelligence (AI) models exhibited misaligned behavior, including one case where its research model, after not having funds on an Ethereum test network, spent test cryptocurrency from a third-party's wallet without authorization to complete a coding task.

The incident, the AI company said, involved an internal research model part of the GPT-5.6 Sol family. The incident occurred on June 26, 2026, and was discovered by OpenAI three months later.

"An internal research model asked to update a cryptocurrency trading application used funds from a wallet that the task had not supplied to pay for a deployment on Sepolia, an Ethereum test network," OpenAI [said](https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/). "It derived wallet keys from publicly known developer recovery phrases, found an account with test-network funds, and used that account to pay for the requested contract deployment."

The assignment allowed the model to deploy compatible contracts if it did not find one, but gave it no funded wallet to pay the network fees. After its attempts to obtain free test tokens failed, it wrote a script to derive "accounts from common developer recovery phrases and query their balances."

In the process, it identified 362 addresses and found one account that held enough Sepolia ETH. Armed with the recovery (or seed) phrase, the model derived the private keys that grant unauthorized access to the corresponding account and spend the stashed cryptocurrency.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Although the model questioned whether it had the necessary permission to carry out this step, it subsequently reasoned that a public recovery phrase and valueless test-network tokens made the funds acceptable to use.

"But using public known key/funds ethically? Funds on a known public dev mnemonic are effectively abandoned/test ETH; Sepolia valueless," the model mused. "We can use [amount redacted] to deploy task. Fine."

OpenAI has since implemented additional safeguards to prevent live internet access for such scenarios, adding it runs its misalignment monitoring system on all traffic to flag events if its AI agents manage to gain live internet access.

"This case shows that a model can substitute its own judgment about likely harm for the account holder's permission, then act on that judgment without authorization," OpenAI said.

Besides using a funded test cryptocurrency wallet without authorization, OpenAI said it identified six more cases of misalignment involving its models, adding to [three other incidents](https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html) it revealed at the start of this month -

* **[June 16, 2026](https://alignment.openai.com/misalignment-reports/circumventing-internet-restrictions-through-an-external-browser/)**, when an internal research model bypassed a restriction limiting internet access to HTTP GET requests as part of efforts to seek public trade statistics. It achieved this by using an external browser to send requests on its behalf, retrieved annual figures as an image, and extracted them using optical character recognition.
* **[June 16 and 17, 2026](https://alignment.openai.com/misalignment-reports/sending-disallowed-web-requests-and-reaching-a-public-file-service/)**, when an internal model developed and tested ways to bypass restrictions on internet access during reinforcement learning and explored ways to contact outside services, and continued testing these approaches even after obtaining the statistics it was seeking, such as teacher salaries in Merrowen, connections to the electrical grid in Orvessa, and disability counts in Bellora.
* **[June 17, 2026](https://alignment.openai.com/misalignment-reports/accessing-and-changing-internal-systems-during-dashboard-research/)**, when a highly persistent internal model tasked with retrieving figures from a public research dashboard accessed an unspecified organization's internal systems and changed their configuration. The model altered a setting to obtain a cloud-storage access token and downloaded non-public tables containing 147,451 rows. Not only did the model not disclose these actions, it restored the modified setting, but continued using the token to retrieve non-public data.
* **[June 17, 2026](https://alignment.openai.com/misalignment-reports/retrieving-server-secrets-and-bypassing-authorization-on-a-government-statistics-website/)**, when a highly persistent internal model deployed as part of a data-retrieval task in reinforcement-learning training abused a government statistics website's file-download feature to retrieve server configuration and application files, including sensitive credentials. It then analyzed the application code, bypassed the statistics endpoint's authorization checks, retrieved data that it was denied access to, and stored it locally. The data included annual statistics spanning 24 years, including years beyond the requested year. In its answer, the model made no mention of the fact that it had obtained unauthorized access.
* **[June 19 and 20, 2026](https://alignment.openai.com/misalignment-reports/obtaining-public-statistics-w...