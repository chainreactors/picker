---
title: kern
url: https://kitploit.com/en/tools/github/getkern/kern
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:51.994102
---

# kern

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

kern — Rootless container runtime and sandbox that launches kernel-enforced OCI images in milliseconds with no daemon, featuring resource profiles, seccomp allowlists, and compose support for untrusted and AI-generated code. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/getkern/kern

![](https://assets.kitploit.com/production/public/tools/51196/cc9da3f330c4e59cc0af071648b8f188e7b3bb40f9acfb2a4f158602635b8d58-display-v1.webp)

[Cloud Infrastructure Security](/en/categories/cloud-infrastructure-security)[Container Security](/en/categories/container-security)[Dynamic Analysis (Sandboxing)](/en/categories/dynamic-analysis-sandboxing)[Security Virtualization](/en/categories/security-virtualization)[DevSecOps](/en/categories/devsecops)[AI Security](/en/categories/ai-security)

![GitHub](/providers/github.png)getkern/kern

# kern

Rootless container runtime and sandbox that launches kernel-enforced OCI images in milliseconds with no daemon, featuring resource profiles, seccomp allowlists, and compose support for untrusted and AI-generated code.

[View Repository](https://github.com/getkern/kern)

6114h 51m ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Website](https://getkern.dev)

![kern](https://assets.kitploit.com/production/public/readmes/51196/f0eaa1657ecc03fc5aa37ca0b25b52a0ac37c4bc8847eec6ea08c15e4375c695/af599375f85ab10dafd86a53d38dda4c44ec2b04f0873a064df245b242216560-display-v1.webp)

**kern:** A fast, rootless sandbox and virtual resource runtime for any workload, including untrusted and AI-generated code.

**A real, kernel-enforced container in ~3.5 ms, out of one 1.52 MB binary with no daemon.**

![Terminal: 'kern box app --image alpine -- echo hello from a real container' prints the greeting, then reports that kern started in 3.5 ms against docker run's 297 ms. A real OCI image, rootless, a 1.52 MB binary, no daemon, on an Intel i7-14700KF, Linux 7.0.](https://assets.kitploit.com/production/public/readmes/51196/cc9da3f330c4e59cc0af071648b8f188e7b3bb40f9acfb2a4f158602635b8d58/305213bceda3804b0b21cf602b3ca932f88bf49b913ed2f7fb25240aba57b2b4-display-v1.webp)

**0 RAM at rest** · no daemon, no socket, nothing to start · one static binary, `libc` its only Rust dependency

[![CI](https://github.com/getkern/kern/actions/workflows/ci.yml/badge.svg)](https://github.com/getkern/kern/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Linux%20%C2%B7%20Windows%20(WSL2)%20%C2%B7%20ARM%20boards-informational.svg)](docs/INSTALL.md)

root@kitploit:~

```
# install the release binary (static, 1.52 MB, checksum-verified by the script)
curl -fsSL https://raw.githubusercontent.com/getkern/kern/main/install.sh | sh

# a throwaway shell in a real OCI image: rootless, kernel-enforced, a few ms
kern box dev --image alpine -it -- sh
```

No native Windows: use WSL2. [Install](#install).

---

## What kern is

**One binary that manages resources, of which isolation is the first.** That is why there is no
single row for kern in a comparison table: it is a container runtime, a sandbox, a resource slicer
and a stack runner at once, in 1.52 MB with no daemon.

* **A real container.** Real OCI images: `pull`, `build` from a Dockerfile, `commit`, `push`,
  `save`/`load`. A box from an image starts in ~3.5 ms.
* **A sandbox, always rootless.** User, PID, mount, network, UTS and IPC namespaces, an overlay or
  read-only root pivoted in, a deny-by-default seccomp allowlist and cgroup v2 limits. One flag,
  `--security-profile untrusted`, is the whole hardened bundle.
* **Resource profiles, not just isolation.** CPU (`vcpu:`), memory, disk (`vdisk:`) and devices
  (`vgpio:`), declared once in a `kern.toml` and attached by name. `kern run` applies the same caps
  to a process on the host, with no sandbox at all. [docs/RESOURCES.md](https://github.com/getkern/kern/blob/HEAD/docs/RESOURCES.md)

Its entire Rust dependency tree is `libc`: JSON and OCI manifests are parsed by hand, and `pull`
shells out to the `curl` and `tar` already on the machine rather than linking a TLS stack. (1.52 MB
is the size-optimized release build; a plain `cargo install` from source is 1.91 MB.)

![Terminal demo: a kern.toml defines reusable vcpu/vdisk/vgpio (device) profiles; 'kern box train --image alpine vcpu:heavy vdisk:scratch' attaches a 4-vCPU, 8 GB, 2 GB-scratch rootless isolated slice in a few ms (docker run takes ~297 ms); 'kern run vcpu:heavy -- ffmpeg' caps a heavy transcode with no sandbox; 'kern box iot --image alpine vgpio:sensor' exposes only /dev/i2c-1 and nothing else; piping a request into 'kern box fn --image python' runs it in a fresh isolated box per request (serverless style); 'kern compose stack.toml up' brings up a multi-box stack; 'kern top' is the live TUI for boxes, profiles and volumes: CPU, memory, disk and devices, sliced per box, in one 1.52 MB static binary, no daemon.](https://raw.githubusercontent.com/getkern/kern/HEAD/assets/demo.svg)

## What kern is not

* **Not a hypervisor.** The boundary is the Linux kernel, so a kernel privilege-escalation bug is an
  escape. Docker and Podman share that condition, which is why gVisor and Firecracker exist.

  Read with the tagline, that is one line seen from both sides: untrusted and AI-generated code is
  what kern is FOR, because you chose to run it and own the blast radius (agent tool-calls, CI jobs,
  build steps, code cells). What it is not for is hostile code from strangers, multi-tenant, on a
  kernel you serve other tenants from. kern does start rootless always, where Docker's is opt-in.
* **Not free of the userns trade.** Its isolation is built on an unprivileged user namespace, a
  fertile source of kernel LPE bugs. [SECURITY.md](https://github.com/getkern/kern/blob/HEAD/SECURITY.md) states this before any claim.
* **Not a wall around what you mount in.** `-v $HOME:/host` gives the box your home directory: a
  mount is a trust decision you make, not a boundary kern enforces. `--net host` and `--privileged`
  are opt-outs by name. (The one path kern refuses to bind is its own runtime registry.)
* **Not a Docker Engine reimplementation.** It speaks Docker's *formats*, not its API: no overlay
  networks, no plugins, no Swarm. Matrix: [docs/DOCKER-COMPAT.md](https://github.com/getkern/kern/blob/HEAD/docs/DOCKER-COMPAT.md).
* **Not a Kubernetes runtime.** No CRI. Use containerd or CRI-O.
* **Not shipping GPU slices.** On the [roadmap](https://github.com/getkern/kern/blob/HEAD/ROADMAP.md), with no GPU code in this edition, so
  there is nothing here to trust or to attack yet.

What it does not know or does not do yet is in [OPEN\_ITEMS.md](https://github.com/getkern/kern/blob/HEAD/OPEN_ITEMS.md) rather than left for
you to find.

## Install

kern needs a Linux kernel with unprivileged user namespaces and cgroup v2. It runs on **Linux, WSL2
and ARM boards** (Raspberry Pi · Jetson · Arduino UNO Q); there is **no native Windows** build...