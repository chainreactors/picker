---
title: Upcoming breaking change in SAP BTP, Kyma Runtime: Enabling the Istio CNI plugin
url: https://blogs.sap.com/2022/12/14/upcoming-breaking-change-in-sap-btp-kyma-runtime-enabling-the-istio-cni-plugin/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:31:56.720881
---

# Upcoming breaking change in SAP BTP, Kyma Runtime: Enabling the Istio CNI plugin

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Upcoming breaking change in SAP BTP, Kyma Runtime:...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158002&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Upcoming breaking change in SAP BTP, Kyma Runtime: Enabling the Istio CNI plugin](/t5/technology-blog-posts-by-sap/upcoming-breaking-change-in-sap-btp-kyma-runtime-enabling-the-istio-cni/ba-p/13550765)

![strekm](https://avatars.profile.sap.com/0/c/id0ce40f5c90aa7473a478866fe6b7f9288a0ab5cb8a2ed12181128419d72d3031_small.jpeg "strekm")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[strekm](https://community.sap.com/t5/user/viewprofilepage/user-id/45483)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158002)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158002)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550765)

‎2022 Dec 14
11:11 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158002/tab/all-users "Click here to see who gave kudos to this post.")

2,259

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (1)

I'm part of the Kyma team responsible for Service Mesh and Security topics. My team and I aim to provide a stable environment that enables exposing and securing a workload with ease. The recently introduced **Istio Container Network Interface (CNI) plugin**, which significantly enhances workload security, will be enabled by default with 2.11 version of Kyma. Let me guide you through the migration process and share the details about this improvement.

## Background

So far, workloads being part of Istio Service Mesh were injected with the `istio-init` container responsible for setting up the networking functionality for the Istio sidecar proxy. Unfortunately, to manage such workloads, their owners needed to have elevated Kubernetes RBAC permissions. The requirement of enabling elevated permissions for every user willing to deploy Pods to Service Mesh caused a security concern that we decided to address. Therefore, we introduced the Istio CNI plugin which does not require the user to have elevated permissions to be able to manage workloads in Service Mesh. Running centrally, it transfers the requirement for elevated permissions from the workload owner to the Service Mesh Namespace. Because the Istio CNI plugin replaces the functionality of the `istio-init` container, enabling it might cause some network connectivity problems to the custom `initContainers` relying on network connectivity during the workload initialization phase.

## Migration

The Istio CNI plugin will be enabled by default with **version 2.11 of SAP BTP, Kyma Runtime scheduled to be released by the end of February 2023**. It is **already** possible to enable the Istio CNI plugin in a development environment and test the upcoming changes there. After successful tests, the migration steps can be replicated in a production environment. Remember that these preparations are **mandatory** and must be made before Kyma 2.11. To mitigate the risk of workload downtime after the release, take the following steps:
- Verify which workloads may be affected.
- Apply the configuration changes.
- Enable the Istio CNI plugin.
- Verify if workloads are healthy.

To check which of your workloads are prone to face connectivity errors, run:

|
 ``` kubectl get all -o="custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,INIT-CONTAINERS:.spec.initContainers[*].name,CONTAINERS:.spec.containers[*].name,KIND:.kind" -A --field-selector=metadata.namespace!=kyma-system,metadata.namespace!=kube-system,metadata.namespace!=istio-system | awk '{n=split($3,a,/,/); if (length(a)>1) {print}}' ``` |

The previous command lists all the workloads outside of the Kyma Namespace and the system Namespace which have the `initContainers` field defined. Here's an example of a Pod with the defined `initContainers`:

|
 ``` apiVersion: v1  kind: Pod  metadata:    name: example-workload    namespace: test-namespace  spec:    containers:    - name: istio-proxy      image: eu.gcr.io/kyma-project/external/istio/proxyv2:1.15.3-distroless      ...    - image: docker.io/kennethreitz/httpbin      name: example-workload      ...    initContainers:    - name: example-init-container      image: eu.gcr.io/kyma-project/external/busybox:1.34.1      ...    - name: istio-init      image: eu.gcr.io/kyma-project/external/istio/proxyv2:1.15.3-distroless      securityContext:        allowPrivilegeEscalation: false        capabilities:          add:          - NET_ADMIN          - NET_RAW          drop:          - ALL        privileged: false        readOnlyRootFilesystem: false        runAsGroup: 0        runAsNonRoot: false        runAsUser: 0    ... ``` |

The previous example shows a Pod having the `example-workload` container and the `istio-proxy` container. Since this workload is part of Service Mesh it also has the `istio-init` container with the `securityContext` which configures the `NET_ADMIN` and `NET_RAW`  capabilities as well as elevated values for the `runAs*` settings. The fact that a workload is listed after executing the command does not mean that it will face errors after the Istio CNI plugin rollout. Each workload should be further analyzed to verify whether its `initContainers` require network. Only the workloads which do rely on network in the initialization phase need to be configured to mitigate connectivity errors. To eliminate the risk of having networking issues, configure these workloads with one of the following settings:

* Set the `UID` of the `initContainer` to `1337`  using `runAsUser` . `1337` is the `UID`  used by the sidecar proxy. The traffic sent by this UID is not captured by the Istio’s iptables rule. Application container traffic is still captured as usual.

* Set the `traffic.sidecar.istio.io/excludeOutboundIPRanges`  annotation to `disable`. It disables redirecting traffic to any CIDRs the `initContainers` communicate with.

* Set the `traffic.sidecar.istio.io/excludeOutboundPorts`  annotation to `disable`. It disables redirecting traffic to the specific outbound ports the `initContainers` use.

> **WARNING:** Be aware that the `excludeOutbound*` annotations affect all the containers in a workload, so setting them might introduce issues in those containers that don't need to be configured.

The recommended configuration should look like this:

|
 ``` apiVersion: apps/v1  kind: Deployment  metadata:  ...    name: example-workload    namespace: example-namespace  spec:    ...    template:      ...      spec:          ...        initContainers:        ...          image: eu.gcr.io/kyma-project/external/busybox:1.34.1          imagePullPolicy: IfNotPresent ...