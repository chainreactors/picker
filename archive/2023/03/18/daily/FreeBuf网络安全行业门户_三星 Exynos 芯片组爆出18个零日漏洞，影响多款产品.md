---
title: 三星 Exynos 芯片组爆出18个零日漏洞，影响多款产品
url: https://www.freebuf.com/news/360767.html
source: FreeBuf网络安全行业门户
date: 2023-03-18
fetch_date: 2025-10-04T09:58:10.536687
---

# 三星 Exynos 芯片组爆出18个零日漏洞，影响多款产品

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

三星 Exynos 芯片组爆出18个零日漏洞，影响多款产品

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

三星 Exynos 芯片组爆出18个零日漏洞，影响多款产品

2023-03-17 13:38:25

所属地 上海

Bleeping Computer 网站披露，谷歌 Project Zero 安全团队在三星用于移动设备、可穿戴设备和汽车的Exynos 芯片组中发现了 18 个漏洞，包括 Pixel 6 系列、Pixel 7 系列、三星 Galaxy S22 系列和 Galaxy A53 等产品均受影响。![1679031561_6413fd098b66392567332.png!small](https://image.3001.net/images/20230317/1679031561_6413fd098b66392567332.png!small)

Exynos 芯片组中的安全漏洞发生在 2022 年末至 2023 年初，其中四个被评为高危漏洞，允许攻击者从互联网到基带执行远程代码。这些互联网到基带远程代码执行（RCE）漏洞（包括 CVE-2023-24033 和其它三个仍在等待 CVE-ID的漏洞）允许攻击者在没有任何用户交互的情况下，远程危害易受攻击的设备。

三星在一份描述 CVE-2023-24033 漏洞的安全咨询中表示，基带软件没有正确检查 SDP 指定接受的格式类型，可能导致三星基带调制解调器中的拒绝服务或代码执行。

Project Zero 安全团队负责人 Tim Willis 指出，潜在攻击者只要有受害者的电话号码，就可以发动袭击。更糟糕的是，只要稍微认真研究一下，经验丰富的攻击者便可以在不引起目标注意的情况下，轻而易举的利用漏洞远程攻击易受攻击的设备。

其余 14个 漏洞主要包括 CVE-2023-24072、CVE-2023-204073、CVE-202 3-24074、CVE-2022 3-24075、CVE-2020 3-24076 以及其它 9 个等待 CVE ID 的漏洞，虽然这些漏洞不会造成很严重的后果，但仍存在安全风险。

**受影响设备列表包括但不限于：**

> 三星的移动设备，包括 S22、M33、M13、M12、A71、A53、A33、A21、A13、A12 和 A04 系列。
>
> Vivo 的移动设备，包括 S16、S15、S6、X70、X60 和 X30 系列。
>
> 谷歌的 Pixel 6 和 Pixel 7 系列设备。
>
> 任何使用 Exynos W920 芯片组的可穿戴设备。
>
> 以及任何使用 Exynos Auto T5123 芯片组的车辆。

## ****受影响设备可采取的解决方法****

目前，虽然三星已经向其它厂商提供了漏洞安全更新，但这些补丁并不对所有用户公开。此外，每个制造商对其设备打补丁的时间表也有所不同，例如，谷歌已经在 2023 年 3 月的安全更新中针对受影响的 Pixel 设备解决了 CVE-2023-24033 问题。![1679031715_6413fda30d4968811fe37.png!small?1679031715412](https://image.3001.net/images/20230317/1679031715_6413fda30d4968811fe37.png!small?1679031715412)

好消息是，在安全补丁可用之前，用户可以通过禁用 Wi-Fi 呼叫和 Vo-over-LTE（VoLTE）来消除攻击媒介，从而挫败针对其设备中的三星 Exynos 芯片组的基带 RCE 利用尝试。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/google-finds-18-zero-day-vulnerabilities-in-samsung-exynos-chipsets/

# 漏洞

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

受影响设备可采取的解决方法

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