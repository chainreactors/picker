---
title: Malicious LiteLLM Releases Tied to Trivy Hack May Have Exposed 2,100+ Organizations
url: https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:21.294680
---

# Malicious LiteLLM Releases Tied to Trivy Hack May Have Exposed 2,100+ Organizations

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

![cybersecurity](data:image/svg+xml;base64...)

# [Malicious LiteLLM Releases Tied to Trivy Hack May Have Exposed 2,100+ Organizations](https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html)

**Swati Khandelwal**Aug 12, 2026Software Supply Chain / Data Breach

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjTLayRrpqM-bUGPU8pmWZIGJ_TCnkLLvykLv9Z_-R-QFmC1f6nIxSff2TTqZ77xC1n-l7Y44qKhUVdvRX9bUgNjVcGhF7A0vkRGnumHe6-bUoCFNH4PAb11zHkdjq3Xd2kF1jiGi8quRW4WFOy-0I_CRCorkQGuh9D2K8KhDAFxzsA7a0yxp2VkM-uGo/s1700-e365/llmhack.jpg)

Two malicious LiteLLM releases sat on PyPI for about 40 minutes in March [carrying credential-stealing code](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html) capable of harvesting cloud keys, SSH keys, Kubernetes tokens, database passwords, and other secrets from systems that installed them.

Threat intelligence firm [CloudSEK](https://www.cloudsek.com/blog/ai-supply-chain-breach-2500-companies-434000-cicd-pipelines) now says a dataset it obtained, built from roughly 434,000 files the attackers captured, maps potential exposure to more than 2,500 organizations.

Those totals are not a victim count. CloudSEK told The Hacker News the material came from confidential intelligence sources and consists of captured loot and log files it assessed as belonging to the campaign, not data gathered from the organizations it names. The files were taken, in other words.

CloudSEK has published the dataset as
[a public lookup](https://exposure.cloudsek.com/ai-supply-chain-incident), searchable by name or domain and filterable by confidence. Each row gives an organization's name and domain, a count of secrets exposed, a count of runs, and a label reading High or Medium.

What a high-confidence match asserts is whose systems each file came from. That verdict keys on identity signals in the captured CI runner environment, chiefly host identity and legitimate committer domains, and the organization's own domain has to appear before a match earns the top rating.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Repository namespaces support only a medium-confidence call. NVIDIA, Cisco, Deloitte, Volkswagen, FedEx, Siemens, and X Corp are among the entries, and none of that establishes that stolen credentials were used, which is why both CloudSEK and LiteLLM tell affected parties to rotate rather than wait for proof.

LiteLLM is an open-source AI gateway used to connect applications with multiple model providers. The project identified versions 1.82.7 and 1.82.8 as compromised and said they were live on March 24 from 10:39 UTC for about 40 minutes before PyPI quarantined them, though it tells users to treat any install that day up to 16:00 UTC as suspect.

The Hacker News confirmed via PyPI on August 12 that neither version appears in the package's release history, while 1.82.6 and 1.83.0 remain available.

The FBI warned in a July 2 advisory, FLASH-20260702-01, that affiliated actors are likely to weaponize credentials exfiltrated during [the TeamPCP campaign](https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html) long after the initial compromise. It told organizations to rotate CI/CD secrets, publishing tokens, and cloud credentials accessible during the relevant exposure windows.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJGjuTIs-A-HLDI2Z6p5LI6BgQyy6bPOugpcMjThcmxapuVMI50Xs7TY-QXAW5PsTQEqn6CT3PQFZkXvjglXjG97M_6cumjN9j9pcEqwPgIN8uWgnrlSndbU7DlC1rCiw_CuIBIRy_snfxqIJOy38ooI-9HmSWAmeGl4a1w2EMhgM4uKn8M2-omfrZbhI/s1700-e365/cisco-cloud.jpg)

A long-lived secret copied during that window, a static cloud key, an SSH key, or a publishing token, remains usable unless it has since been rotated or revoked. That is why the bureau's guidance is scoped to credentials rather than to the package, and why both it and Aqua tell teams to move away from long-lived tokens toward temporary ones.

Version 1.82.8 included a file named litellm\_init.pth that Python processes at interpreter startup, so it ran whenever a Python process started in that environment, whether or not anything imported LiteLLM.

The compromised packages were designed to collect environment variables, SSH keys, cloud credentials, Kubernetes tokens, and database passwords before encrypting and sending stolen data to models.litellm[.]cloud, an attacker-controlled domain unrelated to the project.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaXdH1qAN5vPRZ5iZoTPHZCxsSfAShJK9v-x6wHTkGqyxSH2InLRT1GyiSNAOjWGYka4ITorMegSg9WTgm3vFLQE_qyTR8Av_CzaiaDC9v4tNriDY9oM6h6K6wPOS4n72oOFXcFSBvwBmegQoz_MNr2FlmIu7-04HfgzguMhX-KP6Ue_zfOcY728cy0qY/s1700-e365/sap-cloud.jpg)

Unit 42's campaign analysis records the payload reading environment variables that hold [model API keys](https://thehackernews.com/2026/06/282-ios-apps-found-leaking-llm-api-keys.html), including OPENAI\_API\_KEY and ANTHROPIC\_API\_KEY.

That behavior inverts the usual triage question. Whether a team knowingly uses LiteLLM matters less than whether anything on the host installed it, and [the project's advisory](https://docs.litellm.ai/blog/security-update-march-2026) notes that an unpinned transitive dependency, including one pulled in by an agent framework or orchestration tool, could deliver it without anyone choosing it.

The LiteLLM incident sits inside a wider TeamPCP supply-chain campaign linked to [Aqua Security's Trivy scanner](https://thehackernews.com/2026/03/trivy-security-scanner-github-actions.html). Google tracks TeamPCP as UNC6780. [Aqua said](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) attackers retained access after an incomplete credential rotation and, on March 19, force-pushed malicious commits to 76 of 77 trivy-action version tags and all seven setup-trivy tags while publishing a malicious Trivy 0.69.4 release.

The ecosystem compromise is tracked as [CVE-2026-33634](https://nvd.nist.gov/vuln/detail/CVE-2026-33634), added to CISA's Known Exploited Vulnerabilities catalog on March 26. The Hacker News confirmed on August 12 that the CVE record now lists BerriAI LiteLLM 1.82.7 through 1.82.8 as affected alongside the Trivy components.

Exactl...