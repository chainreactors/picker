---
title: Detection Engineering: Practicing Detection-as-Code – Introduction – Part 1
url: https://blog.nviso.eu/2025/07/08/detection-engineering-practicing-detection-as-code-introduction-part-1/
source: NVISO Labs
date: 2025-07-09
fetch_date: 2025-10-06T23:28:50.216801
---

# Detection Engineering: Practicing Detection-as-Code – Introduction – Part 1

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

# Detection Engineering: Practicing Detection-as-Code – Introduction – Part 1

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

July 8, 2025July 13, 2025
6 Minutes

This is going to be a multipart blog series revolving around Detection Engineering and more specifically practicing Detection-as-Code in Detection Engineering. Throughout this series, we’ll dive deep into concepts, strategies, and practical blueprints that you can adapt to fit your own workflows. From building a detection engineering repository to validating detections, automating documentation, and delivering them at scale to numerous managed environments. We’ll also explore how to effectively test and monitor your detections to ensure they stay reliable.

In this first part we are going through the basic terminology and concepts of a Detection-as-Code approach in Detection Engineering.

But first things first:

## What is Detection Engineering?

> *Detection Engineering is the practice of designing, developing, testing, and maintaining threat detection logic.*

Depending on the size, needs, and maturity of the organization, the detection engineer can either be dedicated to detection engineering or have a broader role that includes tasks not strictly adhering to the definition above and may fall into a bit of grey area.

![Detection Engineer Role Meme](https://blog.nviso.eu/wp-content/uploads/2025/04/image-10.png)

While detection engineers are capable of following through these tasks and can certainly provide input on the data needed to support their work, that doesn’t necessarily make those tasks part of detection engineering, strictly speaking.

So,

## What is NOT Detection Engineering? [1]

* Audit policy configuration and telemetry generation.
* Telemetry collection and normalization.
* Building tooling to apply the detection logic to data.

Before discussing how to implement a Detections-as-Code approach we should first go through the basic steps of developing detections. Similar to software engineers that use the Software Development Life Cycle (SDLC) – a framework for planning, building, and maintaining software, detection engineers are using Detection Development Life Cycle (DDLC) [2] [3]. TheDetection Development Life Cycle (DDLC) is basically a structured approach consisting of 6 phases to design, implement, test, and maintain threat detection capabilities.

## Detection Development Life Cycle (DDLC)

There are a few variations of the framework online but the one I personally like the most is the following:

![](https://blog.nviso.eu/wp-content/uploads/2025/06/ddlc2.drawio-1.png)

A few words about each step:

**Requirement Gathering**
In this phase, the goal is to understand what threat needs to be detected and identifying the detection goals. This includes understanding the risk and urgency in order to prioritize accordingly, but also defining the success criteria for each detection.

**Design**
This phase includes selecting the appropriate data sources and events, identifying the fields needed, and mapping the detection to relevant taxonomies. The questions that should be asked during this phase are: *What’s the best way to catch it? What logs or telemetry are needed?* The design phase also includes considering edge cases, performance concerns, and potential evasion techniques.

**Development**
In development, the actual detection rule or logic is created. The goal is to write the actual query/rule/detection logic using a platform specific (e.g. KQL, EQL, SPL) or platform agnostic (e.g. Sigma) language of choice. The detection should be developed according to the design and be sufficiently documented.

**Testing** **and** **Deployment**
Testing includes validating the detection by replaying attack data or simulating the triggering behaviour to verify that it triggers correctly and tune it to minimize false positives and false negatives. Deployment includes delivering the validated detections into the production environments.

**Monitoring**
An important phase without question is monitoring. Continuously reviewing, adapting and adjusting the detection to the monitored environments to ensure optimal False Positive and False Negative rates. It is within this stage that thresholds are tuned, filter outs are performed and detections are even decommissioned if they are deemed unworthy or unmaintainable.

**Continuous Testing**
This phase involves automated testing and regular threat simulations. Continuous testing ensures the detection remains accurate, resilient to changes, and aligned with new variations or adaptations of the detected technique.

Now that we have an abstract idea of the detection development lifecycle, next, we should define what a Detection-as-Code approach means for Detection Engineering and how we can use it to implement and develop automations for the phases that we described above.

## What does it mean to practice Detection-as-Code?

> *Detection-as-Code (DaC) is the practice of managing and developing threat detections using software engineering principles.*

What characteristics of software development are we able to apply in threat detection development though?

* **Version Control**
  Usually that means a Git repository that will be used to store detection rules. It can be used for change tracking, rollbacks in case a detection breaks something and collaboration within the team members.
* **Code Reviews & PRs**
  New detections or changes in existing ones go through pull requests and peer review to encourage shared ownership and responsibility since not everything is build by a single individual.
* **Testing & Validation**
  Detections may have unit tests and syntax validation or can even be validated against real or simulated attack data before they reach a production environment to ensure that nothing breaks and they operate on optimal false positives and false negatives rates.
* **CI/CD Pipelines** [4]
  Detections are being validated and deployed using CI/CD pipelines. CI stands for Continuous Integration and CD stands for Continuous Delivery or Deployment. This means that validity tests are run as soon as a change in a detection in the repository occurs and that detections can be...