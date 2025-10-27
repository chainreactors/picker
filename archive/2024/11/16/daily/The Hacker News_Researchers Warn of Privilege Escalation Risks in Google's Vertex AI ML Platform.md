---
title: Researchers Warn of Privilege Escalation Risks in Google's Vertex AI ML Platform
url: https://thehackernews.com/2024/11/researchers-warn-of-privilege.html
source: The Hacker News
date: 2024-11-16
fetch_date: 2025-10-06T19:20:30.683878
---

# Researchers Warn of Privilege Escalation Risks in Google's Vertex AI ML Platform

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

# [Researchers Warn of Privilege Escalation Risks in Google's Vertex AI ML Platform](https://thehackernews.com/2024/11/researchers-warn-of-privilege.html)

**Nov 15, 2024**Ravie LakshmananArtificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiG7ldlbkeT1_Tv8K3Qw8oxtlujgy17QAONOzg0YC7in0j3y2qXgiUc48RLGFm6BeMoc_tK-DS0Ya3zp_pTIrYLbSUUXpnXvuR-RLCCIKB6y5cCvQTsZ_PDSoLia_khr4vOF5Uu5x98e5SiPWrshv2xSncePfPRi9WcfREfmxOYRABB_VSEPNhhI_xh7OSF/s790-rw-e365/ai.png)

Cybersecurity researchers have disclosed two security flaws in Google's Vertex machine learning (ML) platform that, if successfully exploited, could allow malicious actors to escalate privileges and exfiltrate models from the cloud.

"By exploiting custom job permissions, we were able to escalate our privileges and gain unauthorized access to all data services in the project," Palo Alto Networks Unit 42 researchers Ofir Balassiano and Ofir Shaty [said](https://unit42.paloaltonetworks.com/privilege-escalation-llm-model-exfil-vertex-ai/) in an analysis published earlier this week.

"Deploying a poisoned model in Vertex AI led to the exfiltration of all other fine-tuned models, posing a serious proprietary and sensitive data exfiltration attack risk."

Vertex AI is [Google's ML platform](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) for training and deploying custom ML models and artificial intelligence (AI) applications at scale. It was first introduced in May 2021.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Crucial to leveraging the privilege escalation flaw is a feature called [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines/introduction), which allows users to automate and monitor MLOps workflows to train and tune ML models using custom jobs.

Unit 42's research found that by manipulating the custom job pipeline, it's possible to escalate privileges to gain access to otherwise restricted resources. This is accomplished by creating a custom job that runs a specially-crafted image designed to launch a reverse shell, granting backdoor access to the environment.

The custom job, per the security vendor, runs in a tenant project with a service agent account that has extensive permissions to list all [service accounts](https://cloud.google.com/iam/docs/service-account-overview), manage storage buckets, and access BigQuery tables, which could then be abused to access internal Google Cloud repositories and download images.

The second vulnerability, on the other hand, involves deploying a poisoned model in a tenant project such that it creates a reverse shell when deployed to an endpoint, and then abusing the read-only permissions of the "custom-online-prediction" service account to enumerate Kubernetes clusters and fetch their credentials to run arbitrary kubectl commands.

"This step enabled us to move from the GCP realm into Kubernetes," the researchers said. "This lateral movement was possible because permissions between GCP and GKE were linked through [IAM Workload Identity Federation](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)."

The analysis further found that it's possible to make use of this access to view the newly created image within the Kubernetes cluster and get the [image digest](https://cloud.google.com/kubernetes-engine/docs/concepts/about-container-images) – which uniquely identifies a container image – using it to extract the image outside of the container by using [crictl](https://github.com/kubernetes-sigs/cri-tools/blob/master/docs/crictl.md) with the authentication token associated with the "custom-online-prediction" service account.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhAWiLmCy1M1pY227ODwwSl-QZdjn9F86BsBeU03FgDNvtgFDH9a7fN1fbhC4rwaaP4SUW6ETn8Y6qjh2DLfQQuLaHp5wJQojxlZGLVXKDBlWIg3Mu2kKMgLsMJXFNSKlcqlAkSB0wVq2_Fjl7rmocTL27bYmzaIo_FUYPLI8ltpxptKe4UPB7S7jvI_VS9/s790-rw-e365/flaws.png)

On top of that, the malicious model could also be weaponized to view and export all large-language models ([LLMs](https://arxiv.org/abs/2408.13296)) and their [fine-tuned adapters](https://magazine.sebastianraschka.com/p/finetuning-llms-with-adapters) in a similar fashion.

This could have severe consequences when a developer unknowingly deploys a trojanized model uploaded to a public repository, thereby allowing the threat actor to exfiltrate all ML and fine-tuned LLMs. Following responsible disclosure, both the shortcomings have been addressed by Google.

"This research highlights how a single malicious model deployment could compromise an entire AI environment," the researchers said. "An attacker could use even one unverified model deployed on a production system to exfiltrate sensitive data, leading to severe model exfiltration attacks."

Organizations are recommended to implement strict controls on model deployments and audit permissions required to deploy a model in tenant projects.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as Mozilla's 0Day Investigative Network (0Din) revealed that it's possible to interact with OpenAI ChatGPT's underlying sandbox environment ("/home/sandbox/.openai\_internal/") via prompts, granting the ability to upload and execute Python scripts, move files, and even download the LLM's playbook.

That said, it's worth noting that OpenAI considers such interactions as intentional or expected behavior, given that the code execution takes place within the confines of the sandbox and is unlikely to spill out.

"For anyone eager to explore OpenAI's ChatGPT sandbox, it's crucial to understand that most activities within this containerized environment are intended features rather than security gaps," security researcher Marco Figueroa [said](https://0din.ai/blog/prompt-injecting-your-way-to-shell-openai-s-containerized-chatgpt...