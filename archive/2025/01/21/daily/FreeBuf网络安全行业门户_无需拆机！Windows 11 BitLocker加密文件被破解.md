---
title: 无需拆机！Windows 11 BitLocker加密文件被破解
url: https://www.freebuf.com/news/420297.html
source: FreeBuf网络安全行业门户
date: 2025-01-21
fetch_date: 2025-10-06T20:10:15.718086
---

# 无需拆机！Windows 11 BitLocker加密文件被破解

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

无需拆机！Windows 11 BitLocker加密文件被破解

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

无需拆机！Windows 11 BitLocker加密文件被破解

2025-01-20 14:10:38

所属地 上海

![](https://image.3001.net/images/20250120/1737355717_678df1c5a8f6825c9315b.jpg!small)

混沌通信大会 (38C3)上，安全研究员Thomas Lambertz展示了一个名为“bitpixie”(CVE-2023-21563)的漏洞。

“bitpixie”漏洞通过利用Windows启动管理器的降级攻击，使攻击者可以在不物理篡改设备的情况下绕过安全启动，只需要能够插入网线和键盘即可解密磁盘。这一漏洞凸显了Windows 11上BitLocker默认配置中的一个严重缺陷，对依赖它进行数据保护的用户敲响了警钟。

BitLocker是微软的全盘加密技术，旨在通过加密整个驱动器来保护敏感数据。它依赖安全启动和可信平台模块（TPM）来确保加密密钥仅在启动期间释放给受信任的组件。然而，bitpixie漏洞利用了这一过程中的设计缺陷。

## 该漏洞如何发挥作用？

该漏洞的根源在于Windows启动管理器在特定恢复流程中，未能从内存中清除加密密钥。攻击者可以通过将启动加载程序降级到较旧的、易受攻击的版本来利用这一点。

**具体过程如下：**

* 启动器降级：通过网络启动（PXE启动），攻击者加载一个过时的Windows启动管理器，该版本仍存在漏洞。
* 触发恢复模式：降级后的启动器会触发恢复序列，导致BitLocker保护数据所需的卷主密钥（VMK）留在系统内存中。
* 内存转储：攻击者随后启动到Linux环境中，并使用取证工具从内存中提取VMK。
* 解密数据：一旦获得VMK，攻击者即可完全访问加密的硬盘。

这种攻击无需打开笔记本电脑或访问内部组件，对于被盗设备来说尤其令人担忧。

![](https://image.3001.net/images/20250120/1737355741_678df1dd3e457f6c66994.png!small)Windows漏洞问题

BitLocker依赖安全启动和TPM进行无人值守解密，虽然这些机制可以通过在启动时自动解锁硬盘来简化用户体验，但它们在被利用时也会产生漏洞，bitpixie就暴露了这一重大弱点。

**主要问题包括：**

* 广泛的适用性：该漏洞影响所有使用BitLocker默认“设备加密”模式的设备，而许多Windows 11系统默认启用此模式。
* 易于执行：该攻击仅需对设备进行物理接触，并使用键盘和网络连接等基本工具。
* 持续风险：尽管微软在2022年底发布了补丁，但由于安全启动证书撤销的限制，攻击者仍可通过启动器降级绕过保护。

## 缓解策略

微软承认完全解决这一漏洞存在挑战。尽虽然较新的启动加载程序已修复该问题，但由于安全启动无法普遍强制执行严格的降级保护，旧版本仍然可利用。为降低风险，建议用户采取以下**额外安全措施：**

* **启用预启动身份验证：**配置BitLocker使用预启动PIN，确保加密密钥不会在没有用户交互的情况下自动释放。
* **应用KB5025885更新：**该更新引入了额外的安全启动证书并撤销了旧证书，减少降级攻击的暴露。
* **调整 PCR 配置：**更改TPM平台配置寄存器（PCRs）以包含额外的测量值，可以防止未经授权的密钥释放。
* **禁用网络启动选项：**在BIOS/UEFI设置中限制PXE启动功能，可以阻止主要的攻击途径之一。

bitpixie等漏洞的持续存在，凸显了基于硬件的安全实现所面临的更广泛问题。由于固件限制以及对制造商更新的依赖，在所有设备上更新安全启动证书是一个缓慢的过程。

微软计划在2026年前引入新的安全启动证书，但这留下了很大的的漏洞窗口。

**参考链接：**

> <https://cybersecuritynews.com/windows-11-bitlocker-encrypted-files-accessed/>

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

该漏洞如何发挥作用？

缓解策略

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