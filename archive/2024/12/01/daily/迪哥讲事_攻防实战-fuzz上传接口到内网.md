---
title: 攻防实战-fuzz上传接口到内网
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496445&idx=1&sn=5dada7b97b53d2949eda0c804ef64b96&chksm=e8a5f89edfd2718828d52c74571359a10b3b4a74044ff194b39cec0e541ed79844fe69002fed&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-01
fetch_date: 2025-10-06T19:37:16.372231
---

# 攻防实战-fuzz上传接口到内网

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj74lib6SOpTTUKXDrFo8Vo1tkeu8ULQ3RJic6qfTjg0gXWn78s5jo1Etcia8cO844P6bVibErCicCK8EoQ/0?wx_fmt=jpeg)

# 攻防实战-fuzz上传接口到内网

迪哥讲事

以下文章来源于极梦C
，作者遥遥

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7ibXfF3wU9jhIeVd3L2HDyG1MyTnp71XQy2X9BOCO3rjg/0)

**极梦C**
.

只专注于实战的实战派。

前言

不更新就是在hwww

不是星标不推送文章了。

师傅也不想吧~

快把极梦C设置成星标吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSlPCA2vI3xOYHWBzrD7soYIHtwq9sBxicB1jiaWzHhjVOSsaEMDiaSBx2OF3FdLXibIPTaox8TvhtyNow/640?wx_fmt=png&from=appmsg&wxfrom=13)

‍

信息收集

对目标进行系统收集，发现只有一个官网。

页面有几个可以跳转的，

官网->xxx系统->根据xxx系统title找到另一个ip

这里的功能点都不全，不过他可以跳转。找到了ip 1.1.1.1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSnFFU7dskBWk5AdEtoOj1nnY73nWicoyKmqG7EU42wmibjIPXSt5zYGPsrBComROB40Uju4N4duzx1Q/640?wx_fmt=png&from=appmsg)

打点

通过对1.1.1.1进行ip端口扫描。发现了一个访问是iis默认页面的端口。1111

http://1.1.1.1:1111

一般对这种页面都比较喜欢，进行目录扫描。

发现存在一个test页面

http://1.1.1.1:1111/test/jmc/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSnFFU7dskBWk5AdEtoOj1nnvZdFibH9MOZ6m0pACYgib5KU4kYgubicNe7Sr0t0icdp4ErRicHlrXas30w/640?wx_fmt=png&from=appmsg)

直接全局搜索upload,看了几个都是404

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSnFFU7dskBWk5AdEtoOj1nnFLjeN2yk9R9vjlvWj14QVzkffqVwELI9dJhTX6BibKYHKg7IdcGibgrg/640?wx_fmt=png&from=appmsg)

虽然是404.但是有基本的路径了。这里想着是不是可以fuzz一下目录。

是否存在可以访问的目录。

当前页面是test.然后拼接,

找到了一个可以访问的路径。

http://1.1.1.1:1111/test/api/upload/uploadfiles/

尝试上传。这里好玩的事情是，无法上传jpg,txt.这里没截图。

上传的时候，直接显示禁止上传。很蒙蔽。

可能一般到这里就结束了。

但是思路了一下，是否这里只能可执行文件文件。

直接上aspx，发现可以成功上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSnFFU7dskBWk5AdEtoOj1nnhXXg6OgERydZwgM7UIysI3kxsvicxgZtXMNibuexWkdOmHh5LkpZuia9w/640?wx_fmt=png&from=appmsg)

确实返回路径了，但是明眼一下看出来

这是一个filepath=xxx是一个下载的url

直接访问确实是下载。

http://1.1.1.1:1111/xxx/file/filepath=E://test/aaa/2024/xxx.aspx

接下来就是找路径的时刻。

看到有test。

直接和上述的上传接口进行拼接，

http://1.1.1.1:1111/test/api/upload/uploadfiles/--发现还是404。

嘶难顶。

继续fuzz，这里主要是找带有aaa路径的地址。

最后在再开始这个页面下面找到了一个带有aaa的路径，然后拼接成功shell。http://1.1.1.1:1111/xxx/aaa/2024/xxx.aspx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSnFFU7dskBWk5AdEtoOj1nnx6O9iaIuJCy6sHblmgyUvJ2yOXaibWZcCriaBJficTmtzhmIGy0PniaZmBA/640?wx_fmt=png&from=appmsg)

内网

内网某服edr，低权限，本想直接fsacn一把梭，但是无法运行，不知道为啥。只能提权，提权使用了PrinterNotifyPotato 进行内存提权。

然后添加账号，或者激活gues。然后远程登录。直接梭哈。

采用hash传递，口令碰撞，上百台服务器。其余都是老样子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PZCtvaaOQSnFFU7dskBWk5AdEtoOj1nnq7cYmo5Ty6q2Rve49aaTDhfA3EycibUUChjQcxaibb9EBXBmfDKuvCZA/640?wx_fmt=png&from=appmsg)

下机。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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