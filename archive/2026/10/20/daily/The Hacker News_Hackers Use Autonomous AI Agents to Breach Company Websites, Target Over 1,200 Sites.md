---
title: Hackers Use Autonomous AI Agents to Breach Company Websites, Target Over 1,200 Sites
url: https://thehackernews.com/2026/10/hackers-use-autonomous-ai-agents-to.html
source: The Hacker News
date: 2026-10-20
fetch_date: 2026-10-21T06:51:12.165401
---

# Hackers Use Autonomous AI Agents to Breach Company Websites, Target Over 1,200 Sites

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

# [Hackers Use Autonomous AI Agents to Breach Company Websites, Target Over 1,200 Sites](https://thehackernews.com/2026/10/hackers-use-autonomous-ai-agents-to.html)

**Swati Khandelwal**Oct 20, 2026Artificial Intelligence / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYic0qXjDFjrKdw3Ed58Uv28Xt2G7GTuEZhXrAiV07Xnn_I9DPNeQuntZ-TNMi_4i0JdPOyLj4geWCj8K_Zv2OBO4qaujmlDFzBDljcRvvbDx-3r1hSDDaDN-mI3u61F2gJW6zhShFGLZBKrLM0k0Y9yl5-VOVXFHiJaEg3V65-yfT1yXWc5FSfaYLCKg/s1700-nu-rw-lo-l85-e365/bot-attack.jpg)

A Chinese-speaking criminal pointed autonomous AI agents at company websites and let them break in with almost no help, and a security researcher watched it happen because the operators left their control panels open on the internet.

The agents tried more than 1,200 sites and reached websites belonging to more than 100 companies, including farm-equipment maker Deere, appliance company SharkNinja and engine maker Cummins, [according to Reuters](https://www.reuters.com/legal/government/how-one-hacker-used-ai-agents-few-thousand-dollars-break-into-scores-sites-2026-10-19/), which reviewed the attacker's own records to identify them. How much data, if any, was taken is not known.

The researcher, Snorre Fagerland of the security firm **NorForge**, found the operations by scanning the internet for exposed copies of [Cairn](https://norforge.com/blog/inside_cairn), an open-source AI tool popular with hackers.

Beginning around October 2, he found about two dozen Cairn instances being used maliciously, which let him read the attackers' work in real time. He set out the findings on Monday, and Reuters, which saw the report before publication, named the victims from its own review of the attacker's activity.

Cairn gives AI agents a starting point and a goal, then lets them work toward it step by step. The agents post what they find to a shared board, and the human operator can add hints along the way. It was built for [authorized penetration testing](https://github.com/oritera/Cairn) and does other jobs too, but here it was pointed at online shops without permission.

Cairn's author, who posts as "le1xia0," told Reuters the tool was not designed for hacking attacks and that harmful use was not their intention.

### What the agents did, and who was hit

NorForge grouped the exposed panels into three clusters and judged more than 20 of them likely to be malicious. The busiest cluster, which NorForge calls AIA0001, is Chinese-language and links 14 panels to more than 1,100 attack projects.

Its aim seems to be lasting access to shop and payment systems for later use, NorForge said, with targets in the United States, Japan and Australia.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

A typical task told the agents to find a way to run code on a shop and then plant a web shell uploader. That is a form that saves uploaded files, not one that runs commands, and attackers can swap it for something worse at any time.

NorForge checked one claimed break-in, at a large hardware-parts vendor, and found the web shell live. It independently confirmed the compromise of one very large US retailer, in which the agents found the single cookie setting that selected a vulnerable backend server.

The three named companies told Reuters the damage was limited. Deere said it took steps to fix the problem and had no sign that sensitive information was accessed. SharkNinja said the attack hit a standalone product-support site and that it had contained the threat.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKWlfztW31xCL9GCv_IM02aBNvK7BQxbPL58zp9C877wrDwqkNoO_514rB4CUMNmacDgMLfSrtmfdBLWswGft9X7pu1GiirF1ReeG7HoP0qnm_TY_f_lnBgqA-98P3cGdi9Pf4BPxqe9tMUROq8jQaCgT16EXRlymHikDKllXsiY20p5XzhYKAemU3-G0/s1700-nu-rw-lo-l85-e365/project1.jpg)

Cummins said it was investigating a report of a possible attack on a website run by one of its vendors. Two smaller businesses also told Reuters they were compromised.

One documented intrusion, by the agent's own account, worked through unauthorized write access to a memcached session store, unsafe handling of saved PHP objects, and a weakness in old Zend Framework code. The paths differ from victim to victim, so this is one chain, not a single method.

### Cheap, fast, and largely unsupervised

The instructions were short. The Chinese-speaking operator sketched out preferred tactics in fewer than 100 Chinese characters, Reuters reported, and the agents went from there.

Successful break-ins took a little under 23 hours on average, NorForge found, and the overall success rate across the tools it saw was around 10%, though it cautioned the clusters chase different goals and are not directly comparable.

The cost was low, but the figures are rough. NorForge put the average at about $5 a task, counting attempts that failed or ended early, and said the uncertainty is considerable. Fagerland separately told Reuters the whole campaign had used about $5,000 worth of tokens, or roughly $50 per successful hack.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxCU0m3ePijI63AQtZy448sq_dsak85AbieKiduMI8l4iUOqsCQFFOfbbs-XnZ0sWoB8SbnDDrXGvOZgK6px8elVG91PPCialgheA9QyNhSXA-NRcIIBLYrmM8uI7ZycBAxYNCZ8rxKTrr6lj2nQFQYKtE7SSD1-iEO2gCWwPfQS_Fu0shvN6-aA7DMG4/s1700-nu-rw-lo-l85-e365/project2.jpg)

All the AIA0001 tasks ran under a worker named claudecode\_deepseek-v4.1-flash, which could point to a [DeepSeek V4.1 Flash](https://openrouter.ai/deepseek/deepseek-v4.1-flash) model driven by Anthropic's Claude Code. Neither the researcher nor Reuters confirmed the models, and Reuters said only that the campaign appeared to use DeepSeek and Claude Code.

### The open panels leak the victims' secrets too

Leaving a Cairn panel open is a separate problem from the break-ins. The panels show who is being attacked, wh...