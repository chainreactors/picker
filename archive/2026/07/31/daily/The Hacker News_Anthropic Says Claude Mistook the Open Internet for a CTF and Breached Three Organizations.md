---
title: Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations
url: https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html
source: The Hacker News
date: 2026-07-31
fetch_date: 2026-08-01T05:13:35.622015
---

# Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations

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

# [Anthropic Says Claude Mistook the Open Internet for a CTF and Breached Three Organizations](https://thehackernews.com/2026/07/anthropic-says-claude-mistook-open.html)

**Ravie Lakshmanan**Jul 31, 2026Artificial Intelligence / Offensive Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ3hIjH82iCzMILnA0uACotjW9waDLj4siTRhyphenhyphenBSiVyis0Ul0j7-7FcWyDzmCAzZPLJ72iYRezpbd9dUAB_UMw5G4eMBRwph0Sb_aQr9yCRXeLXAkjGiNFekM_qDtOZNFsSk6LLC81Ef74JaqIrcJN58-5p2ShHmUuhKC1IYeVgpQ7D76NWXLnR44RN6G6/s1700-e365/claude.jpg)

Anthropic on Thursday became the latest artificial intelligence (AI) company to [reveal](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals) that three of its models, including Claude Opus 4.7, Mythos 5, and an unnamed research model, had breached three unnamed organizations during cybersecurity testing without its knowledge.

The AI firm said the earliest incidents date back to April 2026, adding it made the discoveries after launching a "large-scale retrospective review" in response to a [recent disclosure](https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html) from OpenAI that a combination of its models escaped the sandboxed environment by exploiting a previously unreported zero-day in Artifactory to obtain internet access and break into Hugging Face's production systems with an end goal to cheat on an evaluation.

"After reviewing 141,006 evaluation runs where Claude could have obtained internet access, we identified three incidents in which a model accessed the internet from within or while interacting with the evaluation environment of Irregular, one of our third-party evaluation partners, and then gained unauthorized access to the production infrastructure of three different organizations," Anthropic said.

In all the identified incidents, Claude is said to have been tasked with a capture-the-flag ([CTF](https://en.wikipedia.org/wiki/Capture_the_flag_%28cybersecurity%29)) challenge to assess the models' capabilities, the intent being to locate a piece of secret information hidden on a different machine on simulated networks by any means whatsoever.

Although the evaluation prompt specified to Claude stated that the environment was a simulation and that it had no internet access, Anthropic said a misconfiguration left the machines the model accessed with live internet access due to what it described as a "misunderstanding" between the AI lab and evaluation partner Irregular.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

This, in turn, caused Claude's search to lead it to real systems on the open internet and treat them as in-scope for the exercise, effectively allowing the model to compromise the impacted organizations' infrastructure using basic techniques, including exploiting weak passwords and unauthenticated endpoints.

Anthropic emphasized that the model did not find or exploit any complex vulnerabilities, and that in each it continued working to complete only the specific CTF task its evaluation had assigned.

"However, in some cases, our older model continued its attack even after getting evidence it was running on the open internet; our latest model stopped once it recognized it was on the internet," it said. "In none of these situations did Claude exfiltrate itself or deliberately attempt to escape its test environment."

The details of the three incidents are as follows -

* An incident involving Claude Opus 4.7 in which it breached a real company's infrastructure by identifying and exploiting vulnerabilities, thinking it was part of the challenge after failing to reach its simulated target. This led to the extraction of application and infrastructure credentials and access to a database containing several hundred rows of production data. This is also the only incident where the model continued to attack the system despite "learning" it was operating in a real environment.
* An incident involving Claude Mythos 5 involved setup instructions to install a non-existent PyPI package, causing the model to go to "extensive lengths" to upload a Python package with the same name so that the fictitious company's systems would download and install it automatically. To achieve this, it found a non-blocked email provider, registered a PyPI account, and then used it to upload the package.
* During the roughly one-hour window the package was live on the registry, it was downloaded by 15 real systems, including a legitimate security company that routinely installs Python packages and scans them for malware. It's believed that the scanner deemed the booby-trapped package as safe to install, which led to it exfiltrating the company's credentials to an external endpoint set up by the model. The credentials were then used to access further infrastructure from this company. Neither the name of the package nor the company was disclosed.
* An incident involving an internal research test model that scanned about 9,000 targets and compromised one company's internet-facing application using techniques like reading credentials from an exposed debug page and SQL injection. However, the model later ceased the attack on its own after realizing the "compromised host sat in a cloud account with no connection to the capture-the-flag challenge."

Like in the case of the OpenAI incident, the models in each of these evaluations are said to have run without the standard guardrails that are deployed when they are made generally available to users. These evaluations were executed from dedicated infrastructure, which it said has no access to Anthropic's sensitive internal systems or customer data.

Anthropic also acknowledged that several defense-in-depth measures could have prevented these incidents from taking place, or at the bare minimum, reduced their likelihood. A validation of all internet access paths prior to the evaluations and real-time monitoring of the evaluation logs would have helped surface the issues sooner, it added.

The main takeaway from these isolated incidents is that advanced models are responding more appropriately than their predecessors, although more testing is needed to confirm this behavior, it pointed out.

[![Cybersecurity](data:image/...