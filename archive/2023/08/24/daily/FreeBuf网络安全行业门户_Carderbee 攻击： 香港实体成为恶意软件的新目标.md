---
title: Carderbee 攻击： 香港实体成为恶意软件的新目标
url: https://www.freebuf.com/news/375853.html
source: FreeBuf网络安全行业门户
date: 2023-08-24
fetch_date: 2025-10-04T12:01:35.422463
---

# Carderbee 攻击： 香港实体成为恶意软件的新目标

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

Carderbee 攻击： 香港实体成为恶意软件的新目标

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Carderbee 攻击： 香港实体成为恶意软件的新目标

2023-08-23 11:24:49

所属地 上海

The Hacker News 网站披露，此前从未被记录的威胁组织正在针对香港和亚洲其它地区的实体组织，展开攻击活动，赛门铁克威胁猎人网络安全小组正在以昆虫为主题的“Carderbee”绰号追踪这一活动。![1692761159_64e57c478f022b01624df.png!small](https://image.3001.net/images/20230823/1692761159_64e57c478f022b01624df.png!small)

赛门铁克安全人员指出此次攻击活动利用一个名为 EsafeNet Cobra DocGuard Client 的合法软件的木马版本，在受害者网络上传播一个名为 PlugX（又名 Korplug）的已知后门，在与 The Hacker News 共享的一份报告中，安全人员还指出在攻击过程中，攻击者使用了带有合法微软证书签名的恶意软件。

ESET 在其今年发布的季度威胁报告中着重强调了使用 Cobra DocGuard 客户端实施供应链攻击的黑客活动，还详细描述了 2022 年 9 月香港一家未命名的博彩公司因该软件推送的恶意更新，遭到黑客入侵。

值得一提的是，尽管 Cobra DocGuard 客户端应用程序被安装在大约 2000 个端点上，但据说受 Cobra DocGuard 影响的组织中只有多达 100 台计算机受到了感染，这表明攻击的重点范围可能有所缩小了。

Syamtec 指出恶意软件被发送到受感染计算机上的以下位置：csidl\_system\_drive\program files\esafenet\Cobra DocGuard client\update’，表明涉及 Cobra DocGuard 的供应链攻击或恶意配置是攻击者破坏受影响计算机的方式。

在其中一个攻击实例中，上述描述的情况充当了部署下载器的渠道，该下载器具有来自微软的数字签名证书，随后被用于从远程服务器检索和安装 PlugX，这种模块化植入为攻击者在受感染平台上提供了一个秘密后门，使其可以继续安装其它有效载荷、执行命令、捕获击键、枚举文件和跟踪运行进程等。这些发现揭示了威胁攻击者继续使用微软签名的恶意软件进行攻击后活动并绕过安全保护。

尽管如此，关于 Carderbee 的许多细节仍未披露，目前尚不清楚 Carderbee 的总部位于何处，它的最终目标是什么，以及它是否与 Lucky Mouse 有任何联系。

赛门铁克强调针对香港等地的攻击活动背后的攻击者是极具耐心且技术娴熟的网络攻击者，他们利用供应链攻击和签名恶意软件来开展活动，试图保持低调。此外，这些攻击者似乎只在少数获得访问权限的计算机上部署了有效载荷，这也表明幕后攻击者进行过一定程度的策划和侦察。

**文章来源：**

> https://thehackernews.com/2023/08/carderbee-attacks-hong-kong.html

# 恶意软件

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