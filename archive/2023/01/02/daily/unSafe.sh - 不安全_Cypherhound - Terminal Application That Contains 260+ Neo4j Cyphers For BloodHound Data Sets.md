---
title: Cypherhound - Terminal Application That Contains 260+ Neo4j Cyphers For BloodHound Data Sets
url: https://buaq.net/go-143699.html
source: unSafe.sh - 不安全
date: 2023-01-02
fetch_date: 2025-10-04T02:51:53.406683
---

# Cypherhound - Terminal Application That Contains 260+ Neo4j Cyphers For BloodHound Data Sets

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

![](https://8aqnet.cdn.bcebos.com/53408060ba88e87b60667abc245e9ede.jpg)

Cypherhound - Terminal Application That Contains 260+ Neo4j Cyphers For BloodHound Data Sets

A Python3 terminal application that contains 260+ Neo4j cyphers for BloodHound data sets. W
*2023-1-1 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-143699.htm)
阅读量:56
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpOUJJMNT_swV5DemmX5q0F4Z57a2sDkF30LlKh3KM1YYlZxt_sWyPSr667o-bSi6j6NRM6umvUThrVJ2JMOJho0Ng63WtdzOGwet6Eq9-gqtwRkCQFpa7iVlBaC0K8YIs3QRFzxhD_nqf5P7eTB55BI4RZkIWtZUPTDmmE82lHN7EVJ8S7WycSar8RQ/w640-h358/cypherhound.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpOUJJMNT_swV5DemmX5q0F4Z57a2sDkF30LlKh3KM1YYlZxt_sWyPSr667o-bSi6j6NRM6umvUThrVJ2JMOJho0Ng63WtdzOGwet6Eq9-gqtwRkCQFpa7iVlBaC0K8YIs3QRFzxhD_nqf5P7eTB55BI4RZkIWtZUPTDmmE82lHN7EVJ8S7WycSar8RQ/s748/cypherhound.png)

A `Python3` terminal application that contains 260+ `Neo4j` cyphers for [BloodHound](https://www.kitploit.com/search/label/BloodHound "BloodHound") data sets.

## Why?

`BloodHound` is a staple tool for every red teamer. However, there are some negative side effects based on its design. I will cover the biggest pain points I've experienced and what this tool aims to address:

1. My tools think in lists - until my tools parse exported `JSON` graphs, I need graph results in a line-by-line format `.txt` file
2. Copy/pasting graph results - this plays into the first but do we need to explain this one?
3. Graphs can be too large to draw - the information contained in any graph can aid our goals as the attacker and we *need* to be able to view *all* data efficiently
4. Manually running custom cyphers is time-consuming - let's automate it :)

This tool can also help [blue teams](https://www.kitploit.com/search/label/Blue%20Teams "blue teams") to reveal detailed information about their [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") environments as well.

## Features

Take back control of your `BloodHound` data with `cypherhound`!

* 264 cyphers as of date
  + Set cyphers to search based on user input (user, group, and computer-specific)
  + User-defined regex cyphers
* User-defined exporting of all results
  + Default export will be just end object to be used as target list with tools
  + Raw export option available in `grep/cut/awk`-friendly format

## Installation

Make sure to have `python3` installed and run:

`python3 -m pip install -r requirements.txt`

## Usage

Start the program with: `python3 cypherhound.py -u <neo4j_username> -p <neo4j_password>`

## Commands

The full command menu is shown below:

```
Command Menu
```

## Important Notes

* The program is configured to use the default `Neo4j` database and `URI`
* Built for `BloodHound 4.2.0`, certain edges will not work for previous versions
* `Windows` users must run `pip3 install pyreadline3`
* Shortest paths exports are all the same (`raw` or not) due to their unpredictable number of nodes

## Future Goals

* Add cyphers for `Azure` edges

## Issues and Support

Please be descriptive with any issues you decide to open and if possible provide output (if applicable).

Cypherhound - Terminal Application That Contains 260+ Neo4j Cyphers For BloodHound Data Sets
![Cypherhound - Terminal Application That Contains 260+ Neo4j Cyphers For BloodHound Data Sets](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpOUJJMNT_swV5DemmX5q0F4Z57a2sDkF30LlKh3KM1YYlZxt_sWyPSr667o-bSi6j6NRM6umvUThrVJ2JMOJho0Ng63WtdzOGwet6Eq9-gqtwRkCQFpa7iVlBaC0K8YIs3QRFzxhD_nqf5P7eTB55BI4RZkIWtZUPTDmmE82lHN7EVJ8S7WycSar8RQ/s72-w640-c-h358/cypherhound.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/cypherhound-terminal-application-that.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)