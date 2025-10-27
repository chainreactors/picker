---
title: 黑客利用YouTube 平台传播复杂的恶意软件
url: https://www.freebuf.com/news/412529.html
source: FreeBuf网络安全行业门户
date: 2024-10-12
fetch_date: 2025-10-06T18:52:27.563946
---

# 黑客利用YouTube 平台传播复杂的恶意软件

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

黑客利用YouTube 平台传播复杂的恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客利用YouTube 平台传播复杂的恶意软件

2024-10-11 10:50:42

所属地 上海

最近，卡巴斯基实验室的网络安全分析师发现，黑客一直在频繁利用 YouTube平台来传播复杂的恶意软件。通过劫持热门频道，黑客伪装成原始创作者发布恶意链接、对用户实施诈骗。

![](https://image.3001.net/images/20241011/1728615177_67089309cfbc3d61eb91b.png!small)

研究发现，攻击者曾在 2022 年实施了一项复杂的加密货币挖掘活动，目标主要针对俄罗斯用户。攻击者使用多种攻击媒介（包括被劫持的 YouTube 账户 ）来分发伪装成如uTorrent、Microsoft Office和Minecraft等流行应用的恶意文件。

感染链始于 "受密码保护的 MSI 文件"，其中包含触发 多阶段攻击序列的 VBScript，包括利用隐藏在合法数字签名 DLL 中的 AutoIt 脚本，将权限升级到 SYSTEM 级。 这是一种在隐藏 "恶意代码 "的同时保持签名有效性的技术。

该恶意软件通过 WMI 事件过滤器、注册表修改（特别针对 图像文件执行选项、调试器和MonitorProcess 键）以及滥用开源Wazuh SIEM 代理进行远程访问等多种机制建立了持久性。

此外，攻击者采用了复杂的防御规避技术（通 explorer.exe进程镂空、反调试检查和使用基于特殊 GUID 的目录名操纵文件系统）来隐藏恶意组件。

卡巴斯基表示，最终有效载荷部署为SilentCryptoMiner，用于挖掘Monero和Zephyr等注重隐私的加密货币，同时实施基于进程的隐身机制以逃避检测。

该恶意软件还收集系统遥测数据（包括CPU 规格、GPU 详细信息、操作系统版本和防病毒信息）并通过 Telegram 机器人 API 进行传输，其中一些变体包括剪贴板劫持功能，特别针对加密货币钱包地址。

除了针对俄罗斯用户，这一恶意活动还针对来自白俄罗斯、印度、乌兹别克斯坦、哈萨克斯坦、德国、阿尔及利亚、捷克、莫桑比克和土耳其的用户。由于这些用户经常自愿禁用 AV 工具的保护和安全措施来安装非官方软件，因此特别容易受到攻击。

这种攻击的复杂性体现在其模块化结构上，即可以根攻击者的目标动态加载不同的有效载荷组件，表明大规模活动可通过先进的混淆方法和反分析功能，在保持隐蔽性的同时融入复杂的企业级攻击技术。

**参考来源：**

> [Hackers Using YouTube Videos To Deliver Sophisticated Malware](https://cybersecuritynews.com/hackers-using-youtube-videos-to-deliver-sophisticated-malware/)

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