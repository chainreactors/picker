---
title: Detection Engineering: Practicing Detection-as-Code – Documentation – Part 4
url: https://blog.nviso.eu/2025/08/26/detection-engineering-practicing-detection-as-code-documentation-part-4/
source: NVISO Labs
date: 2025-08-27
fetch_date: 2025-10-07T00:47:50.179747
---

# Detection Engineering: Practicing Detection-as-Code – Documentation – Part 4

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

# Detection Engineering: Practicing Detection-as-Code – Documentation – Part 4

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/)

August 26, 2025September 4, 2025
35 Minutes

Most engineers find documentation unappealing because it often feels like a chore that takes away time from more engaging tasks that solve technical problems and can feel tedious when we are focused on delivering functionality or fixing urgent issues. Regardless, sufficiently documenting our detections is essential in detection engineering as it provides context around the purpose, detection logic, and expected behaviour of each detection rule. Documentation also helps other teams, like SOC analysts, understand what a detection is looking for, how it was built, and how to respond when it fires.

Just as important as documenting individual detections is tracking how the overall detection library evolves. In most cases, the detection library is dynamic and evolves over time to include new content packs and detections as well as modifications to existing ones. These changes impact how the environment is monitored, so it’s crucial to keep other teams informed. In that sense we need to figure out a way to generate a type of change log for our detection library.

That said, let’s look at how we can tackle those issues in the repository we talked about in [Part 2](https://blog.nviso.eu/2025/07/17/detection-engineering-practicing-detection-as-code-repository-part-2/).

## Detection Wiki

To automatically generate wiki pages documenting our detections, we can convert the YAML metadata files into Markdown format. YAML is already easily readable but when communicating our work with other teams we should use a more user friendly format. Markdown is also the supported format for Azure DevOps wiki pages [1]. To perform the conversion we are going to utilize a Jinja [2], which is a templating engine with special placeholders in the template that allow writing code similar to Python. Data is then passed to the template to render the final document.

The Jinja template that we are going to use to convert the meta files to markdown is the following:

```
# {{ data.name }}

**ID:** {{ data.id }}

**Level:** {{ data.level }}

**Version:** {{ data.version }}

## Description
{{ data.description }}

## Data Sources
{% for data_source in data.data_sources %}
### {{ data_source.vendor }} {{ data_source.product }} {{ data_source.service }}
- **Category:** {{ data_source.category }}
- **Vendor:** {{ data_source.vendor }}
- **Product:** {{ data_source.product }}
- **Service:** {{ data_source.service }}
- **Event ID:** {{ data_source.event_id }}
{% endfor %}

## References
{% for ref in data.references %}
- {{ ref }}
{% endfor %}

## Blindspots
{% for blindspot in data.blindspots %}
- {{ blindspot }}
{% endfor %}

## Known False Positives
{% for fp in data.known_false_positives %}
- {{ fp }}
{% endfor %}

## Investigation Steps
{% for step in data.investigation_steps %}
- {{ step }}
{% endfor %}

## Tags
{% for tag in data.tags %}
- {{ tag }}
{% endfor %}
```

```
# {{ data.name }}

**ID:** {{ data.id }}

**Level:** {{ data.level }}

**Version:** {{ data.version }}

## Description
{{ data.description }}

## Data Sources
{% for data_source in data.data_sources %}
### {{ data_source.vendor }} {{ data_source.product }} {{ data_source.service }}
- **Category:** {{ data_source.category }}
- **Vendor:** {{ data_source.vendor }}
- **Product:** {{ data_source.product }}
- **Service:** {{ data_source.service }}
- **Event ID:** {{ data_source.event_id }}
{% endfor %}

## References
{% for ref in data.references %}
- {{ ref }}
{% endfor %}

## Blindspots
{% for blindspot in data.blindspots %}
- {{ blindspot }}
{% endfor %}

## Known False Positives
{% for fp in data.known_false_positives %}
- {{ fp }}
{% endfor %}

## Investigation Steps
{% for step in data.investigation_steps %}
- {{ step }}
{% endfor %}

## Tags
{% for tag in data.tags %}
- {{ tag }}
{% endfor %}
```

Markdown

We will also convert each platform that we support to markdown format. As an example we will provide the Jinja template for Sentinel rules.

```
# {{ data.properties.displayName }}

**ID:** {{ data.id }}

**Severity:** {{ data.properties.severity }}

**Kind**: {{ data.kind }}

**Enabled**: {{ data.properties.enabled }}

**Query:**
```
{{data.properties.query}}
```

### General Configuration
- **Query Frequency**: {{ data.properties.queryFrequency }}
- **Query Period**: {{ data.properties.queryPeriod }}
- **Trigger Operator**: {{ data.properties.triggerOperator }}
- **Trigger Threshold**: {{ data.properties.triggerThreshold }}
- **Suppression Enabled**: {{ data.properties.suppressionEnabled }}
- **Suppression Duration**: {{ data.properties.suppressionDuration }}
- **Event Grouping Settings Aggregation Kind**: {{ data.properties.eventGroupingSettings.aggregationKind }}

### Incident Configuration
- **Create Incident**: {{ data.properties.incidentConfiguration.createIncident }}
- **Grouping Enabled**: {{ data.properties.incidentConfiguration.groupingConfiguration.enabled }}
- **Reopen Closed Incident**: {{ data.properties.incidentConfiguration.groupingConfiguration.reopenClosedIncident }}
- **Lookback Duration**: {{ data.properties.incidentConfiguration.groupingConfiguration.lookbackDuration }}
- **Matching Method**: {{ data.properties.incidentConfiguration.groupingConfiguration.matchingMethod }}

**Group By Entities**:
{% if data.properties.incidentConfiguration.groupingConfiguration.groupByEntities %}
{% for item in data.properties.incidentConfiguration.groupingConfiguration.groupByEntities %}
- {{ item }}
{% endfor %}
{% else %}
- _None_
{% endif %}

**Group By Alert Details**:
{% if data.properties.incidentConfiguration.groupingConfiguration.groupByAlertDetails %}
{% for item in data.properties.incidentConfiguration.groupingConfiguration.groupByAlertDetails %}
- {{ item }}
{% endfor %}
{% else %}
- _None_
{% endif %}

**Group By Custom Details**:
{% if data.properties.incidentConfiguration.groupingConfiguration.groupByCustomDetails %}
{% for item in data.properties.incidentConfiguration.groupingConfiguration.groupByCustomDetails %}
- {{ item }}
{% endfor %}
{% else %}
- _None_...