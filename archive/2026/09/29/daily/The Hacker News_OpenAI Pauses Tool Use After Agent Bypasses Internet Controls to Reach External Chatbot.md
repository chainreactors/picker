---
title: OpenAI Pauses Tool Use After Agent Bypasses Internet Controls to Reach External Chatbot
url: https://thehackernews.com/2026/09/openai-pauses-tool-use-after-agent.html
source: The Hacker News
date: 2026-09-29
fetch_date: 2026-09-30T07:43:00.363642
---

# OpenAI Pauses Tool Use After Agent Bypasses Internet Controls to Reach External Chatbot

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

# [OpenAI Pauses Tool Use After Agent Bypasses Internet Controls to Reach External Chatbot](https://thehackernews.com/2026/09/openai-pauses-tool-use-after-agent.html)

**Ravie Lakshmanan**Sep 29, 2026Artificial Intelligence / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg2NfY2zvkkU95qQwwR7N_yQQf_H2AjYcXccbK2yH7xzzeAqmu3mH9ItszzC14M2suvDnfz6EBB-QzMkCTUBIgaoX9teGfhmBIBvU9R-wsKQBcC90f5lytvP-hYfCy8o-YTDTh8rIqz8mj1NIikN27BE2vsWyaRgiKPeAe3zbmrkdy6Dkg8htztnoyJwS4o/s1700-nu-rw-lo-l85-e365/openai-chatbot.jpg)

OpenAI said it has made the decision to pause training of its most powerful models after one of its agents during reinforcement learning (RL) training contacted an external chatbot by exploiting a loophole in its internet-access restrictions.

"An agent attempting to complete a search-based training task queried a public chatbot service through a gap in our internet-access restrictions: insufficient DNS filtering in its training sandbox," OpenAI [said](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/).

"Before this, the agent issued queries via our search tool and unsuccessfully tried to access search engines directly. Note that all internet access apart from the DNS resolver in this report hit our offline webcache and therefore did not access the live internet."

OpenAI said it has since added blocking controls at two independent layers to prevent this access in the first place. It also said its misalignment monitoring system detected the behavior within 15 minutes and it was acknowledged by a human reviewer three minutes later. The entire run is said to have been killed after 2.5 hours.

"All training, evaluation, and inference with tool-use (defined broadly) of our most capable models remain paused," the company added.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The incident, which took place on September 20, 2026, adds to two other misalignment reports OpenAI made public last week -

* **[May 27, 2026](https://alignment.openai.com/misalignment-reports/exposing-a-github-token-in-a-public-repository/)**, when a highly persistent internally deployed model published a researcher's GitHub token in the public "openai/codex" repository while attempting to cheat on a theorem proving task by obtaining material from another team's Lean proof submission. To avoid secret scanning, the agent split the token into fragments.
* **[Jun 27, 2026](https://alignment.openai.com/misalignment-reports/self-replicating-prompt-injections-exist/)**, when a GPT-Red-style internal model based on GPT-5.4-mini engaged in what has been described as a self-replicating prompt injection that's similar to a computer worm.

In one case highlighted by OpenAI, a prompt injection that arrives by email instructs the agent to copy it into any email it sends, effectively propagating the malicious prompt in a worm-like manner. Such attacks can also replicate via the file system or commit themselves through source code comments.

The disclosure comes as OpenAI said it [discovered](https://openai.com/hugging-face-incident-and-misalignment/) 53 cases where images that people had uploaded to its models and subsequently included in training data were posted to image-hosting sites as links that weren't publicly listed. These were carried out by agents in its research environment.

"This is not an appropriate use of this data," OpenAI said. "We have successfully worked with the hosting providers to remove most of this content and are continuing to work to remove the rest."

OpenAI said it could not notify the affected users because "our technical approach and privacy policy" prevent it from "reassociating" the images with the original providers. It's unclear how the frontier AI lab determined whether the images were provided by users and when these images were posted.

These ongoing findings are part of an ongoing review into the [behavior of its models](https://thehackernews.com/2026/09/openai-agents-linked-to-rubygems.html), as reports of [OpenAI's agents going rogue](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html), escaping containment, and hacking real-world sites [continue to pile up](https://www.axios.com/2026/09/26/openai-anthropic-thousands-ai-security-incidents).

As of September 25, 2026, the company has acknowledged that it notified dozens of third-parties that their websites or online services may have been [targeted](https://www.nytimes.com/2026/09/25/technology/openais-ai-us-government-websites.html?unlocked_article_code=1.D1E.WoUU.RA8YL284X9eQ) by its models. Targets [included](https://www.reuters.com/world/openai-works-understand-full-scope-agent-activity-user-data-leak-emerges-2026-09-25/) governments, universities, public agencies, and other institutions, [such as](https://www.nytimes.com/2026/09/25/technology/openais-ai-us-government-websites.html) the U.S. Securities and Exchange Commission (SEC), Census Bureau, and Department of Education.

"The vast majority of actions we've reviewed were completions of mundane research tasks, such as accessing publicly available web content to answer questions," OpenAI stressed. "That is partly because models performing research tasks are often directed toward authoritative sources of public information."

Last week, AI research firm Transluce [revealed](https://transluce.org/agent-activity) that OpenAI agents had attempted to hack into public data providers by probing for exploitable vulnerabilities, including websites linked to the University of New Mexico, the Australian Institute of Health and Welfare, and Data USA, as part of web search tasks.

The unsanctioned activity occurred between May and June 2026. The Australian government has since also [disclosed](https://www.pm.gov.au/media/press-conference-new-york) that the OpenAI agent infiltrated the Services Australi...