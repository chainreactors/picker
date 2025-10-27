---
title: Unit 42 Develops Agentic AI Attack Framework
url: https://www.paloaltonetworks.com/blog/2025/05/unit-42-develops-agentic-ai-attack-framework/
source: Palo Alto Networks Blog
date: 2025-05-15
fetch_date: 2025-10-06T22:31:18.809467
---

# Unit 42 Develops Agentic AI Attack Framework

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [Products and Services](https://www.paloaltonetworks.com/blog/category/products-and-services/)
* Unit 42 Develops Agentic ...

# Unit 42 Develops Agentic AI Attack Framework

Link copied

By [Sam Rubin](/blog/author/sam-rubin/ "Posts by Sam Rubin")

May 14, 2025

11 minutes

[Products and Services](/blog/category/products-and-services/)

[Agentic AI](/blog/tag/agentic-ai/)

[AI](/blog/tag/ai/)

[attack chain](/blog/tag/attack-chain/)

[Attack Simulations](/blog/tag/attack-simulations/)

### Unit 42 outlines how Agentic AI capabilities can be leveraged by attackers to increase the speed of attacks 100x.

The integration of AI into adversarial operations is fundamentally reshaping the speed, scale and sophistication of attacks. As [AI defense capabilities](/blog/2025/04/deploy-with-prisma-airs/) evolve, so do the AI strategies and tools leveraged by threat actors, creating a rapidly shifting threat landscape that outpaces traditional detection and response methods. This accelerating evolution necessitates a critical examination for CXOs into how threat actors will strategically weaponize AI across each phase of the attack chain.

One of the most alarming shifts we have seen, following the introduction of AI technologies, is the dramatic drop in mean time to exfiltrate (MTTE) data, following initial access. In 2021, the average MTTE stood at nine days. According to our [Unit 42 2025 Global Incident Response Report](/engage/unit42-2025-global-incident-response-report), by 2024 MTTE dropped to two days. In one in five cases, the time from compromise to exfiltration was less than 1 hour.

In our testing, Unit 42 was able to simulate a ransomware attack (from initial compromise to data exfiltration) in just 25 minutes using AI at every stage of the attack chain. That’s a *100x increase in speed, powered entirely by AI*.

##### Recent threat activity observed by Unit 42 has highlighted how adversaries are leveraging AI in attacks:

* Deepfake-enabled social engineering has been observed in campaigns from groups like Muddled Libra (also known as Scattered Spider), who have used AI-generated audio and video to impersonate employees during help desk scams.
* [North Korean IT workers](https://unit42.paloaltonetworks.com/north-korean-synthetic-identity-creation/) are using real-time deepfake technology to infiltrate organizations through remote work positions, which poses significant security, legal and compliance risks.
* Attackers are leveraging generative AI to conduct ransomware negotiations, breaking down language barriers and more effectively negotiating higher ransom payments.
* AI-powered productivity assistants are being used to identify sensitive credentials in victim environments.

A significant evolution is the emergence of Agentic AI – autonomous systems capable of making decisions, learning from outcomes, problem solving and iteratively improving their performance without human intervention. These systems have the potential to independently execute multistep operations, from identifying targets to adapting tactics midattack. This makes them especially dangerous. As agentic models become more accessible, you can expect a surge in automated, self-directed cyberattacks that are faster, more adaptive and increasingly difficult to contain.

#### Palo Alto Networks Unit 42 has been researching and developing an Agentic AI Attack framework that demonstrates how these capabilities can execute attacks with minimal input from the attacker.

Through our research, we are able to demonstrate just how easily this technology could be turned against enterprises and execute attacks with unprecedented speed and scale. Over time, Unit 42 will integrate these capabilities into our [purple teaming](/unit42/assess/purple-teaming) exercises, so you can test and improve your organization’s defenses against Agentic AI attacks.

The emergence of Agentic AI is not just a theoretical risk; it’s an accelerating reality that will challenge how your organization approaches threat detection, response and mitigation.

## The Agentic AI Attack Chain

Unit 42 believes that attackers will leverage Agentic AI to create purpose-built agents with expertise in specific attack stages. When chained together, these AI agents can autonomously test and execute attacks, adjusting tactics in real time, based on feedback. In the near future, we expect to see the rise of a new class of adversaries powered by Agentic AI. These Agentic AI attackers won’t just assist with parts of an attack but can plan, adapt and execute full campaigns, end-to-end with minimal human direction.

Below, we break down how Agentic AI will reshape key tactics in the attack chain, through the lens of what Unit 42 is seeing in the wild, and how to help defend against them.

## Reconnaissance AI Agent — Always Watching, Always Learning

**Traditional Recon:** Recon was often a one-and-done step – run some scripts, scrape LinkedIn, check GitHub and maybe do some passive DNS work. It was time-bound, manual and noisy.

**Agentic AI Recon:** Recon agents operate persistently and autonomously. They self-prompt: “What data do I need to identify a weak point in this org?” Then they go collect it from social media, breach data, exposed APIs and cloud misconfigurations. If a target changes (new hire, new vendor portal, leaked key) the agent re-evaluates and updates its strategy.

**Example:** An agent selects a target organization and constantly scans job postings from that organization. It finds some job listings and infers that the company uses SAP. It checks subdomains, finds a staging SAP server and matches it to a recent CVE. It then shifts to LinkedIn, identifies midlevel IT staff and flags them for phishing, adapting its recon strategy on the fly.

## Initial Access AI Agent — Personalized, Multi-Channel Intrusion

**Traditional Initial Access:** Attackers focus on tactics, like mass phishing, credential stuffing or vulnerability scanning. If one method didn’t work, the campaign often failed or required manual retargeting.

**Agentic AI Initial Access:** Agentic systems don’t just try once. They generate phishing lures using LLMs tailored to individual targets with tone, language and context. If the first attempt fails, they self-prompt: “What alternative channels or messaging might work better?” Then they try again via SMS, LinkedIn or a fake video conferencing invite. Exploitation attempts are just as adaptive with AI matching CVEs to detected tech stacks in real-time.

**Example:** A CFO ignores an initial phishing email. The agent rewrites the message in a more casual tone, references a recent company press release, and delivers it via a spoofed Microsoft Teams chat, thus improving its odds with every iteration.

## Execution AI Agent — Smart Payloads That Wait and Learn

**Traditional Execution:** Payloads used to execute as soon as they were triggered. There was no context check, no real-time decision-making. And there was a high risk of getting caught in a sandbox.

**Agentic AI Execution:** Execution agents can observe before acting. They check where they are, who the user is and what security tools are active, then select an appropriate execution path. If one method fails (e.g., a blocked script, restricted privileges), the agent prompts itself: “What’s the next viable path?” Then, it tries again.

**Example:** A payload lands on a user’s machine, but pauses execution. The agent checks: “Is the user in finance? Is EDR active? Is it business hours?” Based on the answers, it decides to inject into a trusted process and delay execution until the user opens Outlook, blending into normal behavior to avoid detection.

## Persistence AI Agent — Living Long and Quietly

**Traditional Persistence:** Persistence used to rely on one or two techniques – scheduled tasks, registry keys, startup folder implant...