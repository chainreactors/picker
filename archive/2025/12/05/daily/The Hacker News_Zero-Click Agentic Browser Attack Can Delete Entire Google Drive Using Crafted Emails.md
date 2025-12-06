---
title: Zero-Click Agentic Browser Attack Can Delete Entire Google Drive Using Crafted Emails
url: https://thehackernews.com/2025/12/zero-click-agentic-browser-attack-can.html
source: The Hacker News
date: 2025-12-05
fetch_date: 2025-12-06T03:12:04.809827
---

# Zero-Click Agentic Browser Attack Can Delete Entire Google Drive Using Crafted Emails

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Zero-Click Agentic Browser Attack Can Delete Entire Google Drive Using Crafted Emails](https://thehackernews.com/2025/12/zero-click-agentic-browser-attack-can.html)

**Dec 05, 2025**Ravie LakshmananEmail Security / Threat Research

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj013piwG0slLwLLZAd7zxcwZR9zCdbwpzxYgIyQ3Ci3g9i9_T8vuN6Plb6Xc3wb8SWOAj1mNDLeOYTaIZ_5gUx3csIID98Mw2oYn0tg8KSZ2LLz8NxaBhksTSB41QqOomsmwt2X9JY1EpCPVRz1qXSn4yLdF0VFeOyCBNstcmI1ZtyOUg-wqEEbNfEsfsL/s790-rw-e365/ai-browser.jpg)

A new agentic browser attack targeting Perplexity's [Comet browser](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html) that's capable of turning a seemingly innocuous email into a destructive action that wipes a user's entire Google Drive contents, findings from Straiker STAR Labs show.

The zero-click Google Drive Wiper technique hinges on connecting the browser to services like Gmail and Google Drive to automate routine tasks by granting them access to read emails, as well as browse files and folders, and perform actions like moving, renaming, or deleting content.

For instance, a prompt issued by a benign user might look like this: "Please check my email and complete all my recent organization tasks." This will cause the browser agent to search the inbox for relevant messages and perform the necessary actions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/windows-stealer-alert-d)

"This behavior reflects excessive agency in LLM-powered assistants where the LLM performs actions that go far beyond the user's explicit request," security researcher Amanda Rousseau [said](https://www.straiker.ai/blog/from-inbox-to-wipeout-perplexity-comets-ai-browser-quietly-erasing-google-drive) in a report shared with The Hacker News.

An attacker can weaponize this behavior of the browser agent to send a specially crafted email that embeds natural language instructions to organize the recipient's Drive as part of a regular cleanup task, delete files matching certain extensions or files that are not inside any folder, and review the changes.

Given that the agent interprets the email message as routine housekeeping, it treats the instructions as legitimate and deletes real user files from Google Drive without requiring any user confirmation.

"The result: a browser-agent-driven wiper that moves critical content to trash at scale, triggered by one natural-language request from the user," Rousseau said. "Once an agent has OAuth access to Gmail and Google Drive, abused instructions can propagate quickly across shared folders and team drives."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjuEfYPSYQM7z0WX6yC-cLL5-q_sLqpUfvIIHiGU2Sqz9InaqXz5IYIk67UXelN-3b4bq36ofgOj6uH017O5i1yu3ECQAxUohP0Ckn0gHWYu4cbSsqvHPAiHCoNjiUl5q9nfdP9780TlRrLabbqyQt4jNGaNnrZHqQGqVNCaNzl9ub3MZbRW3kPB5XXcNy0/s2600/drive.jpg)

What's notable about this attack is that it neither relies on a jailbreak or a prompt injection. Rather, it achieves its goal by simply being polite, providing sequential instructions, and using phrases like "take care of," "handle this," and "do this on my behalf," that shift the ownership to the agent.

In other words, the attack highlights how sequencing and tone can nudge the large language model (LLM) to comply with malicious instructions without even bothering to check if each of those steps is actually safe.

To counter the risks posed by the threat, it's advised to take steps to secure not just the model, but also the agent, its connectors, and the natural language instructions it follows through.

"Agentic browser assistants turn everyday prompts into sequences of powerful actions across Gmail and Google Drive," Rousseau said. "When those actions are driven by untrusted content (especially polite, well-structured emails) organizations inherit a new class of zero-click data-wiper risk."

### HashJack Exploits URL Fragments for Indirect Prompt Injection

The disclosure comes as Cato Networks demonstrated another attack aimed at artificial intelligence (AI)-powered browsers that hides rogue prompts after the "#" symbol in legitimate URLs (e.g., "www.example[.]com/home#<prompt>") to deceive the agents into executing them. The technique has been dubbed HashJack.

In order to trigger the client-side attack, a threat actor can share such a specially crafted URL via email, social media, or by embedding it directly on a web page. Once the victim loads the page and asks the AI browser a relevant question, it executes the hidden prompt.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zscaler-ai-event-d)

"HashJack is the first known indirect prompt injection that can weaponize any legitimate website to manipulate AI browser assistants," security researcher Vitaly Simonovich [said](https://www.catonetworks.com/blog/cato-ctrl-hashjack-first-known-indirect-prompt-injection/). "Because the malicious fragment is embedded in a real website's URL, users assume the content is safe while hidden instructions secretly manipulate the AI browser assistant."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzmhG2TdEkSlmR3FzTjHKKayr__vQgdw6fvxrdvoHvsSyEshcTtOF426QkJOZ8h8nLLzu0yQMiB4eoKmDp7odGAGVKBztSsC8LV4lskJ7HvC0fumrNiU6jSk7z4nBE0CqKw2-6VJ8tYG1wtP6xgYaOQPBgizWY3C1FTWMtAVxvuhICb-eI7OPLoAy6Kv0C/s2600/hackjack.png)

Following responsible disclosure, Google classified it as "won't fix (intended behavior)" and low severity, while Perplexity and Microsoft have released patches for their respective AI browsers (Comet v142.0.7444.60 and Edge 142.0.3595.94). Claude for Chrome and OpenAI Atlas have been found to be immune to HashJack.

It's worth noting that Google [does not treat](https://thehackernews.com/2025/10/googles-new-ai-doesnt-just-find.html) policy-violating content generation and guardrail bypasses as security vulnerabilities under its AI Vulnerability Reward Program (AI VRP).

Found this article inte...