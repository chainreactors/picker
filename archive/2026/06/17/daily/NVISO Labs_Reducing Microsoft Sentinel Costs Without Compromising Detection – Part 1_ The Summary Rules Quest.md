---
title: Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 1: The Summary Rules Quest
url: https://blog.nviso.eu/2026/06/17/reducing-microsoft-sentinel-costs-without-compromising-detection-part-1-the-summary-rules-quest/
source: NVISO Labs
date: 2026-06-17
fetch_date: 2026-06-18T06:50:09.123550
---

# Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 1: The Summary Rules Quest

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
    - [AI Security](https://blog.nviso.eu/category/ai-security/)
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

# Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 1: The Summary Rules Quest

[Christos Giampoulakis](https://blog.nviso.eu/author/christos-giampoulakis/)

[Kusto Query Language](https://blog.nviso.eu/category/kusto-kql/), [NVISO](https://blog.nviso.eu/category/nviso/), [SIEM](https://blog.nviso.eu/category/siem/), [Logging](https://blog.nviso.eu/category/logging/), [SOC](https://blog.nviso.eu/category/soc/), [Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Cybersecurity](https://blog.nviso.eu/category/cybersecurity/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Sentinel](https://blog.nviso.eu/category/prevent/cloud-security/sentinel/)

June 17, 2026June 17, 2026
10 Minutes

This entry is part 1 in the series [Reducing Microsoft Sentinel Costs Without Compromising Detection](https://blog.nviso.eu/series/reducing-microsoft-sentinel-costs-without-compromising-detection/ "Reducing Microsoft Sentinel Costs Without Compromising Detection")

---

By

[Christos Giampoulakis](https://blog.nviso.eu/author/christos-giampoulakis/) , [Theodoros Polyzos](https://blog.nviso.eu/author/theodoros-polyzos/) , [Dimitrios Patounis](https://blog.nviso.eu/author/dimitrios-patounis/)

June 17, 2026

Storage cost has always been a hot topic when log management discussion are on the table. In today’s enterprise ecosystems, organizations commonly ingest very high volumes of logs into their SIEM platforms from a wide range of sources, including servers, network devices, cloud environments, security tools, identity systems, and, in some cases, endpoint telemetry.

To fit each enterprise’s needs, [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/) [1] offers different log storage tiers. Lower-cost storage tiers, such as Auxiliary, provide clear cost benefits, but they are not designed for frequent data access in the same way as the Analytics tier. The Analytics tier is the high-performance optimized default tier but comes with high cost. Basic Logs is the low-cost limited-analysis tier, and Data Lake is the cheaper long-term cold-storage tier with slower performance .In this blog series, we will explore how Summary Rules, together with the Auxiliary or Data Lake tier, can help you reduce costs while still maintaining effective threat detection and monitoring capabilities.

## What are Summary Rules?

[Summary Rules](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/summary-rules?tabs=api#how-summary-rules-work) [2] are scheduled KQL queries that aggregate log data and send the results to a custom log table in your Log Analytics workspace. This gives us the power to store large volumes of data in more cost-efficient tiers while retaining only the most relevant information for investigation purposes and even leveraging it within analytic rules (which will be discussed later).

The main benefits of using Summary Rules are:

* ***Optimized performance***: Because the data is pre-aggregated according to the Summary Rule query, investigations can be conducted more efficiently and with greater focus on the summarized events. In addition, executing analytic rules or functions against this dataset is significantly faster than querying through very large volumes of log data.
* ***Cost Savings***: Using Summary Rules to store aggregated information in analytic tables in combination with ingesting all initial data into lower-cost storage tiers, such as Auxiliary or Data Lake, is an effective strategy for significantly reducing overall SIEM costs.

The screenshots below show an example comparison of Summary Rule input and output based on a sample aggregation query. In this example, the input consists of 545 firewall events ingested into a Data Lake table. When Summary Rule runs, it applies an aggregate query based on SourceIP and combines all DestinationIPs and ThreatDescription values into a single event.

![](https://blog.nviso.eu/wp-content/uploads/2026/06/image-2-1024x302.png)

Sample input events ingested in 15 minutes

![](https://blog.nviso.eu/wp-content/uploads/2026/06/image-3-1024x263.png)

Sample Summary Rule Output based on dummy SourceIP aggregation

## Data Tiers Comparison

To better understand how we can leverage the different storage capabilities offered by Microsoft we will go through he 3 data tiers available. The data tiers available are: **Analytics**, **Basic,** and **Auxiliary/Data Lake**. While all three are available for Microsoft Sentinel, Microsoft Defender table tier only supports Analytics and Auxiliary/Data Lake.

The *Analytics* tier is the standard “hot” tier for high-performance querying and indexing. It provides full query capabilities in Microsoft Defender and Azure portals, optimized query performance, archived log restore, and the complete set of real-time analytics features. Default retention is 30 days in Microsoft Sentinel and 30 days in Microsoft Defender XDR, with an option to extend for up to two years at an adjusted monthly long-term retention rate.

The *Basic Logs* tier is a cost-optimized tier designed for high-volume data that does not require frequent or advanced analysis. This tier enables the ingestion and retention of large volumes of telemetry at a significantly lower cost than the Analytics tier. It provides 30-day retention with optional extension up to 12 years. However, this cost efficiency comes with trade-offs; query capabilities are more limited, advanced KQL features and cross-table operations are restricted, and support for rich analytics and alerting scenarios is reduced. As a result, Basic Logs are best suited for troubleshooting, auditing, and occasional investigations rather than continuous monitoring.

The *Data Lake* tier provides cost-effective long-term retention for large data volumes (cold storage). Querying is supported but not optimized, so performance is generally slower, especially for larger time ranges or high log volumes. Additionally, each query incurs a small execution cost. It offers full ...