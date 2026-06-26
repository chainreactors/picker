---
title: Beyond IOCs: AI-enabled threat intelligence
url: https://blog.talosintelligence.com/beyond-iocs-ai-enabled-threat-intelligence/
source: Over Security
date: 2026-06-25
fetch_date: 2026-06-26T06:09:10.423272
---

# Beyond IOCs: AI-enabled threat intelligence

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

# Beyond IOCs: AI-enabled threat intelligence

By
[Martin Lee](https://blog.talosintelligence.com/author/martin-lee/)

Thursday, June 25, 2026 14:00

[Threat Source newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)

Welcome to this week’s Threat Source newsletter.

The issue of AI in cybersecurity is often portrayed as a binary choice: either a force multiplier for our adversaries, or a tool bringing professional obsolescence. The reality is more nuanced. While AI certainly brings some advantage to attackers, it also offers advantages to the defender, notably in how we manage, index, and derive value from threat intelligence.

Currently, our industry excels in the use and dissemination of indicators of compromise (IOCs). These atomic indicators fit neatly into key-value data stores and their value can be enhanced with added context, neatly structured in STIX/MISP format. However, this is only the tactical layer.

Ultimately, we want the consumers of threat intelligence reports to develop their knowledge and to build a picture of the relevance of the threat to their own situation, along with understanding of how they can respond given their resources and constraints. This capability is conferred by the natural language found within strategic and operational intelligence briefings.

These reports provide the context required for meaningful response, yet they remain notoriously difficult to index. We are often left with disparate incident reports, darknet monitoring, and malware analysis that fail to cross-reference effectively, further complicated by inconsistent naming conventions for threat actors.

This is a problem that large language models (LLMs) may be able to solve. Although AI models have no real understanding of an issue, they can identify synonyms and relate entities across vast, unstructured datasets. This can only make the retrieval of relevant threat intelligence reports easier, and facilitate the generation of relevant advice to protect against threats.

There are still issues to resolve. We need to be vigilant regarding the veracity of the data that LLMs ingest, and of the confidentiality of the queries made of such a system. However, the development of personal, domain-specific LLMs offers the possibility of a world of integrated threat intelligence where relevant reports from disparate sources can be easily retrieved, and specific advice returned to even the vaguest of queries.

Rather than fearing AI’s potential negative effects on our employment, we can consider AI’s development as a powerful tool that enables access to threat intelligence reports and allows us to provide tailored actionable advice faster to those who need to know it. Ultimately, AI can help us do what we do best: making a difference and making the bad guy’s lives harder.

## The one big thing

Cisco Talos is highlighting how Windows threats [increasingly abuse the Component Object Model (COM)](https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats) to execute malicious activities. While COM is a fundamental Windows technology for legitimate inter-process communication, malware families like Qakbot and WarmCookie hijack it for lateral movement, persistence, and evasion. Because COM functionality relies on opaque GUIDs and indirect vtable calls, it obscures the attacker's intent and makes manual analysis incredibly labor-intensive.

### Why do I care?

Threat actors love COM because it provides convenient access to built-in Windows functionality while making static analysis a nightmare. By hiding malicious behavior behind indirect function calls, attackers easily bypass basic scrutiny and blend in with legitimate system processes. Adversaries are effectively turning Windows' own architecture against itself. If analysts aren't prioritizing COM during triage, they are likely missing critical pieces of the infection chain.

### So now what?

Defenders must sharpen their skills in recognizing COM usage and translating evidence like ProgIDs and vtable offsets into human-readable actions. Leverage specialized tools like OleView.NET, IDA’s COM Helper, and DispatchLogger to map anonymous indirect calls to clear behaviors. Security teams should also build static hunting logic to track these threats. You can find a simplified YARA hunting rule for binaries referencing the Task Scheduler COM class in the [full blog post](https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats).

## Top security headlines of the week

**FortiBleed campaign used custom FortiGate sniffer to steal credentials**
Security firm SOCRadar says the large-scale FortiBleed campaign targeting Fortinet FortiGate devices used custom sniffers to harvest authentication secrets from compromised firewalls and steal credentials. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/))

**Scattered Spider hackers plead guilty on Day 1 of trial**
Two men pleaded guilty in the United Kingdom this week to criminal charges stemming from an August 2024 cyber attack affecting Transport for London, the entity responsible for the public transport network in the Greater London area. ([Krebs on Security](https://krebsonsecurity.com/2026/06/scattered-spider-hackers-plead-guilty-on-day-1-of-trial/))

**Klue says hackers stole credential from 2022 that led to customer data breaches**
Market research company Klue has confirmed that a credential dating back to 2022, which was part of a limited pilot, was used by hackers earlier this month to steal data from its corporate customers, including several cybersecurity companies. ([TechCunch](https://techcrunch.com/2026/06/23/klue-says-hackers-stole-credential-from-2022-that-led-to-customer-data-breaches/))

**New ex...