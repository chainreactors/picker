---
title: 第111篇：Weblogic 8.x早期版本后台部署war包获取shell方法与坑点总结
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247487281&idx=1&sn=199e1ba750cd7b4364b7b30e07eda2da&chksm=c25fc04af528495cbad89a83cbc1dff6291f3b50a8241e594dd8ecfee261a08ceff7cdbe6f7c&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-12-30
fetch_date: 2025-10-06T19:36:47.666048
---

# 第111篇：Weblogic 8.x早期版本后台部署war包获取shell方法与坑点总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450B2HehrDWP8FxhmYITpOVVqo34HicuGNc9jTLLaljVuGRKGqBg8mTJJFAHwPzyULeypSIJX8skal6g/0?wx_fmt=jpeg)

# 第111篇：Weblogic 8.x早期版本后台部署war包获取shell方法与坑点总结

原创

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

## **Part1 前言**

**大家好，我是ABC\_123**。过去几年，在内网中多次遇到weblogic 8.x，与10.x及后续版本相比，早期版本的weblogic后台获取shell的过程会比较复杂。首先，webshell的编写需要兼容JDK 1.4，这就排除了大多数现代的webshell。另外，IE浏览器也需要进行一系列配置，否则许多weblogic后台功能无法正常使用。今天ABC\_123重新搭建了环境进行测试，并将复现过程记录下来，与大家分享，以备后续参考。

**注：**以下文章中对于IE6.0的配置，同样适用于内网环境中所见的很多老旧系统。

## **Part2 技术研究过程**

* ## **配置IE6.0访问weblogic8.x后台**

首先需要设置一下IE浏览器，建议选择IE6.0，安全级别调整为低，并将ActiveX控件和插件设置下的各种单选项都设置为“启用”，最后点击“重置”按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqYicGgeGbJc3VuN2u7x61MucJKNIUAAgh7LEFMQJ57VOpI90MF3ztiaRw/640?wx_fmt=png&from=appmsg)

在“受信任的站点”下，填写weblogic的url地址，添加至“可信站点”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqU4ibXp89mQJRMOadw51IxLTTRR8betYIevMBUmqWoEbRE7IORwW1OOQ/640?wx_fmt=png&from=appmsg)

输入账号密码weblogic:weblogic123进行登录。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqUlVsIUPBe2VAUBH8fsCgu9cyVJ5xiauzicrtic8Ohia0vblFUg52qg9ghA/640?wx_fmt=png&from=appmsg)

登录后，weblogic后台的左侧一列会显示错误，并且提示“您的Java版本已过期”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqtV53zciaWGFAfibzf9p4vaCfIDjaXiboibEg332CDNLtkniaIicicXOFcibsLw/640?wx_fmt=png&from=appmsg)

点击“稍后”按钮之后，会出现如下提示：

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVq5V2ZXuJzEAjPuuE3stUxBibm77tyeHfWNCqdbTWDg4swP4vAibMklMqA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqmkm5TmibSuJ4ViaDprr9XD9kia6bo7Q3TKm3oiaNr7DwYnZWZ7FLCiceNbA/640?wx_fmt=png&from=appmsg)

打开“控制面板”的Java功能选项，点开java控制面板。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqlnSa1gHpXaP88olrKmDADjXbfaDUnCpfHwsLnwuwNnibkmX8PsQoJicA/640?wx_fmt=png&from=appmsg)

在“安全”选项卡下，点击“编辑站点列表”，在“例外站点”列表下，添加weblogic的url http://192.168.237.235:5150/，然后一路点击“确认”按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqnaWaGndChejateybOqjniaq2icI5EafT7s9FMyibPwwPFNY0hXHR0kOcQ/640?wx_fmt=png&from=appmsg)

然后刷新当期页面，重新点击一下左侧报错的页面，会弹出一个“安全警告”，点击“运行”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqm1nBOGkY3ZY8l14dooUS1lf8FJ7grbXzRPlbBTMJickkg6M2jMZiceFQ/640?wx_fmt=png&from=appmsg)

随后，weblogic的后台页面终于可以正常显示了。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqtmb5qoofnYTquGlmThqqfegCntcad7doibJVCFFyiaxT8OSVx6fTRoSw/640?wx_fmt=png&from=appmsg)

