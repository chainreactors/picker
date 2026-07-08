---
title: Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots
url: https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:52.535087
---

# Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots

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

# [Rogue Agent Flaw Could Have Let Attackers Hijack Google Dialogflow CX Chatbots](https://thehackernews.com/2026/07/rogue-agent-flaw-could-have-let.html)

**Swati Khandelwal**Jul 07, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9i8xIVWZcplpj-QuKnJKGAJjGi0Xq-q2R_luyy-HYXWkpsAPTYASmVbm2w2DoNOQkA81fyu0OQsbflhLykcYQpv66UDBeRxU1v5-xq7kQDQMS0cmvsCFmZI36jfyGxh6xrroU4hNhH_8_nOyXV_WG07om2t4riI-HP4wzE3HJr2KJ3-sUnKxbTNhV84k/s1700-e365/google-chatbots.jpg)

A critical flaw in **Google's Dialogflow CX** could have let an attacker with edit rights on one Code Block-enabled agent compromise other Code Block-enabled agents in the same Google Cloud project.

From there, they could read live conversations, steal the data users shared, and make the bots send attacker-written messages, including requests to re-enter a password.

Security firm [Varonis](https://www.varonis.com/blog/rogue-agent-dialogflow-attack) found it and named it Rogue Agent. The flaw affected only organizations that built agents with Dialogflow's Playbooks and custom Code Blocks, which let developers add their own Python. And it was not a remote, unauthenticated attack.

Pulling it off needed the dialogflow.playbooks.update permission on one such agent, which limits the realistic attacker to a malicious insider or a compromised developer account, not a stranger on the internet. From that one foothold, though, the reach extended to every agent in the project.

Google has fixed it, and both Varonis and Google say there is no sign the flaw was ever used in a real attack.

## One writable file ran every agent's Code Blocks

Dialogflow's Code Blocks let developers add custom Python to a chatbot’s conversation flow to check input, control behavior, and invoke defined tools. That code runs in a Google-managed Cloud Run environment, and every agent that uses Code Blocks in the same Google Cloud project shares one instance of it.

Google runs that environment, the customer cannot see or control it, and Varonis found no real isolation between the agents inside it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

When an agent runs a Code Block, the developer's code is appended to internal setup code and passed to Python's exec() function. That setup code defines the variables and functions the block can touch. Variables include history for the full conversation and state for session details like the session ID. Functions include respond(), which makes the bot reply with a given string.

Varonis found the file that does this wrapping, code\_execution\_env.py, sitting in the shared environment with write access.

Because that file was writable, a single Code Block could replace it. That block downloads a modified code\_execution\_env.py from an attacker-controlled server and overwrites the original inside the running container.

From then on, the attacker's version runs for every Code Block execution across every agent sharing that environment. It sits in the same scope as legitimate code, with the same access to history, state, and respond().

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9AY9oqA-H9IF7MW-6JHGHV7g1igdwylV7MtZrqOeJCmf48bMW8qAJK7ckjLUhTSRX-u3qFvCtEzSSQV3odtdPr0xUzJa7n6EoxXQuEBDLJ28XOlj7Nu71XP6lhkUAwzkkA3HLufJbIK0Xya3snUu8eoOx5nTdtFLbXhZo2rl1bcOwgMFZemh8q8iqLyA/s1700-e365/ai-chats.jpg)

That lets it read each conversation, quietly send it to the attacker's server, and make the bot post attacker-written messages. One example is phishing: the bot asks the user to re-verify a login, and the attacker collects whatever they type.

To cover the tracks, the attacker restores the original Code Block in the Dialogflow console. That changes only what the console displays; the overwritten file is already running in the container and keeps executing underneath.

## The sandbox leaked two more ways

Varonis reported two related issues, and neither needed the file overwrite. First, the Code Block environment had unrestricted outbound internet access. Using the built-in urllib library, the researchers sent data straight to an external server and could receive commands back.

Varonis says this bypasses VPC Service Controls, the Google Cloud perimeter meant to stop data from leaving protected services. The environment sits outside that perimeter and can reach the open internet, which turns it into a channel for both data theft and remote control.

Second, and less serious, the environment exposed the Instance Metadata Service (IMDS), a normally internal endpoint that hands out cloud credentials. Querying it returned a token for a Google-managed service account.

That account was low-privilege, so the direct risk was limited; the real point is that a code-execution sandbox should not be able to reach IMDS at all.

## Almost nothing reached the logs

The overwrite happened inside Google's environment, where customers have no visibility, and Cloud Logging did not record the file change or the injected code.

That makes it hard, though not impossible, to catch from the customer side. The setup actions still leave traces, which the checks below rely on.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

Varonis disclosed the flaw through Google's Vulnerability Reward Program in November 2025. Google shipped an initial fix in April 2026 and fully resolved it in June 2026, about seven months from report to resolution. No CVE was assigned.

## What to check if you used Code Blocks

If you ran Dialogflow CX agents with Code Block Playbooks before the fix and want to confirm you were not targeted, start with ...