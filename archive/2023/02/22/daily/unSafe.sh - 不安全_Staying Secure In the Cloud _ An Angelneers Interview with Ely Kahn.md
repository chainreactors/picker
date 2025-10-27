---
title: Staying Secure In the Cloud | An Angelneers Interview with Ely Kahn
url: https://buaq.net/go-150389.html
source: unSafe.sh - 不安全
date: 2023-02-22
fetch_date: 2025-10-04T07:41:06.306734
---

# Staying Secure In the Cloud | An Angelneers Interview with Ely Kahn

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

![](https://8aqnet.cdn.bcebos.com/70c02f60ceca6cd81112f6e928882cd1.jpg)

Staying Secure In the Cloud | An Angelneers Interview with Ely Kahn

Cloud computing has allowed modern organizations to scale at incredible rates, transforming how org
*2023-2-21 21:1:55
Author: [www.sentinelone.com(查看原文)](/jump-150389.htm)
阅读量:29
收藏*

---

Cloud computing has allowed modern organizations to scale at incredible rates, transforming how organizations collaborate and operate. While cloud adoption grows across all industries, its inherent risks have expanded alongside it. This steers security leaders towards implementing the right cybersecurity strategies to protect their cloud environments.

In the latest [Angelneers podcast](https://www.angelneers.com/podcast/79-staying-secure-in-the-cloud/) episode, host [Oleg Sullivan Koujikov](https://www.linkedin.com/in/oleg-koujikov-43703338/) spoke with SentinelOne’s VP, Product Management for Cloud Security, [Ely Kahn](https://www.linkedin.com/in/elykahn/), about the realities of using cloud computing, the three main cloud-based attack vectors, and the rise of cloud native application protection platforms (CNAPPs) in combating threat actors who continue to take aim at this fast-growing attack surface. In this post, we share Ely’s main take aways for staying secure in the cloud.

![](https://www.sentinelone.com/wp-content/uploads/2023/02/Staying-Secure-In-the-Cloud-1.jpg)

## Growing Threats Organizations Face in the Cloud

**Koujikov:** Today, in 2023, many business organizations have completely migrated computing resources to the cloud and other companies are still working to migrate over to the cloud. It seems we are trending in this direction and threats are also growing in cloud computing. Can you talk about some of the cloud security issues and threats organizations face as this larger trend towards cloud computing is adopted?

**Kahn:** The first thing to remember with cloud security is what people use the cloud for. Organizations are using the cloud to host web applications and store their data. Oftentimes, this is time-sensitive data or business-critical web applications that are generating tens, if not hundreds of millions of dollars of revenue.

This in mind, the real goal of cloud security is to defend those applications and the underlying infrastructure that they sit on in the cloud. Given that there are these applications in cloud processing, sensitive data like personal health information, personally identifiable information (PII), or credit card information, attract adversaries who want to either steal that information, resell it on the dark web, or use it to conduct a ransomware attack. Adversaries then extract money from a victim company who are trying to unbrick their application that has been encrypted due to that ransomware incident.

## 3 Common Cloud-Based Attack Vectors

**Kahn:** Adversaries or threat actors are conducting these attacks using one of three ways as their initial access. The following are stack ranked in relative frequency.

### 1. Misconfigured Resources

Number one on the list is misconfigured resources and, specifically, cloud resources that are made publicly accessible to the internet. For example, if I am using an S3 bucket, Elasticsearch cluster, or another type of cloud database and I accidentally misconfigure it so that it is publicly accessible from the internet when it shouldn’t be, I will be breached within minutes.

There are adversaries continuously scanning the internet and AWS IP ranges for any type of resource that is exposed to the internet. Suppose that resource contains sensitive data or connections to other resources through overly permissive identity roles or permissions. This is a classic way in which organizations experience cloud breaches.

### 2. Compromised Access Keys

With cloud providers, there’s the concept of access keys. On one hand, think username and password-type access keys and, on the other, there are ephemeral access keys. Ephemeral access keys are always the recommended way for setting up your access through identity access management (IAM) roles instead of IAM users. Roles have ephemeral access keys; users have long-lasting access keys.

The long-lasting access keys can get compromised in a number of ways. They can get stolen, people can hard code them and then find that the code repos are made public. Essentially, finding access keys and then using them to access cloud accounts is the second most common cloud-based risk organizations face.

### 3. Vulnerable Web Applications

As mentioned before, people are using cloud computing to host web applications from cloud providers. Those web applications could have exploitable vulnerabilities associated with them. For example, a company may be using a version of WordPress that has a badge or corrupted plug-in that can be exploited, or a form on their application is subject to SQL injection.

There are several ways to protect applications from these types of vulnerabilities. You can scan the application vulnerabilities, or put a web application firewall in front of them to limit the malicious actions that can be taken against them. However, once a threat actor has gotten in through that front door, they are able to move laterally and conduct various types of cloud attacks.

**Koujikov:** To summarize these three main cloud-based attack vectors, we can say it’s like one: you left open a door, two: someone got a key, or three: they went right through the front door.

**Kahn:** Exactly, and maybe broke a window in the process!

## Understanding Hybrid & Multi-Cloud Risks

**Koujikov:** Next, can you talk about the growing hybrid cloud approach? It implies that services and applications that can be hosted are configured locally and could be migrated to a cloud. Can you talk about the proliferation of hybrid and multi-cloud security?

**Kahn:** Let me break these down a little bit: What does multi-cloud mean? Multi-cloud means that you’re actually using multiple cloud providers, for example AWS and Azure, for your host workloads. Rarely is the same application being used across multiple cloud providers. More often, organizations are picking one cloud provider for one type of workload and another cloud provider for another type of workload, because you really like their capabilities in a particular area. Back to the example, perhaps an organization is using Azure for its machine learning, but then using AWS for everything else.

With hybrid cloud, this refers to organizations that store some of their data in a public cloud environment while simultaneously running other applications within their own on-prem environment, which could be a private cloud environment. What’s interesting from a security perspective is the idea that security incidents can actually start on-prem and then move into the cloud or vice versa. So, right now, I would say that most security solutions are relatively stovepiped meaning they only focus on cloud security, or they only focus on on-prem security.

Because of that stovepipe-like focus, many security solutions potentially miss these pivots between on-prem and cloud environments. This limits your ability to really, truly understand the full scope of an attack or a full scope of incident.

As an example, a user could accidentally enter credentials in a malicious website linked from a phishing email. An adversary would then use those credentials to log into their machine. From there, actors could use [privilege escalation techniques](https://www.sentinelone.com/blog/enterprise-security-essentials-top-15-most-routinely-exploited-vulnerabil...