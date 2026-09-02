---
title: cloudflared v2026.8.3
url: https://kitploit.com/en/posts/github-cloudflare-cloudflared-202683
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:11.030671
---

# cloudflared v2026.8.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/10327/3514894714d058c38b4cc0fa5d3da2303bf2d0e8c3560cdf7182a341936bf6a0.png)

New releaseSep 1, 2026

# cloudflared v2026.8.3

Secure tunneling daemon that proxies traffic from the Cloudflare network to private origins, enabling zero-trust network access without opening firewall ports. Supports Layer 4 TCP traffic for SSH, RDP, and more.

Share

# Cloudflare Tunnel client

Contains the command-line client for Cloudflare Tunnel, a tunneling daemon that proxies traffic from the Cloudflare network to your origins.
This daemon sits between Cloudflare network and your origin (e.g. a webserver). Cloudflare attracts client requests and sends them to you
via this daemon, without requiring you to poke holes on your firewall --- your origin can remain as closed as possible.
Extensive documentation can be found in the [Cloudflare Tunnel section](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel) of the Cloudflare Docs.
All usages related with proxying to your origins are available under `cloudflared tunnel help`.

You can also use `cloudflared` to access Tunnel origins (that are protected with `cloudflared tunnel`) for TCP traffic
at Layer 4 (i.e., not HTTP/websocket), which is relevant for use cases such as SSH, RDP, etc.
Such usages are available under `cloudflared access help`.

You can instead use [WARP client](https://developers.cloudflare.com/warp-client/)
to access private origins behind Tunnels for Layer 4 traffic without requiring `cloudflared access` commands on the client side.

## Before you get started

Before you use Cloudflare Tunnel, you'll need to complete a few steps in the Cloudflare dashboard: you need to add a
website to your Cloudflare account. Note that today it is possible to use Tunnel without a website (e.g. for private
routing), but for legacy reasons this requirement is still necessary:

1. [Add a website to Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/)
2. [Change your domain nameservers to Cloudflare](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/)

## Installing `cloudflared`

Downloads are available as standalone binaries, a Docker image, and Debian, RPM, and Homebrew packages. You can also find releases [here](https://github.com/cloudflare/cloudflared/releases) on the `cloudflared` GitHub repository.

* You can [install on macOS](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#macos) via Homebrew or by downloading the [latest Darwin amd64 release](https://github.com/cloudflare/cloudflared/releases)
* Binaries, Debian, and RPM packages for Linux [can be found here](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#linux)
* A Docker image of `cloudflared` is [available on DockerHub](https://hub.docker.com/r/cloudflare/cloudflared)
* You can install on Windows machines with the [steps here](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#windows)
* To build from source, install the required version of go, mentioned in the [Development](#development) section below. Then you can run `make cloudflared`.

User documentation for Cloudflare Tunnel can be found at <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>

## Creating Tunnels and routing traffic

Once installed, you can authenticate `cloudflared` into your Cloudflare account and begin creating Tunnels to serve traffic to your origins.

* Create a Tunnel with [these instructions](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/)
* Route traffic to that Tunnel:
  + Via public [DNS records in Cloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/dns/)
  + Or via a public hostname guided by a [Cloudflare Load Balancer](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/public-load-balancers/)
  + Or from [WARP client private traffic](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/)

## TryCloudflare

Want to test Cloudflare Tunnel before adding a website to Cloudflare? You can do so with TryCloudflare using the documentation [available here](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/).

## Deprecated versions

Cloudflare currently supports versions of cloudflared that are **within one year** of the most recent release. Breaking changes unrelated to feature availability may be introduced that will impact versions released more than one year ago. You can read more about upgrading cloudflared in our [developer documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/update-cloudflared/).

For example, as of January 2023 Cloudflare will support cloudflared version 2023.1.1 to cloudflared 2022.1.1.

## Development

### Requirements

* [GNU Make](https://www.gnu.org/software/make/)
* [capnp](https://capnproto.org/install.html)
* [go >= 1.26](https://go.dev/doc/install)
* Optional tools:
  + [capnpc-go](https://pkg.go.dev/zombiezen.com/go/capnproto2/capnpc-go)
  + [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports)
  + [golangci-lint](https://github.com/golangci/golangci-lint)
  + [gomocks](https://pkg.go.dev/go.uber.org/mock)

### Build

To build cloudflared locally run `make cloudflared`

### Test

To locally run the tests run `make test`

### Linting

To format the code and keep a good code quality use `make fmt` and `make lint`

### Mocks

After changes on interfaces you might need to regenerate the mocks, so run `make mocks`

### Git Hooks

To avoid CI errors, you can install pre-push hooks that run linting and tests before each push:

root@kitploit:~

```
make install-hooks
```

This will configure git to use the hooks in `.githooks/` that run `make fmt-check lint test` before each push.

[Read more](/en/tools/github/cloudflare/cloudflared?expand=1)

## Categories

[Cloud Infrastructure Security](/en/categories/cloud-infrastructure-security)[Network Security](/en/categories/network-security)[Cloud Security](/en/categories/cloud-security)[Identity & Access Management (IAM)](/en/categories/identity-access-management)[Remote Access Tool](/en/categories/remote-access-tool)[API Security](/en/categories/api-security)

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