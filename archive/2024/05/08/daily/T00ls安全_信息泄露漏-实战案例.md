---
title: 信息泄露漏-实战案例
url: https://mp.weixin.qq.com/s?__biz=Mzg3NzYzODU5NQ==&mid=2247484623&idx=1&sn=7a70759d47d43421d28a818719cc8e81&chksm=cf1ea263f8692b75fed9fda2cbda32f4cd93c2a64319f9e822991d1a6ae22946d0087e3d6872&scene=58&subscene=0#rd
source: T00ls安全
date: 2024-05-08
fetch_date: 2025-10-06T17:17:16.270537
---

# 信息泄露漏-实战案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicL3wxmicMN2d7IUn9FfSibHrAW177R9QCgraQgM0vKHIez86qXuQYe15w/0?wx_fmt=jpeg)

# 信息泄露漏-实战案例

原创

YinYi

T00ls安全

## 第一个案例

收集资产时得到一个知识库管理平台，本着学习下大公司的企业文化和企业精神就深入了解一下。通过目录爆破扫到了管理员登录界面，密码爆破了一下，没有弱口令。但是看到页面上有个管理员手册，下载下来好好看看里面内容是啥，让咱也看看如何当好一个管理员。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicyDe2SeINFSOU4icV1l88ZL8ZbcbKLFGNWxiahwbicrpuwz8XBsLMb072Q/640?wx_fmt=png&from=appmsg)

打开之后几十页的手册，发现有一页管理员新建用户功能，其中看到了17个用户，能看到的信息登录账户名、登录姓名、登录者邮箱。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicUUBNBVjFtxqZzzibuePyTdhibVQ5QtgPE3iaZMBIbOictibia0BXzlMruictQ/640?wx_fmt=png&from=appmsg)

根据看到的用户名构造了账户密码，尝试登录了一下，很幸运的进入了后台。但是进入后台后，里面没有内容，无法看到企业文化和企业精神。如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicAXTOjepla6ysysvia896qZpXANP4Aic8bh6icYSSZzT3hPQicu8iauVmiaow/640?wx_fmt=png&from=appmsg)

转战到前台，但是前台是双因子认证，需要绕过一下。登录后台后可以修改账户手机号，那就将手机号修改成我的吧。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicdmELA7YPesIG4C8RWKoBhVH7rzxfb1noOIUSd6GSQq4E867asfL7ZA/640?wx_fmt=png&from=appmsg)

修改手机号后，接收到验证码。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicAiaIW9guZDqAuXlib2a0bycicNYyhBMVyCFEicecwqxEztA8OnO0NEa2mQ/640?wx_fmt=png&from=appmsg)

绕过验证码后，登录前台后，看到了运维文件夹。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSic8espIQ0I0nJzU7ic5Ua2t7FpXB6NMzDAzSF6o45hAcLyuHevVoA8QlA/640?wx_fmt=png&from=appmsg)

运维文件夹中，对方很大方的分享了内网的账户密码、网络架构，感谢大哥。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicbYV2bjE80lk2srGiaicqxcDia950uKJXkf0UooNvicK4FNEHy1ykciaUDRQ/640?wx_fmt=png&from=appmsg)

但是全是内网的东西，又不想扫描，尝试下VPN是否开放，找到了VPN登录网址，不好的是使用了SoftEther，根据之前收集到的账户密码尝试使用密码登录后，登录成功如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicZRI3cICy6s9z27GI3B7R0q3iaPujl4hibaOt4AiaIoeq9TIcjzibK7hTGQ/640?wx_fmt=png&from=appmsg)

## 第二个案例

第一天将此漏洞交上去后，对方也是果断，关闭了VPN，关闭了知识库平台，我也没法继续学习了。

第二天还想进内网看看人家的东西，恰好对方还有个自研的APP，那看看人家的APP吧。登录界面有一个功能是输入首字母后会自动输出此字母相关的登录账户，就这样我认识了他们集团的所有人。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicd8OibbO89LTofibRIuTpsrN1JY7icdNd9XqLk1kf5GPJNDn8Egyic4dthg/640?wx_fmt=png&from=appmsg)

收集到账户后，密码没弱口令，APP无法登录。又看到有个Exchange，通过收集到的账户进行了爆破。得到了几千个邮箱账户。对方也是很大方，网络架构、内网账户密码、安全设备口令等。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicatjicqTF9Yk3Fzk8e8FPgVmT4mUPwicAVRiaufcHXN1AkgeOnibrHP1H2A/640?wx_fmt=png&from=appmsg)

邮箱密码拿到了尝试使用邮箱密码登录APP，挺好，邮箱密码就是APP登录密码。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSichUHYPhgRIiajJJ4IW0IdV86ibTasric4YXjWmtTLhoHPhrwINfTulqQSQ/640?wx_fmt=png&from=appmsg)

本着进内网的心，VPN验证码是通过APP接收的，挺好得来全不费功夫。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicZVZINzsI8Xo6s5vHrXiboY6En5RegxQ5PZklJBXnr4ZfpDkzoiaibhGow/640?wx_fmt=png&from=appmsg)

登录到内网后，根据邮箱里获得的内容，登录到内网机器。

![](https://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nN73yVYGkDJP0o6GwZLueSicnmPhOTeddjt1CHiapoohLypfZTScvE3pkWAwoSZ0KlicUaWOnkF8yq2g/640?wx_fmt=png&from=appmsg)

#

## 原文地址

> https://www.t00ls.com/articles-71577.html

预览时标签不可点

个人观点，仅供参考

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nOAjMAKC6icupJMRh71NoyhUB3efic74ESDrBtMlicTvhR5rAJAbiaXxPahyUibJnpbHibNUhtkK5PCUzFQ/0?wx_fmt=png)

T00ls安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xkB4mPD62nOAjMAKC6icupJMRh71NoyhUB3efic74ESDrBtMlicTvhR5rAJAbiaXxPahyUibJnpbHibNUhtkK5PCUzFQ/0?wx_fmt=png)

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