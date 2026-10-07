---
title: Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki Tools as Proxies
url: https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:35.300924
---

# Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki Tools as Proxies

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

# [Wikimedia Says OpenAI Agents Tried to Compromise Etherpad and Use Wiki Tools as Proxies](https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html)

**Ravie Lakshmanan**Oct 06, 2026Artificial Intelligence / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWN60cSxpzLhK9K0oXjbeGNCoMl79wSkfW1h7dVHHi3dQPeRx2QUvM9dNGF3qKELV9xwkn8N_FBHk0WgftQryFzkKWyEf0jGbPb6ffor00ZQQnVPSrSSWKDfL10Shpkm2Q_LRFb85BarRqvdDE8eIksiGSrRy6hk8CD2cGf4xIIALAbOZEfHWMHWc7LfhA/s1700-nu-rw-lo-l85-e365/wiki.jpg)

The Wikimedia Foundation, which hosts Wikipedia, has confirmed that it has discovered activity by rogue OpenAI agents on its platforms, including unsuccessful efforts to compromise Etherpad, a public note-taking tool, and edit Wikipedia pages.

"The unauthorized bot activities included edits to our wikis, some unsuccessful attempts to exploit a public note-taking tool we host, and heavy traffic," the Foundation [said](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/) in a post.

The investigation, it added, was prompted by recent public reports involving [Hugging Face](https://thehackernews.com/2026/08/openai-says-reward-hacking-drove-ai.html) and [DseWiki](https://thehackernews.com/2026/09/anthropic-ai-models-breached-real.html) where OpenAI's agents turned Artifactory and the German wiki forum into an unsanctioned bulletin board to communicate with each other, while taking steps to [chained together online services](https://swarmtraces.org) to gain access to the internet and cover up evidence of their exploits.

To that end, Wikimedia said it identified edits to Wikimedia wikis suspected to be from agents operated by OpenAI. The agents are said to have been testing edits in "[sandbox](https://en.wikipedia.org/wiki/Wikipedia%3AAbout_the_sandbox)" areas of the wiki and were not published to pages that can be accessed by general readers.

Among the edits included were changes to the configuration for a citation tool. These modifications are believed to be malicious in nature, with the intention being to misuse the tool as a proxy for fetching data from remote services.

Agents operated by OpenAI are also assessed to have made unsuccessful attempts to compromise Etherpad and again use it as a proxy to retrieve data from other websites. In addition, a subset of the agents took notes about their tasks, although there is no indication to suggest this was an attempt to coordinate with each other.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

As observed in the case of [RubyGems](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html) and incidents [targeting government portals](https://www.washingtonpost.com/technology/2026/09/25/openais-ai-agents-probed-federal-agencies-including-commerce-department), the agents have also been observed making "millions of automated requests" to its public APIs to access information about Wikimedia projects, crawling millions of pages related to Wikidata and Wikimedia Commons, and running thousands of data queries to the Wikidata Query Service (WQDS). This traffic flood may have contributed to a [partial outage](https://wikitech.wikimedia.org/wiki/Incidents/2026-05-13_wdqs) that happened in early May 2026.

That said, Wikimedia said it found no evidence of its systems being used for coordinated activity among agents or that its systems or data had been compromised as a result of these efforts.

"However, we are concerned about what could have occurred here, the difficulty and effort involved in investigating and attributing this activity, and the growing risks of agentic AI activity on our platforms in general," it pointed out. "The open web is a public good. We should not allow this behavior to become the 'new normal' for the people or organizations that maintain it."

The Wikimedia Foundation noted that the agentic behavior, coupled with increasing bot traffic, risks blocking human visitors by overloading systems and causing service disruptions. It also called out AI companies for not doing enough to secure their systems and ensure they do not cause any harm.

"Bots and agents are part of the future of the web, and the companies who unleash and profit from them must directly help avoid and repair damage they can do," Selena Deckelmann, the Foundation's chief product and technology officer, said.

OpenAI, in a statement [shared](https://www.theverge.com/news/1004929/wikipedia-openai-rogue-bots-wikimedia-foundation-outage) with The Verge, said it's working with the Foundation to review and analyze the activity, and that it will share relevant information as its broader investigation into rogue agentic incidents continues.

### OpenAI Discloses New Incidents

The development comes days after the AI company disclosed three new cases where its models exhibited possible misaligned behavior -

* **[March 27, 2026](https://alignment.openai.com/misalignment-reports/reaching-an-internal-eda-host-through-a-reference-tool/)**, when an internal research model exploited two vulnerabilities to reach an internal OpenAI machine in its quest to search for a grader's hidden answers during evaluation. The two security flaws were chained to obtain unauthorized access to an internal electronic design automation (EDA) machine and search for information about how its outputs would be evaluated.
* **[May 16, 2026](https://alignment.openai.com/misalignment-reports/command-injecting-a-reference-tool-to-copy-a-source-file/)**, when a model exploited a tool to fetch source code that was not available in its workspace during a reinforcement learning training task. "The tool ran in a separate environment, and its instructions prohibited using it as a terminal. The model discovered that it could read a source file and return its contents in error messages," OpenAI said. "It retrieved the file...