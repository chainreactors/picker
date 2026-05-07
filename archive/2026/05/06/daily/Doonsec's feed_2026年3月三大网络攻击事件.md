---
title: 2026年3月三大网络攻击事件
url: https://mp.weixin.qq.com/s/AtApT5TYctY64JUZhQTK_g
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:30:57.927712
---

# 2026年3月三大网络攻击事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0LGiaGIrzXuk13Qef6lg0oNZUWMgicaqLq5B4ZPiaFVZutIdEgAByYAg21GuiaUWicxEBx8rVlO8GyKcLqrcAplVdmibftiayq44soM5MHBhS8ficcQ/0?wx_fmt=jpeg)

# 2026年3月三大网络攻击事件

TtTeam

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于威胁情报Z分析
，作者Z

![](http://wx.qlogo.cn/mmhead/j8cooK2zCqoqY1ibzIuH0db0U6NFgdx4PahHyU6OOprunMrA5RzXbibpMcUA18kVOibjEK1IK7HQ28/0)

**威胁情报Z分析**
.

国际网络安全威胁情报，地缘政治事件分析。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXunnbbcAMaZM04ictLchAICLV1rFPp5fTJ1DkNwbmHHFUHJ2tic0wLyd8F9jRbbCyvtFbUC9IHGRxvCU6guVHiatxLUiblsL2av5ZY8/640?wx_fmt=png&from=appmsg)

2026 年 3 月，针对用户和组织的网络威胁激增，从劫持银行应用程序窃取个人数据，到利用受信任的域名进行网络钓鱼重定向。

网络犯罪分子使用了越来越狡猾和危险的手段。以下是对本月三起最引人注目的网络攻击事件的详细介绍。

## **1. 通过 Telegram 针对安卓用户的虚假银行应用程序**

一款复杂的恶意软件投放器被发现模仿 IndusInd 银行应用程序，以网络钓鱼的方式攻击 Android 用户，旨在窃取敏感的财务信息。

一旦安装，该恶意应用程序会显示一个虚假的银行界面，诱骗用户输入关键信息，例如手机号码、Aadhaar 卡号、PAN 卡号和网上银行凭证。

受害者提交数据后，数据会被发送到钓鱼服务器和 Telegram 控制的命令与控制 (C2) 通道。

该APK文件本身包含base.apk（核心恶意载荷），并拥有安装其他应用的权限。该投放器还经过混淆处理，并使用密钥（“npmanager”）进行XOR加密，以隐藏其代码和行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXumMJmJs0rmJWNlm1VHaIzZDuLTKnvFNBvg8IHUyNwUM5mvoklLyNGxFialZRMbD1KOicCZ86X4YCUoulDqwFXW6eic9toNTPbyVLU/640?wx_fmt=png&from=appmsg)

在沙箱环境中，让我们探索一下虚假银行应用程序的实际界面，并追踪攻击是如何展开的。

通过跟踪流程树和网络连接，您可以观察到用户是如何被诱骗提交其凭据的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXukZEUIF8pHtKpjnIBTk9zm9hQCuPP4QVhia9UuYuGtC89k8oP27CSiaXEwy49GvoWzNeIPHkVII00k8I7SwS1rlXicNphngiaMtAfg/640?wx_fmt=png&from=appmsg)

网络活动还揭示了被盗数据是如何被发送到钓鱼网站，然后转发到 Telegram 控制的命令服务器的。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXun67TURCC18OmOClTw5dC00GKnzwGiaah9TZQo6WyGZsSvJbMPC4YD1eibUib0baSrpWGTVU1tD92479drV38tLSfKC1LLmf7UKFE/640?wx_fmt=png&from=appmsg)

这种攻击凸显了移动威胁增长之快。一名被入侵的员工就可能打开通往敏感数据、内部系统乃至财务账户的大门，使整个企业面临风险。

因此，对于企业而言，提前防范这些威胁至关重要。在可疑应用程序造成问题之前，为其配备合适的工具进行检查，远比事后应对全面入侵要容易得多，也安全得多。

## **2. 受信任的网站被利用进行恶意重定向**

在 ANY.RUN 研究人员 3 月份揭露的另一起攻击活动中，攻击者滥用长期受信任域名上的重定向功能，将用户重定向到钓鱼页面。

其中一个域名早在 1996 年就已注册，被防病毒工具标记为安全，因此用户没有任何理由怀疑存在任何问题。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXulfoiaYfjIKicGjvExmbJu1fWSPALnTM41d6QZgFceWa2TlicWZ1ELmOGQwMlKODSEhqR6VuoAXwVTKXoMHGroXNaxIiatQ6YJKu8o/640?wx_fmt=png&from=appmsg)

