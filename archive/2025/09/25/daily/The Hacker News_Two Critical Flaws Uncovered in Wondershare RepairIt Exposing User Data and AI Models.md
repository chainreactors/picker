---
title: Two Critical Flaws Uncovered in Wondershare RepairIt Exposing User Data and AI Models
url: https://thehackernews.com/2025/09/two-critical-flaws-uncovered-in.html
source: The Hacker News
date: 2025-09-25
fetch_date: 2025-10-02T20:40:35.637464
---

# Two Critical Flaws Uncovered in Wondershare RepairIt Exposing User Data and AI Models

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

# [Two Critical Flaws Uncovered in Wondershare RepairIt Exposing User Data and AI Models](https://thehackernews.com/2025/09/two-critical-flaws-uncovered-in.html)

**Sep 24, 2025**Ravie LakshmananVulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUpI1_woKGeEOBC3QZqRioClIjmzoEC46RzW5QkC_dkhEfpOnn0QZFkVdOkG4PlK6OYusAhV84YBE-AB_3C-DGsU_tjAVEZPn2gR4E6rgoHOgASoruDML6uRNNy1vXhRjTsVRGfCgWS8haCOh_tcaJFyJPberH4yFoVkZcqCZG_ZPibTm3KHSeylUznS89/s790-rw-e365/software.jpg)

Cybersecurity researchers have disclosed two security flaws in [Wondershare RepairIt](https://repairit.wondershare.com) that exposed private user data and potentially exposed the system to artificial intelligence (AI) model tampering and supply chain risks.

The critical-rated vulnerabilities in question, discovered by Trend Micro, are listed below -

* **[CVE-2025-10643](https://www.zerodayinitiative.com/advisories/ZDI-25-895/)** (CVSS score: 9.1) - An authentication bypass vulnerability that exists within the permissions granted to a storage account token
* **[CVE-2025-10644](https://www.zerodayinitiative.com/advisories/ZDI-25-896/)** (CVSS score: 9.4) - An authentication bypass vulnerability that exists within the permissions granted to an SAS token

Successful exploitation of the two flaws can allow an attacker to circumvent authentication protection on the system and launch a supply chain attack, ultimately resulting in the execution of arbitrary code on customers' endpoints.

Trend Micro researchers Alfredo Oliveira and David Fiser [said](https://www.trendmicro.com/en_us/research/25/i/ai-powered-app-exposes-user-data.html) the AI-powered data repair and photo editing application "contradicted its privacy policy by collecting, storing, and, due to weak Development, Security, and Operations (DevSecOps) practices, inadvertently leaking private user data."

The [poor development practices](https://www.trendmicro.com/vinfo/us/security/news/threat-landscape/real-world-threats-hidden-in-devops) include embedding overly permissive cloud access tokens directly in the application's code that enables read and write access to sensitive cloud storage. Furthermore, the data is said to have been stored without encryption, potentially opening the door to wider abuse of users' uploaded images and videos.

To make matters worse, the exposed cloud storage contains not only user data but also AI models, software binaries for various products developed by Wondershare, container images, scripts, and company source code, enabling an attacker to tamper with AI models or the executables, paving the way for supply chain attacks targeting its downstream customers.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Because the binary automatically retrieves and executes AI models from the unsecure cloud storage, attackers could modify these models or their configurations and infect users unknowingly," the researchers said. "Such an attack could distribute malicious payloads to legitimate users through vendor-signed software updates or AI model downloads."

Beyond customer data exposure and AI model manipulation, the issues can also pose grave consequences, ranging from intellectual property theft and regulatory penalties to erosion of consumer trust.

The cybersecurity company said it responsibly disclosed the two issues through its Zero Day Initiative (ZDI) in April 2025, but not that it has yet to receive a response from the vendor despite repeated attempts. In the absence of a fix, users are recommended to "restrict interaction with the product."

"The need for constant innovations fuels an organization's rush to get new features to market and maintain competitiveness, but they might not foresee the new, unknown ways these features could be used or how their functionality may change in the future," Trend Micro said.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQYZ3buYnJ-GJ4avOD-E0348pT_RU5wSWY_nUJ1drIS8MXo44RBcJ8lAgmbJ_wbtJ5zn91Oja2uo7TENRt3TVIfq3h3AKuuA7ukSLVGSSkukp7N-VcmJ0Ig2C1TffVswtSBxSM1M-HV2U8FxsYhni9rLHbz0HhNNl4v8yyh9PnbcOjuuBxjR66B-iisNhS/s790-rw-e365/ai.png)

"This explains how important security implications may be overlooked. That is why it is crucial to implement a strong security process throughout one's organization, including the CD/CI pipeline."

### The Need for AI and Security to Go Hand in Hand

The development comes as Trend Micro previously warned against exposing Model Context Protocol ([MCP](https://thehackernews.com/2025/04/experts-uncover-critical-mcp-and-a2a.html)) servers [without authentication](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/mcp-security-network-exposed-servers-are-backdoors-to-your-private-data) or [storing sensitive credentials](https://www.trendmicro.com/vinfo/us/security/news/vulnerabilities-and-exploits/beware-of-mcp-hardcoded-credentials-a-perfect-target-for-threat-actors) such as MCP configurations in plaintext, which threat actors can exploit to gain access to cloud resources, databases, or inject malicious code.

Each MCP server acts as an open door to its data source: databases, cloud services, internal APIs, or project management systems," the researchers said. "Without authentication, sensitive data such as trade secrets and customer records becomes accessible to everyone."

In December 2024, the company also [found](https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/silent-sabotage-weaponizing-ai-models-in-exposed-containers) that exposed container registries could be abused to gain unauthorized access and pull target Docker images to extract the AI model within it, modify the model's parameters to influence its predictions, and push the tampered image back to the exposed registry.

"The tampered model could behave normally under typical conditions, only displaying its malicious alterations when triggered by specific inputs,...