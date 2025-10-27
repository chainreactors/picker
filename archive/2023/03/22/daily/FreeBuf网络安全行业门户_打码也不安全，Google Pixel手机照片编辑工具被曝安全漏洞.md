---
title: 打码也不安全，Google Pixel手机照片编辑工具被曝安全漏洞
url: https://www.freebuf.com/news/361126.html
source: FreeBuf网络安全行业门户
date: 2023-03-22
fetch_date: 2025-10-04T10:15:42.810102
---

# 打码也不安全，Google Pixel手机照片编辑工具被曝安全漏洞

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

打码也不安全，Google Pixel手机照片编辑工具被曝安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

打码也不安全，Google Pixel手机照片编辑工具被曝安全漏洞

2023-03-21 11:40:00

所属地 上海

最近使用Google Pixel 手机的用户需要注意，你打过码的照片未必安全！

安全研究人员 Simon Aarons 和 David Buchanan 最近在推特披露称，Google Pixel 自带的照片编辑工具Markup存在一个名为“Acropalypse的安全漏洞，能够还原用户照片中已经打码或裁剪掉的内容。

![](https://image.3001.net/images/20230321/1679370257_64192811ca0ef4f0600a7.png!small)

Aarons 分享了一个示例，演示他们如何使用 Acropalypse 漏洞恢复上传到 Discord 的信用卡照片。最开始，该信用卡卡号码已使用Markup工具进行了打码处理。但当他们的利用Acropalypse exploit 运行照片后，已经被打码的卡号信息得到了还原。

![](https://image.3001.net/images/20230321/1679370223_641927efaf5bb089f5d9b.png!small)

Acropalypse 示例

据悉，这两名研究人员于今年1月向谷歌报告了该漏洞，谷歌也与3月13日发布的更新中对其进行了修复。分析指出，经过Markup编辑处理的照片有大约80%能够被恢复，如果用户将未压缩的图片发布至互联网或社交平台，就可能导致敏感信息泄露。当然，一些平台会自动压缩、重新编码上传的照片，从而在一定程度上减少了信息泄露的范围。

虽然Acropalypse漏洞已经得到修复，但仍需值得注意的是，漏洞存在的时间长达5年之久，这期间已经共享出去的照片难以计数，且没有任何补救措施。此外，该漏洞广泛存在于所有运行 Android 9 Pie 及更高版本的 Pixel 型号手机中，一些较老型号的手机并不会在第一时间得到安全更新，安全风险依然存在。

最后，Acropalypse漏洞还会影响其他品牌的定制化Android手机，可能完全沿用原生的Markup对照片进行编辑。

> 参考来源：[Google Pixel flaw allowed recovery of redacted, cropped images](https://www.bleepingcomputer.com/news/security/google-pixel-flaw-allowed-recovery-of-redacted-cropped-images/)

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