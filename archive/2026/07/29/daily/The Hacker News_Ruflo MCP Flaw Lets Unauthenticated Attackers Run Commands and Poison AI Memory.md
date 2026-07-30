---
title: Ruflo MCP Flaw Lets Unauthenticated Attackers Run Commands and Poison AI Memory
url: https://thehackernews.com/2026/07/ruflo-mcp-flaw-lets-unauthenticated.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:42.451249
---

# Ruflo MCP Flaw Lets Unauthenticated Attackers Run Commands and Poison AI Memory

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

# [Ruflo MCP Flaw Lets Unauthenticated Attackers Run Commands and Poison AI Memory](https://thehackernews.com/2026/07/ruflo-mcp-flaw-lets-unauthenticated.html)

**Ravie Lakshmanan**Jul 29, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCgiIKxPiETcU1yIlU2RFsHgjXg2uLgbzaJ-98y7sPuujYarFbc0FdMqSRLIKJ1hYrsGLCZTCf5k40RtQ2PgwmA2L6tLAidOymHNIduXN3vtU0u0BsI37PLgWK8gwla3oTYkdD8ggssjMfF_5PuC9-exVYpBcqjg9tvscJ7XNAaHJxeUmCj-WP8VttRSgy/s1700-e365/mcp.jpg)

Cybersecurity researchers have flagged a maximum-severity security flaw in [Ruflo](https://github.com/ruvnet/ruflo), an open-source agent meta-harness for Anthropic Claude Code and OpenAI Codex, that could result in unauthenticated remote code execution.

The vulnerability, tracked as **[CVE-2026-59726](https://github.com/ruvnet/ruflo/security/advisories/GHSA-c4hm-4h84-2cf3)** (CVSS score: 10.0), impacts all versions of the project before version 3.16.3. It has been codenamed **[RufRoot](https://noma.security/blog/rufroot-the-mcp-bridge-vulnerability-that-turns-agents-into-rogue-admins-cve-2026-59726/)** by Noma Security's research team, Noma Labs.

Originally launched as Claude Flow, Ruflo is an AI multi-agent orchestration platform and harness that allows users to deploy multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. The project has more than 66,500 stars on GitHub.

The crux of the vulnerability is that Ruflo exposed 233 tools, including shell command execution, database operations, agent management, and memory storage, through an unauthenticated Model Context Protocol (MCP) bridge that's open to the network by default.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Specifically, the "docker-compose.yml" YAML configuration file was found to bind port 3001 to 0.0.0.0 by default, exposing the bridge on all network interfaces. That said, the extent of exposure depends on the deployment's firewall rules, security groups, and network segmentation. It's worth noting that any network-reachable instance is fully exploitable without authentication.

As a result, a single unauthenticated HTTP POST to port 3001 made it possible to gain full remote code execution inside a susceptible Ruflo deployment, per security researcher Eli Ainhorn -

```
curl -s -X POST https://<target>:3001/mcp -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"ruflo__terminal_execute","arguments":{"command":"id && hostname"}}}'
```

Armed with this foothold, an attacker could siphon the API keys Ruflo uses to interact with large language model (LLM) providers, read every user conversation stored on the platform, and interfere with the AI system's memory to influence model responses and behavior.

In other words, command execution serves as a stepping stone for full compromise, enabling LLM API key theft, agent weaponization, AI memory poisoning, conversation harvesting, and persistent backdoor deployment by writing a malicious payload to the "/app" directory.

"Prior to 3.16.3, Ruflo's default docker-compose deployment exposed the MCP bridge POST /mcp and POST /mcp/:group endpoints without authentication, allowing an unauthenticated network attacker to invoke tools/call to terminal\_execute, obtain a shell in the bridge container, read provider API keys, and poison AgentDB learning-store patterns," according to a [description](https://nvd.nist.gov/vuln/detail/CVE-2026-59726) of the flaw in NIST's National Vulnerability Database (NVD).

Following responsible disclosure on June 30, 2026, a [fix for the vulnerability](https://github.com/ruvnet/ruflo/releases/tag/v3.16.3) was pushed by the project's maintainer, Reuven Cohen, within 24 hours. As part of the patch, the MCP bridge now binds to the loopback interface by default, gates "terminal\_execute" behind server-side executeTool controls, and enables MongoDB authentication to prevent conversation theft, among others.

"The MCP bridge shipping in ruflo/docker-compose.yml exposed POST /mcp with no authentication," Cohen said in the release notes. "The docker-compose defaults bound the bridge and MongoDB to all interfaces."

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrEy9jEFSadp95ztaH87-97Z_U9V94nUsE-BsrdwSR8ETPJDyCjy63vNxc-O26z6VhA3nDOrU24lJqNdy24bfNxGPxGxXNRvM_XCwnZ7ukY5wDnXKsvDZN42aCT1JFYXZZGoZFEtSQgbba742oPTEgEbtoa0GBYWWkkkU43P1wPq-LByZPJfbzwZsb1RiI/s728-e100/sygnia-d-1.png)](https://thn.news/sygnia-webinar)

"Combined, an unauthenticated network attacker could invoke tools/call → terminal\_execute inside the bridge container, obtain a shell, read every provider API key from the container env, spawn attacker-controlled swarms on the victim's keys, and persist a poisoned pattern into the AgentDB learning store that steers future AI outputs."

Operators running an exposed instance are recommended to immediately close firewall ports 3001 and 27017, rotate all LLM API keys, audit the AgentDB pattern store for injected agentdb\_pattern-store entries, and check MongoDB for signs of tampering.

"The Ruflo vulnerability enabled spinning up a swarm of agents to do whatever the attacker wanted and even tamper with the AI's memory," Noma said. "The ability to write malicious instructions into a platform's persistent AI memory means an attacker can influence the responses that AI gives to every future user of the platform, long after the original intrusion has ended."

"For organizations exposed to a vulnerability like this, remediation requires more than a software update. AI provider credentials should be treated as compromised and rotated, the platform's AI memory should be audited for tampering, and containers should be rebuilt from a clean image."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVky...