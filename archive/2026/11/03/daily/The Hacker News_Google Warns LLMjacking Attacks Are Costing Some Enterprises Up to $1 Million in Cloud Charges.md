---
title: Google Warns LLMjacking Attacks Are Costing Some Enterprises Up to $1 Million in Cloud Charges
url: https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html
source: The Hacker News
date: 2026-11-03
fetch_date: 2026-11-04T08:19:20.565719
---

# Google Warns LLMjacking Attacks Are Costing Some Enterprises Up to $1 Million in Cloud Charges

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Google Warns LLMjacking Attacks Are Costing Some Enterprises Up to $1 Million in Cloud Charges](https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html)

**Ravie Lakshmanan**Nov 03, 2026Cloud Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvqwPJPXsflyvqykVK3Pd1lLXLzEJ6vpLudxQUyYbWkS4nQ0dr9dhcSlMCPwgqfAkyadPSj28XReqkeiymKG5RAZMWpx5Hqhg_XI0HNp3jRMRpaO-wVIRbyJyS8MaaqDNOxXvk8aUENx_aiNMqrqm9SWjtJVpXR2uaP-LNp5deG4U_4YvSxpPKtdJLRNoh/s1700-nu-rw-lo-l85-e365/llmjacking.png)

Google on Monday warned that threat actors are hijacking enterprise access to Large Language Models (LLMs) to fraudulently leverage expensive computing resources and AI services.

The tactic is called **[LLMjacking](https://thehackernews.com/2026/10/railway-says-intruder-may-have-accessed.html)**, a form of resource hijacking adapted for the LLM era, where an attacker obtains an API key through phishing, source code leaks, misconfigured environments, or exposed client-side code to gain unauthorized access to an organization's LLM accounts, while the legitimate owner covers the consumption costs.

Such attacks have a wide geographical footprint, with impacted entities located in North America, South America, and Asia Pacific across the financial services, retail, technology, and transportation sectors.

"Unlike the gradual resource consumption associated with cryptojacking, LLMJacking can generate large spikes in fraudulent cloud charges in a matter of hours," Google Threat Intelligence Group and Mandiant [said](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models) in a report shared with The Hacker News.

"Across individual incidents, we observed fraudulent charges associated with resource consumption exceeding $100,000 USD in a single day, with cumulative charges at some organizations reaching $1 million USD before access was revoked."

On one end of the spectrum are low-level resource theft that involves the manipulation of customer support chatbots to conduct unauthorized tasks like code generation. LLMjacking is on the other end, as they target the backend model resources directly by identifying publicly exposed LLM endpoints or obtaining valid LLM API keys.

The most common initial access vector has been exposed or stolen cloud identity tokens, including IAM credentials, Service Account keys, GitHub Personal Access Tokens (PATs), and active session tokens, which allow an attacker to establish an initial foothold into target organizations' infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

This includes a threat actor called UNC6993, which is said to have breached a cloud instance through a misconfigured Service Account key and used it to obtain access to an LLM API.

"UNC6993 also hosted a session hijacking page masquerading as an application portal to join a group of LLM users," Google said. "This page tricks users into navigating to the legitimate LLM service website, and pasting their raw JSON payload containing an active access token, which was then posted to the backend API to bypass password and multi-factor authentication (MFA) controls."

In another case, an unknown attacker has been observed leveraging a stolen Personal Access Token to access private code repositories, following it up with the exploitation of a suspected web application vulnerability in a package running within a containerized cloud environment.

Other initial access routes include the compromise of IAM credentials of corporate users to programmatically generate fresh access keys to bypass MFA safeguards, as well as the use of a hacked cloud Service Account key with broad project permissions and LLM API keys obtained from public GitHub repositories.

Upon successfully gaining a foothold, the threat actors waste no time escalating privileges, burrowing deeper into the network, establishing persistence, and conducting internal reconnaissance to identify targets and further cloud credentials for lateral movement.

Some of the observed tactics are listed below -

* Enumerate cloud services, code repositories, and data stores for sensitive credentials.
* Perform internal reconnaissance across multiple cloud regions to map available services and identity policies.
* Clone sensitive codebases to search for hard-coded secrets, configuration variables, and developer credentials.
* Scan access logs to identify credentials for secondary cloud environments.
* Run targeted database queries to harvest additional credentials.
* Abuse cloud identity permissions and virtual machine configurations to escalate privileges and maintain persistent access.
* Exploit token-creation privileges associated with service accounts to generate temporary credentials for high-privilege service accounts and exfiltrate infrastructure credentials, internal database passwords, and third-party API keys from cloud secret managers.
* Create unauthorized IAM and service accounts and inject SSH keys into compute instances for persistence.
* Create backdoor service accounts disguised as internal billing optimization utilities.
* Exploit vulnerabilities targeting LLM routing software, such as [CVE-2026-40217](https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce) in LiteLLM, to escalate privileges.

"The ultimate objective of LLMJacking is the monetization and resource-hijacking of foundation models, which actors achieve through token proxying, automated model streaming, and GPU hardware provisioning," Google said. "Threat actors also leveraged their access to host their own proxy endpoints and agentic workloads."

UNC6993, for instance, has created additional API keys to scale their operations within victim cloud projects, racking up over $100,000 USD in billing charges. Some threat actors attempt to bypass rate limits by adopting a "burn and rotate" strategy that involve...