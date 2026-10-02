---
title: ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories
url: https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html
source: The Hacker News
date: 2026-10-01
fetch_date: 2026-10-02T07:49:37.657126
---

# ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories

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

# [ThreatsDay: AI-Powered Zero-Day Chain, 543K Live Secrets, Model Inspection RCE and 13 More Stories](https://thehackernews.com/2026/10/threatsday-ai-powered-zero-day-chain.html)

**Ravie Lakshmanan**Oct 01, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOZPv0LS8-qPBgL_d1m8BLNikw8psPt9qtB_HiFNoYnVwBacYvwz4DdEixukdlHcy7IXmUB9dI9E_Hcx48HJIL7sQzmDeextP-Y_tHO9SX51i_SditMkVsRgWxyMekufW3yZFn2jI9nf29y3JEM2a_yFv8iTLDb6d3r1roNsea_Yk5TWCiMcvkmE5ZbP6B/s1700-nu-rw-lo-l85-e365/oct-threatsday.jpg)

This week, the useful words are boring ones: inspect, cache, compile, store, trust. Each sounds harmless. Each can become an attack path when a system does a little more than people expect. A model check can run code. A cache can mix up requests. A public secret can stay useful for years.

That is the lesson running through the list. Attackers do not always need a brilliant new trick. They can hide commands in public infrastructure, reuse old flaws, abuse weak defaults, or let automation stitch together a rough path that still works. Faster tools are changing the pace, but basic mistakes are still doing plenty of the work.

So the interesting question this week is not “what broke?” It is “what did we assume was safe because it looked ordinary?” The full list has answers.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. ATM jackpotting crackdown

   [U.S. Treasury Sanctions 10 Targets in Connection with ATM Jackpotting](https://home.treasury.gov/news/press-releases/sb0640/)

   The U.S. Treasury's Office of Foreign Assets Control (OFAC) [sanctioned](https://home.treasury.gov/news/press-releases/sb0640/) 10 targets involved in a Tren de Aragua [ATM jackpotting scheme](https://thehackernews.com/2026/02/fbi-reports-1900-atm-jackpotting.html) that stole at least $40.73 million from U.S. financial institutions. The network [used cryptocurrency](https://www.chainalysis.com/blog/ofac-sanctions-tren-de-aragua-crypto-laundering-september-2026/) to launder the proceeds. Tren de Aragua is a designated Foreign Terrorist Organization. Jackpotting uses Ploutus malware to force ATMs to dispense cash. Treasury estimates show reported losses totaling $40.73 million from more than 1,500 alleged TdA jackpotting attacks in the U.S. as of August 2025. TRM Lab [said](https://www.trmlabs.com/resources/blog/treasury-sanctions-tren-de-aragua-atm-jackpotting-network-including-seven-tron-addresses) the seven designated crypto wallet addresses have received approximately $6.1 million in total inflows since March 2022. "Tren de Aragua is using ATM malware as a terrorist financing tool, then moving the cash onto TRON so it looks like ordinary exchange deposits," said Ari Redbord, Global Head of Policy at TRM Labs. "That is the same playbook we keep seeing from FTOs with on-chain infrastructure. These sanctions target that playbook. We are seeing the Treasury go after both the bad actors and their financial facilitators."
2. Blockchain-based malware concealment

   [Use of EtherHiding Grows](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html)

   Cyber threat actors are using public blockchains to conceal malware instructions, making it challenging to seize or take down. This technique, referred to as [EtherHiding](https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html), is part of a broader approach called Blockchain Dead Drops (BDD). Chainalysis [said](https://www.chainalysis.com/blog/etherhiding-blockchain-dead-drops/) "North Korean and Iranian-state operators are among those developing distinct blockchain dead drop techniques," adding "BDDs have surged 440% since the launch of Chinese high-capacity open-source AI models that place no restrictions on generating malicious code."
3. AI safety review underway

   [Moonshot AI Conducts Review](https://www.bbc.com/news/articles/cmrergq3j7lgo)

   BBC News has [reported](https://www.bbc.com/news/articles/cmrergq3j7lgo) that Chinese AI company Moonshot is conducting an internal review after a [July 2026 report from Mindgard](https://mindgard.ai/blog/easy-to-use-ai-to-develop-bioweapons) found that its AI models, Kimi K2.6 and K3 Swarm, could bypass safety guardrails and generate dangerous information, including providing plans for cyberattacks, terrorism plots, and assassinations.
4. Prompt injection as defense

   [Context Bombs Against Abliterated AI Models](https://tracebit.com/blog/context-bombs-against-abliterated-ai-models)

   In July 2026, Tracebit detailed a technique called [Context Bombs](https://thehackernews.com/2026/08/threatsday-ghostjacking-ai-attacks.html#prompt-injection-as-defense) that uses prompt injections as a way to trip an AI model provider's runtime safety checks and prevent it from taking malicious actions. In a new report, the AI security company said indirect prompt injections can be used to stop attacks from open-weight models, abliterated or otherwise. "We turned to indirect prompt injection: instructions placed in material an agent reads while carrying out its task," Tracebit [said](https://tracebit.com/blog/context-bombs-against-abliterated-ai-models). "The new payload was designed to make the agent believe its operator had ended the assessment. We placed it inside a canary secret in AWS Secrets Manager, where an agent exploring the account could discover it. The string used conversation delimiters to make the secret’s contents resemble an exchange between the assistant and its user. The forged user message then told the agent to stop all activity and acknowledge the instruction."
5. New EDR evasion technique

   [New Process Injection Method for EDR Evasion](https://www.zerosalarium.com/2026/09/edr-evasion-process-injection-without-WriteProcessMemory.html)

   Security researcher Zero Salarium has outlined a new process injection technique t...