---
title: 新型Linux后门病毒Auto-color瞄准美国和亚洲系统
url: https://www.freebuf.com/articles/system/423126.html
source: FreeBuf网络安全行业门户
date: 2025-02-28
fetch_date: 2025-10-06T20:37:39.797576
---

# 新型Linux后门病毒Auto-color瞄准美国和亚洲系统

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

新型Linux后门病毒Auto-color瞄准美国和亚洲系统

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

新型Linux后门病毒Auto-color瞄准美国和亚洲系统

2025-02-27 19:43:42

所属地 上海

一种新发现的Linux恶意软件，名为Auto-color，正在针对北美和亚洲的教育机构和政府实体进行攻击。该病毒采用先进的隐身技术，以规避检测和清除。

## Auto-color的隐身与持久化机制

Palo Alto Networks Unit 42的研究人员发现了这种恶意软件。他们的调查显示，该病毒在2024年11月至12月期间活跃。Auto-color的独特之处在于它使用了无害的文件名，如“door”或“egg”等常见词汇，来伪装其初始可执行文件。

Unit 42的博客文章由Alex Armstrong撰写，文中指出：“尽管文件大小总是相同，但哈希值不同。这是因为恶意软件作者将加密的C2配置负载静态编译到每个恶意软件样本中。”

在执行时，Auto-color会检查其文件名，如果不匹配指定的名称，则会启动安装阶段。这一阶段包括在系统中嵌入一个恶意库植入物，模仿合法的系统库。恶意软件的行为会根据用户是否具有root权限而有所不同。如果具有root权限，它将安装一个旨在覆盖核心系统功能的库。

![](https://image.3001.net/images/20250228/1740697285040763_d8abd52919cb40939f5a44434062af3b.png!small)Auto-color流程图（来源：Palo Alto Networks）

Auto-color隐身的一个关键方面是它操纵了Linux系统的ld.preload文件。这使得恶意软件能够确保其恶意库在其他系统库之前加载，从而能够拦截和修改系统功能。这种技术赋予了恶意软件对系统行为的显著控制能力，包括隐藏其网络活动的能力。

## 高级网络隐藏与加密通信

Auto-color采用复杂的方法来隐藏其网络连接。它钩住了C标准库中的函数，从而能够过滤和操纵系统的网络连接信息。通过更改/proc/net/tcp文件的内容，它有效地隐藏了与命令和控制服务器的通信，使安全分析师难以检测。研究人员指出，这种操纵比之前发现的恶意软件所使用的类似技术更为先进。

恶意软件使用一种专有的加密机制来连接远程服务器，从动态生成的配置文件或嵌入的加密负载中检索目标服务器详细信息。它使用自定义的流密码与攻击者的基础设施进行安全通信。

博客文章写道：“流密码是一种加密方案，其中密钥与密文的每个字节进行交互。”

一旦建立连接，恶意软件会与服务器交换加密消息，从而在受感染的系统上执行命令。

## 应对措施与建议

Auto-color的发现凸显了基于Linux的恶意软件的日益复杂化，因为它能够操纵核心系统进程，其先进的规避技术对目标行业构成了重大威胁。组织应加强其安全措施，包括严格的权限控制、行为威胁检测和对Linux系统的持续监控，以降低感染风险。

##### 作者：Deeba Ahmed

![ ](https://image.3001.net/images/20250228/1740697285840277_abb18c2bafd14cf69395762bf409c0a4!small)

Deeba是Hackread.com的资深网络安全记者，拥有超过十年的网络安全报道经验，涵盖网络犯罪、漏洞和安全事件。她的专业知识和深入分析使她成为该平台可信报道的关键贡献者。

**参考来源：**

> [New Backdoor Auto-color Linux Targets Systems in US and Asia](https://hackread.com/new-backdoor-auto-color-linux-systems-us-asia/)

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