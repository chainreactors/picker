---
title: 三菱电机 PLC 曝出多个严重安全漏洞
url: https://www.freebuf.com/news/351595.html
source: FreeBuf网络安全行业门户
date: 2022-12-06
fetch_date: 2025-10-04T00:34:43.665904
---

# 三菱电机 PLC 曝出多个严重安全漏洞

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

三菱电机 PLC 曝出多个严重安全漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

三菱电机 PLC 曝出多个严重安全漏洞

2022-12-05 14:56:22

所属地 上海

美国网络安全和基础设施安全局 (CISA) 在上周发布了一份工业控制系统 (ICS) 咨询，对三菱电机 GX Works3 工程软件存在的多个漏洞发出了安全警告。

![](https://image.3001.net/images/20221205/1670223409_638d9631b2213111cbc86.png!small)

GX Works3是一种用于 ICS 环境的工程软件，能够从控制器上传和下载程序、排除软硬件故障以及执行相应的操作维护。由于功能广泛，使得该软件平台成为攻击者的一个强有力的”集火“目标，攻击者希望破坏此类系统以控制受管理的 PLC。

在CISA揭露的10个缺陷中，有 3 个涉及敏感数据的明文存储，4 个涉及使用硬编码加密密钥，2 个涉及使用硬编码密码，1 个涉及凭证保护不足。最严重的漏洞CVE-2022-25164和CVE-2022-29830的 CVSS 评分高达 9.1，可在无需任何权限的情况下被滥用，以获取对 CPU 模块的访问权限并获取有关项目文件的信息。

三菱表示，工程软件是工业控制器安全链中的一个关键组成部分，如果其中出现任何漏洞，对手可能会滥用它们最终危及托管设备，从而危及受监管的工业过程。

CISA也提到了一个CVSS 评分为8.6的MELSEC iQ-R 系列中的拒绝服务 (DoS) 漏洞信息，并指出由于缺乏适当的输入验证，成功利用此漏洞可能允许未经身份验证的远程攻击者通过发送特制数据包，在目标产品上造成拒绝服务。

## 缓解措施

三菱已经宣布相关补丁将在不久之后发布，在此之前建议应用以下缓解措施：

* 尽可能限制不受信任方访问安全 CPU 项目文件；
* 在传输和静止时充分保护安全 CPU 项目文件（例如通过加密）；
* 更改安全 CPU 模块上设置的所有弱密码；
* 切勿重复使用相同的凭据打开安全 CPU 项目文件和访问安全 CPU 模块。

> 参考来源：[CISA Warns of Multiple Critical Vulnerabilities Affecting Mitsubishi Electric PLCs](https://thehackernews.com/2022/12/cisa-warns-of-multiple-critical.html)

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

缓解措施

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