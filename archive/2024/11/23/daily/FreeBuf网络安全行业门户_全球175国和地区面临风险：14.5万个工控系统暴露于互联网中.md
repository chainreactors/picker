---
title: 全球175国和地区面临风险：14.5万个工控系统暴露于互联网中
url: https://www.freebuf.com/news/415908.html
source: FreeBuf网络安全行业门户
date: 2024-11-23
fetch_date: 2025-10-06T19:18:20.659685
---

# 全球175国和地区面临风险：14.5万个工控系统暴露于互联网中

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

全球175国和地区面临风险：14.5万个工控系统暴露于互联网中

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

全球175国和地区面临风险：14.5万个工控系统暴露于互联网中

2024-11-22 11:31:46

所属地 上海

据The Hacker News消息，攻击面管理公司 Censys 的分析发现，有多达14.5万个工业控制系统 （ICS） 暴露于公开的互联网络中，涉及175 个国家和地区，仅美国就占总暴露量的三分之一以上。

![](https://image.3001.net/images/20241122/1732246441_673ffba9a62ba874bddc7.png!small)

这些暴露指标来自几种常用工控系统协议，包括Modbus、IEC 60870-5-104、CODESYS、OPC UA 等。 Censys发现，38% 的ICS暴露位于北美，35.4% 位于欧洲，22.9% 位于亚洲，1.7% 位于大洋洲，1.2% 位于南美洲，0.5% 位于非洲。其中，Modbus、S7 和 IEC 60870-5-104 在欧洲更广泛，而 Fox、BACnet、ATG 和 C-more 在北美更常见。这两个区域使用的一些工控系统服务包括 EIP、FINS 和 WDBRPC。

Censys 联合创始人兼首席科学家 Zakir Durumeric 在一份声明中表示，许多暴露的工控协议其历史可以追溯到上世纪70年代，但目前仍然是工业流程的基础，且没有像其他领域一样得到相应的安全改进。

Censys 也发现，用于监控和与工控系统交互的人机界面（HMI）也越来越多地通过互联网支持远程访问。 大部分暴露的人机界面位于美国，其次是德国、加拿大、法国、奥地利、意大利、英国、澳大利亚、西班牙和波兰。

有趣的是，大多数已识别的人机界面和 ICS 服务都位于移动或商业级互联网服务提供商 (ISP)，如 Verizon、Deutsche Telekom 、Magenta Telekom 和 Turkcell 等。人机界面通常包含公司徽标或工厂名称，这有助于识别所有者和行业，但工控协议很少提供相同的信息，因此几乎无法识别和通知暴露的所有者。 要解决这个问题，可能需要与托管这些服务的主要电信公司合作。

暴露的工控系统和 OT 网络为攻击者提供了广泛的攻击面，因此企业组织需要采取措施来识别并加以保护，包括更新默认凭证并监控网络是否存在恶意活动。

## 针对工控系统的网络攻击有所增加

专门针对工控系统的网络攻击相对较少，迄今为止仅发现了 9 种恶意软件。但自俄乌战争爆发以来，针对该系统的恶意软件攻击正有所增加。一些比较典型的僵尸网络恶意软件利用 OT 网络的默认凭证，不仅实施了分布式拒绝服务 （DDoS） 攻击，还擦除了其中的数据。

今年7月初，一家位于乌克兰的能源公司成为FrostyGoop恶意软件的目标，该恶意软件被发现利用 Modbus TCP 通信来破坏运营技术（OT）网络。FrostyGoop也称为 BUSTLEBERM，是一种用 Golang 编写的 Windows 命令行工具，可导致公开暴露的设备出现故障，并最终导致拒绝服务 （DoS）。 根据Censys 捕获的遥测数据，在 2024 年 9 月 2 日至 10 月 2 日的一个月内，就有 1088175 台 Modbus TCP 设备暴露在互联网中。

去年，美国宾夕法尼亚州阿利基帕市水务局也因为暴露的Unitronics可编程逻辑控制器（PLC）而被黑客组织攻击，导致相关系统下线并被迫改为手动操作。

**参考来源：**

> [Over 145,000 Industrial Control Systems Across 175 Countries Found Exposed Online](https://thehackernews.com/2024/11/over-145000-industrial-control-systems.html)

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

针对工控系统的网络攻击有所增加

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