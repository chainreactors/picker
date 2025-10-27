---
title: 韩国 ERP 供应商遭黑客攻击，被悄悄安上后门
url: https://www.freebuf.com/news/405396.html
source: FreeBuf网络安全行业门户
date: 2024-07-09
fetch_date: 2025-10-06T17:45:08.278932
---

# 韩国 ERP 供应商遭黑客攻击，被悄悄安上后门

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

韩国 ERP 供应商遭黑客攻击，被悄悄安上后门

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

韩国 ERP 供应商遭黑客攻击，被悄悄安上后门

2024-07-08 10:20:42

所属地 上海

据The Hacker News消息，一家未具名的韩国企业资源规划（ERP）供应商服务器被发现遭到入侵，从而传播了一个名为Xctdoor的基于Go的后门程序。

![](https://image.3001.net/images/20240708/1720405419_668b4dabf3bb915898794.jpg!small)

AhnLab安全情报中心（ASEC）于2024年5月发现了这一攻击，指出其攻击手法与朝鲜恶意软件组织Lazarus Group的一附属组织Andariel类似。该组织曾于2017年通过在软件更新程序中插入恶意程序的方式，利用ERP解决方案传播HotCroissant等恶意软件。

在ASEC最近分析的事件中，攻击者通过可执行文件被篡改，使用regsvr32.exe进程从特定路径执行一个DLL文件，该文件能够窃取系统信息，包括击键、屏幕截图和剪贴板内容，并执行攻击者发出的命令。

ASEC 表示，Xctdoor 使用 HTTP 协议与命令与控制服务器通信，而数据包加密则采用MT19937算法和 Base64 算法。 攻击中还使用了一个名为 XcLoader 的恶意软件，这是一个注入器恶意软件，负责将 Xctdoor 注入合法进程（如 "explorer.exe"）。

ASEC还发现另一个朝鲜黑客组织Kimusky使用了一种代号为HappyDoor的后门，该后门早在2021年7月就已投入使用。该攻击链利用鱼叉式网络钓鱼电子邮件传播一个压缩文件，文件包含一个混淆的JavaScript或dropper，通过regsvr32.exe执行DLL文件，执行时会创建并运行HappyDoor和一个诱饵文件。 HappyDoor可通过Http与远程服务器通信，便于窃取信息、下载/上传文件，以及更新和终止自身活动。

安全研究员伊丹-塔拉布（Idan Tarab）表示，这也是继Konni网络间谍组织（又名Opal Sleet、Osmium或TA406）之后又一起针对韩国策划的 "大规模 "恶意软件传播活动。

**参考来源：**

> [South Korean ERP Vendor's Server Hacked to Spread Xctdoor Malware](https://thehackernews.com/2024/07/south-korean-erp-vendors-server-hacked.html)

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