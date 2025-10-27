---
title: SentinelOne Integrates With Amazon Security Lake to Power Cloud Investigations
url: https://buaq.net/go-137953.html
source: unSafe.sh - 不安全
date: 2022-12-01
fetch_date: 2025-10-04T00:09:44.731647
---

# SentinelOne Integrates With Amazon Security Lake to Power Cloud Investigations

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

![](https://8aqnet.cdn.bcebos.com/bb8e3171c9d05a0cf80e4c7f9ef81abe.jpg)

SentinelOne Integrates With Amazon Security Lake to Power Cloud Investigations

SentinelOne is pleased to announce an integration with Amazon Security Lake, a new Amazon Web Servi
*2022-11-30 22:8:58
Author: [www.sentinelone.com(查看原文)](/jump-137953.htm)
阅读量:35
收藏*

---

SentinelOne is pleased to announce an integration with Amazon Security Lake, a new Amazon Web Services (AWS) security service that enables organizations to aggregate, store, normalize, and analyze security logs from integrated cloud and on-premises data sources and their private applications at scale. SentinelOne ingests these logs into the [Singularity™ XDR](https://www.sentinelone.com/lp/evolution-ppc/) Platform for threat hunting, forensics, and to help investigate and establish root cause of security alerts from [Singularity Cloud Workload Security](https://www.sentinelone.com/resources/sentinelone-cloud-workload-security/).

Amazon Security Lake stores and exports logs using the [Open Cybersecurity Schema Framework (OCSF)](https://github.com/ocsf/). With support for the OCSF standard, Amazon Security Lake reduces the complexity and costs for customers to make their security solutions’ data more readily accessible, to address a wide variety of use cases such as threat detection, investigation, and incident response.

As part of this integration, SentinelOne has natively adopted OCSF as our XDR data schema so that customers can natively view and query these security logs in the Singularity XDR Platform without the hassle of data transformation. This integration is available for customers participating in the [Skylight](https://www.sentinelone.com/press/sentinelone-unveils-skylight-to-power-machine-speed-xdr/) beta program, which extends the Singularity XDR Platform to partner data sources.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Sentinelone-Integrates-With-Amazon-Security-Lake-to-Power-Cloud-Investigations-6.jpg)

## What is OCSF?

OCSF is an open-source security data schema co-founded by AWS in cooperation with security software vendors. By creating an open standard, security data from any number of sources is more easily shared and correlated across various security platforms, thereby creating a more comprehensive view of security and improving security outcomes (e.g., reducing [MTTR](https://www.sentinelone.com/blog/mean-time-to-repair-reduce-mttr/)).

Logs and alerts that leverage OCSF use a common set of fields and formats so that users don’t have to parse and normalize them. In so doing, security analysts, incident responders, and threat hunters have a more enriched dataset to streamline their work.

By more readily sharing security data, it is moved from various siloes and consolidated into a security platform where its value can be unlocked. Better data drives better outcomes.

## How SentinelOne Uses OCSF Data

SentinelOne [ingests OCSF data](https://www.sentinelone.com/platform/xdr-ingestion/) from AWS into our Singularity XDR data lake to assist with the investigation of cloud workload security alerts.

This enhanced perspective helps the security analyst more readily understand the root cause of security alerts related to their workloads within AWS, such as those running on Amazon Elastic Cloud Compute (Amazon EC2) instances, Amazon Elastic Container Service (Amazon ECS), and Amazon Elastic Kubernetes Service (Amazon EKS).

For example, by searching AWS CloudTrail logs associated with the EC2 instance that has a cryptomining alert associated with it, you can identify the user that created that instance, and assess if that user is compromised. This detail in turn informs remediation actions, whether manually initiated or automatically taken according to security policy. The customer controls which types of OCSF logs to ingest, choosing one, many, or all sources.

The OCSF logs available for ingestion from Amazon Security Lake to the Singularity XDR data lake are:

* AWS CloudTrail management events
* Amazon Virtual Private Cloud (Amazon VPC) Flow logs
* Route 53 Resolver query logs
* Amazon Secure Storage Service (Amazon S3) data events
* AWS Lambda function execution activity
* and security findings from 8 AWS services via AWS Security Hub.

More data does not mean more noise. In fact, SentinelOne is uniquely positioned to suppress noise and amplify security signals by virtue of our patented [Storyline™ technology](https://www.sentinelone.com/resources/sentinelone-storyline-active-response-startm/). Storyline automatically monitors thousands of concurrent OS-level process threads in cloud workloads, correlating and assembling a visualization of related events in an incident sequence.

Security data is automatically mapped to the [MITRE ATT&CK framework](https://www.sentinelone.com/resources/enhancing-secops-with-mitre/) tactics, techniques, and procedures (TTPs) so that an adversary’s movement across the organization’s hybrid cloud footprint is constantly observed. If any single incident consists of dozens of TTPs, Storyline assembles them all into a single alert. There are no alert storms or alert fatigue. Instead, just real-time forensic details, automatically distilled, are conveniently presented to the SOC to reduce time to investigation. And of course, configurable security policies can be set within the SentinelOne security console to automatically stop incidents in their tracks.

To get started with the integration, first connect with your SentinelOne account team and request access to the [Skylight](https://www.sentinelone.com/press/sentinelone-unveils-skylight-to-power-machine-speed-xdr/) beta program. Then, go to the [Singularity Marketplace](https://www.sentinelone.com/partners/singularity-marketplace/) to set up the integration.

To install the integration, simply set up a cross-account role for SentinelOne to access the account where your Amazon Security Lake logs are stored. SentinelOne then automatically brings those logs into the Singularity XDR Platform, and that’s it. No infrastructure is needed to deploy this integration. From there, Amazon Security Lake continuously notifies SentinelOne when there are new logs to ingest.

## Closing Thoughts

Open standards for security data sharing is a game changer. Customer benefits include reduced dwell time, increased visibility and context, streamlined incident response (i.e., reduced MTTR), and better threat hunting. As with any change of this magnitude, early adopters will create their own differentiating use cases. At SentinelOne, we look forward to working alongside our customers to create ever-increasing value in security data mining.

If you would like to learn more about the Singularity XDR Platform and how we can help transform your security operations across [cloud workloads](https://www.sentinelone.com/surfaces/cloud/), identity, and user endpoints, or would like to learn more about our beta program, [please contact us](https://www.sentinelone.com/contact/).

SentinelOne Singularity XDR

Supercharge. Fortify. Automate. Extend protection with unfettered visibility, proven protection, and unparalleled response. Discover the power of autonomous with Singularity XDR.

文章来源: https://www.sentinelone.com/blog/sentinelone-integrates-with-amazon-security-lake-to-power-cloud-investigations/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)