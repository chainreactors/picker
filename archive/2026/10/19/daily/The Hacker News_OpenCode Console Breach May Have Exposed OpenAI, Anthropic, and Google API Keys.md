---
title: OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys
url: https://thehackernews.com/2026/10/opencode-console-breach-may-have.html
source: The Hacker News
date: 2026-10-19
fetch_date: 2026-10-20T06:53:59.077677
---

# OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys

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

# [OpenCode Console Breach May Have Exposed OpenAI, Anthropic, and Google API Keys](https://thehackernews.com/2026/10/opencode-console-breach-may-have.html)

**Swati Khandelwal**Oct 19, 2026Data Breach / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzRSuvywT7bfHRl45krYywOIqL__Cw1hXchChbx5ylDNZaHxVDEf8O1pmzajCnItG1rwxKq0k2GHdMeDW_DvQP8Wk5MEiwlE2dZXn9grvDpAOpViWonNWsFMkTXoKpcFj8lk0UuMrGx-xVHRU_KufidsDcY7e0RUSG62aapDC9y9opt8V_rmgxkCG9v6A/s1700-nu-rw-lo-l85-e365/opencode.jpg)

An intruder reached a legacy system at **OpenCode** on the night of October 16 and may have exposed the third-party AI provider keys that users had saved in OpenCode Console, the company said.

Console is OpenCode's optional hosted service: a workspace saves its own OpenAI, Anthropic, or Google key there, and Console uses that key to call the provider so team members can use the models without ever seeing the key.

The affected group is 1.4% of Console users, all of whom have an outside provider linked, and OpenCode has told them via email to revoke those keys with each provider and replace them.

The email went out on the morning of October 17 under the subject line "Action Required: Potential provider key breach." Anyone who did not get one was not affected, [OpenCode said](https://x.com/opencode/status/2111519637049319818) in a post on X later that day.

The keys at risk are the ones pasted into Console. The OpenCode command-line and desktop apps keep provider keys added on the machine in a [SQLite database](https://dev.opencode.ai/v2/docs/cli/providers/) there. The breach involves "the OpenCode Console, not OpenCode itself," co-founder Dax Raad [wrote](https://x.com/thdxr/status/2111572618340188393) in a reply on X, and those keys "never come to us."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

A provider key is a bearer credential: whoever holds a copy can run billable requests against the owner's account until the provider revokes it. Deleting the key from Console does not revoke it, and a Console budget cannot cap that use either, because Console only sees requests that pass through its own [gateway](https://dev.opencode.ai/v2/docs/console/api/providers).

For a key that was saved in a Console workspace, OpenCode's email and the providers' own guidance give these steps:

1. Revoke the key in the provider's own dashboard and create a new one, following the instructions from [OpenAI](https://help.openai.com/en/articles/8304786-keeping-your-openai-account-secure), [Anthropic](https://support.claude.com/en/articles/8384961-what-should-i-do-if-i-suspect-my-api-key-has-been-compromised), or [Google](https://docs.cloud.google.com/docs/authentication/api-keys-best-practices).
2. Update every application and script that used the old key.
3. Review usage and billing at the provider for requests you did not make, going back at least to October 16. OpenCode has not said when the unauthorized access began.
4. Set a spend limit or alert at the provider and give each tool its own key, so a copied key does less damage and its use is easier to trace.

Some users say they have already paid for usage they did not run. [Dealroom reported](https://dealroom.co/news/163473-opencode-breach-drains-users-ai-keys-as-platforms-holding-customer-crede/) that Colin Parsons wrote on X that his OpenAI key had been used for $281 and his Anthropic key for $168, and that Preston Zeller put his losses at $1,700.

[Notebookcheck reported](https://www.notebookcheck.net/OpenCode-hacked-users-urged-to-revoke-their-API-keys.1426957.0.html) a Reddit user's claim of $400 of unauthorized usage on an Anthropic account, and another's of about €200 of Google usage, with the project then suspended.

Those are the users' own accounts. OpenCode's own wording is that the keys "may have been exposed," and it has not said that any key was copied or used.

OpenCode's October 17 post also called the incident ongoing, said the company was working with Anthropic, OpenAI and Google to fix it, and described the breach as "related to a large-scale distillation attack." The company has not named anyone or said how the two connect, what the legacy system was, how it was reached, how many keys it held, or how many users 1.4% represents.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

Distillation is the term AI model providers use for campaigns that pull a model's answers in huge numbers to train a rival model. Anthropic said in September that the labs behind such campaigns reach its models through networks of fake accounts created with stolen credit cards, login credentials and [harvested API keys](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html). A stolen key has other uses too: criminal markets [resell AI tokens and keys](https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html) and use them to run up bills.

Attackers were still trying to get into OpenCode's systems on October 18, Raad [wrote](https://x.com/thdxr/status/2111790511409258796) on X: they had been "non stop trying to attack our systems for the past 48 hours," and "a side effect is everything is getting hardened."

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
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#li...