---
title: Securing Agentic AI: How to Protect the Invisible Identity Access
url: https://thehackernews.com/2025/07/securing-agentic-ai-how-to-protect.html
source: The Hacker News
date: 2025-07-16
fetch_date: 2025-10-07T00:08:59.230597
---

# Securing Agentic AI: How to Protect the Invisible Identity Access

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

# [Securing Agentic AI: How to Protect the Invisible Identity Access](https://thehackernews.com/2025/07/securing-agentic-ai-how-to-protect.html)

**Jul 15, 2025**The Hacker NewsAutomation / Risk Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxC8vGH61wOv2EwdXnWISmWy1q-QOx7bl1YDrttsLSMfHiTCzzQqIjeTS5SZNjN_ow9EjaWGUgNMMKNPEFfUyCqhd8i3tt17TyjyIRPtdG_J9BTcOYmCWB0mrTgduQg1XBNpKn5JLlumYHgMY6H0xTwbV9Ew_Qn9Xfq2MTMCrSzb9kQ8vMAB4wQPoJt4I/s790-rw-e365/astrix.jpg)

AI agents promise to automate everything from financial reconciliations to incident response. Yet every time an AI agent spins up a workflow, it has to authenticate somewhere; often with a high-privilege API key, OAuth token, or service account that defenders can't easily see. These "invisible" non-human identities (NHIs) now outnumber human accounts in most cloud environments, and they have become one of the ripest targets for attackers.

Astrix's Field CTO Jonathan Sander put it bluntly in a recent [Hacker News webinar](https://astrix.security/videos/the-invisible-identities-behind-ai-agents/?utm_source=google&utm_medium=blog&utm_campaign=ai):

*"One dangerous habit we've had for a long time is trusting application logic to act as the guardrails. That doesn't work when your AI agent is powered by LLMs that don't stop and think when they're about to do something wrong. They just do it."*

## **Why AI Agents Redefine Identity Risk**

1. **Autonomy changes everything:** An AI agent can chain multiple API calls and modify data without a human in the loop. If the underlying credential is exposed or overprivileged, each additional action amplifies the blast radius.
2. **LLMs behave unpredictably:** Traditional code follows deterministic rules; large language models operate on probability. That means you cannot guarantee how or where an agent will use the access you grant it.
3. **Existing IAM tools were built for humans:** Most identity governance platforms focus on employees, not tokens. They lack the context to map which NHIs belong to which agents, who owns them, and what those identities can actually touch.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYJ74mTrRVg5K-kTDJKw3oxL-Lu43N2CWOxiWeGL1igrk_F2IFDFLY8knB5rjwOQroH5e6S3p0TSG1U15KjBHQyLb7YQOFXSWltUW7DNwDPt4MGG4pxWUcHyuviyHijeMPWekjI53rULe08DfX-ZXdWOB90QFDJhm7NFJbCryErvqVxyUU1ab1ghyphenhyphenj-qA/s2600/1.png)

## **Treat AI Agents Like First-Class (Non-Human) Users**

Successful security programs already apply "human-grade" controls like birth, life, and retirement to service accounts and machine credentials. [Extending the same discipline to AI agents delivers quick wins](https://astrix.security/use-cases/agentic-ai/?utm_source=google&utm_medium=blog&utm_campaign=ai) without blocking business innovation.

|  |  |
| --- | --- |
| Human Identity Control | How It Applies to AI Agents |
| Owner assignment | Every agent must have a named human owner (for example, the developer who configured a Custom GPT) who is accountable for its access. |
| Least privilege | Start from read-only scopes, then grant narrowly scoped write actions the moment the agent proves it needs them. |
| Lifecycle governance | Decommission credentials the moment an agent is deprecated, and rotate secrets automatically on a schedule. |
| Continuous monitoring | Watch for anomalous calls (e.g., sudden spikes to sensitive APIs) and revoke access in real time. |

## **Secure AI Agent Access**

Enterprises shouldn't have to choose between security and agility.

Astrix makes it easy to protect innovation without slowing it down, delivering all essential controls in one intuitive platform:

### **1. [Discovery and Governance](https://astrix.security/use-cases/nhi-governance/?utm_source=google&utm_medium=blog&utm_campaign=ai)**

Automatically discover and map all AI agents, including external and homegrown agents, with context into their associated NHIs, permissions, owners, and accessed environments. Prioritize remediation efforts based on automated risk scoring based on agent exposure levels and configuration weaknesses.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGSGSfaQeSDHkYlM_8-FJXMgsUZXC96EmSrYfKKnkbRqbYLWu_rgph_wNGaELhDRKe2A3yjmPUW70dD_nIAGvpimHWLXP2BhcYwaFO4NWn-4NDQ4ObzGWQqp_Qr1x8C2RAOUKO-1BaP3erqLIClJUuntn1jgy6H3L9zmAtU4m64Jqqj2puhPWDCCfWbtQ/s2600/2.png)

### **2. [Lifecycle management](https://astrix.security/use-cases/lifecycle-management/?utm_source=google&utm_medium=blog&utm_campaign=ai)**

Manage AI agents and the NHIs they rely on from provisioning to decommissioning through automated ownership, policy enforcement, and streamlined remediation processes, without the manual overhead.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEidcp7ViMHw4ZQtoDid8nSf5b2Pz4S0mxVuCV3C3Hnc9WjQcoQ31CYgwEyFJGZNARkQEkc0DmMkSNxsIKFF0gMNs1BZto4vSX4lqaUx0HhKLzKppBD30mjggsm53AUmfO6HCOgxneKFsTEBWS_C0NH52VfJsnxLl2s-TQ8JQEG_RN3s0WNsFA1DJKTqEYg/s2600/3.png)

### **3. [Threat detection & response](https://astrix.security/use-cases/non-human-itdr/?utm_source=google&utm_medium=blog&utm_campaign=ai)**

Continuously monitor AI agent activity to detect deviations, out-of-scope actions, and abnormal behaviors, while automating remediation with real-time alerts, workflows, and investigation guides.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfAodc-V_sZ9IHa6Z4OoFZJS8G7SVCgsu_r8IM4XHpFIPvmKNPpGCcaERWqkh55Hpokw7ojc6Pqc0KN6lWuFrRhXu6PQxj2eiN_b47fCoUsR2z8S8gus4fhaZHYyCJ0wsIBXrpMC_EcHJEcX0G-Lv29-IVqsel5MBv3Soku-4SjBnQTdydGxSaU2lNNkU/s2600/4.png)

## **The Instant Impact: From Risk to ROI in 30 Days**

Within the first month of deploying Astrix, our customers consistently report three transformative business wins within the first month of deployment:

* **Reduced risk, zero blind spots**

  [Automated discovery](https://astrix.security/product/discover-no...