在本次 ANY.RUN 沙箱分析中，我们可以看到攻击发生的完整过程，从最初于 1996 年注册的目标域名开始。

通过利用重定向验证漏洞，攻击者将这些看似安全的URL变成了恶意网站的跳板。由于用户误以为自己仍在合法页面上，或在不同页面之间跳转，因此更容易落入骗局。

其中一个重定向页面是伪造的 CAPTCHA 页面，由于沙盒内置的交互功能，该页面会自动被绕过，从而为安全团队在分析期间节省了宝贵的时间。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXumkOfYPymUDvYOicDUSqiax2bHtibC9vGtiakrsmked593WsAWgHR097d7hNdWv0iaF0ibhSgrNHaK14GaNV97TdQib39QS7O6q4B3NpI/640?wx_fmt=png&from=appmsg)

之后，用户会被引导到一个钓鱼页面，该页面设计得与合法的微软登录页面非常相似。但仔细查看网址就会发现，它完全是伪造的，充斥着随机字符，显然与微软无关。

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXukyHUzYx4Fd6fgMOHCvSqzxAPv3LDr9kNZ32J8pq3ggiang1cZjZ2TIDCoTfm8rOdgibic3IrKM4wHILgtCaoFWJCF4CjvfCMxEBw/640?wx_fmt=png&from=appmsg)

这种重定向会损害用户信任，并使威胁检测更加困难，尤其是在防病毒引擎没有将其标记为危险的情况下。

## **3. 虚假的 Booking.com 页面传播 XWorm 病毒并窃取信用卡数据**

网络犯罪分子喜欢攻击熟悉的名字，这一次，他们的目标 是Booking.com 。

此次攻击活动利用了通过域名抢注创建的虚假 Booking 品牌页面。攻击者注册了与合法 Booking 网站极其相似的域名，然后引导用户完成一系列看似合理的操作，最终导致恶意软件执行或数据被盗。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXumw8WBgrRHZQ7w0koQMy4AwiaxE40HAed5c93HHoYVnHv7HKoEsibPlc9AUNZ6licDvm1u5ky9wUhSeJltLuumaj2KyqWEnamIfgU/640?wx_fmt=png&from=appmsg)

在这种情况下，虚假页面指示用户按下 Win + R 键，粘贴一段脚本，然后按回车键。这会启动 XWorm 恶意软件，该软件能够窃取数据并赋予攻击者远程控制权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXunibRicco3sWk0pWMuiavRkHmB0GhxfnL5VRanibLJCWw3eJsQkuRItzHSiaVTBfCQ2ibmWlrFrkTtzyQkicf6TticiaJlZEsrEZP8MbIAM/640?wx_fmt=png&from=appmsg)

在另一次**ANY.RUN 分析中，**钓鱼网站诱骗用户输入信用卡信息以“验证入住”。该页面看起来很正规，但实际上只是一个幌子，目的是窃取敏感的财务数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXuk5R1drLN7hFOwlqEZLh4FxlVnYYUXZL5fctZfOpIAXvLYqRV7E9EQGzF4Pq4OFVbFYfoGHeib0qMlJibABfA4wlOu3MjGHNsofc/640?wx_fmt=png&from=appmsg)

像 Iili[.]io 这样的域名与此次活动有关，并且还被发现与 Tycoon2FA 网络钓鱼工具包一起使用，这表明幕后存在更广泛的基础设施。

三月份发生的攻击都有一个共同点：它们利用受信任的名称和平台绕过用户和安全工具的检测。这对所有组织来说都是一个警钟。

## **这就是为什么快速、实际操作的威胁分析比以往任何时候都更加重要的原因：**

* 从 Booking.com 到微软，攻击者正在模仿人们信任的网站， **利用热门网站和品牌作为诱饵。**

* **重定向和虚假应用程序更难被发现。**

  许多此类攻击活动在为时已晚之前都无法被防病毒工具检测到。

* **一名员工的失误可能会让整个公司陷入危险。**

  一次数据盗窃就可能导致内部系统、账户和敏感数据遭到入侵。

因此，为您的团队提供合适的工具来调查可疑文件和链接至关重要。

**ANY.RUN 的交互式沙箱**提供了一个安全的云端环境，可以快速安全地分析 Windows、Linux 和 Android 系统中的威胁。您的团队可以追踪攻击的演变过程，捕获网络活动，并实时收集入侵指标 (IOC)。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

TtTeam

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

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