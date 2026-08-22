---
title: wlctl v0.1.10
url: https://kitploit.com/en/posts/github-aashish-thapa-wlctl-v0110
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:06.346523
---

# wlctl v0.1.10

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/764/0945d0cb1648786e8faa420a118ecdef64254f792b6e9e00ba11e7314b87d763.gif)

New releaseAug 21, 2026

# wlctl v0.1.10

🛜 TUI for managing wifi/ethernet/vpn on Linux with Network Manager

Share

# wlctl

WiFi TUI for NetworkManager.

[![CI](https://github.com/aashish-thapa/wlctl/actions/workflows/ci.yaml/badge.svg)](https://github.com/aashish-thapa/wlctl/actions/workflows/ci.yaml)
[![Crates.io](https://img.shields.io/crates/v/wlctl.svg)](https://crates.io/crates/wlctl)
[![Downloads](https://img.shields.io/crates/d/wlctl.svg)](https://crates.io/crates/wlctl)
[![License](https://img.shields.io/crates/l/wlctl.svg)](https://github.com/aashish-thapa/wlctl/blob/main/LICENSE)

![demo](https://assets.kitploit.com/production/public/readmes/764/0945d0cb1648786e8faa420a118ecdef64254f792b6e9e00ba11e7314b87d763.gif)

## Why

[impala](https://github.com/pythops/impala) is a great wifi TUI but it talks to `iwd`. If your distro already runs NetworkManager (most do — GNOME, KDE, Ubuntu, Fedora, Pop, …), you can't drop impala in without ripping the stack out. wlctl keeps the impala UX and points it at NetworkManager, so it just works alongside what your DE is already doing.

## Features

* Station and Access Point modes
* WPA Enterprise (802.1X)
* Multiple adapters — pick which one to drive, switch on the fly
* VPN connections — toggle, manage autoconnect, and delete saved VPN / WireGuard profiles, like nmtui; an active tunnel shows as a badge in the top-right
* `wlctl doctor` — walks rfkill, driver, association, IP, DHCP, gateway, DNS, internet
* QR code sharing, hidden networks, speed test
* Vim keys, every binding configurable

## Install

root@kitploit:~

```
# crates.io
cargo install wlctl

# Arch (AUR)
yay -S wlctl-bin

# Nix (run without installing)
nix run github:aashish-thapa/wlctl

# from source
git clone https://github.com/aashish-thapa/wlctl && cd wlctl
cargo build --release
```

On NixOS, add the flake as an input and use `wlctl.packages.${system}.default`, or drop it into a shell with `nix shell github:aashish-thapa/wlctl`.

Needs NetworkManager running. [Nerd Fonts](https://www.nerdfonts.com/) optional, for icons.

## Usage

`wlctl` to launch the TUI. `wlctl doctor` when something's broken and you want to know which layer.

### Global

| Action | Key |
| --- | --- |
| Switch panel | `Tab` / `Shift+Tab` |
| Move | `j` `k` / arrows |
| Switch adapter mode (Station ↔ AP) | `Ctrl+R` |
| VPN connections | `v` |
| Quit | `q` / `Ctrl+C` |
| Dismiss popup | `Esc` |

### Known networks

| Action | Key |
| --- | --- |
| Connect / disconnect | `Space` or `Enter` |
| Toggle auto-connect | `t` |
| Forget network | `d` |
| Make this the internet path | `u` |
| Show all | `a` |
| QR share | `p` |
| Speed test (needs `speedtest-cli`) | `Shift+S` |

When both WiFi and Ethernet are up, the link NetworkManager is actually routing internet over is highlighted in green, and the box footer spells it out (`󰖟 Internet: WiFi · <ssid>`). Press `u` on the Ethernet row or the connected WiFi to switch the default route to it (the other link stays up).

The Device box footer shows the active adapter's LAN IP (e.g. `󰩟 wlan0 · 192.168.1.20`) so you can SSH in without running `ip addr`.

### New networks

| Action | Key |
| --- | --- |
| Connect / disconnect | `Space` or `Enter` |
| Connect to hidden | `h` |
| Filter by name | `/` |
| Show all | `a` |

Press `/` to filter the scan list by SSID as you type; `Enter` keeps the filter, `Esc` clears it.

### VPN connections (open with `v`)

| Action | Key |
| --- | --- |
| Toggle on / off | `Space` or `Enter` |
| Toggle autoconnect | `a` |
| Delete profile (confirm `y`/`n`) | `d` |
| Import a WireGuard config | `i` |
| Close | `Esc` |

The selected tunnel's assigned IP and uptime show below the list while it's up.

**Importing WireGuard configs**: press `i`, then either **paste the whole config** (most providers — Proton, Mullvad — just hand you the text) or type a path to a `.conf` file, and press Enter. wlctl parses it and creates a NetworkManager profile — no `nmcli` needed. Pasted configs are named after the server endpoint; file imports after the file name. `~` is expanded in paths. The profile is added without auto-connecting; toggle it on with Enter. OpenVPN `.ovpn` files aren't supported here — import those with `nmcli connection import type openvpn file <path>` (requires the `NetworkManager-openvpn` plugin).

### Device panel

| Action | Key |
| --- | --- |
| Adapter info | `i` |
| Toggle power | `o` |
| Doctor | `?` |

### Station mode

| Action | Key |
| --- | --- |
| Scan | `s` |

### Access Point mode

| Action | Key |
| --- | --- |
| Start AP | `n` |
| Stop AP | `x` |

## Config

`~/.config/wlctl/config.toml`. All keys rebindable.

root@kitploit:~

```
switch = "r"
mode = "station"
esc_quit = false
vpn = "v"

[device]
infos = "i"
toggle_power = "o"
doctor = "?"

[station]
toggle_scanning = "s"

[station.known_network]
toggle_autoconnect = "t"
remove = "d"
show_all = "a"
share = "p"
speed_test = "S"
prefer = "u"

[station.new_network]
show_all = "a"
connect_hidden = "h"
filter = "/"

[access_point]
start = "n"
stop = "x"
```

## vs. impala

|  | impala | wlctl |
| --- | --- | --- |
| Backend | iwd | NetworkManager |
| Coexists with default desktop network stack | no | yes |
| Multi-adapter selector | — | yes |
| VPN connection toggle | — | yes |
| `doctor` subcommand | — | yes |

## Credits

Forked from [pythops/impala](https://github.com/pythops/impala). UI and architecture are theirs.

## License

GPLv3

[Read more](/en/tools/github/aashish-thapa/wlctl?expand=1)

## Categories

[General Purpose Utilities](/en/categories/general-purpose-utilities)[Wi-Fi Auditing](/en/categories/wi-fi-auditing)[Network Security](/en/categories/network-security)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories