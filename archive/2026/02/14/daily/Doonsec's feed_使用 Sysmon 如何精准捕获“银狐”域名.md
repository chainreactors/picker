---
title: 使用 Sysmon 如何精准捕获“银狐”域名
url: https://mp.weixin.qq.com/s/kMX3dYkrvg1dZVGgvi1Efg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:44.104948
---

# 使用 Sysmon 如何精准捕获“银狐”域名

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/H6RmIowwbs4KDyHN6rgC3wcZd6ibeeaDhzgpC7icfMXc4kqgUN5ToEuBMzGicsfwzjjgIfcqDSedMQU6UW9TtWravicuKfFoPe6cJdRHqqOsxPk/0?wx_fmt=jpeg)

# 使用 Sysmon 如何精准捕获“银狐”域名

原创

weiqin
weiqin

大仙安全说

![]()

在小说阅读器中沉浸阅读

点击蓝字，关注我们

关

注

![](https://mmbiz.qpic.cn/mmbiz_png/oZN2pbzJKdWUK3Ne8uSjJibGEKUc8s8FbE3ibZ4mjQicF2gDe1DTSIqmWKU5YsEtQgKubRf5IySO9NkDcr1valibkw/640?wx_fmt=png)

免责声明

大仙安全说的技术文章仅供参考，此文所提供的信息只为网络安全人员进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他! ! !

**场景**：某一天，风和日丽的下午，客户说服务器请求了银狐恶意域名（shunfeng168.vip）客户要求你来处理一下这个病毒 。

![](https://mmecoa.qpic.cn/mmecoa_png/41rzoAia9zheaqOiavPK2XqnRNVnwlNq77H0XW8EFHCnRjTraricDOlK3vqUoT38nCX0EciaTKKLUEma36onLiaZbTQ/640?wx_fmt=png)

**01**

**Sysmon项目介绍**

Sysmon由Sysinternals开发，同时具有windows版和linux版。Sysmon作为强大轻便的监视和记录工具，可以记录系统的各种活动。通过收集系统上发现的事件，可以了解到恶意程序在操作系统上进行了哪些操作。可选择记录网络连接，包括每个连接的源进程、IP 地址、端口号、主机名和端口名。记录注册表和文件的操作记录。

**02**

**windows安装Sysmon**

以管理员身份安装
sysmon64.exe -i   #安装Sysmon

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs60b3SqeiaSJmU7wcWj8rTTdnCric1Em4eO98qrRJ9Eja2WKYicB10BaE0LAknHd3aryBia3DhTj7Y437wQCR6tUjbyZCiabgETPvGU/640?wx_fmt=png)

sysmon64.exe -c sysmonconfig-export.xml

#安装自定义配置文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5Y3fvxzIwY0UFzHS2kzANIXXjPXajMdgDxlrsnFddokJNkgJ8Cd3dY2p3M0ojxcbSIL3PyicBm470D6icyezTeduPjjaHBoYwGU/640?wx_fmt=png)

打开计算机管理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs7uHTNydsicb8nuDiass0UYwjKxfhOZHKHBdS5z4JaxxfMjMl8QFYjJdiaicjwicBxdqaCR4FXsJHSpia9PPic7FhBe4aEiadWvOpViaMLU/640?wx_fmt=png)

如果能看到Sysmon则安装成功

事件查看器->应用程序和服务日志->Microsoft->Windows->Sysmon->Operational

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs4CLfeIMObRHpsXicibCENGESMfic9qgZYMkpj9kmtWewicic6kXJ0PhlCA6AXRibZxyibGNmaSnyCwxQ3tlAM8vfwYicqcuwHtQJTmibKI/640?wx_fmt=png)

**03**

**应急流程**

***一：微步查域名***

确实是恶意的银狐域名

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs4Z83v9Yq8XheJjmIuWibwF5CqXXThTcibFe3mGAiaHdkgtFxFSrekx8JribT20tfGTicwUgxMAdTic4I0ztwO5rhUX1r2TiaC8AIRLGw/640?wx_fmt=png)

***二：排查具体原因***

需要利用sysmon，在Operational里新建id为22的视图

#参考微软官方文档：Event ID 22: DNSEvent (DNS query) DNS查询

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs6mObOQlspYaEvzC7uhhyoib4pVFbEY3D3L8RIpkY3NaS5SPnvGkVzCibibppqwAQsjnJTEP7IWfHBBicYLJIOCuLKu1IkbfAQL1T0/640?wx_fmt=png)

搜索 shunfeng168.vip，发现多个事件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5Q1FxS4jvs3U9iaTophPibvDHgVpq4iaicyePYw4iaWVVNGHZiamKIyMqjXG8UE5PrK1mv9PUcR5qhfibVZ1jypdRXqB4DxCjncYYjNI/640?wx_fmt=png)

显示的目录都为sihost.exe文件

C:\Windows\System32\sihost.exe

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs7YXNYFko2yyqslmqzvdTAUHnbzehSNmeU81VFnGic6Q2tVnZgP4ic5Y6G8z6gcw3l7T2BldJxGUzSU7ja5icl6sicv1TMA3WC3A0U/640?wx_fmt=png)

