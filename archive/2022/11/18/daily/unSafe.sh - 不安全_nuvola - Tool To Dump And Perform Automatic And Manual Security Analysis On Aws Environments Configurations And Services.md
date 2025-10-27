---
title: nuvola - Tool To Dump And Perform Automatic And Manual Security Analysis On Aws Environments Configurations And Services
url: https://buaq.net/go-136094.html
source: unSafe.sh - 不安全
date: 2022-11-18
fetch_date: 2025-10-03T23:05:22.252704
---

# nuvola - Tool To Dump And Perform Automatic And Manual Security Analysis On Aws Environments Configurations And Services

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

![](https://8aqnet.cdn.bcebos.com/d6bb4c76eb1f8394ce4e865b0c211555.jpg)

nuvola - Tool To Dump And Perform Automatic And Manual Security Analysis On Aws Environments Configurations And Services

nuvola (with the lowercase n) is a tool to dump and perform automatic and manual security an
*2022-11-17 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-136094.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgzmURPzSN2TgWknr8VkU8lZFi3OmYW__FqXcXK7E9EggsniyF5TvTVmMkKbOIKnap0o2Y1DI6g4cLEOzbHGR0qrBmOjamJvS2h2TdFbUwECaXkQxQzYiAZus36OWa753eMRyLrSlm0mKYO5tC58u_46q3tBSefqEQX4QwN7BrEixhuXt0TQqQOXgUQ3Q=s320)](https://blogger.googleusercontent.com/img/a/AVvXsEgzmURPzSN2TgWknr8VkU8lZFi3OmYW__FqXcXK7E9EggsniyF5TvTVmMkKbOIKnap0o2Y1DI6g4cLEOzbHGR0qrBmOjamJvS2h2TdFbUwECaXkQxQzYiAZus36OWa753eMRyLrSlm0mKYO5tC58u_46q3tBSefqEQX4QwN7BrEixhuXt0TQqQOXgUQ3Q)

nuvola (with the lowercase n) is a tool to dump and perform automatic and manual security analysis on AWS environments configurations and services using predefined, extensible and custom rules created using a simple Yaml syntax.

The general idea behind this project is to create an abstracted digital twin of a cloud platform. For a more concrete example: nuvola reflects the [BloodHound](https://www.kitploit.com/search/label/BloodHound "BloodHound") traits used for [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") analysis but on cloud environments (at the moment only AWS).

The usage of a graph database also increases the possibility of finding different and innovative attack paths and can be used as an offline, centralised and lightweight digital twin.

## Quick Start

### Requirements

* `docker-compose` installed
* an AWS account configured to be used with `awscli` with full access to the cloud resources, better if in *ReadOnly* mode (the policy `arn:aws:iam::aws:policy/ReadOnlyAccess` is fine)

### Setup

1. Clone the repository

```
git clone --depth=1 https://github.com/primait/nuvola.git; cd nuvola
```

2. Create and edit, if required, the `.env` file to set your DB username/password/URL

3. Start the Neo4j docker instance

4. Build the tool

### Usage

1. Firstly you need to dump all the supported AWS services configurations and load the data into the Neo4j database:

```
./nuvola dump -profile default_RO -outputdir ~/DumpDumpFolder -format zip
```

2. To import a previously executed dump operation into the Neo4j database:

```
./nuvola assess -import ~/DumpDumpFolder/nuvola-default_RO_20220901.zip
```

3. To only perform static assessments on the data loaded into the Neo4j database using the [predefined ruleset](https://github.com/primait/nuvola/tree/master/assess/rules "predefined ruleset"):

4. Or use [Neo4j Browser](https://neo4j.com/docs/operations-manual/current/installation/neo4j-browser/ "Neo4j Browser") to manually explore the digital twin.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjQbhoTT8iOZvEXyq-5kXJNngssFxDFe-QmxWTq817OKgNJNDzsJu7KH4bcwagoqFcbOzC2BRsx4ME8h1U0Xijgd-f_OAD2sx9nFIL_JzpvzmhGcUNxbIdN-yOLC8qzUzTDMsNVOz6OiVv3LyTyaljP3kYmEOiGiGw9XebHCthRKNnWXhMfB6Jd2FWCGQ=w640-h276)](https://blogger.googleusercontent.com/img/a/AVvXsEjQbhoTT8iOZvEXyq-5kXJNngssFxDFe-QmxWTq817OKgNJNDzsJu7KH4bcwagoqFcbOzC2BRsx4ME8h1U0Xijgd-f_OAD2sx9nFIL_JzpvzmhGcUNxbIdN-yOLC8qzUzTDMsNVOz6OiVv3LyTyaljP3kYmEOiGiGw9XebHCthRKNnWXhMfB6Jd2FWCGQ)

## About nuvola

To get started with nuvola and its database schema, check out the nuvola [Wiki](https://github.com/primait/nuvola/wiki "Wiki").

No data is sent or shared with Prima Assicurazioni.

## How to contribute

* reporting bugs and issues
* reporting new improvements
* reviewing issues and pull requests
* fixing bugs and issues
* creating new rules
* improving the overall quality

## Presentations

* RomHack 2022
  + [Slides](https://github.com/primait/nuvola/tree/master/assets/slides/RomHack_2022-You_shall_not_PassRole.pdf "Slides")
  + [Demos](https://github.com/primait/nuvola/tree/master/assets/demos/ "Demos")

## License

nuvola uses [graph theory](https://www.kitploit.com/search/label/Graph%20Theory "graph theory") to reveal possible attack paths and security [misconfigurations](https://www.kitploit.com/search/label/Misconfigurations "misconfigurations") on cloud environments.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is [distributed](https://www.kitploit.com/search/label/Distributed "distributed") in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this repository and program. If not, see [http://www.gnu.org/licenses/](https://www.gnu.org/licenses/ "http://www.gnu.org/licenses/").

nuvola - Tool To Dump And Perform Automatic And Manual Security Analysis On Aws Environments Configurations And Services
![nuvola - Tool To Dump And Perform Automatic And Manual Security Analysis On Aws Environments Configurations And Services](https://blogger.googleusercontent.com/img/a/AVvXsEgzmURPzSN2TgWknr8VkU8lZFi3OmYW__FqXcXK7E9EggsniyF5TvTVmMkKbOIKnap0o2Y1DI6g4cLEOzbHGR0qrBmOjamJvS2h2TdFbUwECaXkQxQzYiAZus36OWa753eMRyLrSlm0mKYO5tC58u_46q3tBSefqEQX4QwN7BrEixhuXt0TQqQOXgUQ3Q=s72-c)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/nuvola-tool-to-dump-and-perform.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)