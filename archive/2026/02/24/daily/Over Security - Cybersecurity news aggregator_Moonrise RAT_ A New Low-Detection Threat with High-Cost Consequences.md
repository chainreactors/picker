---
title: Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences
url: https://any.run/cybersecurity-blog/moonrise-rat-detected/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-24
fetch_date: 2026-02-25T04:15:22.329283
---

# Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* [Guides and tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](/cybersecurity-blog/)

* + Search

![Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences](/cybersecurity-blog/wp-content/uploads/2026/02/Moonrise.png)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences

February 24, 2026

[Add comment](#comments-18719)
1091 views
8 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Moonrise-1024x497.png)

  #### Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences

  1091
  0](/cybersecurity-blog/moonrise-rat-detected/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Awards_blog-1024x497.png)

  #### G2 Recognizes ANY.RUN Among the Top 50 Best Software Companies in the Region

  452
  0](/cybersecurity-blog/g2-top-security-software-provider/)
* [![](/cybersecurity-blog/wp-content/uploads/2026/02/Effective-Alert-Enrichment-1024x497.png)

  #### One Process, Every Metric: How Better Alert Enrichment Transforms SOC Performance

  2416
  0](/cybersecurity-blog/alert-enrichment-soc-performance/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

Moonrise RAT: A New Low-Detection Threat with High-Cost Consequences

Security professionals rely on early detection signals to prioritize and contain incidents. But what happens when a fully capable RAT generates none?

In a recent investigation, the [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Moonrise-rat-analysis&utm_term=240226&utm_content=linktolanding) experts uncovered a new Go-based remote access trojan we named [Moonrise](https://x.com/anyrun_app/status/2024124064311222489/). At the time of analysis, it wasn’t detected on VirusTotal and had no vendor signatures tied to it.

That’s the problem teams can’t ignore: credential theft, remote command execution, and persistence can be active while static checks stay silent. The result is slower triage, and more escalations.

Let’s break down Moonrise’s full attack chain and show how you can detect similar threats earlier, before they turn into longer investigations and real business impact.

## Key Takeaways

* **Moonrise operated without early static detection**, establishing active C2 communication before any vendor alerts were triggered.

* The RAT supports **credential theft, remote command execution, persistence, and user monitoring**, enabling full remote control of an infected endpoint.

* **Silent C2 activity increases business exposure**, extending dwell time and raising the risk of data loss, operational disruption, and financial impact.

* Static reputation checks alone are not enough. [Behavior-based analysis](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Moonrise-rat-analysis&utm_term=240226&utm_content=linktosandboxlanding) is critical to confirm real attacker activity quickly.

## What Moonrise Means for Organizations

Moonrise isn’t just a remote access tool. Its command set shows how an attacker can move from access to impact.

* **Credential theft and clipboard monitoring** can expose passwords, session tokens, and sensitive data copied between systems.

* **Remote command execution and process control** let operators run scripts, interfere with defenses, and manipulate business applications.

* **File upload and execution** creates a clean path to drop additional payloads, including stealers or ransomware.

* **Screen capture, webcam, and microphone access** can reveal what’s happening inside finance workflows, admin panels, and internal communications.

* **Persistence and privilege-related functions** increase dwell time and make removal harder.

One compromised endpoint can disrupt operations and**lead to financial and reputational damage**, especially when the malware stays below static detection thresholds long enough to expand access.

Reduce escalation
and investigation costs
Detect threats earlier with behavior-first clarity

[Integrate in your SOC](https://any.run/enterprise/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Moonrise-rat-analysis&utm_term=240226&utm_content=linktoenterprise#contact-sales)

## Attack Details Exposed: What We Observed in Execution

You can follow the full Moonrise chain in real time, from execution to C2 control, and note the behaviors you can use for detection and triage.

[Check analysis session with Moonrise](https://app.any.run/tasks/d3e5e733-3b0d-4cf7-a7a8-ea1553cd16b9?utm_source=anyrunblog&utm_medium=article&utm_campaign=Moonrise-rat-analysis&utm_term=240226&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2026/02/Moonrise-RAT-detected-inside-ANY.RUN-sandbox-1024x569.png)

Within minutes of execution, Moonrise established outbound communication and began responding to operator-driven commands. What looked harmless in static checks immediately revealed interactive control once behavior was observed.

Reduce investigation time
from hours to minutes

 Act on evidence, not assumptions

[Register now](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=Moonrise-rat-analysis&utm_term=240226&utm_content=linktoregistration)

### 1. Session Registration and Persistent Communication

The communication begins with:

* client\_hello
* connected
* ping/pong

These commands handle client identification and keep the WebSocket session alive. This confirms that the infected system is actively connected and ready to receive instructions.

At this stage, traditional static checks still show nothing suspicious. But behaviorally, the endpoint is already under remote control.

![C2 communication overview of Moonrise RAT ](/cybersecurity-blog/wp-c...