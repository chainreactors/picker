---
title: Introducing BitSight Automation Tool
url: https://blog.nviso.eu/2023/08/08/introducing-bitsight-automation-tool/
source: NVISO Labs
date: 2023-08-09
fetch_date: 2025-10-04T12:01:40.023386
---

# Introducing BitSight Automation Tool

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

# Introducing BitSight Automation Tool

[Konstantinos Papanagnou](https://blog.nviso.eu/author/konstantinos-papanagnou/ "Posts by Konstantinos Papanagnou")

[Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)

August 8, 2023August 17, 2023
17 Minutes

1. [Glossary](#glossary)
2. [Introduction](#introduction)
3. [BitSight](#bitsight)
4. [Automation](#automation)
   1. [Operations](#operations)
5. [Structure](#structure)
6. [Installation](#installation)
   1. [Prerequisites](#prerequisites)
   2. [Configuration](#configuration)
   3. [Generating an API key for your BitSight account](#generating-an-api-key-for-your-bitsight-account)
   4. [Adding the API Key to the BitSight Automation Tool](#adding-the-api-key-to-the-bitsight-automation-tool)
      1. [Windows](#windows)
      2. [Linux](#linux)
   5. [The group\_mapper.json file](#the-group-mapper-json-file)
   6. [The guid\_mapper.json file](#the-guid-mapper-json-file)
   7. [Configuring your Company’s structure](#configuring-your-company-s-structure)
      1. [The groups.conf file](#tool-modification)
      2. [Letting BitSight Automation Tool handle the rest](#letting-bitsight-automation-tool-handle-the-rest)
   8. [Binding into Executable](#binding-into-executable)
7. [Execution](#execution)
   1. [Usage](#usage)
   2. [Use Cases](#use-cases)
      1. [Functional Operation: Rating](#functional-operation-rating)
      2. [Functional Operation: Historical](#functional-operation-historical)
      3. [Functional Operations: Findings](#functional-operations-findings)
      4. [Functional Operation: Assets](#functional-operation-assets)
      5. [Functional Operation: Reverse Lookup](#functional-operation-reverse-lookup)
      6. [Supplementary Operation: List](#supplementary-operation-list)
      7. [Supplementary Operation: Update](#supplementary-operation-update)
   3. [Task Scheduler / Cron Jobs](#task-scheduler-cron-jobs)
      1. [Windows – Task Scheduler](#windows-task-scheduler)
      2. [Linux – Cron Jobs](#linux-cron-jobs)
8. [Troubleshooting](#troubleshooting)
   1. [Total Risk Monitoring Subscription Required](#total-risk-monitoring-subscription-required)
   2. [File not Found \*.JSON](#file-not-found-json)
9. [Conclusion](#conclusion)

# Glossary

|  |  |
| --- | --- |
| Entity | A part of an organization that can be assessed as a single figure. |
| Subsidiary | Same as an Entity on BitSight’s side. |
| Group Cluster | A complex. It can contain entities/subsidiaries, or Groups, or more Group Clusters. |
| Group | A structure that can contain Entities. |

Glossary

# Introduction

In this blog post you will be introduced to the BitSight Automation Tool (<https://github.com/NVISOsecurity/BitSight-Automation-Tool>). BitSight Automation was developed to automate certain manual procedures and extract information such as ratings, assets, findings, etc. Automating most of these tasks is crucial for simplicity and time saving. Besides that, this tool also provides the possibility to collaborate with Scheduled Tasks and cronjobs. You can configure the tool to execute in certain intervals or dates, and retrieve the results from the desired folder without needing to interact with it.

# BitSight

What is BitSight? BitSight is a solution that helps organizations perform three (3) main functions.

1. Quantify their cyber risk
2. Measure the impact of their security efforts
3. Benchmark their performance against peers

It does all that by managing the company’s external facing infrastructure both automatically and manually, by allowing a company to provide updates to BitSight in order to keep their database up to date.

Other functions that are useful and provided by BitSight are:

* Performing periodic vulnerability assessments on those assets to determine the risk factors and reports back the findings.
* Identifies malicious activity such as botnet infections and much more that adds up to the risk factor.
* Provides detailed remediation tips to remediate findings.

# Automation

By utilizing parts of the [BitSight API](https://github.com/InfosecSapper/BitSightAPI) Python wrapper developed by InfosecSapper, we developed an open source tool for the community to use, that fully automates some of BitSight’s operations, which we have named BitSight Automation Tool. This tool has a lot of potential to expand further with even more operations based on the needs that might arise.

## Operations

You might be wondering by this point, what operations can this tool automate? Currently we have 5 operations that can be automated + 2 supplementary to assist with the tool’s maintenance.

1. **Rating** -> Retrieve the current score of an entity and confirm it’s above or equal to your company’s required security policies or digital mandate.
2. **Findings** -> Generate a filtered list of vulnerabilities for an entity to remediate.
3. **Assets** -> Retrieve the asset count and asset list of an entity, to validate your public IP space.
4. **Reverse Lookup** -> Investigate where an IP, IP Range, domain or domain wildcard is attributed to and what IPs or domains it is associated with.
5. **Historical Ratings** -> Sets up an overview of ratings for a given entity or group over a specified timeframe (maximum 1 year) to showcase in reports and review progress or regress.

* **List** ->  Review the correlation between an entity’s custom given name and BitSight’s given name in a list for all defined entities.
* **Update** -> Automatically update the tool and its respective JSON files.

# Structure

The below image is a representation of the current state of the tool. At the time of writing the tool comes with the following structure.

* **BitSightAPI**: This folder contains certain vital Python files from the BitSightAPI Python wrapper.
* **ArgumentsHandler.py**: This file contains the instructions on how to parse the tool’s arguments.
* **README.md**: This file is your friend. It contains all the information on how to execute with examples, as well as troubleshooting advice.
* **bitsight\_automation.py**: This file is the heart of the tool. You can execute this Python file and use it for your Scheduled tasks or cron jobs.
* **group\_mapper.json**: This file is a JSON structure which represents the mapping of the groups and entities within your organization. (More on this in a dedicated section)
* **guid\_mapper.json**: This file is a JSON struc...