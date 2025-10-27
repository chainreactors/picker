---
title: Awareness and guidance related to potential Service Fabric Explorer (SFX) v1 web client risk
url: https://buaq.net/go-131684.html
source: unSafe.sh - 不安全
date: 2022-10-20
fetch_date: 2025-10-03T20:21:05.779585
---

# Awareness and guidance related to potential Service Fabric Explorer (SFX) v1 web client risk

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

![]()

Awareness and guidance related to potential Service Fabric Explorer (SFX) v1 web client risk

SummaryMicrosoft was recently made aware of a Cross-Site Scriptin
*2022-10-19 21:1:0
Author: [msrc-blog.microsoft.com(查看原文)](/jump-131684.htm)
阅读量:16
收藏*

---

## Summary

Microsoft was recently made aware of a Cross-Site Scripting (XSS) vulnerability ([CVE-2022-35829](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35829)), that under limited circumstances, affects older versions of Service Fabric Explorer (SFX). **The current default SFX web client (SFXv2) is not vulnerable to this attack.** However, customers can manually switch from the default web client (SFXv2) to an older vulnerable SFX web client version (SFXv1). The issue requires an attacker to already have code deployment and execution privileges in the Service Fabric cluster and for the target to use the vulnerable web client (SFXv1).

At this time, Microsoft is not aware of any exploitation or abuse of this vulnerability. **To remain secure, we recommend all Service Fabric customers** [**upgrade**](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-upgrade) **to the most recent SFX version and refrain from manually switching to the older, vulnerable SFXv1 web client version.** An upcoming release of SF will remove SFXv1 and the option to switch to it.

We thank Orca Security for informing us of this vulnerability and working with us under [Coordinated Vulnerability Disclosure](https://www.microsoft.com/en-us/msrc/cvd) to help protect our customers.

## Additional References

* Visit the [Security Update Guide](https://msrc.microsoft.com/update-guide/vulnerability) for information on [CVE- 2022-35829](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35829).
* [Azure Service Fabric Product Blog](https://techcommunity.microsoft.com/t5/azure-paas-blog/bg-p/AzurePaaSBlog/label-name/Azure%20Service%20Fabric)
* Instructions for [upgrading](https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-cluster-upgrade) and updating Azure Service Fabric clusters.
* Questions? Open a support case through the Azure Portal at [aka.ms/azsupt](https://ms.portal.azure.com/#view/Microsoft_Azure_Support/HelpAndSupportBlade/~/overview).

文章来源: https://msrc-blog.microsoft.com/2022/10/19/awareness-and-guidance-related-to-potential-service-fabric-explorer-sfx-v1-web-client-risk/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)