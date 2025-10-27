---
title: Proactive threat hunting with Talos IR
url: https://blog.talosintelligence.com/proactive-threat-hunting-with-talos-ir/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-07
fetch_date: 2025-10-06T22:29:36.499329
---

# Proactive threat hunting with Talos IR

# Cisco Talos Blog

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

![](/content/images/2025/05/Proactive-Threat-Hunting-.jpg)

# Proactive threat hunting with Talos IR

By
[Mike Trewartha](https://blog.talosintelligence.com/author/mike/)

Tuesday, May 6, 2025 06:00

[Cisco Talos Incident Response](/category/cisco-talos-incident-response/)

At Cisco Talos, we understand that effective cybersecurity isn’t just about responding to incidents — it’s about preventing them from happening in the first place. One of the most powerful ways we do this is through [proactive threat hunting](https://talosintelligence.com/incident_response/hunting). Our [Talos Incident Response](https://talosintelligence.com/incident_response) (Talos IR) team works closely with organizations to not only address existing threats but to anticipate and mitigate potential future risks. A key component of our threat-hunting approach is the [Splunk](https://www.splunk.com/) SURGe team’s [PEAK Threat Hunting Framework](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html), which enables us to conduct comprehensive and proactive hunts with precision.

## What is the PEAK Threat Hunting Framework?

The PEAK Framework (Prepare, Execute, and Act with Knowledge) offers a structured methodology for conducting effective and focused threat hunts. It ensures that every hunt is aligned with an organization's specific needs and threat landscape. At the core of the PEAK framework are baseline hunts, which lay the foundation for proactive threat detection, alongside advanced techniques such as hypothesis-driven hunts and model-assisted threat hunts (M-ATH), which further enhance threat detection and mitigation.

### Baseline hunts: the foundation of proactive threat hunting

Baseline hunts involve establishing a clear understanding of an organization’s normal operating environment in terms of user activity, network traffic and system processes. By documenting and analyzing this baseline, Talos IR can identify anomalous behavior that may signal malicious activity.

While these hunts can be a reactive measure, it's important to use them proactively to detect threats trying to blend in with regular operations, such as insider threats, advanced persistent threats (APTs) and even novel attack techniques that might otherwise go undetected.

The key steps in baseline hunts are:

1. Defining Normal Activity: Understanding what “normal” looks like in your environment, using data from system logs, user behavior, and network traffic.
2. Anomaly Detection: Proactively hunting for deviations from the baseline that could indicate potential threats.
3. Refining the Baseline: Continuously improving and updating the baseline to account for emerging threats and changes in your infrastructure.

### Hypothesis-driven hunts: Testing assumptions about threats

In addition to baseline hunts, Talos IR also uses hypothesis-driven hunts to proactively test assumptions about potential threats. These hunts are guided by specific hypotheses or educated guesses about what attackers might be doing in a given environment. Rather than relying on a static, one-size-fits-all approach without adjustments, hypothesis-driven hunts are dynamic, adapting to the specific questions and emerging threats that arise.

For example, a hypothesis-driven hunt might begin with the assumption that a particular group of users is being targeted by a phishing campaign. The hunt would focus on testing this assumption by looking for evidence of malicious emails, unusual login patterns or attempts to collect or exfiltrate data.

The key steps in hypothesis-driven hunts are:

1. Forming Hypotheses: Based on threat intelligence and past incidents, teams generate specific hypotheses about possible attack vectors or adversary behaviors.
2. Testing Hypotheses: Using data sources such as endpoint telemetry, authentication logs or network traffic, the hypothesis is tested to see if evidence supports the theory.
3. Analyzing Results: If the hypothesis is validated, further investigation is done to understand the full scope of the potential threat.

### Model-assisted threat hunts: Leveraging machine learning to find hidden threats

Another powerful tool in Talos IR’s proactive hunting approach is model-assisted threat hunts (M-ATHs). These hunts leverage machine learning and advanced statistical models to sift through vast amounts of data and identify patterns that may indicate hidden threats. M-ATHs allow our team to detect threats that would be difficult to find using traditional methods.

Machine learning models are trained to detect suspicious behavior across different domains — such as user activity, network traffic or system logs — by looking for deviations from typical patterns. Over time, as these models learn from new data and threat intelligence, they improve in their ability to detect emerging threats.

The key steps in M-ATHs are:

1. Data Collection: Gathering large datasets from multiple sources, including network traffic, endpoint data, authentication logs, and more.
2. Model Training: Using machine learning algorithms to identify patterns in normal and malicious behavior.
3. Anomaly Detection: The trained model helps identify new, previously undetected anomalies or potential threats by looking for deviations from established patterns.
4. Refinement: The model is refined as new data is collected and analyzed, improving its ability to detect subtle threats.

## Empowering threat hunts with Talos Threat Intelligence

A crucial element that enriches and empowers every [Talos IR threat hunt](https://talosintelligence.com/incident_response/hunting) is Talos Threat Intelligence. By integrating up-to-date, high-fidelity threat intelligence into our hunts, we enhance the accuracy, relevance, and speed of our investigations. Talos Threat Intelligence provides a continuous stream of dat...