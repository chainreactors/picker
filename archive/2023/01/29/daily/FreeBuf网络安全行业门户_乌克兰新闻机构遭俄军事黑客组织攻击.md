---
title: 乌克兰新闻机构遭俄军事黑客组织攻击
url: https://www.freebuf.com/news/355841.html
source: FreeBuf网络安全行业门户
date: 2023-01-29
fetch_date: 2025-10-04T05:07:55.068636
---

# 乌克兰新闻机构遭俄军事黑客组织攻击

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

乌克兰新闻机构遭俄军事黑客组织攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

乌克兰新闻机构遭俄军事黑客组织攻击

2023-01-28 15:22:49

所属地 上海

![](https://image.3001.net/images/20230128/1674888708_63d4c604b869c2c4a4bb6.png!small)

截至 2023 年 1 月 27 日，乌克兰计算机应急响应小组 (CERT-UA) 在该国国家新闻机构 (Ukrinform) 的网络上发现了五种不同的数据擦除恶意软件组合，其功能旨在破坏信息的完整性和可用性（写入零字节/任意数据的文件/磁盘及其随后的删除）。

在针对 Ukrinform 的攻击中部署的破坏性恶意软件列表包括 CaddyWiper (Windows)、ZeroWipe (Windows)、SDelete (Windows)、AwfulShred (Linux) 和 BidSwipe (FreeBSD)。

攻击者使用 Windows 组策略 (GPO) 启动了 CaddyWiper 恶意软件，由此可表明他们事先已经破坏了目标的网络。

正如 CERT-UA 在调查期间发现的那样，攻击者在 12 月 7 日左右获得了对 Ukrinform 网络的远程访问权限，并等待了一个多月才释放恶意软件。

然而，他们试图清除新闻机构系统中所有数据的尝试失败了。擦除器仅成功销毁了“几个数据存储系统”上的文件，这并未影响 Ukrinform 的运营。

CERT-UA 强调网络攻击只是部分成功，特别是在有限数量的数据存储系统方面。

## 与俄罗斯沙虫军事黑客有关的网络攻击

CERT-UA 上周将此次攻击与 Sandworm 威胁组织联系起来，该组织是俄罗斯主要情报局 (GRU) 74455 军事部队的黑客组织，Sandworm 曾在4 月份针对一家大型乌克兰能源供应商的另一次失败攻击中使用了 CaddyWiper 数据擦除器。

在那次攻击中，俄罗斯黑客使用了类似的策略，部署 CaddyWiper 来清除 Industroyer ICS 恶意软件留下的痕迹，以及其他三个为 Linux 和 Solaris 系统设计的擦除器，并被跟踪为 Orcshred、Soloshred 和 Awfulshred。

自 2022 年 2 月俄乌战争以来，除了 CaddyWiper 之外，乌克兰目标网络上还部署了多种数据擦除恶意软件，包括DoubleZero、HermeticWiper、IsaacWiper、WhisperKill、WhisperGate和AcidRain 等。

此外，微软和斯洛伐克软件公司 ESET 也表示最近针对乌克兰的勒索软件攻击与 Sandworm 黑客组织有关。

> 参考链接：https://www.bleepingcomputer.com/news/security/ukraine-sandworm-hackers-hit-news-agency-with-5-data-wipers/

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

与俄罗斯沙虫军事黑客有关的网络攻击

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