---
title: 重大突破，谷歌AI大模型首次找到0Day漏洞
url: https://www.freebuf.com/news/414494.html
source: FreeBuf网络安全行业门户
date: 2024-11-06
fetch_date: 2025-10-06T19:18:22.412463
---

# 重大突破，谷歌AI大模型首次找到0Day漏洞

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

重大突破，谷歌AI大模型首次找到0Day漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

重大突破，谷歌AI大模型首次找到0Day漏洞

2024-11-05 16:05:24

所属地 上海

谷歌公司日前表示，旗下一款名为“ Big Sleep**”**（前称 Project Naptime）的大语言模型（LLM）辅助框架在 SQLite 开源数据库引擎中发现了一个零日漏洞，并称这是该类型AI工具首次在实际广泛使用的软件中发现零日漏洞。

![](https://image.3001.net/images/20241105/1730794417_6729d3b1d30d9a9185b1d.png!small)

SQLite 是一种在开发人员中流行的开源数据库引擎，所发现的漏洞指向其中的堆栈缓冲区下溢，当软件在内存缓冲区开始之前引用内存位置时，就会出现该漏洞，从而导致系统崩溃或任意代码执行。

谷歌研究人员在 10 月初向 SQLite 开发人员报告了该漏洞，对方在同一天修复了漏洞。由于漏洞是在正式版本出现之前被发现，因此不会影响正在使用SQLite的用户。

发现该漏洞的“ Big Sleep**”**AI模型属Google Project Zero 和 Google DeepMind 之间的合作项目，旨在大型语言模型的辅助下进行漏洞研究。 谷歌指出，在 8 月 DEFCON 安全会议上，负责创建 AI 辅助漏洞研究工具的网络安全研究人员表示在 SQLite 中发现了另一个问题，从而激发团队研究是否可以从中找到更严重的漏洞。

通常，许多公司使用一种称为“模糊测试”的过程，通过向软件提供随机或无效数据来测试软件，这些数据旨在识别漏洞、触发错误或使程序崩溃。但谷歌认为，模糊测试在帮助防御者找到难以（或不可能）发现的漏洞方面做得还不够，希望利用人工智能可以缩小这一差距。

而长期存在的漏洞变体问题也是“ Big Sleep**”**项目的主要动机之一， 谷歌在 2022 年发布的报告就曾指出，40% 以上的零日漏洞是已报告漏洞的变种，另有超过 20% 的漏洞也是以前的野外零日漏洞的变种。随着这种趋势的持续，模糊测试已无法成功捕获此类变体，而对于攻击者来说，手动变体分析成为一种经济高效的方法。

在“ Big Sleep**”**中，研究人员利用 LLM 的代码理解和推理能力，在识别和演示安全漏洞时利用 AI 代理来模拟人类行为，其中需要使用一套专用工具来允许代理浏览目标代码库，并在沙盒环境中运行 Python 脚本以生成用于模糊测试的输入、调试程序并观察结果。

“我们认为这项工作具有巨大的防御潜力。在软件发布之前就发现软件中的漏洞，意味着攻击者没有竞争的余地：漏洞甚至在攻击者有机会使用它们之前就被修复了，“谷歌表示。

但谷歌也强调，这些仍然是实验结果，“ Big Sleep”研究团队的立场是，在发现漏洞方面，目前特定于目标的模糊测试程序可能至少同样有效。希望在未来，这项工作将为防御者带来显著的优势——不仅可以找到崩溃的测试用例，还可以提供高质量的根本原因分析，分类和修复漏洞在未来也可能会更便宜、更有效。

**参考来源：**

> [Google's AI Tool Big Sleep Finds Zero-Day Vulnerability in SQLite Database Engine](https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html)
>
> [Google uses large language model to discover real-world vulnerability](https://therecord.media/google-llm-sqlite-vulnerability-artificial-intelligence)

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