---
title: Detection Engineering: Practicing Detection-as-Code – Versioning – Part 5
url: https://blog.nviso.eu/2025/09/09/detection-engineering-practicing-detection-as-code-versioning-part-5/
source: NVISO Labs
date: 2025-09-10
fetch_date: 2025-10-02T19:54:24.211160
---

# Detection Engineering: Practicing Detection-as-Code – Versioning – Part 5

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

# Detection Engineering: Practicing Detection-as-Code – Versioning – Part 5

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

September 9, 2025September 9, 2025
29 Minutes

In software engineering, versioning is the process of assigning unique identifiers to different states or iterations of a software product. The identifiers (a.k.a version numbers) help developers and users track updates, changes, or bug fixes made to the software over time. Versioning is essential for managing software development, ensuring compatibility, and communicating changes to the end users.

In detection engineering, and especially when practicing Detection-as-Code, versioning is just as important. Versioning in the detection library helps us maintain traceability and track changes to individual detections and content packs. It can help us pinpoint the exact state of specific detections at a given point in time, provides a clear history of updates and facilitates troubleshooting and debugging by identifying which version introduced particular changes.

The two most common versioning schemes are Calendar Versioning [1] and Semantic Versioning [2]. In this part, we are going to explore how we could adapt those versioning schemes in our repository.

## Calendar Versioning

Calendar versioning, often referred to as CalVer, is a versioning scheme where the version number is based on the release date. Typically, the format includes the year and month of the release, but it can also be something like YYYY.MM.DD (e.g. 2025.08.23). Calendar versioning is particularly useful for projects with regular release cycles, as it is very intuitive and allows for easy understanding of the timing of releases.

An example of calendar versioning in the scope of detection engineering is the Sigma repository releases [3]. Sigma rules are also being tagged with the modified date which can be used as an identifier for updates on each iteration of the rule.

## Semantic Versioning

Semantic versioning, often referred to as SemVer, is a versioning system that uses a three-part number format – **MAJOR**.**MINOR**.**PATCH** (e.g. v1.0.1). Each part of the version number conveys specific information:

* **MAJOR** – Incremented when there are incompatible changes that may affect backward compatibility.
* **MINOR** – Incremented when new features are added in a backward-compatible manner.
* **PATCH** – Incremented for backward-compatible bug fixes.

This approach helps developers and users understand the nature of changes in each update, ensuring that the impact of updates on existing implementations is clear. Semantic versioning is particularly useful for effective dependency management and communication during the evolution of software projects and very commonly used in APIs.

An example of Semantic versioning in the scope of detection engineering is the Azure Sentinel detections repository [4].

## Versioning in Detection-as-Code

When talking about versioning in the context of Detection Engineering and specifically Detection-as-Code, we are talking about detection library releases, detection versioning, and content pack versioning. We are going to explore those areas and see how we can adopt or adjust the principles that we discussed so far, in our detection library.

### Detection Versioning

In [Part 2](https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/), we defined our metadata file and content pack formats, for which the Semantic versioning scheme was used. Although the Semantic versioning scheme definition is very focused on software, we can adopt it and adjust it to detections and assign an analogous meaning to the **MAJOR**.**MINOR**.**PATCH** format.

* **MAJOR** – A major version change indicates significant changes to the detection rules that may also modify the detection logic. This could involve a complete overwrite of the detection logic, or changes that where caused by modifications to other components used by the rule, e.g. changes in the parser of the logs.
* **MINOR** – A minor version change reflects enhancements to the detection rules. This might include enhancing the metadata of the rule, for example, by adding investigation steps, tags, updating the description etc, but also modifications to the queries like re-arranging conditions to improve performance, renaming fields and others.
* **PATCH** – A patch version change, includes bug fixes to the detection rules. This involves changes that fix and incorrect behaviour of the rule without altering the rule’s core detection logic.

By assigning meaning to versions with Semantic versioning, we can very easily track over time which detections required the most effort by the detection engineering team and why. This is a major advantage, when we do periodic reviews of the detection library, and needs to figure out which detections have been through the most iterations. That way we can review the detection content effectively and possibly identify problematic detections.

### Content Pack Versioning

Considering that content packs are collections of rules, changes to the version of detections increment the version of the content pack as well. However there may be other cases that can cause the version of the content pack to be incremented.

* **MAJOR** – A major version change indicates significant updates to the content pack that may not be backwards compatible. For example, that could be the addition of rules that only work with a specific version of parser or the addition of a batch of rules that greatly enhances the detection capabilities of the content pack.
* **MINOR** – A minor version change represents enhancements to the detections of the content pack, or additions of new ones. For example, the addition or removal of detections to the content pack, without however greatly affecting the detection capabilities of the pack as would be the case if we added or removed 1 detection from a 100 rule pack.
* **PATCH** – A patch version change includes bug fixes to the content pack. This could involve fixing bugs in existing detections, or removing a detection from the content pack that has caused a blowout of alerts.

Versi...