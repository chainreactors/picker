---
title: Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps
url: https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html
source: The Hacker News
date: 2026-08-18
fetch_date: 2026-08-19T03:00:28.458792
---

# Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps

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

# [Microsoft Copilot Personal Flaws Could Let One Click Exfiltrate Data From Connected Apps](https://thehackernews.com/2026/08/microsoft-copilot-personal-flaws-could.html)

**Swati Khandelwal**Aug 18, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjAc2Z6RvtNlJnjkfp-kCEhx8x8Q9XPLHY-oQb8NXu6cb-C5BTfa9HnmWq3G1GT3mPsHLV6Xf6tyBui-ljplsYEo9Qt8kBiNKXOwvTzACMisyS0NQ5U3bGg8O6yVEPStEPbYw4W-4ZasDNssDr2JTJD7GTo6QEpER1L-9Xci-mNSk3A5t_aLXGIHwo04FI/s1700-e365/copilot.jpg)

Varonis Threat Labs has disclosed three vulnerabilities in Microsoft Copilot Personal that it said could allow a single click on a crafted link to silently pull data from connected apps and other information available to the victim's Copilot session.

The flaws, which the researchers collectively named **CoSnitch**, turn in part on an undocumented URL parameter that the assistant itself surfaced during testing.

The company said it reported the issue to Microsoft in December 2025 and that patches shipped on August 18, 2026.

CoSnitch is tracked as **[CVE-2026-24301](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-24301)** in Microsoft's Security Update Guide. The research names Copilot Personal, the consumer assistant hosted at copilot.microsoft.com, and does not state that the same behavior affected Microsoft 365 Copilot.

The researchers said they found no evidence that CoSnitch was exploited in the wild. They reached the parameter by repeatedly asking Copilot why a prompt could not be made to run without user interaction, an approach the firm calls meta-hacking. Each refusal carried a technical justification, and the assistant eventually named a parameter, autorun=1, along with the session conditions under which it worked and the protections that were supposed to have disabled it.

When the researchers built the URL exactly as described, the parameter Copilot had said no longer worked executed. Copilot "wasn't breached; it was played," Varonis [said in its report](https://www.varonis.com/blog/cosnitch).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The attack URL pairs autorun=1 with the existing q parameter. In the CoSnitch report, Varonis said q alone only pre-fills the input box and that both parameters must be present for the prompt to fire without a user gesture.

Its earlier [Reprompt research](https://thehackernews.com/2026/01/researchers-reveal-reprompt-attack.html) also used q as the Parameter-to-Prompt entry point in a one-click attack. Varonis said that once CoSnitch execution begins, the prompt runs to completion even if the victim closes the Copilot tab immediately after the page loads.

Varonis grouped the findings into three vulnerabilities. The first two form the one-click exfiltration path, while the third is a separate memory-poisoning path triggered through web summarization:

* **Automatic prompt execution.** The two parameters together cause an attacker-supplied prompt to run on page load inside the victim's authenticated session, with the same capabilities as an instruction the user typed.
* **Exfiltration through connected services.** The injected prompt can query services the user has already authorized, encode retrieved data, and use [Copilot's built-in URL fetch](https://thehackernews.com/2026/02/researchers-show-copilot-and-grok-can.html) to send it to an attacker-controlled webhook. The technique does not grant Copilot new provider permissions or expand the user's existing access.
* **Persistent memory writes from summarized pages.** Separately, a crafted web page, when summarized by Copilot, can cause the assistant to write attacker instructions into the user's memory store, where they can shape later sessions.

In testing, the researchers said Copilot returned message bodies, subject lines, and sender and recipient metadata from connected mail accounts, calendar titles, attendees, times, and locations, file names and metadata summaries from Google Drive, full prior conversation content from chat history, and the saved instructions and user-defined rules held in the memory store.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZG4Rn8yHh2oJvh8x1RoKBmJ8ex08ojHhjv2VyoO8id2mKXvZha79jHrTmvaALaYSx0AXekr6iT9vKA4FbgmZP8jKs7g5cNqX-4EOlPCRoxVu4Px5zN9uRBBOPDX2iTSlSt1Hv5ETFQ8LQEE6-np__foGyIH8jxMURCtrhDcViXTdGfbC6p0_X3xQnQpw/s1700-e365/co-data.jpg)

Microsoft's [connector documentation](https://support.microsoft.com/en-us/microsoft-copilot/connecting-microsoft-copilot-to-other-services) says users must authorize services before Copilot can access them and that connected services process requests using the user's existing permissions. Microsoft says Copilot does not expand that access and only works with content the account already has permission to view.

Varonis said the exfiltration request is indistinguishable at the network layer from the fetches Copilot performs when it summarizes an ordinary web page, and that base64 encoding can help avoid filters scanning outbound requests for sensitive patterns such as credentials.

On the separate memory path, the firm said an injected instruction survives password changes, session revocation, and device re-enrollment, and stays active in later conversations until the user deletes it from Copilot's memory settings.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Varonis also said the memory write produces no process, file, network connection, or log entry that security tooling would flag, with the change visible in Copilot's memory interface.

The web summarization path is not the first time Copilot memory has been reported to Microsoft. Researcher [Håkon Måløy](https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html) [documented](https://enklypesalt.com/posts/context-collapse-part1-poisoning-copilot-memory/) an attacker-controlled page that persist...