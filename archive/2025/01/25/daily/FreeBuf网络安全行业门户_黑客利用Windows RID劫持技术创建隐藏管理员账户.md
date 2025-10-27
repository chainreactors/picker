---
title: 黑客利用Windows RID劫持技术创建隐藏管理员账户
url: https://www.freebuf.com/articles/system/420811.html
source: FreeBuf网络安全行业门户
date: 2025-01-25
fetch_date: 2025-10-06T20:10:11.526487
---

# 黑客利用Windows RID劫持技术创建隐藏管理员账户

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

黑客利用Windows RID劫持技术创建隐藏管理员账户

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

黑客利用Windows RID劫持技术创建隐藏管理员账户

2025-01-24 12:25:38

所属地 上海

![Hackers use Windows RID hijacking to create hidden admin account](https://image.3001.net/images/20250125/1737741651444291_706b795e69d04afc8f997c80f9ad1556.jpg!small)

一个来自朝鲜的黑客组织正在使用一种名为RID劫持的技术，该技术可以欺骗Windows系统，使其将低权限账户视为具有管理员权限的账户。

黑客使用了一个自定义的恶意文件和一个开源工具来进行劫持攻击。这两种工具都可以执行攻击，但韩国网络安全公司AhnLab的研究人员表示，它们之间存在一些差异。

## RID劫持的工作原理

在Windows系统中，相对标识符（RID）是安全标识符（SID）的一部分，SID是分配给每个用户账户的唯一标识符，用于区分不同的账户。

RID可以取不同的值来表示账户的访问级别，例如“500”表示管理员账户，“501”表示来宾账户，“1000”表示普通用户，“512”表示域管理员组。

当攻击者修改低权限账户的RID，使其与管理员账户的RID值匹配时，就会发生RID劫持，Windows系统会授予该账户提升的权限。

然而，执行这种攻击需要访问SAM注册表，因此黑客首先需要入侵系统并获得SYSTEM权限。

![RID hijacking process](https://image.3001.net/images/20250125/1737741652135083_a80fc139c62547e2b1dffa5e6acbda74.jpg!small)**RID劫持过程** *来源：ASEC*

## Andariel攻击

AhnLab的安全情报中心ASEC的研究人员将此次攻击归因于Andariel威胁组织，该组织与朝鲜的Lazarus黑客组织有关联。

攻击始于Andariel通过利用漏洞在目标系统上获得SYSTEM权限。

黑客使用PsExec和JuicyPotato等工具启动SYSTEM级别的命令提示符，从而实现初始权限提升。

尽管SYSTEM权限是Windows系统中的最高权限，但它不允许远程访问，无法与图形用户界面（GUI）应用程序交互，且非常容易被检测到，并且无法在系统重启后保持持久性。

为了解决这些问题，Andariel首先使用“net user”命令创建一个隐藏的低权限本地用户，并在命令末尾添加“`”字符。

通过这种方式，攻击者确保该账户无法通过“net user”命令显示，只能在SAM注册表中识别。然后，他们执行RID劫持，将该账户的权限提升为管理员。

![Hidden Andariel account on compromised Windows system](https://image.3001.net/images/20250125/1737741652426229_abacb2c77ea0442eaebd05e88a409f44.png!small)**Windows系统上的隐藏Andariel账户** *来源：AhnLab*

据研究人员称，Andariel将其账户添加到远程桌面用户组和管理员组中。

这种RID劫持是通过修改安全账户管理器（SAM）注册表实现的。朝鲜黑客使用自定义恶意软件和开源工具来执行这些更改。

![Tools]()*来源：ASEC*

尽管SYSTEM权限可以直接创建管理员账户，但根据安全设置的不同，可能会受到某些限制。提升普通账户的权限则更加隐蔽，更难被检测和阻止。

Andariel还试图通过导出修改后的注册表设置、删除密钥和恶意账户，然后从保存的备份中重新注册来掩盖其踪迹，从而在不出现在系统日志中的情况下重新激活账户。

## 如何防范RID劫持攻击

为了降低RID劫持攻击的风险，系统管理员应使用本地安全机构（LSA）子系统服务来检查登录尝试和密码更改，并防止未经授权的访问和对SAM注册表的更改。

此外，建议限制PsExec、JuicyPotato等工具的执行，禁用来宾账户，并为所有现有账户（即使是低权限账户）启用多因素认证。

值得注意的是，RID劫持技术早在2018年就已经被公开，当时安全研究员Sebastián Castro在DerbyCon 8上将其作为一种Windows系统的持久化技术进行了演示。

---

通过以上分析，我们可以看到，RID劫持是一种隐蔽且危险的攻击手段，系统管理员应采取多种措施来防范此类攻击，确保系统的安全性。

**参考来源：**

> [Hackers use Windows RID hijacking to create hidden admin account](https://www.bleepingcomputer.com/news/security/hackers-use-windows-rid-hijacking-to-create-hidden-admin-account/)

# 网络安全 # 终端安全

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