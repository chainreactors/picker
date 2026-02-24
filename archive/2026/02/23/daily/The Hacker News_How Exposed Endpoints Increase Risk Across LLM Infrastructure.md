---
title: How Exposed Endpoints Increase Risk Across LLM Infrastructure
url: https://thehackernews.com/2026/02/how-exposed-endpoints-increase-risk.html
source: The Hacker News
date: 2026-02-23
fetch_date: 2026-02-24T04:12:15.775236
---

# How Exposed Endpoints Increase Risk Across LLM Infrastructure

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [How Exposed Endpoints Increase Risk Across LLM Infrastructure](https://thehackernews.com/2026/02/how-exposed-endpoints-increase-risk.html)

**The Hacker News**Feb 23, 2026Artificial Intelligence / Zero Trust

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7sXBbFbgAhWn7fFcyznMrutXhMfRWKQzw6aFcQwiJ-ViGLqg_Vse2wGKgGrAkyXTh2y9XtufC9otYEoUyIPsV6FB1ktgNSVQ15UFYNKN8HVzncL6tYLNYtzqX6rqhgVIfThhll1TxO1627pxBguwt4J1QRKGMOHx7_jBRlhhebK-yq1LMnCAIetPNw1E/s1700-e365/keeper.jpg)

As more organizations run their own Large Language Models (LLMs), they are also deploying more internal services and Application Programming Interfaces (APIs) to support those models. Modern security risks are being introduced less from the models themselves and more from the infrastructure that serves, connects and automates the model. Each new LLM endpoint expands the attack surface, often in ways that are easy to overlook during rapid deployment, especially when endpoints are trusted implicitly. When LLM endpoints accumulate excessive permissions and long-lived credentials are exposed, they can provide far more access than intended. Organizations must prioritize endpoint privilege management because exposed endpoints have become an increasingly common attack vector for cybercriminals to access the systems, identities and secrets that power LLM workloads.

## What is an endpoint in modern LLM infrastructure?

In modern LLM infrastructure, an [endpoint](https://www.keepersecurity.com/resources/glossary/what-is-an-endpoint/) is any interface where something — whether it be a user, application or service — can communicate with a model. Simply put, endpoints allow requests to be sent to an LLM and for responses to be returned. Common examples include inference APIs that handle prompts and generate outputs, model management interfaces used to update models and administrative dashboards that allow teams to monitor performance. Many LLM deployments also rely on plugin or tool execution endpoints, which allow models to interact with external services such as databases that may connect the LLM to other systems. Together, these endpoints define how the LLM connects to the rest of its environment.

The main challenge is that most LLM endpoints are built for internal use and speed, not long-term security. They are typically created to support experimentation or early deployments and then are left running with minimal oversight. As a result, they tend to be poorly monitored and granted more access than necessary. In practice, the endpoint becomes the security boundary, meaning its identity controls, secrets handling and privilege scope determine how far a cybercriminal can go.

## How LLM endpoints become exposed

LLMs are rarely exposed through one failure; more often, exposure happens gradually through small assumptions and decisions made during development and deployment. Over time, these patterns transform internal services into externally reachable attack surfaces. Some of the most common exposure patterns include:

* **Publicly accessible APIs without authentication:** Internal APIs are sometimes exposed publicly to quicken testing or integration. Authentication is delayed or skipped entirely, and the endpoint remains accessible long after it was meant to be restricted.
* **Weak or static tokens:** Many LLM endpoints rely on tokens or API keys that are hardcoded and never rotated. If these secrets are leaked through misconfigured systems or repositories, unauthorized users can access an endpoint indefinitely.
* **The assumption that internal means safe:** Teams often treat internal endpoints as trusted by default, assuming they will never be reached by unauthorized users. However, internal networks are frequently reachable through VPNs or misconfigured controls.
* **Temporary test endpoints that become permanent:** Endpoints designed for debugging or demos are rarely cleaned up. Over time, these endpoints remain active but unmonitored and poorly secured while the surrounding infrastructure evolves.
* **Cloud misconfigurations that expose services:** Misconfigured API gateways or firewall rules can unintentionally expose internal LLM endpoints to the internet. These misconfigurations often occur gradually and go unnoticed until the endpoint is already exposed.

## Why exposed endpoints are dangerous across LLM infrastructure

Exposed endpoints are particularly dangerous in LLM environments because LLMs are designed to connect multiple systems within a broader technical infrastructure. When cybercriminals compromise a single LLM endpoint, they can often gain access to much more than the model itself. Unlike traditional APIs that perform one function, LLM endpoints are commonly integrated with databases, internal tools or cloud services to support automated workflows. Therefore, one compromised endpoint can allow cybercriminals to move quickly and laterally across systems that already trust the LLM by default.

The real danger doesn’t derive from the LLM being too powerful but rather from the implicit trust placed in the endpoint from the beginning. Once an LLM endpoint is exposed, it can act as a force multiplier; cybercriminals can use a compromised endpoint for various automated tasks instead of manually exploring systems. Exposed endpoints can jeopardize LLM environments through:

* **Prompt-driven data exfiltration:** Cybercriminals can create prompts that cause the LLM to summarize sensitive data it has access to, turning the model into an automated data extraction tool.
* **Abuse of tool-calling permissions:** When LLMs call internal tools or services, exposed endpoints can be used to abuse these tools by modifying resources or performing privileged actions.
* **Indirect prompt injection:** Even when access is limited, cybercriminals can manipulate data sources or LLM inputs, causing the model to execute harmful actions indirectly.

### Why NHIs are especially dang...