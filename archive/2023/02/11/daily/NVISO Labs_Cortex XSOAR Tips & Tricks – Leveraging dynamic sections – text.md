---
title: Cortex XSOAR Tips & Tricks – Leveraging dynamic sections – text
url: https://blog.nviso.eu/2023/02/10/cortex-xsoar-tips-tricks-leveraging-dynamic-sections-text/
source: NVISO Labs
date: 2023-02-11
fetch_date: 2025-10-04T06:19:07.107700
---

# Cortex XSOAR Tips & Tricks – Leveraging dynamic sections – text

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

# Cortex XSOAR Tips & Tricks – Leveraging dynamic sections – text

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[SOC](https://blog.nviso.eu/category/soc/)

February 10, 2023March 12, 2024
5 Minutes

This entry is part 11 in the series [Cortex XSOAR Tips & Tricks](https://blog.nviso.eu/series/cortex-xsoar-tips-tricks/ "Cortex XSOAR Tips & Tricks")

---

## Introduction

Cortex XSOAR is a security oriented automation platform, and one of the areas where it stands out is customization.

A recurring problem in a SOC (Security Operation Center) is data availability. As a SOC Analyst, doing a thorough analysis of a security incident requires having access to many pieces of information in order to acquire context on the events you are investigating. In a less mature SOC, this information is at best scattered in many tools, and at worst hardly available. This can be overcome by using multiple data sources to ingest contextual information into your Security Automation and Automated Response platform (SOAR). In turn, this allows you to provide a single pane of glass to the analysts which can then focus on meaningful work, and eliminate data collection from their daily tasks.

## Objectives

In this blogpost, we will focus on the use of dynamic sections to customize layouts in Cortex XSOAR. We will show that they can be used to display raw incident data for debugging purposes without cluttering the main workplace of our analysts.

A dynamic section is a layout element which you can add to a layout tab for either an incident or an indicator.
The fundamental difference between it and most other available layout elements is that it is not bound to displaying incident fields or fields of indicators related to the current incident on display, but instead is purely automation based.
This means that upon being rendered, a dynamic section executes an automation, and it is both the specific format and output of that automation that dictates the style and content that will be rendered.

This is not unlike the behavior of field display scripts, but these will be covered in a later post.

## Real World Example

As part of our operations as an MSSP (Managed Security Services Provider), we are often faced with alert ingestion issues or mishaps.

One way these occur is that an alert will be fetched into Cortex XSOAR but some of it’s important features will not have been picked up by our extraction logic. This could materialize as missing fields in indicators or missing indicators all together. We may for example have received an alert for suspicious actions taken by a user, yet that very user was not added to the incident as an indicator, nor were details about these actions.

![](https://blog.nviso.eu/wp-content/uploads/2023/01/Screenshot-2023-01-23-at-16-48-22-5-Unsanctioned-cloud-app-access-was-blocked-on-one-endpoint-1024x603.png)

Incident Info tab of a Cortex XSOAR incident – the name of the incident points to unsanctioned cloud app usage by a user, but neither information about the user nor about the unsanctioned app was extracted.

This could happen in many different ways, most commonly that the exact data scheme used by the tool that generated the alert has changed. When this happens, the information we want to extract is present in the alert we fetch, it’s just not located where we’re used to find it. In such cases, a manual inspection of the raw data that came in is sufficient to identify where the data we want can be found. However, as shown in the next screenshot, manually inspecting the raw data of an incident is not that user friendly in Cortex XSOAR.

![](https://blog.nviso.eu/wp-content/uploads/2022/11/image.png)

View of the “Context Data” of an Cortex XSOAR incident – the presentation of the available data is unsuitable for manual inspection

To make it easier, we built our own dynamic section, which displays curated data from both the labels and some entries of an incident. The result is as follows:

![](https://blog.nviso.eu/wp-content/uploads/2023/02/002c-Viewing-the-Raw-Event-Digging-Tab-1024x496.png)

In this example, Azure Active Directory identifiers are available and can be leveraged to get the details of the involved user. In a similar manner, the [Cloud Application Id](https://learn.microsoft.com/en-us/azure/sentinel/entities-reference#cloud-application-identifiers) is available.

Our dynamic section is powered by an automation that enumerates the labels of the current incident.

```
ret_labels = {}
incident = demisto.incident()
if not (isinstance(incident, dict) and "labels" in incident.keys()):
	continue
labels = incident["labels"]
if not isinstance(labels, (list, List)):
	continue
for label in labels:
```

Similarly, it also enumerates specifically tagged war room entries.

```
ret_notes = {}
investigation_id = demisto.incident()["id"]
uri = f"investigation/{investigation_id}"
body = {
	"pageSize": 100,
	"categories": [],
	"tags": ["raw_data"],
	"notCategories": [],
	"usersAndOperator": False,
	"tagsAndOperator": False,
}
body = json.dumps(body, indent=4)
args = {"uri": uri, "body": body}
res_cmd = demisto.executeCommand("demisto-api-post", args)
for res in res_cmd:
	if not (isinstance(res, dict) and isinstance(contents := res.get("Contents"), dict)):
		continue
	if not isinstance(response := contents.get("response"), dict):
		continue
	if not isinstance(entries := response.get("entries"), (list, List)):
		continue
	for entry in entries:
```

Once the incident labels are fetched, we extract their contents:

```
for label in labels:
	if not isinstance(label, dict):
		continue
	label_type, label_value = label.get("type"), label.get("value")
	if not (isinstance(label_type, str) and isinstance(label_value, str)):
		continue
	try:
		label_value = json.loads(label_value)
	except Exception:
		pass
	try:
		ret_labels.update({label_type: label_value})
	except Exception:
		pass
```

In a similar fashion, for each returned War Room entry, we extract the name of the parent playbook task and the content of the entry:

```
for entry in entries:
	key = ""
	if not isinstance(entry, dict):
		continue
	if isinstance(entry_id := entry.get("id"), str):
		key += entry_id
	if isinstance(entry_task := entry.get("entryTask"), dict):
		if isinstance(task_name := entry_task.get("taskName"), str):
			key += " - " + task_name
	value = None
	if isinstance(cnt := entry....