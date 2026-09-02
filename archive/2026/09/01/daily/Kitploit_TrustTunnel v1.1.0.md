---
title: TrustTunnel v1.1.0
url: https://kitploit.com/en/posts/github-trusttunnel-trusttunnel-v110
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:08.186264
---

# TrustTunnel v1.1.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12037/0dd585cd3248b54f3f667ccd4627bcf7984db7a7e427f2df3dca7fce8e7907a1.png)

New releaseSep 1, 2026

# TrustTunnel v1.1.0

Open-source VPN protocol that tunnels TCP, UDP, and ICMP traffic over HTTPS, bypassing DPI and throttling. Features split tunneling, SOCKS5 proxy, custom DNS, and cross-platform clients.

Share

![TrustTunnel](https://cdn.adguardcdn.com/website/github.com/TrustTunnel/logo_light.svg)

[Clients](#clients)
· [App store](https://agrd.io/ios_trusttunnel)
· [Play store](https://agrd.io/android_trusttunnel)

---

## Table of Contents

* [Introduction](#introduction)
* [Server Features](#server-features)
* [Client Features](#client-features)
* [Quick start](#quick-start)
  + [Endpoint setup](#endpoint-setup)
    - [Install the endpoint](#install-the-endpoint)
    - [Updating the endpoint](#updating-the-endpoint)
    - [Endpoint configuration wizard](#endpoint-configuration-wizard)
    - [Let's Encrypt certificate lifecycle](#lets-encrypt-certificate-lifecycle)
    - [Running endpoint](#running-endpoint)
    - [Export client configuration](#export-client-configuration)
  + [Client setup](#client-setup)
    - [Install the client](#install-the-client)
    - [Updating the client](#updating-the-client)
    - [Client configuration wizard](#client-configuration-wizard)
    - [Running client](#running-client)
* [Clients](#clients)
* [See also](#see-also)
* [Roadmap](#roadmap)
* [License](#license)

---

## Introduction

TrustTunnel is a modern, open-source VPN protocol originally developed by
[AdGuard VPN](https://adguard-vpn.com) and now available for anyone to use and audit.

It delivers fast, secure, and reliable VPN connections without the usual trade-offs.
By design, TrustTunnel traffic is indistinguishable from regular HTTPS traffic,
allowing it to bypass throttling and deep-packet inspection while maintaining
strong privacy protections.

The TrustTunnel project includes the VPN endpoint (this repository), the
[library and CLI for the client](https://github.com/TrustTunnel/TrustTunnelClient),
and the [GUI application](https://github.com/TrustTunnel/TrustTunnelFlutterClient).

## Server Features

* **VPN Protocol**: The library implements the VPN protocol compatible
  with HTTP/1.1, HTTP/2, and QUIC. By mimicking regular network traffic, it
  becomes impossible to detect and block.
* **Flexible Traffic Tunneling**: TrustTunnel can tunnel TCP, UDP, and ICMP
  traffic to and from the client.
* **Platform Compatibility**: The server is compatible with Linux and macOS.
  The client is available for Android, Apple, Windows, and Linux.

---

## Client Features

* **Traffic Tunneling**: The library is capable of tunneling TCP, UDP, and ICMP
  traffic from the client to the endpoint and back.
* **Cross-Platform Support**: It supports Linux, macOS, and Windows platforms,
  providing a consistent experience across different operating systems.
* **System-Wide Tunnel and SOCKS5 Proxy**: It can be set up as a system-wide
  tunnel, utilizing a virtual network interface, as well as a SOCKS5 proxy.
* **Split Tunneling**: The library supports split tunneling, allowing users to
  exclude connections to certain domains or hosts from routing through the VPN
  endpoint, or vice versa, only routing connections to specific domains or hosts
  through the endpoint based on an exclusion list.
* **Custom DNS Upstream**: Users can specify a custom DNS upstream, which is
  used for DNS queries routed through the VPN endpoint.

---

## Quick start

### Endpoint setup

#### Install the endpoint

An installation script is available that can be run with the following command:

root@kitploit:~

```
curl -fsSL https://raw.githubusercontent.com/TrustTunnel/TrustTunnel/refs/heads/master/scripts/install.sh | sh -s -
```

The installation script will download the prebuilt package from the latest
GitHub release for the appropriate system architecture and unpack it to
`/opt/trusttunnel`. The output directory could be overridden by specifying
`-o DIR` flag at the end of the command above.

If you want to install a specific version (instead of the latest), use `-V <version>`:

root@kitploit:~

```
curl -fsSL https://raw.githubusercontent.com/TrustTunnel/TrustTunnel/refs/heads/master/scripts/install.sh | sh -s - -V <version>
```

> [!NOTE]
> Prebuilt packages are available for `linux-x86_64`, `linux-aarch64`, and
> `macos-universal` (Intel and Apple Silicon) architectures.

#### Updating the endpoint

The installation script always installs the latest available version.
So, to update your installation, run the install command again:

root@kitploit:~

```
curl -fsSL https://raw.githubusercontent.com/TrustTunnel/TrustTunnel/refs/heads/master/scripts/install.sh | sh -s -
```

This re-runs the installer and replaces the binaries in the installation
directory (`/opt/trusttunnel` by default, or the directory you specified with `-o DIR`).

> [!NOTE]
> Don't forget to stop the endpoint before updating:
>
> root@kitploit:~
>
> ```
> sudo systemctl stop trusttunnel
> ```
>
> To start the endpoint again after updating:
>
> root@kitploit:~
>
> ```
> sudo systemctl start trusttunnel
> ```

#### Endpoint configuration wizard

Please refer to the [CONFIGURATION.md](https://github.com/trusttunnel/trusttunnel/blob/HEAD/CONFIGURATION.md) for the more detailed
documentation on how to configure the endpoint.

The installation directory contains `setup_wizard` binary that helps generate
the config files required for the endpoint to run:

root@kitploit:~

```
cd /opt/trusttunnel/
./setup_wizard -h
```

The setup wizard supports interactive mode, so you could run it and it will ask
for data required for endpoint configuration.

root@kitploit:~

```
cd /opt/trusttunnel/
sudo ./setup_wizard
```

> [!NOTE]
> `sudo` is required to manage TLS certificates properly.

The wizard will ask for the following fields, some of them have the default
values you could safely use:

* **The address to listen on** - specify the address for the endpoint to listen
  on. Use `0.0.0.0:443` for native deployments (HTTPS on all interfaces).
  If you run with Docker port mapping `443:8443`, set it to `0.0.0.0:8443`.
* **Path to credentials file** - path where the user credentials for
  authorization will be stored.
* **Username** - the username the user will use for authorization.
* **Password** - the user's password.
* **Add one more user?** - select `yes` if you want to add more users, or `no`
  to continue the configuration process.
* **Path to the rules file** - path to store the filtering rules.
* **Connection filtering rules** - you can add rules that the endpoint will use
  to allow or disallow user's connections based on:

  + Client IP address
  + TLS random prefix
  + TLS random with mask

  Press `n` to allow all connections.
* **Path to a file to store the library settings** - path to store the main
  endpoint configuration file.
* **Certificate selection** - choose how to obtain a TLS certificate:

  + **Issue a Let's Encrypt certificate** (requires a public domain) - the
    setup wizard has built-in ACME support and can automatically obtain a free,
    publicly trusted certificate from Let's Encrypt. You'll need:
    - A registered domain pointing to your server's IP address
    - Port 80 accessible from the internet (for HTTP-01 challenge), or
    - Ability to add DNS TXT records (for DNS-01 challenge)
  + **Generate a self-signed certificate** - suitable for testing or when using
    the CLI client only. Note: The Flutter client does not support self-signed
    certificates **yet**.
  + **Provide path to existing certi...