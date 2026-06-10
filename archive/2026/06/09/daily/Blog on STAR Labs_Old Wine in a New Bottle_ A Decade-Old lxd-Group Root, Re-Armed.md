---
title: Old Wine in a New Bottle: A Decade-Old lxd-Group Root, Re-Armed
url: https://starlabs.sg/blog/2026/06-old-wine-in-a-new-bottle-a-decade-old-lxd-group-root-re-armed/
source: Blog on STAR Labs
date: 2026-06-09
fetch_date: 2026-06-10T06:15:11.264884
---

# Old Wine in a New Bottle: A Decade-Old lxd-Group Root, Re-Armed

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
June 9, 2026
By Shi Weiming (@swing) of STAR Labs SG & guest contributor (@n132)
15 min read

# Old Wine in a New Bottle: A Decade-Old lxd-Group Root, Re-Armed

Table of Contents

* [TL;DR](#tldr)
* [It started by accident](#it-started-by-accident)
* [A group that means root](#a-group-that-means-root)
* [We were not the first to be annoyed by this](#we-were-not-the-first-to-be-annoyed-by-this)
* [What changed underneath everyone](#what-changed-underneath-everyone)
* [We checked every LTS from 18.04 to 26.04](#we-checked-every-lts-from-1804-to-2604)
  + [Precisely: what “pre-installed” means, and why 24.04 is the hinge](#precisely-what-pre-installed-means-and-why-2404-is-the-hinge)
* [The full chain](#the-full-chain)
* [A free hardening downgrade for the whole machine](#a-free-hardening-downgrade-for-the-whole-machine)
* [Disclosure](#disclosure)
* [If you run Ubuntu Server, do this today](#if-you-run-ubuntu-server-do-this-today)
* [Closing thought](#closing-thought)
* [References](#references)

## TL;DR

On a default **Ubuntu Server** install, the first user account is silently placed in the `lxd` group, and `lxd`-group membership is **root-equivalent by design**. From **24.04** onward LXD isn’t even pre-installed, yet the seeded `lxd-installer` socket (owned `root:lxd`, mode `0660`) lets any `lxd`-group user install LXD **password-free**, launch a privileged container with the host filesystem mounted, and walk straight to **root on the host, without the sudo password ever being entered**. Every individual link is documented, intended behaviour; the weakness is the **insecure default composition**. We confirmed the full chain to `euid=0` end-to-end on **20.04, 22.04, 24.04 and 26.04**. The vendor reviewed it, settled on a **won’t-fix** (a deliberate business decision), and cleared this research for publication.

**Full report and self-contained PoC (`exploit.sh`): [lxd-group-privesc-report](https://github.com/star-sg/lxd-group-privesc-report)**

## It started by accident

This one didn’t start with a target. It started with a habit.

We were testing a local privilege escalation exploit on Ubuntu 26.04. The exploit had only been adapted for the **Desktop** image so far, and before shipping it we wanted to confirm it behaved the same on **Server**.

> â md5sum ubuntu-26.04-live-server-amd64.iso
> 1e25e40d6837cdcc416805250af2e1d7 ubuntu-26.04-live-server-amd64.iso

So we pulled down the Ubuntu 26.04 Server ISO, spun it up, logged in as the first user the installer had created, and, out of pure muscle memory, the way you do a hundred times a day, typed:

```
$ id
uid=1000(user) gid=1000(user) groups=1000(user),4(adm),20(dialout),24(cdrom),...,101(lxd),27(sudo)
```

Most of that list is the usual Ubuntu furniture. But one entry caught our eye, mostly because we’d never paid attention to it before:

```
101(lxd)
```

`lxd`. On a freshly installed Server image, the default account was already a member of the `lxd` group, and we hadn’t done anything to put it there. That was enough to make us stop testing the *other* exploit and ask a simpler question: **what does being in the `lxd` group actually get you?**

A short while later the answer turned out to be: *root, without ever touching the sudo password.* And the more interesting part, the part this post is really about, is that this isn’t new. It’s been argued about for the better part of a decade, and yet the way modern Ubuntu is assembled quietly put the loaded gun back on the table after the vendor thought they’d unloaded it.

## A group that means root

The first thing we did was read LXD’s own security documentation[1](#fn:1). It does not mince words:

> *“Local access to LXD through the Unix socket always grants full access to LXD. This includes the ability to attach file system paths or devices to any instance … Therefore, you should only give such access to users who you’d trust with root access to your system.”*

That is about as clear a statement as a vendor ever makes: **`lxd`-group membership is root.** LXD’s daemon runs as root, and a member of the `lxd` group can drive that daemon through its socket. From there the path to host root is textbook:

* Create a container with `security.privileged=true`. A privileged container performs **no UID mapping**: container UID 0 is host UID 0.
* Attach a `disk` device with `source=/`, bind-mounting the host’s entire root filesystem into that container.
* Inside the container you are now *real host root* standing on top of the host’s `/`. Write a SUID-root binary, edit `/etc/shadow`, drop an SSH key for `root`. Pick your poison.

None of that is a bug in LXD. It’s the documented, intended power of the LXD socket. Which is exactly why, when we went looking, we found this argument had already been had, twice.

## We were not the first to be annoyed by this

A little searching turned up two long-closed discussions that are worth reading back to back.

**canonical/lxd issue #3844 (2017)**[2](#fn:2): *“Installation via apt-get automatically adds user to lxd group.”* The reporter pointed out that installing LXD silently dropped the default `uid:1000` user into the `lxd` group, which “effectively grant[s] full root access to an arbitrary user upon installation,” and argued it should be opt-in or at least warn the admin. **Closed**, no behavior change.

**Ubuntu Launchpad #1829071 (2019)**[3](#fn:3): *“Privilege escalation via LXD (local root exploit),”* filed by Chris Moberly, who also published the well-known write-up at Shenanigans Labs[4](#fn:4) and the `initstring/lxd_root` PoC[5](#fn:5). Same core grievance, fuller exploit. The response from LXD’s lead was a **Won’t Fix**:

> *“For the deb we won’t be changing the logic at this point and it’s in line with what’s done for libvirt, changing behavior at this point would cause more harm than good.”*

The compromise from 2019 was a documentation clarification (the `lxd` group is root-equivalent, treat it accordingly) plus one concrete mitigation: **the LXD snap stopped auto-adding users to the `lxd` group.** As far as the 2019 discussion was concerned, the loaded-by-default problem had been defused: if nobody adds you to `lxd`, the group is inert.

So this is a solved, won’t-fix, decade-old non-issue. Right?

## What changed underneath everyone

Here is where the modern install diverges from the 2019 mental model, and why we think the composition deserves a fresh look even though every individual piece is “by design.”

**Change #1: LXD is no longer pre-installed on Ubuntu Server.** Per Ubuntu Launchpad **#2051346**[6](#fn:6) (Fix Released, Jan 2024), starting with 24.04 the LXD snap is no longer pre-seeded (a consequence of the LXD 5.20 AGPL relicensing). Older Server releases shipped LXD pre-installed: the snap on 20.04 and 22.04, and the `lxd` deb further back on 18.04. 24.04 and later ship neither (we verify this release-by-release in the matrix below).

**Change #2: but the OS installer *still* puts the first user in `lxd`.** The 2019 mitigation was about the LXD *snap* no longer adding users. But on 24.04+ the first account isn’t placed in `lxd` by LXD at all; it’s placed there by the **OS installer’s default group set**, independent of whether LXD is ever installed. You can see the intended set in cloud-init’s config:

```
# /etc/cloud/cloud.cfg
default_user:
  name: ubuntu
  groups: [adm, cdrom, dip, lxd, sudo]
```

**Change #3: `lxd-installer` re-arms the path even with no LXD present.** Because the `lxc`/`lxd` commands need to keep working before the snap exists, 24.04+ Server seeds a package called **`lxd-installer`**. It ships stub wrappers at `/usr/sbin/lxc` and `/usr/sbin/lxd` plus a socket-activated installer service. Look at who owns the socket:

```
# /usr/lib/systemd/...