---
title: Subfinder Cheat Sheet
url: https://buaq.net/go-152780.html
source: unSafe.sh - 不安全
date: 2023-03-10
fetch_date: 2025-10-04T09:05:24.426654
---

# Subfinder Cheat Sheet

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

Subfinder Cheat Sheet

HomeBlogAboutServicesHomeBlogAboutServicesSubfinder Cheat S
*2023-3-9 22:37:10
Author: [highon.coffee(查看原文)](/jump-152780.htm)
阅读量:54
收藏*

---

* [What is Subfinder](#what-is-subfinder)
* [Install Subfinder](#install-subfinder)
* [Subfinder API Setup](#subfinder-api-setup)
  + [Subfinder Sources](#subfinder-sources)
* [Example Subfinder API Config File](#example-subfinder-api-config-file)
* [Subfinder Usage](#subfinder-usage)
* [Example Subfinder Commands](#example-subfinder-commands)
  + [Find Subdomains Single Domain](#find-subdomains-single-domain)
  + [Verify Subfinder Results With HTTPX](#verify-subfinder-results-with-httpx)
  + [Subfinder + Naabu Portscan](#subfinder--naabu-portscan)
* [Document Changelog](#document-changelog)

## What is Subfinder

Subfinder is a subdomain discovery tool made by Project Discovery, the following cheat sheet provides and overview of the command flags for Subfinder and common commamnd examples for real world usage. Subfinder can be used to obtain a number of subdomains both passively and actively, to identify more attack surface for [penetration testing](https://highon.coffee/penetration-testing/) or bug bounty recon or assessment.

## Install Subfinder

```
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

##### Configure API Keys

Subfinder works straight after install, however with API keys (even a free key) will improve passive subdomain results.

## Subfinder API Setup

Configuring Subfinder to use free or paid API services will likely improve the discovered domains the tool can find. You can list the sources Subfinder uses by running `subfinder -ls`. In order to setup subfinder api keys you need to create a configuration file at: `$HOME/.config/subfinder/provider-config.yaml` and populate with the API keys that you wil need to obtain from the various sources.

### Subfinder Sources

Subfinder supports the following data API sources:

| NAME | URL |
| --- | --- |
| BeVigil | `https://bevigil.com/osint-api` |
| BinaryEdge | `https://binaryedge.io` |
| BufferOver | `https://tls.bufferover.run` |
| C99 | `https://api.c99.nl/` |
| Censys | `https://censys.io` |
| CertSpotter | `https://sslmate.com/certspotter/api/` |
| Chaos | `https://chaos.projectdiscovery.io` |
| Chinaz | `http://my.chinaz.com/ChinazAPI/DataCenter/MyDataApi` |
| DNSDB | `https://api.dnsdb.info` |
| Fofa | `https://fofa.info/static_pages/api_help` |
| FullHunt | `https://fullhunt.io` |
| GitHub | `https://github.com` |
| Intelx | `https://intelx.io` |
| PassiveTotal | `http://passivetotal.org` |
| quake | `https://quake.360.cn` |
| Robtex | `https://www.robtex.com/api/` |
| SecurityTrails | `http://securitytrails.com` |
| Shodan | `https://shodan.io` |
| ThreatBook | `https://x.threatbook.cn/en` |
| VirusTotal | `https://www.virustotal.com` |
| WhoisXML API | `https://whoisxmlapi.com/` |
| ZoomEye | `https://www.zoomeye.org` |
| ZoomEye API | `https://api.zoomeye.org` |
| dnsrepo | `https://dnsrepo.noc.org` |
| Hunter | `https://hunter.qianxin.com/` |
| Facebook | `https://developers.facebook.com` |
| BuiltWith | `https://api.builtwith.com/domain-api` |

## Example Subfinder API Config File

The following is an example of the API config file:

```
binaryedge:
  - 0bf8919b-aab9-42e4-9574-d3b639324597
  - ac244e2f-b635-4581-878a-33f4e79a2c13
censys:
  - ac244e2f-b635-4581-878a-33f4e79a2c13:dd510d6e-1b6e-4655-83f6-f347b363def9
certspotter: []
passivetotal:
  - [email protected]:sample_password
redhuntlabs:
  - ENDPOINT:API_TOKEN
  - https://reconapi.redhuntlabs.com/community/v1/domains/subdomains:joEPzJJp2AuOCw7teAj63HYrPGnsxuPQ
securitytrails: []
shodan:
  - AAAAClP1bJJSRMEYJazgwhJKrggRwKA
github:
  - ghp_lkyJGU3jv1xmwk4SDXavrLDJ4dl2pSJMzj4X
  - ghp_gkUuhkIYdQPj13ifH4KA3cXRn8JD2lqir2d4
zoomeyeapi:
  - 4f73021d-ff95-4f53-937f-83d6db719eec
quake:
  - 0cb9030c-0a40-48a3-b8c4-fca28e466ba3
facebook:
  - APP_ID:APP_SECRET
intelx:
  - HOST:API_KEY
  - 2.intelx.io:s4324-b98b-41b2-220e8-3320f6a1284d
```

Above file source: https://docs.projectdiscovery.io/tools/subfinder/install#post-install-configuration

## Subfinder Usage

How to use Subfinder to find domains:

## Example Subfinder Commands

### Find Subdomains Single Domain

Find subdomains for a single domain with subfinder:

```
subfinder -d hackerone.com

               __    _____           __
   _______  __/ /_  / __(_)___  ____/ /__  _____
  / ___/ / / / __ \/ /_/ / __ \/ __  / _ \/ ___/
 (__  ) /_/ / /_/ / __/ / / / / /_/ /  __/ /
/____/\__,_/_.___/_/ /_/_/ /_/\__,_/\___/_/ v2.5.1

		projectdiscovery.io

Use with caution. You are responsible for your actions
Developers assume no liability and are not responsible for any misuse or damage.
By using subfinder, you also agree to the terms of the APIs used.

[INF] Enumerating subdomains for hackerone.com
info.hackerone.com
design.hackerone.com
docs.hackerone.com
events.hackerone.com
web-seo-content-for-business.theflyingkick.websitedesignresource.api.hackerone.com
zendesk2.hackerone.com
fsdkim.hackerone.com
email.gh-mail.hackerone.com
a.ns.hackerone.com
support.hackerone.com
www.hackerone.com
mta-sts.managed.hackerone.com
api.hackerone.com
gslink.hackerone.com
zendesk1.hackerone.com
3d.hackerone.com
links.hackerone.com
mta-sts.hackerone.com
resources.hackerone.com
zendesk4.hackerone.com
zendesk3.hackerone.com
go.hackerone.com
mta-sts.forwarding.hackerone.com
_dmarc.hackerone.com
b.ns.hackerone.com
hackerone.com
defcon.hackerone.com
[INF] Found 27 subdomains for hackerone.com in 30 seconds 33 milliseconds
```

### Verify Subfinder Results With HTTPX

Chain up other tools within your workflow, such as verifying targets have web servers using HTTPX:

```
echo hackerone.com | subfinder -silent | httpx -silent
https://docs.hackerone.com
https://mta-sts.forwarding.hackerone.com
https://mta-sts.hackerone.com
https://mta-sts.managed.hackerone.com
http://a.ns.hackerone.com
https://www.hackerone.com
http://b.ns.hackerone.com
http://zendesk4.hackerone.com
http://fsdkim.hackerone.com
http://zendesk1.hackerone.com
http://zendesk2.hackerone.com
http://zendesk3.hackerone.com
https://hackerone.com
https://support.hackerone.com
https://resources.hackerone.com
https://gslink.hackerone.com
https://api.hackerone.com
```

### Subfinder + Naabu Portscan

```
echo hackerone.com | subfinder -silent | naabu -silent
docs.hackerone.com:443
docs.hackerone.com:80
mta-sts.forwarding.hackerone.com:443
mta-sts.forwarding.hackerone.com:80
mta-sts.hackerone.com:80
mta-sts.hackerone.com:443
mta-sts.managed.hackerone.com:80
mta-sts.managed.hackerone.com:443
<--SNIP-->
```

If you found this Subfinder cheat sheet useful, please share it below.

## Document Changelog

* **Last Updated:** 12/02/2024 (12th of February 2024)
* **Author:** Arr0way
* **Notes:** Checked syntax was current for latest version of Subfinder + added Subfinder API sources table.

文章来源: https://highon.coffee/blog/subfinder-cheat-sheet/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)