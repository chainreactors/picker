---
title: Noseyparker - A Command-Line Program That Finds Secrets And Sensitive Information In Textual Data And Git History
url: https://buaq.net/go-156481.html
source: unSafe.sh - 不安全
date: 2023-04-02
fetch_date: 2025-10-04T11:26:27.214719
---

# Noseyparker - A Command-Line Program That Finds Secrets And Sensitive Information In Textual Data And Git History

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

![](https://8aqnet.cdn.bcebos.com/f7d711bec5ae0c36f9d3b26c8ad18df5.jpg)

Noseyparker - A Command-Line Program That Finds Secrets And Sensitive Information In Textual Data And Git History

Nosey Parker is a command-line tool that finds secrets and sensitive information in textual
*2023-4-1 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-156481.htm)
阅读量:38
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHDC0T3Fnjhu0KOrTA0mVA1qNC6NB_ur2X-N86LLDaYLjROQWSDhvHUfQEpyJAwK5OPX1SiTN-I7MiBJ_TGoCVndqhd-CmBfg1abEK4-aQcW-0A3qKiqhx01DzsjEu-lnbPEnxHZvBxx2fsKNvKfFVBgDSt6b3yPykgyi_yAFtECTvPzXQ2lCuNkZu2A/w640-h422/hack_img.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhHDC0T3Fnjhu0KOrTA0mVA1qNC6NB_ur2X-N86LLDaYLjROQWSDhvHUfQEpyJAwK5OPX1SiTN-I7MiBJ_TGoCVndqhd-CmBfg1abEK4-aQcW-0A3qKiqhx01DzsjEu-lnbPEnxHZvBxx2fsKNvKfFVBgDSt6b3yPykgyi_yAFtECTvPzXQ2lCuNkZu2A/s585/hack_img.png)

