---
title: AzureHound - Azure Data Exporter For BloodHound
url: https://buaq.net/go-140316.html
source: unSafe.sh - 不安全
date: 2022-12-17
fetch_date: 2025-10-04T01:46:30.988191
---

# AzureHound - Azure Data Exporter For BloodHound

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

![](https://8aqnet.cdn.bcebos.com/378a94d3744550c7e11e69f5a32f3b7e.jpg)

AzureHound - Azure Data Exporter For BloodHound

The BloodHound data collector for Microsoft Azure Get AzureHound Release Binaries Downloa
*2022-12-16 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-140316.htm)
阅读量:32
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxH4ORvtpJZLry3tPrOdrXtg4IZ3wKmD5jgL1MF4dFmYha42IOKeYVKJFGtwOoacaOZreL3-rixcCank0fW1cBhkwYCBGBO00xJ7-dzulegHFExvvqvhbDjFhutjk13ODp8rcqFlsXFwNPXbJH8qW1PZ0ZM3W6_54t9Jq7o6Lkm7UFPK6g-_1PVUgQbw/w640-h480/azure.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxH4ORvtpJZLry3tPrOdrXtg4IZ3wKmD5jgL1MF4dFmYha42IOKeYVKJFGtwOoacaOZreL3-rixcCank0fW1cBhkwYCBGBO00xJ7-dzulegHFExvvqvhbDjFhutjk13ODp8rcqFlsXFwNPXbJH8qW1PZ0ZM3W6_54t9Jq7o6Lkm7UFPK6g-_1PVUgQbw/s1800/azure.jpg)

The [BloodHound](https://www.kitploit.com/search/label/BloodHound "BloodHound") data collector for [Microsoft](https://www.kitploit.com/search/label/Microsoft "Microsoft") Azure

## Get AzureHound

### Release Binaries

Download the appropriate [binary](https://www.kitploit.com/search/label/Binary "binary") for your platform from one of our [Releases](https://github.com/BloodHoundAD/AzureHound/releases "Releases").

#### Rolling Release

The rolling release contains pre-built binaries that are automatically kept [up-to-date](https://www.kitploit.com/search/label/Up-to-date "up-to-date") with the `main` branch and can be downloaded from [here](https://github.com/BloodHoundAD/AzureHound/releases/tag/rolling "here").

> **Warning:** The rolling release may be unstable.

## Compiling

##### Prerequisites

* [Go 1.18](https://go.dev/dl/ "Go 1.18") or later

To build this project from source run the following:

```
go build -ldflags="-s -w -X github.com/bloodhoundad/azurehound/constants.Version=`git describe tags --exact-match 2> /dev/null || git rev-parse HEAD`"
```

## Usage

### Quickstart

**Print all [Azure](https://www.kitploit.com/search/label/Azure "Azure") Tenant data to stdout**

```
❯ azurehound list -u "$USERNAME" -p "$PASSWORD" -t "$TENANT"
```

**Print all Azure Tenant data to file**

```
❯ azurehound list -u "$USERNAME" -p "$PASSWORD" -t "$TENANT" -o "mytenant.json"
```

**Configure and start data collection service for BloodHound Enterprise**

```
❯ azurehound configure
```

### CLI

```
❯ azurehound --help
AzureHound vx.x.x
Created by the BloodHound Enterprise team - https://bloodhoundenterprise.io

The official tool for collecting Azure data for BloodHound and BloodHound Enterprise

Usage:
  azurehound [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  configure   Configure AzureHound
  help        Help about any command
  list        Lists Azure Objects
  start       Start Azure data collection service for BloodHound Enterprise

Flags:
  -c, --config string          AzureHound configuration file (default: /Users/dlees/.config/azurehound/config.json)
  -h, --help                   help for azurehound
      --json                   Output logs as json
  -j, --jwt string             Use an acquired JWT to authenticate into Azure
      --log-   file string        Output logs to this file
      --proxy string           Sets the proxy URL for the AzureHound service
  -r, --refresh-token string   Use an acquired refresh token to authenticate into Azure
  -v, --verbosity int          AzureHound verbosity level (defaults to 0) [Min: -1, Max: 2]
      --version                version for azurehound

Use "azurehound [command] --help" for more information about a command.
```

AzureHound - Azure Data Exporter For BloodHound
![AzureHound - Azure Data Exporter For BloodHound](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxH4ORvtpJZLry3tPrOdrXtg4IZ3wKmD5jgL1MF4dFmYha42IOKeYVKJFGtwOoacaOZreL3-rixcCank0fW1cBhkwYCBGBO00xJ7-dzulegHFExvvqvhbDjFhutjk13ODp8rcqFlsXFwNPXbJH8qW1PZ0ZM3W6_54t9Jq7o6Lkm7UFPK6g-_1PVUgQbw/s72-w640-c-h480/azure.jpg)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/azurehound-azure-data-exporter-for.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)