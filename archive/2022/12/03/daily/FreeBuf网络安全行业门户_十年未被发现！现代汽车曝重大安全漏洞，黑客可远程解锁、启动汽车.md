---
title: 十年未被发现！现代汽车曝重大安全漏洞，黑客可远程解锁、启动汽车
url: https://www.freebuf.com/news/351422.html
source: FreeBuf网络安全行业门户
date: 2022-12-03
fetch_date: 2025-10-04T00:24:22.000726
---

# 十年未被发现！现代汽车曝重大安全漏洞，黑客可远程解锁、启动汽车

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

十年未被发现！现代汽车曝重大安全漏洞，黑客可远程解锁、启动汽车

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

十年未被发现！现代汽车曝重大安全漏洞，黑客可远程解锁、启动汽车

2022-12-02 15:01:09

所属地 上海

据cybernews消息，现代汽车APP存在一个重大安全漏洞。利用这个漏洞，黑客可以****远程解锁、启动汽车****。更令业界感到惊讶的是，这个漏洞已经****存在了10年之久****，影响了****自2012年生产的现代汽车，以及旗下高端品牌捷尼赛思汽车。但现代汽车发布公告称，该漏洞并未被广泛利用。****![](https://image.3001.net/images/20221202/1669964358_6389a2464d0aa4c77d92a.jpg!small)

这两个APP的名称是MyHyundai 和 MyGenesis，允许经过身份验证的用户启动、停止、锁定和解锁他们的车辆，可进一步提升车主的使用体验。![](https://image.3001.net/images/20221202/1669964369_6389a25163474c1f7747a.jpg!small)

根据网络安全研究人员Sam Curry的说法，原本现代和捷尼赛思汽车的APP仅向授权用户提供车辆的控制权限，但是，该APP与授权服务器的通信之间存在一个严重的安全漏洞，导致攻击者可以轻易取得相应的权限。

Sam Curry在社交平台发文称，“我们注意到服务器不要求用户确认他们的电子邮件地址，此外还有一个非常松散的正则表达式，允许在您的电子邮件中使用控制字符。”![](https://image.3001.net/images/20221202/1669964429_6389a28deba9394b46e99.png!small)

在深入研究绕过身份验证的可能方法后，Sam Curry和他的团队发现，在注册过程中，只需要在现有受害者电子邮件的末尾添加CRLF字符，攻击者就可以使用现有的电子邮件注册一个新帐户。

而这个新帐户将获得一个JSON网络令牌 (JWT)，该令牌与服务器中的合法电子邮件相匹配，从而授予攻击者对目标车辆的访问权限。

Sam Curry发布消息称，“我们目前在确认，是否可以使用被篡改的 JWT 执行解锁或启动汽车等实际操作，如果真的可以做到这一点，那么将有可能全面接管所有远程启动的现代汽车和捷尼赛思汽车。![](https://image.3001.net/images/20221202/1669964454_6389a2a65c287cefd6867.png!small)

随后，有安全研究人员利用他们手里的一辆现代汽车来测试该漏洞。最终结果显示，使用受害者的电子邮件地址并添加 CRLF 字符，就可以让他们远程解锁链接了相应电子邮件地址的车辆。

有消息称，某些黑客团队也盯上了这个漏洞，甚至开发了一个python 脚本，只需要获取受害者的电子邮件地址，即可执行车辆上的所有命令，甚至接管车主的帐户。

目前，该漏洞已经报告给现代汽车公司，并且已经得到修复。在发布的公告中，现代汽车表示，经过调查后并未发现该漏洞被黑客利用了。

现代声称该公司调查了这个问题，并没有发现该漏洞在野外被利用，并强调利用该漏洞条件苛刻，“需要知道与特定现代汽车帐户和车辆相关的电子邮件地址，以及研究人员使用的特定网络脚本。”

而这似乎与目前不少安全人员发布的内容不太相符。

Yuga Labs公司的分析师称，只需要知道目标车辆识别号 (VIN)，就有可能向端点发送伪造的 HTTP 请求，从而顺利利用该漏洞。

在实际情况中，车辆VIN 很容易在停放的汽车上获取，通常在仪表板与挡风玻璃相接的板上可见，攻击者可以轻松访问它。这些识别号码也可以在专门的汽车销售网站上找到，供潜在买家查看车辆的历史记录。

近年来，智能汽车产业正处于快速发展期，越来越多的安全专家们也开始将研究重点放在汽车攻击领域，发现了不少重量级汽车网络安全漏洞，包括远程解锁、启动、停止车辆等，成功向外界展示，攻击者是如何破坏车辆中的各种组件，涉及多个主流汽车品牌。

也正因为如此，汽车厂商们应进一步加大对网络安全的重视程度，并真切投入资源改善这种不安去的状况。汽车作为一个私密、封闭的个人空间，其安全性的重要性毋庸置疑，也是车主们选择汽车的重要衡量因素。

> 参考来源：https://cybernews.com/news/hyundai-bug-allows-unlocking-car-remotely/

# 安全漏洞 # 汽车安全

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