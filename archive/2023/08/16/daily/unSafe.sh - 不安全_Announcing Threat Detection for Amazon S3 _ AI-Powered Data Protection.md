---
title: Announcing Threat Detection for Amazon S3 | AI-Powered Data Protection
url: https://buaq.net/go-174510.html
source: unSafe.sh - 不安全
date: 2023-08-16
fetch_date: 2025-10-04T11:59:15.117698
---

# Announcing Threat Detection for Amazon S3 | AI-Powered Data Protection

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

![](https://8aqnet.cdn.bcebos.com/da11ea301648f6e2a4cce540223eb65a.jpg)

Announcing Threat Detection for Amazon S3 | AI-Powered Data Protection

SentinelOne recently announced the launch of the new Singularity™ Cloud Data Security product line
*2023-8-15 20:58:21
Author: [www.sentinelone.com(查看原文)](/jump-174510.htm)
阅读量:17
收藏*

---

SentinelOne recently announced the launch of the new [Singularity™ Cloud Data Security](https://www.sentinelone.com/platform/singularity-cloud-data-security/) product line to help customers gain visibility and provide protection for their cloud data, storage, downstream applications, and users from risks associated with unscanned files. [Threat Protection for NetApp](https://www.sentinelone.com/blog/announcing-ai-powered-threat-detection-for-netapp/) provides protection for NetApp arrays, and Threat Detection for Amazon S3, which will be highlighted here, provides protection for S3 buckets. Both services provide powerful, low-latency security for cloud storage in a highly efficient and simple user experience.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/Announcing-Threat-Detection-for-Amazon-S3-AI-Powered-Data-Protection.jpg)

## Why Does Amazon S3 Require Protection?

Amazon S3 is one of the most commonly used AWS services. Due to its flexible, scalable, and available nature, it is possible to store and access nearly any object type from anywhere. With this flexibility, there are a variety of use cases for the service, but in today’s environments, we see Amazon S3 being used more by applications than by humans looking for storage. S3 buckets being used by applications house critical application data for apps themselves but also sensitive data. Uptime and performance are mission critical.

Earlier this year, Amazon S3 [turned 17 years old](https://aws.amazon.com/blogs/aws/celebrate-amazon-s3s-17th-birthday-at-aws-pi-day-2023/), and AWS shared that it currently holds more than 280 trillion objects and has an average of over 100 million requests per second. As part of the [shared responsibility model](https://www.sentinelone.com/cybersecurity-101/what-is-the-cloud-shared-responsibility-model-a-comprehensive-guide/), AWS ensures that the infrastructure itself is secure, and even ensures data integrity within S3. However, the security of what is in the bucket and its potential spread to downstream applications or workflows is the responsibility of the customer.

Many Amazon S3 users and security teams think of configuration management as the primary security challenge, and this used to be a bigger issue with buckets with sensitive data accidentally made public. AWS, though, has implemented new measures to encourage proper configuration. To combat this data loss risk,  many organizations use a [Cloud Security Posture Management](https://www.sentinelone.com/blog/evolution-of-cloud-security/) (CSPM) solution to scan for potential misconfigurations, which is an important element of a defense-in-depth strategy. However, CSPM alone is not enough to prevent S3 from being an attack surface.

The sheer volume of data stored in S3, most of it unscanned and accessible to downstream applications and workflows (including user endpoints), poses a security risk to organizations in terms of [malware](https://www.sentinelone.com/cybersecurity-101/what-is-malware-everything-you-need-to-know/), [ransomware](https://www.sentinelone.com/resources/real-time-cwpp-detects-and-remediates-a-cloud-ransomware-incident/), remote access trojans (RATs), supply chain attacks, and more. Without additional protection, an organization’s S3 buckets can become an accidental staging area for malware.

## Threat Detection for Amazon S3

With Threat Detection for Amazon S3, organizations can decrease risk and increase visibility when it comes to the objects in their buckets. Reducing risk is important and so is meeting compliance requirements including data sovereignty. The solution was designed to meet the business, security, and cloud architecture needs of customers, focusing on the following features:

* AI-Driven Threat Detection – Powerful, AI-driven threat detection goes beyond [traditional signature-based approaches](https://www.sentinelone.com/blog/what-is-a-malware-file-signature-and-how-does-it-work/), which are easily evaded, and protects the organization from threats faster.
* Automation, Flexibility, and Scalability – Scan new files added to buckets automatically. Inventory and protect buckets, including new buckets automatically as they are created, based on configurable policy based approaches.
* High Performance, Low Overhead – Easily deploy into cloud-native architectures using CloudFormation Templates with low ongoing overhead and minimal additional compute costs. Files are scanned quickly, keeping applications running smoothly.
* Compliance-Ready – Scanning completed in customer cloud; no sensitive data or files leave the organization’s cloud environment.
* Centralized Management Experience – Delivered in a simple, unified management experience within the SentinelOne console, where customers can also manage the protection of cloud workloads, endpoints, and identity.

Existing solutions in the market have left many customers frustrated due to poor security performance such as a signature-only approach and a lack of visibility into the resources and their protection status. Other challenges include sluggish scanning or unnatural deployment patterns that slow applications down, or require time consuming re-architecture.

## Easy Deployment & Ongoing Security Without Maintenance

### Getting Started

[Threat Detection for Amazon S3](https://assets.sentinelone.com/s3-security/threat-detection-for-amazon-s3-en) is centrally managed in the SentinelOne management console. To get started, onboard an AWS account or organization and create a Stackset to deploy and create an ARN role for SentinelOne to access your cloud environment.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/s3_1.jpg)

The next step is to select the relevant CloudTrail that will be used by SentinelOne to analyze your cloud environment data and provide an inventory of your S3 buckets. Once done, users will receive multiple CloudFormation templates to be deployed, one for each region that the account’s S3 buckets reside in. Once deployed, the admin can then configure the policy to select which buckets will be protected for malware or fully scanned. Admins can also invoke an *ad-hoc* scanning of a bucket.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/s3_2.jpg)

### Scanning and Policy Configuration

In a true “set it and forget it” approach, scanning of S3 buckets is triggered by configuring a cloud policy that will automatically scan every file added to the indicated bucket according to a predefined rule. For example, all buckets tagged as production should be automatically scanned and monitored for new files.

Configuring policy or rules is done in the SentinelOne management console. Policies can filter resources based on any AWS metadata such as tags, regions, “name contains”, OU, org, etc. There are a variety of policy based options available. For example, organizations could choose to apply scanning to new files, and quarantining of all suspected malicious files to all “production” tagged buckets, or to all buckets in a specific region due to compliance requirements. By using a tag-based approach, users save time by automating the policy application vs. applying policies to each bucket by name.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/s3_3.jpg)

A policy-based approach makes it ...