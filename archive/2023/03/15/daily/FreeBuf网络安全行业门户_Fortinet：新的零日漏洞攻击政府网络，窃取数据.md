---
title: Fortinet：新的零日漏洞攻击政府网络，窃取数据
url: https://www.freebuf.com/news/360360.html
source: FreeBuf网络安全行业门户
date: 2023-03-15
fetch_date: 2025-10-04T09:35:58.055782
---

# Fortinet：新的零日漏洞攻击政府网络，窃取数据

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

Fortinet：新的零日漏洞攻击政府网络，窃取数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Fortinet：新的零日漏洞攻击政府网络，窃取数据

2023-03-14 13:31:33

所属地 上海

![](https://image.3001.net/images/20230314/1678761668_640fdec49ea63c65acae9.png!small)

近日，根据 Fortinet 最新报告：不明来源的的攻击者利用零日漏洞针对政府和大型组织，导致操作系统和文件损坏以及数据丢失。

Fortinet于2023年3月7日发布了安全更新，以解决这个高危安全漏洞（CVE-2022-41328），该漏洞可以让攻击者执行未经授权的代码或命令。

该公司在公告中说：FortiOS中的路径名对受限目录漏洞的不当限制（路径穿越）[CWE-22]允许有特权的攻击者通过CLI命令读取和写入任意文件。

受影响的产品包括FortiOS 6.4.0至6.4.11版本，FortiOS 7.0.0至7.0.9版本，FortiOS 7.2.0至7.2.3版本，以及FortiOS 6.0和6.2的所有版本。

虽然该漏洞的公告没有提到该漏洞被人在野外利用，但Fortinet上周发布的一份报告显示，CVE-2022-41328漏洞已被用来入侵并攻陷客户的多个FortiGate防火墙设备。

## 数据窃取恶意软件

该事件是在被攻击的Fortigate设备中断后发现的，由于FIPS错误，系统进入错误模式并无法重新启动。

Fortinet说，发生这种情况是因为其支持FIPS的设备验证了系统组件的完整性，而且它们被设置为自动关闭并停止启动，以便在检测到破坏时阻止网络入侵。

这些Fortigate防火墙是通过受害者网络上的FortiManager设备被破坏的，因为它们同时停止，并且FortiGate路径遍历漏洞与通过FortiManager执行的脚本同时启动。

随后的调查显示，攻击者修改了设备固件镜像（/sbin/init），在启动过程开始前启动一个有效载荷（/bin/fgfm）。

这种恶意软件在收到含有";7(Zu9YTsA7qQ#vm "字符串的ICMP数据包时，可以进行数据渗透，下载和写入文件，或打开远程外壳。

## 用来攻击政府网络的零日

Fortinet认为，这些攻击具有很强的针对性，主要针对政府网络。攻击者还具有很强的攻击手段及能力，包括反向设计FortiGate设备的部分操作系统。因为该漏洞需要对FortiOS和底层硬件有深入的了解。

今年1月，Fortinet披露了一系列非常类似的事件，2022年12月打了补丁并被追踪为CVE-2022-42475的FortiOS SSL-VPN漏洞也被用作针对政府组织和政府相关实体的零日漏洞。

最后，该公司建议Fortinet的用户立即升级到FortiOS的补丁版本，以阻止潜在的攻击。

> 参考链接：www.bleepingcomputer.com/news/security/fortinet-new-fortios-bug-used-as-zero-day-to-attack-govt-networks/

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

数据窃取恶意软件

用来攻击政府网络的零日

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