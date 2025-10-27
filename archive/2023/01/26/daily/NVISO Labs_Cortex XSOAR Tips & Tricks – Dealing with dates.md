---
title: Cortex XSOAR Tips & Tricks – Dealing with dates
url: https://blog.nviso.eu/2023/01/25/cortex-xsoar-tips-tricks-dealing-with-dates/
source: NVISO Labs
date: 2023-01-26
fetch_date: 2025-10-04T04:52:03.991972
---

# Cortex XSOAR Tips & Tricks – Dealing with dates

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

# Cortex XSOAR Tips & Tricks – Dealing with dates

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[SOC](https://blog.nviso.eu/category/soc/)

January 25, 2023March 12, 2024
7 Minutes

## Introduction

As an automation platform, Cortex XSOAR fetches data that represents events set at defined moments in time. That metadata is stored within Incidents, will be queried from various systems, and may undergo conversions as it is moves from machines to humans. With its various integrations, Cortex XSOAR ingests datetimes from sources that use different standards, yet manages to keep track of all of them.

### Objectives

In this blog post, we will go over dates in Cortex XSOAR, showing where they are presented and used, as well as how they are stored and passed around.
We will present a real world use case for extracting the dates being passed to the elements of a dashboard. With that in mind, we will go deeper onto the technicalities of passing timeframes to widgets and present an object oriented approach to interpreting and converting those, ensuring that this becomes an easy process, even when using third party tools.
The codebase for this post is available on the [NVISO Github Repository](https://github.com/NVISOsecurity/blogposts/blob/master/CortexXSOAR/nitro_date_utils.py).

## Dates in XSOAR

Let’s look at the use of dates in Cortex XSOAR throughout the GUI and let’s pay attention to the formats we encounter:
Within incident layout tabs, incident fields of type “date” are formatted in a human readable way.

![](https://blog.nviso.eu/wp-content/uploads/2022/04/01IncidentOverview.jpg)

Occurence, Creation, and Last update dates in the Timeline Information GUI widget of an XSOAR Incident.

However in the raw context of an Incident, we see the same dates but stored in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:

![](https://blog.nviso.eu/wp-content/uploads/2022/04/02aIncidentContextData.jpg)

Multiple datetime fields in the Context GUI of an XSOAR Incident

The dates we can observe in the raw context are formatted to be machine readable, this is what Integrations, Automations, and Playbooks read.

The dates visible in the layout tab are rendered live from those in the context. Cortex XSOAR adapts this view depending on the preferred timezone of the current user, which is saved in it’s user profile. This explains the 1 hour difference between the raw dates and their human readable counterparts in our examples above.

Moving on to the dashboards page, we get a time picker to selectively view Incident and Indicator data restricted to a given period of time. In the next part, we will find out how this time frame is passed down to the underlying code generating the tables and graphs that make up the dashboard. For that purpose, we will build a new dashboard comprised of a single automation based Widget.

![](https://blog.nviso.eu/wp-content/uploads/2022/04/02bDashboardViewLast7Days.jpeg)

Date Range Selector of a XSOAR Dashboard, set to display information from the “Last 7 Days”

## The dashboard date picker

We just saw that Dashboards introduce a date picker element, it lets you select both relative timeframes such as “Last 7 days” and explicit timeframes where you define two precise dates in time. To find out how this is effectively passed down, we will use an automation based widget and dump the parameters provided to this automation.

If you need help on creating an automation, please refer to the [XSOAR documentation on automations](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/automations).

Let’s create an automation with the following code, not forgetting to add a ‘`widget`‘ tag to it.

```
import json
demisto.results(json.dumps(demisto.args()))
```

The snippet above will print the arguments passed down to the automation.

To run our automation and get it’s output, we need to create a new dashboard and add a text element to it, it’s content will be populated by our automation. For help on creating a dashboard and automation based widgets, please refer to [XSOAR – add a widget to a dashboard](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/dashboards/add-a-widget-to-a-dashboard) and [XSOAR – creating a widget automation](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/incidents/incident-management/war-room-overview/add-a-custom-widget-in-the-war-room).

We start our reversing effort by using the dashboard with an explicit timeframe:

![](https://blog.nviso.eu/wp-content/uploads/2022/05/16DashboardViewDefinedDates-2.png)

Dashboard outpout with the date range “19 Apr 2022 – 22 Apr 2022”

At first glance, we identify the two arguments that interest us, “to” and “from”, each containing an ISO 8601 string corresponding respectively to the lower and higher bounds of our selected timeframe.

When we use relative dates, we get still get ISO 8601 strings, However, the “to” argument now holds a default value pointing to January first of year 1.

![](https://blog.nviso.eu/wp-content/uploads/2022/05/14DashboardViewLast6MonthsZomed.jpeg)

Dashboard outpout with the date range “Last 6 months”

Finally, when we use the ‘All dates’ date picker, we get two of these arbitrary strings.

![](https://blog.nviso.eu/wp-content/uploads/2022/05/15DashboardViewLastAllTimesZomed.jpeg)

Dashboard outpout with the date range “All times”

The findings above can be understood as being a standard on passing dates and time frames, and we can assume that all builtin Cortex XSOAR content can handle it. However, this may not be the case for third party tools. To interface with the latter, and to create our own dashboard compatible content, we need a way to interpret these dashboard parameters.

## Objectives redefinition

We have now identified how the dates that define the beginning and the end of a daterange are passed to the elements of a dashboard, after a user selects that date range in the web interface. This opens new capabilities, as we are now not bound anymore to dashboard elements builtin to Cortex XSOAR, but can start to imagine querying period relevant data in third party systems to visualize in our dashboard.

In a future post, we will use our findings to query Microsoft Sentinel for some Incident data, and display the results of that search in dashboard...