sihost.exe这个文件是系统核心组件。这是使用了进程注入的手法，劫持一个正在运行的、受信任的进程，**更容易绕过传统杀毒软件的进程监控。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs66Kumhek7KJ2NNSic9mNGEh7JX6HVeMnuSq8ibibBiagq8eCgibLJN7rWTsHyThhrzAbnqrCpYA6qMBCG1DTmdIjZroL1mThRCajy0/640?wx_fmt=png)

tvpview同样也可以看到，二者都可以发现；要点击解析地址这个功能，可以切换显示域名和IP地址。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5PVnmjPoDpkIeGAX2Z7d9mbV3mTCHhWP3tnlkS9ibgZBmErIG9N6yD73Y7WONx39SAgRaHO7gLrkktIPbovaFLC9oWbJycMQJo/640?wx_fmt=png&from=appmsg)

需要按照上一篇文章的host文件配置，不然无法看到银狐域名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/H6RmIowwbs5hOAg7btvblSEl7MKRiavMtKHUafqFMCdDwp7fZ14UzJFQfrZ3iaJ3WqOko5FmXbjz7lDBaeDozprzkh4MzEJnJAlyjE0oWsQCQ/640?wx_fmt=png)

在浏览器的下载历史中发现了谷歌的安装包，经过分析和验证确认为盗版谷歌引起的。

***三：处置方式***

断开sihost.exe进程，删除掉恶意程序释放的文件并删除盗版软件，重新启动服务器。持续观察是否还有访问银狐域名请求，告诫客户选择从正规渠道下载软件。

**04**

**总结**

有的时候sysmon记录不到一些用了绕过手法的事件（可以自行查阅资料），比如上一篇的主角就是无法在sysmon中查到，所以工具结合分析的用最为稳妥。大部分情况下还是要把工具带全，结合分析更佳。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0FR0MLn8jepbllc2psMbAnk0SA9ibNCnd3Picpv1ibAIicNv0ibt9azaRxN5ibCMXC8xyjQeUDpXrMjgGjQ/640?wx_fmt=png)

c3lzbW9u5LiL6L2977yaaHR0cHM6Ly9sZWFybi5taWNyb3NvZnQuY29tL3poLWNuL3N5c2ludGVybmFscy9kb3dubG9hZHMvc3lzbW9u77yM6YWN572u5paH5Lu25LiL6L2977yaaHR0cHM6Ly9naXRodWIuY29tL1N3aWZ0T25TZWN1cml0eS9zeXNtb24tY29uZmln

解密即可获取微软官方下载地址、配置文件。

感谢关注大仙安全说

![](https://mmbiz.qpic.cn/mmbiz_png/H6RmIowwbs6QGLveqYHoRunY5Emiac8zKKPAia5g9hFt7lqXNuXR8kV6A3u6iasg5WnVWu55ZT8Qnh4wxstubCeE6LwCcpUnuRiaiagiaqy7MHic3k/640?wx_fmt=png)

**添加好友注明来意**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0Eghr41R49Dsaibt7QQtMcrDaRXfz1W7bnr1Ajjd8ia3xhsylXhcJcze1tic4XKZcrn5LFSm3rTicZBhg/640?wx_fmt=png)

**公众号丨大仙安全说**

**VX丨weiqin\_6666**

**长按关注**

《往期阅读》

[整个网安圈子，谁还没用过TCPView](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484768&idx=1&sn=11cbfa0c873858dc079fa27dce967ce4&scene=21#wechat_redirect)

[整个网安圈子，谁还没用过Procmon](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484724&idx=1&sn=0e6aa9c5cf1eeca183f2152105301dfd&scene=21#wechat_redirect)

[整个网安圈子，谁还没用过PCHunter](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484686&idx=1&sn=451c8505a7ecdcdcf772f7d54a04a55b&scene=21#wechat_redirect)

[整个网安圈子，谁还没用过Autoruns](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484649&idx=1&sn=325e00a2b72cacf0d6657568775bd1d4&scene=21#wechat_redirect)

[使用 DNSQuerySniffer 揪出隐蔽钓鱼请求](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247484778&idx=1&sn=277c154e55ac14a63430109329b0b2c2&scene=21#wechat_redirect)

相关话题：

#网络安全#黑客#大仙安全说#网安圈子#应急响应#Sysmon#TCPVIEW#应急工具

![](https://mmbiz.qpic.cn/mmbiz_gif/y00icvcPjkfYXic35ml9MJkg41yEDAQhzc0iapH6CWjEX1NA3nKbfZutZD03lYTDD8xvsicziaB94zOohn2jEhFQnNg/640?wx_fmt=gif)

**分享、在看与点赞，至少我要拥有一个吧**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/afo75o4gacpFHp4O7KXstEGdnGtCnk9v1azmwLFNoS3XPibDA2mw0MKuDbLj96h4eNIdOKXRicDicTn4PiciagBpZWQ/0?wx_fmt=png)

大仙安全说

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/afo75o4gacpFHp4O7KXstEGdnGtCnk9v1azmwLFNoS3XPibDA2mw0MKuDbLj96h4eNIdOKXRicDicTn4PiciagBpZWQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过