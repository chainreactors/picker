---
title: Discord 推出端到端音频、视频加密通话功能
url: https://www.freebuf.com/news/411234.html
source: FreeBuf网络安全行业门户
date: 2024-09-20
fetch_date: 2025-10-06T18:27:10.238066
---

# Discord 推出端到端音频、视频加密通话功能

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

Discord 推出端到端音频、视频加密通话功能

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Discord 推出端到端音频、视频加密通话功能

2024-09-19 10:28:39

所属地 上海

![Discord](https://image.3001.net/images/20240919/1726725124_66ebbc04304f7032207bb.jpg!small)

近日，Discord 推出了 DAVE 协议，这是一个定制的端到端加密 (E2EE) 协议，旨在保护平台上的音频和视频通话免遭未经授权的拦截。

DAVE 是在 Trail of Bits 网络安全专家的帮助下创建的，该专家还对 E2EE 系统的代码和实施进行了审核。

新系统将涵盖用户在私人频道中的一对一音频和视频通话、小型群组聊天中的音频和视频通话、用于大型群组对话的基于服务器的语音频道以及实时流媒体。

Discord 在公告中写道： 他们将开始将 DM、群组 DM、语音频道和 Go Live 流中的语音和视频迁移至使用 E2EE。用户将能够确认通话何时进行了端到端加密，并对这些通话中的其他成员进行验证。

Discord 最初是为游戏玩家在游戏过程中进行交流而建立的，现在已发展成为世界上最流行的交流平台之一，满足了具有共同兴趣爱好的群体、创作者、企业和各种社区的需求。

DAVE 的推出是该平台加强数据安全和隐私保护的重要举措，该平台的使用人数已超过 2 亿。

最重要的是，Discord 决定将协议及其支持库开源，以便安全研究人员进行审查。此外，还发布了一份包含完整技术信息的白皮书，以确保对社区的透明度。

## DAVE 技术概述

DAVE 使用 WebRTC 编码转换 API，允许在媒体帧（音频和视频）编码后和打包传输前对其进行加密。接收端对帧进行解密，然后解码。

只有特殊的编解码器元数据（如标题和保留序列）未加密。

![DAVE's operational overview](https://image.3001.net/images/20240919/1726725128_66ebbc08064b94cc0ad10.jpg!small)

DAVE 的运行概况，资料来源：Discord

在密钥管理方面，信息层安全（MLS）协议用于安全和可扩展的群组密钥交换，每个参与者都有一个按发送者计算的对称媒体加密密钥。椭圆曲线数字签名算法（ECDSA）则用于生成身份密钥对。

当一个群组的组成发生变化时，比如一个成员离开或一个新成员加入，这时候群组的加密状态会通过生成新密钥，这个过程应该在不会对参与者造成明显干扰的情况下完成。

Discord 表示，MLS 会增加密钥交换的延迟，但 DAVE 的设计能将延迟控制在几百毫秒以内，即使在大型群组通话中也是如此。

最后，在用户验证方面，有一些带外方法，如比较从群组的 MLS 时序状态得出的验证码（称为 “语音隐私码”）。

由于每次通话都会为用户分配一个新的密钥，因此通过使用短暂的身份密钥可以防止持续跟踪。

![Screen with Voice Privacy Codes](https://image.3001.net/images/20240919/1726725131_66ebbc0b170711b365f2b.jpg!small)

语音隐私代码屏幕，来源：Discord

## 分阶段推出

Discord 现已开始将所有符合条件的频道迁移到 DAVE，用户可以通过查看界面上的相应指示器来确认他们的通话是否经过端到端加密。

预计还需要一段时间，所有用户才能在所有设备和频道上完全访问新的 E2EE 系统。

用户除了升级到最新的客户端应用程序外无需做任何其他操作，老版本的客户端将仅限于传输加密。最初推出的版本将涵盖 Discord 的桌面和移动应用程序，网络客户端后续也将面世。

> 参考来源：[Discord rolls out end-to-end encryption for audio, video calls (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/discord-rolls-out-end-to-end-encryption-for-audio-video-calls/)

# 加密 # Discord

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

DAVE 技术概述

分阶段推出

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