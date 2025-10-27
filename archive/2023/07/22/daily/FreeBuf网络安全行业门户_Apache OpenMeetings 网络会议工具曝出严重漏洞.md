---
title: Apache OpenMeetings 网络会议工具曝出严重漏洞
url: https://www.freebuf.com/news/372703.html
source: FreeBuf网络安全行业门户
date: 2023-07-22
fetch_date: 2025-10-04T11:54:55.544635
---

# Apache OpenMeetings 网络会议工具曝出严重漏洞

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

Apache OpenMeetings 网络会议工具曝出严重漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Apache OpenMeetings 网络会议工具曝出严重漏洞

2023-07-21 11:44:46

所属地 上海

The Hacker News 网站披露，网络会议服务 Apache OpenMeetings 存在多个安全漏洞，Sonar 漏洞研究员 Stefan Schiller 表示网络攻击者可以利用这些漏洞夺取管理帐户的控制权，并在易受影响的服务器上执行恶意代码。![1689911027_64b9fef3ef94e7fec5c4a.png!small](https://image.3001.net/images/20230721/1689911027_64b9fef3ef94e7fec5c4a.png!small)

2023 年 3 月 20 日，研究人员披露了漏洞详情，2 个月后。 更新的 Openmeetings 7.1.0 版本中解决了漏洞问题。

**漏洞的列表详情如下：**

> CVE-2023-28936 （CVSS 得分：5.3）- 邀请哈希值检查不足；
>
> CVE-2023-29032 （CVSS 得分：8.1）- 身份验证绕过，导致通过邀请哈希进行不受限制的访问；
>
> CVE-2023-29246 (CVSS 得分：7.2) - 一个 NULL 字节 (%00) 注入，允许具有管理员权限的攻击者执行代码。

据悉，使用 OpenMeetings come 创建的会议邀请不仅绑定到特定的会议室和用户，还会附带一个特定的哈希，应用程序使用该哈希来检索与邀请相关的详细信息。简言之，前两个漏洞与用户提供的哈希与数据库中储存的哈希之间的弱哈希比较有关。此外，还存在一个特别的情况，即允许在没有分配会议室的情况下创建房间邀请，导致出现邀请没有附加会议室的情况。

这时候，网络攻击者就可以利用上述漏洞创建一个会议议程并加入相应的房间，此时会为管理员用户创建一个到不存在房间的邀请。下一步，网络攻击者可以利用弱哈希比较错误来枚举发送的邀请，并通过提供通配符哈希输入来兑换邀请。![1689911063_64b9ff174ad6b2ee1ff19.png!small](https://image.3001.net/images/20230721/1689911063_64b9ff174ad6b2ee1ff19.png!small)

Schiller 进一步表示虽然当相关会议议程被删除时，房间也会被删除，但网络攻击者在房间里的存在使这里成为僵尸房间。此外，尽管在兑换此类邀请的哈希时会引发错误，但会为具有此用户完全权限的受邀者创建有效的 web 会话。

换言之，僵尸会议室可能允许攻击者获得管理员权限并对 OpenMeetings 实例进行修改，包括添加和删除用户和组、更改会议室设置以及终止连接用户的会话。

此外，Sonar 表示第三个漏洞源于一项功能，该功能使管理员能够为与 ImageMagick 相关的可执行文件配置路径（ImageMagick 是一种用于编辑和处理图像的开源软件），这就使得具有管理员权限的攻击者可以通过将 ImageMagic 路径更改为“/bin/sh%00x”并触发任意 shell 命令来获得代码执行。

最后，Schiller 强调目前上传一个包含有效图像头和任意 shell 命令的假图像时，转换会产生/bin/sh，第一个参数是假图像，有效地执行了其中的每个命令。结合帐户接管，此漏洞使自注册攻击者能够在底层服务器上远程执行代码。

**文章来源：**

> https://thehackernews.com/2023/07/apache-openmeetings-web-conferencing.html

# 漏洞

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