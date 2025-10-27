---
title: SAP AI Core Vulnerabilities Expose Customer Data to Cyber Attacks
url: https://thehackernews.com/2024/07/sap-ai-core-vulnerabilities-expose.html
source: The Hacker News
date: 2024-07-19
fetch_date: 2025-10-06T17:44:19.421053
---

# SAP AI Core Vulnerabilities Expose Customer Data to Cyber Attacks

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

# [SAP AI Core Vulnerabilities Expose Customer Data to Cyber Attacks](https://thehackernews.com/2024/07/sap-ai-core-vulnerabilities-expose.html)

**Jul 18, 2024**Ravie LakshmananCloud Security / Enterprise Security

[![SAP AI Core Vulnerabilities](data:image/png;base64... "SAP AI Core Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisk_E6g6CL2RM_HmqsXni3CeMtuHeC_gleyTSoEUGHG0LenkRuK9QK3pJmc7MLgtOB4bSgbD-OlSEva-ebhiru3rfaS18CL8bx8uXkI0-NUKbeh-b93Xqe09TdiRefRdjhEvTa0GxdK9Tx-Ly5CEAVlePcosSbGHJ-2lo3PPlJeNXByzZfOAKRbKyOoUC8/s790-rw-e365/wiz.png)

Cybersecurity researchers have uncovered security shortcomings in [SAP AI Core](https://help.sap.com/docs/sap-ai-core?locale=en-US) cloud-based platform for creating and deploying predictive artificial intelligence (AI) workflows that could be exploited to get hold of access tokens and customer data.

The five vulnerabilities have been collectively dubbed **SAPwned** by cloud security firm Wiz.

"The vulnerabilities we found could have allowed attackers to access customers' data and contaminate internal artifacts – spreading to related services and other customers' environments," security researcher Hillai Ben-Sasson [said](https://www.wiz.io/blog/sapwned-sap-ai-vulnerabilities-ai-security) in a report shared with The Hacker News.

Following responsible disclosure on January 25, 2024, the weaknesses were addressed by SAP as of May 15, 2024.

In a nutshell, the flaws make it possible to obtain unauthorized access to customers' private artifacts and credentials to cloud environments like Amazon Web Services (AWS), Microsoft Azure, and SAP HANA Cloud.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

They could also be used to modify Docker images on SAP's internal container registry, SAP's Docker images on the Google Container Registry, and artifacts hosted on SAP's internal Artifactory server, resulting in a supply chain attack on SAP AI Core services.

Furthermore, the access could be weaponized to gain cluster administrator privileges on SAP AI Core's Kubernetes cluster by taking advantage of the fact that the Helm package manager server was exposed to both read and write operations.

"Using this access level, an attacker could directly access other customer's Pods and steal sensitive data, such as models, datasets, and code," Ben-Sasson explained. "This access also allows attackers to interfere with customer's Pods, taint AI data and manipulate models' inference."

Wiz said the issues arise due to the platform making it feasible to run malicious AI models and training procedures without adequate isolation and sandboxing mechanisms.

"The recent security flaws in AI service providers like [Hugging Face](https://thehackernews.com/2024/04/ai-as-service-providers-vulnerable-to.html), [Replicate](https://thehackernews.com/2024/05/experts-find-flaw-in-replicate-ai.html), and SAP AI Core highlight significant vulnerabilities in their tenant isolation and segmentation implementations," Ben-Sasson told The Hacker News. "These platforms allow users to run untrusted AI models and training procedures in shared environments, increasing the risk of malicious users being able to access other users' data."

"Unlike veteran cloud providers who have vast experience with tenant-isolation practices and use robust isolation techniques like virtual machines, these newer services often lack this knowledge and rely on containerization, which offers weaker security. This underscores the need to raise awareness of the importance of tenant isolation and to push the AI service industry to harden their environments."

As a result, a threat actor could create a regular AI application on SAP AI Core, bypass network restrictions, and probe the Kubernetes Pod's internal network to obtain AWS tokens and access customer code and training datasets by exploiting misconfigurations in AWS Elastic File System (EFS) shares.

"People should be aware that AI models are essentially code. When running AI models on your own infrastructure, you could be exposed to potential supply chain attacks," Ben-Sasson said.

"Only run trusted models from trusted sources, and properly separate between external models and sensitive infrastructure. When using AI services providers, it's important to verify their tenant-isolation architecture and ensure they apply best practices."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings come as Netskope revealed that the growing enterprise use of generative AI has prompted organizations to use blocking controls, data loss prevention (DLP) tools, real-time coaching, and other mechanisms to mitigate risk.

"Regulated data (data that organizations have a legal duty to protect) makes up more than a third of the sensitive data being shared with generative AI (genAI) applications — presenting a potential risk to businesses of costly data breaches," the company [said](https://www.netskope.com/netskope-threat-labs/cloud-threat-report/july-2024-ai-apps-in-the-enterprise).

They also follow the emergence of a new cybercriminal threat group called NullBulge that has trained its sights on AI- and gaming-focused entities since April 2024 with an aim to steal sensitive data and sell compromised OpenAI API keys in underground forums while claiming to be a hacktivist crew "protecting artists around the world" against AI.

"NullBulge targets the software supply chain by weaponizing code in publicly available repositories on GitHub and Hugging Face, leading victims to import malicious libraries, or through mod packs used by gaming and modeling software," SentinelOne security researcher Jim Walter [said](https://www.sentinelone.com/labs/nullbulge-threat-actor-masquerades-as-hacktivist-group-rebelling-against-ai/).

"The group uses tools like [AsyncRAT](https://thehackernews.com/2022/01/hackers-using-new-evasive-technique-to.html) and [XWorm](https://thehackernews.com/2023/05/xworm-malware-expl...