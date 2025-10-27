---
title: WogRAT 恶意软件用记事本服务攻击 Windows 和 Linux 系统
url: https://www.freebuf.com/news/393800.html
source: FreeBuf网络安全行业门户
date: 2024-03-09
fetch_date: 2025-10-04T12:10:35.403299
---

# WogRAT 恶意软件用记事本服务攻击 Windows 和 Linux 系统

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

WogRAT 恶意软件用记事本服务攻击 Windows 和 Linux 系统

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

WogRAT 恶意软件用记事本服务攻击 Windows 和 Linux 系统

2024-03-08 12:16:52

近期，ASEC 网络安全分析师发现恶意软件 WogRAT 正在通过记事本 Notepad 服务攻击 Windows 和 Linux 系统。![1709874171_65ea9bfb72ff0ee05d8ae.png!small?1709874172501](https://image.3001.net/images/20240308/1709874171_65ea9bfb72ff0ee05d8ae.png!small?1709874172501)

安全研究人员表示，威胁攻击者通过使用 WogRAT 恶意软件，借助记事本 Notepad 工具，来利用系统资源和用户权限，从而获取未经授权的访问权限并执行恶意代码。

## ****WogRAT 恶意软件利用 Notepad 服务****

研究人员发现威胁攻击者通过 Notepad 在线记事本服务传播后门木马，因恶意软件背后的运营商使用 "WingOfGod "字符串而被业内命名为 "WogRAT"，恶意代码主要针对 Windows（PE 格式）和 Linux（ELF 格式）系统

![1709874191_65ea9c0f40d102d9e7812.png!small?1709874192302](https://image.3001.net/images/20240308/1709874191_65ea9c0f40d102d9e7812.png!small?1709874192302)

记事本平台（来源：ASEC）

WogRAT 恶意软件自 2022 年底开始出现在互联网上，攻击 Windows 时，该恶意软件会伪装成 "flashsetup\_LL3gjJ7.exe "或 "BrowserFixup.exe "等实用程序来引诱受害者。根据 VirusTotal 数据显示，香港、新加坡、中国和日本等亚洲国家和地区是 WogRAT 恶意软件的主要攻击目标。

研究人员在剖析伪装成 Adobe 工具的 Windows WogRAT 样本时，发现了一个基于 .NET 的 Chrome 实用程序伪装隐藏了一个加密下载器。

![1709874201_65ea9c1930d8613bd90c5.png!small?1709874202569](https://image.3001.net/images/20240308/1709874201_65ea9c1930d8613bd90c5.png!small?1709874202569)

加密源代码（source–ASEC）

在执行攻击行动的过程中，WogRAT 恶意软件会自动编译并加载一个 DLL，以从记事本中获取字符串并对其进行 Base64 解码，从而显示在线记事本服务上缓存的经过混淆的 .NET 二进制有效载荷。

研究人员还发现从 C&C 下载的命令包含类型、任务 ID 和相关数据等指令。例如，"upldr "任务会读取 "C:\malware.exe "并通过 FTP 上传到服务器。

值得一提的是，虽然研究人员分析样本使用的是缺乏上传功能的测试 URL，但其它 WogRAT 恶意软件变种很可能利用了这种文件的外渗功能。![](https://image.3001.net/images/20240308/1709876071_65eaa367315649718c243.jpg!small)目前，虽然 WogRAT 恶意软件的初始载体尚不明确，但研究人员观察到了一个 Linux 变种，在运行时，变种会伪装成"[kblockd]"，收集系统元数据用于外泄，其行为与 Windows 版本完全相同。

Linux  WogRAT 不会直接接收指令，而是从 C&C 获取一个反向外壳地址，然后连接接收指令，这表明威胁攻击者拥有 Tiny SHell 服务器基础架构，因为 WogRAT 采用了该开源恶意软件的例程和 C&C 机制，包括通过 HMAC SHA1 进行 AES-128 加密和未更改的 0x10 字节完整性检查。

最后，安全研究人员建议，用户应该避免使用不受信任的可执行文件，日常工作中，也要尽量从官方来源获取程序。

**参考文章：**

> https://cybersecuritynews.com/wograt-malware-exploits-notepad/

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

WogRAT 恶意软件利用 Notepad 服务

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