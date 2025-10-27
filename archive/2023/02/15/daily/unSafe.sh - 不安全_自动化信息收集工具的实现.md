---
title: 自动化信息收集工具的实现
url: https://buaq.net/go-149392.html
source: unSafe.sh - 不安全
date: 2023-02-15
fetch_date: 2025-10-04T06:36:04.695678
---

# 自动化信息收集工具的实现

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

![](https://8aqnet.cdn.bcebos.com/77759e8dc376562754c51bf03ae2fb00.jpg)

自动化信息收集工具的实现

作为一个专业的渗透测试人员，自动化信息收集工具是必不可少的。起因一次对某大型目标的渗透，需要对几百个根域进行信息收集工作，在繁杂的信息收集工作中，重复而又单调的操作会极大消耗我们的耐心，人工去做
*2023-2-14 22:10:24
Author: [www.se7ensec.cn(查看原文)](/jump-149392.htm)
阅读量:75
收藏*

---

> 作为一个专业的渗透测试人员，自动化信息收集工具是必不可少的。

起因一次对某大型目标的渗透，需要对几百个根域进行信息收集工作，在繁杂的信息收集工作中，重复而又单调的操作会极大消耗我们的耐心，人工去做这个事情的话非常不现实的。

于是花了周末两天的时间，做了下众多扫描器的调研，大部分环境配置麻烦不说且系统过于笨重，使用起来十分不方便。

在权衡了系统资源消耗，硬件要求，程序人工可干预性、以及后期代码维护的成本，最终用`Python + Shell`实现了雏形版本，参考了一下[InCloud GitHub云上扫描器](https://github.com/inbug-team/InCloud) 的部分思路，勉强完成了一些基础工具的整合，一些细节的处理都不太完善。

如今经过一年多时间的打磨，基本可以覆盖到信息收集的每一个阶段。

## 7{.}s{.}c{.}a{.}n [资产收集]

> 未开源

我对它的定义是 **“ 轻量、简洁、可扩展、可自定义、基于实战优化后的参数设置”，**下面放一个程序运行流程的思维导图。

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2023.02.14/1.jpg)

## Nuclei+Xray [漏扫集成]

后续的web漏洞主动探测使用`nuclei + xray`

### nuclei

Fast and customizable vulnerability scanner based on simple YAML based DSL.

<https://github.com/projectdiscovery/nuclei>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` nuclei -t /root/nuclei-templates/ -severity critical,high,medium -l all_active_webs.txt -bs 50 -c 50 -rl 150 -nc | anew -q all_nuclei_output.txt ``` |

### xray

多线程调用xray+rad进行自动扫描

<https://github.com/sv3nbeast/X-AutoXray>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` python3 X-AutoXray.py all/all_active_webs.txt all/all_xray_result/ ``` |

## Search\_Server [资产整合]

> 未开源

后期使用发现，`Web`资产多了看起来非常乱，不够直观。

于是基于`Python Flask`实现了一个程序，以网页形式整合`httpx + gowitness`的探测结果，支持 `任意单列排序`、`任意单列搜索`、`全局搜索`（这里要感谢下：[@me1ons](https://github.com/me1ons) 实现的此功能）、`行数统计`、`截图相似度排序`。

![](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2023.02.14/2.jpg)

## CobWeb [资产可视化]

> 已开源：<https://github.com/r00tSe7en/cobweb>

后期使用发现，大型目标收集到的子域名和解析IP的关系错综复杂，肉眼分析起来费时又费力。

`CobWeb`蛛网 将关联数据进行可视化显示，方便快速定位目标资产。

测试页：<https://www.se7ensec.cn/cobweb/>

### 网络显示关系可拖动

![](https://raw.githubusercontent.com/r00tSe7en/cobweb/main/img/cobweb1.jpg)

### 可手动屏蔽选单独立高亮显示

![](https://raw.githubusercontent.com/r00tSe7en/cobweb/main/img/cobweb2.jpg)

<https://github.com/shmilylty/OneForAll>

<https://github.com/projectdiscovery/subfinder>

<https://github.com/boy-hack/ksubdomain>

<https://github.com/lijiejie/subDomainsBrute>

<https://github.com/cgboal/sonarsearch>

<https://github.com/projectdiscovery/dnsx>

<https://github.com/zu1k/nali>

<https://github.com/projectdiscovery/naabu>

<https://github.com/projectdiscovery/httpx>

<https://github.com/P1kAju/httpx>

<https://github.com/adamgordonbell/csvquote>

<https://github.com/projectdiscovery/nuclei>

<https://github.com/soimort/translate-shell>

<https://github.com/sensepost/gowitness>

<https://github.com/lcvvvv/kscan>

<https://github.com/tomnomnom/anew>

<https://github.com/lc/gau>

<https://github.com/six2dez/ipcdn>

<https://github.com/ThreatUnkown/jsubfinder>

<https://github.com/ProjectAnte/dnsgen>

<https://github.com/sv3nbeast/X-AutoXray>

文章来源: https://www.se7ensec.cn/2023/02/14/%E8%87%AA%E5%8A%A8%E5%8C%96%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%E5%B7%A5%E5%85%B7%E7%9A%84%E5%AE%9E%E7%8E%B0/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)