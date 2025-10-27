---
title: DeepSeek Unveiled — Exposing the GenAI Risks Hiding in Plain Sight
url: https://www.paloaltonetworks.com/blog/2025/02/deepseek-unveiled-exposing-genai-risks-hiding-in-plain-sight/
source: Palo Alto Networks Blog
date: 2025-03-01
fetch_date: 2025-10-06T22:01:37.771203
---

# DeepSeek Unveiled — Exposing the GenAI Risks Hiding in Plain Sight

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [AI Security](https://www.paloaltonetworks.com/blog/category/ai-security/)
* DeepSeek Unveiled — Expos...

# DeepSeek Unveiled — Exposing the GenAI Risks Hiding in Plain Sight

Link copied

By [Charles Choe](/blog/author/charles-choe/ "Posts by Charles Choe") and [Himani Singh](/blog/author/himani-singh/ "Posts by Himani Singh")

Feb 28, 2025

5 minutes

[AI Security](/blog/category/ai-security/)

[Must-Read Articles](/blog/security-operations/category/must-read-articles/)

[News & Events](/blog/sase/category/news-events/)

[Reports](/blog/category/reports/)

[Vulnerability Exposed](/blog/category/vulnerability-exposed/)

[DeepSeek](/blog/tag/deepseek/)

[GenAI](/blog/tag/genai/)

The generative AI (GenAI) landscape is evolving at breakneck speed, and with it, the challenges for enterprise security. DeepSeek’s R1 model, released on January 20, 2025, gained rapid popularity due to its high performance and cost-efficiency. It rivaled established AI models at a fraction of the cost. The open-source nature of DeepSeek also allowed AI developers to use it for free, contributing to its swift rise in app stores and industry rankings.

Following the R1 release, Palo Alto Networks observed a 1,800% spike in DeepSeek traffic across our platform. This sudden surge serves as a stark reminder that new AI tools can rapidly penetrate your organization, potentially outpacing your existing security measures.

## The Hidden Dangers of DeepSeek

DeepSeek's popularity stems from its ability to process complex prompts and deliver insightful results. However, this convenience comes at a cost. The DeepSeek-R1 model has recently been implicated in several high-profile [security incidents](https://www.csoonline.com/article/3813224/deepseek-leaks-one-million-sensitive-records-in-a-major-data-breach.html), exposing [critical vulnerabilities](https://krebsonsecurity.com/2025/02/experts-flag-security-privacy-risks-in-deepseek-ai-app/) that can jeopardize enterprise data. Moreover, DeepSeek's open-source availability and strong performance could lower the barrier to entry for malicious actors using AI for attacks, further highlighting the need for AI Security.

Even if companies decide to ban DeepSeek outright, the problem doesn’t end there. Without enforcement controls, employee training and the proper security mechanisms in place, employees may inevitably gravitate to what’s useful (even if banned) without realizing its security implications.

* **Shadow AI Poses a Hidden Threat** – The unauthorized use of GenAI tools creates uncertainties for IT security teams, making it nearly impossible to track AI-based threats and data loss vectors.
* **Inadequate Data Handling Practices** – Regulators in multiple countries are taking action for [concerns over DeepSeek’s data handling practices](https://www.bankinfosecurity.com/security-researchers-warn-new-risks-in-deepseek-ai-app-a-27486). These concerns include unauthorized data access, surveillance and possible threats to national security.
* **Susceptibility to Jailbreaking** – The Bad Likert Judge, Crescendo and Deceptive Delight jailbreaks [bypassed DeepSeek LLM’s safety mechanisms](https://unit42.paloaltonetworks.com/jailbreaking-deepseek-three-techniques/), making it vulnerable to manipulation.

## How to Navigate GenAI Risks

While it can be challenging to guarantee complete protection against all adversarial techniques for a specific LLM, organizations can [implement measures](/blog/2025/01/deepseek-rise-shows-ai-security-remains-moving-target/) to help monitor when and how employees use apps like DeepSeek. That’s the goal we had in mind when we rolled out [AI Access Security](/network-security/ai-access-security).

Organizations’ Capabilities with AI Access Security:

* **Gain real time visibility** into what GenAI applications are being used across your organization and by whom.
* **Protect sensitive data** from unauthorized access and exposure to risky GenAI apps and its training models.
* **Streamline access controls** with the ability to block unsanctioned apps, apply InfoSec policies and protect against threats.

We understand that AI is a powerful enabler of innovation. That's why AI Access Security is designed to be a business enabler, not a roadblock. By providing visibility and control of GenAI apps, like DeepSeek, we empower IT security teams to take control when balancing AI innovation with security.

## Going Beyond Visibility — Addressing the Core Risks

With AI Access Security, new GenAI apps are automatically categorized as unsanctioned, enabling organizations with low risk tolerance to proactively block unvetted apps by default. As for DeepSeek chat, we observed a 26% block rate during the period from January 1 to February 10, 2025.

Whether you choose to block DeepSeek outright or allow its use with established guardrails (e.g., InfoSec policies for deepseek-api, deepseek-chat, and/or deepseek-platform), visibility is the first step to [GenAI risk mitigation](/resources/guides/the-c-suite-guide-to-genai-risk-management).

![Screenshot of plugins, threats and sensitive data assets.](/blog/wp-content/uploads/2025/02/Image-2-view-230x148.png)

AI Access Security dashboard with DeepSeek identified as a use case.

With an industry-leading catalog of over 1,850 GenAI apps and insight into 70+ application attributes, AI Access Security accurately discovers shadow AI apps, monitors user activity, dynamically assesses risk and provides security best practices out-of-the-box. Attributes (e.g., privacy terms and conditions, input/output modes, interface support, compliance checks and information on whether data is used in training models) all contribute to bespoke AI risk scores.

![Screenshot of DeepSeek chat.](/blog/wp-content/uploads/2025/02/Image-3-230x125.png)

Insight into DeepSeek with additional details on application attributes

With DeepSeek, some of the top risk factors identified include data used for model training and compliance. Consequently, any uncontrolled DeepSeek usage can result in noncompliance with [GDPR](/cyberpedia/gdpr-compliance), [CCPA](/cyberpedia/ccpa), [HIPAA](/cyberpedia/what-is-hipaa) and other industry-specific regulations.

What’s more, GenAI app details can also include information on personal instances, interconnected apps, and even AI plugins and extensions via SaaS marketplaces. With a centralized view of all AI activity, you can confidently enforce policies, identify risky behavior and respond to incidents promptly.

## Your Best Defense Is to Fight AI with AI

AI Access Security utilizes a fundamentally different approach specifically designed for the AI era. Instead of simply monitoring DeepSeek usage, we focus on securing access to DeepSeek and the data they handle, regardless of where the user or application is located.

![Screenshot of data loss prevention.](/blog/wp-content/uploads/2025/02/word-image-335758-5.png)

DLP Incidents page with credit card information blocked within DeepSeek chats.

Palo Alto Networks provides 100+ Deep Neural Network (DNN) based classifiers out-of-the-box to automate data discovery and classification. These models train in a wide range of languages to interpret semantics with contextual understanding for near-perfect accuracy. With these AI-powered improvements, sensitive data shared within conversational DeepSeek chats can be quickly identified and blocked.

Moreover, AI Access Security provides AI-driven contextual policy recommendations with guided workflows via the [Strata copilot](/blog/network-security/introducing-strata-copilot/) to simplify operations. Intelligent AI-powered capabilities, combined with real-time end user coaching, is an effective strategy to mitigate GenAI risks.

## The Future of AI Security Is Here

AI is not slowing down and neither should your security strategy. The rapid adoption of DeepSeek serve...