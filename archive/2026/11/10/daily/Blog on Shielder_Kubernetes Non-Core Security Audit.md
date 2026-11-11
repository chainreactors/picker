---
title: Kubernetes Non-Core Security Audit
url: https://www.shielder.com/blog/2026/11/kubernetes-non-core-security-audit/
source: Blog on Shielder
date: 2026-11-10
fetch_date: 2026-11-11T08:35:39.022863
---

# Kubernetes Non-Core Security Audit

[![shielder logo homepage](https://www.shielder.com/img/logoshielder.svg)](https://www.shielder.com/ "homepage")

* [Home](https://www.shielder.com/ "Home")
* [Company](https://www.shielder.com/company "Company")
* [Services](https://www.shielder.com/services "Services")
* [Advisories](https://www.shielder.com/advisories "Advisories")
* [Blog](https://www.shielder.com/blog "Blog")
* [Careers](https://www.shielder.com/careers "Careers")
* [Contacts](https://www.shielder.com/contacts "Contacts")
* ENG

  [ENG](https://www.shielder.com/blog/2026/11/kubernetes-non-core-security-audit/ "ENG")
  [ITA](https://www.shielder.com/it/blog/2026/11/kubernetes-non-core-security-audit/ "ITA")

# Kubernetes Non-Core Security Audit

## TL;DR

In February 2025, Shielder was hired by [OSTIF](https://ostif.org/) to perform a security audit of multiple projects in the Kubernetes non-core ecosystem.

**Today, we are publishing the [full report](https://github.com/ShielderSec/public-reports/blob/main/2026/%5BOSTIF%5D%20Kubernetes%20Non-Core%20-%20Report%20v1.2.pdf) in our [dedicated repository](https://github.com/ShielderSec/public-reports/)**.

**â ï¸â ï¸â ï¸ Disclaimer â ï¸â ï¸â ï¸**
A number of the findings remain open. This was coordinated with the Kubernetes Security Response Committee (SRC), the SIG Security Third-Party Security Audit group, and the relevant maintainers. We encourage anyone using the affected components to review the report for suggested mitigations and workarounds. Most remediation is happening in public issues and pull requests - contributions are very welcome.

## Context

By “non-core” in Kubernetes, we don’t mean a formal definition. It simply indicates Kubernetes components and subprojects that were deemed out-of-scope in previous security audits that focused on some of the core components of Kubernetes, such as the kube-apiserver or the kubelet.

For this audit, the [Kubernetes SIG Security](https://www.kubernetes.dev/community/community-groups/sigs/security/) divided the scope into “high-priority” (16 entries) and “low-priority” (~80 entries) projects, based on perceived criticality and wealth of existing documentation.

This priority indicated the amount of effort and attention a project should receive: high-priority projects needed to be reviewed in full, mapping the attack surface, auditing design choices and implementation. For low-priority projects, instead, the goal was to perform a lightweight security audit, moving to code auditing only in case relevant threats were identified.

The list of projects in scope is contained in the public report.

### Methodology

Auditing such a scope can be challenging for an audit team. First, while being all part of the Kubernetes ecosystem, the projects vary significantly in complexity and domain, ranging from platform-specific system components, like the Windows CSI Driver or the Linux cgroups v2 integration, to standalone control plane extensions, like the Cluster API.
Moreover, many of these projects are maintained in separate repositories, with different threat models, documentation strategies, and deployment scenarios, which makes it impossible to test them dynamically in the same lab (e.g., a Kubernetes Cluster).

To systematically handle the audit, the Shielder team opted for the following methodology:

1. Depth over breadth: rather than “target-hopping”, each researcher was assigned to a single project for a reasonable amount of time, so that they could get comfortable with the codebase, setup a lab for dynamic testing, and report findings in a clear way.
2. Triage of the low-priority entries: each component in the low-priority list was quickly examined against two questions: 1) is it related to a high-priority component already in scope? If so, it is merged into that part of the audit and 2) does it touch a relevant attack surface or introduce real threats? If not, it is quickly reviewed for outstading issues, and set aside. Notably, by following this methodology, a project initially included in the low-priority list, k0ps, was “promoted” to a full security review, as it was deemed to be a sensible component with a high attack surface.
3. A separate threat model and lab for each component: each component got its own threat model and its own test environment.

By adopting this methodology, it was possible to *“divide and conquer”*, treating the big activity as a collection of multiple, more focused and smaller gigs.

## Findings

While auditing, the team reported nineteen (19) vulnerabilities throughout the projects in scope. Of the 19 findings, 4 are High, 5 Medium, 7 Low and 3 Informational.

The current status of the reported findings is reported below (each #N number refers to the ID in the report):

* **Fixed (4):** #7, #14, #15, #20
* **Fix pending (4):** #4, #8, #13, #18
* **Under triage (5):** #6, #9, #10, #11, #12
* **Suggested for public issues (5):** #1, #3, #5, #16
* **Won’t fix (2):** #2, #17

The full list of findings, alongside the threat model and attack surface for each component, is available in the public report. This section showcases some of the findings included there, that we believe are the most relevant to the security posture of the Kubernetes ecosystem.

### [Windows Nodes] NTLM coercion via sym-linking the subPath field

When declaring volume mounts in a Pod specification, a field called `subPath` allows specifying a subdirectory of the volume to mount, rather than its root. To make sure that the `subPath` does not escape the volume via symbolic links (<https://nvd.nist.gov/vuln/detail/cve-2017-1002101>), the kubelet has to follow the symlink chain to resolve its final target, and ensure that it is within the volume’s root directory.

On Windows nodes, this link resolution is performed by the kubelet via the Powershell `Get-Item` cmdlet. This is the typical situation of NTLM coercion: by creating a `subPath` symbolic link that points to an UNC path (i.e., `\\IP\Share`), it is possible to trick the node into initiating an NTLM authentication towards a controlled host, obtaining the NetNTLMv2 hash that can be potentially cracked offline or used for relaying attacks (the Windows red-teaming literature has a wealth of techniques in this sense).

This was assigned a CVE (CVE-2026-76654), and a fix was released to remediate the issue. However, reproducing the PoC on a patched Windows node still triggers the NTLM authentication towards the attacker machine, thus the maintainers have been informed and are currently investigating the issue.

For kubernetes administrator using Windows in their clusters, it is suggested to restrict outbound NTLM connections going out from nodes.

### [Image Builder] Hardcoded credentials in Windows OVA/Nutanix images

When auditing the [Image Builder](https://github.com/kubernetes-sigs/image-builder), the team discovered a hardcoded password baked into some specific build scripts (OVA, Nutanix) used to set the default Windows Administrator password. This meant deploying Windows nodes in clusters with a public administrator password, leaving publicly exposed hosts open to remote compromise.

A CVE (CVE-2025-7342) was assigned to this issue, and it was fixed by <https://github.com/kubernetes-sigs/image-builder/pull/1800>.

### [Cluster API] Path Traversal in Cluster API Flavor Template Generation

One of the interfaces to the [Cluster API](https://cluster-api.sigs.k8s.io/) is its CLI, `clusterctl`. For instance, operators can create new clusters by invoking the `clusterctl generate cluster` command. One of the options supported by the commands, `--flavor`, allows to select a specific deployment target for a given provider (for instance, a deployment target in the AWS CAPI provider turns the IPv6 support on).

The Cluster API expects providers to host cluster provisioning resource files on GitHub. The option mentioned above, `--flavor`, is used in the `clusterctl` machinery to retrieve YAML resources from the repository. However, t...