---
title: Charting the future of SOC: Human and AI collaboration for better security
url: https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/charting-the-future-of-soc-human-and-ai-collaboration-for-better-security/4470688
source: Microsoft Security Blog
date: 2025-11-25
fetch_date: 2025-11-26T03:12:53.714787
---

# Charting the future of SOC: Human and AI collaboration for better security

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Skills Hub](/category/skills-hub)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoftsecurityexperts%2Fcharting-the-future-of-soc-human-and-ai-collaboration-for-better-security%2F4470688)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoftsecurityexperts%2Fcharting-the-future-of-soc-human-and-ai-collaboration-for-better-security%2F4470688)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Security](/category/microsoft-security-product)
7. [Microsoft Security Experts Blog](/category/microsoft-security-product/blog/microsoftsecurityexperts)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDcwNjg4LW1KQWlEMA?revision=8&image-dimensions=2000x2000&constrain-image=true)

Microsoft Security Experts Blog

6 MIN READ

# Charting the Future of SOC: Human and AI Collaboration for Better Security

[![Sylvie_Liu's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0xMDM3Mzc5LUh1elc0Qw?image-coordinates=0%2C180%2C1080%2C1260&image-dimensions=50x50)](/users/sylvie_liu/1037379)

[Sylvie\_Liu](/users/sylvie_liu/1037379)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Nov 18, 2025

##### **Co-authors:**

**Sylvie Liu, Principal Product Manager**

**Rajiv Bharadwaja, Principal Software Engineering Manager**

**Abhishek Kumar, Principal Group Manager - Security Research & Operations**

Security operations centers are under pressure from unprecedented scale and complexity. Speed, precision, and consistency matter more than ever, and AI is everywhere—but hype alone doesn’t solve the challenge. This blog shares our journey and insights from building autonomous AI agents for MDR operations and explores how the shift to a GenAI-powered SOC redefines collaboration between humans and AI.

Beyond our managed services, [Microsoft Defender Experts](https://www.microsoft.com/en-us/security/business/services/microsoft-defender-experts-xdr) strive to be a trusted partner in SOC evolution, helping customers across the broader security ecosystem to anticipate process changes, plan for upskilling, and adopt agentic workflows with confidence.

## From Vision to Reality: Building the SOC of the Future

Attackers are evolving at unprecedented speed, using AI to outpace defenses scale. Defender Experts is pioneering the transformation to build the SOC of the future by integrating advanced AI capabilities into our SOC workflows, which is critical for today’s threat landscape. We’ve seen AI deliver real results—in our earlier [blog](https://techcommunity.microsoft.com/blog/microsoftsecurityexperts/how-microsoft-defender-experts-uses-ai-to-cut-through-the-noise/4443601), we shared how Defender Experts applies AI to cut through noise without compromising on detecting real threats, enabling 50% of noise to be triaged automatically with high precision.

Autonomous AI agents are foundational to the SOC of the future. Our vision is a predictive, adaptive model where agentic AI and automation remove manual toil, accelerate contextual insight, and execute both single tasks and complex workflows. Analysts are elevated, acting as orchestrators of governed action, driving high-impact decisions, and continuously tuning the system for transparency and trust. Agents handle repetitive, time-intensive tasks, while humans remain the final authority for strategic outcomes. Together, this creates a SOC that moves from reactive alert handling to proactive, explainable defense. It is always auditable and under human governance.

## How Microsoft Defender Experts is Pioneering This Shift

Defender Experts builds autonomous AI agents with expert knowledge, expert-defined guardrails and human-in-the-loop validation to deliver structured, trustworthy outputs that accelerate investigations without compromising quality. These AI agents are designed to drive efficiency and consistency across our MDR operations, helping us respond to the threats faster and with confidence.

As we advance this model, we’re not only improving speed and precision, we’re redefining our security operations. That means rethinking SOC analyst roles, skill composition, workflow design, the tooling support, the accompanying automation, and the evaluation and monitoring systems needed to maintain trust.

Abhishek Kumar, lead of the Defender Experts security operations team, is deeply engaged in this transformation as we build the GenAI-powered SOC. From Abhishek’s perspective “This is an exciting era for anyone in security research and operations. We are seeing a monumental shift where security analysts and threat hunters are elevating the role from handling routine tasks, to delivering high value insights. AI agents are rapidly reducing analyst fatigue and freeing up essential time, allowing experts to focus on critical thinking and contextual analysis of incidents."

Agents are not just a productivity leap, they're enabling analysts and hunters to better investigate emerging and hidden threats, develop more hypotheses, and connect clues to unravel complex campaigns. Time once spent on repetitive work is now devoted to advanced tasks like posture data analysis, traversing security graphs, and using cross-product intelligence to uncover novel threats and threat actor infrastructure.

Another way the autonomous AI agents are helping is by reducing cognitive loads on humans and enabling interactions with agents to achieve specific outcomes. For example, if there are hundreds of login attempts from unfamiliar locations, probably only one or two may be worth deeper investigations as they have additional insights attached to them which could be surfaced quickly by the agent. Similarly, an end point process tree that could take significant effort for humans to analyze can be done much faster with the agent to spot suspicious anomalies. To maximize the impact, one important skill needed by SOC analysts is to be able to craft and finetune prompts to get the right insights with GenAI.

## Inside the Technology: How We Bring Autonomous Agents to Life

Behind the scenes, delivering trustworthy GenAI-based solutions at scale requires rigorous engineering and continuous collaboration with the security operations teams. We’ve built AI agents on a foundation of expert-defined guardrails, curated test sets, and deployment-time checks to ensure reliability. Engineers, security analysts and researchers collaborated to refine workflows, enhance precision, and broaden coverage as the agents adapt to real-world threats. Each workflow begins under human oversight, reinforced by efficient engineering and analyst feedback loops that accelerate development while upholding security, privacy, and compliance standards.

This transformation also demanded deep integration into Defender Experts core systems, from case management to remediation services, requiring ground-up engineering to accommodate long-running GenAI-based workflows alongside asynchronous backend processes. There is also a need for an orchestration engine that coordinates multi-layer automations, enabling rule-based logic, GenAI-powered features, and traditional AI models to work seamlessly together with the autonomous AI agents to maximize quality, efficiency and cost-effectiveness.

The impact is clear: AI agents are now running on 75% of t...