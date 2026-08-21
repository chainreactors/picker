---
title: lg-webos-kexec
url: https://kitploit.com/en/tools/github/ggfuchsi-oss/lg-webos-kexec
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:04.754410
---

# lg-webos-kexec

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/ggfuchsi-oss/lg-webos-kexec

![](https://assets.kitploit.com/production/public/tools/50576/e22b3c1eebfc24be7589a1e2200decc6868d92b3670127b3f2f6a3a6e0bc2405.png)

[Embedded Systems Security](/en/categories/embedded-systems-security)[Reverse Engineering](/en/categories/reverse-engineering)[Hardware Hacking](/en/categories/hardware-hacking)[Hardware & IoT Security](/en/categories/hardware-iot-security)[Firmware Analysis](/en/categories/firmware-analysis)

![GitHub](/providers/github.png)ggfuchsi-oss/lg-webos-kexec

# lg-webos-kexec

Boots a custom Linux kernel on rooted LG webOS TVs via kexec, with reverse-engineered SoC watchdog support, framebuffer payloads, and an initramfs kernel build flow.

[View Repository](https://github.com/ggfuchsi-oss/lg-webos-kexec)

6111 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# lg-webos-kexec

Boot a custom Linux kernel on a rooted LG webOS TV via `kexec` — in RAM, no secure-boot bypass.

> **Status: work-in-progress.** A custom kernel can be staged and reaches userspace, but it does **not** yet stay up as a usable OS.

## Target

LG 50UP81009LR (webOS 6.5, Realtek RTD2875, armv7l). Rooted via Homebrew Channel; stock signed kernel + webOS userspace are untouched.

## What's proven (verified live)

* `kexec -l` stages a (stock or from-source) kernel; `/sys/kernel/kexec_loaded` flips to `1`.
* `kexec -e` replaces the running kernel (the TV resets back to stock after).
* A from-source kernel **reaches userspace** — verified by user-mode page faults = `/sbin/init` ran real code.
* Tiny canary payloads draw to the framebuffer (ring-0 + display access confirmed).
* The entire chain runs from the stock webOS `startup.sh` — the signed bootloader / ATF / OP-TEE are never touched.

## What's still missing

* **Watchdog pet** — REVERSE-ENGINEERED + FIX WRITTEN, not yet proven in a live kexec boot. See below.

### Watchdog pet — found it (2026-08-19)

The reset is the **SoC watchdog** (TC block). The stock kernel's `micom_wdt_thread()`
holds it off with three register pokes (`drivers/rtk_kdriver/platform/tv006/intmicom.c`):

root@kitploit:~

```
TCWCR @ 0xFE062204 <- 0xA5         // unlock
TCWOV @ 0xFE062210 <- 0x0FFFFFFF   // max overflow => huge timeout
TCWTR @ 0xFE062208 <- 0x01         // kick
```

Under kexec the driver's raw `*(volatile*)0xFE062208 = 0x01` lands on an **unmapped
VA** and is a silent no-op, so the SoC watchdog fires (~10–21 s). `micom-pet.c` now
does the same pokes from userspace via `/dev/mem` (CONFIG\_DEVMEM=y), which maps
correctly, plus a `0xB1` keepalive to `/dev/sys-intmicom` as defense-in-depth.

**Status:** `micom-pet.c` rewritten, compiles with the musl toolchain, and a 5 s
benign smoke test on the live TV confirmed it runs and writes its breadcrumb
(`0x52455814` = "REX"+beat). The only remaining proof is a `kexec -e` boot that
stays up past ~21 s — that reboots the TV, so it is an attended test.

* **Display** — the panel uses tiled FBDC; raw framebuffer text isn't useful. Real output needs the VCPU RPC (drawing commands to the video engine).
* **Networking** — the stock `wlan` module vermagic must match `CONFIG_LOCALVERSION=""` to load; not yet wired into the initramfs.

## How it works (honest version)

root@kitploit:~

```
boot ROM → ATF → signed LG kernel (~2 s) → startup.sh
    → kexec -l <our zImage + dtb + initramfs>
    → kexec -e
    → OUR kernel runs in RAM (no eMMC writes)
```

Pull power = stock. It cannot brick.

## Built with AI (full disclosure)

Most of this repo was put together by **Rex** — an AI coding-agent instance — helping a human operate on their own TV, in their own living room. The AI wrote the kexec PoC, the boot chain, the framebuffer canaries, and these RE writeups. But the claims in this README were only ever made *after* the human fired the TV, looked at the screen, and confirmed it. If a claim isn't backed by a real screen/photo/uptime check from the hardware, it's not here.

> No TVs were bricked in the making of this repo. Some were temporarily confused (a kexec'd kernel with no watchdog pet resets your box after ~15 s), then power-cycled back to stock. /tmp is wiped by every reset, so the TV forgets everything we did — that's the whole point.

## Repo layout

* `rexos/` — the custom OS: boot hook, kernel build, initramfs, RexBus stub.
* `kexec-poc/` — the load-only proof-of-concept + framebuffer canary payloads.
* `docs/` — reverse-engineering writeups (boot/security, SAM app loading, surface map, luna2 schema).

## Verify it yourself (you need the exact TV: 50UP81009LR, rooted, on the LAN)

These steps reproduce what we did, on the exact hardware. Nothing is faked.

### 0. Prereqs

* LG 50UP81009LR, rooted via Homebrew Channel, root SSH enabled, on your LAN.
* The TV is `192.168.2.103` by default below; edit if yours differs.
* One-time LG K7LP GPL kernel source tree: set `KERNEL_SRC=/path/to/linux-4.4.3` (download the `03.53.45` K7LP GPL tarball from LG open-source), or symlink `~/lgtv-toolkit/kernel-src/kernel/linux-4.4.3`.

### 1. Build the toolchain + static `kexec` (no TV needed, ~2 min)

root@kitploit:~

```
git clone https://github.com/ggfuchsi-oss/lg-webos-kexec
cd lg-webos-kexec/kexec-poc && ./build.sh
```

Expected: a static ARM `kexec` binary at `kexec-arm` (168K, `file` shows `ELF 32-bit LSB ... ARM ... statically linked`).

### 2. Reproduce the safe PoC on your TV (stages + unloads — no boot)

root@kitploit:~

```
cd ../kexec-poc
./run-poc.sh 192.168.2.103 ~/.ssh/tv_key
```

Expected result:

root@kitploit:~

```
staged before      : 0
staged after load  : 1   <- kernel accepted, DTB wired, segments allocated
staged after unload: 0   <- cleared, TV untouched
```

This stages the TV's **own current kernel** via kexec and then immediately unloads it. `/sys/kernel/kexec_loaded` flips to `1` then back to `0`. No reboot, no kernel switch, nothing persists. Pull the plug = stock.

### 3. (Attended) boot your own kernel — reboots the TV

Only do this with the TV on and someone present:

root@kitploit:~

```
cd ../rexos
make                            # builds rexos-kernel.zImage + rexos-initramfs.cpio.gz into out/
./boot/rexos-kexec --load-only   # stage, do NOT fire (same safe state as step 2)
# then, when ready to actually jump:
./boot/rexos-kexec               # kexec -e -> our kernel runs in RAM (TV will reset)
```

Known-honest caveats at step 3 (not bugs I'm hiding):

* After `kexec -e`, the new kernel **reaches userspace** but the TV resets after ~10–21 s because the **micom/SOC watchdog isn't being petted**. That's the current wall, not a crash bug. `rexos/initramfs/micom-pet.c` is the daemon meant to fix this (still wiring it in).
* Display is **tiled FBDC** — there's no text console; solid-color beacons only (see `kexec-poc/canary/`). Real graphics needs the VCPU RPC path (not done).
* A wrong kernel/DTB just black-screens until power-cycle. It **cannot brick**: kexec writes only RAM, never eMMC.

### TL;DR status (honest)

* Kernel ...