---
title: ESXi勒索软件攻击利用SSH隧道逃避检测
url: https://www.freebuf.com/articles/es/420911.html
source: FreeBuf网络安全行业门户
date: 2025-01-28
fetch_date: 2025-10-06T20:09:34.082070
---

# ESXi勒索软件攻击利用SSH隧道逃避检测

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

ESXi勒索软件攻击利用SSH隧道逃避检测

* ![]()
* 关注

* [企业安全](https://www.freebuf.com/articles/es)

ESXi勒索软件攻击利用SSH隧道逃避检测

2025-01-27 10:05:11

所属地 上海

![](https://image.3001.net/images/20250127/1737975637262072_146647f06619446fa22191f584e62492.png!small)

网络安全公司Sygnia的研究人员警告称，ESXi勒索软件攻击背后的威胁行为者利用SSH隧道技术针对虚拟化环境进行攻击，以逃避检测。

## 攻击手法：利用未受监控的ESXi设备

勒索软件团伙利用未受监控的ESXi设备在企业网络中持久存在并获取访问权限。他们采用“就地取材”的技术，利用SSH等原生工具创建未被检测到的SOCKS隧道，用于与C2服务器通信。

研究人员报告称，在许多情况下，攻击者通过使用管理凭据或利用已知漏洞绕过身份验证来入侵ESXi设备。一旦获得设备访问权限，攻击者就会使用原生SSH功能或部署具有类似功能的其他常见工具来设置隧道。

## ESXi设备的日志管理挑战

ESXi设备的日志按活动分成多个文件，这增加了取证调查和监控活动的复杂性。配置日志转发对于简化监控和集中事件捕获至关重要。

Sygnia报告指出：“虽然ESXi确实支持一些第三方监控或遥测代理，但这些工具的可用性有限。作为一种更全面且更具成本效益的解决方案，配置从ESXi服务器到外部syslog服务器的syslog转发可以解决此问题。这种设置能够集中监控ESXi服务器内的所有活动，并作为日志保留的手段。”

报告还列出了以下关键日志文件，这些文件通常有助于检测和调查使用SSH隧道技术的攻击：

* `/var/log/vobd.log`（VMware观察守护进程日志）
* `/var/log/shell.log`（ESXi shell活动日志）
* `/var/log/hostd.log`（主机代理日志）
* `/var/log/auth.log`（认证日志）

报告还提供了多个与恶意活动相关的ESXi syslog文件中常见的活动和消息示例。

**参考来源：**

> [ESXi ransomware attacks use SSH tunnels to avoid detection](https://securityaffairs.com/173487/cyber-crime/esxi-ransomware-attacks-use-ssh-tunnels-to-avoid-detection.html)

# 企业安全 # 安全报告

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