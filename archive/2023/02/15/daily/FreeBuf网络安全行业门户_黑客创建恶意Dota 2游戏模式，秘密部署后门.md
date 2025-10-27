---
title: 黑客创建恶意Dota 2游戏模式，秘密部署后门
url: https://www.freebuf.com/articles/game/357530.html
source: FreeBuf网络安全行业门户
date: 2023-02-15
fetch_date: 2025-10-04T06:37:40.275134
---

# 黑客创建恶意Dota 2游戏模式，秘密部署后门

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

黑客创建恶意Dota 2游戏模式，秘密部署后门

* ![]()
* 关注

* [其他](https://www.freebuf.com/articles/others-articles)

黑客创建恶意Dota 2游戏模式，秘密部署后门

2023-02-14 15:20:05

所属地 上海

Dota 2的玩家注意了，你使用的游戏模式很可能被黑客盯上了。

2月13日消息，未知的威胁行为者为 Dota 2 游戏创建了恶意游戏模式，这些模式可能已经被利用来建立对玩家系统的后门访问。

威胁行为者利用了V8 JavaScript 引擎中的一个高危零日漏洞CVE-2021-38003（CVSS 评分8.8），谷歌在2021年10月已修复该漏洞。

“由于V8在Dota中没有沙盒化，这个漏洞本身就可以对Dota玩家进行远程代码执行，”Avast研究员Jan Vojtěšek在上周发布的一份报告中说。

目前，游戏发行商Valve已经在202年1月12日的更新版本中修复了该漏洞。游戏模式本质上是一种自定义功能，既可以扩展现有游戏，也可以以一种偏离标准规则的方式提供全新玩法。

虽然向Steam商店发布自定义游戏模式需要经过Valve的审查，但威胁行为者还是成功地绕过了审查。

这些游戏模式已经被下架，它们是“test addon plz ignore”“Overdog no annoying heroes”“Custom Hero Brawl”以及 “Overthrow RTZ Edition X10 XP”。据称，该威胁行为者还发布了名为“Brawl in Petah Tiqwa ”的第五种游戏模式，没有包含任何恶意代码。

![](https://image.3001.net/images/20230214/1676359198_63eb361ebf1f4e611e343.png!small)“test addon plz ignore”中嵌入了一个针对V8缺陷的漏洞，该漏洞可以被用来执行自定义的shellcode。

另外三个采取了更隐蔽的方法，其恶意代码被设计成与远程服务器联系以获取JavaScript有效载荷，这也可能是对CVE-2021-38003的利用，因为该服务器已不能访问。

Avast表示，目前还不知道开发者创建这些游戏模式背后的最终目的是什么。

> 参考链接：https://thehackernews.com/2023/02/hackers-create-malicious-dota-2-game.html

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