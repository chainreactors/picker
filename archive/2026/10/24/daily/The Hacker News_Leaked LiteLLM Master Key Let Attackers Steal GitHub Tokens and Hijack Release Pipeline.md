---
title: Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline
url: https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html
source: The Hacker News
date: 2026-10-24
fetch_date: 2026-10-25T07:10:52.701475
---

# Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline

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

# [Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

**Ravie Lakshmanan**Oct 24, 2026Artificial Intelligence / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipiDo2Yur6TXZHLped9EQgORAH65rC4APGTaq_EZzlDnspAaULTQCKblBC0FeIah7nOCKTiQa2Oi8cyx-bbxHj042Km9oYAf2s78XmStFxzPBTSQ_oqv4ZcWGEkUP1wo5JfJ1UDrWQpAtz8ZHd9i3ZbGWWe8s6CMeUU_nObp5tCEywMWGovqFh9NA1H8Sv/s1700-nu-rw-lo-l85-e365/lite.jpg)

LiteLLM on Friday revealed that an Agent Platform master key accidentally published to a public GitHub repository in late May 2026 ultimately allowed the threat actor to [push a malicious version](https://thehackernews.com/2026/10/litellm-suspects-github-token-leak-in.html) of the popular Python package.

"On May 27, 2026, a configuration file was [committed](https://github.com/LiteLLM-Labs/lite-harness/blob/e10b14a/harnesses/opencode/opencode.json) to the public LiteLLM-Labs/lite-harness repository which inadvertently contained the master key to a deployment of the LiteLLM Agent Platform, an open source tool we use for orchestrating agents," LiteLLM's Oliver Jensen and Mateo Wang [said](https://docs.litellm.ai/blog/security-incident-oct-21-2026-attack-chain).

"The error was quickly identified, the commit force-pushed over, and we identified the exposed keys as requiring revocation. However, key revocation did not occur for the master key."

LiteLLM said the unknown attacker (operating from "69.48.229[.]143") used this unrevoked key on October 10, 2026, to gain access to the Agent Platform and extracted a GitHub CLI OAuth token the service was configured with to allow self-hosted cloud agents to file pull requests to GitHub repositories.

The token, per the developers of the open-source large language model (LLM) gateway, was "not scoped down" and associated with its GitHub organization owner's account.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Gaining access to the token allowed the attacker to possess owner-level access to all repositories across the organization and perform additional credential exfiltration. The sequence of actions performed by the threat actor following this step is as follows -

* **October 10, 2026, between 10:11 and 10:12 p.m. UTC:** Author commits into throwaway branches on internal repositories to run workflows (BerriAI/litellm and BerriAI/litellm-auto) designed to acquire GitHub CLI Oauth tokens associated with two engineers with maintainer privileges via an attacker-controlled webhook[.]site endpoint. The two runs are deleted minutes later.
* **October 21, 2026, between 10:08 and 11:08 a.m. UTC:** Override branch protection and alter the release pipeline with the source set to the lookalike repository "Berri-AI/litellm" rather than "BerriAI/litellm."
* **October 21, 2026, between 11:39 and 11:40 a.m. UTC:** LiteLLM version 1.107.0 gets published to PyPI.
* **October 21, 2026, 11:46 a.m. UTC:** Docker Hub and GHCR images are published.
* **October 21, 2026, between 11:53 and 11:54 a.m. UTC:** Production and staging run records are deleted.
* **October 21, 2026, 12:06 p.m. UTC:** Upwind researcher Lidor Machluf reports the supply chain attack.
* **October 21, 2026, 1:23 p.m. UTC:** PyPI quarantines LiteLLM version 1.107.0.
* **October 21, 2025, 2:20 p.m. UTC:** Docker Hub tags v1.107.0, latest, main-latest, and main-stable are removed or repointed to verified clean images.

"In typical operation, building and publishing a release requires being kicked off by an authorized engineer and being approved by a special account locked to a physical device in our office," LiteLLM said.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbaCgLf_HRbv4c5Z6gBruXsV9RF7QyoXK5oTf95H-lymYlKBcRzW_NhrOMNRmnDYt-pD6TJA5CBOU7UUoVzbJrVbtlUcEk9KulNqLp-46QTnrwAb36BUKxS91oFXvEwlpWa7Vfc4RwyTD-iUxnhU09ShFtoVZikcEI2KC8XdAsIKaTd7ypVLRjlPFT9TkG/s1700-nu-rw-lo-l85-e365/json.jpg) |
| Leaked master key in May 2026 |

"This restriction was relaxed earlier this week to accommodate the temporary push for more frequent releases and bugfix backports, allowing any two engineers to trigger and approve a release. As such, the threat actor used one of the tokens to trigger the release (after having repointed the deployer to their malicious repository), and another to approve it."

In addition, the project maintainers noted that the threat actor could have very well loosened this restriction (or removed it entirely) themselves given that they were already in possession of a token belonging to an organization owner. It's suspected that this was not done to evade detection.

LiteLLM also said the workflows are designed to identify and exfiltrate additional keys and tokens, specifically focusing on upstream inference API tokens. In response to the incident, the company said it's working to revoke each and every token associated with every internal system and vendor platform.

The findings rule out LiteLLM's initial hypothesis that the GitHub CLI OAuth tokens were stolen from the logs of an internal LiteLLM deployment. "The investigation was a process in which we continually learned additional information, meaning some of our assumptions and beliefs were later proven to be inaccurate or incomplete," Jensen [acknowledged](https://github.com/BerriAI/litellm/issues/47826#issuecomment-6374891275).

### More Details About the Workflows Emerge

Socket, which [published](https://socket.dev/blog/litellm-attack-timeline) its own investigation into the malicious workflows, said it recovered two malicious commits that each added a workflow at ".github/workflows/cache.yml." The first commit was made on October 10, 2026, at 10:11:45 p.m. UTC. It was followed by a second commit on October 12.

"Neither commit was pushed to a branch that still exists," Socket securit...