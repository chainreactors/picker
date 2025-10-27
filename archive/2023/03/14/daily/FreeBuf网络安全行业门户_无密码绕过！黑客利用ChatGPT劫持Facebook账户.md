---
title: 无密码绕过！黑客利用ChatGPT劫持Facebook账户
url: https://www.freebuf.com/news/360243.html
source: FreeBuf网络安全行业门户
date: 2023-03-14
fetch_date: 2025-10-04T09:30:25.162421
---

# 无密码绕过！黑客利用ChatGPT劫持Facebook账户

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

无密码绕过！黑客利用ChatGPT劫持Facebook账户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

无密码绕过！黑客利用ChatGPT劫持Facebook账户

2023-03-13 14:56:39

所属地 香港

Dark Reading 网站披露， 3 月 3 日- 3 月 9 日，每天至少有 2000 人从 Google Play 应用商店下载"快速访问 ChatGPT“ 的 Chrome 恶意扩展。据悉，一名威胁攻击者可能利用该恶意扩展泄露包括商业账户在内的数千个 Facebook 账户。![1678690800_640ec9f00aedbc78b0365.png!small](https://image.3001.net/images/20230313/1678690800_640ec9f00aedbc78b0365.png!small)

从 Guardio 的分析结果来看，恶意 "快速访问 Chat GPT "的扩展程序承诺用户可以快速与近期大火的人工智能聊天机器人 Chat GPT 进行互动。然而事实上，该扩展程序偷偷地从浏览器中窃取所有授权活动会话的 cookies，并安装了一个后门，使恶意软件运营者能够轻松获得用户 Facebook 账户的超级管理员权限。

值得注意的是，"快速访问 Chat GPT "扩展程序仅仅是威胁攻击者利用 ChatGPT 大火来分发恶意软件和渗透系统的众多方式之一。

近几个月，随着 ChatGPT 持续火爆，以其主题的钓鱼电子邮件急剧增加，越来越多的攻击者使用假冒的 ChatGPT 应用程序传播 Windows 和 Android 恶意软件。

## ****以**** ****Facebook**** ****商业账户为目标的 ”********僵尸军团“****

"快速访问 Chat GPT "的扩展程序实际上是通过连接聊天机器人的 API 实现了对 ChatGPT 的快速访问，但在访问过程中，该扩展还收集了用户浏览器中存储的包括谷歌、Twitter 和 YouTube 以及任何其它活动在内的所有 cookie 列表。

如果某个用户在 Facebook 上有一个活动、经过验证的会话，则恶意扩展插件为开发人员访问 Meta 的 Graph API。API 访问使扩展能够获取与用户 Facebook 帐户相关的所有数据，甚至可以代表用户采取各种行动。

更不幸的是，恶意扩展代码中的一个组件允许劫持用户的 Facebook 帐户，其方法是在用户帐户上注册一个恶意应用程序，并获得 Facebook 的批准。对此 Guardio 表示，Facebook 生态系统下的应用程序通常是一个 SaaS 服务，它被批准使用其特殊的 API。因此，通过在用户帐户中注册应用程序，威胁攻击者可以在受害者的 Facebook 帐户上获得完全管理模式，而无需获取密码或尝试绕过 Facebook 的双重身份验证。

如果恶意扩展遇到了一个 商业 Facebook 帐户，它会快速获取与该帐户相关的所有信息，包括当前活动的促销活动、信用余额、货币、最低计费阈值等。

## 一个有经济动机的网络罪犯

在 Facebook 通过其 Meta Graph API 授予访问权之前，首先必须确认该请求是来自一个经过认证的可信用户，为了规避这一预防措施，威胁者在恶意的浏览器扩展中加入了代码，确保从受害者的浏览器向Facebook 网站发出的所有请求都被修改了标题，以便它们看起来也是可信的，这使得该扩展能够使用受感染的浏览器自由地浏览任何 Facebook 页面（包括进行 API 调用和操作），而不留下任何痕迹。

最后，Guardio 评估后表示，威胁行为者可能会将其从活动中收获的信息卖给出价最高的人，该公司还预计攻击者有可能创建一个被劫持的 Facebook商业账户的机器人大军，利用受害者账户的钱来发布恶意广告。

**参考文章：**

> https://www.darkreading.com/application-security/chatgpt-browser-extension-hijacks-facebook-business-accounts

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

以 Facebook 商业账户为目标的 ”僵尸军团“

一个有经济动机的网络罪犯

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