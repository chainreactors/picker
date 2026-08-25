---
title: 安卓逆向 -- 某小说分析脱壳与去广告
url: https://mp.weixin.qq.com/s/KUaePdlIHMNNyYMyGeWNJg
source: Doonsec's feed
date: 2026-08-24
fetch_date: 2026-08-25T02:57:54.169200
---

# 安卓逆向 -- 某小说分析脱壳与去广告

# 安卓逆向 -- 某小说分析脱壳与去广告

seventeenJoy
seventeenJoy

逆向有你

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明：本文仅供学习交流使用，所涉及的破解版不提供下载渠道。所涉及的技术请勿用于非法活动，否则所带来的一切后果自负。

App名字就不说了，可以直接去某豆荚下载，这里给出下载链接：

https://www.wandoujia.com/apps/8429351

默认选择最新版就可以

开搞前准备：

1.MT管理器/NP管理器

2.jadx反编译软件

3.root手机

4.脱壳工具或网站

5.良好的学习钻研状态

打开App，广告全家桶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWTRiczeG0tEnzhRNa0oWyZ9bic91sRrlV62NAxhtIhGXLUzpLNVMBsPUD79yGRPia1l9KeJzswVIgnvUgU9iaMRpgiaj9KiaiasLtx3o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUVauKsEbt23Cu6DLSkJKsRYRxhPrtZCqoCk6ZAhwkJ78I4SMqynbldutAic0dCkhfo9rrZqT0WWfr1FIDhiaY6q9VtjsLBJibKicibc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUU2lwaFDDA6lGUtCz3jwGicmqPFcnmicmmvicRt0sbGdj8KldFS2b4crSKQOAdBJ4Da4CMSxzhicNicm6NRRSVvr6TeB2GkQBaFibHI0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUWAUvD5VeRhmac6lNTPN9qGvhAnC6oT7EibiadnWoegjicicTq3goxZ9X0YHCqFU1v7fGuxF4nTPd9KrrzT3173EAO833JWgpbF52s/640?wx_fmt=png&from=appmsg)

展现我最近学的去广告技术的时候到了

1.可以定位初始化广告加载的函数，尝试注释掉它以实现跳过逻辑
2.跳过广告加载的Activity，直接进入主Activity，但这种方式有时候不行，因为有可能初始化广告页面的时候加载了一些什么东西（咱也不懂，不知道干了啥），二来是大多只能跳过开屏广告，app主页面的banner、插屏、信息流广告不适用
3.通过libchecker软件查找广告服务，更改对应厂商广告初始化方法，然后通过替换它们完成去广告，这里给出两个教程：
逆向去广告大法  https://flowus.cn/mengqing/share/31f1af3b-f273-402f-90de-e78e93e857e5 --感谢梦倾三生三世大佬。正则一键去广告，去广告终极大法   https://flowus.cn/mengqing/share/39515bac-e86a-4c47-b56f-e207c62e2f3a --感谢大佬整理。但是我们要先解决一个问题：App是被腾讯加固了的，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUU7FppFyffgicItWOWEdfJAibL3jULy7b0IM2U3Pic3JutPugPWlpb1Ae95N2qyZayia7JAql0SVzBNE8HgfImKR5xibb37SCSPyWCo/640?wx_fmt=png&from=appmsg)

真的很头疼，因为我也还不会脱壳，但是我去某站看了一波教程，试着跟着脱了一下

教程链接：
【腾讯御安全脱壳教程】https://www.bilibili.com/video/BV1o7421K7Dg?vd\_source=7f09abe682080fc8629bae8db825a84b
【非常规思路的(腾讯御安全)去加固(脱壳)教程，可解决部分闪退问题！附两种失败方法，超详细讲解！】https://www.bilibili.com/video/BV1c68XeHEpQ?vd\_source=7f09abe682080fc8629bae8db825a84b

接下来的就是我照猫画虎的操作了：

先提取安装包，然后打开脱壳工具或者网站，我这里使用脱壳网站（大佬们有什么好用的工具也可以推荐一下 ），网站地址：APK加固安全测试  https://56.al/
把脱好的dex压缩包下载下来，长这样：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUnKI2J6ElIRKUb5Tpj8IaVDoqOLPuNjKUAUsMktZGDJicR3FvUoS4iaib6aQaIHdHM0OAN0H8wvq0iaLMN6j3JU44icpT9FNqOVRFY/640?wx_fmt=png&from=appmsg)

其中第二个文件里有app启动原入口，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWSInPdbFYjia2POdic9vicNWxp5GlaYTg92wlmUMttNN0X3wNXCHcl7PJiaOV81BMRuTQ0l2rGfohwvAaedBYWog5Om8nujXVBhB4/640?wx_fmt=png&from=appmsg)

然后全选第一个文件夹里的dex进行修复：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUUBFa3JfyrmMHYLQ9Q72DwTfM4Hulchoqr79agB497ibIOAY4Z4qAOaCFlGMju2yb2kvyG5hk620ibWPmaYRoXaDBIZI2d7pvjbc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUUeXsZ5LiaZicSWFZ8MH6nibIVo5tTSLlhGibF6qgmsOibjibIqGJoARgTAdy6nX8LnpODMX2gwN13vKgepLttqkgOqXHSvibDibibqBMJ8/640?wx_fmt=png&from=appmsg)

将修复好的dex替换掉原apk里的，这里注意一定不要勾选自动签名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWQ1rAsOzVy0P9juGlGKxkjn2vWbdibuQgxt0K6n5SDLjsTCqfZGZt4f1iaaVUicO4BydCaianyF885FW0aiceuhjdTXW380bkBGlCs/640?wx_fmt=png&from=appmsg)

