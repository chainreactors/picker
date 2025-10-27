---
title: Announcing public preview: Phishing triage agent in Microsoft Defender
url: https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/announcing-public-preview-phishing-triage-agent-in-microsoft-defender/4438301
source: Microsoft Security Blog
date: 2025-08-08
fetch_date: 2025-10-07T00:16:15.202170
---

# Announcing public preview: Phishing triage agent in Microsoft Defender

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Microsoft Learn](/category/MicrosoftLearn)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoftthreatprotectionblog%2Fannouncing-public-preview-phishing-triage-agent-in-microsoft-defender%2F4438301)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoftthreatprotectionblog%2Fannouncing-public-preview-phishing-triage-agent-in-microsoft-defender%2F4438301)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Defender XDR](/category/microsoft-defender-xdr)
7. [Microsoft Defender XDR Blog](/category/microsoft-defender-xdr/blog/microsoftthreatprotectionblog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDM4MzAxLXQ2ZGVOVw?revision=8&image-dimensions=2000x2000&constrain-image=true)

Microsoft Defender XDR Blog

6 MIN READ

# Announcing Public Preview: Phishing Triage Agent in Microsoft Defender

[![cristinadagamah's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0yOTQ0NDgzLW1NTGczRA?image-coordinates=72%2C304%2C591%2C823&image-dimensions=50x50)](/users/cristinadagamah/2944483)

[cristinadagamah](/users/cristinadagamah/2944483)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Aug 06, 2025

## Intelligent triage for a more agile, autonomous SOC

At Microsoft Secure 2025, we [introduced](https://techcommunity.microsoft.com/blog/microsoftthreatprotectionblog/what%E2%80%99s-new-in-microsoft-defender-xdr-at-secure-2025/4390817) a new wave of innovations across Microsoft Defender aimed at redefining what AI can do for security operations. At the center of these announcements was the [launch of 11 Security Copilot agents](https://techcommunity.microsoft.com/blog/SecurityCopilotBlog/automate-cybersecurity-at-scale-with-microsoft-security-copilot-agents/4394675/), each purpose-built to reduce manual workload and accelerate response through autonomous, adaptive automation. Integrated into existing Microsoft Security infrastructure, they continuously learn and adapt to your unique environment, while keeping your team in control for proactive, end-to-end protection.

Among these is the Phishing Triage Agent in Microsoft Defender, now available in Public Preview. It tackles one of the most repetitive tasks in the SOC: handling reports of user-submitted phish. Instead of manually combing through endless submission, security teams can now rely on an agent that triages thousands of alerts each day, typically within 15 minutes of detection. Early adopters are already seeing accelerated threat response and significant time savings.

## Phishing: A top threat and a burden for SOC analysts

Phishing continues to be one of the most pervasive entry points for threat actors, with over 90% of breaches starting from email-based deception. In just twelve months, [Microsoft Defender for Office 365 detected more than 775 million malware-laced emails](https://www.microsoft.com/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2024), underscoring the relentless, large-scale nature of the threat. While today’s security tools are highly effective at blocking most of these attempts, attackers aren’t standing still. They continuously adapt—tweaking content, spoofing identities, changing tactics, and exploiting new channels to slip past defenses. Increasingly, they’re also using generative AI to craft phishing messages that appear more legitimate and personalized, making detection even harder. As a result, a small but dangerous number of phishing emails still manage to slip through and reach users’ inboxes.

When users report these suspicious messages, they land in SOC queues for further review, creating a significant operational burden for security teams. Most submissions are false alarms, yet analysts must still manually review each one to catch the rare threats buried in the noise. This delays response, drains focus, and raises the risk of a dangerous miss.

## Behind the agent: smarter phishing triage

#### Built to operate autonomously

The Phishing Triage Agent marks a meaningful step forward in autonomous security operations. Powered by large language models (LLMs), it performs sophisticated assessments—including semantic evaluation of email content, URL and file inspection, and intent detection—to determine whether a submission is a true phishing threat or a false alarm. Unlike traditional systems based on static rules or pre-coded logic, the agent dynamically interprets the context and artifacts of each email to reach an independent verdict. It is autonomous defense working behind the scenes, cutting through the noise and elevating what truly matters.

#### Learning from feedback

Equally transformative is the agent’s ability to learn. Rather than relying on fixed conclusions, the Phishing Triage Agent continuously evolves. Analysts can reclassify incidents and provide natural language feedback explaining why a particular verdict was correct or not. The agent incorporates this input, refining its reasoning and adapting to the organization’s specific needs, patterns, and nuances. With every interaction, it becomes more accurate and better attuned to its environment, creating a feedback loop that drives ongoing improvement.

#### Transparent by design

One of the most defining features of the Phishing Triage Agent is how clearly it communicates its decisions. For every verdict, the agent provides a natural language explanation that outlines why a message was or wasn’t classified as phishing. The rationale is clear and accessible, allowing analysts to quickly comprehend what led to the outcome.

For those seeking deeper understanding, the agent also produces a visual map of its decision logic: a step-by-step breakdown of how it evaluated the submission. Each phase is presented as an expandable card within a structured diagram, detailing the signals analyzed, evidence collected, and logic applied. Teams can drill into any step to view the agent’s reasoning in context, making the entire process traceable and reviewable from start to finish. This level of transparency isn’t just helpful, it’s essential for building trust in autonomous security systems.

## How the agent works

#### Quick setup and seamless integration

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDM4MzAxLUlSTVRNSg?image-dimensions=744x434&revision=8)

Getting started is simple. The onboarding experience provides a clear overview of the agent’s capabilities and how it functions in your environment. It can be configured with a dedicated identity and role-based access controls that follow least privilege principles, ensuring it operates strictly within its assigned scope.

Administrators retain full control. They can view, manage, and restrict the agent’s actions, keeping its behavior aligned with the organization’s security policies and standards.

#### Autonomous operation in the background

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDM4MzAxLUZpTW5DQQ?image-dimensions=853x480&revision=8)

Once deployed, the agent operates in the background, automatically triggering whenever a user reports a suspicious email. As new submissions come in, it analyzes each one and assigns a classification. In most organizations, more than 90% of reported emails turn out to be false positives. The agen...