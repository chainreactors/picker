---
title: 篡改NGINX配置文件可实现隐秘的网络流量劫持
url: https://www.anquanke.com/post/id/314763
source: 安全客-有思想的安全新媒体
date: 2026-02-06
fetch_date: 2026-02-07T04:07:57.098169
---

# 篡改NGINX配置文件可实现隐秘的网络流量劫持

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 篡改NGINX配置文件可实现隐秘的网络流量劫持

阅读量**19186**

发布时间 : 2026-02-06 11:08:33

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mark Tarre，文章来源：securityonline

原文地址：<https://securitybrief.asia/story/nginx-config-tampering-enables-stealth-web-traffic-hijack>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Datadog 安全研究团队监测到一起网络流量劫持攻击活动，攻击者通过篡改**NGINX 配置文件**，拦截用户的实时会话流量，并将其重定向至自身控制的服务器。

此次攻击的特点在于，攻击者从以往窃取存储数据，转向对活跃的网络流量进行长期隐秘监控与操控。攻击者潜伏在用户与目标网站的通信链路中，可窃取传输中的账户凭据、伪造用户身份，还能实时篡改网页内容或 API 响应，而受害者端的会话却看似一切正常。

Datadog 经溯源发现，该攻击活动的实施者与近期**React2Shell 漏洞**的利用者相关联。此次攻击所用的核心手段，是通过恶意 NGINX 配置，在用户与正规网络服务之间搭建起隐形的流量中转通道。

研究员克里斯托夫・塔法尼 – 德里佩尔与瑞安・西蒙在 React2Shell 漏洞公开后，持续监测相关利用行为，最终发现攻击者并未在服务器磁盘中植入新恶意程序，而是通过**篡改配置文件**实施攻击。

### 攻击目标特征

目前监测到的攻击目标集中于**亚洲地区的顶级域名**及相关基础设施，Datadog 指出，攻击者的攻击模式中，常以.in、.id、.pe、.bd、.edu、.gov、.th 结尾的域名为攻击对象。

分析结果还显示，攻击者使用了中国境内的托管基础设施，且借助**宝塔面板（BT）** 实施操作 —— 该面板是一款可管理 NGINX 及相关 Web 技术栈组件的主机管理界面。

Datadog 表示，此次攻击是攻击者**滥用正规系统机制**实现持久化驻留的典型案例。由于配置文件的修改属于日常运维操作的一部分，在业务繁忙的环境中，这类未授权的篡改行为更难被发现。

### 攻击实现原理

NGINX 是一款被广泛使用的 Web 服务器和反向代理软件，其配置文件用于定义运行行为，并管控网络流量的路由与处理规则。

攻击者在入侵过程中，滥用了 NGINX 的多个常用配置指令，Datadog 指出，此次攻击中被重点利用的核心指令包括**proxy\_pass、rewrite、proxy\_set\_header、location**。

* proxy\_pass：将客户端请求转发至后端服务器，常用于负载均衡或作为应用网关的核心配置；
* rewrite：修改客户端发起的请求 URL；
* proxy\_set\_header：修改传递给上游服务器的请求头信息；
* location：定义服务器对特定路径请求的处理规则。

攻击者并未在服务器中添加新的可执行文件，而是直接篡改已有的 NGINX 配置文件，这一做法大幅降低了被恶意程序特征检测工具、可疑可执行文件监测工具发现的概率。

### 多阶段攻击工具链

该攻击活动使用一套自动化的**多阶段攻击工具集**，初始入侵入口为一个名为**zx.sh**的脚本，该脚本负责协调后续所有攻击步骤，并通过 curl、wget 等常用工具拉取攻击组件。

若目标服务器中未安装上述工具，该工具集会自动调用一个 Bash 函数，建立原始 TCP 连接并发送 HTTP 请求，确保其能在工具被限制的环境中正常运行。

工具集的其中一个攻击阶段由**bt.sh**脚本实现，专门针对部署了宝塔面板的服务器：该脚本会遍历宝塔面板的 NGINX 配置路径 /www/server/panel/vhost/nginx，并在执行后续操作前，检查目标服务器中是否已存在被恶意代理的域名。

该脚本会通过**server\_name**变量，根据目标域名的顶级域名选择对应的注入模板，再通过硬编码变量选定注入路径；随后遍历配置文件，找到 server\_name 指令所在行，保存原始配置内容，在其后追加恶意配置代码，最终覆盖原配置文件。

