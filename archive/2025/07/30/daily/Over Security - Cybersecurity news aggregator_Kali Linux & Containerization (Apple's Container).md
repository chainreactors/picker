---
title: Kali Linux & Containerization (Apple's Container)
url: https://www.kali.org/blog/kali-apple-container-containerization/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-30
fetch_date: 2025-10-06T23:54:58.855762
---

# Kali Linux & Containerization (Apple's Container)

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-apple-container-containerization/images/banner-kali-apple-containerization.jpg)
Tuesday, 29 July 2025

# Kali Linux & Containerization (Apple's Container)

Table of Contents

* [Setup](#setup)
* [Running Containers](#running-containers)
  + [Alias](#alias)
* [Troubleshooting](#troubleshooting)

If you’re an Apple user, you may have heard of Apple’s upcoming feature `Containerization` during [WWDC 2025](https://www.youtube.com/watch?v=JvQtvbhtXmo).
Quick summary:

* `Container` is a CLI tool, which works with [Containerization](https://github.com/apple/containerization). This is [what end-users interact with](https://github.com/apple/container).
* `Containerization` handles creating the containers, that talks to `Virtualization.framework`.
* `Virtualization.framework` is the hypervisor API (high level), and creates a new VM per container via `Hypervisor.framework`.
* `Hypervisor.framework` is the low level hypervisor API, which uses the macOS kernel *(the hypervisor)*.

It is similar to Microsoft’s [Windows Subsystem for Linux 2 (WSL)](https://www.kali.org/docs/wsl/), where a very small lightweight virtual machine (VM) is launched in the background, so a Linux kernel can be used on a non Linux host *(WSL2 uses Hyper-V)*. *Not to be confused with WSL1, which was more like WINE!*

Its set to be publicly released for the next major OS release, macOS “Tahoe” 26, and also for macOS “Sequoia” 15 .

`Containerization` supports containers which are [“Open Container Initiative (OCI) compliant”, luckily our Kali image are](https://gitlab.com/kalilinux/build-scripts/kali-docker)!

## Setup

If the first thing we see when trying to run `container` is:

```
~ % container
zsh: command not found: container
~ %
```

…We need to install it.

---

Doing a quick check to make sure our system is supported:

```
~ % sw_vers -productVersion
15.5
~ %
~ % uname -m
arm64
~ %
```

We are using macOS 15.5, on an Apple Silicon series device (aka arm64).

We are good to go!

---

If [Homebrew](https://brew.sh/) is installed:

```
~ % brew install --cask container
==> Downloading https://github.com/apple/container/releases/download/0.2.0/container-0.2.0-installer-signed.pkg
==> Downloading from https://release-assets.githubusercontent.com/github-production-release-asset/993475914/c5fb6a42-f282-4dd7-95c2-af9b142f0ed1?sp=r&sv=2018-11-09&sr=b&spr=https&se=2025-07-17T14%3A06%3A32Z&r
######################################################################################################################################################################################################### 100.0%
==> Installing Cask container
==> Running installer for container with sudo; the password may be necessary.
Password:
installer: Package name is container-0.2.0-installer-signed
installer: Upgrading at base path /
installer: The upgrade was successful.
🍺  container was successfully installed!
~ %
```

Otherwise, we can manually grab the (signed) setup file from [github.com/apple/container](https://github.com/apple/container/releases/latest). *At the time of writing its `container-0.2.0-installer-signed.pkg`.*

---

Now when we try and run it:

```
~ % container
OVERVIEW: A container platform for macOS

USAGE: container [--debug] <subcommand>

OPTIONS:
  --debug                 Enable debug output [environment: CONTAINER_DEBUG]
  --version               Show the version.
  -h, --help              Show help information.

CONTAINER SUBCOMMANDS:
  create                  Create a new container
  delete, rm              Delete one or more containers
  exec                    Run a new command in a running container
  inspect                 Display information about one or more containers
  kill                    Kill one or more running containers
  list, ls                List containers
  logs                    Fetch container stdio or boot logs
  run                     Run a container
  start                   Start a container
  stop                    Stop one or more running containers

IMAGE SUBCOMMANDS:
  build                   Build an image from a Dockerfile
  images, image, i        Manage images
  registry, r             Manage registry configurations

OTHER SUBCOMMANDS:
  builder                 Manage an image builder instance
  system, s               Manage system components

~ %
```

…but we are not fully yet there!

---

When we use `container` to try and interact with `Containerization`, we may get:

```
~ % container ls
Error: interrupted: "internalError: "failed to list containers" (cause: "interrupted: "XPC connection error: Connection invalid"")
Ensure container system service has been started with `container system start`."
~ %
```

We can address this by starting up the service in the background:

```
~ % container system start
Verifying apiserver is running...
Installing base container filesystem...
No default kernel configured.
Install the recommended default kernel from [https://github.com/kata-containers/kata-containers/releases/download/3.17.0/kata-static-3.17.0-arm64.tar.xz]? [Y/n]: y
Installing kernel...
~ %
```

Now we are off to the races!

## Running Containers

Like [Docker](https://www.kali.org/docs/containers/using-kali-docker-images/), and [Podman](https://www.kali.org/docs/containers/using-kali-podman-images/), we can run our containers as we would expect:

```
~ % container run --rm -i -t kalilinux/kali-rolling
┌──(root㉿9ff4685f-76e1-42fa-86ba-f12e76c79843)-[/]
└─# id
uid=0(root) gid=0(root) groups=0(root)
```

The first time running, `container` will need to pull down the container image.
The default container registry is currently [DockerHub (which Kali is on)](https://hub.docker.com/u/kalilinux/).

---

We are able to-do the same features as Docker/Podman as you would expect, such as sharing a directory :

```
~ % container run --remove --interactive --tty --volume $(pwd):/mnt --workdir /mnt docker.io/kalilinux/kali-rolling:latest
┌──(root㉿4be77ff5-bd57-4076-8bf0-8e51caff047e)-[/mnt]
└─# uname -a
Linux 4be77ff5-bd57-4076-8bf0-8e51caff047e 6.12.28 #1 SMP Tue May 20 15:19:05 UTC 2025 aarch64 GNU/Linux
```

### Alias

Once everything is working as expected, we c...