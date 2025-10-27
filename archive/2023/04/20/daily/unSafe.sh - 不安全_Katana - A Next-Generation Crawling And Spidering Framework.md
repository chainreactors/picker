---
title: Katana - A Next-Generation Crawling And Spidering Framework
url: https://buaq.net/go-159479.html
source: unSafe.sh - 不安全
date: 2023-04-20
fetch_date: 2025-10-04T11:32:45.148117
---

# Katana - A Next-Generation Crawling And Spidering Framework

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

![](https://8aqnet.cdn.bcebos.com/9f7deb6cdf2b43d0d0d445ee72c636a0.jpg)

Katana - A Next-Generation Crawling And Spidering Framework

A next-generation crawling and spidering framework Features • Installation • Usage
*2023-4-19 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-159479.htm)
阅读量:32
收藏*

---

#### A next-generation crawling and spidering framework

[Features](https://github.com/projectdiscovery/katana#features "Features") • [Installation](https://github.com/projectdiscovery/katana#installation "Installation") • [Usage](https://github.com/projectdiscovery/katana#usage "Usage") • [Scope](https://github.com/projectdiscovery/katana#scope-control "Scope") • [Config](https://github.com/projectdiscovery/katana#crawler-configuration "Config") • [Filters](https://github.com/projectdiscovery/katana#filters "Filters") • [Join Discord](https://discord.gg/projectdiscovery "Join Discord")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiWs_r7NznKYSGfrK2VLbivr5jZeI1z7YJgNX_QKr16teAS9BtFGGGFqu_hjdye3112Eg6mEufau6fHsPFdIyC4C2dH3xDPWS9sipZ0z1jAVibAMkLGLXqHr5pQKVpbbiRctxIub7gkkYcs1l8-lEAs9ElT8M5LyIHiU5SFjCSICR2izzon4TB1-P2bqw=w640-h450)](https://blogger.googleusercontent.com/img/a/AVvXsEiWs_r7NznKYSGfrK2VLbivr5jZeI1z7YJgNX_QKr16teAS9BtFGGGFqu_hjdye3112Eg6mEufau6fHsPFdIyC4C2dH3xDPWS9sipZ0z1jAVibAMkLGLXqHr5pQKVpbbiRctxIub7gkkYcs1l8-lEAs9ElT8M5LyIHiU5SFjCSICR2izzon4TB1-P2bqw)

* Fast And fully configurable web crawling
* **Standard** and **Headless** mode support
* **JavaScript** parsing / crawling
* Customizable **automatic form filling**
* **Scope control** - Preconfigured field / Regex
* **Customizable output** - Preconfigured fields
* INPUT - **STDIN**, **URL** and **LIST**
* OUTPUT - **STDOUT**, **FILE** and **JSON**

## Installation

katana requires **Go 1.18** to install successfully. To install, just run the below command or download pre-compiled binary from [release page](https://github.com/projectdiscovery/katana/releases "release page").

### Usage

This will display help for the tool. Here are all the switches it supports.

```
Usage:
```

## Running Katana

### Input for katana

**katana** requires **url** or **endpoint** to crawl and accepts single or multiple inputs.

Input URL can be provided using `-u` option, and multiple values can be provided using comma-separated input, similarly **file** input is supported using `-list` option and additionally piped input (stdin) is also supported.

#### URL Input

```
katana -u https://tesla.com
```

#### Multiple URL Input (comma-separated)

```
katana -u https://tesla.com,https://google.com
```

#### List Input

```
$ cat url_list.txt

https://tesla.com
https://google.com
```

```
katana -list url_list.txt
```

#### STDIN (piped) Input

```
echo https://tesla.com | katana
```

```
cat domains | httpx | katana
```

Example running katana -

```
katana -u https://youtube.com

__        __
  / /_____ _/ /____ ____  ___ _
 /  '_/ _  / __/ _  / _ \/ _  /
/_/\_\\_,_/\__/\_,_/_//_/\_,_/ v0.0.1

projectdiscovery.io

[WRN] Use with caution. You are responsible for your actions.
[WRN] Developers assume no liability and are not responsible for any misuse or damage.
https://www.youtube.com/
https://www.youtube.com/about/
https://www.youtube.com/about/press/
https://www.youtube.com/about/copyright/
https://www.youtube.com/t/contact_us/
https://www.youtube.com/creators/
https://www.youtube.com/ads/
https://www.youtube.com/t/terms
https://www.youtube.com/t/privacy
https://www.youtube.com/about/policies/
https://www.youtube.com/howyoutubeworks?utm_campaign=ytgen&utm_source=ythp&utm_medium=LeftNav&utm_content=txt&u=https%3A%2F%2Fwww.youtube.com   %2Fhowyoutubeworks%3Futm_source%3Dythp%26utm_medium%3DLeftNav%26utm_campaign%3Dytgen
https://www.youtube.com/new
https://m.youtube.com/
https://www.youtube.com/s/desktop/4965577f/jsbin/desktop_polymer.vflset/desktop_polymer.js
https://www.youtube.com/s/desktop/4965577f/cssbin/www-main-desktop-home-page-skeleton.css
https://www.youtube.com/s/desktop/4965577f/cssbin/www-onepick.css
https://www.youtube.com/s/_/ytmainappweb/_/ss/k=ytmainappweb.kevlar_base.0Zo5FUcPkCg.L.B1.O/am=gAE/d=0/rs=AGKMywG5nh5Qp-BGPbOaI1evhF5BVGRZGA
https://www.youtube.com/opensearch?locale=en_GB
https://www.youtube.com/manifest.webmanifest
https://www.youtube.com/s/desktop/4965577f/cssbin/www-main-desktop-watch-page-skeleton.css
https://www.youtube.com/s/desktop/4965577f/jsbin/web-animations-next-lite.min.vflset/web-animations-next-lite.min.js
https://www.youtube.com/s/desktop/4965577f/jsbin/custom-elements-es5-adapter.vflset/custom-elements-es5-adapter.js
https://w   ww.youtube.com/s/desktop/4965577f/jsbin/webcomponents-sd.vflset/webcomponents-sd.js
https://www.youtube.com/s/desktop/4965577f/jsbin/intersection-observer.min.vflset/intersection-observer.min.js
https://www.youtube.com/s/desktop/4965577f/jsbin/scheduler.vflset/scheduler.js
https://www.youtube.com/s/desktop/4965577f/jsbin/www-i18n-constants-en_GB.vflset/www-i18n-constants.js
https://www.youtube.com/s/desktop/4965577f/jsbin/www-tampering.vflset/www-tampering.js
https://www.youtube.com/s/desktop/4965577f/jsbin/spf.vflset/spf.js
https://www.youtube.com/s/desktop/4965577f/jsbin/network.vflset/network.js
https://www.youtube.com/howyoutubeworks/
https://www.youtube.com/trends/
https://www.youtube.com/jobs/
https://www.youtube.com/kids/
```

## Crawling Mode

### Standard Mode

Standard crawling modality uses the standard go http library under the hood to handle HTTP requests/responses. This modality is much faster as it doesn't have the browser overhead. Still, it analyzes HTTP responses body as is, without any javascript or DOM rendering, potentially missing post-dom-rendered endpoints or [asynchronous](https://www.kitploit.com/search/label/Asynchronous "asynchronous") endpoint calls that might happen in complex web applications depending, for example, on browser-specific events.

### Headless Mode

Headless mode hooks internal headless calls to handle HTTP requests/responses directly within the browser context. This offers two advantages:

* The HTTP [fingerprint](https://www.kitploit.com/search/label/Fingerprint "fingerprint") (TLS and user agent) fully identify the client as a legitimate browser
* Better coverage since the endpoints are discovered analyzing the standard raw response, as in the previous modality, and also the browser-rendered one with javascript enabled.

Headless crawling is optional and can be enabled using `-headless` option.

Here are other headless CLI options -

```
katana -h headless

Flags:
HEADLESS:
   -hl, -headless       enable experimental headless hybrid crawling
   -sc, -system-chrome  use local installed chrome browser instead of katana installed
   -sb, -show-browser   show the browser on the screen with headless mode
   -ho, -headless-options string[]  start headless chrome with additional options
   -nos, -no-sandbox                start headless chrome in --no-sandbox mode
   -noi, -no-incognito              start headless chrome without incognito mode
```

## *`-no-sandbox`*

Runs headless chrome browser with **no-sandbox** option, useful when running as root user.

```
katana -u https://tesla.com -headless -no-sandbox
```

## *`-no-incognito`*

Runs headless chrome browser without incognito mode, useful when using the local browser.

```
katana -u https://tesla.com -headless -no-incognito
```

## *`-headless-options`*

When crawling in headless mode, additional chrome options can be specified using `-headless-options`, for example -

```
katana -u https://tesla.com -headless -system-chrome -headless-options --disable-gpu,proxy-server=http://127.0.0.1:8080
`...