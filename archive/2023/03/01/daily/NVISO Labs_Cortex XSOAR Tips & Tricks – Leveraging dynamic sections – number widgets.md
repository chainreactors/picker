---
title: Cortex XSOAR Tips & Tricks – Leveraging dynamic sections – number widgets
url: https://blog.nviso.eu/2023/02/28/cortex-xsoar-tips-tricks-leveraging-dynamic-sections-number-widgets/
source: NVISO Labs
date: 2023-03-01
fetch_date: 2025-10-04T08:19:16.397783
---

# Cortex XSOAR Tips & Tricks – Leveraging dynamic sections – number widgets

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

# Cortex XSOAR Tips & Tricks – Leveraging dynamic sections – number widgets

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Data Visualisation](https://blog.nviso.eu/category/data-visualisation/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [MDR](https://blog.nviso.eu/category/mdr/)

February 28, 2023March 12, 2024
9 Minutes

## Introduction

Cortex XSOAR is a security oriented automation platform, and one of the areas where it stands out is customization.

A recurring problem in a SOC is data visualization, analysts can be swarmed with information, and finding out what piece of data is currently both relevant and significant can become hard. One of our tasks as SOAR engineers is to ease the decision process for analysts, we do so by providing additional contextual information about the incidents they handle, directly within the incident layout. In this objective, we incorporate number widgets into the analyst interface, these allow us to tell more visual stories about the security incidents we manage in XSOAR. From raw and sometimes unorganized data, they let us bring up eye-catching depictions of elements that can help in assessing the impact and veracity of a detection.

## Objectives

In this blogpost, we will focus on the use of number widgets.

We will show you how to make use of them for outputting information to the war room, incidents, indicators and dasbhoards. On top of that we will also cover how to add trends information and even how to integrate them into a dashboard with a dynamic query. In the [previous post in the series](https://blog.nviso.eu/2023/02/10/cortex-xsoar-tips-tricks-leveraging-dynamic-sections-text/), we looked at dynamic sections in Cortex XSOAR and how to leverage them to display text in a tree like way. If you are not familiar with Cortex XSOAR and dynamic sections, please read the [previous post in the series](https://blog.nviso.eu/2023/02/10/cortex-xsoar-tips-tricks-leveraging-dynamic-sections-text/).

We previously saw that we could use dynamic dections to display text, but there are a few other options available to us. These options are broken down [here](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-9/cortex-xsoar-admin/incidents/customize-incident-view-layouts/examples-of-script-based-widgets-for-incident-layouts). In this post, we will:

* Start with a **simple example** that runs a static query against Microsoft Sentinel and lets us display a single number widget.
* Continue with **extracting a second number** from our query to populate the trend of the number we display.
* Bring our widget to a **dashboard**
* Make our dashboard widget **read the date range** selected by the user and modify the Sentinel query accordingly.

Let’s begin with a new automation and follow the instructions available in the number widget example of the [PaloAlto documentation](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-9/cortex-xsoar-admin/incidents/customize-incident-view-layouts/examples-of-script-based-widgets-for-incident-layouts#id84e80158-eab8-4bb2-ad17-ab3e295da3e4_id5a5fd7cf-af75-43ad-8487-734987c52eb6). When we run their example, we get the following result:

![](https://blog.nviso.eu/wp-content/uploads/2022/11/0-1024x530.png)

Figure 1: War Room output of the code example available in the Cortext XSOAR documentation

As expected, the example works out of the box. Let’s now go and make the widget display data from Microsoft Sentinel.

## A static number from sentinel

To display data pulled from Microsoft Sentinel ([Microsoft Azure’s cloud native SIEM](https://azure.microsoft.com/en-us/products/microsoft-sentinel/#overview)), we first need to call an integration command. Here we use an instance of the Azure Log Analytics integration [available in the Cortex XSOAR marketplace](https://xsoar.pan.dev/docs/reference/integrations/azure-log-analytics):

```
res = demisto.executeCommand(
	"azure-log-analytics-execute-query", {
		"query": THE_QUERY
	}
)
```

We need a query to run, we will develop it on Sentinel before using it from Cortex XSOAR.

We will be looking at entries in `SecurityIncident`, a table that holds information about the security incidents present in your Sentinel deployment. We will query that table, and count the number of distinct incidents in a given month. The query we will use for that is the following:

```
SecurityIncident
| where TimeGenerated between (
    datetime("2022-10-01T00:00:00+00:00")
    ..
    datetime("2022-11-01T00:00:00+00:00"))
| summarize count()
```

![](https://blog.nviso.eu/wp-content/uploads/2022/12/097-sentinel_query_results-1024x651.png)

Figure 2: Screenshot of a Microsoft Sentinel query and it’s results: single value

Now that we know our query works, we will port it to Cortex XSOAR. We start by duplicating our previous automation and adding code to call the integration with the Sentinel query.

```
res = demisto.executeCommand("azure-log-analytics-execute-query", {
"query": """SecurityIncident
| where TimeGenerated between(
	datetime("2022-10-01T00:00:00+00:00")
	..
	datetime("2022-11-01T00:00:00+00:00"))
| summarize count()"""
})
```

We need to extract the `count_` we could observe in the results of Sentinel, let’s inspect the `res` object returned to us by the integration.

![](https://blog.nviso.eu/wp-content/uploads/2022/12/002-sentinel_query_results_in_xsoar.png)

Figure 3: Debug view in PyCharm

Upon inspection of the returned object, we identify that we can use the following logic to extract the count of incidents

```
counts = []

for result in results:
    if not (
        isinstance(result, dict)
        and
        isinstance(contents := result.get("Contents"), list)
    ):
        continue
    for content in contents:
        if (
            isinstance(content, dict)
            and
            isinstance(count := content.get("count_"), int)
        ):
            counts.append(count)

total_count = sum(counts)
```

With the `total_count` obtained, we can simply change the hardcoded number from our previous widget and replace it with the value we just fetched:

```
demisto.results(
    {
        "Type": 17,
        "ContentsFormat": "number",
        "Contents": {
            "stats": total_count,
            "params": {
                "name": "Incidents Last Month",
                "colors": {
                    "items": {
 ...