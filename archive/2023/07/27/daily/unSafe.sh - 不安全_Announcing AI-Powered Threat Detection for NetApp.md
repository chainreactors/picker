---
title: Announcing AI-Powered Threat Detection for NetApp
url: https://buaq.net/go-172998.html
source: unSafe.sh - 不安全
date: 2023-07-27
fetch_date: 2025-10-04T11:52:54.358357
---

# Announcing AI-Powered Threat Detection for NetApp

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

![](https://8aqnet.cdn.bcebos.com/8d4fe83b448316be48a54059b203510b.jpg)

Announcing AI-Powered Threat Detection for NetApp

SentinelOne is pleased to announce general availability (GA) of Threat Detection for NetApp. Part o
*2023-7-26 21:0:6
Author: [www.sentinelone.com(查看原文)](/jump-172998.htm)
阅读量:22
收藏*

---

SentinelOne is pleased to announce general availability (GA) of Threat Detection for NetApp. Part of the new Singularity™ Cloud Data Security product line, this novel security solution applies SentinelOne’s proprietary AI models to scan files and detect malware stored on NetApp arrays, stopping its spread before it begins. Supported as part of the NetApp Partner Connect Program, Threat Detection for NetApp delivers high-performance inline file scans complete in milliseconds for an optimal, low latency user experience.

This blog post explores the key benefits of this solution and how it improves risk management, reduces recovery costs, and helps businesses meet compliance requirements. It also covers initial steps for setting up Threat Detection for NetApp.

![NetApp for AI-powered threat detection](https://www.sentinelone.com/wp-content/uploads/2023/07/Announcing-AI-Powered-Threat-Detection-for-NetApp-3.jpg)

## Disrupting the Storage Security Market

Considering the volume of vital data hosted in networked storage and the number of users with access from endpoints running various operating systems (OSs) and from every corner of an enterprise, a single malicious file can quickly spread across an organization. Absent a security solution, users could unwittingly access and spread the malware such that it resurfaces repeatedly.

With Threat Detection for NetApp, businesses can minimize these unnecessary recovery costs. In addition, compliance regulations typically require that the organization use a security solution to protect their means of storage. The solution is designed to address customer’s most underserved pain points and focuses on the following key features:

* Uncompromising security. Reliance on signatures renders organizations vulnerable. Therefore, our solution must deliver the best protection available against novel and unknown malware.
* High speed performance. Low latency is key to a good user experience. To this point, NetApp invests heavily in performance optimization for a streamlined customer experience.
* Easy management. Administration must be simple. Deployment and configuration must be done once. Existing SentinelOne customers expressed strong interest in a “familiar feel” to the existing management console.

[![](https://www.sentinelone.com/wp-content/uploads/2023/07/threat_detection_for_netapp.jpg)](https://www.sentinelone.com/blog/announcing-ai-powered-threat-detection-for-netapp/threat_detection_for_netapp/)

Threat Detection for NetApp: AI-Powered Cloud Data Security

NetApp uses a dedicated OS for their filers, [ONTAP](https://www.netapp.com/data-management/ontap-data-management-software/), so traditional endpoint agents are incompatible. This is why storage vendors provide a dedicated [protocol](https://docs.netapp.com/ontap-9/index.jsp?topic=%2Fcom.netapp.doc.dot-cm-acg%2FGUID-8713AE4F-9454-4D04-985D-E4390CA9FCD2.html) for security solutions. Conformance to this protocol increases barriers to market entry, and so legacy solutions have dominated an underserved market for years. Innovation waned, even as threat actors evolved.

Legacy solutions to filer security are insufficient for many reasons:

1. They rely upon AV signatures which are easily evaded.
2. Frequent signature updates are an administrative nightmare.
3. Poor scanning performance negatively impacts user experience when accessing the filer.
4. Legacy solutions often require a separate security management console, further increasing administrative overhead.
5. They often lack features to facilitate management, ease of use, and visibility.

## Setup & Configuration

Threat Detection for NetApp communicates directly with the SentinelOne management console. Unlike alternative endpoint security solutions, SentinelOne allows customers to manage storage security alongside the rest of their user endpoints and cloud workloads and achieve a seamless, intuitive security management experience without the administrative overhead of additional console components. No learning curve is required.

Initial setup of Threat Detection for NetApp assumes familiarity with NetApp network management concepts such as Vscan, logical interface (LIF), and storage virtual machine (SVM). For more details, consult the [NetApp ONTAP documentation](https://docs.netapp.com/us-en/ontap/network-management/index.html) and work closely with a NetApp system administrator.

[![](https://www.sentinelone.com/wp-content/uploads/2023/07/netapp_installation.jpg)](https://www.sentinelone.com/blog/announcing-ai-powered-threat-detection-for-netapp/netapp_installation/)

To get started, an administrator first downloads and runs the latest Threat Detection for NetApp Installer package to the Windows Vscan server having the NetApp ONTAP Connector. Upon running the installer, enter the Site or Group Token when prompted. User credentials must have local admin privileges.

## High Performance, Streamlined Administration

Along with the other solutions within the Singularity Platform, Threat Detection for NetApp combines high performance with intuitive administration. From threats and mitigation actions, to exclusions, blocklists, agent management and more, Singularity users can expect the same trusted capabilities that now support NetApp storage arrays too. To help save time, Threat Detection for NetApp respects existing user block lists or exclusions that are already configured, removing the burden of rebuilding them again.

In addition to existing management features, the solution also provides valuable threat metadata for greater insights and analysis. For example, metadata points to the exact endpoint which copied the malicious file to your storage.  It doesn’t matter if that endpoint is unprotected or outside your organization; if it found its way to NetApp storage, SentinelOne will point to it.

Customers can also configure policies to automate how Threat Detection for NetApp responds to threats. That is, configuring the agent policies for Detect Mode or Protect Mode. In the following example, the agent is configured to respond to both Suspicious and Malicious Threats as categorized by the agent’s onboard AI models in Protect Mode. Upon detecting a threat, the agent will automatically quarantine any suspicious or malicious files. Customers are in complete control of their security policy choices, configuring the automation level that works best for their specific use cases.

[![](https://www.sentinelone.com/wp-content/uploads/2023/07/netapp_protection_policies.jpg)](https://www.sentinelone.com/blog/announcing-ai-powered-threat-detection-for-netapp/netapp_protection_policies/)

Two Protection Mode Policies: Detect and Protect

The below GIF shows the agent in action. A user attempts to upload 3 executable files from a Windows pane on the left to a NetApp volume on the right. For illustrative purposes, the files are simply named benign.exe, malicious.exe, and malicious2.exe. The user copies the 3 files, and drops them simultaneously to the protected volume. Upon refresh of the Windows pane on the right, the only remaining file is benign.exe. Both of the malicious files were automatically quarantined in real time, without any human intervention required to detect or stop the spread.

[![](https://www.sentinelone.com/wp-content/uploads/2023/07/netapp_agent....