为减少对目标服务器业务的干扰，脚本会尝试执行**NGINX 重载操作**，保证现有网络连接持续有效；若重载失败，则会尝试对 NGINX 进行完全重启。

另一款更高级的攻击脚本**4zdh.sh**，会将搜索范围扩大至 NGINX 的各类通用配置目录，包括 /etc/nginx/sites-enabled、/etc/nginx/conf.d、/etc/nginx/sites-available，同时也会检查目标服务器是否部署了宝塔面板。该脚本借助**csplit 和 awk 工具**识别配置文件中的服务器块，在注入恶意配置的同时，避免破坏原有配置的结构。

该攻击阶段还会检查目标服务器是否曾被注入过恶意配置，并为相关内容生成 MD5 哈希值；Datadog 的分析显示，脚本会在 /tmp/.domain\_group\_map.conf**路径下生成一个全局映射文件，且在尝试重载 NGINX 前，执行**nginx -t命令验证配置文件的有效性。

还有一个攻击阶段由**zdh.sh**脚本实现，专门针对 Linux 系统或容器化的 NGINX 环境，其扫描的配置路径范围相对较窄，主要瞄准 /etc/nginx/sites-enabled**目录，优先攻击.in、.id 等顶级域名对应的服务器；若重启操作失败，该脚本会通过**pkill 命令  实现兜底重启。

该攻击工具集还包含一个**映射与数据上报阶段**，由**ok.sh**脚本实现。Datadog 表示，该脚本会生成当前已生效的流量劫持规则报告，在 /dev/shm**或**/tmp**目录下创建名为**nginx\_scan.txt**的临时文件，最终将相关数据窃取并发送至攻击者的命令与控制服务器**158.94.210[.]227。

### 防御重点建议

此次攻击活动对安全防御方提出了更高要求：需将 Web 服务器的配置文件视为**安全管控面**，而非单纯的运维配置文件；同时也凸显了一类攻击的安全风险 —— 这类攻击不会安装明显的恶意程序，而终端安全工具的检测重点往往集中于此。

塔法尼 – 德里佩尔表示：“此次攻击暴露了传统 Web 安全领域中一个日益凸显的检测盲区，攻击者正越来越多地通过滥用正规的系统配置机制实现持久化驻留，而非部署特征明显的恶意软件。”

西蒙补充道：“在本次攻击中，攻击者始终选择篡改现有的 NGINX 配置文件，而非植入新的可执行文件。这意味着，仅依靠恶意程序检测或网络特征检测的防御手段，可能根本无法发现这类攻击行为。”

本文翻译自securityonline [原文链接](https://securitybrief.asia/story/nginx-config-tampering-enables-stealth-web-traffic-hijack)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314763](/post/id/314763)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securitybrief.asia/story/nginx-config-tampering-enables-stealth-web-traffic-hijack)

如若转载,请注明出处： <https://securitybrief.asia/story/nginx-config-tampering-enables-stealth-web-traffic-hijack>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1010**

* 粉丝
* **6**

### TA的文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11

### 相关文章

* ##### [网络攻击者利用Click Fix脚本中的DNS TXT记录执行恶意Power Shell命令](/post/id/314749)

  2026-02-06 11:13:00
* ##### [黑客正利用React服务端组件漏洞发起野外用攻击 部署恶意载荷](/post/id/314748)

  2026-02-06 11:12:32
* ##### [ValleyRAT伪装LINE安装程序发起攻击 窃取用户登录凭证](/post/id/314757)

  2026-02-06 11:12:01
* ##### [印度最高法院就WhatsApp数据共享作出里程碑式隐私裁决 判定其行为违规](/post/id/314774)

  2026-02-06 11:11:35
* ##### [PhantomVAI定制加载器借助RunPE工具发起攻击 针对用户实施恶意入侵](/post/id/314778)

  2026-02-06 11:11:11
* ##### [Xcode 26.3落地macOS苹果正式引入智能体式AI编码功能](/post/id/314784)

  2026-02-06 11:10:45
* ##### [RapidFort完成4200万美元A轮融资 深耕自动化漏洞修复领域](/post/id/314788)

  2026-02-06 11:10:18

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)