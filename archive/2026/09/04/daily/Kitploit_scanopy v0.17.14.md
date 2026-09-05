---
title: scanopy v0.17.14
url: https://kitploit.com/en/posts/github-scanopy-scanopy-v01714
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:07.857307
---

# scanopy v0.17.14

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50700/016130103bbadf9a067e2f83dbd170c14ca3f9f37e83f9af75a670520dc8975c-display-v1.webp)

New releaseSep 4, 2026

# scanopy v0.17.14

Network diagrams that update themselves

Share

# Scanopy

![Scanopy Logo](https://assets.kitploit.com/production/public/readmes/50700/4f60e8a2b1ae1553eaf149ae7797a5cefc982dda639ca04719e23b99a7ad8ba4/02acc15cbb399719bdc2ccd688f5e58dc51183faf68a9de94e72e3cf18ab4ac4-display-v1.webp)

**Network documentation, without the drawing.**

Scanopy replaces manual network diagrams with a continuously maintained model of what's actually running. A single daemon scans on a schedule and produces four views from each scan: L2 (physical), L3 (logical), workloads, and applications. Unlike diagrams drawn in draw.io that go stale the week they're saved, or IaC state that misses drift and resources provisioned outside the pipeline, Scanopy reflects the current state of your infrastructure. Export as SVG, Mermaid, or Confluence; embed live maps; or feed the model into your existing source of truth.

![Docker Pulls](https://img.shields.io/docker/pulls/mayanayza/netvisor-server?style=for-the-badge&logo=docker) ![Github Stars](https://img.shields.io/github/stars/scanopy/scanopy?style=for-the-badge&logo=github)
![GitHub release](https://img.shields.io/github/v/release/scanopy/scanopy?style=for-the-badge) ![License](https://img.shields.io/github/license/scanopy/scanopy?style=for-the-badge)
![Daemon image size](https://img.shields.io/docker/image-size/mayanayza/scanopy-daemon?style=for-the-badge&label=Daemon%20image%20size) ![Server image size](https://img.shields.io/docker/image-size/mayanayza/scanopy-server?style=for-the-badge&label=Server%20image%20size)
![Daemon](https://img.shields.io/github/actions/workflow/status/scanopy/scanopy/daemon-ci.yml?label=daemon-ci&style=for-the-badge) ![Server](https://img.shields.io/github/actions/workflow/status/scanopy/scanopy/server-ci.yml?label=server-ci&style=for-the-badge) ![UI](https://img.shields.io/github/actions/workflow/status/scanopy/scanopy/ui-ci.yml?label=ui-ci&style=for-the-badge)
[![Discord](https://img.shields.io/discord/1432872786828726392?logo=discord&label=discord&labelColor=white&color=7289da&style=for-the-badge)](https://discord.gg/b7ffQr8AcZ) [![Translations](https://img.shields.io/weblate/progress/scanopy?style=for-the-badge&logo=weblate)](https://hosted.weblate.org/engage/scanopy/)

> 💡 **Prefer not to self-host?** [Get a free trial](https://scanopy.net?utm_source=github&utm_medium=readme&utm_campaign=cloud_trial) of Scanopy Cloud

|  |  |
| --- | --- |
| ![L2 view](https://assets.kitploit.com/production/public/readmes/50700/016130103bbadf9a067e2f83dbd170c14ca3f9f37e83f9af75a670520dc8975c/8d43c0ff662b09ab13d122beb0bf0443172f82441b0c070d842614b54b22a765-display-v1.webp) **L2 (Physical)** Every switch, every port, every link. | ![L3 view](https://assets.kitploit.com/production/public/readmes/50700/2eb2e0e081807e03bf184ef69aba06028d8a0a64c081b67e267609512b7807e0/84697ff5fe374d6504490be7c3bda77cb3143f05c0db60c4087f5389f5455fee-display-v1.webp) **L3 (Logical)** Subnets and how hosts connect across them. |
| ![Workloads view](https://assets.kitploit.com/production/public/readmes/50700/09ef8e1c12ae3a39812be24ed5ed4835dc75715e8263b2cbb3a34e7d2e115b29/68cc95dbdb7c3edaa3155ee3cd065fb7e7e51471c6208b3d6a7c1edbf334e1b0-display-v1.webp) **Workloads** Bare metal to hypervisors to containers. | ![Applications view](https://assets.kitploit.com/production/public/readmes/50700/ea0bbce1ed46b478f6bff8052b98ad9d291c7fde8f87acef3b339a512ab6a82d/bee9d8a58130a792f6d85841bc3ecb9db341295d056dadb554e5b8c68fb92a9d-display-v1.webp) **Applications** Services and their dependencies, grouped by application. |

## ✨ Features

* **Automatic discovery**: Maps hosts and services by scanning the network. One scanner, no per-device agents.
* **230+ service definitions**: Auto-detects databases, web servers, containers, network infrastructure, and enterprise applications.
* **Four views from one scan**: L2 (physical), L3 (logical), workloads, and application dependencies.
* **Distributed scanning**: Deploy daemons across segments to map multi-site and multi-VLAN topologies.
* **Docker & SNMP integration**: Native discovery for containerized services and network hardware.
* **Scheduled rescans**: Documentation stays current as infrastructure changes.
* **Multi-user + RBAC**: Organization management, role-based access, and shareable live views for teammates or external stakeholders.

## 🎯 Perfect For

* **Platform & DevOps teams**: Trace service dependencies without APM. Map containers, VMs, and hardware in one model.
* **Network engineers**: Multi-VLAN, multi-site topology diagrams derived from SNMP, LLDP, and ARP. No manual drawing.
* **IT operations**: Keep inventory, topology, and dependencies current across teams and sites.
* **MSPs**: Per-client documentation with shareable live views.
* **Home labs**: Document your infrastructure without opening draw.io.

## 📋 Licensing

**Self-hosted ([AGPL-3.0](https://github.com/scanopy/scanopy/blob/main/LICENSE.md)):** Free for all use. Requires source disclosure for network services and copyleft compliance.
**Self-hosted ([Commercial license](https://github.com/scanopy/scanopy/blob/main/COMMERCIAL-LICENSE.md)):** For those who cannot comply with AGPL-3.0 terms. Contact [[email protected]](/cdn-cgi/l/email-protection#bdd1d4ded8d3ced4d3dafdcededcd3d2cdc493d3d8c9)
**Hosted Solution:** **[Scanopy Cloud](https://scanopy.net?utm_source=github&utm_medium=readme&utm_campaign=cloud_trial)** subscription for zero infrastructure management

## 🚀 Quick Start for Self Hosting

**Docker Compose**

root@kitploit:~

```
curl -O https://raw.githubusercontent.com/scanopy/scanopy/refs/heads/main/docker-compose.yml
docker compose up -d
```

**Proxmox**

Use this [helper script](https://community-scripts.github.io/ProxmoxVE/scripts?id=scanopy) to create a Scanopy LXC.

**Unraid**

Available as an Unraid community app.

> 💡 **Prefer not to self-host?** [Get a free trial](https://scanopy.net?utm_source=github&utm_medium=readme&utm_campaign=cloud_trial) of Scanopy Cloud

---

Access the UI at `http://<your-server-ip>:60072`, create your account, and wait for the first discovery to complete.

For detailed setup options and configuration, see the [Installation Guide](https://scanopy.net/docs/server-installation?utm_source=github&utm_medium=readme&utm_campaign=docs).

## 📚 Documentation + API

**[scanopy.net/docs](https://scanopy.net/docs?utm_source=github&utm_medium=readme&utm_campaign=docs)**

## 🚀 Demo

**[demo.scanopy.net](https://demo.scanopy.net/?utm_source=github&utm_medium=readme&utm_campaign=demo)**. Hosted demo app with a sample dataset. Try the full UI without installing anything.

## 🤝 Contributing

We welcome contributions! See our [contributing guide](https://github.com/scanopy/scanopy/blob/main/contributing.md) for details.

Great first contributions:

* [Adding service definitions](https://github.com/scanopy/scanopy/blob/main/contributing.md#adding-service-definitions)
* [Translating Scanopy](https://hosted.weblate.org/engage/scanopy/) into your language

## 💬 Community & Support

* **Discord**: [Join our Discord](https://discord.gg/b7ffQr8AcZ) for help and discussions
* **Issues**: [Report bugs or request features](https://github.com/scanopy/scanopy/issues/new)
* **Discussions**: [GitHub Discussions](https://github.com/scanopy/scanopy/discussions)

---

**Translations powered by Weblate**

**Built with ❤️ in NYC**

[Read more](/en/tools/github/scanopy/scanopy?expand=1)

## Categories

[Network Ma...