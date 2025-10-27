---
title: Mitigating prompt injection attacks with a layered defense strategy
url: http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html
source: Google Online Security Blog
date: 2025-06-14
fetch_date: 2025-10-06T22:50:46.094223
---

# Mitigating prompt injection attacks with a layered defense strategy

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Mitigating prompt injection attacks with a layered defense strategy](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html "Mitigating prompt injection attacks with a layered defense strategy")

June 13, 2025

Posted by Google GenAI Security Team

With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve hidden malicious instructions within external data sources. These may include emails, documents, or calendar invites that instruct AI to exfiltrate user data or execute other rogue actions. As more governments, businesses, and individuals adopt generative AI to get more done, this subtle yet potentially potent attack becomes increasingly pertinent across the industry, demanding immediate attention and robust security measures.

At Google, our teams have a longstanding precedent of investing in a defense-in-depth strategy, including robust evaluation, threat analysis, [AI security best practices](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/), [AI red-teaming](https://blog.google/technology/safety-security/googles-ai-red-team-the-ethical-hackers-making-ai-safer/), adversarial training, and model hardening for generative AI tools. This approach enables safer adoption of [Gemini in Google Workspace](https://workspace.google.com/solutions/ai/) and the [Gemini app](https://blog.google/products/gemini/) (we refer to both in this blog as “Gemini” for simplicity). Below we describe our prompt injection mitigation product strategy based on extensive research, development, and deployment of improved security mitigations.

### A layered security approach

Google has taken a layered security approach introducing security measures designed for each stage of the prompt lifecycle. From Gemini 2.5 model hardening, to purpose-built machine learning (ML) models detecting malicious instructions, to system-level safeguards, we are meaningfully elevating the difficulty, expense, and complexity faced by an attacker. This approach compels adversaries to resort to methods that are either more easily identified or demand greater resources.

Our model training with adversarial data significantly enhanced our defenses against indirect prompt injection attacks in Gemini 2.5 models ([technical details](https://storage.googleapis.com/deepmind-media/Security%20and%20Privacy/Gemini_Security_Paper.pdf)). This inherent model resilience is augmented with additional defenses that we built directly into Gemini, including:

1. Prompt injection content classifiers
2. Security thought reinforcement
3. Markdown sanitization and suspicious URL redaction
4. User confirmation framework
5. End-user security mitigation notifications

This layered approach to our security strategy strengthens the overall security framework for Gemini – throughout the prompt lifecycle and across diverse attack techniques.

1. Prompt injection content classifiers

Through collaboration with leading AI security researchers via [Google's AI Vulnerability Reward Program (VRP)](https://bughunters.google.com/about/rules/google-friends/5238081279623168/abuse-vulnerability-reward-program-rules), we've curated one of the world’s most advanced catalogs of generative AI vulnerabilities and adversarial data. Utilizing this resource, we built and are in the process of rolling out proprietary machine learning models that can detect malicious prompts and instructions within various formats, such as emails and files, drawing from real-world examples. Consequently, when users query Workspace data with Gemini, the content classifiers filter out harmful data containing malicious instructions, helping to ensure a secure end-to-end user experience by retaining only safe content. For example, if a user receives an email in Gmail that includes malicious instructions, our content classifiers help to detect and disregard malicious instructions, then generate a safe response for the user. This is in addition to built-in defenses in Gmail that automatically block more than 99.9% of spam, phishing attempts, and malware.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXePgxMV37fyKPlpp54xFHVtYLigC9Tt32y2B8dOEjRDzvL2xiwN9vx0-oNwPO19CMMNGHovtXa4dLS97sZSJICODbOrCyvKIOivcR_oJzTwM2SFG8DdFIoZPzKOvrV05G7_0fMSQw?key=qBd-QKEP_GpIw65Q_IOEgQ)

A diagram of Gemini’s actions based on the detection of the malicious instructions by content classifiers.

2. Security thought reinforcement

This technique adds targeted security instructions surrounding the prompt content to remind the large language model (LLM) to perform the user-directed task and ignore any adversarial instructions that could be present in the content. With this approach, we steer the LLM to stay focused on the task and ignore harmful or malicious requests added by a threat actor to execute indirect prompt injection attacks.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSfilVHvpF2aOIIc5I2S0mobMGoRwXb85XXRdyCq_j2ylJ30oAaY7KrIYtpcHWs21MxkrOtT1_zpVy-R4CSk3owlx896fckltob_Fc7t7K2TYk7XZjVMWDCY-O8RE4l9QbXxKK5w?key=qBd-QKEP_GpIw65Q_IOEgQ)

A diagram of Gemini’s actions based on additional protection provided by the security thought reinforcement technique.

3. Markdown sanitization and suspicious URL redaction

Our markdown sanitizer identifies external image URLs and will not render them, making the “EchoLeak” 0-click image rendering exfiltration [vulnerability](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2025-32711) not applicable to Gemini. From there, a key protection against prompt injection and data exfiltration attacks occurs at the URL level. With external data containing dynamic URLs, users may encounter unknown risks as these URLs may be designed for indirect prompt injections and data exfiltration attacks. Malicious instructions executed on a user's behalf may also generate harmful URLs. With Gemini, our defense system includes suspicious URL detection based on [Google Safe Browsing](https://safebrowsing.google.com/) to differentiate between safe and unsafe links, providing a secure experience by helping to prevent URL-based attacks. For example, if a document contains malicious URLs and a user is summarizing the content with Gemini, the suspicious URLs will be redacted in Gemini’s response.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeOQ69HwjpDYi9jCb_8alM2rBNC09Kx124kotYR8xzNSXygaNI-2eMBVdMYiBJ_aH-9tGFuXXphLbCg_g74nzI9VsEuSxpLrBGuwkjH2vt2j-WAgJz0dyD1EJt6qGugfBMtTHjPnqU?key=qBd-QKEP_GpIw65Q_IOEgQ)

Gemini in Gmail provides a summary of an email thread. In the summary, there is an unsafe URL. That URL is redacted in the response and is replaced with the text “suspicious link removed”.

4. User confirmation framework

Gemini also features a contextual user confirmation system. This framework enables Gemini to require user confirmation for certain actions, also known as “Human-In-The-Loop” (HITL), using these responses to bolster security and streamline the user experience. For example, potentially risky operations like deleting a calendar event may trigger an explicit user confirmation request, thereby helping to prevent undetected or immediate execution of the operation.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXegtOKYti58PeD2EGB9-tpYShPjKYJdHcv7I5u4s9WL0ZkzZy2P95ETc-RkdU1YUZWtNat9-WhfF5aekjmUiKxLNlV5yUYXUsTiXXj_RjmPd2Z50u4cUuwhFndXU5GslBudLDkGspk?key=qBd-QKEP_GpIw...