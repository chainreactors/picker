---
title: Choose your fighter: Balancing competing requirements to select models for your AI SOC
url: https://blog.talosintelligence.com/choose-your-fighter-balancing-competing-requirements-to-select-models-for-your-ai-soc/
source: Over Security
date: 2026-08-28
fetch_date: 2026-08-29T08:32:57.478084
---

# Choose your fighter: Balancing competing requirements to select models for your AI SOC

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

# Choose your fighter: Balancing competing requirements to select models for your AI SOC

By
[David J. Bianco](https://blog.talosintelligence.com/author/david-j-bianco/)

Wednesday, August 26, 2026 06:00

[Tool Talk](https://blog.talosintelligence.com/category/tool-talk/)
[AI](https://blog.talosintelligence.com/category/ai/)

* Selecting a model for your security operations center (SOC) and digital forensics and incident response (DFIR) tasks is important, but selecting the best one is more involved than you might think. SOC tasks rely on a combination of model efficacy, analysis time, cost, and consistency of results.
* Cisco Talos tested 66 model and reasoning combinations across offerings from both Anthropic and OpenAI on a log analysis task to see if we could identify a clear winner. Instead, we found a repeatable methodology that organizations can use in their own evaluations.
* **Reasoning effort was not a universal quality dial.** More effort often cost more without improving the result. In some cases, more effort produced lower scores.
* **Consistency should be a major decision factor.** A condition with a strong median can still produce an occasional weak run.

Choosing the best model for any task involves a complex balancing act: compute/reasoning effort vs. effectiveness vs. time vs. cost vs... well, lots of other things.  If you are choosing a large language model (LLM) for a security operations center (SOC) or digital forensics and incident response (DFIR) workflow, “Which model scored highest?” is almost certainly not the right question. In fact, it could even have severe negative consequences.

A more useful question might be: Which model and reasoning setting gives me enough investigative quality, at a cost, speed, consistency, and failure rate my workflow can tolerate?

## The experiment

Cisco Talos tested 66 model and reasoning combinations (the conditions) from Anthropic and OpenAI on a tool-assisted log-review task. Using only common Unix command-line tools, the reviewers had to decide whether a given dataset was real or synthetically generated. Each reviewer received an identical dataset. The dataset was synthetic, but the reviewers were told that it might be real.

We chose this task because it required many of the same tools and analytic techniques used in typical incident triage and investigation, but unlike those scenarios, could easily create a single numeric score for comparison. The reviewers investigated the logs using their native agent harnesses (i.e., Anthropic models used Claude Code, OpenAI models used Codex), then assigned a synthetic-confidence score from 0 (real) to 100 (synthetic). Higher scores therefore approached the known answer more closely.

Each experimental panel contained four independently prompted reviewer personas:

* Threat Hunter
* Detection Engineer
* Network Forensics Analyst
* Host/Endpoint Detection and Response (EDR) Analyst

We ran five rounds per condition. A panel counted only when all four reviewers produced valid reports. We allowed a limited number of retries in the case of guardrail refusals or invalid output formats before discounting a panel. The panel score was the mean of the four persona scores, and the condition score was the median of all its complete panel scores.

### What we measured

In addition to the review score mentioned above, we computed the following for each panel:

* **Cost:** Total API-equivalent cost of every attempt for a condition, including failed attempts and retries, divided by the number of complete, usable panels. We calculated cost using a public list-price rate card frozen before testing began, rather than actual incurred spend. Actual costs vary by payment method, subscription plan, credits, and negotiated contract terms, making them unsuitable for consistent cross-provider comparison. The published rates were current when the study began and may differ from today’s prices.
* **Time:** The total wall time consumed across all five planned panels for a condition, also including failures and retries, divided by the number of complete, usable four-persona panels. Within each panel, the four persona evaluations ran concurrently. Any provider-directed waits and targeted retries were included in the panel’s elapsed time, and each panel was fully resolved before the next panel began.
* **Downside score consistency:** Some tested conditions had a wide discrepancy when it came to their efficacy scores, while some clustered tightly together. In a SOC, unexpectedly good answers are unlikely to cause problems, but unexpectedly poor answers can lead to unwelcome false positive or (worse) false negative decisions. Our score consistency is defined as the median score for the panel minus the lowest score in that panel. Smaller numbers indicate higher consistency.

### The data behind the tests

The corpus was generated with [EvidenceForge](https://github.com/Cisco-Talos/EvidenceForge), Talos' open-source synthetic telemetry generator. We froze EvidenceForge at version 1.12.0 and used the same six-hour enterprise scenario for every condition, so the model and reasoning settings changed while the evidence did not.

The reviewer-visible corpus contained **80,054 simulated log records across 20 source formats**, packaged as **88 files totaling 48.0MB (45.8MiB)**. It combined:

1. Network telemetry from two Zeek sensors, including connection, DNS, HTTP, TLS, SMTP, file, certificate, OCSP, DHCP, and NTP logs
2. Perimeter security telemetry from a Cisco ASA firewall and Snort IDS
3. Endpoint telemetry, including Windows Security and Sysmon events, eCAR process, session, and flow records, Linux syslog, and shell history
4. Application access logs from web and proxy services
5. A small set of email artifacts

Every reviewer received an identical copy of the data. Scenario de...