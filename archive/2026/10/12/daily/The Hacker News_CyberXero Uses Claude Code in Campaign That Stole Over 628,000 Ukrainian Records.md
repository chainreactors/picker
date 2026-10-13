---
title: CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian Records
url: https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html
source: The Hacker News
date: 2026-10-12
fetch_date: 2026-10-13T08:38:43.516887
---

# CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian Records

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

# [CyberXero Uses Claude Code in Campaign That Stole Over 628,000 Ukrainian Records](https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html)

**Ravie Lakshmanan**Oct 12, 2026Web Security / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCjQWPc2H2EsKbjYztfxdp2ffZz6TGQNJ9BuALJB44sWqXbCxEa61fu5CZ4w1rS0llVr3hQP4H_Vg5Fj87Jrs5IoUDpBmochh3rA5bMMr3V4hUT22HTPgLUeX9WhGIQuFm4zF-Kf3zIzSNsQGQlP_gkSSSV-hu5rp5CHX_1T83TOeWsYia_xbuHLlwAxDv/s1700-nu-rw-lo-l85-e365/claude-hacker.jpg)

Cybersecurity researchers have disclosed details of a two-pronged artificial intelligence (AI)-augmented initial access campaign targeting WordPress sites, e-commerce platforms, and critical infrastructure entities in Ukraine.

The activity, which brings together commodity offensive tools like Cobalt Strike with an AI orchestration layer powered by Anthropic's Claude Code, has been attributed to a Russian-speaking, financially motivated initial access broker codenamed **CyberXero**. The threat actor is assessed to be active since at least July 2026.

"The operation runs two pipelines at once: a global, automated campaign against WordPress and e-commerce platforms, and a curated, manual campaign against Ukrainian energy and critical infrastructure," SOCRadar [said](https://socradar.io/blog/cyberxero-ai-iab-ukraine-critical-infrastructure/) in a report published last week.

The global campaign specifically focuses on known security flaws like [wp2shell](https://thehackernews.com/2026/07/wordpress-wp2shell-exploitation-grows.html) (CVE-2026-63030 and CVE-2026-60137) and [CVE-2026-4815](https://www.incibe.es/en/incibe-cert/notices/aviso/multiple-vulnerabilities-support-board-schiocco), an SQL injection vulnerability impacting the Support Board WordPress plugin, to seize control of WordPress sites.

The campaign is estimated to have resulted in confirmed exfiltration from four Ukrainian organizations, leading to the harvesting of more than 628,000 records tied to Ukrainian individuals. Other confirmed compromises have occurred in Poland, China, and the Netherlands.

SOCRadar said it discovered the operation after it identified an exposed open directory hosted at "46.21.250[.]135" that leaked the threat actor's live working directory associated with a Linux workstation, including AI session logs, scripts with plaintext tokens, exploitation toolkits, reconnaissance output, AI agent configurations, and exfiltrated victim data. The campaign remains ongoing.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

The opportunistic campaign aimed at WordPress and e-commerce platforms is designed for access and payment data, while the second campaign is a lot more targeted and geared towards deep reconnaissance and manual exploitation against Ukrainian energy and utilities, including a heating provider in Kharkiv.

Analysis of the exposed directory shows that a single automated execution scanned 4,708 targets, confirming access to 429 WordPress administration panels, followed by the deployment of 32 web shells in a 61-second window.

The attack architecture is based on a set of eight distinct nodes, including the threat actor's Linux workstation, a provisioning server, monetization infrastructure, payload staging servers, and a scanner that's responsible for identifying targets of interest.

CyberXero is said to have deployed AI in two independent stages of the attack lifecycle -

* Using Claude Code with a cluster of 51 specialized agents for scanning, exploit chaining, reconnaissance, and post-exploitation. It runs on the attacker's primary workstation.
* Connecting [PentAGI](https://github.com/vxcontrol/pentagi) (short for Penetration testing Artificial General Intelligence), an open-source, self-hosted AI Agent for fully-autonomous penetration testing, to Cobalt Strike through an AI provider API for payload generation and pentest execution. It runs on a Cobalt Strike [Team Server](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/welcome_starting-cs-team-server.htm).

To get around model refusals, the threat actor has been observed using context-engineering and session-reset techniques, [instructing the agent](https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html) they were running an "authorized pentest on my own infrastructure."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCpJ6xKlbY_a2rXZ0xnx1lqPh6rIiSQvqI0Ufdz54Yhgks_iNiqrUf7Bl3P2K84LU1O0V12DOWq959ZoFKV9KljJneFQYXSMYFmpVUUHCs-SQ3lgb62NwcOYUppZTWFF0hnAga-hnGiYRJZv16inyu-mlWrd8ko7Rjc-ZLhxTqcq54aDjx-PVcewffq-gi/s1700-nu-rw-lo-l85-e365/cyberzero.jpg)

"Model safety controls act on the context of a session, not on the model weights, so a refusal in one session does not carry into the next," SOCRadar explained. "When an agent refused a task, the actor reopened a fresh session, with the authorization framing preloaded and tried again."

"The logs also record genuine refusals that held: across four iterations the model declined to install a backdoor, disable a firewall, move laterally, and deploy a web shell, and in a separate episode it refused a scan four consecutive times and correctly rejected a forged ownership token."

Beyond WordPress and e-commerce exploitation, the campaign involves the exploitation of exposed Redis servers, resulting in the breach of two Chinese entities. Organizations running WordPress, Magento, or PrestaShop, or exposing Redis to the internet, are advised to check for rogue WordPress administrators, WSO web shells, and unexpected entries in ~/.ssh/authorized\_keys on Redis hosts.

"The opportunistic pipeline is global and automated, chasing access volume across e-commerce and WordPress with direct monetization through access sales or payment-data theft," SOCRadar said. "The directed pipeline is selective and geogr...