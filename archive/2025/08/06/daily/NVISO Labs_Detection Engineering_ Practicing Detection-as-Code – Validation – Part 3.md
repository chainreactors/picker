---
title: Detection Engineering: Practicing Detection-as-Code – Validation – Part 3
url: https://blog.nviso.eu/2025/08/05/detection-engineering-practicing-detection-as-code-validation-part-3/
source: NVISO Labs
date: 2025-08-06
fetch_date: 2025-10-07T00:18:29.992312
---

# Detection Engineering: Practicing Detection-as-Code – Validation – Part 3

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

# Detection Engineering: Practicing Detection-as-Code – Validation – Part 3

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

August 5, 2025August 23, 2025
39 Minutes

In [Part 2](https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/) of the series, we covered the basics of designing a repository to store detections and established the format and structure for detections and content packs.

In this part, we focus on implementing validation checks to improve consistency and ensure a minimum level of quality within the detection repository. Setting up validation pipelines is a key step, as it helps enforce the defined standards, reduce errors, and ensure that detections are reliable and consistent. We’ll break the validation process into several smaller scripts and pipelines that you can refer to when building your own validation workflows. This approach also helps make the content of this blog post easier to digest.

## Repository Branch Policies

In [Part 1](https://blog.nviso.eu/2025/07/08/detection-engineering-practicing-detection-as-code-introduction-part-1/) of this blog series, we included a diagram illustrating how adopting Detection-as-Code requires that changes to detection code undergo manual peer review. In Azure DevOps Repos, this principle can be implemented and enforced using repository branch policies. Branch policies help ensure that our quality controls are followed, such as requiring pull requests for changes, mandating code reviews by team members, setting a minimum number of reviewers, running validation pipelines, and verifying that all comments are resolved before changes are merged.

We can configure branch policies for our repository in Azure DevOps under the repository settings and the policies tab of the main branch.

![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-11.png)
![](https://blog.nviso.eu/wp-content/uploads/2025/05/image-12.png)

## Validation Checks

Regarding the types of validation checks we can implement, we have included the following:

* **Detections**
  + **Schema** – Check that structured files in detections (e.g., JSON, YAML) conform to their defined schemas.
  + **Query syntax** – Validate that detection queries use correct syntax for the target platform.
  + **References** – Ensure that all referenced URLs in metadata files are not broken.
  + **Spelling** – Scan metadata files for spelling errors to maintain quality and clarity.
* **Content Packs**
  + **Schema** – Check that content packs conform to their defined schemas.
  + **References** – Verify that all detections referenced by content packs actually exist within the repository.
* **Repository**
  + **Structure** – Ensure that required directories (e.g. detections/, parsers/, content\_packs/ etc.) are present, naming conventions (e.g. lowercase, proper prefixes/suffixes) are followed, and that each directory contains the expected files.

Before moving forward with automating these validation checks, we’ll first talk a bit about Azure Pipelines [1] and JSON schemas [2].

## Azure Pipelines

Azure Pipelines is a component of Azure DevOps that automatically builds, tests, and deploys code projects. We will be using Azure Pipelines in this blog series, however there are other alternatives, like GitHub Actions or AWS CodePipeline, depending on the Git platform you selected.

In Azure DevOps, a pipeline may consist of the following basic components [3]:

* **Triggers** that define when the pipeline should start, typically based on code changes in specific branches or parts of the code.
* **Stages** that organize the pipeline into major phases, such as build, test, and deploy, each containing multiple jobs.
* **Jobs** that are units of work executed on agents, potentially running tasks in parallel.
* **Steps** that are defined within jobs and are the individual tasks or scripts that perform specific actions, like installing dependencies or executing scripts.

As an example, the following pipeline will execute the script example.py whenever changes on the main branch occur that include a JSON file.

```
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - "*.json"

stages:
- stage: ExampleStage
  displayName: "Example Stage"
  jobs:
  - job: ExampleJob
    displayName: "Example Job"
    steps:
    - script: |
        python scripts/example.py
      displayName: 'Execute Example Script'
```

```
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - "*.json"

stages:
- stage: ExampleStage
  displayName: "Example Stage"
  jobs:
  - job: ExampleJob
    displayName: "Example Job"
    steps:
    - script: |
        python scripts/example.py
      displayName: 'Execute Example Script'
```

YAML

## JSON Schemas

A JSON schema defines the rules and structure that JSON data must follow. It specifies elements such as required fields, accepted data types (e.g., string, number, boolean), and allowed values. This helps identify human errors early, such as missing fields, incorrect data types, invalid values, or typos. By defining validation schemas for the repository’s detections and content packs, we can ensure consistency across the codebase and improve the overall reliability and quality of the detection library.

An example JSON structure and its corresponding schema are shown below. The schema includes a string field that allows only letters and spaces, with a minimum length of 5 and a maximum of 20 characters. A number field is constrained to values between 0 and 100. A boolean field accepts true or false values, while a null field explicitly allows null values. Additionally, there is an array field that must contain between 2 and 5 unique strings, each string having at least 3 characters. The schema also enforces required properties and forbids any additional unspecified fields.

```
{
  "string_example": "string example",
  "integer_example": 42,
  "boolean_example": true,
  "null_example": null,
  "array_example": ["item1", "item2", "item3"]
}
```

```
{
  "string_example": "string example",
  "integer_example": 42,
  "boolean_example": true,
  "null_example": null,
  "array_example": ["it...