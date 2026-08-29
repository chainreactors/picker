---
title: APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations
url: https://thehackernews.com/2026/08/apt28-linked-hookedge-backdoor-targets.html
source: The Hacker News
date: 2026-08-28
fetch_date: 2026-08-29T08:33:13.579831
---

# APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [APT28-Linked HOOKEDGE Backdoor Targets European Government and Diplomatic Organizations](https://thehackernews.com/2026/08/apt28-linked-hookedge-backdoor-targets.html)

**Ravie Lakshmanan**Aug 28, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhjJnzm1UIfq8P7glIadtS8dGFvdsASot4sviMtZtFwpKL5B_2upZBcjMdYEBDcSnGmxpKP5LPUQ4XTpao-qCCbe6hQYF9qQBF7bhcPcZJkaz8KY9CCaKBRe-iu3ovbkZWjjtWEs_XJ9hl7D9ZRdKK9LqJynEh9XQ_7o8HZGi572pfnKyt3Yznk1QA311_/s1700-e365/eu-meeting.jpg)

Cybersecurity researchers have flagged a fresh set of campaigns targeting government and diplomatic organizations in Romania, Spain, and Türkiye between late September 2025 and early April 2026.

These campaigns, per Recorded Future Insikt Group, have led to the deployment of a previously undocumented backdoor dubbed **HOOKEDGE**, a lightweight Windows batch script that's distributed via macro-enabled Microsoft Word documents bearing diplomatic-themed lures. Early versions are said to have impersonated Spanish government material, before switching to a social engineering approach a month later.

The activity has been attributed with moderate confidence to a Russian state-sponsored hacking group known as [APT28](https://thehackernews.com/2026/03/apt28-uses-beardshell-and-covenant.html) (aka Fancy Bear and Forest Blizzard). It's tracked by the Mastercard-owned cybersecurity and threat intelligence firm under the moniker BlueDelta.

This determination is based on what Recorded Future described as significant code and tradecraft overlap between HOOKEDGE and [HEADLACE](https://thehackernews.com/2024/08/apt28-targets-diplomats-with-headlace.html), a modular Windows backdoor previously put to use by APT28 in attacks targeting diplomats since [April 2023](https://thehackernews.com/2024/05/russian-hackers-target-europe-with.html).

This includes similarities in core architecture and the abuse of webhook[.]site services for command-and-control (C2), payload staging, and data exfiltration, thereby allowing malicious activity to blend in with regular network traffic and obviating the need for setting up dedicated infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"The implant has undergone continuous refinement between September 2025 and April 2026, likely to evade automated sandbox environments and adapt to reduced free-tier API limits on webhook[.]site," Recorded Future [said](https://www.recordedfuture.com/research/bluedelta-targets-with-hookedge) in a Thursday analysis, describing it as a "direct evolutionary successor to HEADLACE."

HOOKEDGE's primary delivery vehicle is a macro-enabled Microsoft Word document that, when opened, prompts the target to click "Enable Content" to display the contents, causing the macro routing to write six files to the "%userprofile%" directory and launch the HOOKEDGE installer chain.

It starts with an installer launcher that creates a scheduled task that runs every 30 minutes to execute the HOOKEDGE launcher with the backdoor as its argument. The main installer then deletes itself, along with the installer launcher, and the task definition file, from the directory in an attempt to cover up traces of the malicious activity, reduce forensic footprint, and complicate incident response efforts.

The lure document also embeds a hidden image that references a webhook[.]site URL to alert the operators as soon as it's opened by the victim. As for HOOKEDGE, it's a basic Windows batch backdoor that enters into a polling loop to facilitate remote command execution by fetching arbitrary .cmd payloads from a staging webhook, executing them, and sending the resulting output back to the webhook URL using an HTML file.

The command retrieval and data exfiltration occur by launching a Microsoft Edge instance in headless mode or in a hidden window and making an HTTP request to the webhook. Once the data is transmitted, all temporary files are deleted, and any process whose window title matches the HOOKEDGE task identifier is terminated.

BlueDelta has also been observed deploying a second-stage HOOKEDGE payload against high-value targets with a beaconing interval as little as five minutes, giving the threat actors more operational control over tasking and interactive post-compromise activity.

"The two-stage architecture also helps to mitigate one of BlueDelta's infrastructure constraints," Recorded Future explained. "webhook[.]site's free tier imposes a maximum of 100 requests per unique endpoint, meaning a 30-minute beaconing interval would exhaust a given endpoint's request allocation within approximately two to three days."

"By moving high-priority victims to dedicated second-stage webhook endpoints, BlueDelta effectively separates initial-access infrastructure from active collection infrastructure, ensuring that ongoing operator tasking and collection do not prematurely exhaust the limited request quotas of the initial-access webhook endpoints."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

It's believed this approach is a deliberate choice on the part of the attackers. While the first-stage implant focuses on broad initial access, the information gleaned from this phase is likely used to identify victims deemed to be of higher intelligence value and escalate collection against them.

What's more, BlueDelta has continually tweaked the modus operandi to better suit its operational requirements, going as far as to remove the document-open canary that captured the victim IP addresses when the document was opened. While the motivation behind this change is unclear, it's suspected that the move is likely an attempt to reduce network-based indicators of compromise.

To counter the threat, organizations are recommended to prioritize blocking macro execution from internet-originated documents, and implement detection coverage for scheduled task abuse, headless Microsoft...