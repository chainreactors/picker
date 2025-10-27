---
title: 这个超火的黑客小工具，可以通过WiFi解锁特斯拉
url: https://www.freebuf.com/news/393813.html
source: FreeBuf网络安全行业门户
date: 2024-03-09
fetch_date: 2025-10-04T12:10:34.316856
---

# 这个超火的黑客小工具，可以通过WiFi解锁特斯拉

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

这个超火的黑客小工具，可以通过WiFi解锁特斯拉

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

这个超火的黑客小工具，可以通过WiFi解锁特斯拉

2024-03-08 13:21:16

所属地 上海

据BleepingComputer消息，一种利用 Flipper Zero 设备进行的简单钓鱼攻击可能导致特斯拉账户被篡改，甚至能让汽车被解锁并启动。该攻击适用于版本为 4.30.6 和 11.1 2024.2.7的特斯拉应用程序。![](https://image.3001.net/images/20240308/1709875398_65eaa0c646dc06529b984.png!small)

安全研究人员塔拉勒哈吉巴克里（Talal Haj Bakry） 和汤米米斯克（Tommy Mysk） 向特斯拉报告了他们的发现，指出将汽车与新手机关联缺乏适当的身份验证安全性。

研究指出，攻击者可以部署一个名为“Tesla Guest”的 WiFi 网络，这是特斯拉服务中心经常出现的 SSID名称，非常具有迷惑性。接着，使用 Flipper Zero 广播 WiFi 网络，一旦受害者连接到伪造的网络，他们将收到一个虚假的特斯拉登录页面，要求使用他们的特斯拉账户凭据登录。无论受害者在钓鱼页面上输入什么，攻击者都可以实时在 Flipper Zero 上看到。

![](https://image.3001.net/images/20240308/1709875468_65eaa10c27789cfb872ed.png!small)网络钓鱼过程

输入特斯拉账户凭据后，钓鱼页面会要求输入账户的一次性密码，以帮助攻击者绕过双因素身份验证保护。攻击者必须在一次性密码过期之前行动，并使用窃取的凭据登录特斯拉应用程序。一旦进入账户，攻击者可以实时跟踪车辆的位置。

此外，通过访问受害者的特斯拉账户，攻击者可以添加一个新的“手机钥匙”。这一操作可在离车辆几米远的地方实现。米斯克表示，通过应用程序添加新的电话钥匙不需要解锁汽车或将智能手机放在车内，这造成了很大的安全漏洞。

![](https://image.3001.net/images/20240308/1709875522_65eaa1423ba05ca65ebd7.png!small)添加新的电话密钥

更糟糕的是，一旦添加了新手机钥匙，特斯拉车主不会通过应用程序收到关于此事的通知，车辆的触摸屏也不会显示警报。而有了新手机钥匙，攻击者可以解锁车辆并激活所有系统，甚至能够驾驶车辆离开，就好像他们是车主一样。

米斯克指出，该攻击在特斯拉 Model 3 上试验成功。在向特斯拉的报告中，他们指出，被劫持的特斯拉账户必须属于主要驾驶员，并且车辆必须已经关联了手机钥匙。

他们认为，应当在添加新手机钥匙时要求使用物理特斯拉卡片钥匙，为新手机添加认证层来提高安全性。

“我能够在新 iPhone 上添加第二个手机钥匙，而特斯拉应用程序并没有提示我使用钥匙卡来对新 iPhone 上的会话进行认证。我只是用我的用户名和密码登录了新 iPhone，一旦我授权应用程序访问位置服务，它就激活了手机钥匙，”二人在向特斯拉的报告中写道。

BleepingComputer 已与特斯拉联系，就上述问题进行了询问，以及他们是否计划发布 OTA 更新，引入安全措施以防止这些攻击，但尚未收到回复。

**参考来源：**

> [Flipper Zero WiFi phishing attack can unlock and steal Tesla cars](https://www.bleepingcomputer.com/news/security/flipper-zero-wifi-phishing-attack-can-unlock-and-steal-tesla-cars/#google_vignette)

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