---
title: 【漏洞通报】Harbor 镜像仓库未授权访问漏洞
url: https://buaq.net/go-145891.html
source: unSafe.sh - 不安全
date: 2023-01-18
fetch_date: 2025-10-04T04:07:22.604194
---

# 【漏洞通报】Harbor 镜像仓库未授权访问漏洞

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

![](https://8aqnet.cdn.bcebos.com/aea0b2d9d56038e5554386c1df5f8e79.jpg)

【漏洞通报】Harbor 镜像仓库未授权访问漏洞

Harbor 是一个开源的 Docker Registry 管理项目，用于托管容器镜像。Harbor 镜像仓库存在配置不当导致的访问控制缺陷，攻击者可通过页面搜索镜像名称
*2023-1-17 23:9:36
Author: [nosec.org(查看原文)](/jump-145891.htm)
阅读量:82
收藏*

---

![1.jpg](https://nosec.org/avatar/uploads/attach/image/cf414dfc5d878675dec69769de3bf521/1.jpg)

Harbor 是一个开源的 Docker Registry 管理项目，用于托管容器镜像。

Harbor 镜像仓库存在配置不当导致的访问控制缺陷，攻击者可通过页面搜索镜像名称，绕过登陆验证逻辑，直接查看结果中未授权的私有镜像仓库并获取仓库信息（Pull、Push的时间和commit信息，以及镜像存在的漏洞信息等）。

本次漏洞影响范围如下：

| Harbor 所有版本 |
| --- |

FOFA Query：

| app="HARBOR" |
| --- |

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（app="HARBOR"）共有 25,524 个相关服务对外开放。中国使用数量最多，共有 15,796 个；美国第二，共有 2,640 个；德国第三，共有 1,310 个；中国香港特别行政区第四，共有679 个；新加坡第五，共有 650 个。

全球范围内分布情况如下（仅为分布情况，非漏洞影响情况）：

![2.png](https://nosec.org/avatar/uploads/attach/image/957fd6d9f66106d62a236a6467e02900/2.png)

中国大陆地区北京使用数量最多，共有1,964 个；广东第二，共有 1,582 个；浙江第三，共有 1,438 个；上海第四，共有 1,228 个；四川第五，共有 440 个。

![3.png](https://nosec.org/avatar/uploads/attach/image/6583dc2242b955172bc30bcdb2851f5d/3.png)

白帽汇安全研究院第一时间复现了该漏洞：

![4.png](https://nosec.org/avatar/uploads/attach/image/dc1193ffe79522037ff793c9149ccafe/4.png)

此漏洞为配置不当导致，建议用户修改配置：“项目设置”——“配置管理”——“项目仓库”中的“公开”取消勾选，即可限制公开访问。如图：

![5.png](https://nosec.org/avatar/uploads/attach/image/55ac1c8749ae7dd24c1aa28878e0c9cf/5.png)

[1.]  <https://github.com/lanqingaa/123/blob/main/README.md>

文章来源: https://nosec.org/home/detail/5061.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)