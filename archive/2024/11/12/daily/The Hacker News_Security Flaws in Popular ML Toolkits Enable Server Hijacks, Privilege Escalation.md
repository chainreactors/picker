---
title: Security Flaws in Popular ML Toolkits Enable Server Hijacks, Privilege Escalation
url: https://thehackernews.com/2024/11/security-flaws-in-popular-ml-toolkits.html
source: The Hacker News
date: 2024-11-12
fetch_date: 2025-10-06T19:23:37.529527
---

# Security Flaws in Popular ML Toolkits Enable Server Hijacks, Privilege Escalation

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Security Flaws in Popular ML Toolkits Enable Server Hijacks, Privilege Escalation](https://thehackernews.com/2024/11/security-flaws-in-popular-ml-toolkits.html)

**Nov 11, 2024**Ravie LakshmananMachine Learning / Vulnerability

[![machine learning](data:image/png;base64... "machine learning")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs05CMDmTIAgAhq-7ZE365ltKyXFmWUpl6anMYtw9aj6Dtho6UUkNMQY8Cw43EAxRTg-KosCfMJ5zhp-vGOK_eKhlyLiWLn0Ddw53zU1ff7kBNVoYIMs1neVjt7cJGHAnCf7JzpepIHVvMjSDoZ14Z9YJ-dOTtJNRN-TNuW8ztvRiAfDFkKmmGSMQEMZJj/s790-rw-e365/face.png)

Cybersecurity researchers have uncovered nearly two dozen security flaws spanning 15 different machine learning (ML) related open-source projects.

These comprise vulnerabilities discovered both on the server- and client-side, software supply chain security firm JFrog said in an analysis published last week.

The server-side weaknesses "allow attackers to hijack important servers in the organization such as ML model registries, ML databases and ML pipelines," it [said](https://jfrog.com/blog/machine-learning-bug-bonanza-exploiting-ml-services/).

The vulnerabilities, discovered in Weave, ZenML, Deep Lake, Vanna.AI, and Mage AI, have been broken down into broader sub-categories that allow for remotely hijacking model registries, ML database frameworks, and taking over ML Pipelines.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A brief description of the identified flaws is below -

* **[CVE-2024-7340](https://research.jfrog.com/vulnerabilities/wandb-weave-server-remote-arbitrary-file-leak-jfsa-2024-001039248/)** (CVSS score: 8.8) - A directory traversal vulnerability in the Weave ML toolkit that allows for reading files across the whole filesystem, effectively allowing a low-privileged authenticated user to escalate their privileges to an admin role by reading a file named "api\_keys.ibd" (addressed in [version 0.50.8](https://github.com/wandb/weave/commit/f43d5fb75e0d52933a52ecd9a0ce2f9b082e6c9f))
* An improper access control vulnerability in the ZenML MLOps framework that allows a user with access to a managed ZenML server to elevate their privileges from a viewer to full admin privileges, granting the attacker the ability to modify or read the Secret Store (No CVE identifier)
* **[CVE-2024-6507](https://research.jfrog.com/vulnerabilities/deeplake-kaggle-command-injection-jfsa-2024-001035320/)** (CVSS score: 8.1) - A command injection vulnerability in the Deep Lake AI-oriented database that allows attackers to inject system commands when uploading a remote Kaggle dataset due to a lack of proper input sanitization (addressed in [version 3.9.11](https://github.com/activeloopai/deeplake/pull/2876))
* **[CVE-2024-5565](https://research.jfrog.com/vulnerabilities/vanna-prompt-injection-rce-jfsa-2024-001034449/)** (CVSS score: 8.1) - A prompt injection vulnerability in the Vanna.AI library that could be [exploited](https://thehackernews.com/2024/06/prompt-injection-flaw-in-vanna-ai.html) to achieve remote code execution on the underlying host
* **[CVE-2024-45187](https://research.jfrog.com/vulnerabilities/mage-ai-deleted-users-rce-jfsa-2024-001039602/)** (CVSS score: 7.1) - An incorrect privilege assignment vulnerability that allows guest users in the Mage AI framework to remotely execute arbitrary code through the Mage AI terminal server due to the fact that they have been assigned high privileges and remain active for a default period of 30 days despite deletion
* **[CVE-2024-45188](https://research.jfrog.com/vulnerabilities/mage-ai-file-content-request-remote-arbitrary-file-leak-jfsa-2024-001039603/), [CVE-2024-45189](https://research.jfrog.com/vulnerabilities/mage-ai-git-content-request-remote-arbitrary-file-leak-jfsa-2024-001039604/), and [CVE-2024-45190](https://research.jfrog.com/vulnerabilities/mage-ai-pipeline-interaction-request-remote-arbitrary-file-leak-jfsa-2024-001039605/)** (CVSS scores: 6.5) - Multiple path traversal vulnerabilities in Mage AI that allow remote users with the "Viewer" role to read arbitrary text files from the Mage server via "File Content," "Git Content," and "Pipeline Interaction" requests, respectively

"Since MLOps pipelines may have access to the organization's ML Datasets, ML Model Training and ML Model Publishing, exploiting an ML pipeline can lead to an extremely severe breach," JFrog said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Each of the attacks mentioned in this blog (ML Model backdooring, ML data poisoning, etc.) may be performed by the attacker, depending on the MLOps pipeline's access to these resources.

The disclosure comes over two months after the company [uncovered](https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html) more than 20 vulnerabilities that could be exploited to target MLOps platforms.

It also follows the release of a defensive framework codenamed [Mantis](https://github.com/pasquini-dario/project_mantis) that leverages prompt injection as a way to counter cyber attacks Large language models (LLMs) with more than over 95% effectiveness.

"Upon detecting an automated cyber attack, Mantis plants carefully crafted inputs into system responses, leading the attacker's LLM to disrupt their own operations (passive defense) or even compromise the attacker's machine (active defense)," a group of academics from the George Mason University [said](https://arxiv.org/abs/2410.20911).

"By deploying purposefully vulnerable decoy services to attract the attacker and using dynamic prompt injections for the attacker's LLM, Mantis can autonomously hack back the attacker."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link...