---
title: Advent of Configuration Extraction – Part 1: Pipeline Overview – First Steps with Kaiji Configuration Unboxing
url: https://blog.sekoia.io/advent-of-configuration-extraction-part-1-pipeline-overview-first-steps-with-kaiji-configuration-unboxing/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-01
fetch_date: 2025-12-02T03:19:01.376566
---

# Advent of Configuration Extraction – Part 1: Pipeline Overview – First Steps with Kaiji Configuration Unboxing

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Advent of Configuration Extraction – Part 1: Pipeline Overview – First Steps with Kaiji Configuration Unboxing

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion, Pierre Le Bourhis and Sekoia TDR](#molongui-disabled-link)
December 1 2025

0

7 minutes reading

This article is the opening chapter of a four-part ***Advent of Configuration Extraction*** series. The series outlines the methodology we employ at Sekoia’s Threat Detection & Research (TDR) team to automate the extraction of malware configuration data, from initial analysis to the production of usable intelligence. Each post of the series focuses on a different scenario, such as analysing .NET malware or using Capstone for disassembly, to show how the approach applies across various families and techniques.

This first article introduces **Assemblyline***,* the analysis pipeline used by TDR and more specifically the configextractor service. To illustrate the workflow, we will use a simple case: the extraction of configuration data from **Kaiji,** an IoTbotnet malware. This article provides a straightforward demonstration of how the pipeline operates and how the configuration extraction service interacts with the rest of the system.

## How Assemblyline Organises Malware Analysis

[Assemblyline](https://github.com/CybercentreCanada/assemblyline) is an open-source malware analysis platform developed by the Canadian Centre for Cyber Security (CCCS). It structures analysis into a set of services, each responsible for a specific task in the processing chain. Among these services is the configuration extraction service, which identifies and processes configuration elements embedded within malware samples.

### Overview and Workflow

Assemblyline operates as a staged pipeline. Each submitted file is processed by one or more services, selected according to predefined rules and service metadata. Services are grouped by stage, which determines the order in which they run. This allows earlier services to prepare or transform the input before later ones act on it. For example, a decompression or unpacking service can run in an early stage to expand an archive or extract inner components. The resulting files are then passed to downstream services, such as the configuration extractor, which can analyse them in their final, usable form. This staged approach ensures that each service receives the most relevant data and that the overall workflow remains predictable and modular.

Assemblyline provides several APIs that allow external systems to submit files for analysis and control how they are processed. Submissions can use predefined analysis templates that specify which services should run and in what configuration. At TDR, files are collected through various channels, including sharing malware samples platform, honeypots and open directory monitoring, and are automatically submitted to Assemblyline through these APIs. The samples are analysed by various Assemblyline services, including the configuration extractor, which produces indicators of compromise that are ingested directly into our threat intelligence database, ensuring that newly identified activity is quickly reflected in detection and monitoring workflows.

![TDR malware analysis pipeline](data:image/svg+xml...)![TDR malware analysis pipeline](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2025/11/extract-part1-2-1024x549.png)

*TDR malware analysis pipeline*

### Automated Configuration Extraction Frameworks

The **[ConfigExtractor](https://github.com/CybercentreCanada/assemblyline-service-configextractor)** service in Assemblyline is dedicated to extracting malware configuration data such as C2 domains, IPs, URLs or cryptographic material from analysed samples. It leverages the open‑source [ConfigExtractor](https://github.com/CybercentreCanada/configextractor-py) Python library also maintained by CCCS. While the service supports several extraction frameworks such as MWCP, MACO, and CAPE, our extractors are built using MACO. To keep up with new malware families, the service includes an updater component that pulls extractors from a private Git repository, dynamically loads them, and installs their dependencies as needed. By default, the service also pulls some public Git repositories.

**[MACO](https://github.com/CybercentreCanada/Maco/tree/main)** (Malware Analysis Configuration Objects) is a framework designed to standardise the extraction of malware configuration data across different families and formats. It provides a structured approach to define parsers for specific malware, specifying which elements to extract and how to normalise them. Within Assemblyline, the ConfigExtractor service integrates MACO parsers to process samples. When a parser matches a given malware type via YARA rules, MACO extracts the relevant configuration fields and returns them in a consistent, structured format. This allows downstream systems to automatically consume the data, such as feeding indicators of compromise into threat intelligence platforms, without requiring custom handling for each malware family.

All scripts used for configuration extraction by the service are called modules and follow a structured workflow.

* **Library Imports**: Load necessary libraries, including MACO, for parsing and structuring configuration data.
* **Extractor Class**: Define a class that calls the extraction logic and includes a **YARA rule** to identify relevant samples. When a sample matches the YARA rule, the extractor triggers the dedicated parsing logic.
* **Extraction Logic**: A set of dedicated functions or classes parse the sample and retrieve configuration fields. Placing this logic outside the main extractor class improves portability and allows reuse across different extractors or projects.
* **Mapping to...