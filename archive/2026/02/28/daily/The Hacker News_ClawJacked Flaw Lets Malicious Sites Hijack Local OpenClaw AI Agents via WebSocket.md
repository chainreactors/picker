---
title: ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket
url: https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html
source: The Hacker News
date: 2026-02-28
fetch_date: 2026-03-01T04:28:18.328050
---

# ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket](https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html)

**Ravie Lakshmanan**Feb 28, 2026Artificial Intelligence / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMEZ7gMViZ9XlXs35FiyviBZR19FbDXmatfjhNRw59daWLw41ScorGKG3xXYWFD6dDuYHajwoUnkWgQV9SrPe9iiV8UqDVjw4K5hX8cng7VDPTsljAZazuxUDdk7_hZ7SFV9rDCxNcYNWjmEY_lUVj01-PEI9D9rY5tMYJZTP5X887UuXOsDD90UOvo_mG/s1700-e365/opem.jpg)

OpenClaw has fixed a high-severity security issue that, if successfully exploited, could have allowed a malicious website to connect to a locally running artificial intelligence (AI) agent and take over control.

"Our vulnerability lives in the core system itself – no plugins, no marketplace, no user-installed extensions – just the bare OpenClaw gateway, running exactly as documented," Oasis Security [said](https://www.oasis.security/blog/openclaw-vulnerability) in a report published this week.

The flaw has been codenamed **ClawJacked** by the cybersecurity company.

The attack assumes the following threat model: A developer has [OpenClaw](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html) set up and running on their laptop, with its [gateway](https://docs.openclaw.ai/cli/gateway), a local WebSocket server, bound to localhost and protected by a password. The attack kicks in when the developer lands on an attacker-controlled website through social engineering or some other means.

The infection sequence then follows the steps below -

* Malicious JavaScript on the web page opens a WebSocket connection to localhost on the OpenClaw gateway port.
* The script brute-forces the gateway password by taking advantage of a missing rate-limiting mechanism.
* Post successful authentication with admin-level permissions, the script stealthily registers as a trusted device, which is auto-approved by the gateway without any user prompt.
* The attacker gains complete control over the AI agent, allowing them to interact with it, dump configuration data, enumerate connected nodes, and read application logs.

"Any website you visit can open one to your localhost. Unlike regular HTTP requests, the browser doesn't block these cross-origin connections," Oasis Security said. "So while you're browsing any website, JavaScript running on that page can silently open a connection to your local OpenClaw gateway. The user sees nothing."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"That misplaced trust has real consequences. The gateway relaxes several security mechanisms for local connections - including silently approving new device registrations without prompting the user. Normally, when a new device connects, the user must confirm the pairing. From localhost, it's automatic."

Following responsible disclosure, OpenClaw pushed a fix in less than 24 hours with [version 2026.2.25](https://github.com/openclaw/openclaw/releases/tag/v2026.2.25) released on February 26, 2026. Users are advised to apply the latest updates as soon as possible, periodically audit access granted to AI agents, and enforce appropriate governance controls for non-human (aka agentic) identities.

The development comes amid a broader security scrutiny of the OpenClaw ecosystem, primarily stemming from the fact that AI agents hold entrenched access to disparate systems and the authority to execute tasks across enterprise tools, leading to a significantly larger blast radius should they be compromised.

Reports from [Bitsight](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances) and [NeuralTrust](https://neuraltrust.ai/blog/openclaw-moltbook) have detailed how OpenClaw instances left connected to the internet pose an expanded attack surface, with each integrated service further broadening the blast radius and can be transformed into an attack weapon by embedding prompt injections in content (e.g., an email or a Slack message) processed by the agent to execute malicious actions.

The disclosure comes as OpenClaw also patched a log poisoning vulnerability that allowed attackers to write malicious content to log files via WebSocket requests to a publicly accessible instance on TCP port 18789.

Since the agent reads its own logs to troubleshoot certain tasks, the security loophole could be abused by a threat actor to embed indirect prompt injections, leading to unintended consequences. The [issue](https://github.com/openclaw/openclaw/security/advisories/GHSA-g27f-9qjv-22pm) was addressed in [version 2026.2.13](https://github.com/openclaw/openclaw/releases/tag/v2026.2.13), which was shipped on February 14, 2026.

"If the injected text is interpreted as meaningful operational information rather than untrusted input, it could influence decisions, suggestions, or automated actions," Eye Security [said](https://research.eye.security/log-poisoning-in-openclaw/). "The impact would therefore not be 'instant takeover,' but rather: manipulation of agent reasoning, influencing troubleshooting steps, potential data disclosure if the agent is guided to reveal context, and indirect misuse of connected integrations."

In recent weeks, OpenClaw has also been found susceptible to multiple vulnerabilities ([CVE-2026-25593](https://github.com/openclaw/openclaw/security/advisories/GHSA-g55j-c2v4-pjcg), [CVE-2026-24763](https://github.com/openclaw/openclaw/security/advisories/GHSA-mc68-q9jw-2h3v), [CVE-2026-25157](https://github.com/openclaw/openclaw/security/advisories/GHSA-q284-4pvr-m585), [CVE-2026-25475](https://github.com/openclaw/openclaw/security/advisories/GHSA-r8g4-86fx-92mq), [CVE-2026-26319, CVE-2026-26322, CVE-2026-26329](https://www.endorlabs.com/learn/how-ai-sast-traced-data-flows-to-uncover-six-openclaw-vulnerabilities)), ranging from moderate to high severity, that could result in remote code execution, c...