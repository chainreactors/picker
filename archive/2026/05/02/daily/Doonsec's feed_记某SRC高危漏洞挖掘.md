---
title: 记某SRC高危漏洞挖掘
url: https://mp.weixin.qq.com/s/1saHZ_Bt_8z5qojaJ7qJFg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:26:54.800867
---

# 记某SRC高危漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6Osr0qsqyIC2ABicB8dAq3ThkU0MBulQ0jlVRJEMstljoPRMIUWv9Sic4z3MPZhUibdD9iaavhwrtVQeYFU2UOZn2AwibaUZBGLCObU/0?wx_fmt=jpeg)

# 记某SRC高危漏洞挖掘

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于Tide安全团队
，作者oh1inge

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7f2r4cHKV0tKOK4v87qvAYZazjibgqC5HkYyaQeibGau4g/0)

**Tide安全团队**
.

Tide安全团队以信安技术研究为目标，致力于分享高质量原创文章、开源安全工具、交流安全技术，研究方向覆盖网络攻防、Web安全、移动终端、安全开发、物联网/工控安全/AI安全等多个领域，对安全感兴趣的小伙伴可以关注我们。

无聊的时候打开了某SRC，发现了新增资产，于是立即开启了本次的漏洞挖掘之路。

## 从开局一个登录框到通用漏洞挖掘

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdVepqsRbeWlA8u7eGOh1VIYxGibicA8JU1iaLzYNsicWyQxyIDSOs57t6S9iaGwVbh1jNg1qyX4ibiciaSEdycXX2aSvwBmwp1GSzlI118/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

一般针对这种登录框的挖掘思路就是提取js文件的接口进行Fuzz测试，看是否存在未授权访问导致的信息泄露漏洞，以及是否有重置密码的接口、SQL注入、账号密码泄露、用户名枚举、弱口令等，这里我几乎跑了所有的js接口，并没看到什么爆红的数据包，但

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdW4Ijoo0TyWsqu76IWRhrkQC32knuBI0yTLQZPiaIA4ibju6OcdDPLlJ4DhiajEGdiaYZzNt3olLbTuib5bDVYPp8KChBJfBJhqaDlA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

心里一喜，是否只要我得到userId值传进去，就可以getuserinfo得到用户敏感数据了？？当时还在想会不会泄露账户密码等信息，js里并未泄露该userid参数，我尝试了11111111 尝试了1 admin 等等 均未成功，于是我决定换个思路，查一下该系统互联网的相同资产。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdV4X93M3cEvJhKw6nypsZpIyLSqAQcVay1V7GA2CAxl2QbXln9ayEXhZvU5jjUDLmqLEib6X79K2xPJTYzhLSBZj2skqfb7p6bg/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

好嘛 这么多资产，我找个存在未授权或者弱口令的进去横向挖掘通用漏洞，或者看是否能够收集到该系统的备份源码进行代码审计，再不济收集到userId岂不美哉？ 此处省略横向打点过程，最终摸到了一个弱口令的系统，进去查看发现存在userid为xxxxxxxxxxxxxxxxxxxxx 很长一段。 发现再次请求该接口只能得到如下信息

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdUzNxNZ0Kbc03xd19dfDiaeP0e71BwOZVW8YWGibzYp4wTIVlOIwdTcybdkEZH8zSe2DtMiaibTOKJ4JWSx1I3OTKxsNGXN30AA1B4/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

还是不够啊，于是我就对互联网那个存在弱口令的资产开始漏洞挖掘，后台某个功能点请求了一个新的js文件，这里我们称它为abcdindex.js 就是该js文件泄露了大量的路由接口拿来拼接测试，果不其然，

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdUFwCbILV8DIWfQPhep3nGwMcrmWg3dKrWWOZjwCp32iavNqC7LibLz8U80vnib0T4CuzVVZj33vC2uXdzicrk1GoUe5aD1kqgNA7M/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

