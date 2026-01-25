---
title: 记某edusrc小程序挖掘案例
url: https://mp.weixin.qq.com/s/qVnZOQnN72Y_ME5t-aRe_A
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:52:03.144639
---

# 记某edusrc小程序挖掘案例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uMqu3mwJukabItiazMwPbRudGmheXRNS9gPlC8xibc8D2aDaYpibPOTsjQ/0?wx_fmt=jpeg)

# 记某edusrc小程序挖掘案例

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

漏洞挖掘

```
找一些没人挖掘的中学，水点rank。。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uqNlzLDSictgibEAtcxCcrQh9OI4LRibB4VFAZVb8KuTxg9BrpkPL7pAicg/640?wx_fmt=png&from=appmsg)

点击小程序可以看到这个页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uibcKkom0H4F6dBAVYd4m03GtCMFw0zFCZNiavxfC7p49XEWggvHwctDA/640?wx_fmt=png&from=appmsg)

可以使用三种身份进行登录，点击访客登录进行抓包（前两种会跳转到账号密码登录）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2ur8ec1SmO7y3T2s8ibvgtUCHz0HCiaYSGiaBLullXew9xf8fAl7EShkySQ/640?wx_fmt=png&from=appmsg)

放行第一个数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2u7EaJWhdcGwLGs7vFu9sjiaQ1syazTDoU3OsWic00WqWGicXFicJHyqT9Hw/640?wx_fmt=png&from=appmsg)

看到这个使用手机号一键登录，点击允许，抓取数据包，并且进行拦截

前置知识:

微信小程序官方提供了一套微信快捷登录的登录逻辑，用户授权手机号快捷登录时，会将本地的手机号使用sessionkey和iv进行aes加密，后端解密后返回该手机号的登录凭证。当sessionkey发生泄露时，攻击者便可以伪造手机号登录任意手机号。

通过数据包请求可以看到泄露了，伪造任意用户登录需要的三要素

sessionkey,encryptedata,iv值。如果这里没有泄露sessionkey可以多看几个数据包，有可能别的数据包，会返回。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uxgmKic5LoOZfJQkT1jTwFUBm6TNERw5vjX6y9ticgoSgjs0a6KfBLf3w/640?wx_fmt=png&from=appmsg)

打开工具伪造编码后的数据（没工具的可以看文章结尾）

将三个值放到对应的位置，先点击解密，可以看到现在我们允许的是，192这个进行登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2ufrc0ibEGR9bIyh6PgWsvmEojBsWcfUrJdLicAMSlpbDvALNL6dnIkLzA/640?wx_fmt=png&from=appmsg)

我们这里我们把手机号进行替换为任意用户的手机号

这里我换成我的另一个手机号131这个，替换之后点击进行加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uWEGVLUUt3VNNpK6YrUdazWYktWRrFoZCks140A3enF8VZL9icfJszLA/640?wx_fmt=png&from=appmsg)

复制加密后的内容encryptedata来到bp里面进行替换，然后放包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2ujlMcVuZfNp5ib7zOlbQHP7Tapwc7jicOmTe4ob7Bv172xicc7l2su4asg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uoPibbyn3MjdOT56ZupqH3XjUicO8neMwSyxEiajvopVV0tkAPOzFgicRNw/640?wx_fmt=png&from=appmsg)

可以看到后面全是131这个手机号发起的请求,直接关闭拦截，放行所有数据包

之后可以看到这个访客记录页面，还有别的页面，没截图就不贴图了，通过这个可以实现一个任意用户访客登录的效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uAA2ZcPbRsWDaOvCWMpzmf2GHLmt8qxUcUgRicOTNZhJEbhaTrfRqLiaw/640?wx_fmt=png&from=appmsg)

案例2

通过定点信息收集来到这个小程序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uV0AnJjiciciahZmhLViaFvHeOH3VRDj3LSuUptJQ8GCOIXzhlW0CKicJicNQ/640?wx_fmt=png&from=appmsg)

点击小程序进行登录，把功能都点击一下，让所有数据都过bp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uV5T9GExIa9jopacMJoHDlVvpDGDbZ1YCQYIRpz8fcoXMKSl92aZokg/640?wx_fmt=png&from=appmsg)

看历史数据包，发现有一个数据包泄露了很多用户的openid以及id信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2uOjxLicfr70HjmDefanicGGqa7N5FCGLw9vU6Gz4d4vuRuibc5VCWOamxQ/640?wx_fmt=png&from=appmsg)

继续观察数据包，发现有一个可以查看用户密码的数据包是通过id进行鉴权的，利用上一步获取的id,或者直接遍历id可以查看系统内所有用户的用户名密码等信息。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO51NIogUB2ty30hwLuQKJ2usTM9zsdFIdDLrYdKWDQLQ5yqjia6tAxVEMPpichV3lTuibcK5nXIeAgYg/640?wx_fmt=png&from=appmsg)

后台回复加群加入交流群

后台回复sessionkey获取工具

有思路需要的师傅可以加入小圈子

主要内容是（2025-2026/edusrc实战报告）

其他内容懂得都懂，持续更新中

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/f7yXib8mBCO7ap4PoUrDa3un6nHVcSDAV25rGkkJ8qOPAooDwASNSaiaGJibu3z2mOqnD2vCnOQB6ia3AfuuOZ0ZDg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

陌笙不太懂安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f7yXib8mBCO4n1wSEsRXe9I7EjtXDn7f7PcEQBD0X8ly0heoXcFtjhDqXg5kHxicuwfL8iaT0nVFGEaibvK3Gib0Ovw/0?wx_fmt=png)

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