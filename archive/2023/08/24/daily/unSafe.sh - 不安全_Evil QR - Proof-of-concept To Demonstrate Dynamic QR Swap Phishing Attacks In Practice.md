---
title: Evil QR - Proof-of-concept To Demonstrate Dynamic QR Swap Phishing Attacks In Practice
url: https://buaq.net/go-175202.html
source: unSafe.sh - 不安全
date: 2023-08-24
fetch_date: 2025-10-04T11:58:54.677170
---

# Evil QR - Proof-of-concept To Demonstrate Dynamic QR Swap Phishing Attacks In Practice

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

![](https://8aqnet.cdn.bcebos.com/183aa373ee72e4063a5476edb56f0843.jpg)

Evil QR - Proof-of-concept To Demonstrate Dynamic QR Swap Phishing Attacks In Practice

Toolkit demonstrating another approach of a QRLJacking attack, allowing to perform remote ac
*2023-8-23 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-175202.htm)
阅读量:36
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg-_ECEghAVf9cpYqU0L2f2w7QElFBdDQIx9D09Px8OmBGp58Mn9aVtaVojZKOvoQNNoFEtXRDg7cXX7sd_yLZY26A7K-6BUGnuXx4Y2hrEhRphio1NQtKr2fhgwesHTe9QF-gWf1Q5Jn-6o6tpXf3TqKDSTmSZBjfBCs4HLNSN_7bDCFhWeWpMD3Yq85S/w640-h360/evilqr.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg-_ECEghAVf9cpYqU0L2f2w7QElFBdDQIx9D09Px8OmBGp58Mn9aVtaVojZKOvoQNNoFEtXRDg7cXX7sd_yLZY26A7K-6BUGnuXx4Y2hrEhRphio1NQtKr2fhgwesHTe9QF-gWf1Q5Jn-6o6tpXf3TqKDSTmSZBjfBCs4HLNSN_7bDCFhWeWpMD3Yq85S/s1280/evilqr.png)

Toolkit demonstrating another approach of a [QRLJacking](https://www.kitploit.com/search/label/QRLJacking "QRLJacking") attack, allowing to perform remote account takeover, through sign-in QR code phishing.

It consists of a browser extension used by the attacker to extract the sign-in QR code and a server application, which retrieves the sign-in QR codes to display them on the hosted [phishing](https://www.kitploit.com/search/label/Phishing "phishing") pages.

Watch the demo video:

Read more about it on my blog: [https://breakdev.org/evilqr-phishing](https://breakdev.org/evilqr-phishing "https://breakdev.org/evilqr-phishing")

## Configuration

The parameters used by **Evil QR** are [hardcoded](https://www.kitploit.com/search/label/Hardcoded "hardcoded") into extension and server source code, so it is important to change them to use custom values, before you build and deploy the toolkit.

| parameter | description | default value |
| --- | --- | --- |
| **API\_TOKEN** | API token used to authenticate with REST API [endpoints](https://www.kitploit.com/search/label/Endpoints "endpoints") hosted on the server | 00000000-0000-0000-0000-000000000000 |
| **QRCODE\_ID** | QR code ID used to bind the extracted QR code with the one displayed on the phishing page | 11111111-1111-1111-1111-111111111111 |
| **BIND\_ADDRESS** | IP address with port the HTTP server will be listening on | 127.0.0.1:35000 |
| **API\_URL** | External URL pointing to the server, where the phishing page will be hosted | [http://127.0.0.1:35000](http://127.0.0.1:35000 "http://127.0.0.1:35000") |

Here are all the places in the source code, where the values should be modified:

#### server/core/config.go:

server/templates/index.html:

extension/background.js:

Installation

### Extension

You can load the extension in Chrome, through `Load unpacked` feature: [https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/#load-unpacked](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/#load-unpacked "https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/#load-unpacked")

Once the extension is installed, make sure to pin its icon in Chrome's extension toolbar, so that the icon is always visible.

### Server

Make sure you have [Go installed](https://go.dev/doc/install "Go installed") version at least 1.20.

To build go to `/server` [directory](https://www.kitploit.com/search/label/Directory "directory") and run the command:

Windows:

Linux:

```
chmod 700 build.sh
```

Built server binaries will be placed in the `./build/` directory.

## Usage

1. Run the server by running the built server binary: `./server/build/evilqr-server`
2. Open any of the supported websites in your Chrome browser, with installed **Evil QR** extension:

```
https://discord.com/login
https://web.telegram.org/k/
https://whatsapp.com
https://store.steampowered.com/login/
https://accounts.binance.com/en/login
https://www.tiktok.com/login
```

3. Make sure the sign-in QR code is visible and click the **Evil QR** extension icon in the toolbar. If the QR code is recognized, the icon should light up with colors.
4. Open the server's phishing page URL: `http://127.0.0.1:35000` (default)

## License

**Evil QR** is made by Kuba Gretzky ([@mrgretzky](https://twitter.com/mrgretzky "@mrgretzky")) and it's released under MIT license.

Evil QR - Proof-of-concept To Demonstrate Dynamic QR Swap Phishing Attacks In Practice
![Evil QR - Proof-of-concept To Demonstrate Dynamic QR Swap Phishing Attacks In Practice](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg-_ECEghAVf9cpYqU0L2f2w7QElFBdDQIx9D09Px8OmBGp58Mn9aVtaVojZKOvoQNNoFEtXRDg7cXX7sd_yLZY26A7K-6BUGnuXx4Y2hrEhRphio1NQtKr2fhgwesHTe9QF-gWf1Q5Jn-6o6tpXf3TqKDSTmSZBjfBCs4HLNSN_7bDCFhWeWpMD3Yq85S/s72-w640-c-h360/evilqr.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/08/evil-qr-proof-of-concept-to-demonstrate.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)