---
title: Anatomy of a Deno-Based Proxy & RAT
url: https://dfir.ch/posts/deno/
source: Over Security
date: 2026-06-16
fetch_date: 2026-06-17T07:03:54.522150
---

# Anatomy of a Deno-Based Proxy & RAT

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Anatomy of a Deno-Based Proxy & RAT

15 Jun 2026

**Table of Contents**

* [Executive Summary](#executive-summary)
* [Introduction](#introduction)
* [Initial Access: Mailbombing Followed by Fake IT Support](#initial-access-mailbombing-followed-by-fake-it-support)
  + [Detection Opportunity: Teams Impersonation](#detection-opportunity-teams-impersonation)
* [Malware Delivery](#malware-delivery)
* [Why Deno Matters](#why-deno-matters)
* [String Array Shifting](#string-array-shifting)
* [Module Analysis](#module-analysis)
  + [app.js: Dropper and Orchestrator](#appjs-dropper-and-orchestrator)
  + [back.js: Command-and-Control Bridge](#backjs-command-and-control-bridge)
  + [helper.js: Local Command Execution Engine](#helperjs-local-command-execution-engine)
  + [webui.js: Network Pivot Tunnel](#webuijs-network-pivot-tunnel)
* [Detection Opportunities](#detection-opportunities)
  + [Identity and Collaboration Telemetry](#identity-and-collaboration-telemetry)
  + [Endpoint Telemetry](#endpoint-telemetry)
* [Conclusion](#conclusion)
* [Indicators of Compromise](#indicators-of-compromise)
* [KQL Queries](#kql-queries)
* [MITRE Mapping](#mitre-mapping)

This is a copy of a blog post I wrote for my employee for [InfoGuard LABS](https://labs.infoguard.ch/).

---

## Executive Summary

In a recent investigation, we encountered malware that combined aggressive social engineering with the unconventional use of **Deno**, a secure JavaScript and TypeScript runtime built on V8.

The attack began with a large-scale email flooding campaign, commonly referred to as mailbombing, designed to overwhelm employees and create confusion. Shortly afterward, the targeted users received Microsoft Teams calls from an attacker impersonating internal IT support. One employee engaged with the caller and was persuaded to download and execute a malicious archive from a fake self-service portal.

The payload was not a traditional compiled implant. Instead, it consisted of a modular Deno-based Remote Access Trojan and proxy framework split across four JavaScript files. The JavaScript files implement a Deno-based remote access and tunneling agent. The launcher starts three child Deno processes. The main backdoor connects to a CloudFront-hosted WebSocket C2 endpoint, registers victim identity metadata, receives commands, and brokers traffic through local helper services. The local helper services provide arbitrary Windows command execution and generic TCP socket forwarding.

**Although endpoint protection was active on the host, the implant and its command-and-control channel were not initially blocked.** Detection occurred later, during follow-on reconnaissance activity. This case highlights the need to monitor not only payload binaries, but also scripting runtimes, unusual permission flags, local loopback services, and suspicious use of legitimate collaboration platforms.

## Introduction

Threat actors increasingly shift from compiled payloads to scripting engines and runtimes for their cross-platform flexibility and lower detection. While mailbombing and fake IT support campaigns have become increasingly common, this intrusion stood out because the attacker deployed a modular Deno-based RAT and proxy framework rather than a traditional compiled implant.

This malware is a modular Remote Access Trojan (RAT) and proxy that leverages Deno’s web APIs to build a microservice-like system on infected hosts using local loopback HTTP servers. Here, we break down its obfuscation, execution flow, and the four core modules.

Although an EDR was active on the compromised host, it did not raise an alert about the C2 communication or the implant, but only about subsequent LDAP queries and certificate-related reconnaissance activities. Therefore, if an attacker were to put more thought into the techniques used, the C2 channel could likely remain undetected for a longer period.

## Initial Access: Mailbombing Followed by Fake IT Support

The intrusion began with a high-volume email flooding campaign against three employees. Over the course of a day, the victims received hundreds of emails. While the email gateway filtered many of them, a significant number still reached users’ inboxes.

This activity served two purposes. First, it created user fatigue. Second, it established a plausible reason for âIT supportâ to contact the affected employees.

Shortly after the mail bombing began, the targeted users received Microsoft Teams calls from an external account impersonating help desk personnel. Two users missed the call. One answered.

The attacker presented themselves as an IT support agent responding to the email issue. They used internal company context and employee names, likely gathered from public sources such as LinkedIn, to increase credibility. This social engineering approach was effective because it aligned with the userâs immediate experience: their inbox was visibly under attack, and someone claiming to be IT support was offering help.

![mailbombing](/images/deno/mailbombing.png "mailbombing")

Figure 1: Snippet of the delivered and filtered out emails

### Detection Opportunity: Teams Impersonation

This action generated a `TeamsImpersonationDetected` operation in the Microsoft 365 Unified Audit Log because the caller used a suspicious external Microsoft tenant identity that resembled an internal IT support identity.

Organizations should monitor for this signal, especially when it occurs near bursts of inbound spam, password reset emails, subscription confirmations, or other mailbombing indicators. Correlating collaboration-platform alerts with email telemetry can provide an early warning before malware execution. The Microsoft Defender XDR platform generates alerts and detections related to suspicious activity in Microsoft Teams if the relevant Microsoft security services are enabled and integrated.

## Malware Delivery

The victim was directed to a fake self-service portal that mimicked a legitimate support workflow. The page instructed the user to download a file named `patch09913.b`. Despite the nonstandard extension, file analysis showed it was an archive that could be extracted with Windows `tar`.

![servicenow](/images/deno/servicenow.png "servicenow")

Figure 2: Malicious webpage tricking the user into downloading and running malware

The user was instructed to extract the ZIP archive into their `AppData\Roaming\DenoJSEnv` directory. Following the extraction, the primary payload was executed:

```
conhostÂ  --headless C:\Users\user.name\AppData\Roaming\DenoJSEnv\deno.exe --allow-run C:\Users\user.name\AppData\Roaming\DenoJSEnv\app.js
```

## Why Deno Matters

Deno is secure by default. **Unlike Node.js, it requires explicit permission flags for access to sensitive resources such as the file system, network, environment variables, and process execution.**

The malware author adapted to this model by splitting functionality across several scripts and launching each with the minimum permission set needed for its role.

This produced a modular architecture:

| Module | Role | Notable Permission Use |
| --- | --- | --- |
| `app.js` | Dropper and orchestrator | Spawns the remaining modules |
| `back.js` | Command-and-control bridge | Network communication, certificate error bypass |
| `helper.js` | Local command execution engine | `--allow-run`, `--allow-env` |
| `webui.js` | TCP proxy and pivot module | `--allow-net` |

This design is operationally useful for the attacker. If one component fails, the rest of the implant may continue operating. It also complicates analysis because no single module contains the entire malware capability.

## String Array Shifting

All four JavaScript files were heavily obfuscated using a common JavaScript technique known as **string array shifting**, also referred to as **array rotation**.

**This technique stores strings ...