---
title: AI IR Overlay – Incident Response Specification for AI Agents
url: https://www.darknet.org.uk/2026/08/ai-ir-overlay-incident-response-specification-for-ai-agents/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-08-28
fetch_date: 2026-08-29T08:30:53.790692
---

# AI IR Overlay – Incident Response Specification for AI Agents

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](data:image/svg+xml...)![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [GenAI](https://www.darknet.org.uk/category/genai/) / AI IR Overlay – Incident Response Specification for AI Agents

# AI IR Overlay – Incident Response Specification for AI Agents

Published August 28, 2026 |

Views: 173

An OAuth token can be valid, the API call authorised, and the action still be something nobody intended. The agent used the credential it was given, through the interface it was approved for, and the audit log records all of it correctly. Nothing in that sequence resembles an intrusion, because nothing was intruded upon.

![AI IR Overlay — Incident Response for AI Agents, with agent, identity, tools, memory, kill_switches, evidence_export and $ python3 scripts/validate.py --strict.](data:image/svg+xml...)![AI IR Overlay — Incident Response for AI Agents, with agent, identity, tools, memory, kill_switches, evidence_export and $ python3 scripts/validate.py --strict.](https://www.darknet.org.uk/wp-content/uploads/2026/08/ai-ir-overlay-incident-response-framework-for-ai-agents-640x360.webp)

AI IR Overlay extends established incident-response practices with AI-agent inventories, graded containment, evidence capture and controlled recovery.

That is the case AI IR Overlay is built around, and it is a genuinely awkward one for an incident response programme. There is no compromised account to disable. Identity telemetry is accurate and unhelpful. The question is not whether the credential was stolen but what the agent was told, what it could reach, and how much of that it did before anyone noticed.

Advertisement

The framework is a specification for answering those questions: 24 playbooks, three JSON schemas, two runnable reference implementations, Apache 2.0, one author. It is better than its adoption numbers suggest, and it stops in a specific and interesting place.

## What it actually supplies

Three artefacts, mapped onto NIST SP 800-61 Rev. 3 and cross-referenced to NIST CSF 2.0, the NIST AI RMF and the OWASP Top 10 for Agentic Applications.

An **AI Bill of Materials** — YAML, one per production agent, recording service identity, scopes, tools, write targets, memory settings and retrieval sources. The insistence throughout is on what the deployed agent can reach rather than what the design document says it should. An agent wired into email, a CRM and an ERP has three separate blast radii before anyone has looked at the model, and that map costs far less to build on a quiet Tuesday than at two in the morning.

A **containment ladder**, M0 to M5, replacing the single kill switch. M1 is the rung that matters: *“All write tools are stripped from the agent’s tool set”*, with read and query tools left running. That is the containment shape you actually want for an agent sitting inside a business process, because destroying the session and rotating every credential also destroys the state needed to reconstruct what happened.

A **minimum evidence set** across six classes — prompts and responses, tool-call records, retrieval traces, memory state, configuration state, and identity or downstream audit logs. Wider than endpoint telemetry by design, because the opening case produces no unusual process tree and no suspicious authentication event.

None of this asks a SOC to invent a new discipline. The command structure, the evidence handling and the recovery process all stay where they are, which is the framework’s best decision and the reason it is worth the reading time.

Advertisement

## What the validator proves

`scripts/validate.py` is 279 lines. It performs JSON Schema validation and date-staleness checks against the AI-BOM and privilege-matrix files — no subprocess call, no network access, nothing that executes the systems being described.

That is more useful than it sounds. A containment-test date that has gone stale becomes a build finding, which is more than most control frameworks manage. Two qualifications matter, though, and both are easy to overstate in the other direction.

**Staleness only fails a build in strict mode.** By default the validator prints `STALE-WARN` and exits zero; `--strict` turns those into errors. A team wiring this into CI without the flag gets warnings the pipeline does not enforce.

**And a passing build says a control was declared, not that it works.** The validator confirms an organisation has written down that it has a kill switch and written down when it last tested one. Whether the switch functions is outside what any schema check can reach. That distinction is the whole subject of this framework, so it is worth not blurring in the one place it can be measured.

## Where the automation stops

The actuation layer is more complete than a quick look suggests. There is a **19KB kill-switch API contract** in `schemas/kill-switch-api.md`, referencing M1 a dozen times, and a **runnable demo** in `reference-impls/kill_switch_demo/` implementing the M0–M4 contract against a synthetic tool registry — M5, controlled re-enable, is explicitly out of scope. A second reference implementation, `evidence_exporter`, ships adapter stubs for each of the six evidence classes. The interface for moving an agent between containment states is specified and demonstrated.

What is not specified is when to move it.

The kill-switch overview is explicit, and the wording repays reading closely:

> the ≤ 10-min Tier-1 SOC activation owner assumes a staffed Security Operations Center available to receive the incident-commander order. For purely autonomous agents in 24/7 operation where no SOC is staffed off-hours (and the agent owner is the only human in the loop), the M3/M4 activation path requires **automation** that this v0.33.0 specification does not yet define.

So the documented activation path assumes a staffed SOC. The escalation path to M3 or M4 assumes a human incident commander reachable inside ten minutes, and where that assumption fails, the specification says so and stops. No signals, no thresholds, no policy for which mode to enter at what scope.

**The hole sits exactly where the agent is most autonomous and the team is smallest.** An organisation with a 24/7 SOC has the least need of an automatic trigger and matches the operating model the specification assumes. A two-person team running an agent unattended overnight has the most need and gets an acknowledged gap.

One smaller thing, on the same page: it describes itself as v0.33.0 while the current release is v0.35.0, and nothing has been pushed to the repository since 9 July. Version drift on the safety-controls page is the drift that costs most.

## What the archive says about this problem

Darknet reviewed [FIDO](https://www.darknet.org.uk/2016/06/fully-integrated-defense-operation-fido-automated-incident-response/) in 2016 — Netflix’s orchestration layer for automated incident response, evaluating and scoring malware detections. Its own capability list at the time read: *“Enforcement – ...