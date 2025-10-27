---
title: 致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业
url: https://www.freebuf.com/news/422787.html
source: FreeBuf网络安全行业门户
date: 2025-02-26
fetch_date: 2025-10-06T20:37:09.369419
---

# 致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业

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

致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

致命RAT钓鱼攻击瞄准使用中国云服务的亚太行业

2025-02-25 11:21:00

所属地 上海

![image](https://image.3001.net/images/20250225/1740467042241097_647d4861734449eb8dde016d06d47e81.png!small)

亚太地区的多家工业组织已成为钓鱼攻击的目标，这些攻击旨在传播一种名为致命RAT（FatalRAT）的已知恶意软件。卡巴斯基工业控制系统应急响应中心在一份周一发布的报告中表示：“攻击者利用合法的中国云内容分发网络（CDN）myqcloud和网易有道云笔记服务作为其攻击基础设施的一部分。”报告还指出：“攻击者采用了一种复杂的多阶段载荷递送框架，以确保逃避检测。”

这次攻击的主要目标是政府机构和工业组织，特别是制造业、建筑业、信息技术、电信、医疗、电力与能源、大规模物流和运输等行业，涉及台湾、马来西亚、中国、日本、泰国、韩国、新加坡、菲律宾、越南和香港等地区。邮件中使用的诱饵附件表明，此次钓鱼攻击主要针对中文用户。

值得注意的是，致命RAT的活动曾利用虚假的谷歌广告作为分发渠道。2023年9月，Proofpoint公司记录到另一起以电子邮件为媒介的钓鱼攻击，传播了多种恶意软件家族，包括致命RAT、Gh0st RAT、紫狐（Purple Fox）和ValleyRAT。这两次入侵活动的有趣之处在于，它们主要针对中文用户和日本组织。其中部分活动被归因于一个名为银狐APT（Silver Fox APT）的威胁组织。

### 攻击链与恶意软件加载

最新攻击链的起点是一封包含中文文件名ZIP压缩包的钓鱼邮件。当用户打开该压缩包后，会启动第一阶段加载程序，随后向有道云笔记发送请求，以获取动态链接库（DLL）文件和致命RAT配置器。配置器模块则从note.youdao[.]com下载另一条笔记的内容，以访问配置信息，同时打开一个诱饵文件以避免引起怀疑。

另一方面，DLL是第二阶段加载程序，负责从配置文件中指定的服务器（“myqcloud[.]com”）下载并安装致命RAT载荷，同时显示一个关于应用程序运行问题的虚假错误信息。此次攻击的一个重要特点是使用了DLL侧加载技术，以推进多阶段感染序列并加载致命RAT恶意软件。

![image](https://image.3001.net/images/20250225/1740467043550556_19671d8abd6344ac8709f03909bb472f.png!small)

卡巴斯基表示：“威胁行为者采用了一种黑白结合的方法，利用合法二进制文件的功能，使事件链看起来像正常活动。攻击者还使用了DLL侧加载技术，将恶意软件的持久性隐藏在合法进程内存中。”致命RAT还执行了17项检查，以确定恶意软件是否在虚拟机或沙盒环境中运行。如果其中任何一项检查失败，恶意软件将停止执行。

### 恶意软件功能与幕后黑手

致命RAT在等待命令与控制（C2）服务器的进一步指令之前，会终止所有rundll32.exe进程实例，并收集系统信息和已安装的各种安全解决方案的相关数据。致命RAT是一款功能强大的木马，能够记录键盘输入、损坏主引导记录（MBR）、打开/关闭屏幕、在Google Chrome和Internet Explorer等浏览器中搜索和删除用户数据、下载AnyDesk和UltraViewer等附加软件、执行文件操作、启动/停止代理，以及终止任意进程。

目前尚不清楚是谁在背后操纵使用致命RAT的攻击，但战术和工具与其他活动的重叠表明，“它们都反映了某种程度上相关的不同系列攻击”。卡巴斯基以中等置信度评估，背后可能是一个中文威胁行为者。研究人员表示：“致命RAT的功能为攻击者提供了几乎无限的攻击开发可能性：通过网络传播、安装远程管理工具、操纵设备、窃取和删除机密信息。”

“在攻击的各个阶段持续使用中文服务和界面，以及其他间接证据，表明可能有一个中文威胁行为者参与其中。”

**参考来源：**

> [FatalRAT Phishing Attacks Target APAC Industries Using Chinese Cloud Services](https://thehackernews.com/2025/02/fatalrat-phishing-attacks-target-apac.html)

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