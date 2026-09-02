---
title: pingap v0.13.10
url: https://kitploit.com/en/posts/github-vicanso-pingap-v01310
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:10.260472
---

# pingap v0.13.10

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/12455/7628e9082e570515522f9f2ebcc1594fbb8f3feeb12fa5ff820a873eee6e1bef.png)

New releaseSep 1, 2026

# pingap v0.13.10

A reverse proxy like nginx, built on pingora, simple and efficient.

Share

# pingap

Before the pingap version is stable, no pull requests will be accepted. If you have any questions, please create a new issue first.

![Pingap Logo](https://assets.kitploit.com/production/public/readmes/12455/7628e9082e570515522f9f2ebcc1594fbb8f3feeb12fa5ff820a873eee6e1bef.png)

## Overview

Pingap is a high-performance reverse proxy powered by the [`Cloudflare Pingora`](https://github.com/cloudflare/pingora) . It simplifies operational management by enabling dynamic, zero-downtime configuration hot-reloading through concise TOML files and an intuitive web admin interface.

Its core strength lies in a powerful plugin system, offering over twenty out-of-the-box features for Authentication (JWT, Key Auth), Security (CSRF, IP/Referer/UA Restrictions), Traffic Control (Rate Limiting, Caching), Content Modification (Redirects, Content Substitution), and Observability (Request ID). This makes `Pingap` not just a proxy, but a flexible and extensible application gateway, engineered to effortlessly handle complex scenarios from API protection to modern web application deployments.

[中文说明](https://github.com/vicanso/pingap/blob/HEAD/README_zh.md) | [Documentation](https://pingap.io/) · [中文文档](https://pingap.io/zh/) | [Examples](https://github.com/vicanso/pingap/blob/HEAD/examples/README.md) | [Plugins](https://github.com/vicanso/pingap/blob/HEAD/pingap-plugin/README.md) | [Crates](https://github.com/vicanso/pingap/blob/HEAD/docs/README.md)

root@kitploit:~

```
flowchart LR
  internet("Internet") -- request --> pingap["Pingap"]
  pingap -- proxy:pingap.io/api/* --> apiUpstream["10.1.1.1,10.1.1.2"]
  pingap -- proxy:cdn.pingap.io --> cdnUpstream["10.1.2.1,10.1.2.2"]
  pingap -- proxy:/* --> upstream["10.1.3.1,10.1.3.2"]
```

## Key Features

* 🚀 High Performance & Reliability

  + Built with Rust for memory safety and top-tier performance.
  + Powered by Cloudflare Pingora, a battle-tested asynchronous networking library.
  + Supports HTTP/1.1, HTTP/2, and gRPC-web proxying.
* 🔧 Dynamic & Easy to Use

  + Zero-downtime configuration changes with hot-reloading.
  + Simple, human-readable TOML configuration files.
  + Full-featured Web UI for intuitive, real-time management.
  + Supports both file and etcd as configuration backends.
  + Supports configuration history record, can restore to the history version with one click.
* 🧩 Powerful Extensibility

  + A rich plugin system to handle common gateway tasks.
  + Advanced routing with host, path, and regex matching.
  + Built-in service discovery via static lists, DNS, or Docker labels.
  + Automated HTTPS with Let's Encrypt (supporting both HTTP-01 and DNS-01 challenges).
* 📊 Modern Observability

  + Native Prometheus metrics for monitoring (pull & push modes).
  + Integrated OpenTelemetry support for distributed tracing.
  + Highly customizable access logs with over 30 variables.
  + Detailed performance metrics, including upstream connect time, processing time, and more.

## 🚀 Getting Started

The easiest way to get started with Pingap is by using Docker Compose.

1. Create a `docker-compose.yml` file:

root@kitploit:~

```
# docker-compose.yml
version: '3.8'

services:
  pingap:
    image: vicanso/pingap:latest # For production, use a specific version like vicanso/pingap:0.12.1-full
    container_name: pingap-instance
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      # Mount a local directory to persist all configurations and data
      - ./pingap_data:/opt/pingap
    environment:
      # Configure using environment variables
      - PINGAP_CONF=/opt/pingap/conf
      - PINGAP_ADMIN_ADDR=0.0.0.0:80/pingap
      - PINGAP_ADMIN_USER=pingap
      - PINGAP_ADMIN_PASSWORD=<YourSecurePassword> # Change this!
    command:
      # Start pingap and enable hot-reloading
      - pingap
      - --autoreload
```

2. Create a data directory and run:

root@kitploit:~

```
mkdir pingap_data
docker-compose up -d
```

3. Access the Admin UI:

Your Pingap instance is now running! You can access the web admin interface at <http://localhost/pingap> with the credentials you set.

### Install the binary via curl

For Linux and macOS, you can install the latest pre-built binary to `/usr/local/bin/pingap` with one command:

root@kitploit:~

```
curl -sSL https://raw.githubusercontent.com/vicanso/pingap/main/install.sh | sh
```

Optional environment variables:

* `PINGAP_FULL=1` — install the `-full` build (all optional features enabled)
* `PINGAP_LIBC=gnu` — on Linux, use the glibc build instead of the default musl static build

root@kitploit:~

```
# Full-featured build
curl -sSL https://raw.githubusercontent.com/vicanso/pingap/main/install.sh | PINGAP_FULL=1 sh
```

Supported targets: `Linux x86_64/arm64`, `Darwin x86_64/arm64`. See the [releases page](https://github.com/vicanso/pingap/releases) for all available assets.

For more detailed instructions, including running from a binary, check out our [Documentation](https://pingap.io/).

### Start a proxy without a config file

A single command is enough to serve a domain over https and forward it to a backend:

root@kitploit:~

```
# certificate requested from let's encrypt
pingap --domain=pingap.io --upstream=192.168.1.1:3000

# or bring your own certificate
pingap --domain=pingap.io --upstream=192.168.1.1:3000 --cert=/etc/ssl/pingap.io
```

Without `--cert`, Pingap asks Let's Encrypt for a certificate through the
HTTP-01 challenge, so `pingap.io` must resolve to this host and port 80 must be
reachable from the internet. The issued certificate is kept in
`~/.pingap/acme/<domains>.toml` and reused on restart — issuing is rate limited,
so do not delete it. Everything else still comes from the command line: changing
`--upstream` takes effect on the next start without touching the certificate.

`--cert` accepts the certificate itself or the directory holding it — the common
`fullchain.pem` / `privkey.pem`, `cert.pem` / `key.pem` and `tls.crt` / `tls.key`
layouts are detected automatically, use `--key` for anything else. The listener
defaults to `0.0.0.0:443` when there is a certificate and `0.0.0.0:80` when there
is neither a certificate nor a domain, and `--addr` overrides it. `--upstream`
takes a comma separated list of backends, `--domain` a comma separated list of
hosts (omit it to serve every host over plain http).

The configuration is generated on every start, so it cannot be edited through
the admin UI: for anything beyond a single server use `--conf`, which cannot be
combined with these flags.

## Dynamic Configuration

Pingap is designed to adapt to configuration changes without downtime.

Hot Reload (--autoreload): For most changes—like updating upstreams, locations, or plugins—Pingap applies the new configuration within 10 seconds without a restart. This is the recommended mode for containerized environments.

Graceful Restart (-a or --autorestart): For fundamental changes (like modifying server listen ports), this mode performs a full, zero-downtime restart, ensuring no requests are dropped.

## 🔧 Development

root@kitploit:~

```
make dev
```

If you need a web admin, you should install nodejs and build web asssets.

root@kitploit:~

```
# generate admin web asset
cd web
npm i
cd ..
make build-web
```

## 📝 Configuration

root@kitploit:~

```
server "test" {
  addr = "127.0.0.1:6118"

  location "github-api" {
    path = "/api"
    proxy_se...