后删除加固特征（全程均不要开启自动签名）：
1.删除assets里的两个：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUUW3XWiaV4n0NVo3xFtjZJk3ApNWibcAhA6qkKjl4UxEhSzsZzNZkxlibviacoibKZe5lFcNSy3LJamP0UNL0TyhwzyRmJia4Jz5qywc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUVUjTZ3g5ADDkUibGf301CDTbkf4qH0CLqJHNA8ADaJiaD1qXzaPmqrY0Khj70ib8hjjiaFbmJAibIHC8VhaulIvcaTcML2ywQT9tLc/640?wx_fmt=png&from=appmsg)

2.除lib里面带shell的so文件（32位和64位的都删掉）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUUnaVwBt0DN6wpoKMOslcoz3mXDWcCW1tMqrGIVxzAf9x7XQqqODDicTe6nTOltGe5GL9NsoCPXAHaqyzm9CqccnRibYJMoQRs2M/640?wx_fmt=png&from=appmsg)

3.最后替AndroidManifest.xml里的application里的android:name="MyWrapperProxyApplication"android:name="com.yl.frame.app.MyApplication"，名称就是刚才脱壳后压缩的第二个文件里面的。最后保存xml退出，不要自动签名，这时我们再看app：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUWlUNF33yq9EybmqxnVMBv3CIVc39ianYFdhZuQdAFjDQ3iaibbg1RGBJicwktKeGH8PnuseLyXGECcFfgQuJZibX0tJvJBPCiafKawE/640?wx_fmt=png&from=appmsg)

还有一些加固特征没删掉，这个我也不会了，但是测试发现app可以正常使用，随后我们使用MT/NP管理器去除签名校验、安装就行了，对，软件有签名校验，现在正式开始去广告操作：使用MT管理器Activity记录功能：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUVv5PE4bRkDk1ZmB0pephUYpuNrZRqvfYq7j00JHJ7huPeEsPzVrWsgVlqwblia6h80qMcWzS0wHtqEWiakhU0SIyuKhblM7JiaR8/640?wx_fmt=png&from=appmsg)

其中Splashactivity就是开屏广告Activity界面，我们使用jadx反编译软件后查找这个类名
随后一般搜索OnCreate方法，但是这里搜索不到，于是我一顿分析，最后偶然看到一个这个函数名：

![](https://mmbiz.qpic.cn/mmbiz_png/Gv6JExJQjUVicEKZj8ibbiaDW0IE5VUQx0TLwNAjcQjgqBCk9d5G831lYT5ezBibwBQiay6RtWP81uwykq2eu7mOPoLRrZ11ArjJFTmNBEFichKlA/640?wx_fmt=png&from=appmsg)

closeAllAd？字面意思就是关闭全部广告，我们猜测让它执行能不能跳过全部广告，于是我们再次打开MT管理器进入这个类的smali代码部分，让那个if判断走这里，原本是nez，我们改成eqz，保存再签名看一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUXEDiaOMICpd2CTcfOj65ceibNckpgwtCQEaEL235OMWVywEFakQwU6Xib0qfNLTMGibVp1wVHEXCLYojEnibPHDMQiaj00I7N3XQduw/640?wx_fmt=png&from=appmsg)

最后你惊喜的发现：

广告通通没有了！！！！！打开直接进入首页，没有任何一点多余的操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUX7EC4nTT5iaEicjKqLUYibgPn7CZI8cWN8GdmicznBBA0VgjvOumf02xfpnFYGDZicuvQmvCBRNWYjZJA4c13kibsVkLFjSJNfHrrLc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Gv6JExJQjUUF0c3FiaiaggfMO1yZntfOPv9p7EZSBpicjAa9eLBL0IrSmwxNUsKxPaIBWwvUibEiaA7M1GdQcyVnB8SFCm6ZxfSnut6EMRw7HLtg/640?wx_fmt=png&from=appmsg)

随后也没有什么其他可以再逆向的了；至此，我们逆向就结束了，有时候就是一点运气成分在的

如果教程有不妥之处，不够详细之处，望请见谅

最后一些友情链接（如有侵权，联系删除）：

android逆向奇技淫巧一:去掉开屏广告&跳过app的某些activity  https://www.cnblogs.com/theseventhson/p/14670336.html

Android漏洞之战——整体加壳原理和脱壳技巧详解 https://mp.weixin.qq.com/s?\_\_biz=MjM5NTc2MDYxMw==&mid=2458457914&idx=1&sn=1d505597b47089cbd8bdc1e6e0a2b068&chksm=b18e27b086f9aea63d4404f118b0dc4c0b87c5986f20e556a5a85c967834df0d7f3e8e6d98d6&scene=27----里面好多专业名词APK逆向分析入门-以某app脱壳为例 https://xz.aliyun.com/news/12761

不知道为啥，链接插入用不了，只能这样给出网址了，格式有点乱，望见谅

**欢 迎 关 注**

更多精彩内容关注下方公众号：逆向有你

个人微信：ivu123ivu

每日自动更新各类学习教程及工具下载合集

https://pan.quark.cn/s/8c91ccb5a474

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8H1dCzib3UibuuhdO7GMx4wqK5PQMWgr8pNaudBlYJUYXP6R6LcL0d3UYmPLoiajIXwaibhvlchGibgiaBGwMSwuq58g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/WJRHqUiaud0ouQQFouib41PSeoKKZO7mHSXDQ01XdAqPlLVKZD1yyPlfnErolowiaaDic5GDnU7B2GNhkou8PGqaCQ/0?wx_fmt=png)

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