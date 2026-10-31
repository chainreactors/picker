---
title: Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 1 – Introduction and Concept
url: https://blog.nviso.eu/2026/10/30/detection-engineering-implementing-detection-as-code-in-an-existing-environment-part-1-introduction-and-concept/
source: NVISO Labs
date: 2026-10-30
fetch_date: 2026-10-31T07:46:32.162080
---

# Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 1 – Introduction and Concept

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# Detection Engineering: Implementing Detection-as-Code in an Existing Environment: Part 1 – Introduction and Concept

[Felix Hartmond](https://blog.nviso.eu/author/felix-hartmond/)

[Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

October 30, 2026October 30, 2026
8 Minutes

This entry is part 1 in the series [Detection Engineering: Implementing Detection-as-Code in an Existing Environment](https://blog.nviso.eu/series/detection-engineering-implementing-detection-as-code-in-an-existing-environment/ "Detection Engineering: Implementing Detection-as-Code in an Existing Environment")

---

This article presents a case study of how Detection Engineering can be improved by applying Detection-as-Code principles in an established, operational environment.

The focus is deliberately practical. The environment already had an active detection library, ongoing development work, and regulatory requirements requiring the continuous development and deployment of new detections. The migration therefore had to improve the engineering model without causing material disruption to existing operations.

Previously, my colleague Stamatis Chatzimangou published [a detailed series](https://blog.nviso.eu/series/detection-engineering-practicing-detection-as-code/) on this blog about Detection Engineering and Detection-as-Code, covering the underlying concepts and building blocks. If you are new to Detection-as-Code, I recommend reading that series first.

This case study summarises work performed in a recent customer project. Some details have been removed or adjusted to protect customer confidentiality. However, the technical challenges we faced and the essential migration steps remain intact, providing a realistic view of how such a transformation can be carried out in a live environment.

## Starting Position

The environment contained multiple detection platforms, each requiring platform-specific detection implementations. This article uses Splunk as its primary example and explains how other platforms fit into the resulting structures and processes without covering them in detail.

The organisation had already taken initial steps towards Detection-as-Code. Some detection-related data was stored and versioned in Git repositories. Changes were reviewed through pull requests, and development work was tracked through issues on a GitHub Project board.

Each detection platform had its own repository containing the relevant configuration. In the Splunk case, the repository largely contained the complete `apps` directory that was deployed to the Splunk infrastructure. A manual deployment process copied this directory to the Splunk server and reloaded the configuration. Other platforms used separate repositories containing their respective configuration files.

In addition to the detection implementations in the platform configurations, each detection had a metadata document in YAML format. These documents were still stored on a file share. Test implementations based on Atomic Red Team were also available. However, each test file contained test cases for all detections covering the same MITRE ATT&CK technique, and the tests were stored within the Splunk repository.

The existing setup provided a useful starting point. Git-based storage and existing deployment processes meant that the project could focus on improving data handling and engineering workflows. The deployment mechanisms for the detection platforms did not need to be replaced, provided that the new process could still generate the required Splunk app configuration and equivalent artefacts for other platforms. Developers were also already familiar with Git, issues, pull requests, and project boards.

## Weaknesses

At the same time, the existing setup had several significant weaknesses. The data was organised by detection platform rather than by the semantic unit developers worked on: the individual detection. Files belonging to one detection were distributed across multiple locations, including multiple repositories and a file share. As a result, a single change could require multiple pull requests and separate file-share changes. This made development and review unnecessarily difficult, increased the likelihood of human error, and made it hard to trace changes reliably.

For example, `savedsearches.conf` files in the Splunk apps contained several thousand lines of configuration for many unrelated detections. Such files are difficult to review as GitHub does not always render them conveniently. Further they can contain configuration fragments for detections that have already been retired but were never removed.

With this fragmented data, there was reduced visibility into data quality, completeness, and coverage. Thereby, reviews required substantial manual effort. Furthermore, without confidence in the data consistency and general quality, the files could only be used to deploy detections to the platforms, but they were not suited for further use, and a need existed for separately maintained reports and lists. In addition to the manual effort required to keep these up to date and in sync, significant potential was lost. Cleanly structured and validated data would enable fully automated report generation, data analysis, and further integrations (for example automated generation of compliance reports required by auditors). This would progressively eliminate manual work for developers, reviewers, and other stakeholders who need to assess information from the detection library.

## Goals

To address these issues, we defined three goals:

1. **Restructure the existing data**
   The data structure should reflect the semantic structure of detections and the way developers interact with them. Platform-specific structures should be generated automatically by deployment processes.
2. **Consolidate all detection-related data in GitHub**
   All data maintained outside GitHub should be mig...