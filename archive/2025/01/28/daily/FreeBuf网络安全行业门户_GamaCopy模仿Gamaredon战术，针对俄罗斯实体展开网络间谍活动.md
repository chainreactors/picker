---
title: GamaCopy模仿Gamaredon战术，针对俄罗斯实体展开网络间谍活动
url: https://www.freebuf.com/articles/network/420909.html
source: FreeBuf网络安全行业门户
date: 2025-01-28
fetch_date: 2025-10-06T20:09:32.557624
---

# GamaCopy模仿Gamaredon战术，针对俄罗斯实体展开网络间谍活动

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

GamaCopy模仿Gamaredon战术，针对俄罗斯实体展开网络间谍活动

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

GamaCopy模仿Gamaredon战术，针对俄罗斯实体展开网络间谍活动

2025-01-27 13:29:00

所属地 上海

![image](https://image.3001.net/images/20250127/1737968444323398_eeb44e5fd3ab46cb9c53797e7d0df216.png!small)

近日，一个此前未知的威胁组织被发现模仿与克里姆林宫相关的Gamaredon黑客组织的战术，针对俄语实体展开网络攻击。该活动被归因于一个名为**GamaCopy**的威胁集群，据评估，该集群与另一个名为Core Werewolf（也被追踪为Awaken Likho和PseudoGamaredon）的黑客组织存在重叠。

## 攻击手法与工具

根据Knownsec 404高级威胁情报团队的分析，攻击者利用与军事设施相关的内容作为诱饵，投放UltraVNC，从而使威胁行为者能够远程访问受感染的主机。该公司在上周发布的一份报告中表示：“该组织的战术、技术和程序（TTP）模仿了针对乌克兰发动攻击的Gamaredon组织。”

此次披露距离卡巴斯基揭露俄罗斯政府机构和工业企业成为Core Werewolf攻击目标已有近四个月。与GamaCopy不同的是，Core Werewolf通过鱼叉式网络钓鱼攻击为MeshCentral平台铺路，而非UltraVNC。

## 攻击链的起点与执行

攻击链的起点与俄罗斯网络安全公司描述的类似，即使用7-Zip创建的自解压（SFX）归档文件作为投放下一阶段有效载荷的渠道。这包括一个负责投放UltraVNC的批处理脚本，同时显示一个诱饵PDF文档。

![image](https://image.3001.net/images/20250127/1737968445533960_f7343fade069490cb72f9ad9852e398c.png!small)

UltraVNC可执行文件被命名为“OneDrivers.exe”，可能是为了伪装成与Microsoft OneDrive相关的二进制文件，从而逃避检测。

## 与Core Werewolf的相似之处

Knownsec 404表示，该活动与Core Werewolf的多个活动存在相似之处，包括使用7z-SFX文件安装和执行UltraVNC、通过443端口连接到服务器，以及使用EnableDelayedExpansion命令。该公司指出：“自曝光以来，该组织频繁模仿Gararedon组织的TTP，并巧妙地利用开源工具作为掩护，在混淆公众的同时实现其目标。”

## 俄乌战争背景下的威胁组织

GamaCopy是俄乌战争爆发后针对俄罗斯组织的众多威胁行为者之一，其他组织还包括Sticky Werewolf（又名PhaseShifters）、Venture Wolf和Paper Werewolf。Positive Technologies的Irina Zinovkina表示：“像PhaseShifters、PseudoGamaredon和Fluffy Wolf这样的组织因其旨在窃取数据的持续网络钓鱼活动而引人注目。”

**参考来源：**

> [GamaCopy Mimics Gamaredon Tactics in Cyber Espionage Targeting Russian Entities](https://thehackernews.com/2025/01/gamacopy-mimics-gamaredon-tactics-in.html)

# 终端安全 # 企业安全

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)