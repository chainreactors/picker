---
title: Columbus-Server - API first subdomain discovery service, blazingly fast subdomain enumeration service with advanced features
url: https://buaq.net/go-174300.html
source: unSafe.sh - 不安全
date: 2023-08-13
fetch_date: 2025-10-04T11:58:49.741311
---

# Columbus-Server - API first subdomain discovery service, blazingly fast subdomain enumeration service with advanced features

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

![](https://8aqnet.cdn.bcebos.com/4f41fd67a119391b87910b17988d99db.jpg)

Columbus-Server - API first subdomain discovery service, blazingly fast subdomain enumeration service with advanced features

Columbus Project is an API first subdomain discovery service, blazingly fast subdomain enume
*2023-8-12 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-174300.htm)
阅读量:26
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj83r20JOHBjm61cGPmMNj7DeslxjD94aApEC159HPsyyLrZ96Vmv8mfXsG2JeKj2AttCIxdz5ryZxuS-9D3YT7xg3akX0Wm6jlFeRVJkbbqjKgcOAh58DtURRFSUYyZZegHjNkdZuP62cKbf-0sTwc53VjQ1M5yP6PcidljfFPDZ432PuOYgTWrN0iHYHy/w400-h400/21375_320x0_resize_box_3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj83r20JOHBjm61cGPmMNj7DeslxjD94aApEC159HPsyyLrZ96Vmv8mfXsG2JeKj2AttCIxdz5ryZxuS-9D3YT7xg3akX0Wm6jlFeRVJkbbqjKgcOAh58DtURRFSUYyZZegHjNkdZuP62cKbf-0sTwc53VjQ1M5yP6PcidljfFPDZ432PuOYgTWrN0iHYHy/s320/21375_320x0_resize_box_3.png)

Columbus Project is an API first [subdomain](https://www.kitploit.com/search/label/Subdomain "subdomain") [discovery](https://www.kitploit.com/search/label/Discovery "discovery") service, blazingly fast [subdomain enumeration](https://www.kitploit.com/search/label/Subdomain%20Enumeration "subdomain enumeration") service with advanced features.

*Columbus returned 638 [subdomains](https://www.kitploit.com/search/label/Subdomains "subdomains") of tesla.com in 0.231 sec.*

## Usage

By default Columbus returns only the subdomains in a JSON string array:

```
curl 'https://columbus.elmasy.com/lookup/github.com'
```

But we think of the bash lovers, so if you don't want to mess with JSON and a newline separated list is your wish, then include the `Accept: text/plain` header.

```
DOMAIN="github.com"

curl -s -H "Accept: text/plain" "https://columbus.elmasy.com/lookup/$DOMAIN" | \
```

**For more, check the [features](https://columbus.elmasy.com/tools "features") or the [API documentation](https://columbus.elmasy.com/swagger/index.html "API documentation").**

## Entries

Currently, entries are got from [Certificate Transparency](https://certificate.transparency.dev/ "Certificate Transparency").

## Command Line

```
Usage of columbus-server:
  -check
    	Check for updates.
  -config string
    	Path to the config file.
  -version
    	Print version informations.
```

`-check`: Check the lates version on GitHub. Prints `up-to-date` and returns `0` if no update required. Prints the latest tag (eg.: `v0.9.1`) and returns `1` if new release available. In case of error, prints the error message and returns `2`.

## Build

```
git clone https://github.com/elmasy-com/columbus-server
make build
```

## Install

Create a new user:

```
adduser --system --no-create-home --disabled-login columbus-server
```

Create a new group:

```
addgroup --system columbus
```

Add the new user to the new group:

```
usermod -aG columbus columbus-server
```

Copy the binary to `/usr/bin/columbus-server`.

Make it executable:

```
chmod +x /usr/bin/columbus-server
```

Create a directory:

Copy the config file to `/etc/columbus/server.conf`.

Set the permission to 0600.

```
chmod -R 0600 /etc/columbus
```

Set the owner of the config file:

```
chown -R columbus-server:columbus /etc/columbus
```

Install the service file (eg.: `/etc/systemd/system/columbus-server.service`).

```
cp columbus-server.service /etc/systemd/system/
```

Reload systemd:

Start columbus:

```
systemctl start columbus-server
```

If you want to columbus start automatically:

```
systemctl enable columbus-server
```

Columbus-Server - API first subdomain discovery service, blazingly fast subdomain enumeration service with advanced features
![Columbus-Server - API first subdomain discovery service, blazingly fast subdomain enumeration service with advanced features](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj83r20JOHBjm61cGPmMNj7DeslxjD94aApEC159HPsyyLrZ96Vmv8mfXsG2JeKj2AttCIxdz5ryZxuS-9D3YT7xg3akX0Wm6jlFeRVJkbbqjKgcOAh58DtURRFSUYyZZegHjNkdZuP62cKbf-0sTwc53VjQ1M5yP6PcidljfFPDZ432PuOYgTWrN0iHYHy/s72-w400-c-h400/21375_320x0_resize_box_3.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/08/columbus-server-api-first-subdomain.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)