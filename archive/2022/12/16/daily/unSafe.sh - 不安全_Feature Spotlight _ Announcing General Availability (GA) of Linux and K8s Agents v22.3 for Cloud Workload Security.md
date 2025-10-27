---
title: Feature Spotlight | Announcing General Availability (GA) of Linux and K8s Agents v22.3 for Cloud Workload Security
url: https://buaq.net/go-140177.html
source: unSafe.sh - 不安全
date: 2022-12-16
fetch_date: 2025-10-04T01:38:53.563332
---

# Feature Spotlight | Announcing General Availability (GA) of Linux and K8s Agents v22.3 for Cloud Workload Security

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

![](https://8aqnet.cdn.bcebos.com/0acf26809295f622ca4f629da35609a2.jpg)

Feature Spotlight | Announcing General Availability (GA) of Linux and K8s Agents v22.3 for Cloud Workload Security

SentinelOne is pleased to announce general availability of version 22.3 of our Linux and Kubernetes
*2022-12-15 23:4:41
Author: [www.sentinelone.com(查看原文)](/jump-140177.htm)
阅读量:20
收藏*

---

SentinelOne is pleased to announce general availability of version 22.3 of our Linux and Kubernetes Cloud Workload Security (CWS) agents.

Our Linux and Kubernetes agents are specifically architected for the unique needs of cloud workloads. Our agents operate entirely in user space, making use of eBPF (Extended Berkeley Packet Filter) probes for visibility into the kernel without the hassles of kernel dependencies that would needlessly complicate deployment, impede agility, and consistently cause downtime and loss of business continuity from alternative solutions that use kernel modules.

eBPF is a powerful framework for the monitoring of traffic at the kernel level without the complication of kernel modules. As such, eBPF can be used to collect cloud workload telemetry and feed it to an XDR system for real-time detection of suspicious or malicious activity. This is precisely the SentinelOne approach for cloud workload security, which in turn is augmented by machine-speed response capabilities within the Singularity XDR Platform.

From an architectural perspective, the choice of eBPF is more stable, scalable, and performant than those which rely upon kernel modules. In this way, DevOps are free to innovate quickly, updating host OS images when they see fit and without fear of conflict between an agent version and Linux distribution/version combination.

Moreover, we have made a number of advancements that further enhance performance and detections, including:

* Resource efficiency gains
* Crypto mining detections
* Detection of local privilege escalation
* Detection of ransomware encryption

![](https://www.sentinelone.com/wp-content/uploads/2022/12/Announcing-General-Availability-GAGA-of-Linux-CWPP-agent-v22.3-4.jpg)

## Outstanding Performance With Half the Resources

For any SentinelOne customers still running Linux or K8s agent v21.x, the resource efficiency gains alone are compelling reasons to upgrade your cloud workload protection agent to v22.1 or higher. We’ve been working with some forward-leaning customers, taking their feedback and further extending our resource efficiency. As a result, v22.1 (and higher) improves performance in 2 dimensions compared to version 21.x: 40-50% improvement in memory usage, and 40-50% improvement in CPU usage.

We would be remiss if we did not take the opportunity to thank those customers for taking this journey with us. Together, we achieved these results without sacrificing a single inch of detection performance. In fact, quite the opposite: we raised the bar on Linux detections.

The resource efficiency story is even more compelling for Kubernetes customers. A single, specialized [Singularity Cloud Workload Security for Kubernetes](https://assets.sentinelone.com/abm-cloud/cloud-kubernetes-workload-detection-response) agent protects the host OS of the K8s worker node, all its pods, and all their containers. It does so with no container sidecar or usage of kernel modules, and with complete visibility into and runtime security for Kubernetes workloads. This architectural approach is very compelling for digital natives running workloads at scale.

As a representative example, if a typical sidecar agent takes 128 MB of memory per container, and each worker node has, on average, 30 containers, then the overhead of a sidecar architecture amounts to nearly 4 GB of additional memory per worker node. Multiply that by the number of worker nodes in each K8s cluster, and then again by the number of clusters running workloads across your DEV and PROD cloud accounts, and the operational overhead that the customer pays quickly stacks up. In stark contrast, SentinelOne provides industry-leading performance with half that memory and CPU.

Customers have done the napkin math themselves and drawn their own conclusions. We even have a [business value calculator](http://s1.ai/calc) which takes this into account, to help our prospective customers build their own business case specific to their needs, and to share with their upper management because securing limited budget dollars in the current economic context requires rigorous cash flow analysis.

## Enhanced Detection and Protection

Operational efficiency matters, but the primary job of a runtime agent is workload protection. To borrow from an F1 racing analogy, this is truly where “the rubber meets the road.” The Linux agent v22.3 brings enhanced detections of cryptomining earlier in the chain, local privilege escalation, and ransomware. These gains extend our performance leadership as evidenced by the MITRE ATT&CK benchmark testing, which for the last 2 years has included Linux.

### Cryptomining Detections

Cryptomining malware is a nuisance and financial drain, quietly siphoning off costly compute cycles from workloads. We have made even further advancements in the Singularity Cloud Workload Security ability to detect cryptomining malware. We detect the invocation of cryptominers associated with known suspicious wallets and/or URLs.

With v22.3, we detect cryptominer setup activity before mining even begins. By detecting the configuration and preparation activities, the SentinelOne agent stops cryptomining before it hits the organization’s cloud bill and bogs down workload operations.

### Local Privilege Escalation

The SentinelOne Linux v22.3 agent also alerts on suspicious attempts to escalate local privilege via a SUID binary exploit.

### Ransomware

We’ve seen an increase in ransomware attempts targeting cloud infrastructure, implementing new techniques and methods to compromise workloads. To address it, we enhanced our ransomware detection, identifying file encryption activity via common Linux utilities such as OpenSSL. Ransomware attacks on cloud workloads represent a potentially devastating risk to those businesses that rely upon the integrity and availability of their workloads.

## SentinelOne K8s Agent Now Supports Graviton-backed Amazon EC2

The SentinelOne Kubernetes agent now supports the AWS Graviton-based EC2 instances. Our Linux agent achieved the AWS Graviton Ready Service Designation [back in July 2022](https://assets.sentinelone.com/abm-cloud/edr-for-cloud-workloads-running-on-AWS-Graviton). Extending that support to Kubernetes clusters was a logical next step. The arm64 architecture of Graviton brings with it some compelling efficiency gains which make it very attractive to compute-intensive workloads. Singularity Cloud Workload Security for Kubernetes stands ready to deliver runtime workload protection to your Graviton-based clusters.

## Conclusion

The SentinelOne eBPF-powered CWS agent is architected for the unique needs of cloud infrastructure. By operating entirely in user space, kernel dependency hassles are eliminated, thereby simplifying deployment and maintenance while simultaneously delivering complete runtime visibility and security across the hybrid cloud enterprise. Moreover, DevOps can update their host OS image without fear of agent conflict, so that business agility is supported, not impeded.

To learn more, visit the Singularity Cloud Workload Security for Server/VMs or Kubernetes [product page](https://www.sentinelone.com/platform/singularity-cloud/). There, you can find customer case studies, product informati...