---
title: GitHub项目评论被用来传播Lumma Stealer恶意软件
url: https://www.freebuf.com/news/409987.html
source: FreeBuf网络安全行业门户
date: 2024-09-03
fetch_date: 2025-10-06T18:24:34.800826
---

# GitHub项目评论被用来传播Lumma Stealer恶意软件

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

GitHub项目评论被用来传播Lumma Stealer恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

GitHub项目评论被用来传播Lumma Stealer恶意软件

2024-09-02 11:12:39

所属地 上海

据BleepingComputer消息，GitHub  teloxide rust 库的一位贡献者发现，GitHub项目中的评论以提供修复程序为幌子，实际在其中植入了Lumma Stealer 恶意软件。

BleepingComputer 进一步审查发现， GitHub 上的各种项目中有数千条类似的评论，这些评论都为用户的提问提供了虚假的修复程序。

以下图为例，该评论告诉用户从 mediafire.com 或通过 bit.ly URL 下载受密码保护的压缩包，然后运行其中的可执行文件。 逆向工程师告诉 BleepingComputer，仅在 3 天时间里就有超过2.9万条推送该恶意软件的评论。

![](https://image.3001.net/images/20240902/1725255326_66d54e9e0bd2f502b11e9.png!small)传播Lumma Stealer 恶意软件的评论回复

![](https://image.3001.net/images/20240902/1725255429_66d54f05934acdcbc792f.png!small)含有 Lumma Stealer的安装程序

单击该链接会将用户带到一个名为“fix.zip”的文件下载页面，其中包含一些 DLL 文件和一个名为 x86\_64-w64-ranlib.exe 的可执行文件。通过在 Any.Run分析发现，这是一个Lumma Stealer 信息窃取恶意软件。

Lumma Stealer 是一种高级信息窃取程序，能够从 Google Chrome、Microsoft Edge、Mozilla Firefox 和其他 Chromium 浏览器中窃取 cookie、凭证、密码、信用卡和浏览历史记录。此外，它还能窃取加密货币钱包、私钥和名称为 seed.txt、pass.txt、ledger.txt、trezor.txt、metamask.txt、bitcoin.txt、单词、wallet.txt、\*.txt 和 \*.pdf 等名称的文本文件。这些数据被收集并发送回给攻击者，攻击者可以使用这些信息进行进一步的攻击或在网络犯罪市场上出售。

虽然 GitHub的工作人员会在检测到这些评论时进行删除，但已经有受害者在Reddit上进行了反馈。

就在最近，Check Point Research 披露了名为Stargazer Goblin 的攻击者进行的类似活动，他们通过在Github上创建3000多个虚假账户传播恶意软件。目前尚不清楚这两起事件是否由同一攻击者所为。

**参考来源：**

> [GitHub comments abused to push password stealing malware masked as fixes](https://www.bleepingcomputer.com/news/security/github-comments-abused-to-push-password-stealing-malware-masked-as-fixes/)

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