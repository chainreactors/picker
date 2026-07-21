---
title: Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs
url: https://thehackernews.com/2026/07/russian-speaking-hacker-uses-google.html
source: The Hacker News
date: 2026-07-20
fetch_date: 2026-07-21T05:03:17.523730
---

# Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs

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

# [Russian-Speaking Hacker Uses Google Gemini CLI to Control Botnet of Eight Dental Clinic PCs](https://thehackernews.com/2026/07/russian-speaking-hacker-uses-google.html)

**Ravie Lakshmanan**Jul 20, 2026Artificial Intelligence / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyO5FC_n2BBZmiHphtqs0UN5r3DPgtRvkrVfaHOW-1Fv2VPXZliRYDryKR5I-vdZxtmChQJB6eAlJsND-e47t5lLQQ4SWkSJ_D02SEL6nRBmnJ-klfjSSg7rjRyf5AfzX340_se2vNrobCydtV-NZPsDm8MvL9UG0atiMekaxCNzHwizxZFlRhvpuM8BjE/s1700-e365/gemini-cc.jpg)

A solo Russian-speaking threat actor known as "**bandcampro**" outsourced a chunk of their operations to Google's open-source Gemini CLI artificial intelligence (AI) and commandeered a live botnet.

The findings come from an analysis of 200 Gemini CLI session logs between March 19 and April 21, 2026, which found the threat actor using AI, among other things, to crack passwords, set up a residential proxy, compromise WordPress merchants, and plan a phone-based cryptocurrency fraud scheme aimed at elderly people in the U.S. and Canada.

"The logs documented how the threat actor used an AI agent to migrate a command-and-control (C&C) server, and to control a small-scale botnet, among other hacking activities," Trend Micro researchers Joseph C Chen, Philippe Lin, Lucas Silva, Vladimir Kropotov, and Fyodor Yarochkin [said](https://www.trendmicro.com/en_us/research/26/g/actor-behind-patriot-bait-used-ai-to-deploy-c2-botnet.html).

"The entire C&C operation fits in three plaintext files totaling roughly 5 KB, making it highly replicable and effectively disposable. The AI was also observed to proactively (unprompted) propose improvements 59 times without being asked."

Specifically, the threat actor is said to have abused Google Gemini CLI to deploy and operate a C&C infrastructure to control eight computers in a dental clinic and access their OpenDental database. Besides writing code snippets, the AI served as the "primary hacking agent, consultant, and interface" to the entire operation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

This included setting up the server, deploying it on a new virtual private server (VPS), configuring the infrastructure, setting up Cloudflare tunnels, managing the bots, and debugging connectivity issues.

Details of "bandcampro" [first emerged](https://thehackernews.com/2026/06/weekly-recap-new-linux-flaw-pan-os.html#:~:text=Solo%20Russian%2DSpeaking%20Threat%20Actor%20Linked%20to%20Patriot%20Bait%20Campaign) in late May 2026 in connection with a campaign dubbed **Patriot Bait** that used AI-assisted information operation (IO) techniques to run a Telegram channel, targeting politically engaged American audiences for cryptocurrency fraud and AI-assisted credential theft.

Trend Micro has described the threat actor as a Russian speaker who used Google Gemini to "impersonate an American veteran patriot and to avoid Russian phrasing," while tricking the AI agent into bypassing its guardrails by assuming the role of an "authorized pentester."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqtKyUyCoZLnEFwgjc7-v8BpywctBXKhT97rVg3wq1rBEtVOIjEWDQhnkJiAM7W9SO5AhZkZtWzh-yaOCWN_pa9P1Tj1rwUGRuO5lVV6cbWaWCN350jvNt0aEeRhMepFN7xsjZX_LppfGmeZWZUTbZD8w9xCno2AKSL_nplbeRCMrMLl1-AVERJk3Zv-7N/s1700-e365/cc.png)

The threat actor is said to have run prompts to study the old C&C infrastructure where the victim machines connected using Cloudflare tunnels and migrate it to a new architecture within six minutes. The architecture involves victims issuing outbound requests to a C&C server over HTTPS to pull and run PowerShell commands staged by the threat actor on the server.

"The migration hit errors immediately, but the AI agent resolved them: When the payload distribution server returned a '502 Bad Gateway' error, the AI diagnosed the issue and automatically added the necessary header to resolve it," Trend Micro said.

"As Cloudflare still blocked the requests, the AI identified that the User-Agent header was required to bypass the WAF and thus added it to the request header. The actor did none of the debugging, and the migration was done in merely six minutes."

Once the migration was complete, the AI agent carried out additional debugging to successfully remediate errors that left all the victim machines disconnected from the C&C infrastructure. In addition, the threat actor has been found to leverage the AI agent to perform botnet management tasks by sending natural language instructions in Russian, which then enabled the AI tool to perform the following tasks -

* Report which machines are active
* Send a file enumeration command to the bot
* Send reconnaissance commands to the front desk machine
* Generate a one-line PowerShell command to infect a machine

What's particularly concerning about this AI-assisted setup is that the entire C&C operation can be easily ported to a fresh server through three markdown files that instruct the agent to disable its safety protections, contain the architecture description, and include steps to build it from scratch, making takedowns a lot less effective than before.

"Facilitated by AI, the infrastructure becomes disposable, and the operators replaceable," Trend Micro said. "Even though the takedowns are still efficient, they become much less impactful. If a server is burned, the actor could simply unpack the bundle on a new VPS, and AI configures and restores everything in a few minutes."

The findings show that the technology can not only cut the resources necessary to run large-scale operations, but also enable bad actors with little to no technical knowledge to set up such schemes with minimal effort or distribute them on underground forums in the form of malicious skill files, effectively paving the way for new AI-powered malware services that go beyond the conventional "as-a-service" models.

This playbook also has t...