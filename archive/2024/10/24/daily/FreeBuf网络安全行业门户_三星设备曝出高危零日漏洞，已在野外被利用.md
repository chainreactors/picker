---
title: 三星设备曝出高危零日漏洞，已在野外被利用
url: https://www.freebuf.com/news/413479.html
source: FreeBuf网络安全行业门户
date: 2024-10-24
fetch_date: 2025-10-06T18:51:49.168050
---

# 三星设备曝出高危零日漏洞，已在野外被利用

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

三星设备曝出高危零日漏洞，已在野外被利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

三星设备曝出高危零日漏洞，已在野外被利用

2024-10-23 09:56:15

所属地 上海

![1729649259_67185a6b6a92b2d2f058f.png!small](https://image.3001.net/images/20241023/1729649259_67185a6b6a92b2d2f058f.png!small)

谷歌威胁分析小组（TAG）警告称，三星存在一个零日漏洞，被追踪为 CVE-2024-44068（CVSS 得分为 8.1），且该漏洞已被发现存在被利用的情况。

攻击者可利用该漏洞在安卓设备上提升权限。专家称该漏洞存在于三星移动处理器中，且已与其他漏洞连锁，可在易受攻击的设备上实现任意代码执行。

今年 10 月，三星已正式发布安全更新，解决了这一漏洞。其集团发布的公告中写道：移动处理器中的‘自由使用’（Use-After-Free）会导致权限升级。公司并未证实该漏洞在野外被积极利用。

受到该漏洞影响的版本包括： Exynos 9820、9825、980、990、850 和 W920。

该漏洞最早是由谷歌设备与服务安全研究部门的研究人员金星宇（Xingyu Jin）和谷歌威胁分析小组的克莱门特-莱西金（Clement Lecigene）发现的。

谷歌 TAG 发现该漏洞的事实表明，商业间谍软件供应商可能已经利用该漏洞瞄准了三星设备。谷歌零项目发布的公告警告说，零日漏洞是权限提升链的一部分。行为者能够在有权限的进程中执行任意代码。该漏洞还将进程名称重命名为 “vendor.samsung.hardware.camera.provider@3.0-service”，可能是出于反取证目的。

谷歌研究人员在报告中解释说，该漏洞存在于一个为 JPEG 解码和图像缩放等媒体功能提供硬件加速的驱动程序中。

通过与 IOCTL M2M1SHOT\_IOC\_PROCESS 交互，为 JPEG 解码和图像缩放等媒体功能提供硬件加速的驱动程序可能会将用户空间页面映射到 I/O 页面，执行固件命令并删除映射的 I/O 页面。

该漏洞通过取消映射 PFNMAP 页来工作，从而导致‘释放后使用’漏洞，即 I/O 虚拟页可能映射到已释放的物理内存。然后，漏洞利用代码使用特定的固件命令复制数据，可能会覆盖页表中的页中间目录（PMD）条目。这可以通过向页表发送垃圾邮件、操纵内核内存和利用释放的页面来导致内核空间镜像攻击 （KSMA）。

> 参考来源：<https://securityaffairs.com/170119/security/samsung-zero-day-activey-exploited.html>

# 三星漏洞

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