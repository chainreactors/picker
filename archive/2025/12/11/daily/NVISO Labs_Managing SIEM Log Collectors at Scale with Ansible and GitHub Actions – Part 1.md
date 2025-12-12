---
title: Managing SIEM Log Collectors at Scale with Ansible and GitHub Actions – Part 1
url: https://blog.nviso.eu/2025/12/11/managing-siem-log-collectors-at-scale-with-ansible-and-github-actions-part-1/
source: NVISO Labs
date: 2025-12-11
fetch_date: 2025-12-12T03:21:04.829067
---

# Managing SIEM Log Collectors at Scale with Ansible and GitHub Actions – Part 1

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Managing SIEM Log Collectors at Scale with Ansible and GitHub Actions – Part 1

[Tryfon Skandamis](https://blog.nviso.eu/author/tryfon-skandamis/ "Posts by Tryfon Skandamis")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [MDR](https://blog.nviso.eu/category/mdr/), [SIEM](https://blog.nviso.eu/category/siem/), [Tools](https://blog.nviso.eu/category/tools/), [Logging](https://blog.nviso.eu/category/logging/), [SOC](https://blog.nviso.eu/category/soc/)

December 11, 2025December 11, 2025
6 Minutes

This entry is part 1 in the series [Managing SIEM Log Collectors at Scale with Ansible and GitHub Actions](https://blog.nviso.eu/series/siem-log-collectors-scale-ansible-github-actions-devops/ "Managing SIEM Log Collectors at Scale with Ansible and GitHub Actions")

---

A Security Operations Center (SOC) watches an organization’s IT systems for cyber threats 24/7. It quickly finds and fixes security problems and uses Security Information and Event Management (SIEM) tools to collect and analyze alerts and logs. SIEMs depend on log Collectors servers, which gather data from many sources and send it to the SIEM. If the Collectors fail, the SIEM loses input and the SOC can miss attacks or respond too slowly.

That means Collectors’ uptime, reliability, and log availability and integrity aren’t just “nice to have”. They are essential for detecting threats quickly, getting real-time alerts, supporting investigations, and ensuring compliance. Managing dozens of Collectors across different networks is complex and challenging. Each Collector misconfiguration or downtime is not just a drift. It is a potential security and visibility gap.

In this blog series, I will show how to solve these challenges with [DevOps](https://github.com/resources/articles/what-is-devops) and [Infrastructure as Code (IaC)](https://github.com/resources/articles/what-is-infrastructure-as-code) practices. [Ansible](https://docs.ansible.com/projects/ansible/latest/network/getting_started/basic_concepts.html) and [GitHub Actions](https://github.com/features/actions) power the solution.

## The unique Collectors management challenges

Most DevOps or IaC use cases focus on efficiency, like avoiding configuration drift and making deployments scale easily. But when managing Collectors, priorities go beyond these basic advantages. The top priorities are nonstop availability, especially during chaos, and keeping investigation data reliable and correct. That makes Collectors much more sensitive and higher risk than typical infrastructure.

The biggest challenges we are facing are:

* **Evidence integrity**
  Logs moving through Collectors can end up in investigations, audits, or reports. When Collector configurations aren’t consistent or tracked, it’s hard to know where the logs came from. It’s also unclear if the data has been changed. Trust in the evidence drops quickly.
* **Detection Quality**
  What Collectors do to events, like parsing, filtering, dropping, etc., decides which logs reach the SIEM, how fast they arrive, and how they are structured. Even a small change in these configurations can stop a detection from working or slow down alerts. It can also cause false negatives that hide real attacks.
* **Attack surface**
  Collectors are usually exposed to many log sources and often sit in the middle of sensitive traffic. Poor control over configurations, credentials, or setup methods can be dangerous. They let attackers create blind spots, suppress or rewrite logs to hide their actions.

In a SOC, managing Collectors manually is not just slow and inefficient. It is also risky.

## The Solution: Let the Code Do the Work

We needed a way to manage all Collector setups and track every change. We also needed an easy way to repeat setups and automate updates or new installs.

Here’s how we did it. Instead of logging into each server individually and performing manual actions, we have:

* **Everything in one trusted place**
  All Collector configurations are stored in a central GitHub repository. Every update is versioned and documented in the commit history. So, you always know what changed and can easily roll back if something goes wrong.
* **Automated Collector Setup**
  New Collector? Add it to the Ansible inventory and make a few clicks on GitHub Actions. Then, Ansible installs everything, deploys configurations, and validates that the server is working. What used to take hours now takes minutes.
* **Fast recovery**
  If a Collector fails, it can be easily restored with a GitHub Actions workflow that runs Ansible playbooks. No manual guesswork and minimum downtime.
* **Consistency**
  Every Collector gets the exact same setup, with the exact same settings. No surprises, which makes fixing problems faster and easier when you know everything is set up the same way.
* **Configuration as Code**
  We write setup in simple, human-friendly YAML files. This is code that anyone on the team can understand and review.
* **Easy and secure connection**
  The solution uses a secure VPN to reach Collectors behind firewalls or private networks. No manual access steps are needed each time. Updates become quicker and safer.

## How It Actually Works – Architecture

![](https://blog.nviso.eu/wp-content/uploads/2025/12/Centralized-Configuration-Management-V2.4-Architecture-Flow-chart.drawio-2.png)

Here’s a simplified technical breakdown of the architecture.

**GitHub repositories**. The single source of truth with:

* One repository with Collectors’ configurations: It has log collection rules (e.g. log parsing and dropping rules) and configurations (e.g. High Availability and Load Balancing configurations).
* One repository with Ansible code: Ansible playbooks, inventory, etc.
* GitHub Actions workflows on each repository.
* All configurations and code versioned and tracked.

**Ansible control node**. A Linux central server with:

* SSH access to all managed Collectors. Establishes a secure VPN connection, so it can reach Collectors within other private networks. Ensure that all connections are logged and monitored.
* Access to a key vault (where credentials and SSH keys are stored securely).
* Access to our GitHub private repositories (to pull configurations and push updates).
* Ansible installed.
* Ansible Inventory: A list of all Collectors with their IP addresses and SSH connection details. This fil...