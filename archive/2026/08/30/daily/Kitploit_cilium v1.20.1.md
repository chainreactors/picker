---
title: cilium v1.20.1
url: https://kitploit.com/en/posts/github-cilium-cilium-v1201
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:43.005674
---

# cilium v1.20.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/4489/11ad861cc5d9ca773026432a9cfa1cc72455b3f7d8b58cb4fc58e7eff28761fd.png)

New releaseAug 30, 2026

# cilium v1.20.1

eBPF-based Networking, Security, and Observability

Share

.. raw:: html

![Cilium Logo](https://assets.kitploit.com/production/public/readmes/4489/5c974d9528e79bc795122178b45c9b8bfd0d4f929c554da3045d2391573fb9cc.png)

|cii| |go-report| |clomonitor| |artifacthub| |slack| |go-doc| |rtd| |apache| |bsd| |gpl| |fossa| |gateway-api| |codespaces|

Cilium is a networking, observability, and security solution with an eBPF-based
dataplane. It provides a simple flat Layer 3 network with the ability to span
multiple clusters in either a native routing or overlay mode. It is L7-protocol
aware and can enforce network policies on L3-L7 using an identity-based security
model that is decoupled from network addressing.

Cilium implements distributed load balancing for traffic between pods and to
external services, and is able to fully replace kube-proxy, using efficient
hash tables in eBPF, allowing for almost unlimited scale. It also supports
advanced functionality like integrated ingress and egress gateways, bandwidth
management, and service mesh, and provides deep network and security visibility and monitoring.

A new Linux kernel technology called eBPF\_ is at the foundation of Cilium. It
supports dynamic insertion of eBPF bytecode into the Linux kernel at various
integration points such as: network IO, application sockets, and tracepoints to
implement security, networking, and visibility logic. eBPF is highly efficient
and flexible. To learn more about eBPF, visit `eBPF.io`\_.

.. image:: Documentation/images/cilium-overview.png
:alt: Overview of Cilium features for networking, observability, service mesh, and runtime security

.. raw:: html

[![CNCF Graduated Project](https://raw.githubusercontent.com/cncf/artwork/main/other/cncf-member/graduated/white/cncf-graduated-white.svg)](https://cncf.io/)
[![eBPF Logo](https://raw.githubusercontent.com/cilium/cilium/HEAD/.github/assets/ebpf-horizontal-dark-back.svg)](https://ebpf.io/)

# Stable Releases

The Cilium community maintains minor stable releases for the last three minor
Cilium versions. Older Cilium stable versions from minor releases prior to that
are considered EOL.

For upgrades to new minor releases, please consult the `Cilium Upgrade Guide`\_.

Listed below are the actively maintained release branches along with their latest
patch release, corresponding image pull tags and their release notes:

+---------------------------------------------------------+------------+------------------------------------+----------------------------------------------------------------------------+
| `v1.20 <https://github.com/cilium/cilium/tree/v1.20>`\_\_ | 2026-07-29 | `quay.io/cilium/cilium:v1.20.0` | `Release Notes <https://github.com/cilium/cilium/releases/tag/v1.20.0>`\_\_ |
+---------------------------------------------------------+------------+------------------------------------+----------------------------------------------------------------------------+
| `v1.19 <https://github.com/cilium/cilium/tree/v1.19>`\_\_ | 2026-07-16 | `quay.io/cilium/cilium:v1.19.6` | `Release Notes <https://github.com/cilium/cilium/releases/tag/v1.19.6>`\_\_ |
+---------------------------------------------------------+------------+------------------------------------+----------------------------------------------------------------------------+
| `v1.18 <https://github.com/cilium/cilium/tree/v1.18>`\_\_ | 2026-07-16 | `quay.io/cilium/cilium:v1.18.12` | `Release Notes <https://github.com/cilium/cilium/releases/tag/v1.18.12>`\_\_ |
+---------------------------------------------------------+------------+------------------------------------+----------------------------------------------------------------------------+

## Architectures

Cilium images are distributed for AMD64 and AArch64 architectures.

## Software Bill of Materials

Starting with Cilium version 1.13.0, all images include a Software Bill of
Materials (SBOM). The SBOM is generated in `SPDX`\_ format. More information
on this is available on `Cilium SBOM`\_.

.. \_`SPDX`: <https://spdx.dev/>
.. \_`Cilium SBOM`: <https://docs.cilium.io/en/latest/configuration/sbom/>

# Development

For development and testing purposes, the Cilium community publishes snapshots,
early release candidates (RC) and CI container images built from the `main branch <https://github.com/cilium/cilium/commits/main>`\_. These images are
not for use in production.

For testing upgrades to new development releases, please consult the latest
development build of the `Cilium Upgrade Guide`\_.

Listed below are branches for testing along with their snapshots or RC releases,
corresponding image pull tags and their release notes where applicable:

+----------------------------------------------------------------------------+------------+-----------------------------------------+---------------------------------------------------------------------------------+
| `main <https://github.com/cilium/cilium/commits/main>`\_\_ | daily | `quay.io/cilium/cilium-ci:latest` | N/A |
+----------------------------------------------------------------------------+------------+-----------------------------------------+---------------------------------------------------------------------------------+
| `v1.21.0-pre.0 <https://github.com/cilium/cilium/commits/v1.21.0-pre.0>`\_\_ | 2026-08-03 | `quay.io/cilium/cilium:v1.21.0-pre.0` | `Release Notes <https://github.com/cilium/cilium/releases/tag/v1.21.0-pre.0>`\_\_ |
+----------------------------------------------------------------------------+------------+-----------------------------------------+---------------------------------------------------------------------------------+

# Functionality Overview

.. begin-functionality-overview

## CNI (Container Network Interface)

`Cilium as a CNI plugin <https://cilium.io/use-cases/cni/>`\_ provides a
fast, scalable, and secure networking layer for Kubernetes clusters. Built
on eBPF, it offers several deployment options:

* **Overlay networking:** an encapsulation-based virtual network spanning all
  hosts with support for VXLAN and Geneve. It works on almost any network
  infrastructure as the only requirement is IP connectivity between hosts
  which is typically already given.
* **Native routing mode:** Use of the regular routing table of the Linux
  host. The network must be capable of routing the IP addresses
  of the application containers. It integrates with cloud routers, routing
  daemons, and IPv6-native infrastructure.
* **Flexible routing options:** Cilium can automate route learning and
  advertisement in common topologies such as using L2 neighbor discovery
  when nodes share a layer 2 domain, or BGP when routing across layer 3
  boundaries.

Each mode is designed for maximum interoperability with existing
infrastructure while minimizing operational burden.

## Load Balancing

Cilium implements distributed load balancing for traffic between application
containers and to/from external services. The load balancing is implemented
in eBPF using efficient hash tables, enabling high service density and low
latency at scale.

* **East-west load balancing** rewrites service connections at the socket
  level (`connect()`), avoiding the overhead of per-packet NAT and fully
  `replacing kube-proxy <https://cilium.io/use-cases/kube-proxy/>`\_.
* **North-south load balancing** supports XDP for high-throughput scenarios
  and `layer 4 load balancing <https://cilium.io/use-cases/load-balancer/>`\_
  including Direct Server Return...