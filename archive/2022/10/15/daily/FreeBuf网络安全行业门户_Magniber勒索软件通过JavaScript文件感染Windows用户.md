---
title: Magniber勒索软件通过JavaScript文件感染Windows用户
url: https://www.freebuf.com/news/346826.html
source: FreeBuf网络安全行业门户
date: 2022-10-15
fetch_date: 2025-10-03T19:56:56.007054
---

# Magniber勒索软件通过JavaScript文件感染Windows用户

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

Magniber勒索软件通过JavaScript文件感染Windows用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Magniber勒索软件通过JavaScript文件感染Windows用户

2022-10-14 15:05:53

所属地 上海

Bleeping Computer 网站披露，9 月初，Magniber 勒索软件运营商创建了宣传网站，力推 Windows 10 虚假的安全更新文件，一旦用户下载了包含 JavaScript 的恶意文件（ZIP档案），其文件就会遭到勒索软件加密。![1665731195_63490a7b6533d38e705df.jpg!small?1665731194007](https://image.3001.net/images/20221014/1665731195_63490a7b6533d38e705df.jpg!small?1665731194007)

惠普公司威胁情报团队在一份报告中指出，Magniber 勒索软件运营商要求受害用户支付高达 2500 美元的费用，以获得解密工具并恢复其文件。![1665731202_63490a82125600be9f146.jpg!small?1665731200709](https://image.3001.net/images/20221014/1665731202_63490a82125600be9f146.jpg!small?1665731200709)

受威胁的Windows版本

2022 年 1 月，Magniber 运营商主要使用 Chrome 和 Edge 浏览器的安全更新来推送恶意 Windows 应用程序包文件（.APPX）。

## ****Magniber**** **使用新的感染链**

以往 Magniber传播活动中，背后运营商主要使用 MSI 和 EXE 文件，最近则改用了 JavaScript 文件，名称如下：

> 系统.关键.升级.Win10.0.ba45bd8ee89b1.js
>
> 系统安全数据库升级.Win10.0.jse
>
> 抗病毒\_Upgrade\_Cloud.29229c7696d2d84.jse
>
> 警报.系统.软件.升级.392fdad9ebab262cc97f832c40e6ad2c.js

这些文件经过混淆处理，使用 "DotNetToJScript "技术变种，在系统内存中执行.NET 文件，可以很好降低被主机上防病毒产品发现的风险。

.NET文件对使用自身包装器进行隐秘系统调用的 shellcode 代码进行解码，并在终止自己的 shellcode 代码之前将其注入新进程。

shellcode 代码通过 WMI 删除卷影副本文件，并通过 “bcdedit” 和 “wbadmin” 禁用备份和恢复功能。这样的话，受害者恢复其文件的选项就会变得的很少，增加了攻击者获得报酬的机会，

为了执行这一操作，Magniber 使用 Windows 中用户帐户控制（UAC）功能的旁路。它依赖于一种机制，该机制涉及创建允许指定 shell 命令的新注册表项。

在后面的步骤中，将执行“fodhelper.exe”实用程序来运行用于删除卷影副本的脚本。![1665731240_63490aa832339b021229c.jpg!small?1665731238732](https://image.3001.net/images/20221014/1665731240_63490aa832339b021229c.jpg!small?1665731238732)

UAC绕过程序

最后，Magniber 对主机上的文件进行加密，并删除包含受害者恢复文件指示的赎金说明。![1665731248_63490ab0ba7792c5048d3.jpg!small?1665731247374](https://image.3001.net/images/20221014/1665731248_63490ab0ba7792c5048d3.jpg!small?1665731247374)

Magniber 的新感染链(HP)

惠普的分析师注意到，虽然 Magniber 试图将加密只限于特定的文件类型，但在枚举过程中生成的伪哈希并不完美，会导致哈希碰撞和 "附带损害"（即也会加密非目标的文件类型）。

用户可以通过定期备份文件并将其保存在一个离线存储设备上来防御勒索软件攻击，这样可以将数据恢复到一个新安装的操作系统上。注意，在恢复数据之前，用户应确保其备份未被感染。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/magniber-ransomware-now-infects-windows-users-via-javascript-files/

# 系统安全 # 恶意软件

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

Magniber 使用新的感染链

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