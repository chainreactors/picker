---
title: rustnet v1.6.0
url: https://kitploit.com/en/posts/github-domcyrus-rustnet-v160
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:05.135397
---

# rustnet v1.6.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/8708/ae2bf2333c88d399fefab7aaab14b19a6d27b93223202c53a616febc0935521f.png)

New releaseAug 21, 2026

# rustnet v1.6.0

Per-process network monitoring for your terminal with deep packet inspection. Cross-platform, sandboxed.

Share

# RustNet

**Per-process network monitoring for your terminal: live TCP, UDP, and QUIC connections with deep packet inspection, sandboxed by default.**

[![Built With Ratatui](https://ratatui.rs/built-with-ratatui/badge.svg)](https://ratatui.rs/)
[![Build Status](https://github.com/domcyrus/rustnet/workflows/Rust/badge.svg)](https://github.com/domcyrus/rustnet/actions)
[![Crates.io](https://img.shields.io/crates/v/rustnet-monitor.svg)](https://crates.io/crates/rustnet-monitor)
[![GitHub Stars](https://img.shields.io/github/stars/domcyrus/rustnet?style=flat&logo=github)](https://github.com/domcyrus/rustnet/stargazers)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/domcyrus/rustnet.svg)](https://github.com/domcyrus/rustnet/releases)
[![Docker Image](https://img.shields.io/badge/docker-ghcr.io-blue?logo=docker)](https://github.com/domcyrus/rustnet/pkgs/container/rustnet)

**English** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

![RustNet demo](https://assets.kitploit.com/production/public/readmes/8708/dac7699b8fd47411c7d169863fa87a61fd950657e6461a709fa3ecb79819c58c.gif)

*Real-time visibility into every connection your machine makes, who owns it, and what protocol it's speaking. No tcpdump, X11 forwarding, or root piping.*

## Features

* **Per-process attribution**: Every TCP, UDP, and QUIC connection mapped to its owning process, via eBPF on Linux, PKTAP on macOS, ETW with an automatic IP Helper fallback on Windows, and native APIs on FreeBSD. Details include PID, executable, user/group names, match confidence, and a capped parent-process chain on every platform. Wireshark and tcpdump can't do this; `netstat` / `ss` can't show live state.
* **Deep packet inspection**: Identify HTTP, HTTPS/TLS with SNI, DNS, SSH, FTP, QUIC, MQTT, BitTorrent, STUN, NTP, mDNS, LLMNR, DHCP, SNMP, SSDP, and NetBIOS, without external dissectors.
* **Annotated PCAPNG export**: `--pcapng-export` writes a Wireshark-ready capture with process, PID, direction, DPI/SNI, and GeoIP embedded as per-packet comments. Open it in Wireshark and every packet already names its owning process, with no post-processing. Classic `--pcap-export` with a JSONL sidecar for offline correlation is also available.
* **Security sandboxing**: Landlock (Linux 5.13+), Seatbelt (macOS), token privilege drop + job-object child-process block (Windows). Drops privileges immediately after libpcap initializes. See [SECURITY.md](https://github.com/domcyrus/rustnet/blob/HEAD/SECURITY.md).
* **Network analytics**: Real-time round-trip times for TCP, QUIC handshakes, DNS responses, and ICMP echo, plus TCP retransmission, out-of-order, and fast-retransmit detection.
* **Smart connection lifecycle**: Protocol-aware timeouts with white → yellow → red staleness indicators. Toggle `t` to keep historic (closed) connections visible for forensics.
* **Vim/fzf-style filtering**: `port:`, `src:`, `dst:`, `sni:`, `process:`, `state:`, `proto:`, plus regex via `/(?i)pattern/`.
* **GeoIP enrichment**: Country lookups via local MaxMind GeoLite2. No network calls.
* **LAN device identification**: MAC address and vendor (from the embedded IEEE OUI database) for on-link peers and the gateway, learned passively from ARP traffic and shown in the details pane.
* **Kubernetes attribution** (optional `kubernetes` feature): connections mapped to their pod, namespace, and container, shown in the details pane, JSON/PCAPNG exports, and the `pod:`, `ns:`, `container:` filters. Enabled in the official Docker image; on a cluster, use the [kubectl-rustnet](https://github.com/domcyrus/kubectl-rustnet) plugin to run it as an ephemeral debug pod. See [USAGE.md](https://github.com/domcyrus/rustnet/blob/HEAD/USAGE.md#--kubernetes-mode-optional-feature).
* **Cross-platform**: Linux, macOS, Windows, FreeBSD.

## Why RustNet?

RustNet fills the gap between simple connection tools (`netstat`, `ss`) and packet analyzers (`Wireshark`, `tcpdump`):

* **Process attribution**: See which application owns each connection. Wireshark cannot provide this because it only sees packets, not sockets.
* **Connection-centric view**: Track states, bandwidth, and protocols per connection in real-time
* **SSH-friendly**: TUI works over SSH so you can quickly see what's happening on a remote server without forwarding X11 or capturing traffic

RustNet complements packet capture tools. Use RustNet to see *what's making connections*. For direct Wireshark inspection, `--pcapng-export` writes live best-effort packet comments with PID/process context. For cleanup-time correlation, use `--pcap-export` plus the JSONL sidecar and optional `scripts/pcap_enrich.py`. See [PCAP Export](https://github.com/domcyrus/rustnet/blob/HEAD/USAGE.md#pcap-export) and [Comparison with Similar Tools](https://github.com/domcyrus/rustnet/blob/HEAD/ARCHITECTURE.md#comparison-with-similar-tools) for details.

Built on ratatui, libpcap, eBPF (libbpf-rs), DashMap, crossbeam, ring, MaxMind GeoLite2, and Landlock. See [ARCHITECTURE.md](https://github.com/domcyrus/rustnet/blob/HEAD/ARCHITECTURE.md#dependencies) for the full dependency breakdown.

**eBPF Enhanced Process Identification (Linux Default)**

RustNet uses kernel eBPF programs by default on Linux for enhanced performance and lower overhead process identification.

**Process Names:**

* eBPF records the process group leader's TGID and `comm` name (a kernel field limited to 16 characters) rather than the acting thread's name, so multi-threaded applications show the main process name instead of thread names like "Socket Thread"
* RustNet then re-resolves the current name via `/proc/<tgid>/comm`, recovers comm-truncated names from the executable's file name (e.g. "chromium-browse" becomes "chromium-browser"), and resolves the full executable path shown in the Details view
* Short-lived processes that exit before this enrichment runs keep the eBPF-recorded 16-character name

**Fallback Behavior:**

* When eBPF fails to load or lacks sufficient permissions, RustNet automatically falls back to standard procfs-based process identification
* Standard mode resolves names the same way via procfs scanning, but with higher CPU overhead
* eBPF is enabled by default; no special build flags needed

To disable eBPF and use procfs-only mode, build with:

root@kitploit:~

```
cargo build --release --no-default-features
```

See [ARCHITECTURE.md](https://github.com/domcyrus/rustnet/blob/HEAD/ARCHITECTURE.md) for technical information.

**Process Activity and Interface Monitoring**

RustNet combines process-level traffic accounting with real-time network interface statistics:

* **Overview Tab**: Shows active interfaces with current rates, errors, and drops
* **Activity Tab** (press `3`): Ranks processes by Egress (TX) or Ingress (RX), including retained and rolling traffic, rates, shares, connections, and destinations
* **Security Workflow**: Sort by Egress, identify an unexpected uploader, then inspect its top remote peer and retained traffic even after the connection closes
* **Interface Details** (press `i` on Activity): Shows the original comprehensive metrics for every interface
* **Cross-Platform**: Linux (sysfs), macOS/FreeBSD (getifaddrs), Windows (GetIfTable2 API)
* **Smart Filtering**: Windows automatically excludes virtual/filter adapte...