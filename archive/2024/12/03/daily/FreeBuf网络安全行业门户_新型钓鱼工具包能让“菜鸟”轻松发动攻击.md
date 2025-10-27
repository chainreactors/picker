---
title: 新型钓鱼工具包能让“菜鸟”轻松发动攻击
url: https://www.freebuf.com/news/416616.html
source: FreeBuf网络安全行业门户
date: 2024-12-03
fetch_date: 2025-10-06T19:39:23.335397
---

# 新型钓鱼工具包能让“菜鸟”轻松发动攻击

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

新型钓鱼工具包能让“菜鸟”轻松发动攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型钓鱼工具包能让“菜鸟”轻松发动攻击

2024-12-02 11:18:40

所属地 上海

据The Hacker News消息，研究人员近日发出警告，称一种恶意电子邮件活动正利用名为 Rockstar 2FA 的网络钓鱼即服务（PhaaS）工具包窃取 Microsoft 365 用户帐户凭证。

![](https://image.3001.net/images/20241202/1733109695_674d27bfcbce0a33907d7.png!small)

Trustwave 研究人员 Diana Solomon 和 John Kevin Adriano 表示，该恶意活动采用了 AitM 中间对手攻击，允许攻击者拦截用户凭证和会话 cookie，意味着即使启用了多因素身份验证 （MFA） 的用户仍然容易受到攻击。

Rockstar 2FA 被认为是 DadSec（又名 Phoenix）网络钓鱼工具包的更新版本，通过 ICQ、Telegram 和 Mail.ru 等服务以订阅模式进行广告宣传，价格为期两周 200 美元（或每月 350 美元），能够让没有技术专长的网络犯罪分子大规模开展攻击活动。

根据Rockstar 2FA的推广介绍，其工具包功能包括双因素身份验证 （2FA） 绕过、2FA cookie 收集、反机器人保护、模仿流行服务的登录页面主题、完全无法检测 （FUD） 链接和 Telegram 机器人集成，并且还声称拥有一个 "更直观、用户友好的管理面板"，使客户能够跟踪其网络钓鱼活动的状态、生成 URL 和附件，甚至个性化应用于所创建链接的主题。

Trustwave 发现的钓鱼邮件活动利用了不同的初始访问媒介，例如 URL、二维码和文档附件，除了使用合法的链接重定向器（例如，缩短的 URL、开放重定向、URL 保护服务或 URL 重写服务）作为绕过反垃圾邮件检测的机制外，该工具包还集成了使用 Cloudflare Turnstile 的反机器人检查，以试图阻止对 AitM 网络钓鱼页面的自动分析。

Trustwave 还观察到该工具包利用 Atlassian Confluence、Google Docs Viewer、LiveAgent 以及 Microsoft OneDrive、OneNote 和 Dynamics 365 Customer Voice 等合法服务来托管钓鱼链接。

与此同时，安全公司，Malwarebytes 披露了一个名为 Beluga 的网络钓鱼活动，该活动使用.HTM附件来欺骗收件人在虚假登录表单上输入 Microsoft OneDrive 凭证，然后将这些数据泄露给 Telegram 机器人。而该活动的推广传播渠道利用了社交媒体上的网络钓鱼链接和在线网络博彩游戏广告。

**参考来源：**

> [Phishing-as-a-Service "Rockstar 2FA" Targets Microsoft 365 Users with AiTM Attacks](https://thehackernews.com/2024/11/phishing-as-service-rockstar-2fa.html)

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