发现该系统其实有多个子系统功能模块，每个mulu.json都给出了对应系统的API接口也就是BaseUrl和后台接口。拼接遍历，成功取得通用型未授权访问漏洞，某个接口泄露了大量的视频摄像头权限。贴一张厚码的图（大概几百多个摄像头调度权限）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdWI0MqRPo59Mvb6brWf1g8TP1hOIn9siaGvAArfqXCCGL0R90ADHGRoUvCcia3m3zhKwMrRFWLyM2ibVgILaiblK4FbT4TTAR7kmZY/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

提交该漏洞也是成功斩获高危

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdWFOpLFYK5gfRIeRBksnIpsY19LfzYA5VfJez5nhJiaa2adFFOXd6x4UZBQDzcq4saGvDClS2QG4Z11kBMmrDCfa6KibhOImibNME/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

发现了那么多的隐藏接口，该漏洞肯定不能到此为止，于是继续开始挖掘。

## 逻辑缺陷导致鉴权缺失

发现很多接口功能点均提示缺少userId  这种归为A类， A类的接口还需要提供数据库存在的用户id和绑定的租户Id即可实现越权查看该用户信息，但还有一些接口提示鉴权缺失，该接口这里称为B类，但发现只需讲数据包的B的Authorization: Bearer认证头删除即会提示A类的问题，只需添加也可绕过，所以这里对提取到的后台目录进行访问这里直接访问 如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdVtG4hcuHibyAspum6m2sg3xsQZOE0RQmmRpZs5Zja2e4LQAvjrcPEGZIiaD6op0hB93OibM4FOuFYvTsMibQeXytichHJeBP3fqAFU/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

空白页面，这里使用bp抓包对每一个后端交互的数据包进行认证头删除

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdUhfNP2ltSXsiazibgtq0fjYkniaLSKcnAyyjj7icJHJDW7qQDIlzd0Szmu9EhGjjArTrDkib8q4a72MwmWroKuR5FlribxtA5Sara0U/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

？？？？？？？不是你？

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdUiaviaxoWStwYpzDoDPSicnYpmDrrorGZg0gJRlaNqDKXOfMKvZhgHszPjibyRnkicVDvPuAaVqdgwIyUUA9UemJ5zzVlTfW3YSswM/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

这么烂的系统没有权限就能难道本菜鸡吗，我拿前面收集到的用户ID 身份ID 进行参数FUZZ遍历 成功得到数据，舒服了。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jS2mB7OlsdXJf6jicsBib5KibDxu95IIJaf7GNRvIcBBdrlGpTySrCicfxv4JdsnQEoVuZHHDelichicOyRL7deRZlW6AbMoJO1moj18aSu36EEOQ/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

其实还有很多人员管理等功能模块全部存在缺陷，也是成功绕过拿到该系统的后台管理员权限。斩获高危漏洞，这里根据日志泄露的用户名其实还发现了弱口令用户等多个漏洞，但还未来得及提交，项目就已经进行了关闭。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdWkHIhB1DU9u4DgntdZyR0w2aKvNnGk2gcia9Fr4RF6krKAl2VxUdOR0MF9iaUx7bjCh8yjGzOeicznZiaYBD3jDZJRJSgibZAkb7ew/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13)

这两个漏洞相信有耐心的师傅其实都可以挖的到，本文仅是做个记录分享，但实际挖掘过程中需要去寻找的参数还是很多的，而且登录的默认管理用户名比较复杂，也是通过信息收集找了一波操作手册，像一般的SRC资产肯定都被大佬们挖掘的差不多了，几乎不会存在JS接口提取未授权的漏洞产生，但有时转变下思路，去打通杀，再根据0day漏洞或隐藏的文件接口针对性的对原始目标开展攻击，也许会发现到别人挖不到的漏洞，撕开不一样的口子。

文章来源：Tide安全团队

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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