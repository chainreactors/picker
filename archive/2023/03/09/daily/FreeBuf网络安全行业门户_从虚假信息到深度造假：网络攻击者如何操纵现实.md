---
title: 从虚假信息到深度造假：网络攻击者如何操纵现实
url: https://www.freebuf.com/news/359699.html
source: FreeBuf网络安全行业门户
date: 2023-03-09
fetch_date: 2025-10-04T09:01:50.440740
---

# 从虚假信息到深度造假：网络攻击者如何操纵现实

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

从虚假信息到深度造假：网络攻击者如何操纵现实

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

从虚假信息到深度造假：网络攻击者如何操纵现实

2023-03-08 11:40:29

所属地 上海

近期，电视剧《狂飙》的爆火，激起了一些UP主的二创激情，将剧中的“CP”角色通过AI换脸移植到其他影视片段中，形成让网友惊呼“眼前一黑”的戏剧化效果，同时也收获了满满流量。乍一看这只是单纯的娱乐行为，但有时诸如”AI换脸“等深度造假技术（Deepfakes）可不只是”逗你笑“这么简单，背后的安全隐患不容忽视。

![](https://image.3001.net/images/20230308/1678255473_64082571b594606d65dcd.png!small)

《狂飙》中安欣和高启强的角色人脸被AI换脸至《西游记》女儿国的桥段中

## 什么是深度造假？

深度造假是指将真实图像、视频甚至音频进行替换、伪造，以此可以实现对信息的操纵。要创建质量足以用于深度造假的音视频，往往需要 AI（人工智能） 和 ML（机器学习）技术。使用这类技术不同于一般类型的信息操纵，不需要采取片面截取、屏蔽等方式来让信息按自身的意图传递，而是**更加接近信息本源，以”狸猫换太子“的方式制作虚假内容，**因此在技术上更加高阶。Cato Networks 安全战略高级总监 Etay Maor认为，现今AI 生成的文本（例如 GPT3）已经与深度伪造结合使用，以创建更具互动性、看起来像人类的对话机器人。

## 深度造假举例

深度造假围绕音视频可以有各种形式，有些简单，有些更高级。一下例举一些时下流行的深度造假形式：

### 换脸

换脸是将视频或图像中的某个人脸替换为另一个人的行为。换脸需要专门的软件，但不一定要基于先进的技术，一般人甚至可以找到支持换脸的移动应用程序。移动应用程序中可用的面部交换通常仅限于简单的用例，例如在某电影场景中将用户的照片和演员的面部进行交换。

![](https://image.3001.net/images/20230308/1678255535_640825af2e45400ecca12.png!small)

而高级的换脸需要更多的模型训练和代码，因此需要 GPU，这既昂贵又占用资源。下方的视频截图展示了一个高级的换脸伪造示例，把著名影星汤姆·姆克鲁斯的脸换在了视频中的主播身上。

![](https://image.3001.net/images/20230308/1678255554_640825c22e24369698ef8.png!small)

据悉，在这个例子中，需要在 GPU 上进行两个小时的训练以及几天的专业视频编辑后期处理。这还不是最复杂的，因为这名主播的声音和发型与汤姆·姆克鲁斯相似，从而适当减少了机器训练和后期处理的工作量。

### 口型同步

口型同步又被称为”木偶大师“（Puppet Master），是一种操纵口型图像的技术，使人看起来好像在说他们实际上没有说过的话。与换脸训练模型相比，口型同步的技术基于合成面具，是在原始图像的人物脸上训练模型，特别是在嘴部动作上，并将其放置在模仿者的模型之上，并对他们进行口型同步。

![](https://image.3001.net/images/20230308/1678255594_640825ea43f7a5fbd35fa.png!small)

### 音频

这一类深度伪造类型基于音频。Audio deep fakes 是一种音频文件，它采用真人的声音并使其听起来像是在说他们从未说过的话。音频深度伪造是通过获取音频文件、为声音分配注释、根据注释训练 ML 模型以将声音与文本相关联，进而生成新的音频文件。

## 深度造假的网络风险

目前，深度造假的效果正越来越达到以假乱真的地步，进行造假的方法也变得更加容易而，且创建速度也比以往任何时候都快。这使**深度造假在网络上成为强大的武器化工具，可用于社会工程、欺诈、威胁等网络犯罪行为，进而对企业甚至国家构成安全风险。**比如用来模仿 CEO 的声音，并说服一位高管将数十万美元汇到一个诈骗账户。

深度造假也可用于传播虚假信息，以影响公众舆论或掩盖真相。往小了说，这会对个人声誉和形象构成侵犯，比如2021年底，国内一段以“搞钱万能论”为主题的视频在网络上疯狂传播。乍一看，这段言论竟出自是新东方教育科技集团董事长俞敏洪。但随后俞敏洪就通过其个人社交帐号发布了辟谣视频，他表示搞钱视频里的话没有一句是自己说的。而随后也证实这段视频是通过语音合成技术生成。

![](https://image.3001.net/images/20230308/1678262472_640840c85af90b0f7034b.jpg!small)

往大了说，深度造假可用于冒充国家领导人并引发国家冲突。据ASI数据科学公司曾经做过的一项测试，通过音频生成算法，只需要借助两小时的语料并训练五天时间，就可以模拟出一份以假乱真的特朗普向俄罗斯宣战的语音。

在其他情况下，**深度造假可以实现似是而非的否认，大众可以通过声称它们是深度造假来否认所有媒体来源，从而造成对社会信任的严重破坏。**

## 如何检测深度造假

### 初级检测方法

初级检测方法依赖于 ML 模型，这些模型经过训练可以识别通过深度伪造生成的伪影或像素化。人眼可能无法察觉这些伪影，但在真实图像和深度伪造图像上训练的模型能够对其进行检测。

### 高级检测方法

高级检测方法使用可以识别语义上有意义特征的模型，包括不自然的动作，如眨眼、头部姿势或独特的举止，以及音素-语音的不匹配。

虽然这些检测方法目前被认为是准确的，但随着深度造假技术的改进以及复杂度的加深，预计这些检测效果将会有所折扣，需要更新和改进。

除了这些技术之外，大众都可以通过验证自己收到的音视频来源，以帮助检测深度造假。

> 参考来源：[From Disinformation to Deep Fakes: How Threat Actors Manipulate Reality](https://thehackernews.com/2023/03/from-disinformation-to-deep-fakes-how.html)

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

什么是深度造假？

深度造假举例

* 换脸
* 口型同步
* 音频

深度造假的网络风险

如何检测深度造假

* 初级检测方法
* 高级检测方法

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