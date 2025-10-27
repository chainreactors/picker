---
title: 新的隐秘技术让黑客可获得Windows系统最高权限
url: https://www.freebuf.com/news/376019.html
source: FreeBuf网络安全行业门户
date: 2023-08-25
fetch_date: 2025-10-04T12:01:54.074606
---

# 新的隐秘技术让黑客可获得Windows系统最高权限

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

新的隐秘技术让黑客可获得Windows系统最高权限

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新的隐秘技术让黑客可获得Windows系统最高权限

2023-08-24 11:39:44

所属地 上海

据BleepingComputer消息，网络安全公司 Deep Instinct 的安全研究人员发布了一个滥用Windows筛选平台（ WFP) 来提升用户权限的工具NoFilter，能将访问者的权限增加到Windows上的最高权限级别——SYSTEM权限。

![](https://image.3001.net/images/20230824/1692854257_64e6e7f1238256c164a4f.png!small)

该实用程序在后利用场景中非常有用，在这种场景中，攻击者需要以更高的权限执行恶意代码，或者在其他用户已经登录到受感染设备时在受害者网络上横向移动。

微软将WFP 定义为一组 API 和系统服务，为创建网络过滤应用程序提供平台。开发人员可以使用 WFP API 创建代码，在网络数据到达目的地之前对其进行过滤或修改，这些功能在网络监控工具、入侵检测系统或防火墙中可见。

研究人员开发了三种新的攻击来提升的权限，既不会留下太多证据，也不会被众多安全产品检测到。

## 复制访问令牌

第一种方法允许使用 WFP 复制访问令牌，即在线程和进程的安全上下文中识别用户及其权限的代码片段。当线程执行特权任务时，安全标识符会验证关联的令牌是否具有所需的访问级别。

安全研究员解释称，调用 NtQueryInformationProcess 函数可以获取包含进程持有的所有令牌的句柄表。这些令牌的句柄可以复制，以便另一个进程升级到 SYSTEM。Windows 操作系统中一个名为 tcpip.sys的重要驱动程序 具有多个函数，可以通过设备 IO 请求向 WPF ALE（应用程序层执行）内核模式层调用这些函数，以进行状态过滤。NoFilter工具 通过这种方式滥用WPF来复制令牌，从而实现权限提升。

研究人员表示，通过避免调用 DuplicateHandle，可以提高隐蔽性，并且许多端点检测和响应解决方案可能会忽视恶意操作。

## 获取系统和管理员访问令牌

第二种技术涉及触发 IPSec 连接并滥用 Print Spooler 服务以将 SYSTEM 令牌插入表中。使用 RpcOpenPrinter 函数按名称检索打印机的句柄。通过将名称更改为“\\127.0.0.1”，该服务将连接到本地主机。在 RPC 调用之后，需要向 WfpAleQueryTokenById 发出多个设备 IO 请求才能检索 SYSTEM 令牌。

研究人员表示，这种方法比第一种方法更隐蔽，因为配置 IPSec 策略通常是由网络管理员等合法特权用户完成的操作。

第三种方法允许获取登录到受感染系统的另一个用户的令牌，以进行横向移动。研究人员表示，如果可以将访问令牌添加到哈希表中，则可以使用登录用户的权限启动进程。为了获取令牌并以登录用户的权限启动任意进程，研究人员滥用了 OneSyncSvc 服务和 SyncController.dll，它们是攻击性工具领域的新组件。

## 检测建议

黑客和渗透测试人员很可能会采用这三种方法，但Deep Instinct也给出了如下缓解措施：

* 配置与已知网络配置不匹配的新 IPSec 策略。
* 当 IPSec 策略处于活动状态时，RPC 调用 Spooler/OneSyncSvc。
* 通过多次调用 WfpAleQueryTokenById 来暴力破解令牌的 LUID。
* BFE 服务以外的进程向设备 WfpAle 发出设备 IO 请求。

> 参考来源：[New stealthy techniques let hackers gain Windows SYSTEM privileges](https://www.bleepingcomputer.com/news/security/new-stealthy-techniques-let-hackers-gain-windows-system-privileges/)

# 系统安全

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

复制访问令牌

获取系统和管理员访问令牌

检测建议

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