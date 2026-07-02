---
title: Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls
url: https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:23.085100
---

# Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls

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

# [Anthropic Restores Claude Fable 5 After U.S. Lifts Jailbreak-Linked Export Controls](https://thehackernews.com/2026/07/anthropic-restores-claude-fable-5-after.html)

**Swati Khandelwal**Jul 01, 2026Artificial Intelligence / Critical Infrastructure

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2AmA92QCIqSJfXqC3z9I1jjdJGEkIvN4k-Oc5MlWZb4yZLPg5clokead6q8yXUfeI4DbdsKVn4qbd1sufvo47zyIy-Wcr15xK9oJJyet1vlFGiOKOU0ylMhgXWI0Duuztk7W_YURPKwdgfOyFsm2k3Rj1Db5tEVB9jzNi3xeYD0R_wfOaRKranmNj6kOy/s1700-e365/claude-fable-5.jpg)

Anthropic is putting **Claude Fable 5** back online worldwide. On [June 30](https://www.anthropic.com/news/redeploying-fable-5), the U.S. Commerce Department lifted the export controls it had imposed on Fable and its more tightly controlled sibling Mythos 5 about two and a half weeks earlier.

Fable 5 returns to users on Wednesday, July 1, across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork.

Export controls restrict who can receive or use a technology. The [June 12 order](https://thehackernews.com/2026/06/us-orders-anthropic-to-suspend-fable-5.html) told Anthropic to cut off both models for any foreign national, inside or outside the United States, including its own non-citizen staff.

The rule took effect at once, and the company had no reliable way to check every user's nationality in real time, so it shut both models down for everyone.

The trigger was a jailbreak: a prompt that gets a model to bypass its safety rules. Amazon researchers found one in Fable 5. By Anthropic's account, the prompt got the model to flag a few software flaws and, in one case, to write code showing how a flaw could be abused.

Anthropic played the finding down. It says the same requests work on plenty of weaker models too, including its own Claude Opus 4.8, OpenAI's GPT-5.5, and China's Kimi K2.7. The company calls the flagged behavior routine defensive security work, not a hidden super-capability.

The government and the partner that reported the jailbreak saw it as serious enough to justify emergency controls.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

To settle the concern, Anthropic trained a new safety filter, called a **classifier**, that watches for the exact technique in the report and blocks it. The company says it now stops that technique in more than 99% of tries, as of the June 30 write-up. Blocked requests get handed to the weaker Opus 4.8 instead, and the user is told. The trade-off is more false alarms on normal coding and debugging.

Mythos 5, the same underlying model with fewer safety guardrails, stays on a shorter leash. Access returned June 26 for roughly 100 U.S. companies and federal agencies that defend critical infrastructure. Anthropic says it is still working with the government to widen access.

Commerce Secretary Howard Lutnick, who signed off on the reversal, said his department had spent two weeks reviewing the models with Anthropic. In his letter, the company agreed to hunt for security problems on its own, coordinate on future launches, and report any malicious use it spots.

The negotiations were reportedly led by co-founder Tom Brown rather than CEO Dario Amodei, who has clashed with the administration for much of the year.

The fight was messy from the start. Multiple reports, including from The Wall Street Journal, said Amazon's research and concerns from CEO Andy Jassy helped drive the original order. Former AI czar [David Sacks](https://x.com/DavidSacks/status/2065853007619588171) accused Anthropic of having "prioritized the continued offering of the consumer model over safety." Others read it as an overcorrection.

University of Sydney AI governance researcher Francesco Bailo told Al Jazeera the reversal looked like the government conceding it had gone too far, and a group of security leaders had signed an open letter asking for the controls to be lifted.

Hanging over all of it was competition. The pause landed just as cheap, capable Chinese open-source models were gaining ground, and several executives warned that freezing U.S. models handed rivals free time to catch up.

Anthropic is also proposing something the industry has lacked: a shared way to rank how dangerous a jailbreak really is. With Amazon, Microsoft, Google, and other partners, it wants to score each one on four things:

* **Capability gain:** how much further the jailbreak takes a user beyond the tools they already have.
* **Breadth:** how many different attacks the same trick unlocks.
* **Ease of weaponization:** how much skill and effort it takes to turn it into a real attack.
* **Discoverability:** how easy the trick is to find or copy.

For the worst cases, such as a jailbreak that enables attacks on power grids or banks, Anthropic says it will start deploying fixes the moment severity is confirmed, and it is standing up a team to watch jailbreak reports around the clock.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqmM4NpfZsx4cw-HrXQlCjZQmrF8bYnmB23AmpOPi16kPNB9lvICjpdYEclxJwyQ9OE8GgzQ8aOEI68tRuxNqov0MHz2Sq8xEPiYWM3Js6FM5t2nm2JHWodmR7qVSot14ZtWVqQRQ6B88OnMaVxCPwRG7xGPoIIZxF6QAhWVhMkQfs11NjyNtHsGEUH4_q/s728-e100/sygnia-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

It also opened a [HackerOne program](https://hackerone.com/anthropic-cyber-jailbreak/) for researchers to report new Fable 5 jailbreaks, and promised the U.S. government earlier access to test future frontier models before release.

Anthropic is not the only lab in this position. Days earlier, OpenAI [previewed GPT-5.6](https://thehackernews.com/2026/06/openai-limits-gpt-56-rollout-as-sol.html) to a small, government-approved group rather than the public, citing the same dual-use worry: a model good enough to help defenders patch bugs is also good enough to help attackers find them.

The risk is not hypothetical. Earlier this spring, Anthropic tested a prior Mythos model tha...