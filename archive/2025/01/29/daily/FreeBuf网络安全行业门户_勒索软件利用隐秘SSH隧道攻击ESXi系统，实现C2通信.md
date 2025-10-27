---
title: 勒索软件利用隐秘SSH隧道攻击ESXi系统，实现C2通信
url: https://www.freebuf.com/articles/system/420939.html
source: FreeBuf网络安全行业门户
date: 2025-01-29
fetch_date: 2025-10-06T20:08:49.525829
---

# 勒索软件利用隐秘SSH隧道攻击ESXi系统，实现C2通信

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

勒索软件利用隐秘SSH隧道攻击ESXi系统，实现C2通信

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

勒索软件利用隐秘SSH隧道攻击ESXi系统，实现C2通信

2025-01-28 16:31:00

所属地 上海

![image](https://image.3001.net/images/20250128/1738065693571064_e9537f71c1e946efa73a7babcb75227d.png!small)

网络安全研究人员发现，针对ESXi系统的勒索软件攻击不仅利用其访问权限，还将这些设备重新用作隧道流量的通道，以连接到命令与控制（C2）基础设施，从而躲避检测。

Sygnia的研究人员钟元浩（Aaron）和饶仁杰在上周发布的一份报告中表示：“未受监控的ESXi设备正越来越多地被用作持久化机制和访问企业网络的网关。威胁行为者通过采用‘就地取材’技术，使用SSH等原生工具在其C2服务器与被入侵环境之间建立SOCKS隧道。”

通过这种方式，攻击者可以混入合法流量中，并在被入侵的网络上建立长期持久性，几乎不会被安全控制措施检测到。

## ESXi系统成为攻击目标

这家网络安全公司表示，在其许多事件响应案例中，ESXi系统要么是通过使用管理员凭据被入侵，要么是通过利用已知的安全漏洞绕过身份验证保护。随后，威胁行为者被发现使用SSH或其他具有等效功能的工具建立隧道。

研究人员指出：“由于ESXi设备具有弹性且很少意外关闭，这种隧道技术可以在网络中充当半持久性的后门。”

![image](https://image.3001.net/images/20250128/1738065694896140_9e9f86b984ad4843aabf2ad7a8ac1a98.png!small)

Sygnia还强调了监控ESXi日志的挑战，强调需要配置日志转发，以便将所有相关事件集中在一个地方进行取证调查。

为了检测涉及在ESXi设备上使用SSH隧道的攻击，建议组织审查以下四个日志文件：

* `/var/log/shell.log`（ESXi shell活动日志）
* `/var/log/hostd.log`（主机代理日志）
* `/var/log/auth.log`（身份验证日志）
* `/var/log/vobd.log`（VMware观察守护程序日志）

## Andariel组织利用RID劫持技术

与此同时，AhnLab安全情报中心（ASEC）详细介绍了与朝鲜有关的Andariel组织发起的一次攻击，该攻击涉及使用一种称为相对标识符（RID）劫持的技术，在下次登录时秘密修改Windows注册表，为访客或低权限账户分配管理员权限。

这种持久化方法非常隐蔽，因为它利用了普通账户不会受到与管理员账户相同级别的监控这一事实，从而使威胁行为者能够在不被发现的情况下执行恶意操作。

然而，为了执行RID劫持，攻击者必须已经入侵了一台机器并获得管理员或SYSTEM权限，因为这需要将标准账户的RID值更改为管理员账户的RID值（500）。

![image](https://image.3001.net/images/20250128/1738065695578283_7f78c874c2a04a0ab8d6d6be9d75d10f.png!small)

在ASEC记录的攻击链中，威胁行为者在使用PsExec和JuicyPotato等权限提升工具获得SYSTEM权限后，创建了一个新账户并为其分配了管理员权限。

该公司表示：“威胁行为者随后使用‘net localgroup’命令将创建的账户添加到远程桌面用户组和管理员组。当账户被添加到远程桌面用户组时，该账户可以通过RDP访问。”

“一旦RID值被更改，Windows操作系统将识别威胁行为者创建的账户具有与目标账户相同的权限，从而实现权限提升。”

## 新的EDR规避技术

此外，还发现了一种基于硬件断点的方法可以用来绕过Windows事件追踪（ETW）检测。ETW提供了一种机制来记录由用户模式应用程序和内核模式驱动程序引发的事件。

这种方法涉及使用名为NtContinue的原生Windows函数，而不是SetThreadContext，来设置调试寄存器并避免触发ETW日志记录和事件，这些事件通常由EDR解析以标记可疑活动，从而规避依赖于SetThreadContext的遥测。

Praetorian研究员Rad Kawar表示：“通过在CPU级别利用硬件断点，攻击者可以在用户态中挂钩函数并操纵遥测，而无需直接进行内核补丁——这对传统防御构成了挑战。”

“这很重要，因为它突显了对手可以使用的一种技术，在实施‘无补丁’挂钩时规避并保持隐蔽，从而防止AMSI扫描并避免ETW日志记录。”

**参考来源：**

> [Ransomware Targets ESXi Systems via Stealthy SSH Tunnels for C2 Operations](https://thehackernews.com/2025/01/ransomware-targets-esxi-systems-via.html)

# 终端安全 # 企业安全

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