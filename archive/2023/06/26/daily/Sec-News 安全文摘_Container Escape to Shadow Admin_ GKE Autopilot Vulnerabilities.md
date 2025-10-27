---
title: Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities
url: https://govuln.com/news/url/9NDp
source: Sec-News 安全文摘
date: 2023-06-26
fetch_date: 2025-10-04T11:44:33.684285
---

# Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities

[![Logo](/wp-content/uploads/2021/07/PANW_Parent.png)](https://www.paloaltonetworks.com/)

[![Unit42 Logo](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/unit42-logo-white.svg)](https://unit42.paloaltonetworks.com/)

Menu

* [Tools](https://unit42.paloaltonetworks.com/tools/)
* [ATOMs](https://unit42.paloaltonetworks.com/atoms/)
* [Security Consulting](https://www.paloaltonetworks.com/unit42)
* [About Us](https://unit42.paloaltonetworks.com/about-unit-42/)
* [**Under Attack?**](https://start.paloaltonetworks.com/contact-unit42.html)

English

* [English](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/)
* [Japanese](https://unit42.paloaltonetworks.com/ja/gke-autopilot-vulnerabilities/)

* [Threat Research Center](https://unit42.paloaltonetworks.com "Threat Research")
* [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/ "Threat Research")
* [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/ "Cloud Cybersecurity Research")

[Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)

# Container Escape to Shadow Admin: GKE Autopilot Vulnerabilities

![Clock Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-clock.svg)  13  min read

Related Products

[![Prisma Cloud icon](https://unit42.paloaltonetworks.com/wp-content/uploads/2024/06/prisma_RGB_logo_Icon_Color.png)Prisma Cloud](https://unit42.paloaltonetworks.com/product-category/prisma-cloud/ "Prisma Cloud")

* ![Profile Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-profile-grey.svg)

  By:
  + [Yuval Avrahami](https://unit42.paloaltonetworks.com/author/yuval-avrahami/)
* ![Published Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-calendar-grey.svg)

  Published:March 8, 2022
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-category.svg)

  Categories:
  + [Cloud Cybersecurity Research](https://unit42.paloaltonetworks.com/category/cloud-cybersecurity-research/)
  + [Threat Research](https://unit42.paloaltonetworks.com/category/threat-research/)
  + [Vulnerabilities](https://unit42.paloaltonetworks.com/category/vulnerabilities/)
* ![Tags Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-tags-grey.svg)

  Tags:
  + [Containers](https://unit42.paloaltonetworks.com/tag/containers/)

* [![Download Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-download.svg)](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/?pdf=download&lg=en&_wpnonce=63bb46f30e "Click here to download")
* [![Print Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-print.svg)](https://unit42.paloaltonetworks.com/gke-autopilot-vulnerabilities/?pdf=print&lg=en&_wpnonce=63bb46f30e "Click here to print")

Share![Down arrow](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/down-arrow.svg)

* ![Link Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-share-link.svg)
* ![Link Email](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-sms.svg)
* [![Facebook Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-fb-share.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in Facebook")
* [![LinkedIn Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-linkedin-share.svg)](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F&title=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities "Share in LinkedIn")
* [![Twitter Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-twitter-share.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F&text=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities "Share in Twitter")
* [![Reddit Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-reddit-share.svg)](//www.reddit.com/submit?url=https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in Reddit")
* [![Mastodon Icon](https://unit42.paloaltonetworks.com/wp-content/themes/unit42-v6/dist/images/icons/icon-mastodon-share.svg)](https://mastodon.social/share?text=Container%20Escape%20to%20Shadow%20Admin:%20GKE%20Autopilot%20Vulnerabilities%20https%3A%2F%2Funit42.paloaltonetworks.com%2Fgke-autopilot-vulnerabilities%2F "Share in Mastodon")

## **Executive Summary**

In February 2021, Google announced [Autopilot](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-autopilot), a new mode of operation in [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE). With Autopilot, Google provides a "hands-off" Kubernetes experience, managing cluster infrastructure for the customer. The platform automatically provisions and removes nodes based on resource consumption and enforces secure Kubernetes best practices out of the box.

In June 2021, Unit 42 researchers disclosed several vulnerabilities and attack techniques in GKE Autopilot to Google. Users able to create a pod could have abused these to (1) escape their pod and compromise the underlying node, (2) escalate privileges and become full cluster administrators, and (3) covertly persist administrative access through backdoors that are completely invisible to cluster operators.

An attacker who obtained an initial foothold on an Autopilot cluster, for example, through a compromised developer's account, could have exploited these issues to escalate privileges and become a "shadow administrator," with the ability to covertly exfiltrate secrets, deploy malware or cryptominers and disrupt workloads.

Following our disclosure, Google fixed the reported issues, deploying patches universally across GKE. All Autopilot clusters are now protected.

This blog provides a technical analysis of the issues, as well as mitigations for preventing similar attacks against Kubernetes and GKE environments. For a high-level overview of the issues, please refer to our blog on the Palo Alto Networks site, [Unit 42 Discloses Newly Discovered Vulnerabilities in GKE Autopilot](https://www.paloaltonetworks.com/blog/2022/03/gke-autopilot-vulnerabilities).

Palo Alto Networks customers receive protections from the issues discussed below through the Kubernetes admission control and auditing features of [Prisma Cloud](https://www.paloaltonetworks.com/prisma/cloud).

|  |  |
| --- | --- |
| Affected Product | Google Kubernetes Engine (GKE) Autopilot |
| Related Unit 42 Topics | [Container Escape](https://unit42.paloaltonetworks.com/tag/containers/), [Cloud](https://unit42.paloaltonetworks.com/category/cloud/) |

## **Background on GKE Autopilot**

Autopilot is a new mode of operation in GKE, providing what Google describes as a "hands-off" Kubernetes experience. In GKE Standard, customers manage their cluster infrastructure and pay per node. With GKE Autopilot, Google takes care of cluster infrastructure, and customers only pay for their running pods. This allows customers to focus on their applications, cutting operational costs.

In a nutshell, managed cluster infrastructure means Google automatically:

1. Provisions and adjusts the number of nodes according to your pods' resource consumption.
2. Enforces a built-in policy to ensure the cluster adheres to secure best practices and can be safely managed by Google.

Below is a simplified diagram ...