---
title: Researchers Identify Over 20 Supply Chain Vulnerabilities in MLOps Platforms
url: https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html
source: The Hacker News
date: 2024-08-27
fetch_date: 2025-10-06T18:08:42.031305
---

# Researchers Identify Over 20 Supply Chain Vulnerabilities in MLOps Platforms

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

# [Researchers Identify Over 20 Supply Chain Vulnerabilities in MLOps Platforms](https://thehackernews.com/2024/08/researchers-identify-over-20-supply.html)

**Aug 26, 2024**Ravie LakshmananML Security / Artificial Intelligence

[![MLOps Platforms](data:image/png;base64... "MLOps Platforms")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIqO9WE1xCBsO_HgoHbRLs5HnSu_3-EGbtyIWpwv-1sNkXsUcR9oWmxpSjr6ecg29Qea9A9hdspar1y1tZ0xp_e4xF-1tp8rugbcgxA-b99gV44HcIDFGBqUTxiJtrOVJi8f8eHdGUGMubL9QjrJrJoW-YX3gBouOlX_0jqvONRZljNdxPXOcPX2qV-tG2/s790-rw-e365/aiml.png)

Cybersecurity researchers are warning about the security risks in the machine learning (ML) software supply chain following the discovery of more than 20 vulnerabilities that could be exploited to target MLOps platforms.

These vulnerabilities, which are described as inherent- and implementation-based flaws, could have severe consequences, ranging from arbitrary code execution to loading malicious datasets.

MLOps platforms offer the ability to design and execute an ML model pipeline, with a model registry acting as a repository used to store and version-trained ML models. These models can then be embedded within an application or allow other clients to query them using an API (aka model-as-a-service).

"Inherent vulnerabilities are vulnerabilities that are caused by the underlying formats and processes used in the target technology," JFrog researchers [said](https://jfrog.com/blog/from-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms/) in a detailed report.

Some examples of inherent vulnerabilities include abusing ML models to run code of the attacker's choice by taking advantage of the fact that models support automatic code execution upon loading (e.g., [Pickle model files](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html)).

This behavior also extends to certain dataset formats and libraries, which allow for automatic code execution, thereby potentially opening the door to malware attacks when simply loading a publicly-available dataset.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Another instance of inherent vulnerability concerns JupyterLab (formerly Jupyter Notebook), a web-based interactive computational environment that enables users to execute blocks (or cells) of code and view the corresponding results.

"An inherent issue that many do not know about, is the handling of HTML output when running code blocks in Jupyter," the researchers pointed out. "The output of your Python code may emit HTML and [JavaScript] which will be happily rendered by your browser."

The problem here is that the JavaScript result, when run, is not sandboxed from the parent web application and that the parent web application can automatically run arbitrary Python code.

In other words, an attacker could output a malicious JavaScript code such that it adds a new cell in the current JupyterLab notebook, injects Python code into it, and then executes it. This is particularly true in cases when exploiting a cross-site scripting (XSS) vulnerability.

To that end, JFrog said it identified an XSS flaw in MLFlow ([CVE-2024-27132](https://github.com/advisories/GHSA-6749-m5cp-6cg7), CVSS score: 7.5) that stems from a lack of sufficient sanitization when running an untrusted [recipe](https://mlflow.org/docs/latest/recipes.html), resulting in client-side code execution in JupyterLab.

[![MLOps Platforms](data:image/png;base64... "MLOps Platforms")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZ6ICPxd_mGt8b0vbzIW8Ro5scNFiLWjzw_7rRLrqde5X1KrETXH9GiqDjZO4omAMkWqF4bFi2uDYxhwdDaXt7t6U9nzjFM4Zwm5Q2MCft5rEwls-OjtFcIRN4sTGLcc7KA_KpLHvdVfVdWfd3UtfViqdvEk9zwNxpxkoTgpooRcVmwhq2V1YgacUufPTL/s790-rw-e365/attacks.jpg)

"One of our main takeaways from this research is that we need to treat all XSS vulnerabilities in ML libraries as potential arbitrary code execution, since data scientists may use these ML libraries with Jupyter Notebook," the researchers said.

The second set of flaws relate to implementation weaknesses, such as lack of authentication in MLOps platforms, potentially permitting a threat actor with network access to obtain code execution capabilities by abusing the ML Pipeline feature.

These threats aren't theoretical, with financially motivated adversaries abusing such loopholes, as recently observed in the case of cyber attacks targeting unpatched Anyscale Ray ([CVE-2023-48022](https://thehackernews.com/2024/03/critical-unpatched-ray-ai-platform.html), CVSS score: 9.8) instances, to deploy cryptocurrency miners.

A second type of implementation vulnerability is a container escape targeting Seldon Core that enables attackers to go beyond code execution to move laterally across the cloud environment and access other users' models and datasets by uploading a malicious model to the inference server.

The net outcome of chaining these vulnerabilities is that they could not only be weaponized to infiltrate and spread inside an organization, but also compromise servers.

"If you're deploying a platform that allows for model serving, you should now know that anybody that can serve a new model can also actually run arbitrary code on that server," the researchers said. "Make sure that the environment that runs the model is completely isolated and hardened against a container escape."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Palo Alto Networks Unit 42 [detailed](https://unit42.paloaltonetworks.com/langchain-vulnerabilities/) two now-patched vulnerabilities in the open-source LangChain generative AI framework (CVE-2023-46229 and CVE-2023-44467) that could have allowed attackers to execute arbitrary code and access sensitive data, respectively.

Last month, Trail of Bits also [revealed](https://blog.trailofbits.com/2024/07/05/auditing-the-ask-astro-llm-qa-app/) four issues in Ask Astro, a retrieval augmented generat...