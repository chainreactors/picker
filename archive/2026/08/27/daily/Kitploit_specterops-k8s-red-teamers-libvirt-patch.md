---
title: specterops-k8s-red-teamers-libvirt-patch
url: https://kitploit.com/en/tools/github/gregdurys/specterops-k8s-red-teamers-libvirt-patch
source: Kitploit
date: 2026-08-27
fetch_date: 2026-08-28T13:36:43.695035
---

# specterops-k8s-red-teamers-libvirt-patch

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/gregdurys/specterops-k8s-red-teamers-libvirt-patch

![](https://assets.kitploit.com/production/public/tools/53190/45213fdaaf51a43666c755fbc0ed472e8443c39067a7712ca322baef4e35cc25-display-v1.webp)

[Cloud Security](/en/categories/cloud-security)[Learning & Education](/en/categories/education)[Red Teaming](/en/categories/red-teaming)[Labs & Practice](/en/categories/labs-practice)

![GitHub](/providers/github.png)gregdurys/specterops-k8s-red-teamers-libvirt-patch

# specterops-k8s-red-teamers-libvirt-patch

Unofficial libvirt patch for the free SpecterOps Kubernetes for Red Teamers lab

[View Repository](https://github.com/gregdurys/specterops-k8s-red-teamers-libvirt-patch)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

10415 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

Share

# SpecterOps Kubernetes for Red Teamers Libvirt Patch

An unofficial libvirt and QEMU/KVM patch for the free SpecterOps Kubernetes for
Red Teamers course. The original network addresses, Kubernetes topology, Mythic
callbacks and lab behaviour remain unchanged.

## Why?

Because running VirtualBox on Linux is like bringing a portable generator to a
house that is already connected to the grid; you're paying twice for something
the kernel already gives you, while adding another hypervisor and kernel-module
attack surface. KVM is part of Linux, while QEMU and libvirt provide the
virtual-machine and management layers around it. This avoids adding a separate
third-party hypervisor module stack to a Linux host.

VirtualBox solves the course's cross-platform distribution problem; libvirt
solves the Linux host problem. The original VirtualBox provider remains untouched
for Windows and macOS users, while this patch lets Linux users run the same lab
on KVM.

This repository intentionally does not contain the SpecterOps lab archive or a
copy of its source tree. Obtain the original material through the official course:

1. Register or sign in at
   [Kubernetes for Red Teamers](https://academy.specterops.io/kubernetes-for-red-teamers?next=%2Fkubernetes-for-red-teamers%2F521336).
2. Open Lab Infrastructure and Configuration.
3. Download Lab Environment Files.

## Repository contents

root@kitploit:~

```
README.md
ARCHITECTURE.md
LICENSE
NOTICE.md
UPSTREAM_SHA256SUMS
docs/
  libvirt-lab-provisioned.png
patches/
  libvirt.patch
  SHA256SUMS
```

`patches/libvirt.patch` contains only the changes needed to add libvirt support.
It does not contain the original archive, internal conversion plans, review
reports, local test harness, generated credentials, or VM state.

## Requirements

* A Linux host with QEMU/KVM and libvirt;
* Vagrant 2.4 or newer;
* The `vagrant-libvirt` plugin;
* Enough resources to run four lab VMs, which use 8 vCPUs and 16 GiB RAM
  between them
* A bidirectional synced-folder backend selected automatically or explicitly.

## Installation

Download `k8s-attack-path-part-1-lab-assets.tar.gz` from the
[Lab Infrastructure and Configuration section of the free SpecterOps course](https://academy.specterops.io/kubernetes-for-red-teamers?next=%2Fkubernetes-for-red-teamers%2F521336).

Extract the original lab files:

root@kitploit:~

```
mkdir -p ~/kubernetes-for-red-teamers
cd ~/Downloads
tar xzvf k8s-attack-path-part-1-lab-assets.tar.gz -C ~/kubernetes-for-red-teamers
```

Clone the patch repository:

root@kitploit:~

```
cd ~
git clone https://github.com/GregDurys/specterops-k8s-red-teamers-libvirt-patch.git
```

Verify the patch:

root@kitploit:~

```
cd ~/specterops-k8s-red-teamers-libvirt-patch
sha256sum -c patches/SHA256SUMS
```

The result should be:

root@kitploit:~

```
patches/libvirt.patch: OK
```

Optionally, verify the downloaded archive against the version used to test this
patch:

root@kitploit:~

```
cd ~/Downloads
sha256sum -c ~/specterops-k8s-red-teamers-libvirt-patch/UPSTREAM_SHA256SUMS
```

If the checksum differs, SpecterOps may have updated the lab files.

Apply the patch:

root@kitploit:~

```
cd ~/kubernetes-for-red-teamers
git apply --check ~/specterops-k8s-red-teamers-libvirt-patch/patches/libvirt.patch
git apply ~/specterops-k8s-red-teamers-libvirt-patch/patches/libvirt.patch
```

Validate the configuration:

root@kitploit:~

```
vagrant validate
```

The result should be:

root@kitploit:~

```
Vagrantfile validated successfully.
```

The patch adds its own lab usage README and architecture document to the
extracted directory.

Start the lab from the patched course directory:

root@kitploit:~

```
vagrant up --provider=libvirt
```

The Vagrantfile automatically disables parallel startup because later machines
consume files generated by the control plane.

![Mythic developer and noaccess callbacks alongside the completed libvirt provisioning and four running VMs](https://assets.kitploit.com/production/public/readmes/53190/45213fdaaf51a43666c755fbc0ed472e8443c39067a7712ca322baef4e35cc25/7b9b29cf57cd9fa28dede41a98e38a1e0e8c7e1015890a048cef3e00bf082c2e-display-v1.webp)

## Lab topology

The functional topology shown in the course diagram is preserved:

| Diagram element | Libvirt conversion |
| --- | --- |
| Teamserver | `192.168.56.10`, DNS `teamserver` |
| Control plane | `192.168.56.20`, API server on TCP 6443 |
| Worker 1 | `192.168.56.30` |
| Worker 2 | `192.168.56.31` |
| Mythic UI | TCP 7443 |
| Callback port | TCP 8081 |
| TLS registry | TCP 5000, trusted by the cluster nodes |
| Mythic callbacks | Developer and noaccess callbacks retained |
| Host access | Vagrant forwards ports 7443 and 8081 to the teamserver |
| Private lab traffic | Remains on the isolated `192.168.56.0/24` network |
| Internet access | Retained through adapter 1 |
| Hostname resolution | Retained across all four VMs |
| Code-server and lab manifests | Unchanged from upstream |

The network implementation has one deliberate difference:

* VirtualBox gives each VM an independent NAT engine on adapter 1.
* Libvirt connects all four VMs to the dedicated `k8s-workshop-mgmt` NAT
  network, normally `192.168.157.0/24`.

The libvirt VMs can therefore communicate through adapter 1, whereas
VirtualBox's separate NAT adapters do not provide that path. Kubernetes, Calico,
Mythic callbacks, the registry and lab hostname resolution are explicitly pinned
to adapter 2, so the lab topology remains unchanged.

Read [ARCHITECTURE.md](https://github.com/gregdurys/specterops-k8s-red-teamers-libvirt-patch/blob/HEAD/ARCHITECTURE.md) for details of the topology, collision
handling and synced-folder rationale.

## Post-provisioning checks

After provisioning completes:

root@kitploit:~

```
vagrant status
vagrant ssh control-plane-1 -c 'kubectl get nodes -o wide'
vagrant port --guest 7443 teamserver
curl --insecure --head https://192.168.56.10:7443
```

All three Kubernetes nodes should be `Ready` with internal addresses `.20`,
`.30`, and `.31`. The Mythic login page should be reachable through the forwarded
host port and directly at `https://192.168.56.10:7443`. The two course callbacks
should appear in Mythic as described by the official cours...