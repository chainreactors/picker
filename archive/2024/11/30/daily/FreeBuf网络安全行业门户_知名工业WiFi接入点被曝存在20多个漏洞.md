---
title: 知名工业WiFi接入点被曝存在20多个漏洞
url: https://www.freebuf.com/news/416495.html
source: FreeBuf网络安全行业门户
date: 2024-11-30
fetch_date: 2025-10-06T19:15:36.284775
---

# 知名工业WiFi接入点被曝存在20多个漏洞

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

知名工业WiFi接入点被曝存在20多个漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

知名工业WiFi接入点被曝存在20多个漏洞

2024-11-29 11:26:58

所属地 上海

近期，Advantech工业级无线接入点设备被曝光存在近二十个安全漏洞，部分漏洞可被恶意利用以绕过身份验证并执行高权限代码。![](https://image.3001.net/images/20241129/1732851076_674935841806b8cad795e.png!small)

网络安全公司Nozomi Networks在周三发布的分析报告中警告称：“这些漏洞带来了严重的安全风险，它们允许未经身份验证的远程代码以根权限执行，全面威胁到受影响设备的保密性、完整性和可用性。”

在负责任的披露流程之后，这些安全漏洞已在以下固件版本中得到修复：

- 1.6.5版本，适用于EKI-6333AC-2G和EKI-6333AC-2GD型号；
- 1.2.2版本，适用于EKI-6333AC-1GPO型号。

在这些被识别的漏洞中，有六个被标记为关键漏洞，它们使得攻击者能够通过植入后门获得对内部资源的持续访问，触发拒绝服务（DoS）攻击，甚至将受感染的端点转变为Linux工作站，以实现网络内的横向移动和进一步渗透。

在这六个关键漏洞中，有五个（CVE-2024-50370至CVE-2024-50374，CVSS评分为9.8）与操作系统命令中特殊元素的不当处理有关，而CVE-2024-50375（CVSS评分为9.8）则涉及关键功能缺乏身份验证的问题。

特别值得关注的是CVE-2024-50376（CVSS评分为7.3），这是一个跨站脚本（XSS）漏洞，它可以与CVE-2024-50359（CVSS评分为7.2）相结合，后者是一个需要身份验证的操作系统命令注入漏洞，使得攻击者能够通过无线方式执行任意代码。

为了成功实施这种攻击，外部恶意用户需要靠近Advantech的接入点并广播恶意信号。

当管理员访问Web应用程序中的“Wi-Fi分析器”部分时，攻击就会被触发，导致页面自动嵌入攻击者广播的信标帧信息，而未进行任何消毒检查。

![](https://image.3001.net/images/20241129/1732851113_674935a9b319ff8219a98.png!small)

Nozomi Networks指出：“攻击者可以通过其恶意接入点广播SSID（即Wi-Fi网络名称）。”因此，攻击者可以在其恶意接入点的SSID中嵌入JavaScript有效载荷，利用CVE-2024-50376触发Web应用程序内的XSS漏洞。

这将导致在受害者的Web浏览器上下文中执行任意JavaScript代码，进而可以与CVE-2024-50359结合，实现具有根权限的操作系统级别的命令注入。这种攻击可能以反向shell的形式出现，为攻击者提供持久的远程访问权限。

该公司进一步解释道：“这将使攻击者能够远程控制受损设备，执行命令，并进一步渗透网络，提取数据或部署额外的恶意脚本。”

参考来源：<https://thehackernews.com/2024/11/over-two-dozen-flaws-identified-in.html>

# 资讯

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