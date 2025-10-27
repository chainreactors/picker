---
title: 谷歌发现用于部署间谍软件的 Windows 漏洞利用框架
url: https://www.freebuf.com/news/351256.html
source: FreeBuf网络安全行业门户
date: 2022-12-02
fetch_date: 2025-10-04T00:17:55.218867
---

# 谷歌发现用于部署间谍软件的 Windows 漏洞利用框架

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

谷歌发现用于部署间谍软件的 Windows 漏洞利用框架

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌发现用于部署间谍软件的 Windows 漏洞利用框架

2022-12-01 11:56:26

所属地 上海

据BleepingComputer 11月30日消息，谷歌的威胁分析小组 (TAG) 发现一家西班牙软件公司试图利用 Chrome 、 Firefox 浏览器以及 Microsoft Defender 安全应用程序中的漏洞从事间谍活动，目前漏洞已经得到修复。

![](https://image.3001.net/images/20221201/1669872272_63883a908e4c65d4bbf26.png!small)

谷歌TAG表示，这家总部位于巴塞罗那的软件公司虽然官方宣称是一家安全解决方案提供商，但其实也从事商业监控活动。

该公司使用Heliconia 框架，利用了 Chrome、Firefox 和 Microsoft Defender 中的 N-day 漏洞，提供了将有效载荷部署到目标设备所需的所有工具。该利用框架由多个组件组成，每个组件都针对目标设备软件中的特定安全漏洞：

* **Heliconia Noise：**一个 Web 框架，用于部署 Chrome 渲染器错误利用，以及 Chrome 沙箱逃逸以在目标设备上安装代理
* **Heliconia Soft：**一个部署包含 Windows Defender 漏洞的 PDF  Web 框架，被跟踪为 CVE-2021-42298
* **Heliconia 文件****：**一组针对 Linux 和 Windows 的 Firefox 漏洞利用，其中一个被跟踪为 CVE-2022-26485

对于 Heliconia Noise 和 Heliconia Soft，这些漏洞最终会在受感染的设备上部署名为“agent\_simple”的代理。

TAG分析了一个包含虚拟代理的框架样本，得到的结果是在运行和退出的情况下未执行任何恶意代码，认为该框架的客户提供了他们自己的代理，或者是谷歌没有权限访问整个框架。

尽管没有证据表明目标安全漏洞被积极利用，并且谷歌、Mozilla 和微软在 2021 年和 2022 年初修补了这些漏洞，但TAG 表示这些漏洞很可能在野外被用作零日漏洞。

## 对间谍软件供应商的跟踪

TAG 属于谷歌旗下的安全专家团队，专注于保护谷歌用户免受国家支持的网络攻击，但团队也跟踪了数十家从事间谍或监视服务的公司。

2022年6 月，TAG 注意到意大利间谍软件供应商 RCS Labs在一些互联网服务提供商 (ISP) 的帮助下，在意大利和哈萨克斯坦的 Android 和 iOS 用户的设备上部署了商业监控工具。期间，目标用户被提示安装伪装成合法移动运营商应用的监控软件。

最近，TAG 揭露了另一场监视活动，受国家支持的攻击者利用五个零日漏洞，在目标设备上安装商业间谍软件开发商 Cytrox 开发的 Predator 间谍软件。

TAG表示，间谍软件行业的发展使用户处于危险之中，并降低了互联网的安全性，虽然根据国家或国际法律，监控技术可能是合法的，但它们经常以有害的方式被用来对一系列群体进行数字间谍活动。

> 参考来源：<https://www.bleepingcomputer.com/news/security/google-discovers-windows-exploit-framework-used-to-deploy-spyware/>

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

对间谍软件供应商的跟踪

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