---
title: maigret v0.6.5
url: https://kitploit.com/en/posts/github-soxoj-maigret-v065
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:09.008893
---

# maigret v0.6.5

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/216/643e47591a403b0bb269477dcdd0a945091187ded99666f49914dcf8792a8af4.png)

New releaseAug 25, 2026

# maigret v0.6.5

🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites

Share

# Maigret

[![PyPI version badge for Maigret](https://img.shields.io/pypi/v/maigret?style=flat-square)](https://pypi.org/project/maigret/)
[![Total downloads](https://static.pepy.tech/badge/maigret)
![Downloads/month](https://static.pepy.tech/badge/maigret/month)](https://pepy.tech/project/maigret)

[![View count for Maigret project](https://komarev.com/ghpvc/?username=maigret&color=brightgreen&label=views&style=flat-square)](https://github.com/soxoj/maigret)
[![Minimum Python version required: 3.10+](https://img.shields.io/badge/Python-3.10+-brightgreen?style=flat-square)](https://github.com/soxoj/maigret)
[![License badge for Maigret](https://img.shields.io/github/license/soxoj/maigret?style=flat-square)](https://github.com/soxoj/maigret/blob/main/LICENSE)

![Maigret logo](https://assets.kitploit.com/production/public/readmes/216/f4ea992b7e00fe5e906d35323dd806650b89309c635ef77372bc1f8e497950f7.png)

[![Ask Code Wiki about Maigret](https://img.shields.io/badge/Code_Wiki-ask_about_repo-yellow?logo=googlegemini)](https://codewiki.google/github.com/soxoj/maigret)
[![Ask DeepWiki about Maigret](https://img.shields.io/badge/DeepWiki-ask_about_repo-yellow)](https://deepwiki.com/soxoj/maigret)

**English** · [简体中文](README.zh-CN.md)

**Maigret** collects a dossier on a person **by username only**, checking for accounts on a huge number of sites and gathering all the available information from web pages. No API keys required. **[AI profiling (demo)](#ai-analysis)**.

## Sponsors

[![IPcook](https://assets.kitploit.com/production/public/readmes/216/5d5cc2e20ee17fd555c1e641df2c8ce85c49f3dae1dce6ff239ba502e5114950.png)](https://www.ipcook.com/?ref=githubmaigret&utm_source=github&utm_medium=referral&utm_campaign=maigret)

[**IPcook**](https://www.ipcook.com/?ref=githubmaigret&utm_source=github&utm_medium=referral&utm_campaign=maigret) provides reliable residential proxies for online research, username discovery, and public data collection workflows. High success rates • 99.99% uptime • Response time under 0.5s • Monthly & Pay-as-you-go • Non-expiring traffic • Up to 10 free sub-accounts for team collaboration • Residential proxies from $0.3–$3.2/GB.
**Special Offer**: FREE 100MB trial available. Use code WELCOME20 for 20% off.

[![RapidProxy](https://assets.kitploit.com/production/public/readmes/216/d0d5d0f98e98ee2bae78bf2fc510e47089760ef9ce72121edc7ce6de19295d9f.jpg)](https://www.rapidproxy.io/?ref=soxoj)

[**RapidProxy**](https://www.rapidproxy.io/?ref=soxoj) provides high-performance residential proxies for Twitter scraping, Selenium automation, and web data extraction. 90M+ IPs • Smart rotation • Anti-block • Non-expiring traffic.
**Special Offer**: Try it free — Plans from $0.65/GB. Use code **RAPID10** for 10% off.

## Contents

* [In one minute](#in-one-minute)
* [Main features](#main-features)
* [Demo](#demo)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Commercial Use](#commercial-use)
* [About](#about)

## In one minute

Ensure you have Python 3.10 or higher.

root@kitploit:~

```
pip install maigret
maigret YOUR_USERNAME
```

No install? Try the [community Telegram bot](https://sites.google.com/view/maigret-bot-link) or a [Cloud Shell](#cloud-shells).

Want a web UI? See [how to launch it](#web-interface).

See also: [Quick start](https://maigret.readthedocs.io/en/latest/quick-start.html).

## Main features

* Supports 3,000+ sites ([see full list](https://github.com/soxoj/maigret/blob/main/sites.md)). A default run checks the 500 highest-ranked sites by traffic; pass `-a` to scan everything, or `--tags` to narrow by category/country.
* Embeddable in Python projects — import `maigret` and run searches programmatically (see [library usage](https://maigret.readthedocs.io/en/latest/library-usage.html)).
* [Extracts](https://github.com/soxoj/socid_extractor) all available information about the account owner from profile pages and site APIs, including links to other accounts.
* Performs recursive search using discovered usernames and other IDs.
* Allows filtering by tags (site categories, countries).
* Detects and partially bypasses blocks, censorship, and CAPTCHA.
* Fetches an [auto-updated site database](https://maigret.readthedocs.io/en/latest/settings.html#database-auto-update) from GitHub each run (once per 24 hours), and falls back to the built-in database if offline.
* Works with Tor and I2P websites; able to check domains.
* Ships with a [web interface](#web-interface) for browsing results as a graph and downloading reports in every format from a single page.
* Optional [AI analysis mode](#ai-analysis) (`--ai`) that turns raw findings into a short investigation summary using an OpenAI-compatible API.

For the complete feature list, see the [features documentation](https://maigret.readthedocs.io/en/latest/features.html).

### Used by

Professional OSINT and social-media analysis tools built on Maigret:

[![Social Links API](https://assets.kitploit.com/production/public/readmes/216/e4e6afb8670aa5d3b703f1073907398ff6cc84031b15f4108bf1da37e01ab023.png)](https://github.com/SocialLinks-IO/sociallinks-api)
[![Social Links Crimewall](https://assets.kitploit.com/production/public/readmes/216/fc0028a249da7498721b8783b585545203c93a3e51de565f4d27aa9a71882743.png)](https://sociallinks.io/products/sl-crimewall)
[![UserSearch](https://assets.kitploit.com/production/public/readmes/216/e0b60e01a3af3ac089eebc120d9627aeb0cbf3d9ee68c4f62e8d1e46fa5df5ad.png)](https://usersearch.ai/)

## Demo

### Video

[![asciicast](https://asciinema.org/a/Ao0y7N0TTxpS0pisoprQJdylZ.svg)](https://asciinema.org/a/Ao0y7N0TTxpS0pisoprQJdylZ)

### Reports

[PDF report](https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotographycars.pdf), [HTML report](https://htmlpreview.github.io/?https://raw.githubusercontent.com/soxoj/maigret/main/static/report_alexaimephotographycars.html)

![HTML report screenshot](https://assets.kitploit.com/production/public/readmes/216/643e47591a403b0bb269477dcdd0a945091187ded99666f49914dcf8792a8af4.png)

![XMind 8 report screenshot](https://assets.kitploit.com/production/public/readmes/216/42bfa79f6b803e29da14610e4f8364155232e980fe2f378a1067c57e6e3befc2.png)

[Full console output](https://raw.githubusercontent.com/soxoj/maigret/main/static/recursive_search.md)

## Installation

Already ran the [In one minute](#one-minute) steps? You're set. Below are alternative methods.

Don't want to install anything? Use the [community Telegram bot](https://sites.google.com/view/maigret-bot-link).

### Windows

Download `maigret_standalone.exe` from [Releases](https://github.com/soxoj/maigret/releases). You can launch it two ways:

* **Double-click it** — Maigret will ask for a username, run a default search, and wait at the end so the report links stay visible.
* **Run it from a terminal** — open Command Prompt (press `Win+R`, type `cmd`, hit Enter) or PowerShell to pass extra options:

root@kitploit:~

```
cd %USERPROFILE%\Downloads
maigret_standalone.exe USERNAME
maigret_standalone.exe USERNAME --html       :: also save an HTML report
maigret_standalone.exe --help                :: list all options
```

Video guide: <https://youtu.be/qIgwTZOmMmM>.

### Cloud Shells

Run Maigret in the browser via cloud shells or Jupyter notebooks:

[![Open in Cloud Shell](https://assets.kitploit.com/production/public/readmes/216/7dc64fe3ed6727...