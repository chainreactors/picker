---
title: Patch, track, repeat: The 2025 CVE retrospective
url: https://blog.talosintelligence.com/patch-track-repeat-the-2025-cve-retrospective/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-05
fetch_date: 2026-03-06T04:04:29.453100
---

# Patch, track, repeat: The 2025 CVE retrospective

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Patch, track, repeat: The 2025 CVE retrospective

By
[Thorsten Rosendahl](https://blog.talosintelligence.com/author/thorsten/)

Thursday, March 5, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week's edition of the Threat Source newsletter.

It's time to look back at a year that pushed the vulnerability landscape to new heights. I'll admit this retrospective is arriving a bit later than planned. With 48,196 CVEs in 2025 (a stunning 132 vulnerabilities per day), the analysis takes time — especially when you're operating one-handed after an encounter with black ice breaks your dominant arm. But better thorough than rushed, right?

![](https://blog.talosintelligence.com/content/images/2026/03/blog_CVEline.jpg)

What concerns me more than the sheer volume is what's *inside* these CVEs. XSS, SQL injection, and deserialization vulnerabilities continue to dominate, accounting for roughly 10,000 CVEs. Despite decades of awareness, these fundamental software security weaknesses persist.

The Known Exploited Vulnerabilities (KEV) Catalog tells an even more sobering story. With 241 KEVs in 2025 compared to 186 in 2024, we saw a 30% increase in confirmed active exploitation.

![](https://blog.talosintelligence.com/content/images/2026/03/blog_KEVline.jpg)

94 KEVs (39%) added in 2025 originated from CVE-2024 and earlier. We saw actively exploited vulnerabilities from as far back as 2007 — yes, vulnerabilities old enough to vote in some countries are still causing problems today. Patch management must address legacy systems. It starts with visibility: maintaining accurate asset inventories and understanding what's actually running in your environment. For those systems that truly can't be patched, whether due to operational constraints or vendor abandonment, compensating controls become essential. Microsegmentation, network isolation, and enhanced monitoring can reduce the radius of damage when (not if) something goes wrong.

![](https://blog.talosintelligence.com/content/images/2026/03/blog_pie.jpg)

With 54 KEVs targeting firewalls, VPNs, and other network appliances, we saw network infrastructure take a disproportionate hit. And the vendor landscape in KEVs expanded to 99 vendors in 2025, up from 79 when I last checked in October. Connect that with supply chain complexity and the patch management visibility challenges I mentioned earlier, and you'll quickly realize why security teams are spending more time — not less — on vulnerability management. Every additional vendor in your environment is another patch cycle to track, another advisory to monitor, another potential weak link in the chain.

This is the first time I've attempted to systematically track AI-related vulnerabilities in the CVE data, and the methodology is still evolving. Defining what constitutes an "AI vulnerability" isn'tstraightforward. For this initial pass, I searched for CVEs containing specific keywords across several categories:

|  |  |
| --- | --- |
| Category | Keywords |
| AI Platforms | AutoGPT, Open WebUI, Ollama, vLLM, llama.cpp, LLaMA-Factory, MaxKB, Dify, LangChain |
| ML Frameworks | PyTorch, TensorFlow, scikit-learn, XGBoost, Hugging Face, MLflow |
| LLM Products | ChatGPT, GPT-3, GPT-4, OpenAI, Anthropic, Claude Code |
| AI Concepts | prompt injection, large language model, Model Context Protocol |

Using this approach, AI-related CVEs nearly **doubled** year-over-year, jumping from 168 to 330. Notably, “Model Context Protocol (MCP)” and “Claude” didn't appear in 2024 data at all.

A word of caution: While CVE data provides valuable insight into disclosed vulnerabilities in AI tools and frameworks, it doesn't capture emergent risks such as jailbreaking, hallucination-based misinformation, training data extraction, or model inversion attacks. See <https://genai.owasp.org/llm-top-10/> and <https://atlas.mitre.org/> if you want to learn more.

Keep tracking, keep patching, and stay tuned for the 2025 Year in Review for more trend analysis.

## The one big thing

Cisco Talos [continues to monitor](https://blog.talosintelligence.com/talos-developing-situation-in-the-middle-east/) the ongoing conflict in the Middle East. At this time we have not seen any significant cyber impacts, with some small incidents such as web defacements and small-scale distributed-denial-of-service (DDoS) attacks occurring. As with any highly fluid or dynamic situation, we are focused on providing our customers with highly accurate and timely intelligence and information. We will remain vigilant looking to identify any cyber related activity relevant to the region.

### Why do I care?

Currently there does not appear to be any significant increase in cyber activity associated with state-sponsored or state-affiliated groups. However, cyber criminals are likely to take advantage of the war to try and increase their scope of infections through the use of lures and other social engineering avenues.

### So now what?

Recommendations for organizations are currently focused on security hygiene, to include having multi-factor authentication (MFA) enabled, being diligent around any links or documents that are circulating, and ensuring you have proper monitoring in place to ensure you are prepared for any collateral impacts as they arise. Additional inspection or controls may be warranted to insulate potential larger impacts to the wider organization. Warn employees against clicking on unsolicited links related to the Middle East conflict, whether news or humanitarian. As always, ensure all software has been updated to the latest versions to minimize the attack surface and ensure you have a robust patching process.

If and/or when more relevant information becomes available, we will update [this blog](https://blog.talosintellig...