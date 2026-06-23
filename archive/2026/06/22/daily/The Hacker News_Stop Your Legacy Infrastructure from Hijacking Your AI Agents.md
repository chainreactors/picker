---
title: Stop Your Legacy Infrastructure from Hijacking Your AI Agents
url: https://thehackernews.com/2026/06/stop-your-legacy-infrastructure-from.html
source: The Hacker News
date: 2026-06-22
fetch_date: 2026-06-23T06:08:26.213886
---

# Stop Your Legacy Infrastructure from Hijacking Your AI Agents

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Stop Your Legacy Infrastructure from Hijacking Your AI Agents](https://thehackernews.com/2026/06/stop-your-legacy-infrastructure-from.html)

**The Hacker News**Jun 22, 2026Exposure Management / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSdS_7552zEvsn5xVfDcVMG2u8ponFIE1E65j5A8Wx-qUroU49h-f6qF7FPCABA063IjNnw-JntL-L1iZjHpiuqATqkDv-2vpi6lCVG1idXkg_elRJkyoUgASk4uYCTJ95EHfVQLJngVLKOxM2H5zLkdeFY7kpzveHUuKFoks0_ujNo9tJNQxm7XVgYb4/s1700-e365/xmcyber.jpg)

Earlier this month, I spoke at the [Gartner Security & Risk Management Summit](https://www.gartner.com/en/conferences/na/security-risk-management-us) about a blind spot most security programs are still not accounting for - how attackers are circumventing AI security programs by using legacy infrastructure to hijack AI agents.

AI adoption is moving faster than security programs can account for. Roughly 71% of organizations are piloting AI agents across their enterprise applications, and 31% have already moved them into production workflows.

For this reason, organizations are legitimately pouring resources into securing AI workloads against model poisoning, prompt injection, data leakage, and other emerging threats. Yet this focus misses everything *underneath* the AI layer. Because an unpatched server, a misconfigured Active Directory permission, or a cached credential on a developer's machine are exposures that give attackers a direct route to everything your AI agents depend on - knowledge bases, cloud storage, Lambda functions, SaaS integrations, and the credentials that connect them.

This means that threat actors don’t really need to attack your AI head-on - *they just need to reach what it connects to.* In this article, I'll walk through how legacy infrastructure becomes the attack path into AI agent environments and what security teams can do to block those paths.

## **AI Agents Use What They Inherit**

Despite their novelty and power, in some ways AI agents operate like other assets in your environment. They authenticate through existing identity providers, store data in existing cloud buckets, execute tasks through existing Lambda functions, and inherit permissions from existing IAM roles. Every one of those dependencies carries whatever security debt the organization had before the AI deployment started.

What’s more, most organizations are inadvertently *compounding* that debt. According to [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/overprivileged-ai-45-times-higher/), 70% of organizations grant their AI systems *more* privileged access than a human in the same role. Not surprisingly, this comes with a painful price tag. Organizations with over-privileged AI reported a 76% incident rate, compared to just 17% for those enforcing least privilege.

All of those connections - identity providers, cloud buckets, Lambda functions, IAM roles - run through the infrastructure your teams have managed for years: Active Directory, cloud IAM, service accounts, stored credentials. Yet none of it was designed with AI agents in mind, and most of it was provisioned long before the first agent went into production. The result is that an attacker who finds their way in through any of those layers doesn't need to touch the AI. The agent's own permissions do the work for them.

## **How a CVE from 2025 Hijacks an AI Agent in 2026**

The diagram below shows a typical enterprise AI agent architecture. A customer success team uses an AI-powered Co-Pilot - hosted on AWS Bedrock - to query customer data exported from Salesforce into an S3 bucket. The Co-Pilot executes tasks through Lambda functions and integrates with business applications. John, a developer, builds and maintains the agent. Users across the organization interact with it daily.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtq2sXOxN2xCbuERqpNh4NYGBG7A1U5PZQKuQJyxiBmKzf8S6tpbN5eXPajK0kygVuLJJNagrDP3CTCDQtfYCB23xeyQIhyphenhyphenjOMDb-nzlHSvMfxFllux2alKSAsQRSjT94RfOXCo7-4uzc4ml8zaJZ0KPG8Nj7h32aE5wIegbqRdS4ktweZUYnKKozfFPg/s1700-e365/1.png)

Now here's what happens when an attacker finds a way in. The following diagram shows an attack path my team modeled in a real enterprise environment. None of these exposures are exotic - they exist, in some combination, in most enterprise networks right now. What makes them dangerous is how they connect. Here is how the attack developed, stage-by-stage.

* **Stage 1: An S3 bucket becomes a critical asset.** To feed the CSM Co-Pilot, the team exported Salesforce data into an S3 bucket. That export turned the bucket into a high-value target holding sensitive customer records. Multiple users across the AWS account received overly broad read access to production S3 buckets - including John, the Co-Pilot developer, who never needed access to production data. On its own, this is a simple permissions misconfiguration.
* **Stage 2: An unpatched server on the perimeter.** An external-facing server runs Apache Tomcat. That server is exposed to [CVE-2025-24813](https://nvd.nist.gov/vuln/detail/CVE-2025-24813) - a remote code execution flaw disclosed in March 2025 and added to CISA's Known Exploited Vulnerabilities catalog the same month. It was never patched. Because the server sits in the enterprise environment and is joined to Active Directory, an attacker who exploits the vulnerability can dump cached credentials from server memory and compromise an AD user account. In isolation, this is a known vulnerability on a single server - serious, but not critical.

  [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4wtPMzt5TBw_hkVktUro7qow4bjOzxTpmo0O7VxfFaSgheN2NN0tkzbHs5BNxKbsxrzxXxD3QOugD0Q1DK7EAdACb9qVV2bGjifJiNS8MuTsRdsZ1F3_2VsTxozWY5zqYZBZ9GJ3gVoL0x8Isegy2a46bPT8IYBtfmarvNWwz_rrJ0iYiVkawd7Ohc1Q/s1700-e365/2.png)
* **Stage 3: Active Directory misconfiguration enables lateral movement.** That compromised AD accou...