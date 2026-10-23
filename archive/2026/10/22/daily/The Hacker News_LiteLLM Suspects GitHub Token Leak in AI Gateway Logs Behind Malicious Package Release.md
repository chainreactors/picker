---
title: LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release
url: https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:43.801965
---

# LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [LiteLLM Suspects GitHub Token Leak in AI Gateway Logs Behind Malicious Package Release](https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html)

**Ravie Lakshmanan**Oct 22, 2026Cloud Security / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiEKKMESHBCMBHXA8Yf_clmAeFQXSdaKTEz0t_6RDzj1zXcwiPxA4gy2MPmftM6vyCkoG7OsCZJ2a8t7xJe1qbn3tEWRZfVgStzQVJy0ZfwEkjhg6-A34iT3XnQG7nYku04cWbIaHwkQmuDVghCeJBx5xJcbtozsyD3Genw4wyxFtgWIVD-rRGRLMBKoq2/s1700-nu-rw-lo-l85-e365/litellm-breach.jpg)

LiteLLM on Wednesday [disclosed](https://docs.litellm.ai/blog/security-incident-oct-21-2026) that threat actors compromised "multiple independent security controls" to push a [malicious version of the Python package](https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html) containing a credential stealer and a backdoor.

On October 21, 2026, LiteLLM's release pipeline was [compromised](https://github.com/BerriAI/litellm/issues/47826) to push 1.107.0 to the Docker Hub registry and the Python Package Index (PyPI) repository. The incident took place around 4:00 a.m. PST. The following compromised versions were published -

* LiteLLM v1.107.0 (PyPI)
* v1.107.0, latest, main-latest, and main-stable (Docker)
* v1.107.0, latest, main-latest, and main-stable (GHCR)

Users who downloaded an unpinned version of LiteLLM between 11:39 a.m. and 1:23 p.m. UTC via pip or used the Docker image v1.107.0, latest, main-latest, or main-stable between 11:46 a.m. and 2:20 p.m. UTC are impacted.

The poisoned version [incorporated](https://research.jfrog.com/post/litellm-hijacked-again/) code to harvest credentials and keys, and run arbitrary code from a remote server every hour, turning it into a remote access trojan (RAT).

Specifically, the Python interpreter processes a path file ("cook.pth"), which includes a command to import "cook," a Python script ("cook.py") that deobfuscates itself and runs a stealer routine named "privcollect" to gather system, browser, developer, cloud, and AI tool secrets, and exfiltrate the data to "litellm[.]dev/healthcheck" via an HTTP POST request.

In addition, the interpreter attempts to execute "sitecustomize.py," which runs only on Linux and macOS machines, and is configured to fetch "domain.txt" from a now-removed GitHub dead drop ("github[.]com/letters9813"). Should this file return a valid response, the malware proceeds to download a second-stage Python script from "<domain>/codepy" and execute it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

"It forks a background daemon that acquires a lock at '/tmp/remote\_code\_loader.lock' to prevent multiple instances, then enters an infinite loop," Aikido researcher Ilyas Makari [said](https://www.aikido.dev/blog/litellm-compromised-infostealer-rat). "Every hour, the daemon fetches the attacker's current C2 domain from a GitHub repository (raw[.]githubusercontent[.]com/letters9813/pythonclient-test/main/domain[.]txt), then fetches and executes a Python payload from https://{domain}/codepy."

According to Google-owned cloud security subsidiary Wiz, the text file was only populated with initial test values prior to its takedown by GitHub around 1:30 p.m. UTC.

"The dual-technique approach, using both .pth files and sitecustomize.py simultaneously, appears to be the first documented case in the wild," Wiz researchers Benjamin Read and Rami McCarthy [said](https://www.wiz.io/blog/litellm-compromised-steals-credentials).

Wiz said it has since observed abuse of stolen credentials, starting about 4.5 hours post-exfiltration, with the attacker validating AWS instance role credentials captured from compromised CI runners and Kubernetes nodes from the following IP addresses between 4:20 p.m. and 5:01 p.m. UTC -

* 168.100.8[.]57
* 165.227.201[.]8

"Each credential was checked with sts:GetCallerIdentity, followed by bedrock:ListFoundationModels and a ListModels call, consistent with LLMjacking," Wiz added. "In a small number of environments, the attacker also enumerated IAM (ListRoles, ListUsers, ListAccessKeys) and performed general discovery (ListAccounts, DescribeTrails, etc.)."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimTJr-sZDOSzfHY1WBASwIEYbOhxD28x2tSVzpuOHP5XUIw9KcNjKgv8yzfsz2M1cYN9hHvq0PuUUjrbS-CzKVD_5DtoyrSWQMVvBGUibepXQWmEI_vSxveT8G3y5Wqz3hgy16Sp1W6G1u-M5T8t57sFqX-Afdlzcgytl9O7fVtYJbv9u44DqSDHh2VIvI/s1700-nu-rw-lo-l85-e365/llm1.jpg)

In an advisory published Wednesday, LiteLLM said it had hardened its release pipeline following a [similar incident](https://docs.litellm.ai/blog/security-update-march-2026) that [took place](https://www.trendmicro.com/en_gb/research/26/c/inside-litellm-supply-chain-compromise.html) earlier this March. This included moving releases to a private repository, making Docker release tags immutable, and signing Docker images.

However, after the open-source project maintainers temporarily expanded release permissions to allow two internal engineers to publish daily bugfix backports for customers, the attacker leveraged their access to three sets of developer GitHub CLI credentials to ultimately push a malicious version.

The entire sequence of actions is below -

* On October 19, 2026, LiteLLM temporarily expanded release permissions for two internal engineers.
* The attacker had access to three sets of developer GitHub CLI credentials, including one that had the ability to run GitHub workflows.
* The attacker used a token belonging to one of its GitHub organization owners to disable branch protections and force-push the malicious changes.
* The attacker ran the compromised workflow, pointing it to a lookalike repository "Berri-AI/litellm" instead of "BerriAI/litellm," causing the poisoned artifacts to be signed and published.

"After a thorough investigation, we have observed specific situations in which Claude Code will embed a user's GitHub CLI...