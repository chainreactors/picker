---
title: 被同事问了一下午等保，我把答案都整理出来了
url: https://mp.weixin.qq.com/s/aPDCa4hBT4mUNAM-YR9qDw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:04:01.597998
---

# 被同事问了一下午等保，我把答案都整理出来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Vibx6YRY7WRSyQW0EjVM1xRD4PY4N5E7pH1ax7uh5T5nklmFskp4Aia9iczM45CrIdKibyWImzRo90SvQNEvXicBrQ0eOzMfOnQeO4gWPnyF9OAQ/0?wx_fmt=jpeg)

# 被同事问了一下午等保，我把答案都整理出来了

原创

瓜瓜虾
瓜瓜虾

透明魔方

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

前几天，我正在客户现场忙着一个项目经理要做的沟通。

一个配合客户做等保的同事：“方便腾讯会议吗？我有好几个等保整改的问题咨询？”

我正忙着“淡定”地处理各个干系人的“威逼利诱”，于是说文字吧，我得空了就回复。其实我也存了一个小心思，因为我好久没做等保咨询，有些新的和数据相关的要求，我不一定知晓，也需要查查资料消化一下。

这些小问题，我感觉对大家可能有帮助，就分享出来。

问题一：应用系统未采用两种或两种以上组合的鉴别技术。

同事：“我们这个应用平台登录口，有图形识别+账户名密码登录，这个难度不算两种身份鉴别吗? ”

我：“不算，一般来说手机验证码、身份验证App的动态码、指纹/人脸等生物识别、U盾等都是可以的。”

同事：“应用系统的我就加个手机验证码好了，那数据库和服务器的双因素验证又怎么做呢？我去下载一个开源软件实现可以吗？”

我：“ 开源软件没有销售许可证和网专许可证，因为违反了安全建设管理要求，又成为一条高风险项，可以限制服务器/数据库登录地址，仅通过堡垒机远程管理，然后堡垒机启用双因素，或者把服务器/数据库远程登录关掉，只能本机访问，通过这种方式降风险。”

同事：“ 服务器防病毒软件，有没有不花钱的方法？”

我：“火绒，360都是免费的，可以用。”

同事：“还有一堆，你看看？“

她给我截了几张图，例如：

![](https://mmbiz.qpic.cn/mmbiz_png/Vibx6YRY7WRQDXF9MfAXSDKEYOU7hKvstzVTm4onWn3iaeREZ73GueqoyVQ306cd3K2uicI8iaNh4MR65AcgGlv6WfMSAGUibxRzuZ34VsrgNnDk/640?wx_fmt=png&from=appmsg)

我看了下，基本就是传输+存储要加密。

我：“我看就是系统用https，TLS1.3版本以上，关闭弱加密套件。数据库开启ssl，加密传输的问题就解决了。存储加密，目前有很多免费加密算法可以用，推荐 **AES-256、SM4（国密）** 等算法，不建议MD5之类的加密算法。”

同事：“太谢谢了，我感觉能处理了。”

等保已经是常规动作，很多看似难解决的问题，换个思路——比如用堡垒机统一管控、用白名单缩小暴露面——就能降低风险。这些常规动作可以直接列成一个清单，方便后续调用。当然，每个系统环境不同，具体方案可以直接和测评机构沟通确认。

THE END

希望进大群交流的朋友，关注本号后，加微备注：进大群。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnltCm5ZvL07Mm4DwTUefYEPXR7QRNQxXvc9xPEOz18ws0djQpfmVIQq9Js0TcSKH8tu1g1AyWMibBw/0?wx_fmt=png)

透明魔方

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/U6oY6Hu3lnltCm5ZvL07Mm4DwTUefYEPXR7QRNQxXvc9xPEOz18ws0djQpfmVIQq9Js0TcSKH8tu1g1AyWMibBw/0?wx_fmt=png)

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