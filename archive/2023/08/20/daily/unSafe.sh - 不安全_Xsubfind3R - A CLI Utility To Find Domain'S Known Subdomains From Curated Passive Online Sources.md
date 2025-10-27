---
title: Xsubfind3R - A CLI Utility To Find Domain'S Known Subdomains From Curated Passive Online Sources
url: https://buaq.net/go-174833.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:46.247948
---

# Xsubfind3R - A CLI Utility To Find Domain'S Known Subdomains From Curated Passive Online Sources

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Xsubfind3R - A CLI Utility To Find Domain'S Known Subdomains From Curated Passive Online Sources

xsubfind3r is a command-line interface (CLI) utility to find domain's known subdomains from
*2023-8-19 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-174833.htm)
阅读量:32
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNUU02QE-Yw9IlS7oBVH3Kfxte3lMa-HrL4DcQrWnX5Cd6--jGqdloFEkQFpi8O14OZ0nI-VPLJ5oXaCu-1l4T0VsYHXxJQ6zPjG2_i3__6FGMtVLJWM9CxTATCJrQiGe6VrarBm8tZqTy7T7jbStckXLsQ2u3qQkM_541NrdaZe0PBoH9zIONnNeVTbu4/w640-h538/xsubfind3r.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNUU02QE-Yw9IlS7oBVH3Kfxte3lMa-HrL4DcQrWnX5Cd6--jGqdloFEkQFpi8O14OZ0nI-VPLJ5oXaCu-1l4T0VsYHXxJQ6zPjG2_i3__6FGMtVLJWM9CxTATCJrQiGe6VrarBm8tZqTy7T7jbStckXLsQ2u3qQkM_541NrdaZe0PBoH9zIONnNeVTbu4/s1046/xsubfind3r.png)

`xsubfind3r` is a command-line interface (CLI) utility to find domain's known [subdomains](https://www.kitploit.com/search/label/Subdomains "subdomains") from curated passive online sources.

## Features

* Fetches domains from curated passive sources to maximize results.
* Supports `stdin` and `stdout` for easy integration into workflows.
* Cross-Platform (Windows, Linux & macOS).

## Installation

### Install release binaries (Without Go Installed)

