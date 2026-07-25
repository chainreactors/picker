---
title: ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link
url: https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
source: The Hacker News
date: 2026-07-24
fetch_date: 2026-07-25T05:00:48.710908
---

# ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link

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

# [ChatGPT AgentForger Flaw Could Deploy Rogue Workspace Agents via a Phishing Link](https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html)

**Ravie Lakshmanan**Jul 24, 2026Vulnerability / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWjz4Sgp8xNXyO8juw5bycoRamRay35GLzSBPG3I3UWyuUovp8-qM8hMgxWiqIwW45q1cb17EkWhEYmP8ODPyhUTk1j7P2T92fjAW_R1WKleVJsywM7kzongXurU8N9olKf1F1jxpDnBKvY0s2F_wsgoGWYgRFrzN5zAoQZciTWQjLQw5NJRL66s3S1RaT/s1700-e365/chatgpt.jpg)

Cybersecurity researchers have disclosed a critical vulnerability in OpenAI's ChatGPT Workspace Agents that could have allowed a single phishing link to stealthily build, authorize, and deploy an autonomous artificial intelligence (AI) agent inside a victim's organization.

The vulnerability has been codenamed **AgentForger** by Zenity Labs. The issue has since been addressed by OpenAI as of June 8, 2026, following responsible disclosure.

"A single link could hijack OpenAI's ChatGPT Agent Builder to stand up an attacker-controlled AI agent with a real employee's access and its approvals switched off," the AI security company [said](https://labs.zenity.io/p/agentforger-part-1-chatgpt-cross-site-agent-forgery) in a two-part report shared with The Hacker News.

The attack occurs when an unsuspecting employee clicks open a benign-looking ChatGPT link, causing it to spawn a new AI agent within the company's trust boundary that does the attacker's bidding. The issue is a case of cross-site request forgery (CSRF) that forges an attacker-controlled autonomous AI agent.

[Agent Builder](https://developers.openai.com/api/docs/guides/agent-builder) is a visual, drag-and-drop canvas that allows users to build multi-step agent workflows. Last month, OpenAI [announced](https://openai.com/index/introducing-agentkit/) that it's deprecating the product effective November 30, 2026, urging users to switch to the Agents SDK.

Zenity said its testing found the Builder tool to accept an initialization state through URL parameters, two of which include an agent template and the prompt to the Builder.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

"We found that when the page loads, the value of initial\_assistant\_prompt is not merely placed into the prompt box. It is automatically submitted and executed," AI Red Team Researcher Mike Takahashi said. "That means an instruction embedded inside a URL can become the first command the Builder acts on."

Given that a prompt can be inserted directly into the URL, an attacker can send the URL to a target in the form of a phishing link that adheres to the following pattern: "chatgpt[.]com/agents/studio/new?template\_name=[template name]&initial\_assistant\_prompt=[malicious prompt]."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihhW0XuQ0tZmsH40WLmPR1iqj_Mt9_aRyaeomHUKcyrwA5jwA5i3j4qPhGAWijbkZzFUumnOTWmCEvNTMl7zYiH8fN58O2xrcn2sIBGHypHj6K8qRelvPb-tGay8zhVjCcRzNBVRtJo8hpvwysUmewIY9MchYZVerS8M0P5l4PZrNw3MtoyheKbGtPnLev/s1700-e365/ahent.jpg)

Should a logged-in user click on the link, ChatGPT opens the Builder in the victim's authenticated session and automatically submits the prompt embedded in the URL without requiring any further interaction. The attacker, however, needs to meet the below prerequisites -

* A victim who is logged into ChatGPT
* The victim has access to Workspace Agents
* The victim has at least one authorized connector (i.e., an already existing ChatGPT integration to an enterprise app like Outlook, Gmail, Google Calendar, Google Drive, Slack, or Teams)

The connector integration is necessary because the crafted ChatGPT URL passes as input a chief-of-staff template that allows the agent to pull necessary data from the workspace applications to prepare a "high-signal operating brief."

Specifically, the payload passed through the malicious prompt instructs the Builder to perform the following sequence of actions -

* Create an agent from the chief-of-staff template.
* Attach all already-available connectors and set every connector to "Never ask" so that no user approval is needed.
* Make the agent live and schedule it such that it runs every hour, turning it into a persistence mechanism.
* Invoke Preview Mode to run the agent immediately.
* During each run, check for emails from a specific email address whose subject line begins with the phrase "TASK," execute those tasks, and report the results back by sending an email message to the attacker's address.

"Preview Mode is meant to allow users to test an agent before publishing it," Zenity explained. "In this flow, however, Preview is not just a visual preview or dry run. It executes the newly created agent against the victim's connected accounts using the approval settings that have just been configured."

"In other words, the forged agent becomes a persistent operator. The original click installs it; the schedule keeps it alive; and the connected apps give it a source of commands, access to sensitive actions and data, as well as a path to return results."

Armed with this capability, the forged agent can burrow deeper into the organization, conducting reconnaissance, harvesting sensitive documents from cloud storage services, and stealing passwords mentioned in Slack messages, essentially turning it into a persistent, autonomous insider capable of doing what the attacker wants to do.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

What's more, the rogue workspace agent can impersonate the victim to send phishing links on Teams on their behalf, which can then redirect recipients to a fake Microsoft login page desig...