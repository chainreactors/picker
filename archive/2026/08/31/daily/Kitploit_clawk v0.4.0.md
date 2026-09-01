---
title: clawk v0.4.0
url: https://kitploit.com/en/posts/github-clawkwork-clawk-v040
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:40.428493
---

# clawk v0.4.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/7237/56b97e90b5af190abc2e1de5cc7b8ad4e835a05dd6e7a1e2f3416d78021a6a8b.gif)

New releaseAug 31, 2026

# clawk v0.4.0

Give coding agents a disposable Linux VM, not your laptop

Share

![clawk](https://assets.kitploit.com/production/public/readmes/7237/193b3f67135a6e0f90c36ec914e8c5fd73a4d6181ea56b6ba75e042e6335dc72.png)

*Give a coding agent its own disposable Linux machine, not yours.*

[![CI](https://github.com/clawkwork/clawk/actions/workflows/ci.yml/badge.svg)](https://github.com/clawkwork/clawk/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Go 1.26+](https://img.shields.io/badge/Go-1.26+-00ADD8?logo=go&logoColor=white)](go.mod)
![Platform: macOS · Linux (experimental)](https://img.shields.io/badge/platform-macOS%20%C2%B7%20Linux%20(experimental)-lightgrey)

**[Install](#install)** · **[Quickstart](#quickstart)** ·
**[Why a VM?](#why-a-vm)** · **[How it works](#how-it-works)** ·
**[Compared to](#compared-to)** · **[FAQ](#faq)** · **[Docs](https://github.com/clawkwork/clawk/blob/HEAD/docs/)**

A coding agent is only useful when you let it actually *do* things: install
packages, run the code it writes, start servers, use the network. On your own
machine that leaves two bad options. You approve every command (and babysit a
prompt every few seconds), or you run `--dangerously-skip-permissions` and hope
nothing important is one `rm -rf` or one leaked token away.

clawk is a third option. `cd` into a repo, type `clawk`, and Claude Code (or
Codex, or pi, or a shell) is working inside a disposable Linux VM (your code mounted
in, root in the guest, no permission prompts) while your files, your keychain,
and the rest of your machine stay out of reach. **The agent gets its own
machine instead of yours.**

![clawk demo: clawk boots a VM and attaches claude; a blocked attempt to send data to an unknown server shows up in clawk network denials; clawk attach resumes the sandbox later](https://assets.kitploit.com/production/public/readmes/7237/56b97e90b5af190abc2e1de5cc7b8ad4e835a05dd6e7a1e2f3416d78021a6a8b.gif)

*One command to a working agent; an attempt to send data to an
unknown server, blocked by the network allow-list; `clawk attach`
resumes the session later.*

The boundary isn't a rule in a prompt the agent could be talked out of. It's
a separate machine, and the only openings are the ones you mounted. From a
shell inside a sandbox:

root@kitploit:~

```
$ curl https://tracker.evil.example   # not on the allow-list: blocked
curl: (7) Failed to connect to tracker.evil.example port 443 after 2 ms: Connection refused

$ cat ~/.ssh/id_rsa                   # your keys never entered the VM
cat: /home/agent/.ssh/id_rsa: No such file or directory

$ git push                            # ...yet this works: ssh-agent is forwarded
Enumerating objects: 5, done.
```

To be honest about the limits, the allow-list blocks connections to *unknown*
servers, not to ones you've allowed: github.com is pre-allowed and the
forwarded ssh-agent can push, so treat anything the agent can read as
something it could publish. The
[security model](#security-model-and-its-limits) spells this out.

And if the agent wrecks the VM, run `clawk destroy && clawk`: a fresh VM, same
repo, and `--resume` restores the conversation.

> [!IMPORTANT]
> **Pre-1.0 and moving fast.** Expect breaking changes between releases and
> the occasional rough edge; things can and will break. Please file issues;
> that feedback is shaping 1.0.

## Highlights

* **Let the agent do anything.** It runs in a disposable VM with a restricted
  network, so `rm -rf`, package installs, and untrusted code can't reach your
  host, your files, or anything you didn't explicitly share.
* **Working in one command.** `cd` into a repo and run `clawk`. No
  Dockerfile, devcontainer, or setup file. First boot builds a rootfs from
  your image; every boot after takes seconds.
* **Break it without losing anything.** Destroy and recreate freely; your
  code and the agent's conversations live on the host. Only the disposable
  VM disk is lost.
* **A real Linux box, your toolchain.** Any OCI image is the rootfs: a full
  OS with exactly the tools your project needs. No Docker daemon required.
* **Secrets stay on your machine.** Outbound traffic is allow-listed and your
  ssh-agent is forwarded, so `git push` works without keys entering the VM.
* **A sandbox per project or ticket.** Run several at once; multi-repo
  tickets get a git worktree per repo with coordinated PRs. Idle VMs
  automatically release memory and suspend to disk, so a forgotten sandbox
  costs (almost) nothing.

## Why a VM?

clawk is a general-purpose local environment for autonomous coding agents.
The VM is the point: it's a whole machine the agent can own, not a process
wrapped in policy on the one you're using.

* **A separate kernel.** The guest runs its own Linux kernel, so the host
  filesystem isn't hidden behind deny rules; it was never mounted.
* **A conventional Linux environment.** Standard kernel, standard userland,
  `/dev/kvm`-shaped expectations, so tools behave the way their docs say,
  without a syscall-filter surprise.
* **Root in the guest.** Install system packages, edit `/etc`, load a module,
  bind a privileged port. It's the agent's box to reconfigure.
* **A disposable lifecycle.** Cheap to break and quick to recreate; a wrecked
  VM is one `clawk destroy && clawk` away, with your repo and conversations
  untouched on the host.
* **Stronger separation from the host.** Isolation rests on the hypervisor
  boundary rather than on getting a process-sandbox policy exactly right.

That combination runs workloads a restricted process sandbox tends to fight
you on:

* installing packages and native dependencies;
* running background services (databases, queues, dev servers);
* executing untrusted builds and tests at full speed;
* using system-level Linux tooling that expects a real machine;
* and, with a KVM-enabled guest kernel on supported hardware, container and
  Kubernetes dev workflows such as Docker or Kind running *inside* the
  sandbox. This is opt-in and hardware-gated; see
  [Images](https://github.com/clawkwork/clawk/blob/HEAD/docs/images.md#guest-kernel-override) for the exact requirements.

None of this is the *product*; clawk is for local agent work in general.
Docker and Kubernetes are just the sharpest example of "needs a real machine,
not a sandboxed process."

## Install

Requires macOS 14+ on Apple silicon. (Linux is supported via firecracker and
currently experimental — start with
**[docs/linux-quickstart.md](https://github.com/clawkwork/clawk/blob/HEAD/docs/linux-quickstart.md)**, which covers setup,
the workflow, and the gaps. This README is macOS-first.)

root@kitploit:~

```
brew install clawkwork/tap/clawk
```

**From source** (contributors, or if you don't use Homebrew), needs Go 1.26+:

root@kitploit:~

```
git clone https://github.com/clawkwork/clawk && cd clawk
make install
```

Either way there's no extra host tooling: no Docker, no qemu, no sudo. The
hypervisor is Apple's Virtualization.framework, linked into the binary, and the
release binaries carry the in-guest agent prebuilt — so a Go toolchain is only
needed if you build from source, in which case you have one. First run probes
for anything missing and offers to fix it.

**Uninstall:** `clawk destroy` your sandboxes, `rm -rf ~/.clawk`, then remove
the binary with `brew uninstall clawk` (or delete it from `$GOBIN` for a
source install). Nothing else was installed: there are no launchd jobs; the
...