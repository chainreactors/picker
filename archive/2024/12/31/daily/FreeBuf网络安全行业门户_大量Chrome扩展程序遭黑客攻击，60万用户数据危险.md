---
title: 大量Chrome扩展程序遭黑客攻击，60万用户数据危险
url: https://www.freebuf.com/news/418743.html
source: FreeBuf网络安全行业门户
date: 2024-12-31
fetch_date: 2025-10-06T19:40:50.545997
---

# 大量Chrome扩展程序遭黑客攻击，60万用户数据危险

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

大量Chrome扩展程序遭黑客攻击，60万用户数据危险

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

大量Chrome扩展程序遭黑客攻击，60万用户数据危险

2024-12-30 11:11:53

所属地 上海

一场新的攻击活动针对知名的Chrome浏览器扩展程序，导致至少16个扩展程序被入侵，超过60万用户面临数据泄露和凭证被盗的风险。

此次攻击通过钓鱼活动针对Chrome Web Store上的浏览器扩展程序发布者，并利用其访问权限在合法扩展程序中插入恶意代码，以窃取用户的Cookie和访问令牌。

![](https://image.3001.net/images/20241230/1735528425_67720fe9e7c7f707e18c9.png!small)

已知首个被曝光的企业是网络安全公司Cyberhaven。12月27日，Cyberhaven披露称，威胁行为者入侵了其浏览器扩展程序，并注入了恶意代码，与位于域名cyberhavenext[.]pro的外部命令与控制（C&C）服务器通信，下载额外的配置文件并窃取用户数据。

专注于浏览器扩展安全的LayerX Security公司CEO Or Eshed表示：“浏览器扩展是网络安全的软肋。尽管我们倾向于认为浏览器扩展是无害的，但实际上，它们通常被授予访问敏感用户信息的广泛权限，例如Cookie、访问令牌、身份信息等。”

Eshed补充道：“许多组织甚至不知道他们的终端上安装了哪些扩展程序，也不清楚其暴露的程度。”

在Cyberhaven被入侵的消息曝光后，其他同样被入侵并与同一C&C服务器通信的扩展程序也迅速被识别出来。SaaS安全公司Nudge Security的CTO Jamie Blasco发现了其他解析到与Cyberhaven入侵事件中使用的C&C服务器相同IP地址的域名。

目前怀疑被入侵的其他浏览器扩展程序包括：

> AI Assistant - ChatGPT and Gemini for Chrome
> Bard AI Chat Extension
> GPT 4 Summary with OpenAI
> Search Copilot AI Assistant for Chrome
> TinaMInd AI Assistant
> Wayin AI
> VPNCity
> Internxt VPN
> Vindoz Flex Video Recorder
> VidHelper Video Downloader
> Bookmark Favicon Changer
> Castorus
> Uvoice
> Reader Mode
> Parrot Talks
> Primus

这些被入侵的扩展程序表明，Cyberhaven并非孤立的目标，而是一场针对合法浏览器扩展程序的大规模攻击活动的一部分。

![](https://image.3001.net/images/20241230/1735528499_67721033befb3842f8b07.png!small)

对Cyberhaven被入侵事件的分析显示，恶意代码主要针对Facebook账户的身份数据和访问令牌，特别是Facebook商业账户。

Cyberhaven表示，恶意版本的浏览器扩展程序在上线约24小时后被移除。其他一些被曝光的扩展程序也已更新或从Chrome Web Store中移除。

然而，Or Eshed指出，扩展程序从Chrome商店中移除并不意味着风险已经结束。“只要被入侵的扩展程序版本仍在终端上运行，黑客仍然可以访问并窃取数据。”

安全研究人员正在继续寻找其他被曝光的扩展程序，但此次攻击活动的复杂性和范围已使许多组织更加重视保护其浏览器扩展程序的安全性。

参考来源：<https://thehackernews.com/2024/12/16-chrome-extensions-hacked-exposing.html>

# 数据安全

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