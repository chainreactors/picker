---
title: “ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络
url: https://www.4hou.com/posts/J13l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-24
fetch_date: 2025-11-25T03:11:42.710884
---

# “ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络

“ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# “ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10222

收藏

导语：两轮攻击均利用了编号为CVE-2023-48022的旧版高危漏洞。

一场名为“ShadowRay 2.0”的全球攻击活动正利用一处旧版代码执行漏洞，劫持暴露在公网的Ray集群，将其改造为具备自传播能力的加密货币挖矿僵尸网络。

Ray是由Anyscale开发的开源框架，可在以“集群”或“头节点”形式组织的分布式计算生态中，助力构建和扩展人工智能（AI）及Python应用。

据研究人员介绍，他们追踪的威胁者“IronErn440”正使用AI生成的载荷，攻击公网可访问的易受攻击Ray基础设施。研究人员指出，此类恶意活动不仅限于加密货币挖矿，部分情况下还涉及数据与凭证窃取，以及发起分布式拒绝服务（DDoS）攻击。

**新攻击活动，旧（未修复）漏洞**

“ShadowRay 2.0”是此前另一轮“ShadowRay”攻击活动的延续——该活动由Oligo曝光，活跃于2023年9月至2024年3月期间。

Oligo研究人员发现，两轮攻击均利用了编号为CVE-2023-48022的旧版高危漏洞。这一安全问题尚未推出修复补丁，原因是Ray的设计初衷是运行在“严格受控的网络环境”这类可信环境中。

但研究人员表示，目前公网可访问的Ray服务器已超23万台，较“首次发现ShadowRay活动时观测到的数千台”出现大幅激增。

Oligo在今日发布的报告中提到，已监测到两轮攻击浪潮：一轮通过滥用GitLab分发载荷，于11月5日终止；另一轮则滥用GitHub，自11月17日起持续至今。

![github.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251119/1763535592101745.jpg "1763535436286201.jpg")

恶意的 GitHub 仓库

**载荷功能解析**

Oligo指出，攻击中使用的载荷由大语言模型生成。这一结论基于对代码结构、现有注释及错误处理模式的分析得出。

例如，研究人员在对某一载荷进行反混淆后发现，其包含“文档字符串和无意义回显语句，这强烈表明代码由LLM生成”。

![code(1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251119/1763535593185909.jpg "1763535501212943.jpg")

有效负载的一部分

攻击者利用CVE-2023-48022漏洞，向Ray未授权的Jobs API提交任务，运行多阶段Bash与Python载荷，并借助平台的编排能力在所有节点部署恶意软件，实现集群间的自主传播。

其中的加密货币挖矿模块似乎同样由AI生成，会检测可用的CPU、GPU资源及访问权限类型。研究人员在载荷代码中发现，攻击者偏好“至少8核且具备root权限”的系统，并将此类系统称为“a very good boy”（意为“非常理想的目标”）。

该模块使用XMRig软件挖掘门罗币（Monero），且仅占用60%的处理能力，以规避即时检测。

Oligo发现，挖矿程序被植入具有迷惑性的文件路径，并使用“dns-filter”等伪造进程名掩盖活动痕迹；同时通过定时任务和修改systemd配置实现持久化驻留。

另一处有趣的发现是：攻击者会确保自己是唯一利用被劫持Ray集群挖矿的主体——他们会终止其他竞争对手的挖矿脚本，并通过修改/etc/hosts文件和iptables规则屏蔽其他矿池。

![killminers.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251119/1763535594874224.jpg "1763535543115086.jpg")

矿工配置

除加密货币挖矿外，该恶意软件还会向攻击者基础设施开启多个Python反向shell，以实现交互式控制，进而获取并窃取工作负载环境数据、MySQL数据库凭证、专有AI模型及集群中存储的源代码。

此外，它还可利用Sockstress工具发起DDoS攻击——该工具通过原始套接字建立大量TCP连接，利用“非对称资源消耗”的原理瘫痪目标。

从攻击者创建的定时任务来看，Oligo发现有一个脚本每15分钟执行一次，用于检查GitHub仓库中是否存在更新后的载荷。

![persistence.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251119/1763535599736734.jpg "1763535599736734.jpg")

设置持久化机制

**“ShadowRay 2.0”防御建议**

由于CVE-2023-48022漏洞目前尚无修复补丁，建议Ray用户在部署集群时遵循厂商推荐的“最佳实践”。

在首次“ShadowRay”攻击活动被曝光后，Anyscale已就该问题发布更新说明，列出多项建议，其中包括“将Ray部署在安全可信的环境中”。同时，应通过防火墙规则和安全组策略保护集群，防止未授权访问。

安全研究人员还建议在Ray控制台端口（默认8265）基础上增加授权验证，并对AI集群实施持续监控，以识别异常活动。

文章来源自：https://www.bleepingcomputer.com/news/security/new-shadowray-attacks-convert-ray-clusters-into-crypto-miners/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?icY9gy4y)

#### 你可能感兴趣的

* [![]()

  “ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)
* [![]()

  Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)
* [![]()

  公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)
* [![]()

  Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)
* [![]()

  Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)
* [![]()

  捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [“ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)
  2025-11-24 12:00:00
* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)
  2025-11-21 12:01:00
* [公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)
  2025-11-21 10:13:24
* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)
  2025-11-19 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [“ShadowRay 2.0”全球攻击活动：利用旧漏洞劫持Ray集群构建自传播挖矿僵尸网络](https://www.4hou.com/posts/J13l)

  胡金鱼
* [Cloudflare将本周大规模服务中断事件归咎于数据库问题](https://www.4hou.com/posts/MX3B)

  胡金鱼
* [公安部计算机信息系统安全产品质量监督检验中心检测发现40款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/Dx3Y)

  胡金鱼
* [Finger协议遭滥用 沦为 ClickFix 恶意软件攻击工具](https://www.4hou.com/posts/omLN)

  胡金鱼
* [Cloudflare全球网络服务突发中断 多国用户遭遇访问故障](https://www.4hou.com/posts/Ey3K)

  胡金鱼
* [捷豹路虎遭网络攻击 损失超 2.2 亿美元](https://www.4hou.com/posts/pnMr)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)