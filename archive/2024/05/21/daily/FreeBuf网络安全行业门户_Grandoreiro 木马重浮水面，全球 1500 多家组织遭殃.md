---
title: Grandoreiro 木马重浮水面，全球 1500 多家组织遭殃
url: https://www.freebuf.com/news/401362.html
source: FreeBuf网络安全行业门户
date: 2024-05-21
fetch_date: 2025-10-06T16:51:01.748829
---

# Grandoreiro 木马重浮水面，全球 1500 多家组织遭殃

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

Grandoreiro 木马重浮水面，全球 1500 多家组织遭殃

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Grandoreiro 木马重浮水面，全球 1500 多家组织遭殃

2024-05-20 13:48:06

所属地 上海

近日，研究人员发现基于 Windows 的 Grandoreiro 特洛伊银行木马再次重新浮出水面。据悉，这是该木马在 2024 年 3 月份之后，又一次在全球范围内发动攻击。![](https://image.3001.net/images/20240520/1716185587_664ae9f3a8be2653a5a94.jpg!small)

> IBM X-Force 表示，大规模网络钓鱼攻击活动可能由其他网络犯罪分子通过“推行”恶意软件即服务（MaaS）模式，针对遍布中美洲和南美洲，非洲，欧洲和印太地区的 60 多个国家 1500 多家银行，发动网络攻击行动。

值得一提的是，自出道以来，Grandoreiro 背后的运营商一直将“目光”锁定在了拉丁美洲、西班牙和葡萄牙等地区，也曾在这些地区发动了多次网络攻击活动，获得很多坏“名声”，但自从巴西当局试图关闭其基础设施后，该组织便开始了战略转变，谋求大规模自主扩张。

**同时，Grandoreiro  恶意软件自身也进行了重大改进。**

安全研究人员 Golo Mühr 和 Melissa Frydrych 指出， 在对 Grandoreiro  恶意软件进行详细分析后，发现其对字符串解密和域生成算法（DGA）进行了重大更新，并能在受感染主机上使用微软 Outlook 客户端进一步传播钓鱼电子邮件。

在进行网络攻击时，钓鱼邮件会指示收件人点击链接查看发票或付款（具体取决于诱惑的性质和邮件中假冒的政府实体），一旦点击了链接，用户会被重定向到一个 PDF 图标图像，最终被引导着下载一个包含 Grandoreiro 载入器可执行文件的 ZIP 压缩包。

自定义加载程序被人为地膨胀到 100 MB 以上，以绕过反恶意软件扫描软件。此外，它还负责确保受感染的主机不在沙盒环境中，将基本受害者数据收集到命令和控制 （C2） 服务器，以及下载和执行主要银行木马。

> 值得注意的是，该验证步骤还跳过了位于俄罗斯、捷克、波兰和荷兰的系统，以及位于美国且未安装杀毒软件的 Windows 7 机器。

特洛伊木马组件通过 Windows 注册表建立持久性开始执行，然后使用重新设计的 DGA 与 C2 服务器建立连接以接收进一步的指令，Grandoreiro 支持各种命令，允许威胁攻击者远程征用系统，执行文件操作并启用特殊模式，包括收集Microsoft Outlook数据并滥用受害者的电子邮件帐户以向其他目标发送垃圾邮件的新模块。

研究人员强调，为了与本地 Outlook 客户端进行交互，Grandoreiro 使用 Outlook 安全管理器工具，通过使用本地 Outlook 客户端发送垃圾邮件，Grandoreiro 可以利用电子邮件在受感染的受害者收件箱中传播，这很可能是导致从 Grandoreiro 中观察到大量垃圾邮件的原因。

**参考文章：**

> https://thehackernews.com/2024/05/grandoreiro-banking-trojan-resurfaces.html

# 恶意软件

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