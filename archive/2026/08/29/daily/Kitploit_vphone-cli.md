---
title: vphone-cli
url: https://kitploit.com/en/tools/github/lakr233/vphone-cli
source: Kitploit
date: 2026-08-29
fetch_date: 2026-08-30T07:42:01.724987
---

# vphone-cli

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

vphone-cli — Boot and manage virtual iPhones on Apple Silicon with firmware patching, jailbreak variants, and security research features for iOS testing and analysis. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/lakr233/vphone-cli

![](https://assets.kitploit.com/production/public/tools/53458/baa413a8104308f42ad8341722a6b8cb25de1c2b48c948c626544dbb0f0b762f-display-v1.webp)

[iOS Security](/en/categories/ios-security)[Exploitation](/en/categories/exploitation)[Security Virtualization](/en/categories/security-virtualization)[Penetration Testing](/en/categories/penetration-testing)[Mobile Security](/en/categories/mobile-security)[Firmware Analysis](/en/categories/firmware-analysis)

![GitHub](/providers/github.png)lakr233/vphone-cli

# vphone-cli

Boot and manage virtual iPhones on Apple Silicon with firmware patching, jailbreak variants, and security research features for iOS testing and analysis.

[View Repository](https://github.com/lakr233/vphone-cli)

8.8k1.2k661 day ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

**[🇰🇷한국어](./docs/README_ko.md)** | **[🇯🇵日本語](./docs/README_ja.md)** | **[🇨🇳中文](./docs/README_zh.md)** | **🇬🇧English**

# vphone-cli

Boot a virtual iPhone via Apple's Virtualization.framework using PCC research VM infrastructure.

![poc](https://assets.kitploit.com/production/public/readmes/53458/baa413a8104308f42ad8341722a6b8cb25de1c2b48c948c626544dbb0f0b762f/22ee69924cfb493bf1729a005cee55e543b0454ad0ad7ee7486273971cdcabba-display-v1.webp)

## Prerequisites

**Host:**

* Apple Silicon
* macOS 15+ (Sequoia)
* Xcode + iOS SDK (cross-compiles the guest daemon)
* [SIP/AMFI relaxation to allow private PV=3 entitlements with unsigned-binary](#sipamfi-relaxation)

**Dependencies:**

root@kitploit:~

```
brew install [email protected] aria2 wget gnu-tar openssl@3 ldid-procursus sshpass keystone cmake libusb ipsw zstd
```

## Install

root@kitploit:~

```
brew install zqxwce/tap/vphone-cli
```

## Build

root@kitploit:~

```
git clone --recurse-submodules https://github.com/Lakr233/vphone-cli.git

./scripts/setup_tools.sh      # install deps, build toolchain submodules, create the Python venv
./scripts/build.sh            # build + sign vphone-cli, bundle the .app, cross-compile vphoned

cd .build/vphone-cli.app/Contents/MacOS/
vphone-cli --help
```

## Quick Start

One command creates a VM end-to-end (download → patch → DFU restore → CFW install → first boot):

root@kitploit:~

```
vphone-cli vm create myphone -V jb        # -V / --variant

vphone-cli vm launch myphone
```

## Commands

`vphone-cli vm create` runs the whole pipeline; the individual steps below let you drive it manually or re-run one stage.

### Manage

root@kitploit:~

```
vphone-cli vm list                         # list VMs (--json for scripting)
vphone-cli vm info myphone                  # show one VM
vphone-cli vm new myphone                   # create an empty bundle (cpu/mem/disk options)
vphone-cli vm config myphone --cpu 8 --memory 8192
vphone-cli vm clone myphone myphone-2       # fast APFS clone, fresh device identity
vphone-cli vm export myphone --out myphone.tzst   # zstd fast by default (--max = xz -9); --out may be a dir (auto-names <vm>.tzst/.txz); skips restore dir + staging files
vphone-cli vm import myphone.tzst --name restored
vphone-cli vm rename myphone iphone16
vphone-cli vm delete iphone16
```

### Build a VM manually (what `vm create` automates)

root@kitploit:~

```
vphone-cli vm new myphone                              # 1. empty bundle
vphone-cli fw prepare myphone --iphone-version 26.1     # 2. download + merge IPSWs
vphone-cli fw patch myphone --variant jb                # 3. patch the boot chain

vphone-cli vm launch myphone --dfu &                    # 4. boot into DFU (background)
vphone-cli restore myphone --get-shsh                   #    fetch SHSH
vphone-cli restore myphone                              #    DFU restore
vphone-cli vm stop myphone                              #    stop the DFU boot

vphone-cli cfw install myphone --variant jb             # 5. install CFW (host-mount; asks for sudo)
vphone-cli vm launch myphone                            # 6. first boot
```

Update to a newer iOS by pointing `fw prepare` at an IPSW: `--iphone-source /path/to.ipsw --cloudos-source /path/to.ipsw`.

## Firmware Variants

Five patch variants with increasing security bypass — pass one to `--variant`:

See [`research/0_binary_patch_comparison.md`](https://github.com/lakr233/vphone-cli/blob/HEAD/research/0_binary_patch_comparison.md) for the per-component breakdown.

## Running & Connecting

* **SSH (jailbreak):** `ssh -p 22222 mobile@<vm-ip>` (password `alpine`)
* **SSH (regular/dev):** `ssh -p 22222 root@<vm-ip>`
* **VNC:** `vnc://<vm-ip>:5901`

## Locations

Everything vphone-cli creates lives under `~/.vphone/` — kept outside the repo and the `.app` so the signed bundle stays portable. Redirect the whole tree with `$VPHONE_ROOT`:

Precedence: the per-item overrides (`$VPHONE_LIBRARY_ROOT`, `$VPHONE_VENV_DIR`) win over `$VPHONE_ROOT`, which wins over the `~/.vphone` default. The `ipsws/`, `tools/`, and `debs/` caches always sit directly under whichever root is active.

## SIP/AMFI Relaxation

**Option A — fully disable SIP, then disable AMFI via boot-arg (most permissive).**

In Recovery (long-press power → Terminal):

root@kitploit:~

```
csrutil disable
csrutil allow-research-guests enable
```

Then reboot into macOS and set the AMFI boot-arg (needs SIP fully off to take effect):

root@kitploit:~

```
sudo nvram boot-args="amfi_get_out_of_my_way=1 -v"   # reboot after
```

**Option B — keep SIP on (debug-only relaxed), then allowlist the binary with amfidont** (leaves AMFI enabled system-wide).

In Recovery:

root@kitploit:~

```
csrutil enable --without debug
csrutil allow-research-guests enable
```

Then reboot into macOS and:

root@kitploit:~

```
vphone-amfidont         # .build/vphone-cli.app/Contents/Resources/vphone-amfidont for local builds
```

## Tested Environments

## FAQ

**`zsh: killed ./vphone-cli`** — AMFI/debug restrictions aren't bypassed; see [Prerequisites](#prerequisites) (`amfi_get_out_of_my_way=1` or `amfidont`).

**`Virtualization is not available on this hardware`** — your Mac is itself a VM; PV=3 guest boot can't nest. Use a non-nested macOS 15+ host.

**Stuck on "Press home to continue"** — connect via VNC and right-click (two-finger click) to simulate the home button.

**System apps won't install** — during iOS setup, don't pick Japan or the EU as your region (extra regulatory checks the VM can't satisfy); pick e.g. United States.

**App crashes on launch with `EXC_GUARD` / `GUARD_TYPE_MACH_PORT`** — re-patch with `vphone-cli fw patch <name> --variant <v> --force-exc-guard`, then re-restore/install ([#291](https://github.com/Lakr233/vphone-cli/issues/291)). Always on for iOS 18 bases.

**Install a `.ipa`/`.tipa`** — use the running VM's Install menu (drag-drop or file picker).

**`cfw install` hangs re-signing a system binary (e.g. `Campo`), mem...