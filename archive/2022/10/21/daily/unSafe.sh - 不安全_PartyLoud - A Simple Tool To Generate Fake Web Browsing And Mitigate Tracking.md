---
title: PartyLoud - A Simple Tool To Generate Fake Web Browsing And Mitigate Tracking
url: https://buaq.net/go-131864.html
source: unSafe.sh - 不安全
date: 2022-10-21
fetch_date: 2025-10-03T20:27:03.936637
---

# PartyLoud - A Simple Tool To Generate Fake Web Browsing And Mitigate Tracking

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

![](https://8aqnet.cdn.bcebos.com/9231cdcf0416f3262a826f2f726edb61.jpg)

PartyLoud - A Simple Tool To Generate Fake Web Browsing And Mitigate Tracking

PartyLoud is a highly configurable and straightforward free tool that helps you prevent
*2022-10-20 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-131864.htm)
阅读量:28
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgfik1VBgFBYXx3Jijkq7L26Znz8PyZqaUpokPqDSK7smln8HsMyWgynYJX_uHxHcyeDDwSP3pmFRiXxaEu20bDje5OSVyX2k_Kr4MgLhcoe2TvE54OUR0zqF4PSm_vj2UOGVpGnjp3B-2Z8DgmjZdRYe3IO7LfS3aLHYV9Hjkt1ZtbJXNkbvvCSfbOWg=w640-h434)](https://blogger.googleusercontent.com/img/a/AVvXsEgfik1VBgFBYXx3Jijkq7L26Znz8PyZqaUpokPqDSK7smln8HsMyWgynYJX_uHxHcyeDDwSP3pmFRiXxaEu20bDje5OSVyX2k_Kr4MgLhcoe2TvE54OUR0zqF4PSm_vj2UOGVpGnjp3B-2Z8DgmjZdRYe3IO7LfS3aLHYV9Hjkt1ZtbJXNkbvvCSfbOWg)

* **Simple.** 3 files only, no installation required, just clone this repo an you're ready to go.
* **Powerful.** Thread-based navigation.
* **Stealthy.** Optimized to emulate user navigation.
* **Portable.** You can use this script on every unix-based OS.

This project was inspired by [noisy.py](https://github.com/1tayH/noisy "noisy.py")

## How It Works

1. URLs and keywords are loaded (either from partyloud.conf and badwords or from user-defined files)
2. If proxy flag has been used, proxy config will be tested
3. For each URL in ULR-list a thread is started, each thread as an [user agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent "user agent") associated
4. Each thread will start by sending an [HTTP](https://www.scaler.com/topics/hypertext-transfer-protocol/ "HTTP") request to the given URL
5. The response if filtered using the keywords in order to prevent 404s and [malformed](https://www.kitploit.com/search/label/Malformed "malformed") URLs
6. A new URL is choosen from the list generated after filering
7. Current thread sleeps for a random time
8. Actions from 4 to 7 are repeated using the new URL until user send kill signal (CTRL-C or enter key)

## Features

* Configurable urls list and blocklist
* Random DNS Mode : each request is done on a different DNS Server
* Multi-threaded request engine (# of thread are equal to # of urls in partyloud.conf)
* Error [recovery](https://www.kitploit.com/search/label/Recovery "recovery") mechanism to protect Engines from failures
* Spoofed User Agent prevent from [fingerprinting](https://www.kitploit.com/search/label/Fingerprinting "fingerprinting") (each engine has a different user agent)
* Dynamic UI

## Setup

Clone the repository:

```
git clone https://github.com/realtho/PartyLoud.git
```

Navigate to the [directory](https://www.kitploit.com/search/label/Directory "directory") and make the script executable:

```
cd PartyLoud
chmod +x partyloud.sh
```

Run 'partyloud':

## Usage

```
Usage: ./partyloud.sh [options...]

-d --dns <file>                    DNS Servers are sourced from specified FILE,
                                   each request will use a different DNS Server
                                   in the list
                                   !!WARNING THIS FEATURE IS EXPERIMENTAL!!
                                   !!PLEASE LET ME KNOW ISSUES ON GITHUB !!
-l --url-list <file>               read URL list from specified FILE
-b --blocklist <file>              read blocklist from specified FILE
-p --http-proxy <http://ip:port>   set a HTTP proxy
-s --https-proxy <https://ip:port> set a HTTPS proxy
-n --no-wait                       disable wait between one request and an other
-h --help                          dispaly this help
```

##### To stop the script press either enter or CRTL-C

## File Specifications

**In current release there is no input-validation on files.**
 If you find bugs or have suggestions on how to improve this features please help me by opening issues on GitHub

### Intro

###### If you don’t have special needs , default config files are just fine to get you started.

Default files are located in:

* [badwords](https://github.com/davideolgiati/PartyLoud/blob/master/badwords "badwords")
* [partyloud.conf](https://github.com/davideolgiati/PartyLoud/blob/master/partyloud.conf "partyloud.conf")
* [DNSList](https://github.com/davideolgiati/PartyLoud/blob/master/DNSList "DNSList")

Please note that file name and extension are not important, just content of files matter

#### [badwords](https://github.com/davideolgiati/PartyLoud/blob/master/badwords "badwords") - Keywords-based blocklist

[badwords](https://github.com/davideolgiati/PartyLoud/blob/master/badwords "badwords") is a keywords-based blocklist used to filter non-HTML content, images, document and so on.
 The default config as been created after several weeks of testing. If you really think you need a custom blocklist, my suggestion is to start by copy and modifying default config according to your needs.
 Here are some hints on how to create a great blocklist file:

| DO ✅ | DONT  |
| --- | --- |
| Use only ASCII chars | Define one-site-only rules |
| Try to keep the rules as general as possible | Define case-sensitive rules |
| Prefer relative path | Place more than one rule per line |

#### [partyloud.conf](https://github.com/davideolgiati/PartyLoud/blob/master/partyloud.conf "partyloud.conf") - ULR List

[partyloud.conf](https://github.com/davideolgiati/PartyLoud/blob/master/partyloud.conf "partyloud.conf") is a ULR List used as starting point for fake navigation generators.
 The goal here is to create a good list of sites containing a lot of URLs.
 Aside suggesting you not to use google, youtube and social networks related links, I've really no hints for you.

###### Note #1 - To work properly the URLs must be [well-formed](https://earthsci.stanford.edu/computing/hosting/urlsyntax/index.php "well-formed")

###### Note #2 - Even if the file contains 1000 lines only 10 are used (first 10, working on randomness)

###### Note #3 - Only one URL per line is allowed

#### [DNSList](https://github.com/davideolgiati/PartyLoud/blob/master/DNSList "DNSList") - DNS List

[DNSList](https://github.com/davideolgiati/PartyLoud/blob/master/DNSList "DNSList") is a List of DNS used as argument for random DNS feature. Random DNS is not enable by default, so the “default file” is really just a guide line and a test used while developing the function to se if everything was working as expected.
 The only suggestion here is to add as much address as possible to increase randomness.

###### Note #1 - Only one address per line is allowed

PartyLoud - A Simple Tool To Generate Fake Web Browsing And Mitigate Tracking
![PartyLoud - A Simple Tool To Generate Fake Web Browsing And Mitigate Tracking](https://blogger.googleusercontent.com/img/a/AVvXsEgfik1VBgFBYXx3Jijkq7L26Znz8PyZqaUpokPqDSK7smln8HsMyWgynYJX_uHxHcyeDDwSP3pmFRiXxaEu20bDje5OSVyX2k_Kr4MgLhcoe2TvE54OUR0zqF4PSm_vj2UOGVpGnjp3B-2Z8DgmjZdRYe3IO7LfS3aLHYV9Hjkt1ZtbJXNkbvvCSfbOWg=s72-w640-c-h434)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/10/partyloud-simple-tool-to-generate-fake.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)