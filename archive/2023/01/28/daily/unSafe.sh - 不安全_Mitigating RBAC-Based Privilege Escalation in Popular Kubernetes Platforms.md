---
title: Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms
url: https://buaq.net/go-146860.html
source: unSafe.sh - 不安全
date: 2023-01-28
fetch_date: 2025-10-04T05:03:00.186769
---

# Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms

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

![](https://8aqnet.cdn.bcebos.com/538f55cf80a5551ab11de655c05ecc94.jpg)

Mitigating RBAC-Based Privilege Escalation in Popular Kubernetes Platforms

This post is also available i
*2023-1-27 22:0:20
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-146860.htm)
阅读量:30
收藏*

---

![A pictorial representation of RBAC-based privilege escalation. Illustrated figures pilot a boat carrying the image of an anchor on a green shield.](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/Kubernetes-v2b.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/kubernetes-privilege-escalation/)

## Executive Summary

Prisma Cloud and Unit 42 recently released a [report examining the use of powerful credentials](https://www.paloaltonetworks.com/resources/whitepapers/kubernetes-privilege-escalation-excessive-permissions-in-popular-platforms) in popular Kubernetes platforms, which found most platforms install privileged infrastructure components that could be abused for privilege escalation. We're happy to share that, as of today, all platforms mentioned in our report have addressed built-in node-to-admin privilege escalation. However, it’s possible third party add-ons might reintroduce the issue.

In the research we presented at [KubeCon EU and BlackHat USA](https://www.youtube.com/watch?v=PGsJ4QTlKlQ), we found that in half the platforms, any container escape had previously allowed for a full cluster compromise because all nodes hosted admin-equivalent credentials. Most of the platforms mentioned in our report made their infrastructure unprivileged by default, while one did so through an optional add-on.

Stripping permissions is often complex, and we recognize fixing this is no small matter. We'd like to thank Azure Kubernetes Service (AKS), AWS Elastic Kubernetes Service (EKS), Google Kubernetes Engine (GKE), RedHat OpenShift Container Platform, Antrea and Calico for working to harden their access control.

We provide a short recap of our research and look into the different mitigations the platforms implemented to address privilege escalation and powerful permissions in Kubernetes. If you're interested in evaluating your own cluster's Role Based Access Control (RBAC) posture, try [rbac-police](https://github.com/PaloAltoNetworks/rbac-police), our open-source RBAC analyzer for Kubernetes.

[Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud) users can catch Kubernetes misconfigurations like excessive RBAC permissions before they're deployed to the cluster via the [Cloud Code Security](https://www.paloaltonetworks.com/prisma/cloud/cloud-code-security) (CCS) module. In the runtime phase, users can rely on the built-in [admission controller for Kubernetes](https://docs.paloaltonetworks.com/prisma/prisma-cloud/21-04/prisma-cloud-compute-edition-admin/access_control/open_policy_agent) to enforce policies that alert on suspicious activity in their clusters, including Kubernetes privilege escalation.

| **Related Unit 42 Topics** | [Privilege Escalation](https://unit42.paloaltonetworks.com/tag/privilege-escalation/), [Cloud Security](https://unit42.paloaltonetworks.com/tag/cloud-security/), [Kubernetes](https://unit42.paloaltonetworks.com/tag/kubernetes/), [Containers](https://unit42.paloaltonetworks.com/tag/containers/), [Container Escape](https://unit42.paloaltonetworks.com/tag/container-escape/) |
| --- | --- |

## **Table of Contents**

[Recap: Powerful Permissions Everywhere](#post-126770-_sl0n3imdgwwx)

## **Recap: Powerful Permissions Everywhere**

Kubernetes managed services, distributions and add-ons install a set of system pods into our cluster to manage its infrastructure and enable core functions such as networking, DNS and logging. Commonly, these pods are deployed via [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) that distribute them onto every node in the cluster.

If those DaemonSets' permissions are loosely granted, they could inadvertently spread powerful credentials throughout the cluster. This could be abused for privilege escalation, as shown in Figure 1.

![Image 1 is a diagram showing how a threat actor exploits DaemonSet credentials to spread in a cluster. It shows the escaped container, api server, and the pods. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126770-1.png)

Figure 1. An attacker who escaped a container exploits the credentials of a powerful DaemonSet to spread in the cluster.

To understand the prevalence of powerful DaemonSets, we analyzed popular Kubernetes platforms—managed services, distributions and container network interfaces (CNIs)—to identify privileged infrastructure components. We found that **most platforms ran powerful DaemonSets**, installing privileged credentials onto every node in the cluster.

As shown in Figure 2, in half the platforms, those credentials were admin-equivalent, allowing a single container escape to compromise the entire cluster.

![Image 2 is a pie chart showing the percentage of platforms where a container escape led to a complete cluster takeover. 50% of credentials used were admin equivalent, with the some prerequisites and no prerequisites splitting the remainder. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2023/01/word-image-126770-2.png)

Figure 2. Percentage of platforms where a container escape allowed a complete cluster takeover.

We believe powerful DaemonSets became common for three main reasons:

1. **Historically, Kubernetes clusters weren't secured by default**.
   In environments where crucial components like Kubelets allowed unauthenticated access, maintaining a least-privileged RBAC posture wasn't a priority. The infrastructure built then set a precedent for powerful DaemonSets.
2. **Some Kubernetes permissions are simply too broad**.
   This means they authorize a large set of operations. Often, granting a service account the ability to perform a necessary but sensitive operation implicitly authorizes it to perform other, potentially harmful operations. RBAC is not a great model for many of these use cases, and an attribute-based access control model that matches some attribute of the principal to some attribute of the resource would often make more sense.
3. **Certain** **permissions appear benign, but are in fact quite powerful**.
   If someone believes a permission is harmless, they won't have second thoughts about granting it. For example, the ability to update the status of pods implicitly allows deleting pods that are part of ReplicaSets.

## Mitigation

After identifying a powerful DaemonSet, we reached out to the relevant platform and started a discussion on mitigation. The response was extremely positive – the teams understood the issue and wanted to resolve it. Mitigations were developed, tested and deployed in recent months. And as of today, all of the privilege escalation attacks we identified are resolved.

Thanks to the work done by the different platforms, the Kubernetes landscape is a safer one, where nodes aren't admins by default. In the following sections, we'll highlight the different approaches platforms took to address powerful DaemonSets in their offerings.

## **Strip Permissions**

The simplest way to address a risky permission is to remove it. A number of platforms identified certain risky permissions that weren't explicitly necessary, and they removed them. Some permissions were made safe by scoping them down to certain [resourceNames](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#referring-to-resources) or subresources.

For example, Cilium found that the “dele...