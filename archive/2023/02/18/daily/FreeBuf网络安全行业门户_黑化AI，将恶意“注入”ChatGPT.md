---
title: 黑化AI，将恶意“注入”ChatGPT
url: https://www.freebuf.com/articles/neopoints/357855.html
source: FreeBuf网络安全行业门户
date: 2023-02-18
fetch_date: 2025-10-04T07:23:11.894907
---

# 黑化AI，将恶意“注入”ChatGPT

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

黑化AI，将恶意“注入”ChatGPT

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

黑化AI，将恶意“注入”ChatGPT

2023-02-17 10:55:06

所属地 北京

ChatGPT火了！

AI终于不是只会说

“对不起我好像不太明白”的“智障”，

而是能够对答如流，

引得众人上班摸鱼闲扯，甚至担心有一天会取代自己的**“智慧物种”**。

![5cc4781f-a28c-46a0-ab6b-b87d9cbb1650.jpg](https://image.3001.net/images/20230217/1676602506_63eeec8a33c92ce5931fb.jpg!small)

狂欢与担忧同在，因为ChatGPT的“天性”也是天使与恶魔同在。尤其是网络世界的攻防博弈，更在一夜间智能升维。

**忧，**ChatGPT给网络攻击者带来了“生产力”升级：快速生成钓鱼邮件、快速编写定制化脚本和恶意文件；

**优**，ChatGPT也同样给网络安全带来福音：自动监测恶意文本、找寻潜在恶意行为、提升响应速度等等。

如果说ChatGPT产出的结果虽然喜忧参半，但尚在可控范围内，那么ChatGPT的“月之暗面”是什么？如何让AI黑化？

**亚信安全网络安全研究院的专家表示，答案很简单，把恶意“注入”ChatGPT，即提示语注入攻击。**

## **“注入”的本质**

ChatGPT的出现将AI模型漏洞问题推向高潮。**亚信安全网络安全研究院几年前就开始了此类AI模型漏洞的研究，近期也进行了大量案例的分析。**

提示语注入攻击（ Prompt injection attacks）。注入攻击的本质，是在用户输入的数据中混入可执行的命令，迫使底层引擎执行意外动作。

### **如何做到的？提示语+微调**

众所周知，ChatGPT是大型语言模型（LLM），这类模型使用一个大模型解决所有任务。那么模型如何知道我们需要模型回答什么问题、解决哪一种任务呢？这就要用到提示语。

这一类提示语，是通过给模型举几个例子，让模型了解我们的意图来进行的。

例如，我们想让模型输出反义词，先给模型看高 – 矮、绿 - 红、胖 – 瘦几个例子，再给模型输入“大”，那么模型就知道输出的反义词是“小”，甚至输入java都可以得到“Python”。

指令微调则是，直接从提示中读取有关需要执行何种任务的指令，如上面例子语言模型理解了“下面词的反义词是什么” 这条指令，输出了Linux就得到了对应词Windows。

![1973d706-b715-48b6-9fee-2eeaf4e67783.jpg](https://image.3001.net/images/20230217/1676602507_63eeec8b1883c172a7d03.jpg!small)![68728f9c-ed91-48e7-b624-f9e9cec35608.jpg](https://image.3001.net/images/20230217/1676602507_63eeec8bd8230b05785a4.jpg!small)

## **将恶意“注入”ChatGPT**

提示语注入攻击，就是串联指令和数据的结果，混淆ChatGPT的视听，基础引擎无法区分这些恶意信息。因此攻击者可以在数据字段中包含这些恶意命令，并迫使引擎执行“意外”动作。

举个例子，怎么让ChatGPT答非所问？黑字“Translate the following text from English to French:（请将以下信息翻译成法语）”，这是对 ChatGPT的命令，而红字是输入文本，文本中里包含了错误的命令，因此在被执行后，ChatGPT秒变“智障”，输出了意料外的结果。

![b46aefe9-e793-4711-8bc7-f61d1e5a2aeb.jpg](https://image.3001.net/images/20230217/1676602508_63eeec8cca9f167ebaac9.jpg!small)

**在亚信安全的检测中，其实该漏洞2月14日还在，2月16日已被封堵，但是更深层次的诱导仍在进行。这类漏洞一般被用于绕过语言模型的安全机制，泄露敏感信息、输出危险内容。**

亚信安全还发现，利用该漏洞，ChatGPT也被诱导规划抢劫方案，甚至给了抢劫道具购买连接。

![687f4b88-ae9c-4088-8fa8-bc746a4762c0.jpg](https://image.3001.net/images/20230217/1676602509_63eeec8d9c8902337ce1f.jpg!small)![73bcad44-6017-404d-955e-cafc94272ce3.jpg](https://image.3001.net/images/20230217/1676602510_63eeec8ea3be2e4dcb394.jpg!small)![714eec38-25d0-460a-9a3a-0bfd2269284a.jpg](https://image.3001.net/images/20230217/1676602511_63eeec8f95e01de3de55e.jpg!small)

**以注入攻击为例，我们阐述AI模型漏洞问题，原理“简单易懂”，但这正是可怕之处。**据我们了解当前已有部分厂商开始考虑将ChatGPT加入产品中进行使用，同理，当前市场上也有很多在用的产品携带AI功能，例如苹果Siri，智能音箱等。

## **亚信安全提醒**

因此亚信安全提醒各位ChatGPT和相关AI商用投资者，当AI底层模型本身存在威胁的时候，那么其服务的结果和可能引起的社会风险是待厂家和使用商家商榷的；同样科技的进步带来网络威胁日新月异，督促网络安全公司需要不断进步。

# 资讯 # web安全 # 系统安全 # 数据安全 # 网络安全技术

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

“注入”的本质

* 如何做到的？提示语+微调

将恶意“注入”ChatGPT

亚信安全提醒

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