---
title: Cisco曝超严重漏洞，黑客可修改管理员密码
url: https://www.freebuf.com/news/406337.html
source: FreeBuf网络安全行业门户
date: 2024-07-19
fetch_date: 2025-10-06T17:41:46.961717
---

# Cisco曝超严重漏洞，黑客可修改管理员密码

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

Cisco曝超严重漏洞，黑客可修改管理员密码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Cisco曝超严重漏洞，黑客可修改管理员密码

2024-07-18 13:54:20

所属地 上海

近日，思科公司披露了其智能软件管理器本地版（SSM On-Prem）中的一个关键漏洞，该漏洞允许未经身份验证的远程攻击者更改任何用户的密码，包括管理员用户的密码。这个漏洞被追踪为 CVE-2024-20419，其严重程度评分为 10 分。

![](https://image.3001.net/images/20240718/1721281815_6698ad17846733060ff4e.jpg!small)据悉，该漏洞是由于思科 SSM On-Prem 认证系统中密码更改过程执行不当造成的。

攻击者可以通过向受影响的设备发送特制的 HTTP 请求来利用这个漏洞。成功利用将允许攻击者以受影响用户的权限访问 Web UI 或 API，从而在未经授权的情况下对设备进行管理控制。

## 受影响的产品

* 思科 SSM On-Prem
* 思科智能软件管理器卫星版（SSM Satellite）

思科 SSM 卫星版已更名为思科智能软件管理器。对于 7.0 版本之前发布的版本，该产品称为思科 SSM 卫星版。从 7.0 版本开始，它被称为思科 SSM On-Prem。

## 已修复的软件

思科已发布软件更新来解决此漏洞。修复的版本如下：

![](https://image.3001.net/images/20240718/1721281902_6698ad6e0da8a8ed1bd23.png!small)

思科建议所有客户升级到修复版本以降低风险，保护其系统安全。

截至目前，尚未有公开的公告或证据表明此漏洞被恶意利用，思科的产品安全事件响应团队（PSIRT）将继续监控这一情况。

另外，拥有服务合同的客户应通过其常规更新渠道获得安全修复程序，没有服务合同的客户可以联系思科技术援助中心（TAC）以获得必要的更新。

## 如何检查思科智能软件管理器本地版的版本

### 访问管理门户

打开一个 Web 浏览器，输入思科 SSM On-Prem 服务器的 IP 地址和端口号。例如，如果 IP 地址是 172.16.0.1，则输入：https://172.16.0.1:8443/admin

### 登录

使用管理员凭据登录管理门户。

### 查找系统运行状况部分

登录后，导航到管理门户的“系统运行状况”部分。此部分通常显示的是思科 SSM On-Prem 安装的当前软件发布版本。

参考来源：https://cybersecuritynews.com/cisco-ssm-password-change-vulnerability/

# 安全漏洞 # cisco

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

受影响的产品

已修复的软件

如何检查思科智能软件管理器本地版的版本

* 访问管理门户
* 登录
* 查找系统运行状况部分

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