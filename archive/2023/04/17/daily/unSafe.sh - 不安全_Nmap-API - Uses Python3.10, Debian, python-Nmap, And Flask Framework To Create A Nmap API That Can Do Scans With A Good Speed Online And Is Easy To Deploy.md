---
title: Nmap-API - Uses Python3.10, Debian, python-Nmap, And Flask Framework To Create A Nmap API That Can Do Scans With A Good Speed Online And Is Easy To Deploy
url: https://buaq.net/go-158890.html
source: unSafe.sh - 不安全
date: 2023-04-17
fetch_date: 2025-10-04T11:31:37.485549
---

# Nmap-API - Uses Python3.10, Debian, python-Nmap, And Flask Framework To Create A Nmap API That Can Do Scans With A Good Speed Online And Is Easy To Deploy

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

![](https://8aqnet.cdn.bcebos.com/aa544bd4f21bcf7db05850e058806236.jpg)

Nmap-API - Uses Python3.10, Debian, python-Nmap, And Flask Framework To Create A Nmap API That Can Do Scans With A Good Speed Online And Is Easy To Deploy

Uses python3.10, Debian, python-Nmap, and flask framework to create a Nmap API that can do s
*2023-4-16 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-158890.htm)
阅读量:30
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDXdh_qCTiy0ll3nFeDhL9QB5rA1KiewKTl6MUHhNWs6q7awlz7FqQhvWCxUiTBk2b4Z2nYdyxMaGiUlspAZVNCh7ce0RXwKIWw1Kg3hYnxH2ty-6EwdQY_2v4sww2EfboVEvy1E8btqjo-3qvwMhZxpoZhf-ETAzPbKX_29kvGMgFoV_J2i4jrQiypg/w640-h424/nmap.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDXdh_qCTiy0ll3nFeDhL9QB5rA1KiewKTl6MUHhNWs6q7awlz7FqQhvWCxUiTBk2b4Z2nYdyxMaGiUlspAZVNCh7ce0RXwKIWw1Kg3hYnxH2ty-6EwdQY_2v4sww2EfboVEvy1E8btqjo-3qvwMhZxpoZhf-ETAzPbKX_29kvGMgFoV_J2i4jrQiypg/s576/nmap.png)

Uses python3.10, Debian, python-Nmap, and [flask](https://www.kitploit.com/search/label/Flask "flask") framework to create a [Nmap](https://www.kitploit.com/search/label/Nmap "Nmap") API that can do [scans](https://www.kitploit.com/search/label/Scans "scans") with a good speed online and is easy to deploy.

This is a implementation for our college PCL project which is still under development and constantly updating.

## API Reference

#### Get all items

```
  GET /api/p1/{username}:{password}/{target}
```

| Parameter | Type | Description |
| --- | --- | --- |
| `username` | `string` | **Required**. [username](https://www.kitploit.com/search/label/Username "username") of the current user |
| `password` | `string` | **Required**. current user password |
| `target` | `string` | **Required**. The target Hostname and IP |

#### Get item

```
  GET /api/p1/
  GET /api/p2/
  GET /api/p3/
  GET /api/p4/
  GET /api/p5/
```

| Parameter | Return data | Description | Nmap Command |
| --- | --- | --- | --- |
| `p1` | `json` | Effective Scan | `-Pn -sV -T4 -O -F` |
| `p2` | `json` | Simple Scan | `-Pn -T4 -A -v` |
| `p3` | `json` | Low Power Scan | `-Pn -sS -sU -T4 -A -v` |
| `p4` | `json` | Partial Intense Scan | `-Pn -p- -T4 -A -v` |
| `p5` | `json` | Complete Intense Scan | `-Pn -sS -sU -T4 -A -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script=vuln` |

#### Auth and User management

```
  POST /adduser/{admin-username}:{admin-passwd}/{id}/{username}/{passwd}
  POST /deluser/{admin-username}:{admin-passwd}/{t-username}/{t-userpass}
  POST /altusername/{admin-username}:{admin-passwd}/{t-user-id}/{new-t-username}
  POST /altuserid/{admin-username}:{admin-passwd}/{new-t-user-id}/{t-username}
  POST /altpassword/{admin-username}:{admin-passwd}/{t-username}/{new-t-userpass}
```

* make sure you use the ADMIN CREDS MENTIONED BELOW

| Parameter | Type | Description |
| --- | --- | --- |
| `admin-username` | `String` | Admin username |
| `admin-passwd` | `String` | Admin password |
| `id` | `String` | Id for newly added user |
| `username` | `String` | Username of the newly added user |
| `passwd` | `String` | Password of the newly added user |
| `t-username` | `String` | Target username |
| `t-user-id` | `String` | Target userID |
| `t-userpass` | `String` | Target users password |
| `new-t-username` | `String` | New username for the target |
| `new-t-user-id` | `String` | New userID for the target |
| `new-t-userpass` | `String` | New password for the target |

**DEFAULT** **CREDENTIALS**

`ADMINISTRATOR : zAp6_oO~t428)@,`

Nmap-API - Uses Python3.10, Debian, python-Nmap, And Flask Framework To Create A Nmap API That Can Do Scans With A Good Speed Online And Is Easy To Deploy
![Nmap-API - Uses Python3.10, Debian, python-Nmap, And Flask Framework To Create A Nmap API That Can Do Scans With A Good Speed Online And Is Easy To Deploy](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDXdh_qCTiy0ll3nFeDhL9QB5rA1KiewKTl6MUHhNWs6q7awlz7FqQhvWCxUiTBk2b4Z2nYdyxMaGiUlspAZVNCh7ce0RXwKIWw1Kg3hYnxH2ty-6EwdQY_2v4sww2EfboVEvy1E8btqjo-3qvwMhZxpoZhf-ETAzPbKX_29kvGMgFoV_J2i4jrQiypg/s72-w640-c-h424/nmap.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/04/nmap-api-uses-python310-debian-python.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)