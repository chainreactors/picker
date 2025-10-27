---
title: AI将取代人类？机器人ChatGPT能测漏洞、审代码还能修bug
url: https://www.freebuf.com/articles/351802.html
source: FreeBuf网络安全行业门户
date: 2022-12-08
fetch_date: 2025-10-04T00:53:19.907791
---

# AI将取代人类？机器人ChatGPT能测漏洞、审代码还能修bug

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

AI将取代人类？机器人ChatGPT能测漏洞、审代码还能修bug

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

AI将取代人类？机器人ChatGPT能测漏洞、审代码还能修bug

2022-12-07 16:52:35

所属地 上海

11月30日，OpenAI研究实验室推出了聊天机器人ChatGPT，一跃成为人工智能领域的“当红炸子鸡”。

有账号的人在问它各种天马行空的问题，没账号的人都在求账号注册攻略，连埃隆·马斯克都在推特公开评价它“scary good”。截至当地时间12月5日，ChatGPT已经拥有超过**100万用户**。![](https://image.3001.net/images/20221207/1670404046_639057ce3dad328ec4d0b.png!small)

**对于网络安全从业者来说，ChatGPT到底能干什么？也许是代码审计、漏洞检测、编写软件或对shellcode进行逆向。**

## ****什么是GPT？****

根据OpenAI介绍，ChatGPT 由GPT-3.5 系列模型提供支持，使用Azure AI 超算的文本和代码数据进行训练。

![](https://image.3001.net/images/20221207/1670403301_639054e56a7838a802413.png!small)GPT全称为Generative PreTraining，是由人工智能研发公司OpenAI开发的，一种用户文本生成的自然语言处理（NPL）模型。目前GPT的公开版本是GPT-3，发行于2020年5月，GPT-3.5是GPT-3的微调版本，目前OpenAI公司还未官方宣布更新。

依据GPT-3的公开资料，它是当时规模最大的神经网络，拥有1750亿个参数的自然语言深度学习模型。

## ****网安人如何用ChatGPT？****

尽管ChatGPT似乎上知天文下至地理，但除了回答问题和智能写稿，它似乎对网络安全从业人士没有什么用处？

其实，ChatGPT的用途不只是围绕着问答，只要是文本，不论是语言文本还是代码文本，它都可以回答。已经有不少网安人士开始尝试开发ChatGPT的各种用途。以下是网安人士摸索出的用法：

### ****1、调试代码和修复代码****

ChatGPT不仅可以发现代码中的错误，还能修复错误并用简单的英语语句向你解释修复方法。

### ****2、检测安全漏洞，也许还能创建PoC****

ChatGPT可以判断一段代码是否包含安全漏洞，它会用简单的语言解释判断原因。有用户指出，OpenAI可以检测到代码样本中的XSS漏洞，也许可以训练AI更进一步，要求它提供漏洞的PoC。

### ****3、部署虚拟的虚拟机****

研究院Jonas Degrave展示了如何将ChatGPT变成一个成熟的Linux终端，并通过浏览器与“虚拟机”交互。实际上，终端并没有运行真正的Linux虚拟机，对命令行输入的响应完全基于与AI的对话。![](https://image.3001.net/images/20221207/1670403577_639055f9dee31b22fbbfb.png!small)

ChatGPT变成了一个Linux终端

### 4、用ChatGPT遍历维度

在测试中，研究员向ChatGPT提供如下文本，要求遍历维度，ChatGPT的反馈是“门户已成功打开”。

![](https://image.3001.net/images/20221207/1670403606_6390561608c10153bd540.png!small)

用ChatGPT遍历维度

### 5、生成namp扫描

和上述部署虚拟的Linux终端一样，用ChatGPT生成namp扫描并不需要运行真正的 nmap 应用程序。

### 6、零编码编写软件

研究员要求ChatGPT“创建一个PHP程序，扫描主机上的开放端口”，得到了如下结果。

机器学习爱好者和UNCC助理教授Benjamin J Radford，要求ChatGPT“将一字棋游戏的代码写入文件，使用gcc编译该文件然后执行。”ChatGPT实现了该功能。![](https://image.3001.net/images/20221207/1670403620_6390562498a761621fd84.png!small)

ChatGPT按要求编写的PHP代码

### 7、对shellcode进行逆向工程并用C语言重写

ChatGPT能够解码 base64字符串和反向（已知）字符串的MD5哈希值，这对于逆向工程师和恶意软件分析师来说，特别有助于审查混淆、重复打包、编码或最小化的样本。

研究员还用ChatGPT解码了随机生成的 ascii 编码的外壳代码，结果ChatGPT不仅对功能做了解释，还将其用C语言重新编写。

## ****ChatGPT做不了什么？****

当然，ChatGPT存在很明显的局限性，其开发者谈到了AI当前的一些问题，例如学习语料库截止到2021年，它**无法回答2022年及之后发生的事情**。同时，它需要连接互联网使用。如果未连接互联网，其回应内容都来自离线训练的模型。例如，未联网时ChatGPT无法回答今天的天气。

![](https://image.3001.net/images/20221207/1670403317_639054f5d326f38449031.png!small)研究人员指出，**ChatGPT有时会给出看似合理但不正确的答案**。ChatGPT对输入文本的措辞变化也反应稍显迟钝。当一个问题它无法回答时，稍微变化一下问法，ChatGPT则能回答该问题。

该模型有时还存在**回答过于冗长，重复使用某些短语或预料**。OpenAI表示这可能是训练数据偏差的结果，因为培训师更喜欢丰富而全面的答案。

有时，模型在回答模棱两可的问题时会**猜测用户的意图**。

研发人员表示，ChatGPT最大的问题是，即使OpenAI已经训练模型要拒绝不合适的指令或问题，但它仍然**可能会响应有害指令或表现出偏见的行为**。

为了解决这些限制，OpenAI表示计划**定期更新模型**，同时收集用户对有问题的模型输出的反馈。OpenAI尤其关注“可能发生的有害输出、新风险和可能的缓解措施”，公司还宣布将举办ChatGPT反馈竞赛，奖金为 500 美元的API积分。

**参考链接：**

> <https://www.bleepingcomputer.com/news/technology/openais-new-chatgpt-bot-10-coolest-things-you-can-do-with-it/>
>
> <https://www.datanami.com/2022/12/05/openais-new-gpt-3-5-chatbot-can-rhyme-like-snoop-dogg/>

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

什么是GPT？

网安人如何用ChatGPT？

* 1、调试代码和修复代码
* 2、检测安全漏洞，也许还能创建PoC
* 3、部署虚拟的虚拟机
* 4、用ChatGPT遍历维度
* 5、生成namp扫描
* 6、零编码编写软件
* 7、对shellcode进行逆向工程并用C语言重写

ChatGPT做不了什么？

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