---
title: 自动化信息收集工具的实现
url: https://www.se7ensec.cn/2023/02/14/%E8%87%AA%E5%8A%A8%E5%8C%96%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%E5%B7%A5%E5%85%B7%E7%9A%84%E5%AE%9E%E7%8E%B0/
source: Se7en's Blog|专注渗透测试。
date: 2023-02-15
fetch_date: 2025-10-04T06:34:56.691856
---

# 自动化信息收集工具的实现

[![Se7en's Blog|专注渗透测试。](/img/logo.png)](/)

[Home](/)[Archives](/archives)[Categories](/categories)[Tags](/tags)[About](/about)

![自动化信息收集工具的实现](https://raw.githubusercontent.com/r00tSe7en/pictures/master/hacking.png)

2023-02-14发表2023-02-15更新[渗透测试](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)6 分钟读完 (大约853个字)0次访问

# 自动化信息收集工具的实现

> 作为一个专业的渗透测试人员，自动化信息收集工具是必不可少的。

# 初衷

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

# 感谢

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

自动化信息收集工具的实现

<https://www.se7ensec.cn/2023/02/14/%E8%87%AA%E5%8A%A8%E5%8C%96%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%E5%B7%A5%E5%85%B7%E7%9A%84%E5%AE%9E%E7%8E%B0/>

###### 作者

Se7en

###### 发布于

2023-02-14

###### 更新于

2023-02-15

###### 许可协议

#[信息收集](/tags/%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86/)

[域渗透|Delegation](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-Delegation/)

### 评论

Please activate JavaScript for write a comment in LiveRe

### 目录

* [1初衷](#初衷)
  + [1.17{.}s{.}c{.}a{.}n [资产收集]](#7-s-c-a-n-资产收集)
  + [1.2Nuclei+Xray [漏扫集成]](#Nuclei-Xray-漏扫集成)
    - [1.2.1nuclei](#nuclei)
    - [1.2.2xray](#xray)
  + [1.3Search\_Server [资产整合]](#Search-Server-资产整合)
  + [1.4CobWeb [资产可视化]](#CobWeb-资产可视化)
    - [1.4.1网络显示关系可拖动](#网络显示关系可拖动)
    - [1.4.2可手动屏蔽选单独立高亮显示](#可手动屏蔽选单独立高亮显示)
* [2感谢](#感谢)

### 最新文章

[![自动化信息收集工具的实现](https://raw.githubusercontent.com/r00tSe7en/pictures/master/hacking.png)](/2023/02/14/%E8%87%AA%E5%8A%A8%E5%8C%96%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%E5%B7%A5%E5%85%B7%E7%9A%84%E5%AE%9E%E7%8E%B0/)

2023-02-14

[自动化信息收集工具的实现](/2023/02/14/%E8%87%AA%E5%8A%A8%E5%8C%96%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86%E5%B7%A5%E5%85%B7%E7%9A%84%E5%AE%9E%E7%8E%B0/)

[渗透测试](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)

[![域渗透|Delegation](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.07.12/who-am-i.jpg)](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-Delegation/)

2021-11-01

[域渗透|Delegation](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-Delegation/)

[渗透测试](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)

[![域渗透|Relay](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.07.12/who-am-i.jpg)](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-Relay/)

2021-11-01

[域渗透|Relay](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-Relay/)

[渗透测试](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)

[![域渗透|MS14-068](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.07.12/who-am-i.jpg)](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-MS14-068/)

2021-11-01

[域渗透|MS14-068](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-MS14-068/)

[渗透测试](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)

[![域渗透|票据伪造](https://raw.githubusercontent.com/r00tSe7en/pictures/master/2020.07.12/who-am-i.jpg)](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-%E7%A5%A8%E6%8D%AE%E4%BC%AA%E9%80%A0/)

2021-11-01

[域渗透|票据伪造](/2021/11/01/%E5%9F%9F%E6%B8%97%E9%80%8F-%E7%A5%A8%E6%8D%AE%E4%BC%AA%E9%80%A0/)

[渗透测试](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)

### 分类

* [渗透测试55](/categories/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)
* [生活随笔16](/categories/%E7%94%9F%E6%B4%BB%E9%9A%8F%E7%AC%94/)

### 标签

[00截断1](/tags/00%E6%88%AA%E6%96%AD/)

[BurpSuite1](/tags/BurpSuite/)

[BypassAV1](/tags/BypassAV/)

[GetShell3](/tags/GetShell/)

[Golang1](/tags/Golang/)

[HTML4](/tags/HTML/)

[JavaScript4](/tags/JavaScript/)

[PHP3](/tags/PHP/)

[Python1](/tags/Python/)

[SQL注入8](/tags/SQL%E6%B3%A8%E5%85%A5/)

[Short filename1](/tags/Short-filename/)

[Sqlmap3](/tags/Sqlmap/)

[WIN提权4](/tags/WIN%E6%8F%90%E6%9D%83/)

[XSS4](/tags/XSS/)

[一星期实战总结3](/tags/%E4%B8%80%E6%98%9F%E6%9C%9F%E5%AE%9E%E6%88%98%E6%80%BB%E7%BB%93/)

[乐理基础1](/tags/%E4%B9%90%E7%90%86%E5%9F%BA%E7%A1%80/)

[信息收集1](/tags/%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86/)

[内网渗透9](/tags/%E5%86%85%E7%BD%91%E6%B8%97%E9%80%8F/)

[域渗透6](/tags/%E5%9F%9F%E6%B8%97%E9%80%8F/)

[小技巧1](/tags/%E5%B0%8F%E6%8A%80%E5%B7%A7/)

[文件上传1](/tags/%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0/)

[旅行4](/tags/%E6%97%85%E8%A1%8C/)

[暴力破解1](/tags/%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/)

[水坑攻击2](/tags/%E6%B0%B4%E5%9D%91%E6%94%BB%E5%87%BB/)

[电音1](/tags/%E7%94%B5%E9%9F%B3/)

[端口渗透1](/tags/%E7%AB%AF%E5%8F%A3%E6%B8%97%E9%80%8F/)

[网站建设1](/tags/%E7%BD%91%E7%AB%99%E5%BB%BA%E8%AE%BE/)

[网络安全法1](/tags/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%B3%95/)

[解析漏洞1](/tags/%E8%A7%A3%E6%9E%90%E6%BC%8F%E6%B4%9E/)

[随想8](/tags/%E9%9A%8F%E6%83%B3/)

[面试经验1](/tags/%E9%9D%A2%E8%AF%95%E7%BB%8F%E9%AA%8C/)

[鱼叉攻击2](/tags/%E9%B1%BC%E5%8F%89%E6%94%BB%E5%87%BB/)

[![Se7en's Blog|专注渗透测试。](/img/logo.png)](/)

© 2023 Se7en  Powered by [Hexo](https://hexo.io/) & [Icarus](https://github.com/ppoffice/hexo-theme-icarus)
共0个访客

Copyright © 2016 - 2021 All Rights Reserved.[冀ICP备16029197号-1](https://beian.miit.gov.cn/)

×