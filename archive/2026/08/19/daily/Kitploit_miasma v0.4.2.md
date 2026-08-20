---
title: miasma v0.4.2
url: https://kitploit.com/en/posts/github-austin-weeks-miasma-v042
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:01.541718
---

# miasma v0.4.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F12808%2F4781b9a87273912eced394e6b663dd93d30ecc1fd85f136a454560ea3667ab91.png&w=3840&q=75)

New releaseAug 19, 2026

# miasma v0.4.2

Trap AI web scrapers in an endless poison pit.

Share

# 🌀 Miasma

![No AI](https://custom-icon-badges.demolab.com/badge/No%20AI-2f2f2f?logo=non-ai&logoColor=white&logoSize=auto)
[![crates.io](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)](https://crates.io/crates/miasma)
[![downloads](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)](https://crates.io/crates/miasma)
[![Release](https://github.com/austin-weeks/miasma/actions/workflows/Release.yaml/badge.svg)](https://github.com/austin-weeks/miasma/actions/workflows/Release.yaml)
![GitHub commits since latest release](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)

![Web crawlers getting stuck in a cloud of poison miasma.](https://assets.kitploit.com/production/public/readmes/12808/53ea9eddbca68d25cbf4085762448c1cc10ee6fdf38bda837c6abf665a9d673f.png "Cover art by @delphoxlover334")

AI companies continually scrape the internet at an enormous scale, swallowing up all of its contents to use as training data for their next models. If you have a public website, *they are already stealing your work.*

*Miasma* is here to help you fight back! Spin up the server and point any malicious traffic towards it. *Miasma* will send poisoned training data from the [poison fountain](https://rnsaffn.com/poison3) alongside multiple self-referential links. It's an endless buffet of slop for the slop machines.

*Miasma* is lightning fast and has a minimal memory footprint - you should not have to waste compute resources fending off the internet's leeches.

> [!CAUTION]
> There is inherent risk in deploying this software. Please fully read [configuration](#configuration) and [disclaimer](#disclaimer) before use.

## Usage

You can run *Miasma* locally, or with the official [docker image](https://hub.docker.com/r/austinweeks/miasma).

If you would like to incorporate *Miasma* into an existing Rust server, you may also [use *Miasma* as a library](https://docs.rs/miasma/).

### Running Locally

Install with [cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html) (recommended):

root@kitploit:~

```
cargo install miasma
```

Alternatively, download a pre-built binary from [releases](https://github.com/austin-weeks/miasma/releases).

Community-maintained packages are also available for a variety of package managers:

[![Packaging status](https://repology.org/badge/vertical-allrepos/miasma.svg?exclude_unsupported=1&minversion=0.2)](https://repology.org/project/miasma/versions)

Start *Miasma* with default configuration:

root@kitploit:~

```
miasma
```

View all available [configuration options](#configuration):

root@kitploit:~

```
miasma --help
```

### Running with Docker

Run *Miasma* using the official [docker image](https://hub.docker.com/r/austinweeks/miasma):

root@kitploit:~

```
docker run --rm -p 9999:9999 austinweeks/miasma:latest
```

Pass the same [configuration flags](#configuration) you would use locally:

root@kitploit:~

```
docker run --rm -p 9999:9999 austinweeks/miasma:latest \
    --link-prefix '/naughty-bots' \
    --max-in-flight 30
```

Or, run within a docker compose cluster:

root@kitploit:~

```
services:
  miasma:
    image: austinweeks/miasma:latest
    command: ["--link-prefix", "/naughty-bots", "--max-in-flight", "30"]
    ports:
      - 9999:9999
```

## How to Trap Scrapers

Let's walk through an example of setting up a server to trap scrapers with *Miasma*. We'll pick `/naughty-bots` as our server's path to direct scraper traffic. We'll be using [*Nginx*](https://nginx.org/) as our server's reverse proxy, but the same result can be achieved with many different setups.

When we're done, scrapers will be trapped like so:

![Flow chart depicting cycle of trapped scrapers.](https://assets.kitploit.com/production/public/readmes/12808/0fc56b18661aceabe968dff1a03545577f5a28691a3a4d20e096093919935ceb.png)

### Embedding Hidden Links

Within our site, we'll include a few hidden links leading to `/naughty-bots`.

root@kitploit:~

```
<a
  href="/naughty-bots/"
  style="display: none;"
  aria-hidden="true"
  tabindex="-1"
>
  Amazing high quality data here!
</a>
```

The `style="display: none;"`, `aria-hidden="true"`, and `tabindex="-1"` attributes ensure links are totally invisible to human visitors and will be ignored by screen readers and keyboard navigation. They will **only** be visible to scrapers.

### Configuring our Nginx Proxy

Since our hidden links point to `/naughty-bots/`, we'll configure this path to proxy requests to *Miasma*. Let's assume we're running *Miasma* on port `9855`.

We'll also set up aggressive rate limiting based on the scraper's user agent to help ensure we don't accidentally DDoS ourselves.

root@kitploit:~

```
http {
  # Reserve 8MB memory for tracking user agents
  limit_req_zone $http_user_agent zone=miasma:8m rate=1r/s;

  server {
    location = /naughty-bots {
      port_in_redirect off;
      return 301 /naughty-bots/;
    }
    location /naughty-bots/ {
      # Rate limit via the 'miasma' zone with no queueing
      limit_req_status 429;
      limit_req zone=miasma burst=5 nodelay;

      # Proxy requests to Miasma
      proxy_pass http://localhost:9855/;
    }
  }
}
```

This configuration will catch all variations of the `/naughty-bots` path -> `/naughty-bots`, `/naughty-bots/`, `/naughty-bots/12345`, etc.

### Run *Miasma*

Lastly, we'll start *Miasma* and specify `/naughty-bots` as the link prefix. This instructs *Miasma* to start links with `/naughty-bots/`, which ensures scrapers are properly routed through our *Nginx* proxy back to *Miasma*.

Let's limit the number of max in-flight connections to 50. At 50 connections, we can expect 50-60 MB peak memory usage. Note that any requests exceeding this limit will immediately receive a **429** response rather than being added to a queue.

We'll also force *Miasma* to gzip compress all responses regardless of scrapers' `Accept-Encoding` header. Since gzipped responses are significantly smaller, this will help us cut down on egress costs.

While we could keep scrapers trapped forever, we'll use the link count and max depth options to let scrapers go after they consume ~100K poisoned pages. With this setup, *Miasma* will send around **250MB** of total data per scraper.

root@kitploit:~

```
miasma --link-prefix '/naughty-bots' -p 9855 -c 50 --force-gzip --link-count 5 --max-depth 8
```

### Enjoy!

Let's deploy and watch as misbehaving bots greedily eat from our endless slop machine!

![](https://raw.githubusercontent.com/austin-weeks/miasma/main/.github/images/logs.gif)

### `robots.txt`

Be sure to protect well-behaved bots and search engines from *Miasma* via your [`robots.txt`](https://developers.google.com/search/docs/crawling-indexing/robots/intro)!

root@kitploit:~

```
User-agent: *
Disallow: /naughty-bots
```

## Metrics

*Miasma* offers the ability to track scraper request counts per unique User-Agent. This can be useful for identifying which bots are hitting your site most heavily. Metrics are written to a local SQLite database file and can be viewed at an endpoint of your choosing.

## Configuration

*Miasma* can be configured via CLI flags or a [config file](https...