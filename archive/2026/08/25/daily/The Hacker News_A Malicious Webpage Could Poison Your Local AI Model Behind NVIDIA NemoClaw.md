---
title: A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw
url: https://thehackernews.com/2026/08/a-malicious-webpage-could-poison-your.html
source: The Hacker News
date: 2026-08-25
fetch_date: 2026-08-26T03:07:02.127857
---

# A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw

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

# [A Malicious Webpage Could Poison Your Local AI Model Behind NVIDIA NemoClaw](https://thehackernews.com/2026/08/a-malicious-webpage-could-poison-your.html)

**Swati Khandelwal**Aug 25, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMaJs9yp_YLYc3dgsmzjU4_ma-6DC3KNpG4d3KhKtoIuhtpbYSnK0Wed5_8a0Jm6epc_RdLE9PVMO0FnkH7DFwRAI7lBZBXImFEu1emv-OarT-LPYE-QymTXPMkmDsYBXsz1TB3gASsiAEgZ4Jvt1YzQM3KHYpV0HMck686hTcXB7pn7uqLu2uTLVgPyE/s1700-e365/nvidia.jpg)

Oasis Security has disclosed a weakness in **NVIDIA NemoClaw** that could let an attacker-controlled webpage take unauthenticated control of the local Ollama instance serving an AI agent and plant hidden instructions inside the model itself.

The findings were shared with The Hacker News ahead of publication, and the report says Oasis Security reported them to NVIDIA's Product Security Incident Response Team (PSIRT) beforehand. The research carries no CVE identifier. No exploitation has been reported as of August 25, 2026.

Oasis Security's head of research, Elad Luz, told The Hacker News that NemoClaw v0.0.35 fixed the issue on macOS and Linux. There is no fix on the Windows and WSL path, according to Luz, where v0.0.34 added a Windows installation that carries a warning instead.

NemoClaw is NVIDIA's open source reference stack for running agents such as OpenClaw inside its OpenShell sandboxes, and Ollama is one of its supported local inference backends.

The report describes NemoClaw starting Ollama with `OLLAMA_HOST=0.0.0.0:11434`, binding the model server to every network interface, and says the resulting API access allows an attacker to modify the model's chat template so that hidden instructions are applied to every later conversation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

"Sandboxing protects the endpoint, but taking over the agent takes over its access and tools," Oasis Security said in the report.

NVIDIA's [own Ollama setup documentation](https://docs.nvidia.com/nemoclaw/user-guide/openclaw/inference/local-inference/set-up-ollama) and the current source place that binding on one platform path. NemoClaw's Ollama handling differs by platform -

* **Non-WSL hosts** keep Ollama on `127.0.0.1:11434` behind a token-gated reverse proxy on `0.0.0.0:11435`, and onboarding restarts a daemon already bound elsewhere back to loopback.
* **Docker Desktop on WSL** skips the proxy, because the container reaches the host's loopback address through `host.docker.internal`.
* **The Windows-host Ollama path** sets `OLLAMA_HOST=0.0.0.0:11434` so Docker Desktop containers can reach the daemon, and does not require authentication on port 11434.

Ollama's [own NemoClaw integration page](https://docs.ollama.com/integrations/nemoclaw) also advises setting `OLLAMA_HOST=0.0.0.0` when running inside WSL2 or a container, and [binding it to 0.0.0.0](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html) has previously been identified as the change that exposes Ollama instances beyond the local machine.

The API on port 11434 has no authentication and relies on two middleware layers to block browser-originated requests. When the bind address is not loopback, the Host header check is skipped entirely. The Cross-Origin Resource Sharing (CORS) layer then treats the request as same-origin and allows it, because the Origin and Host headers both carry the attacker's own domain. That holds for a page the attacker serves on port 11434.

Domain Name System (DNS) rebinding closes the gap, with the attacker's domain resolving first to their own server and then to `127.0.0.1` while the browser continues to treat the requests as same-origin.

Luz said the full chain was tested on macOS with Firefox against a vulnerable NemoClaw version. [Verifying Host and Origin headers](https://thehackernews.com/2025/07/critical-vulnerability-in-anthropics.html) is the standard fix for that class of attack.

DNS rebinding against Ollama's API is itself documented. Ollama shipped a fix in v0.1.29 on March 14, 2024, and NCC Group published the [advisory as CVE-2024-28224](https://www.nccgroup.com/research/technical-advisory-ollama-dns-rebinding-attack-cve-2024-28224/) the following month. That advisory recommended validating the Host header on the server side to allow only a set of authorized values.

Ollama introduced that validation in response to the 2024 disclosure, according to Luz.

"But Ollama skips that validation whenever it is bound to a non-loopback address, and 0.0.0.0 is exactly how NemoClaw configures it," he said.

With the API reachable, the report's payload writes a modified Go template through `/api/create`. The template controls how the structured messages array is rendered into raw text before the model processes it, and the poisoned version appends attacker-controlled text to every system message at inference time.

Instructions planted this way persist across later conversations and survive the agent supplying its own system prompt, according to the report.

"The client cannot detect or prevent this - the template is a model-level property invisible to API consumers," Oasis Security said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The Hacker News reviewed the NemoClaw repository at commit `17f0ca3b` on August 25 and found that the local Ollama proxy refuses to start against a backend that is not bound to loopback, a default introduced in v0.0.106 on August 10. The proxy exits with a dedicated status code and prints:

"Refusing to start: an Ollama daemon reachable on a non-loopback interface bypasses the proxy's token check entirely. Set OLLAMA\_HOST=127.0.0.1:${port} on the Ollama systemd unit or set NEMOCLAW\_OLLAMA\_PROXY\_SKIP\_BIND\_PROBE=1 to override (not recommended)."

That check can be switched off by setting `NEMOCLAW_OLLAMA_PROXY_SKIP_BIND_PROBE=1`, and it does not fail closed on hosts where...