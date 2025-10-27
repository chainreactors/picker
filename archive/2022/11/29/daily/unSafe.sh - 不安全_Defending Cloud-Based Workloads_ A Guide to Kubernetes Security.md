---
title: Defending Cloud-Based Workloads: A Guide to Kubernetes Security
url: https://buaq.net/go-137611.html
source: unSafe.sh - 不安全
date: 2022-11-29
fetch_date: 2025-10-03T23:57:05.215192
---

# Defending Cloud-Based Workloads: A Guide to Kubernetes Security

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

![](https://8aqnet.cdn.bcebos.com/8c0e9a49c06b2b1c565afb4aee4f6d14.jpg)

Defending Cloud-Based Workloads: A Guide to Kubernetes Security

As more businesses move their applications to the cloud, in many cases they turn to Kubernetes (k8s
*2022-11-28 22:15:35
Author: [www.sentinelone.com(查看原文)](/jump-137611.htm)
阅读量:34
收藏*

---

As more businesses move their applications to the cloud, in many cases they turn to Kubernetes (k8s) to manage them. In 2021, [96% of organizations surveyed](https://www.cncf.io/wp-content/uploads/2022/02/CNCF-AR_FINAL-edits-15.2.21.pdf) by CNCF (Cloud Native Computing Foundation) were either using or evaluating Kubernetes. This open-source platform helps organizations orchestrate and automate the deployment of containerized applications and services.

While Kubernetes offers many benefits, it also presents new security challenges to overcome. In this post, we discuss how cybercriminals target Kubernetes environments and what organizations can do to protect their business.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Defending-Cloud-Based-Workloads-A-Guide-to-Kubernetes-Security-2.jpg)

## Kubernetes Fundamentals

Kubernetes (hereafter, “k8s”) is an open-source container orchestration platform that was originally designed by Google and subsequently then transferred to the Cloud Native Computing Foundation (CNCF). It automates the deployment, scaling, and management of containerized workloads.

K8s has become a popular choice for DevOps as it provides a mechanism for reliable container image build, deployment, and rollback, ensuring consistency across deployment, testing, and product.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Screenshot-2022-11-28-at-11.32.51-AM.jpg)

[Source](https://kubernetes.io/docs/concepts/overview/components/): Kubernetes

In many ways, containers are very similar to virtual machines; however, the biggest difference is that they are more relaxed in isolation properties, allowing sharing of the operating system across applications. Containers are lightweight (especially compared to VMs), have their own file system, and share CPU, memory, and process space.

## Quick Environmental Facts About Kubernetes

The majority of K8s implementations are managed via [Infrastructure-as-a-Service](https://www.sentinelone.com/blog/cloud-security-understanding-the-difference-between-iaas-and-paas/) (IaaS) tooling, such as Amazon Elastic Kubernetes Service (EKS) or GCP’s Google Kubernetes Engine (GKE). By using these Kubernetes-as-a-service tools, teams can focus on building and deploying, while the Cloud Service Provider (CSP) curates and updates core aspects of the K8s services.

Kubernetes is deployed in a *cluster*, whereas the physical server or virtual machines which are part of the cluster are known as *worker nodes*. Each worker node operates a number of *pods*, which are a logical grouping of 1 or more *containers* running within each pod.

Applications are composed of microservices in a modern cloud-native architecture.

Microservices is an architecture design that allows building distributed applications that can break applications into independent and standalone deployable services. The best practice is to run one microservice per pod.

Orchestration is key to simplifying and automating workload infrastructure management, so there’s a *control plane* with many components such as schedules, detects, responds, controllers for nodes, cloud providers, and an API to query and manipulate the current state.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Screenshot-2022-11-28-at-11.35.48-AM.jpg)

[Source](https://docs.cambridgesemantics.com/anzo/v5.1/userdoc/k8s-concepts.htm)

Several features are relevant for security professionals to be aware of:

* DaemonSet – A manifest of pods to automatically deploy to all worker nodes within a cluster. As demand on the workload varies, a DaemonSet provides a means of auto-scaling infrastructure to meet that demand, with each worker given the appropriate pods and containers upon startup. This simplifies on-demand workload management. This is helpful for security and monitoring.
* Namespace – A logical construct which allows isolation of resources within the cluster. A namespace separates users, apps, and resources into a specific scope.
* SecurityContext – defines privileges and capabilities for individual pods and containers.
* Helm Chart – A manifest of files which describes a related set of K8s resources and which simplifies deployment.

## Threat Landscape for Kubernetes

With Kubernetes being still relatively complex to implement, it is often misconfigured and underprotected, which makes it a prime target for cybercriminals. Attacks often escape detection by traditional security tools and systems, and a compromise can allow a threat actor to take control of many containers and applications at once. Further, cloud workloads can provide cybercriminals with access to sensitive data and information that can then be used to launch attacks on other systems.

## Real-World Kubernetes Attack Examples

### CRI-O Container Runtime Allows Attackers Host Access

CRI-O is a container runtime for Kubernetes that allows users to run containers without a full operating system. [A recent security flaw in CRI-O allowed attackers](https://www.infoq.com/news/2022/03/container-runtime-vulnerability/) to gain host access to systems running the container runtime. The flaw has since been patched, and users are advised to update their CRI-O installations as soon as possible.

### Kubernetes Flaw Exposes Cluster Data to Attackers

A flaw in the Kubernetes API server allowed attackers to gain access to sensitive data stored in etcd, the cluster’s key-value store. The flaw researchers at Red Hat discovered could be exploited to gain access to data such as passwords, API keys, and SSL certificates.

The researchers found that the flaw could be exploited by creating a malicious container sending requests to the Kubernetes API server. These requests would then be forwarded to the `etcd` database, allowing the attacker to access the sensitive data.

### Cryptomining Attack Against Kubernetes Cluster in Microsoft Azure

Microsoft disclosed that Kubernetes clusters running on [Microsoft Azure were targeted by cybercriminals for cryptomining](https://www.infosecurity-magazine.com/news/kubernetes-hit-kubeflow/). While by default, the Kubeflow dashboard is only accessible internally, some developers had modified the configuration of the Istio Service to Load-Balancer, which exposed the service to the internet. By exposing the service directly to the internet, anyone could directly access the Kubeflow dashboard and, with that, perform operations such as deploying new containers in the cluster.

## Security Tooling Challenges

Traditional security tools and procedures often focus on what is running within the enterprise network. For some organizations, when procedures like those for incident response were built and implemented, containerization or, to some extent, cloud computing wasn’t even broadly available. With that in mind, there are several challenges regarding protection, detection, and response capabilities for Kubernetes.

### By Default, k8s Are Not Optimized for Security

K8s offers a lot of advantages for DevOps to rapidly scale operations. However, many are not aware that, by default, K8s are not optimized to be secure. For example, organizations need to consider how they will secure the API server from malicious access or how they can protect `etcd` with TLS, Firewall, and Encryption. Also, things like aud...