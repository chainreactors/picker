---
title: 热门摄像头曝零日漏洞，黑客借此入侵政府部门
url: https://www.freebuf.com/news/414217.html
source: FreeBuf网络安全行业门户
date: 2024-11-02
fetch_date: 2025-10-06T19:17:03.594967
---

# 热门摄像头曝零日漏洞，黑客借此入侵政府部门

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

热门摄像头曝零日漏洞，黑客借此入侵政府部门

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

热门摄像头曝零日漏洞，黑客借此入侵政府部门

2024-11-01 10:24:55

所属地 上海

据GreyNoise公司安全研究人员Konstantin Lazarev披露，PTZOptics PTZ 摄像头存在两个零日漏洞，漏洞编号分别是CVE-2024-8956和CVE-2024-8957，目前已经发现有黑客正在利用这些零日漏洞发起网络攻击。![](https://image.3001.net/images/20241101/1730432357_67244d65d887fa1feb5ce.jpg!small)

PTZ摄像机是一种集成了平移（Pan）、倾斜（Tilt）和变焦（Zoom）功能的摄像头，能够通过遥控或自动控制系统进行全方位的监控。这种相机广泛应用于各种场景，如安全监控、交通监控、远程会议等，能够提供高质量的视频传输和灵活的监控角度调整‌。

2024年4月，GreyNoise在其蜜罐网络上的AI驱动威胁检测工具Sift检测到异常活动，并发现了上述两个漏洞。值得一提的是，在事后复盘分析时，GreyNoise研究人员发现了一次针对摄像头的基于CGI的API和嵌入的'ntp\_client'的利用尝试，旨在实现命令注入。

### 漏洞信息

**CVE-2024-8956**

漏洞类型：弱身份验证问题，允许未经授权的用户访问CGI API。

影响：基于Hi3516A V600 SoC V60、V61和V63的支持NDI的摄像机，运行的VHD PTZ摄像机固件版本早于6.3.40。

攻击者可以利用此漏洞，通过构造特殊的请求，绕过身份验证，访问摄像机的CGI API。这可能导致敏感信息泄露，如用户名、MD5密码哈希和网络配置，更严重的情况下，攻击者可能会利用此漏洞进行远程代码执行，完全接管摄像头，或将其感染恶意软件，进而攻击网络中的其他设备。

**CVE-2024-8957**

漏洞类型：远程代码执行
影响范围：基于Hi3516A V600 SoC V60、V61和V63的支持NDI的摄像机，运行的VHD PTZ摄像机固件版本早于6.3.40。

由于“ntp\_client”二进制文件处理的“ntp.addr”字段中的输入清理不足，攻击者可以使用特制的有效载荷插入命令以进行远程代码执行。利用此漏洞可能会导致摄像头完全被接管、被机器人感染、转移到连接同一网络的其他设备或中断视频源

针对上述两大漏洞，PTZOptics于2024年9月17日发布了安全更新，但部分型号如PT20X-NDI-G2和PT12X-NDI-G2等因已达到使用寿命而未获得固件更新。后来，PTZOptics于2024年10月25日收到了有关扩大范围的通知，但截至2024年11月1日时尚未发布针对这些型号的修复程序。

GreyNoise指出，利用这两个漏洞可能导致完全接管摄像头，感染机器人，转移到同一网络上连接的其他设备，或中断视频源。

![](https://image.3001.net/images/20241101/1730432371_67244d734cb0cec3a69ac.jpg!small)

尽管初始活动的源头在蜜罐攻击后不久就消失了，但GreyNoise 在6月份观察到了使用wget下载shell脚本进行反向shell访问的单独尝试。

### 建议措施

升级固件：建议受影响的用户尽快升级到PTZOptics摄像机的最新固件版本，特别是对于未收到更新的型号。
监控网络活动：对网络进行持续监控，以检测任何异常活动，这可能是攻击者利用此漏洞的迹象。
加强安全措施：采取额外的安全措施，如更改默认凭据、限制远程访问和强化身份验证机制，以减少潜在的风险。

参考来源：<https://www.bleepingcomputer.com/news/security/hackers-target-critical-zero-day-vulnerability-in-ptz-cameras/>

# 数据安全

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