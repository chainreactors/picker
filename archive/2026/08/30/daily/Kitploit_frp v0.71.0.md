---
title: frp v0.71.0
url: https://kitploit.com/en/posts/github-fatedier-frp-v0710
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:46.940843
---

# frp v0.71.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/3770/0f836cc321c1fd65416940b5e12ca576cccc68f12d61ff045a09582ccfff74c1.png)

New releaseAug 30, 2026

# frp v0.71.0

A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet.

Share

# frp

[![Build Status](https://circleci.com/gh/fatedier/frp.svg?style=shield)](https://circleci.com/gh/fatedier/frp)
[![GitHub release](https://img.shields.io/github/tag/fatedier/frp.svg?label=release)](https://github.com/fatedier/frp/releases)
[![GitHub Releases Stats](https://img.shields.io/github/downloads/fatedier/frp/total.svg?logo=github)](https://somsubhra.github.io/github-release-stats/?username=fatedier&repository=frp)

[README](https://github.com/fatedier/frp/blob/HEAD/README.md) | [中文文档](https://github.com/fatedier/frp/blob/HEAD/README_zh.md)

## Sponsors

frp is an open source project with its ongoing development made possible entirely by the support of our awesome sponsors. If you'd like to join them, please consider [sponsoring frp's development](https://github.com/sponsors/fatedier).

### Gold Sponsors

[![](https://assets.kitploit.com/production/public/readmes/3770/9dea6d22dea95b2cea07185ed4ffaf0b0a0ba5c9fc43ab754e67abbcd3251d2a.jpg)

**The complete IDE crafted for professional Go developers**](https://jb.gg/frp)

[![](https://assets.kitploit.com/production/public/readmes/3770/80690d9c287f9f4c53a9fb9daba4e7b4923f44e596c2b094e9f9362747ac72e5.jpg)

**The sovereign cloud that puts you in control**

An open source, self-hosted alternative to public clouds, built for data ownership and privacy](https://github.com/beclab/Olares)

## Recall.ai - API for meeting recordings

If you're looking for a meeting recording API, consider checking out [Recall.ai](https://www.recall.ai/?utm_source=github&utm_medium=sponsorship&utm_campaign=fatedier-frp),

an API that records Zoom, Google Meet, Microsoft Teams, in-person meetings, and more.

## What is frp?

frp is a fast reverse proxy that allows you to expose a local server located behind a NAT or firewall to the Internet. It currently supports **TCP** and **UDP**, as well as **HTTP** and **HTTPS** protocols, enabling requests to be forwarded to internal services via domain name.

frp also offers a P2P connect mode.

## Table of Contents

* [Development Status](#development-status)
  + [About V2](#about-v2)
* [Architecture](#architecture)
* [Example Usage](#example-usage)
  + [Access your computer in a LAN network via SSH](#access-your-computer-in-a-lan-network-via-ssh)
  + [Multiple SSH services sharing the same port](#multiple-ssh-services-sharing-the-same-port)
  + [Accessing Internal Web Services with Custom Domains in LAN](#accessing-internal-web-services-with-custom-domains-in-lan)
  + [Forward DNS query requests](#forward-dns-query-requests)
  + [Forward Unix Domain Socket](#forward-unix-domain-socket)
  + [Expose a simple HTTP file server](#expose-a-simple-http-file-server)
  + [Enable HTTPS for a local HTTP(S) service](#enable-https-for-a-local-https-service)
  + [Expose your service privately](#expose-your-service-privately)
  + [P2P Mode](#p2p-mode)
* [Features](#features)
  + [Configuration Files](#configuration-files)
  + [Using Environment Variables](#using-environment-variables)
  + [Split Configures Into Different Files](#split-configures-into-different-files)
  + [Server Dashboard](#server-dashboard)
  + [Client Admin UI](#client-admin-ui)
    - [Dynamic Proxy Management (Store)](#dynamic-proxy-management-store)
  + [Monitor](#monitor)
    - [Prometheus](#prometheus)
  + [Authenticating the Client](#authenticating-the-client)
    - [Token Authentication](#token-authentication)
    - [OIDC Authentication](#oidc-authentication)
  + [Encryption and Compression](#encryption-and-compression)
    - [TLS](#tls)
  + [Hot-Reloading frpc configuration](#hot-reloading-frpc-configuration)
  + [Get proxy status from client](#get-proxy-status-from-client)
  + [Only allowing certain ports on the server](#only-allowing-certain-ports-on-the-server)
  + [Port Reuse](#port-reuse)
  + [Bandwidth Limit](#bandwidth-limit)
    - [For Each Proxy](#for-each-proxy)
  + [TCP Stream Multiplexing](#tcp-stream-multiplexing)
  + [Support KCP Protocol](#support-kcp-protocol)
  + [Support QUIC Protocol](#support-quic-protocol)
  + [Connection Pooling](#connection-pooling)
  + [Load balancing](#load-balancing)
  + [Service Health Check](#service-health-check)
  + [Rewriting the HTTP Host Header](#rewriting-the-http-host-header)
  + [Setting other HTTP Headers](#setting-other-http-headers)
  + [Get Real IP](#get-real-ip)
    - [HTTP X-Forwarded-For](#http-x-forwarded-for)
    - [Proxy Protocol](#proxy-protocol)
  + [Require HTTP Basic Auth (Password) for Web Services](#require-http-basic-auth-password-for-web-services)
  + [Custom Subdomain Names](#custom-subdomain-names)
  + [URL Routing](#url-routing)
  + [TCP Port Multiplexing](#tcp-port-multiplexing)
  + [Connecting to frps via PROXY](#connecting-to-frps-via-proxy)
  + [Port range mapping](#port-range-mapping)
  + [Client Plugins](#client-plugins)
  + [Server Manage Plugins](#server-manage-plugins)
  + [SSH Tunnel Gateway](#ssh-tunnel-gateway)
  + [Virtual Network (VirtualNet)](#virtual-network-virtualnet)
* [Feature Gates](#feature-gates)
  + [Available Feature Gates](#available-feature-gates)
  + [Enabling Feature Gates](#enabling-feature-gates)
  + [Feature Lifecycle](#feature-lifecycle)
* [Related Projects](#related-projects)
* [Contributing](#contributing)
* [Donation](#donation)
  + [GitHub Sponsors](#github-sponsors)
  + [PayPal](#paypal)

## Development Status

frp is currently under development. You can try the latest release version in the `master` branch, or use the `dev` branch to access the version currently in development.

We are currently working on version 2 and attempting to perform some code refactoring and improvements. However, please note that it will not be compatible with version 1.

We will transition from version 0 to version 1 at the appropriate time and will only accept bug fixes and improvements, rather than big feature requests.

### About V2

The complexity and difficulty of the v2 version are much higher than anticipated. I can only work on its development during fragmented time periods, and the constant interruptions disrupt productivity significantly. Given this situation, we will continue to optimize and iterate on the current version until we have more free time to proceed with the major version overhaul.

The concept behind v2 is based on my years of experience and reflection in the cloud-native domain, particularly in K8s and ServiceMesh. Its core is a modernized four-layer and seven-layer proxy, similar to envoy. This proxy itself is highly scalable, not only capable of implementing the functionality of intranet penetration but also applicable to various other domains. Building upon this highly scalable core, we aim to implement all the capabilities of frp v1 while also addressing the functionalities that were previously unachievable or difficult to implement in an elegant manner. Furthermore, we will maintain efficient development and iteration capabilities.

In addition, I envision frp itself becoming a highly extensible system and platform, similar to how we can provide a range of extension capabilities based on K8s. In K8s, we can customize development according to enterprise needs, utilizing features such as CRD, controller mode, webhook, CSI, and CNI. In frp v1, we introduced the concept of server plugins, which implemented some basic extensibility. However, it relies on a simple HTTP protocol and requires u...