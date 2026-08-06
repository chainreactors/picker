---
title: Poison Claude Sells Discounted Claude Access While Its Operator Sees Every Customer Prompt
url: https://thehackernews.com/2026/08/poison-claude-sells-discounted-claude.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:51.233727
---

# Poison Claude Sells Discounted Claude Access While Its Operator Sees Every Customer Prompt

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

![cybersecurity](data:image/svg+xml;base64...)

# [Poison Claude Sells Discounted Claude Access While Its Operator Sees Every Customer Prompt](https://thehackernews.com/2026/08/poison-claude-sells-discounted-claude.html)

**Ravie Lakshmanan**Aug 05, 2026AI Security / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp3V9f5UsiH1E6dHfRvy0DEOYvcK14BatMbbLVfdPjLbu3PMInRmVXDi4xoGw-pSIuxUjZS1rdv4X7N1V9xRoV9RRVfaYdAWI6OTxKZzOhAlHYh6dKZNeAWCPkaPdGAvwgcOwFQ0atoRBUxKfE_KfhJpnm1yV1tXr5_Wv2yqND0vZCMMEfRB0V220SZbne/s1700-e365/ai-access.jpg)

Cybersecurity researchers have discovered more than half-a-dozen services advertisements for illegal access to artificial intelligence (AI) models on underground cybercrime forums and messaging platforms.

One such service, Poison Claude, claims to offer access to Anthropic's large language models (LLMs), including Opus 4.8, Opus 4.7, Opus 4.6, and Sonnet 4.6.

"Advertisements for Poison Claude explain how the service can offer the cheap tokens: by taking advantage of free bonus credits, such as the US$100 bonus credit on AWS for Bedrock accounts," Okta researchers Jeremy Kirk and Mathew Woodyard [said](https://www.okta.com/blog/threat-intelligence/free_tokens_for_sale/) in an analysis published Tuesday.

"The service plainly states on its website that: 'We add those accounts to our pool, your request is routed to a specific account under the hood (you don't see this), and you get charged 5-15% of the official per-token price depending on the model.'"

Poison Claude accepts payments in cryptocurrencies. Once a customer completes a payment, they are provisioned an API key for an Anthropic-compatible API and instructed to set certain environment variables to ensure that their development environment (i.e, Claude Code) uses the Poison Claude API instead of Anthropic's.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

Prompts entered as inputs are then passed from Poison Claude's API to Anthropic, with the answers eventually returned to the customer in the same fashion.

The identity security company said a configuration error exposed the API's "api.claudeopus[.]shop/api/status" endpoint, querying which returns the number of total and active users as 881 and 872, respectively. The exposure has since been fixed.

The main domain for Poison Claude, poison-claude.bitsender[.]top, is hosted behind Cloudflare's CDN to conceal its originating IP address. Following responsible disclosure, Cloudflare has placed a phishing warning in front of the site, but appears to have "declined to take action" on the API domain, which uses Cloudflare Turnstile for bot protection.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVH8DnWdzJxIIqzS7lJJP_m9KmbR2cKwCW756fJqyfxa9zlpexxd5x5VqbgLdNL1u5AdWJZyif0h9CoQTkyZE8KIFn47ODe1exoRRV7pg1Wnm4cFHwHBj2EqN5YaZGRTrIwuX4mQ5T4yetxbO5pqOPa70x9dtyWpioGhRRqcNbM_n4-k2kpDNmqHfqnjfi/s1700-e365/okta.png)

A similar service that operates in the gray market is Ecomagent.in, which is estimated to have nearly 970 users and claims to offer discounted access to Anthropic's Opus 4.8, Opus 4.6, Sonnet 4.6 and OpenAI's GPT Codex 5.5 via a custom API endpoint.

While there are many reasons why users may seek out such services offering AI model access, including cost, access restrictions, and some degree of privacy and anonymity, they also come with several inherent risks.

Model providers may cut off access to fraudulent accounts, or service providers may lure customers with a frontier model but deliver a less expensive and less capable model.

"When services are configured as a gateway proxy, the service provider has full visibility into prompts, as those prompts must be forwarded to a model," Okta said. "This is a privacy concern, as the service provider could accidentally leak or sell data."

The findings come amid a [growing Chinese market](https://www.chinatalk.media/p/the-grey-market-for-american-llms) for U.S.-based LLMs that are either explicitly banned (as in the case of ChatGPT) or inaccessible in the country due to the Great Firewall. These services offer [API relay or proxy platforms](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html) that allow local developers in China to access the models.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Earlier this year, Anthropic [accused](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html) three Chinese firms, DeepSeek, Moonshot AI, and MiniMax, of orchestrating "industrial-scale campaigns" to illegally extract Claude's capabilities to improve their own models. As recently as last week, Reuters [reported](https://thehackernews.com/2026/08/weekly-recap-rogue-ai-models-88m.html#:~:text=Chinese%20Military%20Taps%20Into%20U%2ES%2E%20Models) that Chinese military researchers have used AI models developed by OpenAI and Anthropic to train domestic AI systems with an aim to advance their defense capabilities.

What's more, evidence shows that bad actors are abusing free trials offered by AI services to facilitate synthetic identity creation at scale using disposable domains like dakaka[.]org, emailinbo[.]live, and ratixq[.]com.

"Bot activity is rising across the internet, particularly with the increasing deployments of AI agents," Okta said. Those running bot networks also have more choice than ever with which to counter bot detection methods, such as residential proxies. Residential proxies allow malicious traffic to come from benign consumer IP connections with often little or no history of malicious activity, making it risky to block."

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
[**Share on Reddit](#link_...