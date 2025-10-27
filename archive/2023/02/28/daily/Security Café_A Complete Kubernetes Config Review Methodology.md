---
title: A Complete Kubernetes Config Review Methodology
url: https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/
source: Security Café
date: 2023-02-28
fetch_date: 2025-10-04T08:15:00.550609
---

# A Complete Kubernetes Config Review Methodology

[Skip to content](#content)

[Security Café](https://securitycafe.ro/)

Security Research and Services

* [Things we do on a daily basis](https://securitycafe.ro/security-services-for-business/)
  + [Red Team (DORA/TIBER) exercises](https://securitycafe.ro/security-services-for-business/dora-tiber-exercises/)
  + [Web Application Penetration Testing](https://securitycafe.ro/security-services-for-business/web-application-penetration-testing/)
  + [Mobile Application Penetration Testing](https://securitycafe.ro/security-services-for-business/mobile-application-penetration-testing/)
  + [Infrastructure Penetration Testing](https://securitycafe.ro/security-services-for-business/infrastructure-penetration-testing/)
  + [Vulnerability Assessment](https://securitycafe.ro/security-services-for-business/vulnerability-assessment/)
* [CVEs, Talks and Tools](https://securitycafe.ro/cves-talks-and-tools/)
* [Contact](https://securitycafe.ro/contact/)
* [About](https://securitycafe.ro/about/)

[![](https://securitycafe.ro/wp-content/uploads/2015/01/cropped-cropped-coffee-banner-2-4.jpg)](https://securitycafe.ro/)

![](https://securitycafe.ro/wp-content/uploads/2023/01/kube1.png?w=673)

# A Complete Kubernetes Config Review Methodology

[February 27, 2023](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/ "10:16 am") [Stefan Tita](https://securitycafe.ro/author/stitakpmgcom/ "View all posts by Stefan Tita") [Cloud Security](https://securitycafe.ro/category/cloud-security/), [Kubernetes](https://securitycafe.ro/category/cloud-security/kubernetes/), [Penetration Testing](https://securitycafe.ro/category/penetration-testing/) [Leave a comment](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#respond)

The are many resources out there that tap into the subject of Kubernetes Pentesting or Configuration Review, however, they usually detail specific topics and misconfigurations and don’t offer a broad perspective on how to do a complete Security Review. That is why in this article I want to cover a more complete overview on all the possible aspects that should be reviewed when dealing with a Kubernetes Security Assessment.

Because there are many topics in this discussion, I will avoid going into too much details on each aspect and instead I will be providing links to references where you can find more details.

#### Table of Contents

* [Intro](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#intro)
* [1. Image and Container inspection](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#1-image-and-container-inspection)
* [2. Configuration Review (aka Benchmark Tests)](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#2-configuration-review-aka-benchmark-tests)
* [3. Permissions/RBAC (Privilege Escalation vectors)](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#3-permissions-rbac-privilege-escalation-vectors)
  + [1. Create Pods (BadPods)](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#1-create-pods-badpods)
  + [2. List/Get/Watch Secrets](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#2-list-get-watch-secrets)
  + [3. Any Resource or Verb (wildcards)](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#3-any-resource-or-verb-wildcards)
  + [4. Create Pods/Exec](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#4-create-pods-exec)
  + [5. Create/Update/Delete Deployment, Daemonsets, Statefulsets, Replicationcontrollers, Replicasets, Jobs and Cronjobs](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#5-create-update-delete-deployment-daemonsets-statefulsets-replicationcontrollers-replicasets-jobs-and-cronjobs)
  + [6. Get/Patch/Create Rolebindings](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#6-get-patch-create-rolebindings)
  + [7. Get/Create Node/Proxy](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#7-get-create-node-proxy)
  + [8. Impersonate user, group, service account](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#8-impersonate-user-group-service-account)
* [4. Publicly Exposed Services and Ingresses](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#4-publicly-exposed-services-and-ingresses)
* [5. Vulnerability/Service Scanning](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#5-vulnerability-service-scanning)
* [6. Add-ons](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#6-add-ons)
* [Wrap-Up](https://securitycafe.ro/2023/02/27/a-complete-kubernetes-config-review-methodology/#wrap-up)

## Intro

Dealing with a Kubernetes (K8s) Security Assessment is relatively similar to a Cloud (AWS/Azure) Configuration Review/Pentest, in that there are many components that each introduce specific security implications and in order to understand these implications a basic understanding of these underlying components is necessary.

![](https://securitycafe.ro/wp-content/uploads/2023/01/k8s-2.png?w=1024)

At a high level a K8s cluster consists of at least one **Worker Node** which hosts the Pods that run containerized applications, and one **Control Plane** (or Master Node) that manages the worker nodes and the Pods in the cluster. For more details on what each underlying component (API Server, etcd, Scheduler, Kubelet, etc.) is responsible for, visit the official documentation:

* <https://kubernetes.io/docs/concepts/overview/components/>

On top of the main components, the K8s Cluster contains many **resources** and each of them comes with specific security implications. Resources can be configured through the API Server located on the Control Plane. The following is a list of all resources running under a K8s Cluster:

```
//kubectl api-resources    #gets a list of all resources

configmaps
secrets
persistentvolumeclaims
pods
daemonsets
deployments
replicasets
statefulsets
jobs
cronjobs
services (ClusterIP, LoadBalancer, NodePort)
ingresses
events
bindings
endpoints
limitranges
podtemplates
replicationcontrollers
resourcequotas
serviceaccounts
controllerrevisions
localsubjectaccessreviews
horizontalpodautoscalers
leases
endpointslices
networkpolicies
securitygrouppolicies    #Security groups for pods, only on AWS EKS
poddisruptionbudgets
rolebindings
roles
```

In order to conduct the Configuration Review the “*get*” and “*list*” permissions should be allowed on all these resources (maybe except secrets in order to avoid disclosure). In order to review the nodes, SSH access would be ideal in order to inspect file permissions and their content settings. In case Amazon EKS (Elastic Kubernetes Service) is used, in order to review the Control Plane configuration the ListCluster and DescribeCluster permission would be required (<https://docs.aws.amazon.com/eks/latest/userguide/security_iam_id-based-policy-examples.html#policy_example2>).

## 1. Image and Container inspection

There is a good change that during the assessment you will also have access to container images. Depending on the company practices these can be publicly available images (such as from Docker Hub, Google Container Registry, GitHub Container Registry, etc.) or images from a private container registry, either way it is a good idea for a company to have a defined standard for allowed and trusted image sources.

One manual method of inspecting images would be to perform Image Forensics by decompressing the archive (a Docker image is essentially an archive) and searching for sensitive information inside the files ([Docker Container Forensics](https://www.youtube.com/watch?v=pOO_dDKGvY4)). Another option would be to deploy co...