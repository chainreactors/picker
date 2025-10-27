---
title: LLAMATOR – Red Team Framework for Testing LLM Security
url: https://www.darknet.org.uk/2025/09/llamator-red-team-framework-for-testing-llm-security/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-17
fetch_date: 2025-10-02T20:15:32.945758
---

# LLAMATOR – Red Team Framework for Testing LLM Security

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

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# LLAMATOR – Red Team Framework for Testing LLM Security

September 12, 2025

Views: 520

LLAMATOR is a Python framework that helps offensive security teams evaluate the real-world security of large language model systems. It focuses on repeatable campaigns rather than one-off prompts. You define three roles for each test run: an attack model that crafts adversarial inputs, a tested model that represents the target application, and a judge model that scores responses. LLAMATOR includes adapters for OpenAI-compatible REST endpoints and popular orchestration stacks, allowing teams to test the same interfaces used in production. It also produces artefacts for stakeholders, including structured logs and documents suitable for audit and remediation tracking.

![LLAMATOR - Red Team Framework for Testing LLM Security](https://www.darknet.org.uk/wp-content/uploads/2025/09/LLAMATOR-Red-Team-Framework-for-Testing-LLM-Security-640x427.jpg)

## Features

* **Preset attack library.** Curated single-stage and multi-stage tests that exercise common LLM risks such as prompt injection, system prompt leakage, unsafe tool invocation, and retrieval contamination.
* **Multi-client adapters.** Clients for OpenAI-compatible REST APIs and LangChain-style integrations. The pattern supports drop-in use with local servers and commercial APIs.
* **Three-model test harness.** Separate roles for attacker, target, and judge to score outcomes in a structured way.
* **Artefacts** and reports. Options to log to CSV or Excel and to generate a DOCX-style report so findings can be consumed by leadership and tracked to closure.
* **Examples and notebooks.** Quick starts that demonstrate local testing with desktop servers as well as code-driven campaigns.

## Installation

Install the published package from PyPI.

<code>pip install llamator==3.3.0</code>

|  |  |
| --- | --- |
| 1 | <code>pip install llamator==3.3.0</code> |

Pinning to a specific version keeps tests reproducible across team members.

## Usage

LLAMATOR has several helper functions and preset configurations.

`print_test_preset`

Prints example configuration for presets to the console.

Available presets: `all, eng, llm, owasp:llm01, owasp:llm07, owasp:llm09, rus, vlm`

Usage:

from llamator import print\_test\_preset
# Print configuration for all available tests
print\_test\_preset("all")

|  |  |
| --- | --- |
| 1  2  3  4 | from llamator import print\_test\_preset    # Print configuration for all available tests  print\_test\_preset("all") |

## Attack Scenario

**Target.** A customer support chatbot with Retrieval Augmented Generation that answers order and account questions from a private knowledge base. The team mirrors production locally against a compatible REST server to avoid testing in the live environment.

**Approach.** The red team defines the three roles and selects attack presets that map to standard failure modes in RAG systems. The set includes prompt injection that attempts data exfiltration, system prompt disclosure to extract hidden instructions, and base64 payloads intended to contaminate retrieval. Logging and reports are enabled to capture every exchange.

**Outcome.** Several injections bypass content policy when the target model is presented with blended support tickets that contain crafted instructions. The judge model flags responses that leak system prompt fragments and returns a score with evidence. The team hands off the DOCX report and CSV log that link each failure to system prompts and retrieval parameters, with recommendations for stronger instruction hierarchies, stricter tool invocation rules, and sanitisation of retrieved context.

## Red Team Relevance

LLM security testing needs repeatability. LLAMATOR’s three-role harness, preset attack library, and reporting close the gap between clever prompt screenshots and a defensible testing program. Client adapters allow teams to exercise the same endpoints, chains, and agents that power production. Artefacts in standard formats make it straightforward to track remediation and to re-run identical campaigns after changes to prompts, safety filters, or retrieval logic.

## Conclusion

LLAMATOR provides red teams with a structured approach to testing chatbots, agents, RAG pipelines, and related systems. It installs from PyPI, integrates with OpenAI-style endpoints, ships curated attacks, and produces evidence suitable for audits. If you are building a formal adversarial evaluation program for LLM applications, LLAMATOR is a practical starting point.

You can read more or download LLAMATOR here: <https://github.com/LLAMATOR-Core/llamator>

## Related Posts:

* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [testssl.sh - Test SSL Security Including Ciphers,…](https://www.darknet.org.uk/2018/10/testssl-sh-test-ssl-security-including-ciphers-protocols-detect-flaws/)
* [TREVORspray - Credential Spray Toolkit for Azure,…](https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/)
* [fping 3 - Multi Target ICMP Ping Tool](https://www.darknet.org.uk/2016/07/fping-3-multi-target-icmp-ping-tool/)
* [Windows\_EndPoint\_Audit - Endpoint Security Auditing Toolkit](https://www.darknet.org.uk/2025/07/windows_endpoint_audit-endpoint-security-auditing-toolkit/)
* [Malvertising and TDS Cloaking Tactics Uncovered](https://www.darknet.org.uk/2025/07/malvertising-and-tds-cloaking-tactics-uncovered/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fllamator-red-team-framework-for-testing-llm-security%2F)

[Tweet](https://twitter.com/intent/tweet?text=LLAMATOR+-+Red+Team+Framework+for+Testing+LLM+Security&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fllamator-red-team-framework-for-testing-llm-security%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fllamator-red-team-framework-for-testing-llm-security%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fllamator-red-team-framework-for-testing-llm-security%2F&text=LLAMATOR+-+Red+Team+Framework+for+Testing+LLM+Security)

[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F09%2Fllamator-red-team-framework-for-testing-llm-security%2F)

[Email](/cdn-cgi/l/email-protection#a59ad6d0c7cfc0c6d198e9e9e4e8e4f1eaf780979588809795f7c0c1809795f1c0c4c8809795e3d7c4c8c0d2cad7ce809795c3cad7809795f1c0d6d1cccbc2809795e9e9e8809795f6c0c6d0d7ccd1dc83c7cac1dc98e9e9e4e8e4f1eaf7809795ccd6809795c4809795f5dcd1cdcacb809795c3d7c4c8c0d2cad7ce809795c3cad7809795d7c0c1809795d1c0c4c8cccbc2809795c9c4d7c2c0809795c9c4cbc2d0c4c2c0809795c8cac1c0c9809795d6dcd6d1c0c8d6809795d2ccd1cd809795d5d7c0d6c0d1809795c4d1d1c4c6ced68097e6809795c8d0c9d1cc88c6c9ccc0cbd1809795c4c1c4d5d1c0d7d68097e6809795c4cbc1809795d7c0d5cad7d1c4c7c9c0809795d7c0d6d0c9d1d68b8095e18095e48095e1809...