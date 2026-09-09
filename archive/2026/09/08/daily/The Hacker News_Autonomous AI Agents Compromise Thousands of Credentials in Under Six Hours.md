---
title: Autonomous AI Agents Compromise Thousands of Credentials in Under Six Hours
url: https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:58.470587
---

# Autonomous AI Agents Compromise Thousands of Credentials in Under Six Hours

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Autonomous AI Agents Compromise Thousands of Credentials in Under Six Hours](https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html)

**Ravie Lakshmanan**Sep 08, 2026Artificial Intelligence / Cybercrime

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdVKt_UmqEYNHNt0K516skza4MoV47hITqzcoC3WLLI3QkQ_jUEffHvaL7VHVtzRqvdt6k2bZwGAFVif-hRkoiTQva6JM95w3NgNRU_WpuTaZfhLGXAcOdLQXy_sMWU1dxAunMAsf7J8PEDG2AKvkFuXbOFyOmIQcaocMIBhNpaYscCUeJElKDXu6xGhkX/s1700-nu-rw-lo-l85-e365/ai-agent.jpg)

Threat actors are continuing to leverage artificial intelligence (AI) to [streamline their operations](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html), with one financially motivated hacking group employing an autonomous, multi-agent attack framework to carry out a large-scale credential harvesting campaign within six hours.

Google Threat Intelligence Group (GTIG) [said](https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai) it has observed attackers with diverse motivations targeting proprietary AI models across healthcare, government, and media sectors, exfiltrating API credentials, and co-opting victim cloud environments to sustain unauthorized AI workloads. This highlights [growing attacker focus](https://thehackernews.com/2026/09/cisa-adds-seven-exploited-flaws-as.html) on enterprise AI assets for espionage, extortion, and resource theft.

"At this point, we can assume that all threat actors are using AI in some capacity and their operations have benefited," John Hultquist, chief analyst at GTIG, said in a statement shared with The Hacker News. "Like everyone else, we're concerned about the vulnerability problem, but AI is being applied to several other areas, and it will be especially challenging as it is applied agentically, creating a scaled, faster adversary. Criminals, like the ones who conducted a mass exploitation campaign in just six hours, will gravitate to attacks that are faster than we can respond to."

Google noted that the integration of AI-assisted coding tools has not only accelerated software development cycles but also increased threat actors' targeting of developers, AI coding assistants, and LLM security scanning tools, thereby raising open-source supply chain risks.

This has been fueled primarily by a financially motivated threat actor known as TeamPCP (aka Altered Spider and UNC6780), which has conducted a series of large-scale software supply chain compromises targeting PyPI, npm, and Docker Hub. The initial compromise is followed by the deployment of credential stealers like SANDCLOCK and DUSTMAKER to obtain sensitive data and target AI coding assistants, which are then monetized either via direct sale or through partnerships with ransomware and data theft extortion groups.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

"DUSTMAKER is a successor to the SANDCLOCK credential stealer in TeamPCP operations," GTIG told The Hacker News. "SANDCLOCK (used in March and April 2026) is a component of what has publicly been referred to as [CanisterWorm](https://thehackernews.com/2026/03/trivy-supply-chain-attack-triggers-self.html), was primarily written in Python, and is designed to operate on Linux and interact with Kubernetes. It includes container escape functionality and targeted cryptocurrency wallets in addition to cloud and developer credentials."

"DUSTMAKER (used in April and beyond) is a cross-platform JavaScript payload optimized for CI/CD pipelines. It does not contain container escape functionality, and while some variants have targeted cryptocurrency wallets, its overall focus is credential theft to facilitate extortion operations. The AI-targeting techniques [...] – specifically the poisoning of AI assistant workspaces and the [use of prompt injection](https://thehackernews.com/2026/09/russia-aligned-uac-0099-plants-nuclear.html) for defense evasion – are exclusive to DUSTMAKER and were not present in earlier SANDCLOCK variants."

Elsewhere, Google said it detected instances where threat actors are misappropriating proprietary AI research and models -

* A China-nexus threat actor known as [UNC6508](https://thehackernews.com/2026/06/chinese-hackers-abused-google-workspace.html), which is suspected to have compromised cloud environments to deploy local LLM infrastructure that uses a local, open-weight model, as opposed to a commercial frontier model, thereby evading monitoring by AI model providers.
* Several data theft extortion operations in which threat actors have been observed stealing proprietary AI data, including models, skills, prompts, source code, and related research.
* Threat actors carrying out distillation attacks against Google's AI models that target its visual and audio understanding, image generation, and video generation capabilities.

Adversaries have also been observed ramping up use of agentic AI to facilitate malware and tooling development, with a China-aligned cyber espionage group leveraging Gemini to design and develop an automated penetration testing framework.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlLddknuw8aFvWAMpFrYulsOTQRkifYjek2UMtc_hUsbIObcW8I8efpDn1fWJ31v616vS_rju2zAfKEeN6KWzbznd8U-l_AUzvrPJjnnTCj2dFFizwV5aMHYyIQp5mzUHieOIw8To6EDsFtdwcJCOodVtXhcwh780eOiomQ26s6eVcTJ9VZL2WG6Th6JOd/s1700-nu-rw-lo-l85-e365/agents.png)

"The group sought to build an agentic architecture capable of observing target state, reasoning through actions, and executing tasks in unpredictable environments," Google said. "The planned agent was designed to perform discovery tasks such as port scanning and service parsing, demonstrating an intent to automate initial discovery and execution phases."

Another threat actor found engaging in similar efforts is believed to be financially driven. The activity involved the attacke...