---
title: 揭秘macOS Apple Silicon内核防护机制：KASLR破解技术分析
url: https://www.freebuf.com/articles/system/421738.html
source: FreeBuf网络安全行业门户
date: 2025-02-14
fetch_date: 2025-10-06T20:35:59.511042
---

# 揭秘macOS Apple Silicon内核防护机制：KASLR破解技术分析

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

揭秘macOS Apple Silicon内核防护机制：KASLR破解技术分析

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

揭秘macOS Apple Silicon内核防护机制：KASLR破解技术分析

2025-02-13 08:54:47

所属地 上海

![image](https://image.3001.net/images/20250213/1739437313868991_edb883e3209a467e89a9bd6a61ff8c79.webp!small)

韩国大学的安全研究人员近日揭示了一项针对搭载Apple Silicon处理器的macOS系统的新漏洞，该漏洞名为“SysBumps”，成功绕过了内核地址空间布局随机化（KASLR）机制。KASLR是保护内核内存免遭攻击的关键安全机制。

在2024年ACM SIGSAC计算机与通信安全会议（CCS '24）上，研究人员展示了这一发现，暴露了Apple先进内核隔离技术的重大缺陷。

## **KASLR技术简介**

KASLR是一种内核加固技术，通过在系统启动时随机化内存地址，防止攻击者预测关键内核结构的位置。这种随机性对于缓解内存损坏漏洞至关重要，因为它迫使攻击者猜测内核的基地址，而高熵值使得这一任务的难度呈指数级增加。

在Apple Silicon的macOS系统中，Apple进一步强化了KASLR，实施了“双重映射”内核隔离技术，将用户空间和内核空间的地址布局分开。然而，SysBumps攻击表明，即使是这些高级防御措施也能被绕过，研究人员在多种M系列处理器（包括M1、M2及其Pro和Max版本）上实现了96.28%的成功率。

## **SysBumps攻击的工作原理**

SysBumps利用了macOS系统调用中的推测执行漏洞。推测执行是现代处理器中的一种性能优化技术，能够提前预测并执行指令。虽然这有助于提升速度，但也会在微架构组件（如转换后备缓冲区TLB）中留下痕迹，攻击者可以将其作为侧信道加以利用。

该攻击主要分为三个步骤：

\*\*触发推测执行：\*\*某些macOS系统调用会对用户提供的参数进行验证检查。通过故意误导分支预测器，SysBumps诱导系统对无效输入进行推测执行。这种短暂的执行会访问内核地址，如果地址有效，则会在TLB中留下可检测的痕迹。

\*\*TLB侧信道分析：\*\*通过逆向工程了解Apple Silicon的TLB架构，攻击者采用“prime+probe”技术监控TLB状态变化。通过测量访问延迟，他们能够区分有效和无效的内核地址。

\*\*破解KASLR：\*\*通过系统性地探测内存区域，SysBumps会识别有效的内核地址范围，并高精度计算内核基地址。

Apple的双重映射内核隔离技术本应通过确保用户空间无法访问内核地址来防止此类攻击。然而，SysBumps利用系统调用中的推测执行绕过了这一屏障。

## **攻击性能与实际影响**

研究人员通过性能监控单元（PMU）逆向工程了Apple M系列处理器的TLB架构，揭示了其共享设计的关键细节。这些知识使他们能够构建出区分有效和无效内核地址的攻击原语。

SysBumps攻击通过暴露内核的随机化布局，削弱了macOS对抗内存损坏漏洞的核心防御。该攻击的平均执行时间仅为3秒，在现实场景中既实用又高效。其影响十分严重：一旦KASLR被攻破，攻击者将更容易利用其他漏洞获取未授权访问或执行任意代码。

## **缓解措施与行业响应**

研究人员于2024年4月负责任地向Apple披露了这一发现。Apple已确认该漏洞（追踪编号为CVE-2024-54531），并正在研究缓解策略。研究提出了几种应对措施：

\*\*TLB分区：\*\*将用户和内核进程的TLB入口分开，可以消除共享竞争，减少侧信道泄漏。

\*\*推测执行隔离：\*\*在条件分支前插入DSB和ISB等序列化指令，可以防止敏感代码路径的推测执行。

\*\*TLB行为修改：\*\*为无效地址分配TLB入口，将使攻击者更难区分有效和无效地址。

随着Apple向ARM架构的过渡，解决此类漏洞对于维护用户信任和系统安全至关重要。鉴于这些发现，macOS用户应尽快安装最新的安全补丁，以保持系统的安全性。

**参考来源：**

> [KASLR Exploited: Breaking macOS Apple Silicon Kernel Hardening Techniques](https://cybersecuritynews.com/kaslr-exploited-apple-silicon/)

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