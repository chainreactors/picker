---
title: Detection Engineering: Practicing Detection-as-Code – Repository – Part 2
url: https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/
source: NVISO Labs
date: 2025-07-18
fetch_date: 2025-10-06T23:38:58.342078
---

# Detection Engineering: Practicing Detection-as-Code – Repository – Part 2

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Detection Engineering: Practicing Detection-as-Code – Repository – Part 2

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

July 17, 2025August 19, 2025
12 Minutes

In Part 1, we introduced Detection-as-Code, covering its core concepts and benefits and the Detection Development Life Cycle (DDLC) essential for modern threat detection practices.

In the second part of the Practicing Detection-as-Code series, we will cover some basic elements of designing a repository to develop, store, and deploy detections from. We’ll go through several different aspects of the setup like the Git platform, branch strategy, repository structure, detections structure, taxonomies, and content packs. These are core elements that we will inevitably encounter when designing our repository and it is important to put some thought into them early, so that we avoid unnecessary refactoring down the road and ensure our work is as organized and structured as possible.

However it is important to note beforehand that the principles, methodologies, and design elements are intended to be used as a blueprint that can be adjusted to meet the individual needs of your team. What may work for a larger team focused exclusively on detection engineering may not fit a smaller one that may have mixed roles and responsibilities. Your ultimate goal should be to adapt these elements to your internal processes, to provide structure and improve efficiency in your detection engineering day-to-day tasks. Be cautious of over-engineering, as it can drain your resources without adding significant value.

## Selecting the Git Platform

The first step in implementing a Detection-as-Code approach is selecting the Git platform. You can choose GitHub, Gitlab, AWS CodeCommit, Azure DevOps or another platform, depending on your organization’s preferred technology stack. For the purposes of this blog series, we will provide examples from a repository hosted on Azure DevOps.

## Standardizing Detection Structure

The next step is to standardize the detections stored in the repository. In the context of Detection-as-Code, standardization refers to enforcing uniform structures and formats across the detections library. Adhering to a predefined set of conventions will help us maintain and search the detection library with less effort.

Using YAML or JSON to store your detections is a battle-tested approach. These data-serialization formats offer the advantage of being structured, human-readable, and integrating well with CI/CD. Furthermore, many platforms support exporting rules directly in JSON, YAML, or even XML format.

The metadata fields available for detection rules vary depending on the platform. Some platforms will allow you to store tags and notes while others are limited to only a title and description field. If you are also supporting multiple platforms, this inconsistency of available fields could be problematic. In that case, maintaining a dedicated metadata file alongside the detection could be a beneficial approach. For inspiration on what kind of information you should include in your metadata file, so that the detection is sufficiently documented, you can consult the Sigma Specification [1], which is a vendor agnostic detection format, or Palantir’s Alerting and Detection Strategy Framework [2]. You can either adopt and extend one of those or create your own. Whichever your choose, we recommend to include at least the following fields:

```
id:                     # A unique identifier for the detection.
title:                  # A brief title for the detection.
description:            # A comprehensive description of the detection.
level:                  # Severity of the detection (low, medium, high).
version:                # The version of the detection that we are on.
references:             # References to the source(s) that the detection was derived from e.g. blogs, papers, presentations, tweets.
  -
data_sources:           # The data source on which the detection relies.
  - category:           # The category of the log source e.g. dns, network, os.
    vendor:             # The vendor e.g. cisco, microsoft.
    product:            # The product e.g. asa, windows.
    service:            # The service e.g. traffic_logs, security_event, antivirus.
    event_id:           # The event ID used e.g. ASA-3-201008, 4688
blindspots:             # Recognized shortcomings of the detection.
  -
known_false_positives:  # A list of known false positives that may occur.
  -
investigation_steps:    # Investigation steps that the analyst can follow to investigate an alert generated by this detection.
  -
tags:                   # Taxonomies or notable things about the detection.
  - tactic.$tactic      # MITRE ATT&CK tactics.
  - technique.tXXXX.XXX # MITRE ATT&CK (sub)techniques.
  - group.gxxx          # MITRE ATT&CK adversary group name.
  - software.sxxx       # MITRE ATT&CK software name.
  - car.XXXX-XX-XXX     # MITRE Cyber Analytics IDs.
  - cve.xxxx-xxxxxx     # CVE IDs.
  - notable.$entity     # Notables about the detection e.g. name of lolbin.
```

```
id:                     # A unique identifier for the detection.
title:                  # A brief title for the detection.
description:            # A comprehensive description of the detection.
level:                  # Severity of the detection (low, medium, high).
version:                # The version of the detection that we are on.
references:             # References to the source(s) that the detection was derived from e.g. blogs, papers, presentations, tweets.
  -
data_sources:           # The data source on which the detection relies.
  - category:           # The category of the log source e.g. dns, network, os.
    vendor:             # The vendor e.g. cisco, microsoft.
    product:            # The product e.g. asa, windows.
    service:            # The service e.g. traffic_logs, security_event, antivirus.
    event_id:           # The event ID used e.g. ASA-3-201008, 4688
blindspots:             # Recognized shortcomings of the detection.
  -
known_false_positives:  # A list of known false positives that may occur.
  -
investigation_steps:    # Investigation steps ...