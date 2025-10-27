---
title: How Anomaly Detection Advances Cloud Threat Hunting - Uptycs
url: https://buaq.net/go-161878.html
source: unSafe.sh - 不安全
date: 2023-05-06
fetch_date: 2025-10-04T11:38:37.906670
---

# How Anomaly Detection Advances Cloud Threat Hunting - Uptycs

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2a5c3b0ef06c9289752f3f112fd09754.jpg)

How Anomaly Detection Advances Cloud Threat Hunting - Uptycs

I’ve done a lot of research on threat hunting and detection for most of my life
*2023-5-5 20:0:0
Author: [www.uptycs.com(查看原文)](/jump-161878.htm)
阅读量:26
收藏*

---

I’ve done a lot of research on threat hunting and detection for most of my life. Over the past 6-7 years I have spent a lot of time on cloud threat hunting and detection, which is interesting, because it is a different beast due to cloud infrastructure complexity and the extensive use of API services.

Very often in this landscape, people bring their existing security tools, technologies, standards, and practices to the cloud and expect to do security the same way they did in the on-premise world. It's not that you can't do that, or that it doesn't have value. It does have some value because there are virtual networks to monitor, and we can put EDR agents, endpoint agents, or instrumentation on virtual machines and servers. But there are other worlds to consider, where traditional tools simply are not revealing.

The vast majority of cloud environments consist of services that can’t be monitored with a firewall, an intrusion detection system (IDS), or any kind of host-based or endpoint instrumentation. It takes a totally different approach to look for and detect threats in the cloud. That’s why Uptycs incorporates anomaly detection into our threat hunting and detection capabilities.

[Click here](https://www.uptycs.com/resources/webinars/uptycs-live-anomaly-detection) to see Uptycs anomaly detections in action, as I walk through the use cases discussed in this article and demonstrate detections right from the Uptycs platform.

## What is Anomaly Detection?

Let me start with a basic definition of what I mean by “anomaly detection.” In practical terms, anomaly detection usually means looking for some kind of behavior, transaction, or a combination of factors, observables, or field values that represents an outlier. That is, what is observed is extremely rare, extremely dense, or possibly new because it hasn’t manifested before.

In some cases, really large spikes in certain kinds of event data streams—like errors, and really large spikes in data volumes to/from particular kinds of destinations—can be interesting. Some anomaly detection aspects are about things that 1) are statistically sparse or dense, and 2) are at the extreme opposite ends of that spectrum. And sometimes we're looking for things that are new that we simply haven't seen before.

Anomaly detection is good at discovering items of potential concern within the haystack that initially appear too similar to normal, innocent activity. It's also good at finding the next emerging threat where we don't yet know what it is or what it looks like. That is, we need to be able to find and see what's coming.

Though I’m a big advocate of the latter, I’m not saying you should get rid of existing threat detection technologies and only use anomaly detection. No single detection technology uncovers every kind and class of threat. You get much better results and much better efficacy when you use different kinds of detection technologies and tools in concert with each other, in ways that are complementary.

### Case Study – How Anomaly Detection Could Have Identified Unusual Cloud Activity

There are a few public record case studies of data breaches that contain elements relevant to anomaly detection. [One event](https://www.justice.gov/file/1080281/download) occurred in the political sector in 2016 (see pg. 13, § 34). Here, an attacker obtained cloud user credentials, authenticated as that person, then shared snapshots to exfiltrate data. The attacker wasn’t copying data around a network or anything like that. They were just sharing snapshots with their account as a method of large-scale data exfiltration in order to forklift data from the victim account to the attacker's account. It was a case of credentialed access in large-scale exfiltration.

There's nothing inherently unusual or malicious about sharing snapshots. That's true of most cloud actions because most organizations have many accounts where such activity is completely normal. On any given day, there might be up to 13,000 other actions to consider being performed by hundreds or thousands of users. That makes it really hard to try to find those few suspicious events among millions or possibly billions of normal actions. That's quite the formidable haystack.

### Case Study – Correlating Activities to Spot an Employee’s Rogue Behavior

Another interesting [case study](https://www.docketalarm.com/cases/Washington_Western_District_Court/2--19-cr-00159/USA_v._Thompson/1/) is where an employee had legitimate cloud service access but started using their access to do illegitimate things, as alleged in the public record indictment. Their suspicious activity began at 3:00 AM.

You might ask, "Can I just look for people logging in at that time and assume it’s malicious activity?" If everyone is a 9–5 knowledge worker, that might have good efficacy. But in large distributed systems (cloud or otherwise), there are SREs, there are people that are doing break/fix, and they're logging in that early because they're on pager duty and something is broken. There is a good amount of just normal people logging in to debug and fix things, sometimes in the middle of the night, sometimes at odd hours to negate alerting on a single data point (i.e., odd activity time) likely isn’t a viable detection. Moreover, people roam in the post-COVID era and log in from various time zones.

Geolocation traceability – Another data point that differed in this second case study was how the user logged in via a VPN—possibly to obfuscate their location and identity. The presence of that particular VPN in the log data was likely new, whereby that provider didn’t normally appear in the system logs. (Some VPNs are located in geographies that don't make sense in relation to a company’s business; they’re fertile ground for the appearance of anomalies.)

Uptycs enriches CloudTrail events with the name of the source, city, region, and country, as well as the latitude-longitude coordinates so we can plot it on a map. This enables analysts to reason about which geographies users are logging in from and what kinds of activity correspond with those geolocations.

Something else of note is that the user modified some retention policies on specific logs. Presumably, their rationale was to create short log retention; by the time anybody looked at the affected log the next day or a few days later, there might not exist any evidence in the log to use for an investigation.

Log retention, log truncation, log destruction and deactivation are common. In a cloud environment, modifying lifecycle retention policies for logging is not abnormal by itself. Applications, systems, and worlds get spun up and torn down; logging and associated services get turned on and off. Since much of this is done by automation or by a small number of users. So, working in this particular service, modifying and truncating of the logs was likely anomalous for the user in question.

Better anomaly detection results are often achieved from using a combination of fields and observables. For example, don’t just look for rare values in a single field, but rather rare combinations of, say, user and service—such as a user working in a service they don't normally use. (It could be that somebody started a new project, but it could otherwise be due to unauthorized credentialed access—their account ...