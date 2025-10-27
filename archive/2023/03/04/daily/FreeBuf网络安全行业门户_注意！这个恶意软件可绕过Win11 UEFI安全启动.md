---
title: 注意！这个恶意软件可绕过Win11 UEFI安全启动
url: https://www.freebuf.com/news/359289.html
source: FreeBuf网络安全行业门户
date: 2023-03-04
fetch_date: 2025-10-04T08:38:11.061348
---

# 注意！这个恶意软件可绕过Win11 UEFI安全启动

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

注意！这个恶意软件可绕过Win11 UEFI安全启动

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

注意！这个恶意软件可绕过Win11 UEFI安全启动

2023-03-03 16:12:39

所属地 上海

![](https://image.3001.net/images/20230303/1677830837_6401aab572a323f92dece.png!small)

来自 ESET 的安全研究人员近日发现了一种劫持 UEFI 的恶意软件，并将其命名为 BlackLotus。**该恶意软件被认为是首个可以在 Win11 系统上绕过 Secure Boot 的 UEFI bootkit 恶意软件。**

![ffbf-dafca0bce11553dd7ec0b22a2b15c57d.jpg](https://image.3001.net/images/20230303/1677831162_6401abfa297b9a00f07d3.jpg!small)

设备一旦感染该恶意软件，就会在 Win11 系统中禁用 Defender、Bitlocker 和 HVCI 等防病毒软件。该恶意软件最早可以追溯到 2022 年 10 月，在黑客论坛上以 5000 美元的价格出售。

![](https://image.3001.net/images/20230303/1677830896_6401aaf0f189b157f29ed.png!small)

BlackLotus 利用存在一年多的安全漏洞（CVE-2022-21894）绕过 UEFI 安全启动并将自身永久嵌入计算机中。

ESET说，BlackLotus安装程序可以是在线或离线的，它们之间的区别是，离线变体携带有漏洞的Windows二进制文件；在线版本的安装程序 直接从微软商店 下载Windows二进制文件。

研究人员看到以下三个文件被bootkit所滥用。

https://msdl.microsoft.com/download/symbols/bootmgfw.efi/7144BCD31C0000/bootmgfw.efi
https://msdl.microsoft.com/download/symbols/bootmgr.efi/98B063A61BC000/bootmgr.efi
https://msdl.microsoft.com/download/symbols/hvloader.efi/559F396411D000/hvloader.Efi

Smolár解释说，利用CVE-2022-21894，允许绕过安全启动并安装引导工具包。然后可以在早期启动阶段执行任意代码，此时UEFI启动服务功能仍然可用。这允许攻击者在没有物理访问的情况下，在启用了UEFI安全启动的机器上做许多他们不应该做的事情，比如修改只有Boot-services的NVRAM变量。而这正是攻击者在下一步为bootkit设置持久性的优势所在。

通过向MokList、Boot-services-only NVRAM变量写入它自己的MOK来设置持久性。通过这样做，它可以使用合法的微软签名的垫片来加载其自签名（由属于写入MokList的密钥的私钥签名）的UEFI启动包，而不是在每次启动时利用漏洞。

要注意的是，CVE-2022-21894的概念验证（PoC）利用代码自2022年8月以来已经公开提供了半年多的时间。虽然微软已经在 2022 年 1 月发布更新修复了该漏洞，但由于受影响的、有效签名的安装文件仍未添加到 UEFI 锁定列表中，因此攻击者依然可以利用该漏洞。

> 参考链接：https://www.bleepingcomputer.com/news/security/blacklotus-bootkit-bypasses-uefi-secure-boot-on-patched-windows-11/

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