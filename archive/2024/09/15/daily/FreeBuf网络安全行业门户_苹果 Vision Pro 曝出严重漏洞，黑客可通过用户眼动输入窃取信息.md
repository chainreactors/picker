---
title: 苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息
url: https://www.freebuf.com/news/411003.html
source: FreeBuf网络安全行业门户
date: 2024-09-15
fetch_date: 2025-10-06T18:26:04.316825
---

# 苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息

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

苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息

2024-09-14 10:17:43

所属地 上海

![1726280346_66e4f29a570afc47a52cc.png!small](https://image.3001.net/images/20240914/1726280346_66e4f29a570afc47a52cc.png!small)

近日，苹果公司的 Vision Pro 混合现实头戴式设备曝出一个安全漏洞，一旦被黑客成功利用，他们就可以推断出用户在该设备的虚拟键盘上输入的具体数据。

该攻击活动名为 GAZEploit，该漏洞被追踪为 CVE-2024-40865。

佛罗里达大学的学者对此表示：这是一种新颖的攻击，因为攻击者可以从头像图片中推断出与眼睛有关的生物特征，从而重建通过注视控制输入的文本。GAZEploit攻击利用了用户共享虚拟化身时凝视控制文本输入的固有漏洞。

在该漏洞披露后，苹果公司在 2024 年 7 月 29 日发布的 visionOS 1.3 中解决了这一问题。据苹果描述，该漏洞影响了一个名为 “Presence ”的组件。

该公司在一份安全公告中说：虚拟键盘的输入可能是从 Persona 中推断出来的，其主要通过 “在虚拟键盘激活时暂停 Persona ”来解决这个问题。

研究人员发现，黑客可以通过分析虚拟化身的眼球运动或 “凝视”来确定佩戴该设备的用户在虚拟键盘上输入的内容，极易导致用户的隐私泄露。

假设黑客可以分析通过视频通话、在线会议应用程序或直播平台共享的虚拟化身，并远程执行按键推断，那么他们就可以利用这一点提取用户键入的密码等敏感信息。

攻击主要是通过对 Persona 记录、眼球长宽比（EAR）和眼球注视估计进行训练的监督学习模型来完成的，以区分打字会话和其他 VR 相关活动（如观看电影或玩游戏）。虚拟键盘上的注视方向会被映射到特定的按键上，以便确定潜在的击键方式，同时还考虑到键盘在虚拟空间中的位置。

研究人员表示：通过远程捕捉和分析虚拟化身视频，攻击者可以重建用户键入的按键。目前，GAZEploit 是该领域首个已知利用泄露的注视信息远程执行按键推断的攻击方式。

> 参考来源：[Apple Vision Pro Vulnerability Exposed Virtual Keyboard Inputs to Attackers](https://thehackernews.com/2024/09/apple-vision-pro-vulnerability-exposed.html)

# 安全漏洞 # 苹果漏洞

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