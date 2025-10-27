---
title: frood, an Alpine initramfs NAS
url: https://words.filippo.io/dispatches/frood/
source: Filippo Valsorda
date: 2024-12-06
fetch_date: 2025-10-06T19:34:01.023423
---

# frood, an Alpine initramfs NAS

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

5 Dec 2024

# frood, an Alpine initramfs NAS

My NAS, [frood](https://hitchhikers.fandom.com/wiki/Frood), has a bit of a weird setup. It’s just one big initramfs containing a whole Alpine Linux system. It’s delightful and I am not sure why it’s not more common.

* As long as the bootloader can find the kernel and initramfs, the machine comes up cleanly.
* A/B deployments and rollbacks are just a matter of choosing a different boot option.
* The system is defined declaratively in the git repo that builds the initramfs.
* Importantly to me, it’s not defined in some complex DSL: if I want a file to exist at `/etc/example.conf` I put it in `root/etc/example.conf`, and the rest is done by a few hundred lines of scripts I can (and have) read.
* Configuring it doesn’t look any different than configuring any regular Alpine system.
* I can test the next deploy with a qemu oneliner.
* There are very very few moving parts.

If this already sounds appealing, you can skip to the “How it works” section below.

## But why

I’ve always liked running systems from memory: it’s fast and prevents wear on the system storage device, which is often some janky SD card, because the good drives are dedicated to the ZFS pool.

However, you immediately have the problem of how to persist configuration changes.

Alpine’s answer to this is “[diskless mode](https://wiki.alpinelinux.org/wiki/Diskless_Mode)” where any customization is kept in an overlay file. After boot, the stock system looks for a file matching `*.apkovl` in all available filesystems, applies it, and then installs any missing apk packages from a local cache.

The first problem with that is complexity: the tool to generate and manage the apkovl, [lbu(1)](https://wiki.alpinelinux.org/wiki/Alpine_local_backup), is pretty good but that process has *a lot* of moving parts. Find the apkovl, apply it, mount the filesystems in the new fstab, install the missing apks, resume the boot process. Over the past year, I had this break multiple times, either because [it couldn’t find the filesystem anymore](https://gitlab.alpinelinux.org/alpine/aports/-/issues/14624) or because the apks did not get installed. The boot process depends on the package manager!

The second problem is that I would really like the state of the system to be tracked in git. Graham Christensen has a very good pitch for declarative or immutable systems in “[Erase your darlings](https://grahamc.com/blog/erase-your-darlings/)”.

> I erase my systems at every boot.
>
> Over time, a system collects state on its root partition. This state lives in assorted directories like `/etc` and `/var`, and represents every under-documented or out-of-order step in bringing up the services.
>
> “Right, run `myapp-init`.”
>
> These small, inconsequential “oh, oops” steps are the pieces that get lost and don’t appear in your runbooks.
>
> “Just download ca-certificates to … to fix …”
>
> Each of these quick fixes leaves you doomed to repeat history in three years when you’re finally doing that dreaded RHEL 7 to RHEL 8 upgrade.
>
> “Oh, touch `/etc/ipsec.secrets` or the l2tp tunnel won’t work.”

I used to solve that by making (most) changes via Ansible, but then I had a multi-layer situation where I needed to make a change in Ansible, then deploy it, then save it with lbu to the apkovl.

There are of course many alternatives for declarative systems: from [NixOS](https://nixos.org/) (which [just doesn’t sound fun](https://bsky.app/profile/filippo.abyssdomain.expert/post/3l76qq2gwdz2h)) to [gokrazy](https://gokrazy.org/) (which is [not quite ready to ship ZFS](https://abyssdomain.expert/%40zekjur%40mas.to/113338344895999793)) to embedded toolchains like [buildroot](https://buildroot.org/) or the newer [u-root](https://u-root.org/).

Thing is though, I really like Alpine: a simple, well-packaged, lightweight, GNU-less Linux distribution. What I don’t like are its init and persistence mechanisms.

![a screenshot of four texts saying "yeah I think all my objections to Alpine are basically its flaky init and its persistency mechanism" "if I run apk at build time to make a chonky initramfs, write 300 lines to replace init, I might be golden" "all of the mkinitfs complexity and flakyness is in finding the modules, loading them, finding the root, finding the apk cache, installing it" "all of that goes poof”](https://assets.buttondown.email/images/78a269fb-a4f2-42a4-9306-a9c9700d4c83.png)

## How it works

When it boots, Linux expects an [“initramfs” image](https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html). It’s a simple [cpio](https://www.kernel.org/doc/html/latest/filesystems/ramfs-rootfs-initramfs.html#why-cpio-rather-than-tar) archive of the files that make up the very first root filesystem at boot. *Usually* the job of this system is to load enough modules to mount the real rootfs and pivot into it. Nothing stops us from putting the entire system in it, though! Who needs a rootfs?

### Building an initramfs

The starting point is [alpine-make-rootfs](https://github.com/alpinelinux/alpine-make-rootfs), which is a short (~500 lines) script meant to build a container image. It’s really 90% of what we need.

```
#!/bin/sh
set -e

wget https://raw.githubusercontent.com/alpinelinux/alpine-make-rootfs/v0.7.0/alpine-make-rootfs \
    && echo 'e09b623054d06ea389f3a901fd85e64aa154ab3a  alpine-make-rootfs' | sha1sum -c && \
    chmod +x alpine-make-rootfs

ROOTFS_DEST=$(mktemp -d)

# Stop mkinitfs from running during apk install.
mkdir -p "$ROOTFS_DEST/etc/mkinitfs"
echo "disable_trigger=yes" > "$ROOTFS_DEST/etc/mkinitfs/mkinitfs.conf"

export ALPINE_BRANCH=edge
export SCRIPT_CHROOT=yes
export FS_SKEL_DIR=root
export FS_SKEL_CHOWN=root:root
PACKAGES="$(cat packages)"
export PACKAGES
./alpine-make-rootfs "$ROOTFS_DEST" setup.sh
```

alpine-make-rootfs will copy the files from the `root` directory, install the packages from the `packages` file, and run the `setup.sh` script in a chroot.

Then, we extract the boot directory and package the rest into an initramfs archive.

```
cd "$ROOTFS_DEST"
mv boot "$IMAGE_DEST"
find . | cpio -o -H newc | gzip > "$IMAGE_DEST/initramfs-lts"
```

That’s truly very nearly it! It’s impressive how Alpine lends itself to this with practically no hacks.

### Packages

The packages we install are the usual stuff you’d install on a server. Only a few are noteworthy.

* [alpine-base](https://pkgs.alpinelinux.org/package/edge/main/x86_64/alpine-base) is the metapackage that installs apk, busybox, openrc, and a few config files.
* [linux-lts](https://pkgs.alpinelinux.org/package/edge/main/x86_64/linux-lts) is the kernel, along with its modules. I considered thinning down the modules to only the ones I needed, but it’s ultimately a lot of hacks just to save a couple hundred MB. Note there is no modloop! The modules are always available.
* [linux-firmware-i915](https://pkgs.alpinelinux.org/package/edge/main/x86_64/linux-firmware-i915) is the i915 folder of Linux firmware. Need to install at least one package providing `linux-firmware-any` (including `linux-firmware-none`) or `linux-firmware` gets installed, which installs them all.
* [intel-ucode](https://pkgs.alpinelinux.org/package/edge/main/x86_64/intel-ucode) is the microcode update. It installs a file in `/boot` that can be used as a pre-initramfs. This is in fact easier to set up than on bigger systems.
* [syslinux](https://pkgs.alpinelinux.org/package/edge/main/x86_64/syslinux) is the bootloader. Way simpler than GRUB, it installs in the filesystem partition, and then boots the kernel from that partition. This closes the loop: as long as we boot the right partition, there is no way for anything but our system to load. Nothing in the boot process needs to discover *or even give a name to* a filesystem.
* [openrc-init](https://pkgs.alpinelinux.org/package/edge/main/...