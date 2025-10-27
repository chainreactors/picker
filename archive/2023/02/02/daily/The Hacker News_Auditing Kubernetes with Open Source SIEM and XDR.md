---
title: Auditing Kubernetes with Open Source SIEM and XDR
url: https://thehackernews.com/2023/02/auditing-kubernetes-with-open-source.html
source: The Hacker News
date: 2023-02-02
fetch_date: 2025-10-04T05:32:08.290656
---

# Auditing Kubernetes with Open Source SIEM and XDR

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Auditing Kubernetes with Open Source SIEM and XDR](https://thehackernews.com/2023/02/auditing-kubernetes-with-open-source.html)

**Feb 01, 2023**The Hacker NewsSIEM / Kubernetes

[![Auditing Kubernetes](data:image/png;base64... "Auditing Kubernetes")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1rjaFk6Tftt19hJicagpIzaNfyEiEM3AU9H40dqCVnjIPb_HxIEvdapTKBgNOFjNWW2NEObN_DO3mga8cjrILGiAZeqLPUHc9Pt8jau1KuAcEKx-sCeS9b4mMAJZWAFElgJFAhsmwdGaHhhagy5lrFk-mTtgtyaG5Z-x1pOF5jYifst7jtWj7Hq-o/s790-rw-e365/wazuh.png)

Container technology has gained traction among businesses due to the increased efficiency it provides. In this regard, organizations widely use Kubernetes for deploying, scaling, and managing containerized applications. Organizations should audit Kubernetes to ensure compliance with regulations, find anomalies, and identify security risks. The Wazuh open source platform plays a critical role in monitoring Kubernetes and other components of an organization's infrastructure.

## What is Kubernetes?

Kubernetes is an open source container management solution that automates the deployment and scaling of containers and also manages the life cycle of containers. It organizes containers into logical units for simple management and discovery. Kubernetes extends how we scale containerized applications so that we may use a truly persistent infrastructure.

You can build cloud-native applications based on microservices with Kubernetes. Enthusiasts view Kubernetes as the cornerstone of application modernization. It enables the containerization of current applications, allowing developers to create applications quickly.

The complexity of running programs grows when they spread across several servers and containers. To handle this complexity, Kubernetes offers an open source API that manages where and how those containers will execute. Kubernetes incorporates load balancing, controls service discovery, keeps track of resource allocation, and scales based on compute use. Additionally, it assesses the condition of each resource and gives programs the ability to self-fix by replicating containers or restarting them automatically.

## Auditing Kubernetes

There are several policies that organizations should comply with, depending on the jurisdiction and sector in which they operate. Some of these policies enhance the cyber resilience of the IT infrastructure, for example, PCI DSS and GDPR. The Kubernetes cluster is part of the IT infrastructure, and organizations should ensure they comply with policies and security best practices where applicable.

One of the requirements that appear in most IT policy documents is the log retention policy. Log retention policies dictate how long you should store logs. You can use these logs to identify threats during active monitoring and incident investigation.

Administrators interact with the Kubernetes cluster via the Kubernetes API, and the cluster can log all API requests and responses. You can detect unusual or unwanted API calls from the Kubernetes audit logs. In more detail, you can get alerts for events such as authentication failure, container creation, modification, and deletion. The Kubernetes audit logging feature is disabled by default. Therefore, you need to take some necessary steps to turn it on.

### Using Wazuh to monitor and archive Kubernetes audit logs

You need to monitor the audit logs to detect security threats and anomalies. Additionally, you need to index the logs to search for relevant information during an incident investigation. [Wazuh](https://wazuh.com/) monitors, stores, and indexes the Kubernetes audit logs. Wazuh is an open source unified XDR and SIEM platform. It is commercially free and has over 10 million annual downloads.

The Wazuh development team has a detailed guide on [auditing Kubernetes with Wazuh](https://wazuh.com/blog/auditing-kubernetes-with-wazuh/). The guide details steps on how to do the following:

* Configure the Wazuh server to receive and process the Kubernetes audit logs.
* Enable audit logs on the Kubernetes cluster and forward them to the Wazuh server.

You can create custom rules to trigger alerts when Wazuh detects specific events in the Kubernetes audit log. For example, you can create rules to trigger alerts when resources are created or deleted on the Kubernetes cluster.

|  |
| --- |
| [![SIEM and XDR](data:image/png;base64... "SIEM and XDR")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJNtaFV5hBu2KePBiKU4cG3DoZ2es02UrI22BtxQbjW5MrYhIIl9EZWNSPsgKvbARo5RdjKEBODlPhWcNYYuOw8c-CDZt4YZyeFbxUdiTErzPB4D35BFU0wMKLG9mZ0Xb2qUre_6hzsBcOUEGm-19llw8c-C_XbCWskCulHB8WTqfl76jVH832TCGKMg/s790-rw-e365/wazuh-1.png) |
| Figure 1: Alerts triggered from Kubernetes audit logs on the Wazuh dashboard |

You can configure Wazuh to display all archived logs on the dashboard. These are logs of Kubernetes events that did not trigger an alert.

|  |
| --- |
| [![SIEM and XDR](data:image/png;base64... "SIEM and XDR")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdGIjvuQzTUr39HdUCaVGQr-nN3tomY--4DvvPDg50vQFX3ROOY2eEbigwr2e0_trPvB50x6xMMvWpuprTChO-hNMKZMgb2HD76VJmMgA_ypmfMZXq2ePoP1FXtNmqZ0X4HvEthW58V0dNhEgaBVWVHAkzsmAVeE9toPUTuTR_U604Er_GFfcSe4JDMg/s790-rw-e365/wazuh-2.png) |
| Figure 2: Kubernetes audit log archive on the Wazuh dashboard |

The Wazuh indexer is a highly scalable full-text search and analytics engine. The indexer indexes and stores the Kubernetes audit logs to provide you with real-time data search and analytics capabilities. The Wazuh indexer increases efficiency during an incident investigation when you need to retrieve relevant data from the audit logs.

## Summary

Kubernetes is widely used to deploy, scale, and manage applications. You should maintain Kubernetes audit logs for security and compliance purposes. The audit logs contain data that can indicate unusual or unwanted activities. Wazuh is an open source XDR and SIEM solution that monitors, archives, and queries Kubernetes audit logs to identify securit...