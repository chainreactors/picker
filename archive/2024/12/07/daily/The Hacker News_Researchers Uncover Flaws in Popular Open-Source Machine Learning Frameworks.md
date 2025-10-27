---
title: Researchers Uncover Flaws in Popular Open-Source Machine Learning Frameworks
url: https://thehackernews.com/2024/12/researchers-uncover-flaws-in-popular.html
source: The Hacker News
date: 2024-12-07
fetch_date: 2025-10-06T19:59:28.702113
---

# Researchers Uncover Flaws in Popular Open-Source Machine Learning Frameworks

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

# [Researchers Uncover Flaws in Popular Open-Source Machine Learning Frameworks](https://thehackernews.com/2024/12/researchers-uncover-flaws-in-popular.html)

**Dec 06, 2024**Ravie LakshmananArtificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEia1UI8-w6ihOHAxW_rag0lwL_ksW9lIyTZn6Ib3LsOCmUQJUIDoZkgR4URLpY2-TT9KtRE5Dyg3DLj7cGx3wwQKKoYAxNi5NT1Rxs9QgKY8bMJYUH3sC1LwIlH2C64nS8j0-uyH5bWWnvXej9ZtokT81257ZXnCW7Fp1smuSCbwR_EkCGudkACK64PZn2L/s790-rw-e365/ai-model.png)

Cybersecurity researchers have disclosed multiple security flaws impacting open-source machine learning (ML) tools and frameworks such as MLflow, H2O, PyTorch, and MLeap that could pave the way for code execution.

The vulnerabilities, discovered by JFrog, are part of a broader collection of 22 security shortcomings the supply chain security company [first disclosed](https://thehackernews.com/2024/11/security-flaws-in-popular-ml-toolkits.html) last month.

Unlike the first set that involved flaws on the server-side, the newly detailed ones allow exploitation of ML clients and reside in libraries that handle safe model formats like [Safetensors](https://thehackernews.com/2024/02/new-hugging-face-vulnerability-exposes.html).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Hijacking an ML client in an organization can allow the attackers to perform extensive lateral movement within the organization," the company [said](https://jfrog.com/blog/machine-learning-bug-bonanza-exploiting-ml-clients-and-safe-models/). "An ML client is very likely to have access to important ML services such as ML Model Registries or MLOps Pipelines."

This, in turn, could expose sensitive information such as model registry credentials, effectively permitting a malicious actor to backdoor stored ML models or achieve code execution.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjp5itCmDyn-7bS7iQMtoaFxU6zG-G9-KWFe3aoZj8MCnuYTOXFNxlWZlhhMdShjnFtRAjEQCVtHe-qz7LdHs3w-_aDZbjtMEvO77ENhDLjQCliAmYFk2tpS0MrOVsOCaBO7b1LW-X2HgRmlI5HsTzcFQQ5y6ap40iTkaIhV_4z2NFA8tM70xlmDg9Sg2jB/s790-rw-e365/exploit.png)

The list of vulnerabilities is below -

* **[CVE-2024-27132](https://nvd.nist.gov/vuln/detail/CVE-2024-27132)** (CVSS score: 7.2) - An insufficient sanitization issue in MLflow that leads to a cross-site scripting (XSS) attack when running an untrusted [recipe](https://mlflow.org/docs/latest/recipes.html) in a Jupyter Notebook, ultimately resulting in client-side remote code execution (RCE)
* **[CVE-2024-6960](https://nvd.nist.gov/vuln/detail/cve-2024-6960)** (CVSS score: 7.5) - An unsafe deserialization issue in H20 when importing an untrusted ML model, potentially resulting in RCE
* A path traversal issue in PyTorch's TorchScript feature that could result in denial-of-service (DoS) or code execution due to arbitrary file overwrite, which could then be used to overwrite critical system files or a legitimate pickle file (No CVE identifier)
* **[CVE-2023-5245](https://nvd.nist.gov/vuln/detail/CVE-2023-5245)** (CVSS score: 7.5) - A path traversal issue in MLeap when loading a saved model in zipped format can lead to a [Zip Slip vulnerability](https://thehackernews.com/2023/10/openrefines-zip-slip-vulnerability.html), resulting in arbitrary file overwrite and potential code execution

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

JFrog noted that ML models shouldn't be blindly loaded even in cases where they are loaded from a safe type, such as Safetensors, as they have the capability to achieve arbitrary code execution.

"AI and Machine Learning (ML) tools hold immense potential for innovation, but can also open the door for attackers to cause widespread damage to any organization," Shachar Menashe, JFrog's VP of Security Research, said in a statement.

"To safeguard against these threats, it's important to know which models you're using and never load untrusted ML models even from a 'safe' ML repository. Doing so can lead to remote code execution in some scenarios, causing extensive harm to your organization."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data security](https://thehackernews.com/search/label/data%20security)[machine learning](https://thehackernews.com/search/label/machine%20learning)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolvin...