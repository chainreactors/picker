---
title: radmin-vpn-linux v1.1.0
url: https://kitploit.com/en/posts/github-baptisterajaut-radmin-vpn-linux-v110
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:03:27.971824
---

# radmin-vpn-linux v1.1.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/13598/7504653724040af45e281f46e3af4226b418dd71ade3dd85ce848009f9e1b807.png)

New releaseAug 20, 2026

# radmin-vpn-linux v1.1.0

Run Radmin VPN on Linux via Wine — custom driver, TAP bridge, zero packet loss

Share

# Radmin VPN for Linux

Run [Radmin VPN](https://www.radmin-vpn.com/) on Linux via Wine. Join VPN networks, see peers, play games — all without a Windows VM.

> I did not build this because it was easier than a VM. I built it because I thought it was easier than a VM.

**AI-assisted code.** Built collaboratively between a human and Claude (Anthropic). The driver, hooks, and bridge were written with extensive AI-assisted reverse engineering of Radmin VPN's undocumented driver protocol using Ghidra. **This works, but comes with no guarantees.** Not affiliated with Famatech. Radmin VPN is proprietary — download it yourself from [radmin-vpn.com](https://www.radmin-vpn.com/). Use at your own risk.

## How it works

Radmin VPN's Windows service talks to an NDIS miniport driver for its virtual network adapter. Wine doesn't support NDIS, so we replace the driver with our own implementation that bridges to a Linux TAP device. A hook DLL handles Wine compatibility issues (adapter naming, registry permissions). The result is a fully functional Radmin VPN client running natively under Wine.

root@kitploit:~

```
Linux app ← TAP (radminvpn0) ← tap_bridge ← FIFO ← rvpnnetmp.sys (Wine driver) ← RvControlSvc.exe
```

## Quick start (AppImage, recommended)

Grab `RadminVPN-Linux-x86_64.AppImage` from the [latest release](https://github.com/baptisterajaut/radmin-vpn-linux/releases/latest). Nothing to install — Wine is bundled.

> **Release candidates** (e.g. `v1.0.0-rc1`) are published as GitHub *pre-releases*. The `latest` link above always points to the newest *stable* build, so pre-releases won't appear there — grab those from the [full releases list](https://github.com/baptisterajaut/radmin-vpn-linux/releases).

root@kitploit:~

```
chmod +x RadminVPN-Linux-x86_64.AppImage
./RadminVPN-Linux-x86_64.AppImage
```

On first launch it will prompt for the Radmin VPN installer (download `Radmin_VPN_*.exe` from [radmin-vpn.com](https://www.radmin-vpn.com/) first). A terminal opens with progress, and one sudo password prompt is needed for TAP setup.

Persistent state (wineprefix, MAC, logs) lives in `~/.local/share/radmin-vpn-linux/`.

## Prerequisites (source build / non-AppImage)

* **Wine** >= 11.0 (tested on Wine 11.5 Arch Linux and on Wine 11.6 Ubuntu 24.04)
* **mingw-w64** cross-compilers (`i686-w64-mingw32-gcc`, `x86_64-w64-mingw32-gcc`) — for building from source
* **iconv** (glibc) — for service log parsing
* **sudo** access — for TAP device creation and routing
* **TUN/TAP kernel support** — usually built-in, check with `modprobe tun`
* **Radmin VPN installer** — download from [radmin-vpn.com](https://www.radmin-vpn.com/). **Must be a 2.0.x build** (developed against 2.0.4899.9). Radmin VPN **1.4 is not supported** — it registers and opens the adapter but never finishes connecting under the Wine shim, leaving the GUI stuck at "Connecting...".

### Arch Linux

root@kitploit:~

```
sudo pacman -S wine mingw-w64-gcc
```

### Ubuntu/Debian

root@kitploit:~

```
sudo apt install wine64 wine32 gcc-mingw-w64
```

## Source quick start

root@kitploit:~

```
git clone https://github.com/baptisterajaut/radmin-vpn-linux.git
cd radmin-vpn-linux

# Option A: download pre-built binaries from GitHub Releases
mkdir -p build
TAG=$(curl -sI https://github.com/baptisterajaut/radmin-vpn-linux/releases/latest | grep -i location | grep -oP 'v[\d.]+')
curl -sL "https://github.com/baptisterajaut/radmin-vpn-linux/releases/download/${TAG}/radmin-vpn-linux-${TAG}.tar.gz" \
  | tar xz -C build/

# Option B: build from source
make

# Download Radmin VPN installer from https://www.radmin-vpn.com/
./run.sh --installer ~/Downloads/Radmin_VPN_*.exe
```

On subsequent runs, just:

root@kitploit:~

```
./run.sh
```

### Command-line flags

| Flag | Description |
| --- | --- |
| `--installer <path>` | Path to the `Radmin_VPN_*.exe` installer (first run only). |
| `--no-ui` | Run the service without launching the Radmin GUI. |
| `--no-broadcast-routes` | Don't add the broadcast/multicast → TAP routes. |
| `--filter-ui` | Launch the optional GTK4 packet-filter UI (off by default). |
| `--fix-chat` | Patch Qt's `qwindows.dll` to fix the chat-window crash under Wine (off by default). |

Both `--filter-ui` and `--fix-chat` are opt-in. The filter UI needs the `rvpn_filter_ui`
binary (built by `make`); the chat fix needs `patch_qwindows_font.py` and a Python 3 interpreter.

## Headless / server modes

Two extra launchers run Radmin VPN without a local desktop — for a VPS or datacenter host. Both install and configure exactly like `run.sh` (same wineprefix, same `--installer` first-run flow, same TAP bridge); they only differ in how the GUI is reached.

### `run_datacenter.sh` — GUI over the browser

Runs the real Radmin GUI on a virtual display (Xvfb) and serves it through VNC + noVNC, so you can configure your networks from a browser and then leave it running.

root@kitploit:~

```
sudo apt install -y xvfb x11vnc websockify novnc   # or: make install-datacenter-deps
./run_datacenter.sh --installer ~/Downloads/Radmin_VPN_*.exe
```

| Flag | Default | Description |
| --- | --- | --- |
| `--vnc-port <n>` | `5900` | Port for the x11vnc server. |
| `--web-port <n>` | `6080` | Port for the noVNC web endpoint. |
| `--vnc-password <pw>` | *(none)* | Password for the VNC / web session. |
| `--web-bind <addr>` | `127.0.0.1` | Address noVNC listens on. |

By default noVNC binds to `127.0.0.1`, so it's only reachable through an SSH tunnel:

root@kitploit:~

```
ssh -L 6080:localhost:6080 your-vps    # then open http://localhost:6080/vnc.html
```

To expose it publicly, pass `--web-bind 0.0.0.0` **together with** `--vnc-password` — otherwise anyone who reaches the web port lands on an unauthenticated, root-capable desktop. The script prints a loud warning if you bind publicly without a password.

### `run_vps.sh` — service only, fixed GUID

Starts the service headless with a hardcoded TAP GUID (no Wine WMI required) and no GUI at all. If a custom network enumerator (`rv_net_enum.exe`, not shipped in this repo) is present one directory up, it is launched; otherwise the service just runs until you Ctrl+C. Only `--installer` is accepted.

root@kitploit:~

```
./run_vps.sh --installer ~/Downloads/Radmin_VPN_*.exe
```

## Building from source

Requires `mingw-w64` cross-compilers. Pre-built binaries are available from [Releases](https://github.com/baptisterajaut/radmin-vpn-linux/releases) (built by CI on each tagged version) if you don't want to install mingw.

root@kitploit:~

```
make          # build everything to build/
make clean    # remove build artifacts
```

Produces:

* `build/rvpnnetmp.sys` — Wine kernel driver (64-bit PE)
* `build/adapter_hook.dll` — Hook DLL (32-bit PE)
* `build/rvpn_launcher.exe` — DLL injector (32-bit PE)
* `build/netsh.exe` — netsh replacement (32-bit PE, installed to SysWOW64)
* `build/netsh64.exe` — netsh replacement (64-bit PE, installed to System32)
* `build/drvinst.exe` — no-op stub replacing Radmin's real NDIS driver installer (issue #12)
* `build/tap_bridge` — native Linux TAP bridge
* `build/rvpn_dnsfix.so` — native LD\_PRELOAD shim, preloaded into the service only
* `build/rvpn_filter_ui` — optional GTK4 packet-filter UI (`--filter-ui`)

### Building the AppImage

root@kitploit:~

```
make
./packaging/build-appimage.sh       # → packaging/dist/RadminVPN-Linux-x86_64.AppIma...