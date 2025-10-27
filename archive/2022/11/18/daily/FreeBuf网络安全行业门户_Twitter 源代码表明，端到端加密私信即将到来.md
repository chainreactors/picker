---
title: Twitter 源代码表明，端到端加密私信即将到来
url: https://www.freebuf.com/news/350033.html
source: FreeBuf网络安全行业门户
date: 2022-11-18
fetch_date: 2025-10-03T23:07:13.560386
---

# Twitter 源代码表明，端到端加密私信即将到来

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

Twitter 源代码表明，端到端加密私信即将到来

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Twitter 源代码表明，端到端加密私信即将到来

2022-11-17 15:03:11

所属地 上海

据BleepingComputer 11月16日消息，Twitter 正准备为其平台上用户之间的私信 (DM) 添加端到端加密 (E2EE)，预计这一功能将很快到来。

![](https://image.3001.net/images/20221117/1668668648_6375dce80f657a811a1c7.png!small)

这是一项广受欢迎且需求量很大的功能，它将有助于进一步保护通信双方的私密性，免受任何第三方甚至是法律请求的影响。

早在2018年，Twitter就曾尝试推出 E2EE 系统的原型，并将其命名为“秘密对话”（Secret Conversation），但随后就没有了下文。而最近，移动研究员 Jane Manchun Wong发推称，她发现Twitter的安卓版源代码中出现了关于E2EE 的内容。在一个字符串中，出现了“这个号码是根据你这次对话的加密密钥生成，如果它与接收者手机中的号码相匹配，就能保证端到端加密”的描述。

而Twitter CEO马斯克对此回复了一个“眨眼”的表情，暗示该功能确实正在开发中。

![](https://image.3001.net/images/20221117/1668668709_6375dd250cc7d9d621470.png!small)马斯克对发现E2EE代码的推文回复了一个“眨眼”的表情

## 为什么 Twitter 需要 E2EE

端到端加密确保信息以加密形式发送，收件人需要解密才能得到其中的内容。为此，双方必须使用加密密钥对信息进行加密或解密。在大多数 E2EE 实践中，发件人使用收件人的数字签名公钥来加密信息，而收件人使用私钥来解密。

在 Twitter 的案例中，Wong 提到了“对话密钥”（conversation key），因此实施的 E2EE 方法可能是“对称的”，这意味着聊天中的两个人都使用相同的密钥进行加密和解密。发件人的消息在传输过程中被转换成不可读的密文，因此任何中间人，如互联网服务提供商、黑客，甚至Twitter本身，都无法读取消息内容。

如果 Twitter 在 DM 上引入 E2EE，即使平台被黑客攻破，用户间的这种加密通信也不容易被破解。2020 年 7 月，黑客曾入侵员工帐户并访问管理面板读取了 36 位知名用户的 DM 收件箱，并下载其中 7 位用户的内容。如果 Twitter 当时有 E2EE，那么所有黑客获得的消息都将是不可读的密文，从而减轻对受感染用户的影响。

> 参考来源：[Twitter source code indicates end-to-end encrypted DMs are coming](https://www.bleepingcomputer.com/news/security/twitter-source-code-indicates-end-to-end-encrypted-dms-are-coming/)

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

为什么 Twitter 需要 E2EE

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