* ## **制作war包（兼容weblogic8.及jdk1.4）**

Weblogic8.x后台所用的war包是有校验的，不符合要求的会直接报错，随便将webshell文件打一个压缩包，改扩展名为.war是不可行的。如下图所示，**weblogic8.x是在jdk1.4下运行的，现在所用的大多数jsp文件都会直接提示错误**，因为其代码所使用的一些类和方法并不支持jdk1.4。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqXCvcNKJhE4mP17viaiaeb9Jw9MSzOaYjpRpY7vtgicbyt0O3xxfVqmw1w/640?wx_fmt=png&from=appmsg)

如下所示，提示缺少WEB-INF/web.xml文件。经过一系列测试，发现web.xml文件也需要专门制作，随便写一些内容是不行的。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqvPKfYibDohruLtjPYgtJO8s83GYWzmmsDLYykAw3PGiaGCD2dmYYBEbw/640?wx_fmt=png&from=appmsg)

经过测试，如下的写法是简单的而且可以通用于weblogic8.x、weblogic9.x版本。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqlKicSjXPPw64X2nWFvB4V2H2ucbhqA8pXLRBIQO7KICowFTrq6RsM7Q/640?wx_fmt=png&from=appmsg)

最终制作好的war包内容如下，在war包文件中，我加入了一大堆的jsp shell，便于我们挨个测试哪些webshell可以兼容weblogic8.x。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqhIic5oRjPy7HlksbqjnibbwxhHZicyLRUY2Urx7rayfxicxOIxQMfKsUBw/640?wx_fmt=png&from=appmsg)

* ## **后台部署war包**

登录后台之后，点击“部署”选项下的“Web应用程序模块”，点击“部署新的Web应用程序模块”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqk3N5gEBOyIHqIUXPRojzuGwyKxfwAU7Jfzq3w4iaYaOrRlvpTxCGiaeQ/640?wx_fmt=png&from=appmsg)

继续点击“上传文件”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqfIApL7JXEGP6eSS0esyQGSO33cXibfMibmLo4iaicgjhbWqBlCHnA0YTIg/640?wx_fmt=png&from=appmsg)

点击“浏览”，选择制作好的包含jsp版webshell的war包，点击“上传”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqy1ibLJ1vLcyeWk8DsRgYZHGPzzfwLkQkfg9QF78ra08Qa0w2icGLdricA/640?wx_fmt=png&from=appmsg)

然后继续选择war包文件，点击“目标模块”。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqggoTY4zm3xJ5bia9n83LIq98mwlmJrhklwSzCpicTw7753cdS7svjCnA/640?wx_fmt=png&from=appmsg)

继续点击“部署”按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVq59tpmIsp5lTwNicKCjWqOdgRvqkRNxBo0ic7H5NOQLjJwwlBYHXniaibvw/640?wx_fmt=png&from=appmsg)

如下所示，提示“成功”，说明war包部署成功。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqr557tpTSvsyLxAL8hplWveW8VVVK97ticn7gbGOeKegxXDW1lt4DvQw/640?wx_fmt=png&from=appmsg)

继续点击“测试”标签页，提供了webshell的访问地址。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqaCiaxByJrVGvshZRE10ibLf1YvkdKA7A7bKWEl8JxpepUibmM88GO86eA/640?wx_fmt=png&from=appmsg)

在上述URL地址上，拼接JSP版webshell的文件名，即可获取webshell。经过一系列措施，发现如下几个webshell是可用的，冰蝎、哥斯拉、蚁剑、菜刀等等通通不兼容。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqHicDeJRVmtqzoFHeEmVsJlVX8o9nMF0HkLia6AaWQ9eQzQTbDYzAOpibQ/640?wx_fmt=png&from=appmsg)

如下图所示，此webshell是2004年老外写的，适用于jdk1.3，已经是20年前的了。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450B2HehrDWP8FxhmYITpOVVqwfBsIHFcriavsmHQa8l1rs6FrTmziczRMBq7fvU1dNM45Hj8LLnanic0w/640?wx_fmt=png&from=appmsg)

**Part3 总结**

**1.**  后续会继续分享weblogic中间件的其它利用技巧，敬请期待。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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