---
title: 福特曝WiFi安全漏洞，官方称仍可安全驾驶
url: https://www.freebuf.com/news/374817.html
source: FreeBuf网络安全行业门户
date: 2023-08-15
fetch_date: 2025-10-04T12:02:41.791766
---

# 福特曝WiFi安全漏洞，官方称仍可安全驾驶

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

福特曝WiFi安全漏洞，官方称仍可安全驾驶

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

福特曝WiFi安全漏洞，官方称仍可安全驾驶

2023-08-14 17:57:36

所属地 上海

据bleepingcomputer消息，福特汽车供应商的安全人员向福特公司报告了一个安全漏洞，漏洞编号 CVE-2023-29468。该漏洞位于汽车信息娱乐系统集成的 WiFi 系统 WL18xx MCP 驱动程序中，允许 WiFi 范围内的攻击者使用特制的帧触发缓冲区溢出。![](https://image.3001.net/images/20230814/1692006998_64d9fa5649ed3a0d4fb5c.jpg!small)

资料显示，SYNC3 是一款现代信息娱乐系统，支持车载 WiFi 热点、电话连接、语音命令、第三方应用程序等，YNC3 信息娱乐系统被广泛应用于多款福特和林肯汽车上。

受影响的汽车型号如下所示：![](https://image.3001.net/images/20230814/1692007028_64d9fa74bb0f7976a414f.png!small)

该漏洞发布后，安全研究人员与福特汽车公司、供应商和其他汽车制造商合作，承诺将很快推出相关漏洞补丁，客户可通过USB安装到车辆上，以保护其客户、产品和企业免受影响。

福特汽车公司发布公告称，尚未有任何证据表明该漏洞已经被黑客利用，原因在于利用WiFi软件漏洞需要较为扎实的黑客技术，且攻击者还需在物理上靠近已打开点火装置和 Wi-Fi 设置的车辆。

福特汽车公司进一步指出，哪怕该漏洞已经被利用，也不会影响车辆乘坐人员的人身安全，因为该漏洞只纯在于娱乐系统集成中，转向、油门和制动等控制装置有专门的防火墙保护。“如果用户担心该漏洞带来风险，可通过 SYNC 3 信息娱乐系统的设置菜单关闭 WiFi 功能。”

事实上，随着汽车智能化程度持续提升，所包含的安全漏洞也越来越多，福特、大众、丰田等知名汽车制作商屡屡被曝出存在安全漏洞，直接影响用户的使用体验和安全。

英国消费杂志《Which》曾联合网络安全公司Context Information Security发布报告称：大众、福特两大汽车行业巨头计算机系统存在大量安全漏洞，可导致车辆监控、预警系统发出错误信息，误导驾驶员行驶判断，并泄露娱乐系统中的相关敏感信息。

报告显示，大众Polo SELTSI手动1.0L的汽车计算机系统中，负责车辆湿滑路面行驶时牵引力控制的模块存在安全漏洞，黑客可借此获取车辆信息娱乐系统中存储的电话号码、地址以及导航历史记录等敏感信息。

此外，研究人员还发现，只要抬起汽车前部的大众徽章就能进入前雷达模块，黑客可通过这一动作进一步篡改车辆碰撞预警系统。

报告数据显示，福特汽车的安全漏洞似乎更严重一些。研究人员发现，他们使用亚马逊的“廉价笔记本电脑和售价25英镑的渗透小工具”，就能拦截篡改福特福克斯车型上由轮胎压力监控系统（TPMS）发送的消息，比如，在轮胎没有充气时错误地报告轮胎已经正确充气，以此干扰驾驶员做出正确的行驶判断。

在更进一步的分析中，福特计算机系统的代码中还被发现了一些包括wifi详细信息和一个似乎是福特生产线计算机系统的密码，扫描过后，确认该网络属于是福特位于密歇根州底特律的装配厂。同样的，福特汽车中也存在应用程序随时共享车辆敏感信息的现象。

安全研究人员所测试的这两款车型在世界范围内的购买率十分之高，一旦这些漏洞被黑客组织用于投入实战进行攻击，后果不堪设想。

参考来源：https://www.bleepingcomputer.com/news/security/ford-says-cars-with-wifi-vulnerability-still-safe-to-drive/

# 系统安全 # 数据安全 # 漏洞分析

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