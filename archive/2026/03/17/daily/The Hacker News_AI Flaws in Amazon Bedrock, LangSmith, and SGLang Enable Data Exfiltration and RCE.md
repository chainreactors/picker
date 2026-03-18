---
title: AI Flaws in Amazon Bedrock, LangSmith, and SGLang Enable Data Exfiltration and RCE
url: https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html
source: The Hacker News
date: 2026-03-17
fetch_date: 2026-03-18T04:22:52.787063
---

# AI Flaws in Amazon Bedrock, LangSmith, and SGLang Enable Data Exfiltration and RCE

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [AI Flaws in Amazon Bedrock, LangSmith, and SGLang Enable Data Exfiltration and RCE](https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html)

**Ravie Lakshmanan**Mar 17, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlC6FiLJ9YVGC1W0eo-MmFsPTu2DNqMSdo-QKnv1gdH_HpaKV3zPaWZrQTGNdklpv62BXb3ECiBqlkR1BzLbfz0tFWfMKNM1vZq88yf90XpycB2OSDq3NScWav6ZO_4IVjCWaJRJLwvthFo-7VJ-Uc8qijyycpXfkQRHcPr9pf-QVgGzyOeBFnwfOGnmLN/s1700-e365/lang-ai.jpg)

Cybersecurity researchers have disclosed details of a new method for exfiltrating sensitive data from artificial intelligence (AI) code execution environments using domain name system (DNS) queries.

In a report published Monday, BeyondTrust [revealed](https://www.beyondtrust.com/blog/entry/aws-bedrock-agentcore-sandbox-breakout) that Amazon Bedrock AgentCore Code Interpreter's sandbox mode permits outbound DNS queries that an attacker can exploit to enable interactive shells and bypass network isolation. The issue, which does not have a CVE identifier, carries a CVSS score of 7.5 out of 10.0.

[Amazon Bedrock AgentCore Code Interpreter](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-agentcore-code-interpreter/) is a fully managed service that enables AI agents to securely execute code in [isolated sandbox environments](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html), such that agentic workloads cannot access external systems. It was launched by Amazon in August 2025.

The fact that the service allows DNS queries despite "no network access" configuration can allow "threat actors to establish command-and-control channels and data exfiltration over DNS in certain scenarios, bypassing the expected network isolation controls," Kinnaird McQuade, chief security architect at BeyondTrust, said.

In an experimental attack scenario, a threat actor can abuse this behavior to set up a bidirectional communication channel using DNS queries and responses, obtain an interactive reverse shell, exfiltrate sensitive information through DNS queries if their IAM role has permissions to access AWS resources like S3 buckets storing that data, and perform command execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

What's more, the DNS communication mechanism can be abused to deliver additional payloads that are fed to the Code Interpreter, causing it to poll the DNS command-and-control (C2) server for commands stored in DNS A records, execute them, and return the results via DNS subdomain queries.

It's worth noting that Code Interpreter requires an IAM role to access AWS resources. However, a simple oversight can cause an overprivileged role to be assigned to the service, granting it broad permissions to access sensitive data.

"This research demonstrates how DNS resolution can undermine the network isolation guarantees of sandboxed code interpreters," BeyondTrust said. "By using this method, attackers could have exfiltrated sensitive data from AWS resources accessible via the Code Interpreter's IAM role, potentially causing downtime, data breaches of sensitive customer information, or deleted infrastructure."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4gwwDqqCOtOURMZKC3ZkMohSzFz8Q1WcKeomOQ88UDz-3somcDlJ1JXxBQyWbIfjZ2fgcj7lQKnVf4zqimi7lTWlyVwr2tLpBBxGRu_OUGChr7GC4Hc8VXLpcOMtuiX9jLhkgVHNanbniiON1assbvB7mPuTbH5aLN-S6wxG9IuxKri7pj__ivIJc4uMX/s1700-e365/chatbot-attack.jpg)

Following responsible disclosure in September 2025, Amazon has determined it to be intended functionality rather than a defect, urging customers to use [VPC mode](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) instead of sandbox mode for complete network isolation. The tech giant is also recommending the use of a [DNS firewall](https://aws.amazon.com/blogs/security/protect-against-advanced-dns-threats-with-amazon-route-53-resolver-dns-firewall/) to filter outbound DNS traffic.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1iLVUjIiSkk1ca72MpSGxKhA5wjrO-Mj05TJLrpoU6EjKmvhk16knLOo2_Kpj-Wx845uWagUnvS1-i1eVbqH-_KmeJlerwZJbsH3QRATPvqzmsYiplto-XA3y7BEnRvxHRwB17JTsVqsAO1JVSa2rzRnTmtTfoNAM4ARVQkZ-oqnB8HuI6oHMQ5hsTa7O/s1700-e365/llm.png)

"To protect sensitive workloads, administrators should inventory all active AgentCore Code Interpreter instances and immediately migrate those handling critical data from Sandbox mode to VPC mode," Jason Soroko, senior fellow at Sectigo, said.

"Operating within a VPC provides the necessary infrastructure for robust network isolation, allowing teams to implement strict security groups, network ACLs, and Route53 Resolver DNS Firewalls to monitor and block unauthorized DNS resolution. Finally, security teams must rigorously audit the IAM roles attached to these interpreters, strictly enforcing the principle of least privilege to restrict the blast radius of any potential compromise."

## LangSmith Susceptible to Account Takeover Flaw

The disclosure comes as Miggo Security disclosed a high-severity security flaw in [LangSmith](https://thehackernews.com/2025/06/langchain-langsmith-bug-let-hackers.html) ([CVE-2026-25750](https://nvd.nist.gov/vuln/detail/cve-2026-25750), CVSS score: 8.5) that exposed users to potential token theft and account takeover. The issue, which affects both self-hosted and cloud deployments, has been addressed in LangSmith version 0.12.71 released in December 2025.

The shortcoming has been characterized as a case of URL parameter injection stemming from a lack of validation on the baseUrl parameter, enabling an attacker to steal a signed-in user's bearer token, user ID, and workspace ID transmitted to a server under their control through social engineering techniques like tricking the victim into clicking on a spe...