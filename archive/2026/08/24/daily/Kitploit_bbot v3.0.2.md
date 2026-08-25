---
title: bbot v3.0.2
url: https://kitploit.com/en/posts/github-blacklanternsecurity-bbot-v302
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:58:59.005842
---

# bbot v3.0.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/668/17569ba95dd320f86c75e4ffe4ac0a6e5c3cd4653bee3b3ec8dcd4f71a03cd63.gif)

New releaseAug 24, 2026

# bbot v3.0.2

The recursive internet scanner for hackers. 🧡

Share

[![bbot_banner](https://assets.kitploit.com/production/public/readmes/668/3f7d75070b188fb745d38f275e40c53cbb7e2f57b3eccc109c7e7a2b62cff0e0.png)](https://github.com/blacklanternsecurity/bbot)

[![Python Version](https://img.shields.io/badge/python-3.10+-FF8400)](https://www.python.org) [![License](https://img.shields.io/badge/license-AGPLv3-FF8400.svg)](https://github.com/blacklanternsecurity/bbot/blob/dev/LICENSE) [![PyPi Downloads](https://static.pepy.tech/personalized-badge/bbot?right_color=orange&left_color=grey)](https://pepy.tech/project/bbot) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Tests](https://github.com/blacklanternsecurity/bbot/actions/workflows/tests.yml/badge.svg?branch=stable)](https://github.com/blacklanternsecurity/bbot/actions?query=workflow%3A%22tests%22) [![Codecov](https://codecov.io/gh/blacklanternsecurity/bbot/branch/dev/graph/badge.svg?token=IR5AZBDM5K)](https://codecov.io/gh/blacklanternsecurity/bbot) [![Discord](https://img.shields.io/discord/859164869970362439)](https://discord.com/invite/PZqkgxu5SA)

### **BEE·bot** is a multipurpose scanner inspired by [Spiderfoot](https://github.com/smicallef/spiderfoot), built to automate your **Recon**, **Bug Bounties**, and **ASM**!

<https://github.com/blacklanternsecurity/bbot/assets/20261699/e539e89b-92ea-46fa-b893-9cde94eebf81>

*A BBOT scan in real-time - visualization with [VivaGraphJS](https://github.com/blacklanternsecurity/bbot-vivagraphjs)*

## Installation

root@kitploit:~

```
# stable version
pipx install bbot

# bleeding edge (dev branch)
pipx install --pip-args '\--pre' bbot
```

*For more installation methods, including [Docker](https://hub.docker.com/r/blacklanternsecurity/bbot), see [Getting Started](https://www.blacklanternsecurity.com/bbot/Stable/)*

> **Upgrading from 2.x?** BBOT 3.0 contains breaking changes to the CLI, presets, modules, events, and Python API. See the [2.x → 3.0 Migration Guide](https://www.blacklanternsecurity.com/bbot/Stable/migration/3.0_breaking_changes/) ([source](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/migration/3.0_breaking_changes.md)) before upgrading.

> **Speed tip:** BBOT's DNS resolver ([blastdns](https://github.com/blacklanternsecurity/blastdns)) spins up multiple threads per resolver in `/etc/resolv.conf`. Adding more unfiltered resolvers dramatically speeds up scans. See the [sample resolv.conf](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/data/resolv-sample.conf) and [Tips and Tricks](https://www.blacklanternsecurity.com/bbot/Stable/scanning/tips_and_tricks/#speed-up-scans-with-more-dns-resolvers) for details.

## Example Commands

### 1) Subdomain Finder

Passive API sources plus a recursive DNS brute-force with target-specific subdomain mutations.

root@kitploit:~

```
# find subdomains of evilcorp.com
bbot -t evilcorp.com -p subdomain-enum

# passive sources only
bbot -t evilcorp.com -p subdomain-enum -rf passive
```

**`subdomain-enum.yml`**

root@kitploit:~

```
description: Enumerate subdomains via APIs, brute-force

flags:
  # enable every module with the subdomain-enum flag
  - subdomain-enum

output_modules:
  # output unique subdomains to TXT file
  - subdomains

config:
  dns:
    threads: 25
    brute_threads: 1000
  # put your API keys here
  # modules:
  #   github:
  #     api_key: ""
  #   chaos:
  #     api_key: ""
  #   securitytrails:
  #     api_key: ""
```

BBOT consistently finds 20-50% more subdomains than other tools. The bigger the domain, the bigger the difference. To learn how this is possible, see [How It Works](https://www.blacklanternsecurity.com/bbot/Stable/how_it_works/).

![subdomain-stats-ebay](https://assets.kitploit.com/production/public/readmes/668/5fff4853068a9417e00afeae96d3b98e7240accb1dad210fa9abcf2419f104ed.png)

### 2) Web Spider

root@kitploit:~

```
# crawl evilcorp.com, extracting emails and other goodies
bbot -t evilcorp.com -p spider
```

**`spider.yml`**

root@kitploit:~

```
description: Recursive web spider

modules:
  - http

blacklist:
  # Prevent spider from invalidating sessions by logging out
  - "RE:/.*(sign|log)[_-]?out"

config:
  web:
    # how many links to follow in a row
    spider_distance: 2
    # don't follow links whose directory depth is higher than 4
    spider_depth: 4
    # maximum number of links to follow per page
    spider_links_per_page: 25
```

### 3) Email Gatherer

root@kitploit:~

```
# quick email enum with free APIs + scraping
bbot -t evilcorp.com -p email-enum

# pair with subdomain enum + web spider for maximum yield
bbot -t evilcorp.com -p email-enum subdomain-enum spider
```

**`email-enum.yml`**

root@kitploit:~

```
description: Enumerate email addresses from APIs, web crawling, etc.

flags:
  - email-enum

output_modules:
  - emails
```

### 4) Web Scanner

root@kitploit:~

```
# run a light web scan against www.evilcorp.com
bbot -t www.evilcorp.com -p web

# run a heavy web scan against www.evilcorp.com
bbot -t www.evilcorp.com -p web-heavy
```

**`web.yml`**

root@kitploit:~

```
description: Quick web scan

include:
  - iis-shortnames

flags:
  - web
```

**`web-heavy.yml`**

root@kitploit:~

```
description: Aggressive web scan

include:
  # include the web preset
  - web

flags:
  - web-heavy
```

### 5) Everything Everywhere All at Once

root@kitploit:~

```
# everything everywhere all at once
bbot -t evilcorp.com -p kitchen-sink

# roughly equivalent to:
bbot -t evilcorp.com -p subdomain-enum cloud-enum code-enum email-enum spider web paramminer webbrute web-screenshots
```

**`kitchen-sink.yml`**

root@kitploit:~

```
description: Everything everywhere all at once

include:
  - subdomain-enum
  - cloud-enum
  - code-enum
  - email-enum
  - spider
  - web
  - paramminer
  - webbrute
  - web-screenshots
  - baddns-heavy

config:
  modules:
    dnsbrute:
      recursive_mutations: true
    dnscommonsrv:
      recursive_mutations: true
    webbrute:
      avoid_wafs: False
    wayback:
      urls: True
      parameters: True
      archive: True
```

## How it Works

Click the graph below to explore the [inner workings](https://www.blacklanternsecurity.com/bbot/Stable/how_it_works/) of BBOT.

[![image](https://assets.kitploit.com/production/public/readmes/668/7ba853b4527122716b32ad46d3f56951bd65cf4faa53b10181e33c8b0f2af427.png)](https://www.blacklanternsecurity.com/bbot/Stable/how_it_works/)

## Output Modules

* [Neo4j](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#neo4j)
* [Teams](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#teams)
* [Discord](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#discord)
* [Slack](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#slack)
* [Postgres](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#postgres)
* [MySQL](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#mysql)
* [SQLite](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#sqlite)
* [Splunk](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#splunk)
* [Elasticsearch](https://github.com/blacklanternsecurity/bbot/blob/HEAD/docs/scanning/output.md#elasticsearch)
* [CSV](https://github.com/blacklanter...