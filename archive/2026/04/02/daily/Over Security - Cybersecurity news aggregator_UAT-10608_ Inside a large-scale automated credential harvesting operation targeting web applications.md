---
title: UAT-10608: Inside a large-scale automated credential harvesting operation targeting web applications
url: https://blog.talosintelligence.com/uat-10608-inside-a-large-scale-automated-credential-harvesting-operation-targeting-web-applications/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-02
fetch_date: 2026-04-03T04:29:10.621815
---

# UAT-10608: Inside a large-scale automated credential harvesting operation targeting web applications

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

# UAT-10608: Inside a large-scale automated credential harvesting operation targeting web applications

By
[Asheer Malhotra](https://blog.talosintelligence.com/author/asheer-malhotra/),
[Brandon White](https://blog.talosintelligence.com/author/brandon/)

Thursday, April 2, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[malware](https://blog.talosintelligence.com/category/malware/)

* Cisco Talos is disclosing a large-scale automated credential harvesting campaign carried out by a threat cluster we are tracking as “UAT-10608.”
* Post-compromise, UAT-10608 leverages automated scripts for extracting and exfiltrating credentials from a variety of applications, that are then posted to its command and control (C2).
* The C2 hosts a web-based graphical user interface (GUI) titled “NEXUS Listener” that can be used to view stolen information and gain analytical insights using precompiled statistics on credentials harvested and hosts compromised.

---

Talos is disclosing a large-scale automated credential harvesting campaign carried out by a threat cluster we currently track as UAT-10608. The campaign is primarily leveraging a collection framework dubbed “NEXUS Listener.” The systematic exploitation and exfiltration campaign has resulted in the compromise of at least 766 hosts, as of time of writing, across multiple geographic regions and cloud providers. The operation is targeting Next.js applications vulnerable to React2Shell (CVE-2025-55182) to gain initial access, then is deploying a multi-phase credential harvesting tool that harvests credentials, SSH keys, cloud tokens, and environment secrets at scale.

The breadth of the victim set and the indiscriminate targeting pattern is consistent with automated scanning — likely based on host profile data from services like Shodan, Censys, or custom scanners to enumerate publicly reachable Next.js deployments and probe them for the described React configuration vulnerabilities.

The core component of the framework is a web application that makes all of the exfiltrated data available to the operator in a graphical interface that includes in-depth statistics and search capabilities to allow them to sift through the compromised data.

This post details the campaign's methodology, tools, breadth and sensitivity of the exposed data, and the implications for organizations impacted by this activity.

*This analysis is based on data collected for security research purposes. Specific credentials and victim identifiers have been withheld from this publication.* *Talos has informed service providers of exposed and at-risk credentials* *and is working with industry partners such as GitHub and AWS to quarantine credentials and inform victims.*

|  |  |
| --- | --- |
| Metric | Count |
| Compromised hosts | 766 |
| Hosts with database credentials | ~701 (91.5%) |
| Hosts with SSH private keys | ~599 (78.2%) |
| Hosts with AWS credentials | ~196 (25.6%) |
| Hosts with shell command history | ~245 (32.0%) |
| Hosts with live Stripe API keys | ~87 (11.4%) |
| Hosts with GitHub tokens | ~66 (8.6%) |
| Total files collected | 10,120 |

## Initial access

UAT-10608 targets public-facing web applications using components, predominately Next.js, that are vulnerable to CVE-2025-55182, broadly referred to as “React2Shell.”

React2Shell is a pre-authentication remote code execution (RCE) vulnerability in React Server Components (RSC). RSCs expose Server Function endpoints that accept serialized data from clients. The affected code deserializes payloads from inbound HTTP requests to these endpoints without adequate validation or sanitization.

### Exploitation steps

1. An attacker identifies a publicly accessible application using a vulnerable version of RSCs or a framework built on top of it (e.g., Next.js).
2. The attacker crafts a malicious serialized payload designed to abuse the deserialization routine — a technique commonly used to trigger arbitrary object instantiation or method invocation on the server.
3. The payload is sent via an HTTP request directly to a Server Function endpoint. No authentication is required.
4. The server deserializes the malicious payload, resulting in arbitrary code execution in the server-side Node.js process.

Once the threat actor identifies a vulnerable endpoint, the automated toolkit takes over. No further manual interaction is required to extract and exfiltrate credentials harvested from the system.

## Automated harvesting script

Data is collected via nohup-executed shell scripts dropped in /tmp with randomized names:

```
/bin/sh -c nohup sh /tmp/.eba9ee1e4.sh >/dev/null 2>&1
```

This is consistent with a staged payload delivery model. The initial React exploit delivers a small dropper that fetches and runs the full multi-phase harvesting script. Upon execution, the harvesting script iterates through several phases to collect various data from the compromised system, outlined below:

* **environ** - Dump running process environment variables
* **jsenv** - Extract JSON-parsed environment from JS runtime
* **ssh** - Harvest SSH private keys and authorized\_keys
* **tokens** - Pattern-match and extract credential strings
* **history** - Capture shell command history
* **cloud\_meta** - Query cloud metadata APIs (AWS/GCP/Azure)
* **k8s** - Extract Kubernetes service account tokens
* **docker** - Enumerate container configurations
* **cmdline** - List all running process command lines
* **proc\_all**- Aggregate all process environment variables

The framework leverages a meta.json file that tracks execution state:

![](https://blog.talosintelligence.com/content/images/2026/03/data-src-image-93ec01b9-6994-4f76-a2f1-ba60f6042023.png)

 Following the completion of each collection phase, an HTTP request is made back to the C2 server running the NEXU...