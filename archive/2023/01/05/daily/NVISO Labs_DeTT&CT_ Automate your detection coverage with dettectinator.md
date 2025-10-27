---
title: DeTT&CT: Automate your detection coverage with dettectinator
url: https://blog.nviso.eu/2023/01/04/dettct-automate-your-detection-coverage-with-dettectinator/
source: NVISO Labs
date: 2023-01-05
fetch_date: 2025-10-04T03:04:21.631863
---

# DeTT&CT: Automate your detection coverage with dettectinator

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

# DeTT&CT: Automate your detection coverage with dettectinator

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

January 4, 2023March 12, 2024
6 Minutes

## Introduction

Last year, I published an article on mapping detection to the MITRE ATT&CK framework using [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT). In the article, we introduced DeTT&CT and explored its features and usage. If you missed it, you can find the article [here](https://blog.nviso.eu/2022/03/09/dettct-mapping-detection-to-mitre-attck/).

Although, after writing that article, I encountered some challenges. For instance, I considered using DeTT&CT in a production environment but there were hundreds of existing detection rules to consider, and it would have been a tedious process to manually create the necessary YAML file for building a detection coverage layer. As a result, I decided not to use DeTT&CT and instead focused on increasing detection in other ways.
Fortunately, a new tool called [Dettectinator](https://github.com/siriussecurity/dettectinator) has recently been released. Its purpose is to address these kinds of issues and make it easier to automate detection coverage.

In this article, we will explore Dettectinator, its features, and walk through the steps to automate the detection coverage for Sentinel Analytics rules and Elastic detection rules.

## What is dettectinator

Dettectinator is a tool developed by Martijn Veken and Ruben Bouman of Sirius Security that enables the automation of DeTT&CT data source and technique administration YAML files needed to create visibility and detection layers in the ATT&CK Navigator. This tool can be integrated as a Python library within your security operations center (SOC) automation tools or used via the command line.

To use the Python library, install it with “pip install dettectinator” and import one of the following classes into your code:

* DettectDataSourcesAdministration
* DettectTechniquesAdministration

These classes allow you to programmatically edit [DeTT&CT YAML files](https://blog.nviso.eu/2022/03/09/dettct-mapping-detection-to-mitre-attck/), including creating new data source and techniques administration files and modifying existing ones.

```
from dettectinator import DettectDataSourcesAdministration
from dettectinator import DettectTechniquesAdministration

# Open an existing YAML file:
dettect_ds = DettectDataSourcesAdministration('data_sources.yaml')

# Or create a new YAML file:
dettect_ds = DettectDataSourcesAdministration()

# Open an existing YAML file:
dettect = DettectTechniquesAdministration('techniques.yaml')

# Or create a new YAML file:
dettect = DettectTechniquesAdministration()
```

To run as a CLI tool:

```
$ python dettectinator.py

Please specify a valid data import plugin using the "-p" argument:
 - DatasourceCsv
 - DatasourceDefenderEndpoints
 - DatasourceExcel
 - DatasourceWindowsSecurityAuditing
 - DatasourceWindowsSysmon
 - TechniqueCsv
 - TechniqueDefenderAlerts
 - TechniqueDefenderIdentityRules
 - TechniqueElasticSecurityRules
 - TechniqueExcel
 - TechniqueSentinelAlertRules
 - TechniqueSigmaRules
 - TechniqueSplunkConfigSearches
 - TechniqueSuricataRules
 - TechniqueSuricataRulesSummarized
 - TechniqueTaniumSignals
```

```
$ python3 dettectinator.py -p TechniqueElasticSecurityRules -h

Plugin "TechniqueElasticSecurityRules" has been found.
usage: dettectinator.py [-h] [-c CONFIG] -p PLUGIN -a APPLICABLE_TO [-d {enterprise,ics,mobile}] [-i INPUT_FILE] [-o OUTPUT_FILE] [-n NAME] [-s STIX_LOCATION] [-ch] [-cl] [-ri RE_INCLUDE] [-re RE_EXCLUDE]
                        [-l LOCATION_PREFIX] [-clp] --host HOST --user USER --password PASSWORD [--filter FILTER]
```

Dettectinator provides a range of plugins for various detection systems and data source platforms, and you can even create custom plugins to suit your specific workflow. Some of the available plugins for detection include:

* Microsoft Sentinel: Analytics Rules (API)
* Microsoft Defender: Alerts (API)
* Microsoft Defender for Identity: Detection Rules (loaded from MS Github)
* Tanium: Signals (API)
* Elastic Security: Rules (API)
* Suricata: rules (file)
* Suricata: rules summarized (file)
* Sigma: rules (folder with YAML files)
* Splunk: saved searches config (file)
* CSV: any csv with detections and ATT&CK technique ID’s (file)
* Excel: any Excel file with detections and ATT&CK technique ID’s (file)

Plugins for data sources include:

* Defender for Endpoints: tables available in Advanced Hunting (based on OSSEM)
* Windows Sysmon: event logging based on Sysmon (based on OSSEM and your Sysmon config file)
* Sentinel Window Security Auditing: event logging (based on OSSEM and EventID’s found in your logging)
* CSV: any csv with ATT&CK data sources and products (file)
* Excel: any Excel file with ATT&CK data sources and products (file)

It’s easy to create your own Dettectinator plugins or edit the ones provided to cover additional scenarios. An instruction on how to create your own plugins can be found [here](https://github.com/siriussecurity/dettectinator/wiki/Using-plugins#create-your-own-plugins).

Dettectinator can be seamlessly integrated into your detection engineering workflow, as illustrated in the picture below. Steps 1 and 3 can be automated using version control system (VCS) pipelines or scheduling. The analyst can enhance the techniques identified by Dettectinator by assigning appropriate scores, resulting in an enriched YAML file that can be used in future runs of the tool.

![Dettectinator workflow](https://blog.nviso.eu/wp-content/uploads/2023/01/image-2.png)

Figure 1: Dettectinator workflow

## How to use dettectinator

To illustrate how to use Dettectinator from a production environment, we will walk through the steps to build your coverage from Elastic Security detection rules and Microsoft Sentinel analytics rules.

Let’s start with Elastic Security. As shown in the picture below, we enabled the built-in detection rules from Elastic which represent 724 rules in total.

![Elastic Security detection rules](https://blog.nviso.eu/wp-content/uploads/2023/01/image-3.png)

Figure 2: Elastic Security detection rules

Ensure that the Elastic user has the appropriate permissions to manage...