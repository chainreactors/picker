---
title: Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities
url: https://buaq.net/go-170232.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:59.905369
---

# Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities

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

![](https://8aqnet.cdn.bcebos.com/4e97b1f69141693ab7ddc5dea6b15b5b.jpg)

Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities

This post is also available i
*2023-6-25 19:7:57
Author: [govuln.com(查看原文)](/jump-170232.htm)
阅读量:29
收藏*

---

![A conceptual image representing Kubernetes security, including the GKE Autopilot vulnerabilities discussed here, which, before fixed, could have allowed for container escape leading to a shadow administrator.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/03/Unit42-blog-2by1-characters-r4d1-2020_Kubernetes-v1b.png)

This post is also available in:
[日本語 (Japanese)](https://unit42.paloaltonetworks.jp/gke-autopilot-vulnerabilities/)

## **Executive Summary**

In February 2021, Google announced [Autopilot](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-autopilot), a new mode of operation in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE). With Autopilot, Google provides a "hands-off" Kubernetes experience, managing cluster infrastructure for the customer. The platform automatically provisions and removes nodes based on resource consumption and enforces secure Kubernetes best practices out of the box.

In June 2021, Unit 42 researchers disclosed several vulnerabilities and attack techniques in GKE Autopilot to Google. Users able to create a pod could have abused these to (1) escape their pod and compromise the underlying node, (2) escalate privileges and become full cluster administrators, and (3) covertly persist administrative access through backdoors that are completely invisible to cluster operators.

An attacker who obtained an initial foothold on an Autopilot cluster, for example, through a compromised developer's account, could have exploited these issues to escalate privileges and become a "shadow administrator," with the ability to covertly exfiltrate secrets, deploy malware or cryptominers and disrupt workloads.

Following our disclosure, Google fixed the reported issues, deploying patches universally across GKE. All Autopilot clusters are now protected.

This blog provides a technical analysis of the issues, as well as mitigations for preventing similar attacks against Kubernetes and GKE environments. For a high-level overview of the issues, please refer to our blog on the Palo Alto Networks site, [Unit 42 Discloses Newly Discovered Vulnerabilities in GKE Autopilot](https://www.paloaltonetworks.com/blog/2022/03/gke-autopilot-vulnerabilities).

Palo Alto Networks customers receive protections from the issues discussed below through the Kubernetes admission control and auditing features of [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud).

## **Table of Contents**

[Background on GKE Autopilot](#Background-on-GKE-Autopilot)

## **Background on GKE Autopilot**

Autopilot is a new mode of operation in GKE, providing what Google describes as a "hands-off" Kubernetes experience. In GKE Standard, customers manage their cluster infrastructure and pay per node. With GKE Autopilot, Google takes care of cluster infrastructure, and customers only pay for their running pods. This allows customers to focus on their applications, cutting operational costs.

In a nutshell, managed cluster infrastructure means Google automatically:

1. Provisions and adjusts the number of nodes according to your pods' resource consumption.
2. Enforces a built-in policy to ensure the cluster adheres to secure best practices and can be safely managed by Google.

Below is a simplified diagram of Autopilot's architecture. Components unique to Autopilot are colored in green and shown with a number corresponding to their role from the list above. Unlike GKE Standard, where nodes are visible as Compute Engine VMs, Autopilot nodes are completely managed by Google, thus colored in green.

![A simplified diagram of Autopilot's architecture. Components unique to Autopilot are colored in green and shown with a number corresponding to their role from the list above. Unlike GKE Standard, where nodes are visible as Compute Engine VMs, Autopilot nodes are completely managed by Google, thus colored in green.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/03/word-image-15.png)

Figure 1. GKE Autopilot architecture.

As seen in Figure 1, two components enforce Autopilot's policy. First is an [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/) validating admission webhook, an open-source project widely used for policy enforcement in Kubernetes. The second is a proprietary Kubernetes authorization mode named GKEAutopilot, which Google implemented by modifying the Kubernetes source code.

The built-in policy serves two [purposes](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#limits): (a) prevent users from accessing cluster components managed by Google, like nodes; and (b) uphold secure Kubernetes best practices. For example, Autopilot forbids running privileged containers, fulfilling both (a) and (b).

![GKE Autopilot's built-in policy prevents users from accessing cluster components managed by Google and upholds secure Kubernetes best practices.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/03/word-image-16.png)

Figure 2. Autopilot's built-in policy prevents privileged containers (Gatekeeper).

Autopilot's policy goes beyond preventing container escapes. Figures 3, 4, and 5 highlight a few interesting examples. [GKE's documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#limits) lists every limit enforced by the policy.

![GKE Autopilot's policy goes beyond preventing container escapes. This screenshot shows how the kube-system namespace is managed. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/03/word-image-17.png)

Figure 3. The kube-system namespace is managed, customers are limited to read-only access.

![GKE Autopilot's policy goes beyond preventing container escapes. This screenshot shows how users cannot list or create mutating admission webhooks.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/03/word-image-18.png)

Figure 4. Users cannot list or create mutating admission webhooks.

![GKE Autopilot's policy goes beyond preventing container escapes. This screenshot shows how External IP services are denied to protect against CVE-2020-8554. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/03/word-image-19.png)

Figure 5. External IP services are denied to protect against CVE-2020-8554.

Reading the error messages in the Figures above, you can see that Gatekeeper prevented the operations in Figures 2 and 5, while the GKEAutopilot authorization mode prevented the operations in Figures 3 and 4.

## **Attack Surfaces Unique to GKE Autopilot**

Autopilot's built-in policy blocks several exploitation paths out of the box, providing better security posture compared to standard Kubernetes or GKE Standard. That being said, it also creates attack surfaces unique to Autopilot:

1. Administrators may rely on Autopilot's policy to prevent risky configurations. If attackers can somehow circumvent that policy, they may escalate privileges via methods customers expect to be blocked, like deploying a privileged container.
2. Autopilot administrators aren't fully privileged, restricted by the built-in policy from accessing nodes and certain privileged Kubernetes APIs. If attackers can bypass Autopilot's policy, they may gain higher privileges than administrators, opening the door for invisible backdoors.

The following sections present vulnerabilities, privilege escala...