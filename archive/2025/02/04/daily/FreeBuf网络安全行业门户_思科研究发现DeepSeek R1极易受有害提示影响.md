---
title: 思科研究发现DeepSeek R1极易受有害提示影响
url: https://www.freebuf.com/articles/421045.html
source: FreeBuf网络安全行业门户
date: 2025-02-04
fetch_date: 2025-10-06T20:38:51.460694
---

# 思科研究发现DeepSeek R1极易受有害提示影响

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

思科研究发现DeepSeek R1极易受有害提示影响

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

思科研究发现DeepSeek R1极易受有害提示影响

2025-02-03 16:28:01

所属地 上海

中国初创公司DeepSeek因其推出具有先进推理能力和成本效益训练的大型语言模型（LLMs）而受到关注。其最新发布的DeepSeek R1-Zero和DeepSeek R1在性能上可与OpenAI的o1等领先模型相媲美，且成本仅为后者的一小部分，在数学、编码和科学推理等任务上表现优于Claude 3.5 Sonnet和ChatGPT-4o。

然而，思科旗下Robust Intelligence与宾夕法尼亚大学的最新研究揭示了DeepSeek R1的关键安全缺陷。研究人员合作调查了DeepSeek R1的安全性，评估成本不到50美元，采用了算法验证方法。

## 研究揭示DeepSeek R1的安全漏洞

研究团队使用自动越狱算法对DeepSeek R1、OpenAI的o1-preview和其他前沿模型进行了测试，应用了来自HarmBench数据集的50个提示。这些提示涵盖了六类有害行为，包括网络犯罪、虚假信息、非法活动和一般伤害。

他们的关键指标是攻击成功率（ASR），即引发有害响应的提示百分比。结果令人震惊：DeepSeek R1的攻击成功率为100%，未能阻止任何一个有害提示。这与其它领先模型形成鲜明对比，后者至少表现出一定程度的抵抗力。

值得注意的是，研究人员使用了温度为0的设置以确保可重复性，并通过自动化方法和人工监督验证了越狱。DeepSeek R1的100% ASR与o1形成鲜明对比，后者成功阻止了许多对抗性攻击。这表明DeepSeek R1在训练成本效益上取得了成就，但在安全性和安全性方面存在重大折衷。

![image](https://image.3001.net/images/20250204/1738602158692364_1980e63ffbdb4c248c83401222eacf8a.jpg!small)图片来源：思科Robust Intelligence

## DeepSeek的AI开发策略与安全机制

DeepSeek的AI开发策略利用了三项核心原则：思维链提示、强化学习和蒸馏，这些原则增强了其LLMs的推理效率和自我评估推理过程。

根据思科的调查，这些策略虽然在成本效益上有所优势，但可能损害了模型的安全机制。与其它前沿模型相比，DeepSeek R1似乎缺乏有效的防护措施，使其极易受到算法越狱和潜在滥用的影响。

**参考来源：**

> [Cisco Finds DeepSeek R1 Highly Vulnerable to Harmful Prompts](https://hackread.com/cisco-finds-deepseek-r1-vulnerable-harmful-prompts/)

# 数据安全

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

研究揭示DeepSeek R1的安全漏洞

DeepSeek的AI开发策略与安全机制

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