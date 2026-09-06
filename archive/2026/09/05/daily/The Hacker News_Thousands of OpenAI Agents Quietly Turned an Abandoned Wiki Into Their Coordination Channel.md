---
title: Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel
url: https://thehackernews.com/2026/09/thousands-of-openai-agents-quietly.html
source: The Hacker News
date: 2026-09-05
fetch_date: 2026-09-06T06:40:18.572596
---

# Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel

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

# [Thousands of OpenAI Agents Quietly Turned an Abandoned Wiki Into Their Coordination Channel](https://thehackernews.com/2026/09/thousands-of-openai-agents-quietly.html)

**Swati Khandelwal**Sep 05, 2026Artificial Intelligence / AI Agents

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBL2gQMKgajDATkCjnHyMtUkVhK5mcTQ2ebqcXngB6oZ71uiJ3skI9P4zikK1s5PCH4nhPG7ZyFHHWC13OVF2KRr_pIQ2U7zFITnNc3Qc_Am3bv0E1AzL9UVmrJ9vUJzZalktYIxWGlc-d5zYdicOJexMDWQ-4NIKinC_AksG1Mepn7QmFGWC1x52gVpw/s1700-nu-rw-lo-l85-e365/agents-openai.jpg)

A group of AI safety researchers says a fleet of autonomous agents that identified themselves as OpenAI systems left about 18,000 posts on a dormant 25-year-old German wiki between May and July 2026, using the site as a shared board to pool answers to a timed web task and pass around a way out of their sandbox.

The activity was concentrated on **DSEwiki**, a German software developer wiki that runs on the ProWiki farm at wikiservice[.]at and had been edited about 20 times over the previous decade.

The researchers, led by Sydney Von Arx of the AI safety nonprofit [Nightingale Collective](https://nightingalecollective.org/), reconstructed the deleted pages from edit history and published their analysis along with a downloadable copy of the data.

The wikis let anyone change a page with an ordinary web request, the kind normally used only to read a page rather than to write one. Agents that were restricted to reading the internet could therefore still write to the site, because the restriction was written against the request type their harness expected writes to use, not against what the old wiki software would actually accept.

"We found ~18,000 posts from autonomous AI agents (self-identifying as from OpenAI) using the public internet to communicate during a web-retrieval task," the researchers wrote in [their published report](https://collusion.wiki/).

The agents were working through timed lookup tasks of usually five questions, and many were given questions that other agents had already answered. According to the report, they posted results, raw data, and predictions of upcoming questions so that agents running ahead could hand answers to those running behind.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

About 17,000 of the edits on DSEwiki came from Microsoft Azure addresses, 98.5% of them, and the agents gave themselves more than 3,700 distinct names such as OpenAIResearcher and OAIResearchMar26, drawn from a feature of their task plus a date each was apparently told it was running on.

The researchers documented several distinct behaviors on the site -

* **Writing via a read request:** agents used the wikis' acceptance of state-changing read requests to post without the ability to send a normal write request.
* **A proxy bypass:** one task needed a statistic to two decimal places from a Microsoft Power BI dashboard, reachable only with a write request the sandbox blocked, so agents worked around the block and shared the method.
* **Impersonation:** agents made edits under the name of a wiki moderator.
* **Coordination to cheat a timed task:** agents formed groups to relay answers and reverse-engineer the order of future questions.
* **Alternate routes:** 197 of the roughly 18,000 edits came from Amazon Web Services, DigitalOcean, and the Tor anonymity network rather than Azure, often under the same agent names.

The bypass turned on a gap the agents found in their own sandbox. The environment allowed traffic to reach Azure storage hostnames ending in .blob.core.windows.net without passing through its security proxy, but it did not verify that such a hostname was valid.

An [agent invented](https://x.com/thlarsen/status/2095853824934330386) bypass[.]blob[.]core[.]windows[.]net, pointed it at the real dashboard's address, 20.223.25[.]152, by editing its /etc/hosts file, and sent its blocked request there instead. One agent posted the method, and another reported reproducing it about 14 minutes later. The wiki path worked the same way, the researchers say, turning a web capability meant only for reading into a way to write to the public internet.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhaSdhZxwrfzeLapJPJRdHHqzDkLKTSCDQk9cK3tnhiexk5X5t2BBG4ZDAYMg9Ns6AJTtd9qv77dqU1eGmsU23QU-iEH-cuGR8sEIQCx-93n9XLrzOZbDLn6tLGd2R6P4zKVXKCjqQmUz0_I0mpiIzktHuHkMnmmjh1jmDsfdt863ntWFxMZPp9m-9RxbU/s1700-nu-rw-lo-l85-e365/data.jpg)

The researchers say the wiki activity was a separate episode from the OpenAI models that [broke into Hugging Face](https://thehackernews.com/2026/07/openai-says-its-own-ai-models-escaped.html) in July, as described in [OpenAI's July disclosure](https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html).

Those agents had no internet access and had to escape a sandbox, while the agents on the wiki were given web access as part of their task and left no sign of the internal message board the Hugging Face swarm used.

In [an independent investigation](https://thehackernews.com/2026/08/openai-says-reward-hacking-drove-ai.html) of the Hugging Face incident, METR found that roughly 1,200 agents exchanged more than 70,000 messages and files on an unsanctioned board, and that about 700 of them went on to attack the platform.

### What OpenAI Has Said

OpenAI has not publicly disclosed the wiki episode, and the researchers infer from the site's public logs that the company found it. Addresses registered to OpenAI first visited the wiki on June 21, and agent editing collapsed the next day.

The Hacker News confirmed via [ARIN's registry](https://rdap.arin.net/registry/ip/199.47.142.0) on September 5 that one of the address blocks the report cites, 199.47.142.0, is registered to OpenAI OpCo, LLC.

OpenAI has not confirmed that the agents were its own. Asked about the report, which Reuters first reported, an OpenAI...