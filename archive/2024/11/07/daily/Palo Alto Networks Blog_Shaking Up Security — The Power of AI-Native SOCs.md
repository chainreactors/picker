---
title: Shaking Up Security — The Power of AI-Native SOCs
url: https://www.paloaltonetworks.com/blog/2024/11/power-of-ai-native-socs/
source: Palo Alto Networks Blog
date: 2024-11-07
fetch_date: 2025-10-06T19:21:15.255929
---

# Shaking Up Security — The Power of AI-Native SOCs

* [Blog](https://www.paloaltonetworks.com/blog)
* [Palo Alto Networks](https://www.paloaltonetworks.com/blog/corporate)
* [AI Governance](https://www.paloaltonetworks.com/blog/category/ai-governance/)
* Shaking Up Security — The...

# Shaking Up Security — The Power of AI-Native SOCs

Link copied

By [Dena De Angelo](/blog/author/ddeangelo/ "Posts by Dena De Angelo")

Nov 06, 2024

7 minutes

[AI Governance](/blog/category/ai-governance/)

[AI Security](/blog/category/ai-security/)

[Points of View](/blog/category/points-of-view/)

[native-AI](/blog/tag/native-ai/)

[SOC](/blog/tag/soc/)

![](/blog/wp-content/themes/panwblog2023/dist/images/audio-icon.svg)

Kieran Norton — AI-Native SOCs

*00:00*
*00:00*

Volume Slider

10s

10s

10s

10s

Seek Slider

Like legacy security tools, such as traditional firewalls and signature-based antivirus software, organizations that have more traditional (and potentially more vulnerable) SOCs are struggling to keep pace with the increasing volume and sophistication of threats. This challenge is underscored by the fact that approximately 450,000 new malware variants are detected each day, according to [data by AV-Test](https://www.av-test.org/en/statistics/malware/#:~:text=Every%20day%2C%20the%20AV%2DTEST,to%20their%20characteristics%20and%20saved.). With such a staggering rate of new threats emerging, traditional SOCs simply cannot keep up using manual analysis and outdated solutions.

As organizations grapple with tedious alerts, staffing challenges and prolonged response times, the need for a new approach to security becomes clear. Enter the concept of an AI-native SOC – a revolutionary approach that promises to transform how we detect, analyze and respond to cybersecurity threats.

In a recent [Threat Vector podcast](https://thecyberwire.com/podcasts/threat-vector/34/notes), Unit 42 director of thought leadership, David Moulton, interviewed Kieran Norton, principal at Deloitte & Touche, LLP, a cyber and AI automation leader. They discussed evolving security strategies that support digital transformation and the necessity to keep innovating to stay ahead of threats.

## The Limitations of Traditional SOCs

Getting to the heart of the matter, Norton explains one of the challenges faced by traditional SOCs — there is too much data to manage:

> Given the volume of data that's now coming in from the significantly larger attack surface, that old model is starting to show real kinds of issues, one of which is alert fatigue. There are just too many alerts coming in for the SOC to manage.

In the [*2024 Cortex Xpanse Attack Surface Threat Report: Lessons in Attack Surface Management from Leading Global Enterprises*](https://start.paloaltonetworks.com/2024-asm-threat-report.html), Palo Alto Networks outlined some key findings:

* **Attack Surface Change Inevitably Leads to Exposures**

Across industries, attack surfaces are always in a state of flux. The research indicates that, on average, an organization’s attack surface has over 300 new services every month. These additions account for nearly 32% of new high or critical cloud exposures for organizations.

* **Opportunities for Lateral Movement and Data Exfiltration are Abundant**

Just three categories of exposures (IT and Networking Infrastructure, Business Operations Applications and Remote Access Services) account for 73% of high-risk exposures across the organizations studied. They can be exploited for lateral movement and data exfiltration.

* **Critical IT and Security Services are Dangerously Exposed to the Internet**

Over 23% of exposures involve critical IT and security infrastructure, opening doors to opportunistic attacks. These include vulnerabilities in application-layer protocols, like SNMP, NetBIOS, PPTP and internet-accessible administrative login pages of routers, firewalls, VPNs and other core networking and security appliances.

As such, traditional SOCs struggle with an overwhelming number of alerts, leading to burnout among analysts and increased dwell time for threats.

## Embracing AI for Enhanced Security Operations

The AI-native SOC model aims to address these challenges by leveraging artificial intelligence and machine learning to automate routine tasks and enhance threat detection capabilities. As Norton describes:

"We need machines – autopilots – to do a lot of the volume for us and take care of those things that are relatively straightforward that can be automated, that can be addressed through leveraging AI and a lot of other things. And then the analysts are now tuning the machine and making sure the machine is operating as effectively as possible."

This approach aligns perfectly with [Cortex XSIAM's](/cortex/cortex-xsiam) capabilities, which use AI and ML to automate data integration, analysis and triage, allowing analysts to focus on high-priority incidents.

## Real-World Benefits of AI-Native SOCs

The advantages of adopting an AI-native SOC approach are significant. Norton shares a compelling case study:

"We have a client that was seeing over 100,000 alerts a day from their cloud security posture management tool. Through a combination of applying AI/ML to the log aggregation, consolidation, stitching, et cetera, as well as automating the highest volume, most frequently identified alerts in the environment, we were able to carve down the time significantly. We saw a 12x improvement in mean time to resolve. And a 5x improvement in the number of alerts resolved per day."

This dramatic reduction in alert volume and improved resolution time demonstrates the power of AI in streamlining SOC operations. It's not just about handling more alerts faster. It's about fundamentally changing how security teams operate, allowing them to focus on strategic initiatives rather than being overwhelmed by a flood of low-level or low fidelity alerts. This shift can lead to more proactive security measures and a stronger overall defense posture.

## Enhancing Threat Intelligence with AI

AI-native SOCs also revolutionize how organizations collect and utilize threat intelligence. Norton explains, "In an AI-native kind of world, you're using intel and data from your own environment, right? You are finding what you know about your environment, and you are responding with higher degrees of context."

Cortex XSIAM's strengths dovetail seamlessly with this strategy. For instance, XSIAM's AI-driven analytics can automatically identify anomalies specific to an organization's network behavior, creating a custom threat detection model. Furthermore, XSIAM's ability to stitch together data from multiple sources (including endpoints, identity, networks and cloud environments) provides a comprehensive view of the security landscape, enabling more accurate and contextual threat intelligence. This “storyline” allows security teams to respond to threats with a deeper understanding of their potential impact on the specific organization, rather than relying solely on generic threat feeds. Looking ahead, Norton predicts an increase in the development and use of bespoke AI models:

"We're going to see more agents deployed more widely from a cyber perspective. Ultimately, the vision that we're working toward is to chain together a series of agents that allow us to perform services for clients faster, more effectively, with better outcomes."

This foresight aligns with Cortex XSIAM's continuous evolution, powered by Palo Alto Networks [Precision AI](/precision-ai-security), to stay ahead of emerging threats.

## Embracing AI — A No-Regret Decision

The key difference between an AI-native SOC and a traditional SOC with some AI capabilities is that in an AI-native SOC, AI is *fundamental to its operations*. It drives most of the initial analysis and decision-making processes. This allows human analysts to focus on more complex, strategic tasks (like threat hunting) that require human judgment and creativity. Norton uses an analogy to explain this:

"Today we have the abilit...