---
title: 新威胁组织GamaCopy模仿俄罗斯Gamaredon APT，针对俄语目标发起攻击
url: https://www.freebuf.com/articles/endpoint/420915.html
source: FreeBuf网络安全行业门户
date: 2025-01-28
fetch_date: 2025-10-06T20:09:32.979813
---

# 新威胁组织GamaCopy模仿俄罗斯Gamaredon APT，针对俄语目标发起攻击

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

新威胁组织GamaCopy模仿俄罗斯Gamaredon APT，针对俄语目标发起攻击

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

新威胁组织GamaCopy模仿俄罗斯Gamaredon APT，针对俄语目标发起攻击

2025-01-27 12:28:26

所属地 上海

![](https://image.3001.net/images/20250127/1737982839188461_155f0fa3d9fa413b8fbfc6b1a4c10d55.png!small)

## GamaCopy模仿俄罗斯Gamaredon APT，针对俄语目标发起攻击

近日，Knownsec 404高级威胁情报团队分析了一起针对俄语目标的攻击活动。攻击者使用军事主题的诱饵文档、7z自解压文件（SFX）作为载荷，并利用UltraVNC进行远程控制，模仿了俄罗斯Gamaredon APT组织的战术、技术和程序（TTPs）。研究人员将该活动与APT组织Core Werewolf（又名Awaken Likho、PseudoGamaredon）联系起来，由于它模仿了Gamaredon，因此研究人员将其命名为GamaCopy。

GamaCopy自2021年8月以来一直活跃，并于2023年6月被发现。该组织主要针对俄罗斯的国防和基础设施领域，模仿Gamaredon的TTPs。

Knownsec 404高级威胁情报团队在报告中指出：“通过追踪样本来源，我们将其与Core Werewolf组织关联起来，该组织曾多次对俄罗斯发起攻击。众所周知，在南亚地区存在另一对有趣的APT攻击组织，即SideWinder和SideCopy，它们之间存在着爱恨交织的关系。此次发现的攻击活动模仿了针对乌克兰的Gamaredon组织，因此可以将其命名为GamaCopy。”

## GamaCopy的攻击手法与特点

研究人员注意到，其他安全厂商曾将多个同类型的历史样本归因于Gamaredon组织。GamaCopy通过成功的假旗行动，欺骗了一些未进行深入分析的安全厂商。

攻击链始于一个7-Zip自解压（SFX）文件，该文件释放载荷，包括一个用于安装UltraVNC并显示诱饵PDF的批处理脚本。攻击者将UltraVNC可执行文件重命名为“OneDrivers.exe”，试图模仿微软OneDrive二进制文件以逃避检测。

GamaCopy攻击中使用的诱饵文档主要围绕军事设施，反映了俄乌冲突的主题。然而，与Gamaredon使用乌克兰语诱饵不同，GamaCopy针对的是俄语用户。

![image](https://image.3001.net/images/20250127/1737982840383119_e5724b0ae6af4d3b9d5fbf730d380f99.png!small)

## 研究人员对GamaCopy的评估

报告总结道：“从代码相似性、诱饵文档中的语言使用以及端口资产的角度来看，更倾向于将此次发现的攻击样本归因于GamaCopy组织。自曝光以来，该组织频繁模仿Gamaredon组织的TTPs，并巧妙地利用开源工具作为掩护，在实现自身目标的同时混淆公众视听。”

Knownsec 404团队还发布了此次攻击活动的入侵指标（IoCs）。

**参考来源：**

> [GamaCopy targets Russia mimicking Russia-linked Gamaredon APT](https://securityaffairs.com/173501/apt/gamacopy-mimics-russia-linked-gamaredon-apt.html)

# 终端安全 # 安全报告

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