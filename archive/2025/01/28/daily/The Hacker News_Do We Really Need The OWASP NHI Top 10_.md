---
title: Do We Really Need The OWASP NHI Top 10?
url: https://thehackernews.com/2025/01/do-we-really-need-owasp-nhi-top-10.html
source: The Hacker News
date: 2025-01-28
fetch_date: 2025-10-06T20:12:52.356478
---

# Do We Really Need The OWASP NHI Top 10?

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

# [Do We Really Need The OWASP NHI Top 10?](https://thehackernews.com/2025/01/do-we-really-need-owasp-nhi-top-10.html)

**Jan 27, 2025**The Hacker NewsApplication Security / API Security

[![OWASP NHI Top 10](data:image/png;base64... "OWASP NHI Top 10")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5GdGQZj4zg5hRQ2pnUW2aji88mvX85OngxOaDqtCeH64hAkPNIqMJC1EkMuS8be2iFPOSnmNdzEJ_fB5RXUhdP9bCsGhaAzpSodIACU0qtG4Vp8Dr-cydUfFbFxZYOPp7IwqmHG7gdpX3ZzfHqDr_IwTuSSCXhhZdEsK9FDrjF8oaMGrdUHXrhDru3mY/s790-rw-e365/owasp.jpg)

The Open Web Application Security Project has recently introduced a new Top 10 project - the Non-Human Identity (NHI) Top 10. For years, OWASP has provided security professionals and developers with essential guidance and actionable frameworks through its Top 10 projects, including the widely used API and Web Application security lists.

Non-human identity security represents an emerging interest in the cybersecurity industry, encompassing the risks and lack of oversight associated with API keys, [service accounts](https://astrix.security/learn/blog/the-service-accounts-guide-part-1-origin-types-pitfalls-and-fixes/), OAuth apps, SSH keys, IAM roles, secrets, and other machine credentials and workload identities.

Considering that the flagship OWASP Top 10 projects already cover a broad range of security risks developers should focus on, one might ask - do we really need the NHI Top 10? [The short answer is - yes](https://astrix.security/events/introducing-owasp-nhi-top-10/). Let's see why, and explore the top 10 NHI risks.

## **Why we need the NHI Top 10**

While other OWASP projects might touch on related vulnerabilities, such as secrets misconfiguration, NHIs and their associated risks go well beyond that. Security [incidents](https://astrix.security/learn/blog/nhi-attacks-making-waves-insights-on-latest-5-incidents/) leveraging NHIs don't just revolve around exposed secrets; they extend to excessive permissions, OAuth phishing attacks, IAM roles used for [lateral movement](https://astrixvideos.wistia.com/live/events/j0smwxglmc), and more.

While crucial, the existing OWASP Top 10 lists don't properly address the unique challenges NHIs present. Being the critical connectivity enablers between systems, services, data, and AI agents, NHIs are extremely prevalent across development and runtime environments, and developers interact with them at every stage of the development pipeline.

With the [growing frequency of attacks targeting NHIs](https://astrix.security/learn/blog/11-attacks-in-13-months-the-new-generation-of-supply-chain-attacks/), it became imperative to equip developers with a dedicated guide to the risks they face.

[![OWASP NHI Top 10](data:image/png;base64... "OWASP NHI Top 10")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIXyqM-YZ4xxYQbyIBPfkDFGF2B3HqnDnfyez20ldgy7tnkXeGT8Izubi_rOU5cv2aD0HZglxe4ZFVD-rmoa0h6lD3MkDJ_LYHizf9eRomyTVw6UYSb_LutK50-WSGG8TUxQpxEVlRUxKGKKWXWF_NyXeR7OU20zN4at62odSTLxmOryYkFt9nGQRdByw/s790-rw-e365/image.png)

## **Understanding the OWASP Top 10 ranking criteria**

Before we dive into the actual risks, it's important to understand the ranking behind the Top 10 projects. OWASP Top 10 projects follow a standard set of parameters to determine risk severity:

* **Exploitability:** Evaluate how easily an attacker can exploit a given vulnerability if the organization lacks sufficient protection.
* **Impact:** Considers the potential damage the risk could inflict on business operations and systems.
* **Prevalence:** Assesses how common the security issue is across different environments, disregarding existing protective measures.
* **Detectability:** Measures the difficulty of spotting the weakness using standard monitoring and detection tools.

## **Breaking down the OWASP NHI Top 10 risks**

Now to the meat. Let's explore the top risks that earned a spot on the [NHI Top 10](https://owasp.org/www-project-non-human-identities-top-10/) list and why they matter:

### **NHI10:2025 - Human Use of NHI**

NHIs are designed to facilitate automated processes, services, and applications without human intervention. However, during the development and maintenance phases, developers or administrators may repurpose NHIs for manual operations that should ideally be conducted using personal human credentials with appropriate privileges. This can cause privilege misuse, and, if this abused key is part of an exploit, it's hard to know who is accountable for it.

### **NHI9:2025 - NHI Reuse**

NHI reuse occurs when teams repurpose the same [service account](https://astrix.security/learn/blog/the-service-account-guide-part-2-challenges-compliance-and-best-practices/), for example, across multiple applications. While convenient, this violates the principle of least privilege and can expose multiple services in the case of a compromised NHI - increasing the blast radius.

### **NHI8:2025 - Environment Isolation**

A lack of [strict environment isolation](https://www.brighttalk.com/webcast/10415/632223?bt_tok=%7B%7BRecipient.ID%7D%7D&utm_source=) can lead to test NHIs bleeding into production. A real-world example is the [Midnight Blizzard](https://www.microsoft.com/en-us/security/security-insider/midnight-blizzard) attack on Microsoft, where an OAuth app used for testing was found to have high privileges in production, exposing sensitive data.

### **NHI7:2025 - Long-Lived Secrets**

Secrets that remain valid for extended periods pose a significant risk. A notable incident involved Microsoft AI inadvertently exposing an access token in a public GitHub repository, which remained active for over two years and provided access to 38 terabytes of internal data.

### **NHI6:2025 - Insecure Cloud Deployment Configurations**

CI/CD pipelines inherently require extensive permissions, making them prime targets for attackers. Misconfigurations, such as hardcoded credentials or overly permissive OIDC configurations, can lead to unauthorized access to critical resources, exposing them to breache...