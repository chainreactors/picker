---
title: FreeBuf早报 | H-CoT攻击揭示LRMs严重漏洞；Black Basta内部攻击技术揭秘
url: https://www.freebuf.com/news/422984.html
source: FreeBuf网络安全行业门户
date: 2025-02-27
fetch_date: 2025-10-06T20:36:02.494141
---

# FreeBuf早报 | H-CoT攻击揭示LRMs严重漏洞；Black Basta内部攻击技术揭秘

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

FreeBuf早报 | H-CoT攻击揭示LRMs严重漏洞；Black Basta内部攻击技术揭秘

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

FreeBuf早报 | H-CoT攻击揭示LRMs严重漏洞；Black Basta内部攻击技术揭秘

2025-02-26 19:01:25

所属地 上海

## 全球网安事件速递

### 1. 央视曝光电诈新招，“手机口”充当诈骗分子“隐形传话筒”

据央视新闻报道，近期流行的一种名叫\*\*“**手机口**”\*\*的电诈骗局：用两部手机，免提都打开，双方就可以直接对话，但是又能成功掩饰诈骗电话归属地。 【[阅读原文](https://www.ithome.com/0/833/853.htm)】

### 2. DISA 数据泄露影响了 330 万人

DISA 提供背景筛查、药物和酒精检测以及合规解决方案。该公司自称服务了超过 55,000 名客户，并表示每年进行数百万次药物检测和背景筛查。该公司本周向公众和当局表示，去年由于网络事件，  333 万名现任或前任雇主使用 DISA 筛查服务的个人信息被盗。【外刊-[阅读原文](https://www.securityweek.com/3-3-million-people-impacted-by-disa-data-breach/)】

### 3. GitVenom 攻击利用数百个 GitHub 存储库窃取加密货币

一个名为 GitVenom 的恶意软件活动使用数百个 GitHub 存储库诱骗用户下载信息窃取程序、远程访问木马 (RAT) 和剪贴板劫持程序，以窃取加密和凭证。 【外刊-[阅读原文](https://www.bleepingcomputer.com/news/security/gitvenom-attacks-abuse-hundreds-of-github-repos-to-steal-crypto/)】

### 4. 两个AI对话视频在网上热传，网友:毛骨悚然

近日，一段两个AI进行语音交流的视频在网络上热传，视频中对话双方在意识到彼此都是人工智能后，开始使用名为“GibberLink”的语言工具沟通。这段视频在网络上引发热议，一些网友称AI用人类无法听懂这种语言沟通的景象让人感到毛骨悚然。《福布斯》撰稿人黛安·汉密尔顿称，虽然这种加密语言更为高效，但这也会让AI更难被监管。 【[阅读原文](https://world.huanqiu.com/article/4Ldw6RZkx3L)】

### 5. LockBit威胁FBI新任局长，声称掌握能摧毁该机构的“机密信息”

勒索软件组织LockBit向新上任的FBI局长卡什·帕特尔发送了一条奇怪讯息，声称其掌握了“机密信息”，如果这些信息被公开，将可能“摧毁”FBI。 【外刊-[阅读原文](https://securityaffairs.com/174639/cyber-crime/lockbit-taunts-fbi-director-kash-patel.html)】

### 6. 间谍软件LightSpy升级：新增100+指令，跨平台控制能力大幅提升

网络安全研究人员近日发现了一款更新版本的LightSpy植入程序，其数据收集功能大幅扩展，能够从Facebook和Instagram等社交媒体平台提取信息。LightSpy是一款模块化间谍软件，能够感染Windows和苹果系统以窃取数据。它最早于2020年被记录在案，主要针对香港用户。 【外刊-[阅读原文](https://thehackernews.com/2025/02/lightspy-expands-to-100-commands.html)】

### 7. AI安全防线崩塌？H-CoT攻击揭示大型推理模型严重漏洞

随着大型推理模型（LRMs）在复杂任务中的广泛应用，其安全性和可靠性成为关键问题。OpenAI的o1/o3系列、DeepSeek-R1和谷歌的Gemini 2.0 Flash Thinking等模型通过思维链（Chain-of-Thought, CoT）推理机制进行安全决策，旨在平衡模型效用与内容无害性。然而，这种机制是否足够稳健，能否抵御复杂的攻击，仍是一个未解之谜。 【[阅读原文](https://mp.weixin.qq.com/s/jDEo-grSHZzPrrqMRfjL1w)】

### 8. 超级勒索软件内部攻击技术揭秘：Black Basta泄露数据分析

全球最活跃的勒索软件组织之一Black Basta近一年多的内部通信在网上公开，泄露了其成员的战术、商业机密和内部裂痕。据分析，这些通信记录是Black Basta成员在2023年9月至2024年9月期间，通过Matrix聊天平台相互发送的20多万条信息。【[阅读原文](https://www.secrss.com/articles/76049)】

### 9. WordPress 插件漏洞导致数百万网站遭受脚本注入攻击

Essential Addons for Elementor 插件中的一个严重安全漏洞 (CVE-2025-24752) 导致超过 200 万个 WordPress 网站面临跨站点脚本 (XSS)攻击的风险。 【外刊-[阅读原文](https://cybersecuritynews.com/wordpress-plugin-script-injection-attacks/)】

### 10. 2.84亿账户信息被窃取，网络安全警报再次拉响

Have I Been Pwned (HIBP) 已将 2.84 亿个被信息窃取恶意软件攻击的电子邮件地址纳入其违规通知服务。该数据来自被称为“ALIEN TXTBASE”的 1.5TB 窃取日志库，这是 HIBP 11 年历史上最大的恶意软件相关数据集之一。 【外刊-[阅读原文](https://cybersecuritynews.com/have-i-been-pwned-added-284-million-accounts-stolen/)】

## 优质文章推荐

### 1. 深剖 MacOS 高危TCC绕过漏洞，全面解析 AMFI

CVE-2024-54527 是一个苹果 MediaLibraryService XPC 服务的漏洞，允许应用程序绕过 TCC（透明度、同意和控制），可未经用户许可访问敏感数据。 【[阅读原文](https://www.freebuf.com/vuls/422700.html)】

### 2. 对抗沙箱的非常规手法深度解析

沙箱为快速分析通常限制资源分配，通过触发真实硬件才具备的资源响应特征进行检测。 【[阅读原文](https://www.freebuf.com/articles/web/422597.html)】

### 3.Windows图形化应急分析工具-Hawkeye

探讨在哪些情形下，个人信息处理者应主动删除用户个人信息，个人可通过行使删除权来维护自身权益。 【[阅读原文](https://www.freebuf.com/articles/system/422654.html)】

## 漏洞情报速览

### 1.脸爱云一脸通智慧平台 MoneyMng 信息泄露漏洞

<https://vip.tophant.com/detail/1894647710292774912>

### 2.29网课交单平台 默认口令漏洞

<https://vip.tophant.com/detail/1894628549122461696>

### 3.竞优商业租赁管理系统 account 信息泄露漏洞

<https://vip.tophant.com/detail/1894581418349170688>

**\*本文内容收集自全球范围内的媒体与刊物，制作者对其完整性负责，但不对其真实性和有效性负责。**

**\*标明为【外刊】的内容主要来源为英语国家的媒体与刊物，部分内容需要注册原链接平台账号后方可阅读。**

# FreeBuf早报

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

全球网安事件速递

* 1. 央视曝光电诈新招，“手机口”充当诈骗分子“隐形传话筒”
* 2. DISA 数据泄露影响了 330 万人
* 3. GitVenom 攻击利用数百个 GitHub 存储库窃取加密货币
* 4. 两个AI对话视频在网上热传，网友:毛骨悚然
* 5. LockBit威胁FBI新任局长，声称掌握能摧毁该机构的“机密信息”
* 6. 间谍软件LightSpy升级：新增100+指令，跨平台控制能力大幅提升
* 7. AI安全防线崩塌？H-CoT攻击揭示大型推理模型严重漏洞
* 8. 超级勒索软件内部攻击技术揭秘：Black Basta泄露数据分析
* 9. WordPress 插件漏洞导致数百万网站遭受脚本注入攻击
* 10. 2.84亿账户信息被窃取，网络安全警报再次拉响

优质文章推荐

* 1. 深剖 MacOS 高危TCC绕过漏洞，全面解析 AMFI
* 2. 对抗沙箱的非常规手法深度解析
* 3.Windows图形化应急分析工具-Hawkeye

漏洞情报速览

* 1.脸爱云一脸通智慧平台 MoneyMng 信息泄露漏洞
* 2.29网课交单平台 默认口令漏洞
* 3.竞优商业租赁管理系统 account 信息泄露漏洞

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