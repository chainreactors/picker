---
title: 潜藏系统2个月未被发现，新型网络攻击瞄准中国高价值目标
url: https://www.freebuf.com/articles/410082.html
source: FreeBuf网络安全行业门户
date: 2024-09-04
fetch_date: 2025-10-06T18:27:36.366709
---

# 潜藏系统2个月未被发现，新型网络攻击瞄准中国高价值目标

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

潜藏系统2个月未被发现，新型网络攻击瞄准中国高价值目标

* ![]()
* 关注

潜藏系统2个月未被发现，新型网络攻击瞄准中国高价值目标

2024-09-03 11:48:50

所属地 上海

![](https://image.3001.net/images/20240903/1725335319_66d687176caf3ecc5a11e.jpg!small)近期，针对说中文的企业的新一轮网络攻击活动引起了广泛关注。攻击者使用了Cobalt Strike载荷，针对特定目标进行了精确打击。Securonix研究人员Den Iuzvyk和Tim Peck在报告中指出，攻击者设法在系统内横向移动，建立持久性，并在两个多月的时间里未被发现。

## **攻击概括**

这个秘密的攻击活动代号为SLOW#TEMPEST，尚未归因于任何已知的威胁行为者。攻击开始于恶意的ZIP文件，当这些文件被解压缩时，会激活感染链，导致在被攻击的系统上部署后开发工具包。攻击者通过发送精心设计的钓鱼邮件，诱导受害者下载并执行恶意文件，从而启动感染链。

研究人员强调，鉴于诱饵文件中使用的语言，与中国相关的商业或政府部门很可能是其特定的目标。尤其是那些雇佣了遵守“远程控制软件规定”的人员的公司，通常被认为具有较高的商业价值和数据价值，吸引了攻击者的注意。

值得注意的是，感染链还设置了定期执行名为"lld.exe"的恶意文件的任务，该文件可以直接在内存中运行任意shellcode，从而在磁盘上留下最小的足迹。

研究人员表示，攻击者进一步通过手动提升内置访客用户帐户的权限，使自己能够在被攻击的系统中隐藏。这个账户通常被禁用并且最小化权限，但只有将其添加到关键的管理员组并分配新密码，就可以转变成一个强大的访问点。这个后门允许他们以最小的检测维持对系统的访问，毕竟访客账户通常不像其他用户账户那样受到密切监控。

未知的威胁行为者随后使用远程桌面协议（RDP）和通过Mimikatz密码提取工具获得的凭据，在网络中横向移动，然后在每台机器上设置返回他们命令与控制（C2）服务器的远程连接。

## **攻击细节**

### **攻击手段****：****Beacon和Listener**

Beacon：Beacon是Cobalt Strike运行在目标主机上的payload，负责与攻击者的命令与控制（C2）服务器通信，接收和执行任务。

Listener：Listener模块用于接收Beacon的请求信息，并转发给攻击者的Team Server控制器。

### **隐蔽通信**

多种通信协议：Cobalt Strike支持HTTP、HTTPS、DNS和SMB等多种通信协议，确保C2通信的隐蔽性和稳定性。

分段载荷：攻击者使用分段载荷技术，防止shellcode过长导致异常，并通过多阶段下载和解码来规避检测。

## Cobalt Strike 分析

Cobalt Strike Payloads确实支持多种语言环境，并且可以在不同的操作系统上运行。

### Cobalt Strike Payloads支持的语言

* C
* C#
* Python
* Java
* Perl
* Powershell脚本
* Powershell命令
* Ruby
* Raw
* 免杀框架Veli中的shellcode

### Cobalt Strike Payloads在不同操作系统上的使用情况

Cobalt Strike Payloads可以在Linux和Windows上运行，这得益于其基于Meterpreter shellcode的设计，使得它能够跨平台执行。

### Cobalt Strike Payloads的本地化支持

Cobalt Strike Payloads的本地化支持主要通过其模块化设计实现，允许攻击者根据目标环境定制payload，以绕过本地安全检测。

### Cobalt Strike Payloads的检测与防御

检测Cobalt Strike Payloads通常依赖于内存取证技术和特定的工具，如Yara规则。防御措施包括使用端点检测和响应(EDR)技术来实时监控内存活动，以及定期更新安全软件和系统补丁。

## **攻击影响**

1. 数据泄露：攻击者通过Cobalt Strike获取了受感染系统上的敏感数据，包括员工和客户的个人信息。
2. 系统控制：攻击者能够在受感染系统中执行任意代码，控制系统行为，甚至加密文件进行勒索。
3. 系统中断：攻击导致一些企业系统中断，员工不得不重新使用纸张和笔进行记录，经销商甚至让员工回家，因为系统中断导致无法进行正常工作。
4. 业务中断：企业因系统中断和数据泄露，面临巨大的经济损失和业务中断风险。

总的来说，针对说中文的企业的新一轮网络攻击活动正愈演愈烈，攻击者使用了Cobalt Strike载荷，通过鱼叉式钓鱼和隐蔽通信手段，成功渗透并控制了目标系统。

但这并不只是特例。近年来越来越多的APT组织持续对我国包括企业、政府部门、研究机构、关键基础设施等高价值机构发起网络攻击。

报告数据显示，2024年上半年，针对中文企业的网络攻击呈现出攻击频次和强度增加、受害行业多样化以及新型攻击手段不断涌现的特点。与2023年同期相比，2024年上半年的网络攻击频次和强度均有所增加。特别是APT攻击和勒索软件攻击的次数大幅上涨，表明这些攻击方式仍然是网络安全领域的主要威胁。

参考来源：<https://thehackernews.com/2024/08/new-cyberattack-targets-chinese.html>

# 系统安全 # 数据安全

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

攻击概括

攻击细节

* 攻击手段：Beacon和Listener
* 隐蔽通信

Cobalt Strike 分析

* Cobalt Strike Payloads支持的语言
* Cobalt Strike Payloads在不同操作系统上的使用情况
* Cobalt Strike Payloads的本地化支持
* Cobalt Strike Payloads的检测与防御

攻击影响

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