Visit the [releases page](https://github.com/hueristiq/xsubfind3r/releases "releases page") and find the appropriate archive for your operating system and architecture. Download the archive from your browser or copy its URL and retrieve it with `wget` or `curl`:

* ...with `wget`:

  ```
   wget https://github.com/hueristiq/xsubfind3r/releases/download/v<version>/xsubfind3r-<version>-linux-amd64.tar.gz
  ```
* ...or, with `curl`:

  ```
   curl -OL https://github.com/hueristiq/xsubfind3r/releases/download/v<version>/xsubfind3r-<version>-linux-amd64.tar.gz
  ```

...then, extract the binary:

```
tar xf xsubfind3r-<version>-linux-amd64.tar.gz
```

> **TIP:** The above steps, download and extract, can be combined into a single step with this onliner
>
> ```
> curl -sL https://github.com/hueristiq/xsubfind3r/releases/download/v<version>/xsubfind3r-<version>-linux-amd64.tar.gz | tar -xzv
> ```

**NOTE:** On [Windows](https://www.kitploit.com/search/label/Windows "Windows") systems, you should be able to double-click the zip archive to extract the `xsubfind3r` executable.

...move the `xsubfind3r` binary to somewhere in your `PATH`. For example, on GNU/Linux and OS X systems:

```
sudo mv xsubfind3r /usr/local/bin/
```

**NOTE:** Windows users can follow [How to: Add Tool Locations to the PATH Environment Variable](https://msdn.microsoft.com/en-us/library/office/ee537574%28v%3Doffice.14%29.aspx "How to: Add Tool Locations to the PATH Environment Variable") in order to add `xsubfind3r` to their `PATH`.

### Install source (With Go Installed)

Before you install from source, you need to make sure that Go is installed on your system. You can install Go by following the official instructions for your operating system. For this, we will assume that Go is already installed.

#### `go install ...`

```
go install -v github.com/hueristiq/xsubfind3r/cmd/xsubfind3r@latest
```

#### `go build ...` the development Version

* Clone the repository

  ```
   git clone https://github.com/hueristiq/xsubfind3r.git
  ```
* Build the utility

  ```
   cd xsubfind3r/cmd/xsubfind3r && \
  ```
* Move the `xsubfind3r` binary to somewhere in your `PATH`. For example, on GNU/Linux and OS X systems:

  ```
   sudo mv xsubfind3r /usr/local/bin/
  ```

  **NOTE:** Windows users can follow [How to: Add Tool Locations to the PATH Environment Variable](https://msdn.microsoft.com/en-us/library/office/ee537574%28v%3Doffice.14%29.aspx "How to: Add Tool Locations to the PATH Environment Variable") in order to add `xsubfind3r` to their `PATH`.

**NOTE:** While the development version is a good way to take a peek at `xsubfind3r`'s latest features before they get released, be aware that it may have bugs. Officially released versions will generally be more stable.

## Post Installation

`xsubfind3r` will work right after [installation](https://github.com/hueristiq/xsubfind3r#installation "installation"). However, **[BeVigil](https://bevigil.com "BeVigil")**, **[Chaos](https://chaos.projectdiscovery.io/#/ "Chaos")**, **[Fullhunt](https://fullhunt.io/ "Fullhunt")**, **[Github](https://github.com "Github")**, **[Intelligence X](https://intelx.io "Intelligence X")** and **[Shodan](https://shodan.io/ "Shodan")** require API keys to work, **[URLScan](https://urlscan.io "URLScan")** supports API key but not required. The API keys are stored in the `$HOME/.hueristiq/xsubfind3r/config.yaml` file - created upon first run - and uses the YAML format. Multiple API keys can be specified for each of these source from which one of them will be used.

Example `config.yaml`:

```
version: 0.3.0
sources:
    - alienvault
    - anubis
    - bevigil
    - chaos
    - commoncrawl
    - crtsh
    - fullhunt
    - github
    - hackertarget
    - intelx
    - shodan
    - urlscan
    - wayback
keys:
    bevigil:
        - awA5nvpKU3N8ygkZ
    chaos:
        - d23a554bbc1aabb208c9acfbd2dd41ce7fc9db39asdsd54bbc1aabb208c9acfb
    fullhunt:
        - 0d9652ce-516c-4315-b589-9b241ee6dc24
    github:
        - d23a554bbc1aabb208c9acfbd2dd41ce7fc9db39
        - asdsd54bbc1aabb208c9acfbd2dd41ce7fc9db39
    intelx:
        - 2.intelx.io:00000000-0000-0000-0000-000000000000
    shodan:
        - AAAAClP1bJJSRMEYJazgwhJKrggRwKA
    urlscan:
        - d4c85d34-e425-446e-d4ab-f5a3412acbe8
```

## Usage

To display help message for `xsubfind3r` use the `-h` flag:

help message:

```
                _      __ _           _ _____
__  _____ _   _| |__  / _(_)_ __   __| |___ / _ __
\ \/ / __| | | | '_ \| |_| | '_ \ / _` | |_ \| '__|
 >  <\__ \ |_| | |_) |  _| | | | | (_| |___) | |
/_/\_\___/\__,_|_.__/|_| |_|_| |_|\__,_|____/|_| v0.3.0

USAGE:
  xsubfind3r [OPTIONS]

INPUT:
 -d, --domain string[]                 target domains
 -l, --list string                     target domains' list file path

SOURCES:
      --sources bool                   list supported sources
 -u,  --sources-to-use string[]        comma(,) separeted sources to use
 -e,  --sources-to-exclude string[]    comma(,) separeted sources to exclude

OPTIMIZATION:
 -t,  --threads int                    number of threads (default: 50)

OUTPUT:
     --no-color bool                   disable colored output
 -o, --output string                   output subdomains' file path
    -O, --output-directory string         output subdomains' directory path
 -v, --verbosity string                debug, info, warning, error, fatal or silent (default: info)

CONFIGURATION:
 -c,  --configuration string           configuration file path (default: ~/.hueristiq/xsubfind3r/config.yaml)
```

## Contribution

[Issues](https://github.com/hueristiq/xsubfind3r/issues "Issues") and [Pull Requests](https://github.com/hueristiq/xsubfind3r/pulls "Pull Requests") are welcome! **Check out the [contribution guidelines](https://github.com/hueristiq/xsubfind3r/blob/master/CONTRIBUTING.md "contribution guidelines").**

## Licensing

This utility is [distributed](https://www.kitploit.com/search/label/Distributed "distributed") under the [MIT license](https://github.com/hueristiq/xsubfind3r/blob/master/LICENSE "MIT license").

Xsubfind3R - A CLI Utility To Find Domain'S Known Subdomains From Curated Passive Online Sources
![Xsubfind3R - A CLI Utility To Find Domain'S Known Subdomains From Curated Passive Online Sources](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNUU02QE-Yw9Il...