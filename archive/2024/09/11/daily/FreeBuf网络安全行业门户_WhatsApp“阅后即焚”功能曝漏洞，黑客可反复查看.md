---
title: WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看
url: https://www.freebuf.com/news/410675.html
source: FreeBuf网络安全行业门户
date: 2024-09-11
fetch_date: 2025-10-06T18:28:36.332864
---

# WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看

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

WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

WhatsApp“阅后即焚”功能曝漏洞，黑客可反复查看

2024-09-10 16:42:44

所属地 上海

据BleepingComputer消息，全球拥有20亿用户的即时通讯工具 WhatsApp最近修复了一个十分重要的隐私漏洞，该漏洞能允许攻击者多次查看用户发送的“阅后即焚”（View once）内容。

![](https://image.3001.net/images/20240910/1725957799_66e006a735509ede922f0.png!small)

WhatsApp的“阅后即焚”于3年前推出，允许用户发送只能浏览一次的照片、视频和语音消息，且接收者无法转发、分享、复制或截取消息。

但这其中有一个Bug，Zengo X 研究团队发现，“阅后即焚” 功能可用于向收件人的所有设备发送加密媒体消息，包括桌面端，即使这些消息在桌面端无法显示。 这些消息与普通消息几乎完全相同，但包含一个指向 WhatsApp 网络服务器（"blob store"）托管的加密数据 URL 以及解密密钥。

研究人员称，这些消息在下载后不会立即从 WhatsApp 的服务器中删除，且某些版本的“阅后即焚 ”消息还包含无需下载即可查看的低质量预览。

此外，“阅后即焚 ”消息与常规消息类似，但带有一个“View once”值为“true”的标记，攻击者仅需将“true“改为” false“，就可绕过此隐私功能 ，下载、转发和共享这些“阅后即焚 ”消息。

Zengo X 据称是第一个向 WhatsApp母公司Meta 详细报告这一漏洞的组织，但在此之前该漏洞可能至少 已经暴露了1年。BleepingComputer甚至已观察到两款谷歌浏览器插件（其中一个已于 2023 年发布）能够便捷地实现反复查看并共享“阅后即焚 ”消息。

目前Meta已表示对漏洞进行了修复，但这背后所反映出的更深层次问题也引发了人们的忧虑，即这些科技巨头所谓的为用户着想的隐私措施可能仅仅是个”空壳“，其本质上仍然漏洞百出。

**参考来源：**

> [Meta fixes easily bypassed WhatsApp ‘View Once’ privacy feature](https://www.bleepingcomputer.com/news/security/meta-fixes-easily-bypassed-whatsapp-view-once-privacy-feature/)

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