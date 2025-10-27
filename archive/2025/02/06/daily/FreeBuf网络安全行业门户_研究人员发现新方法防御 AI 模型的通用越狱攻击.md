---
title: 研究人员发现新方法防御 AI 模型的通用越狱攻击
url: https://www.freebuf.com/news/421076.html
source: FreeBuf网络安全行业门户
date: 2025-02-06
fetch_date: 2025-10-06T20:35:40.091401
---

# 研究人员发现新方法防御 AI 模型的通用越狱攻击

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

研究人员发现新方法防御 AI 模型的通用越狱攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

研究人员发现新方法防御 AI 模型的通用越狱攻击

2025-02-05 10:30:00

所属地 上海

来自Anthropic保障研究团队的研究人员开发了一种新方法，用于保护人工智能模型免受通用越狱攻击。这种创新方法被称为“宪法分类器”，已在数千小时的人类红队测试和合成评估中表现出了显著的抗攻击能力。

![](https://image.3001.net/images/20250205/1738724526_67a2d4aebfab27133e88c.jpg!small)

通用越狱攻击是指攻击者通过精心设计的输入，绕过人工智能模型的安全防护，迫使模型产生违反其安全准则的有害回应。这些攻击可能涉及用长提示信息淹没模型，或者使用不寻常的大写方式改变输入风格，尽管经过广泛的安全训练，大型语言模型仍然容易受到此类漏洞利用的攻击。

## 宪法分类器的工作原理

宪法分类器是基于合成数据训练的输入和输出分类器。它们能够过滤掉大多数越狱尝试，同时将过度拒绝率降至最低，并保持适度的计算开销。该系统基于“宪法”——一份定义允许和禁止内容类别的原则清单。

![](https://image.3001.net/images/20250205/1738724585_67a2d4e92987e73ff8bbc.jpg!small)

宪法分类器的训练和实施（来源：Anthropic）

**以下是其工作原理：**

* **宪法制定：**制定一部宪法，明确无害和有害的类别。
* **合成数据生成：**根据宪法，生成大量涵盖所有内容类别的合成提示和模型完成内容。这些数据通过翻译成不同语言以及模仿已知越狱风格进行增强。
* **分类器训练：**使用合成数据训练输入和输出分类器，以检测和阻止有害内容。
* **部署：**将这些分类器作为保护 AI 模型的安全措施实施。

## 实际测试结果

在一个漏洞赏金计划中，183名活跃参与者花费超过3000小时，试图对保护Claude 3.5 Sonnet的原型系统进行越狱。尽管奖金丰厚，但并未发现任何通用越狱漏洞。不过，该原型系统的过度拒绝率和计算成本较高。

![](https://image.3001.net/images/20250205/1738724670_67a2d53e38c377183b82a.jpg!small)

自动化评估结果（来源：Anthropic）

宪法分类器的更新版本在Claude 3.5 Sonnet上进行了测试，使用了1万个合成越狱提示。越狱成功率从86%降至4.4%，拒绝率仅略有上升（0.38%），额外计算成本适度增加（23.7%）。

虽然宪法分类器为AI模型提供了显著的保护，但要注意的是，它们并非万无一失。研究人员建议使用补充防御措施，并根据新出现的越狱技术不断调整“宪法”。

不过这一突破确实为未来安全部署更强大的 AI 模型带来了希望，减轻了越狱相关的风险，并确保AI系统符合安全原则。

2025年2月3日至2月10日，宪法分类器系统的实时演示将开放供红队测试。此次演示专注于与化学武器相关的查询，并邀请用户尝试越狱，以提供对系统改进的宝贵反馈。

**参考来源：**

> [https://cybersecuritynews.com/researchers-uncovers-new-methods-to-defend-ai-models/#google\_vignette﻿](https://cybersecuritynews.com/researchers-uncovers-new-methods-to-defend-ai-models/#google_vignette)

# 资讯

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

文章目录

宪法分类器的工作原理

实际测试结果

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