---
title: ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务
url: https://www.anquanke.com/post/id/312381
source: 安全客-有思想的安全新媒体
date: 2025-09-25
fetch_date: 2025-10-02T20:37:58.479860
---

# ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务

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

# ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务

阅读量**86541**

发布时间 : 2025-09-24 16:40:43

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ravie Lakshmanan，文章来源：https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html

原文地址：<https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

根据 Darktrace 的分析，ShadowV2 主要针对亚马逊云（AWS）上的配置错误的 Docker 容器，投递基于 Go 的恶意软件，将受感染系统转化为攻击节点，进一步纳入庞大的 DDoS 僵尸网络。研究人员指出，他们在 2025 年 6 月 24 日通过蜜罐监测到了这一恶意软件。

Darktrace 安全研究员 Nathaniel Bill 表示，本次攻击的核心是一个托管在 GitHub Codespaces 上的 Python C2（命令与控制）框架。与传统活动相比，ShadowV2 的最大不同在于其攻击工具集的高度复杂性。攻击者不仅能实施 HTTP/2 Rapid Reset 攻击，还能绕过 Cloudflare 的 Under Attack Mode（UAM），并执行大规模 HTTP 洪水攻击，体现出威胁行为者在结合多种 DDoS 技术与定向利用方面的成熟能力。

值得注意的是，ShadowV2 包含一个基于 Python 的扩散模块，专门用于入侵 AWS EC2 上暴露的 Docker 守护进程；同时，基于 Go 的远程访问木马（RAT）则支持命令执行，并通过 HTTP 协议与攻击者通信。研究人员将 ShadowV2 形容为一个\*\*“高级攻击平台”\*\*。

与以往直接在受害者机器上拉取 Docker Hub 镜像的方式不同，ShadowV2 首先会从 Ubuntu 基础镜像启动一个通用容器，然后在其中安装攻击所需工具，再构建并部署新的镜像。这种方法的动机尚不明确，但 Darktrace 认为可能是为了减少在受害主机上留下取证痕迹。

![]()

当容器环境就绪后，会执行一个基于 Go 的 ELF 二进制文件，与位于 shadow.aurozacloud[.]xyz 的 C2 服务器建立通信，定期发送心跳信息并拉取新指令。该恶意软件还具备实施 HTTP/2 Rapid Reset 攻击的能力，并借助 ChromeDP 工具尝试绕过 Cloudflare 的 JavaScript 挑战，获取通行 Cookie。不过研究人员指出，这种方式大概率无法生效，因为 Cloudflare 的机制专门针对无头浏览器流量设计。

进一步分析表明，该 C2 基础设施隐藏在 Cloudflare 之后，真实源站难以追踪。后端使用了 FastAPI 和 Pydantic，并提供登录面板与操作界面，显示出攻击者正以 DDoS 租用服务 为目标进行产品化开发。其 API 接口允许操作者新增、更新或删除用户，配置不同类型的攻击，分配攻击节点清单，甚至指定排除目标。

Nathaniel Bill 总结称：“通过容器化、API 扩展以及完整的用户界面，ShadowV2 清晰展示了\*\*‘网络犯罪即服务’的持续演进\*\*。利用 Go RAT 模块化功能，并向操作者暴露结构化 API，这种模式凸显了部分威胁行为者的专业化水平。”

与此同时，F5 Labs 发现了另一个基于 Mozilla 浏览器 User-Agent 伪造的扫描僵尸网络，该网络利用超过 11,690 种不同 UA 字符串，持续探测暴露在互联网上的系统漏洞。

另一方面，Cloudflare 今日在 X 平台发文称，其自主防御系统阻止了一场史上最大规模的 DDoS 攻击，攻击峰值高达 22.2 Tbps 和 106 亿 PPS，攻击仅持续 40 秒。就在本月早些时候，Cloudflare 还曾披露拦截了一起 11.5 Tbps 的超大流量攻击，持续时间同样仅为数十秒。

来自中国的奇安信 XLab 近日发布报告称，另一款名为 AISURU 的僵尸网络（AIRASHI 变种）正是部分攻击的幕后推手。该网络感染了近 30 万台设备，主要为路由器与安防摄像头，由三名核心成员负责开发、漏洞整合和销售。最新版本增加了 改进的 RC4 算法、自动测速选择低延迟服务器、检测 tcpdump/Wireshark 等网络工具及 VMware、QEMU、VirtualBox、KVM 等虚拟化环境。

XLab 强调，AISURU 攻击范围遍布全球，目标涉及中国、美国、德国、英国和香港等地区。除了传统的 DDoS 功能，新版本还支持代理服务，反映出在全球执法打击压力上升的背景下，对匿名化服务的需求正不断增长。

本文翻译自https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html [原文链接](https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/312381](/post/id/312381)

安全KER - 有思想的安全新媒体

本文转载自: <https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html>

如若转载,请注明出处： <https://thehackernews.com/2025/09/shadowv2-botnet-exploits-misconfigured.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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