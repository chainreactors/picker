---
title: Hunting for Remote Management Tools: Detecting RMMs
url: https://blog.nviso.eu/2024/10/21/hunting-for-remote-management-tools-detecting-rmms/
source: NVISO Labs
date: 2024-10-22
fetch_date: 2025-10-06T18:50:34.430363
---

# Hunting for Remote Management Tools: Detecting RMMs

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

# Hunting for Remote Management Tools: Detecting RMMs

[Stef Collart](https://blog.nviso.eu/author/stef-collart/ "Posts by Stef Collart")

[Blue Team](https://blog.nviso.eu/category/blue-team/)

October 21, 2024November 21, 2024
9 Minutes

In our previous blog post about [RMM](https://blog.nviso.eu/2024/07/18/hunting-for-remote-management-tools/) (Remote Management and Monitoring) tools, we highlighted the prevalence of such tooling in nearly every organization’s environment. In today’s world, where many organizations support remote work, RMM tools are frequently utilized to help provide assistance to end users and to allow IT administrators to perform their tasks from the comfort of their own home or a branch office. As mentioned in the previous blog, most organizations on which we have performed threat hunting engagements use two or more RMM tools, demonstrating that there is not always a clear policy on which software is accepted for internal use, and which software could potentially have been installed for malicious purposes.

Given the wide range of different RMM tools available, performing a threat hunt to identify all different available tools used in the organization brings a couple of challenges. In this blog, we’ll dive a little deeper into how we tackled this challenge and share this knowledge so you can use it to keep your organization safe.

## Difficulties

It might seem like a straightforward task to gather a list of executable names and domains used by RMMs. Unfortunately, when putting theory into practice, we noticed that it wasn’t as straightforward as it might seem. One of the biggest issues we encountered was the duplicate findings per device, as multiple artifacts were identified.

First of all, we want to rely as little as possible on only one of the fields where the keyword might be present. To get a more elaborate overview, we want to additionally search for keywords in filenames, folder paths, process command lines, and domains.

Using multiple fields to search for our RMM keywords increases the likelihood of detecting an RMM at the cost of having duplicate entries. Another factor to take into account when building the query is to keep in mind how the query language works and follow best-practices to keep the execution time low.

## **How to remove duplicates**

The way we solve duplicate entries is through grouping. We did this by defining a recognizable name for each keyword that we search for. Using Bomgar as an example, we have four entries defined for this RMM. Beyondtrust, bomgar-rdp, bomgarcloud and license.bomgar.

A device that has Bomgar installed will have anywhere from 1 to 4 of these entries on their filesystem. If they have all four, that would generate four entries within our hunting results. Not being able to reduce this number to one in an environment with tens of thousands of hosts would return unnecessary entries. In essence, we only want to know if any Bomgar artifacts are on a device or not. If any artifacts are found, we want to know which artifacts and group them together to end up with only one log entry per device.

Hunting for RMMs through SIEM logs requires the usage of its query langauge. For this blog post we will focus on the [Kusto Query Language](https://learn.microsoft.com/en-us/kusto/query/) (KQL), employed in the Microsoft security suite and widely supported by NVISO’s MDR service.

## Diving into the query

We start off the query by creating a [datatable](https://learn.microsoft.com/en-us/kusto/query/datatable-operator) where we define a common name for the tool which matches a keyword. This ensures that regardless of the matched keyword, the identified tool name remains consistent.

```
let RMMs = datatable(Tool: string, Keyword: string) [
//entries removed for example readability
    "Bomgar", "beyondtrust",
    "Bomgar", "bomgar-rdp",
    "Bomgar", "bomgarcloud",
    "Bomgar", "license.bomgar",
//entries removed for example readability
];
```

Kusto

Next up, we make a list of all keywords we want to look for. This is achieved by selecting the “Keyword” field from the above RMMs table and storing these in a new variable named Keywords.

```
let Keywords = RMMs | project Keyword;
```

Kusto

To optimize the execution time, we’re using the “[has\_any](https://learn.microsoft.com/en-us/kusto/query/has-operator)” operator in the next part of the query. It is also the reason why we have multiple values for Bomgar RMM that contain the word “bomgar”. If we would use the “[contains](https://learn.microsoft.com/en-us/kusto/query/contains-operator)” operator, which is a lot slower, we could reduce the keywords “bomgar-rdp”, “bomgarcloud” and “license.bomgar” to just a single “bomgar” keyword. With the “has” operator (and it’s variants), the search happens on [indexed terms](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators#what-is-a-term) (three characters or more), significantly increasing the search speed. A downside of this is that if we would use “bomgar” as a keyword, it would not match on “bomgarcloud” as the characters that form the word “bomgar” are not separated by a non-alphanumeric character. This is just one example of utilizing [best practices](https://learn.microsoft.com/en-us/kusto/query/best-practices) in our queries to minimize search time. It’s especially useful with complex queries covering large amounts of data.
The following step is to define which table we want to use and in which columns we’re looking for the Keyword values from the datatable. More specifically, in the below example we look in the table DeviceEvents for our defined keywords in the columns FileName, FolderPath, ProcessCommandLine and RemoteUrl.

```
DeviceEvents
| where TimeGenerated > ago(30d) and (FileName has_any(Keywords) or FolderPath has_any(Keywords) or ProcessCommandLine has_any(Keywords) or RemoteUrl has_any(Keywords))
```

Kusto

The last part of the query, before we start grouping the findings, combines each event with all possible RMMs (indicator and tool), after which we filter for any event matching the indicator, effectively attributing the event to one or more RMM tools. This is done as an optimization to ensure we only map keywords to tools on events which contain keywords.

```
| extend _=true
| lookup (RMMs | extend _=true) on _
| where FileName has Keyword or FolderPath has Keyword or ProcessCom...