Nosey Parker is a command-line tool that finds secrets and [sensitive information](https://www.kitploit.com/search/label/Sensitive%20Information "sensitive information") in textual data. It is useful both for offensive and defensive security testing.

**Key features:**

* It supports scanning files, directories, and the entire history of Git repositories
* It uses [regular expression](https://www.kitploit.com/search/label/Regular%20Expression "regular expression") matching with a set of 95 patterns chosen for high signal-to-noise based on experience and feedback from offensive security engagements
* It groups matches together that share the same secret, further emphasizing signal over noise
* It is fast: it can scan at hundreds of megabytes per second on a single core, and is able to scan 100GB of Linux kernel source history in less than 2 minutes on an older MacBook Pro

This open-source version of Nosey Parker is a reimplementation of the internal version that is regularly used in offensive security engagements at [Praetorian](https://praetorian.com "Praetorian"). The internal version has additional capabilities for false positive suppression and an alternative machine learning-based detection engine. Read more in blog posts [here](https://www.praetorian.com/blog/nosey-parker-ai-secrets-scanner-release/ "here") and [here](https://www.praetorian.com/blog/six-months-of-finding-secrets-with-nosey-parker/ "here").

## Building from source

**1. (On x86\_64) Install the [Hyperscan](https://github.com/intel/hyperscan "Hyperscan") library and headers for your system**

On macOS using Homebrew:

```
brew install hyperscan pkg-config
```

On Ubuntu 22.04:

```
apt install libhyperscan-dev pkg-config
```

**1. (On non-x86\_64) Build [Vectorscan](https://github.com/Vectorcamp/vectorscan "Vectorscan") from source**

You will need several dependencies, including `cmake`, `boost`, `ragel`, and `pkg-config`.

Download and extract the source for the [5.4.8 release](https://github.com/VectorCamp/vectorscan/releases/tag/vectorscan/5.4.8 "5.4.8 release") of Vectorscan:

```
wget https://github.com/VectorCamp/vectorscan/archive/refs/tags/vectorscan/5.4.8.tar.gz && tar xfz 5.4.8.tar.gz
```

Build with cmake:

```
cd vectorscan-vectorscan-5.4.8 && cmake -B build -DCMAKE_BUILD_TYPE=Release . && cmake --build build
```

Set the `HYPERSCAN_ROOT` environment variable so that Nosey Parker builds against your from-source build of Vectorscan:

```
export HYPERSCAN_ROOT="$PWD/build"
```

**Note:** The Nosey Parker [`Dockerfile`](https://github.com/praetorian-inc/noseyparker/blob/main/Dockerfile "Nosey Parker is a command-line program that finds secrets and sensitive information in textual data and Git history. (9)") builds Vectorscan from source and links against that.

**2. Install the Rust toolchain**

Recommended approach: install from [https://rustup.rs](https://rustup.rs "https://rustup.rs")

**3. Build using [Cargo](https://doc.rust-lang.org/cargo/ "Cargo")**

This will produce a binary at `target/release/noseyparker`.

## Docker Usage

**A prebuilt Docker image is available for the latest release for x86\_64:**

```
docker pull ghcr.io/praetorian-inc/noseyparker:latest
```

**A prebuilt Docker image is available for the most recent commit for x86\_64:**

```
docker pull ghcr.io/praetorian-inc/noseyparker:edge
```

**For other architectures (e.g., ARM) you will need to build the Docker image yourself:**

```
docker build -t noseyparker .
```

**Run the Docker image with a mounted volume:**

```
docker run -v "$PWD":/opt/ noseyparker
```

**Note:** The Docker image runs noticeably slower than a native binary, particularly on macOS.

## Usage quick start

### The datastore

Most Nosey Parker commands use a *datastore*. This is a special directory that Nosey Parker uses to record its findings and maintain its internal state. A datastore will be implicitly created by the `scan` command if needed. You can also create a datastore explicitly using the `datastore init -d PATH` command.

### Scanning filesystem content for secrets

Nosey Parker has built-in support for scanning files, recursively scanning directories, and scanning the entire history of Git repositories.

For example, if you have a Git clone of [CPython](https://github.com/python/cpython "CPython") locally at `cpython.git`, you can scan its entire history with the `scan` command. Nosey Parker will create a new datastore at `np.cpython` and saves its findings there.

```
$ noseyparker scan --datastore np.cpython cpython.git
Found 28.30 GiB from 18 plain files and 427,712 blobs from 1 Git repos [00:00:04]
Scanning content  ████████████████████ 100%  28.30 GiB/28.30 GiB  [00:00:53]
Scanned 28.30 GiB from 427,730 blobs in 54 seconds (538.46 MiB/s); 4,904/4,904 new matches

Rule                      Distinct Groups   Total Matches
───────────────────────────────────────────────────────────
 PEM-Encoded Private Key             1,076           1,1   92
 Generic Secret                        331             478
 netrc Credentials                      42           3,201
 Generic API Key                         2              31
 md5crypt Hash                           1               2

Run the `report` command next to show finding details.
```

### Scanning Git repos by URL, GitHub username, or GitHub organization name

Nosey Parker can also scan Git repos that have not already been cloned to the local filesystem. The `--git-url URL`, `--github-user NAME`, and `--github-org NAME` options to `scan` allow you to specify [repositories](https://www.kitploit.com/search/label/Repositories "repositories") of interest.

For example, to scan the Nosey Parker repo itself:

```
$ noseyparker scan --datastore np.noseyparker --git-url https://github.com/praetorian-inc/noseyparker
```

For example, to scan accessible repositories belonging to [`octocat`](https://github.com/octocat "Nosey Parker is a command-line program that finds secrets and sensitive information in textual data and Git history. (14)"):

```
$ noseyparker scan --datastore np.noseyparker --github-user octocat
```

These input specifiers will use an optional GitHub token if available in the `NP_GITHUB_TOKEN` environment variable. Providing an access token gives a higher API rate limit and may make additional repositories accessible to you.

See `noseyparker help scan` for more details.

### Summarizing findings

Nosey Parker prints out a summary of its findings when it finishes scanning. You can also run this step separately:

```
$ noseyparker summarize --datastore np.cpython

Rule                      Distinct Groups   Total Matches
───────────────────────────────────────────────────────────
 PEM-Encoded Private Key            ...