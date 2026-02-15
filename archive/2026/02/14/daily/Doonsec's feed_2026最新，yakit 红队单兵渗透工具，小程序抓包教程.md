---
title: 2026最新，yakit 红队单兵渗透工具，小程序抓包教程
url: https://mp.weixin.qq.com/s/3OUaTuxrIlPhguPloKv4Ag
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:21:42.205520
---

# 2026最新，yakit 红队单兵渗透工具，小程序抓包教程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNYM2xGCwvVGibnkJ6nmux2dRZ6q6kS1J6DSlwkbUCOp097KpiaZEJicqIfBgqztXwSXU8mLuF5yYCtV2iausu0hFD7fWs7XibJC5TQ/0?wx_fmt=jpeg)

# 2026最新，yakit 红队单兵渗透工具，小程序抓包教程

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器中沉浸阅读

小程序封闭性比较强，抓取数据包容易被刚入门没多久的师傅们忽略,

下面分享一套实测稳定的方案：YAit+Proxifier代理工具，只要几步就能快速获取小程序https流量，适用于渗透测试、接口调试等场景，新手也能快速获取。

再推荐一个视频学习的知识库===》我们的官方B站视频

> ❝
>
> **💖 温馨提示：**本文一切操作基于本地环境复现，请不要利用文章中的任何技术对未授权的靶标进行渗透测试，这样属于违法行为，如有使用，还请自行承担所造成后果，与智榜样网络安全无关。

## 一、工具准备

**Yakit**：红队常用的渗透测试工具，内置代理功能，可拦截、分析网络流量；

**Proxifier**：全局代理，指定程序（如小程序进程）流量经过Yakit代理，解决了小程序绕过系统代理的问题。

工具下载：https://yaklang.com/（建议下载最新版，兼容性更好）至于安装过程，这里就不讲解了，相信师傅们会通过自己的双手丰衣足食

![image-20251230203538991](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPV4icREN05EwVaFveBq1sDiciat0u99fFzH0bz6RtaFpwdAuQNIibmia23JGJxIWyB3uUKgGbjPpyW4MmibWp1N6jNDiaaBadOTW95N8/640?wx_fmt=other&from=appmsg)

image-20251230203538991

Proxifier：可以通过其官网“https://www.proxifier.com/”获取(个人版需要授权，也可以免费使用proxyCAP）。

## 二、yakit基础配置

### 2.1 安装并信任证书

Yakit 需通过证书解密 HTTPS 流量，必须完成这一步：

点击左上角的那个感叹标志，我们点击手动安装

![image-20251216211858920](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauOnhQr4AiaY84cZOYYDx3YOZPuNvlckz8qw6MLVb22ibqpcaZW5sfsa1IS7kjb8BHBhnaTUfufibCeUgdMcP9icOT4sMFjqryR5aAA/640?wx_fmt=other&from=appmsg)

image-20251216211858920

之后会跳转到yakit的安装目录，双击执行这个bat文件安装证书

![image-20251216212057653](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauN40dujdxE1oT5yHm4JNtgwnexUiaEDRYXHMtA9CvRcs8E6NUN1rgD9KdBkofLjkUia7fnMEvkKUDbEy5pGwvyh0zOxGlodEvC6Y/640?wx_fmt=other&from=appmsg)

image-20251216212057653

弹出来一个终端，又提示你是否需要安装此证书，我们选择是

![image-20251216212118532](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauMP0mTlpYUPftwTYe3mWicE8tEBCO6Uyicax1qY2dM6xwh5ZEDCiciaygUbpXhBiaL5Swf1mPnhOAibkULT1HEFicxl8v6fUrRd0hyjfs/640?wx_fmt=other&from=appmsg)

image-20251216212118532

### 2.2 配置代理监听

再找到按照下图这里箭头的顺序，点首页 > 下拉菜单配置监听的主机（127.0.0.1）和端口为8080，其他任意端口都行，但是主机必须是127.0.0.1

![image-20251230204529804](https://mmbiz.qpic.cn/sz_mmbiz_png/1E8ULvdwpfPGES2VJFuH2t5I6IBGz2jSY610Osj9r6iaz6m0ic6N1ibhNfP4ozYmFuQdiaXELZa38icb9JlaMbznKFUDibibSme1LfsuOp2viaf7jk4/640?from=appmsg)

image-20251230204529804

之后会跳转到这个界面，就可以开始配置proxifier了

![image-20251230215144746](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauMGOyibYian2ibSILWf9Amq0v01PykaXdKZvrNBH81NCDzZeFiaRpk0hDLAeEm4pib7ZeZIicokMOxXtRZI1p1hy2foaQFbrt4PdIZjs/640?wx_fmt=jpeg)

image-20251230215144746

## 三、proxifier配置

### 3.1 添加代理服务器

打开 Proxifier，点击顶部「配置文件」

![image-20251230215432731](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauOVteOJoGwoYoM8H9zdGsiaLxoicg5jlbcO2DlltJjRk0Kh3X1XKb3MEASZqicQulGUzJicjCjDSkzdB0iazFF23ibc671vMGaiagReKk/640?wx_fmt=other&from=appmsg)

image-20251230215432731

选择[代理服务器]

![image-20251230215458220](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauP7kX3Yu6L9e79PTgOZmEOWjh1vPmyXiauWMghFP0S7c957icce78yUKjeGcRuyS7K8TYWQJT0edOh84nXGHyU2GhRiae4qCwC4Lc/640?wx_fmt=other&from=appmsg)

image-20251230215458220

点击编辑第一个代理，将proxifier的流量代理到yakit的代理主机以及端口中（如果默认的没有那就选择添加一项）

![image-20251230215627035](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMeU6EcgmuYom7OribBPwlA5MNWrfteKeTMJDyAYk7rfQdKqGqRZ4RxX213CZkX435H3VomtLUsOZyRE8ANTKuLZDIYV7HMYdcY/640?wx_fmt=other&from=appmsg)

image-20251230215627035

我们再选择代理规则，配置需要将流量转发到yakit的应用程序为小程序的路径

![image-20251230220611857](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauMCyuElibVeiaVe61sq8uvEmOJyuDyfWMiaweWMhVBWqDRKGZZ2WiaiaSTqL3ye5TtVrJ1JiaQ0QCvxgBwBHF7uBuFIVXZ3214KElLhg/640?wx_fmt=other&from=appmsg)

image-20251230220611857

这里随便新建一个，因为我已经新建好了，给师傅们看看我的配置吧

![image-20251230220708249](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPHoU9FVbLysTxOAT33m7SdBpKNmOn7ia7ekZIvRboNTuaVeUGp5ar7uuGJvNk5ALncu6zScO0ODuodP1sQeIaAveKot9jkBibKE/640?wx_fmt=other&from=appmsg)

image-20251230220708249

这是我的编辑详细界面，最重要的是应用程序的选择需要填入wechatappex.exe

![image-20251230220755312](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauNkbxMJBZwp4nCEoSezRlFQLtWUMhYntUmzYQWvhzibolemJzZFHIst83K0JXJlDheDdibwtia8ibicmFlk6m0asIfcMf4MkWKtiaddI/640?wx_fmt=other&from=appmsg)

image-20251230220755312

为什么要填wechatappex.exe？而不是其他的？

让我们随便点开一个应用程序，比如圆通

![image-20251230220937926](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauNAzDt0a6Vobu9wQnUl9eYEZiaiagYuJr8YhrMuVv9qtyvRBCib1LIibVlubVAJqCS7WLeOTGeXKpTHfdaYrFy0R0WR6rPia2IVoQ7M/640?wx_fmt=other&from=appmsg)

image-20251230220937926

在底部导航栏右键，找到任务管理器

![image-20251230220956553](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauObS6bYGXovvTgTia9obRAN19d1Lb4Yb1S2ZudT710ljTDkBlMeNAZnIoW13P9oFoC2Bp2DHUkcuMItuPctsP7coFGKKp4bZDao/640?wx_fmt=other&from=appmsg)

image-20251230220956553

在旁边选择进程，这里会多出一个运行的应用程序，这个应用程序就是微信小程序运行的进程

![image-20251230221018436](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauPAA2xXWyMqeibutibtSj7phAEibvOWXoq5S7OQZPyWbVN8bavkSSChRLdx4x3JqxicaSic11BaUI3V8icPqiaAuAMuVoMp2ic0g9N9zUA/640?wx_fmt=other&from=appmsg)

image-20251230221018436

展开这个应用程序，随便选择一个，右键再打开文件所在的位置

![image-20251230221205143](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauOPgSj1bcJMyROAtfS0nVkLW7EI3TAMo3fMaPQoIkpbfAybezDqY1xBvviaicUo3QibH0kMoIDoqtnicv1sC3VVHftAZCdPmLvBBrk/640?wx_fmt=other&from=appmsg)

image-20251230221205143

记住这个路径（可以直接复制）和文件名

```
C:\Users\用户名\AppData\Roaming\Tencent\xwechat\XPlugin\Plugins\RadiumWMPF\18055\extracted\runtime
```

![image-20251230221411988](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauP7ibSkuHZfCKKX4f2hcYnExvvC4NIWAnjwkrgsZ9qCd2Z79RHMxMic2ibeyzBXMVn5dJ3hasxTgvmzypFY0tEhevEmSQianlibsjKA/640?wx_fmt=other&from=appmsg)

image-20251230221411988

返回proxifier代理规则配置，选择浏览

![image-20251230221621625](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauPibBuOGQonmyn0Zkwg91lLMQxX1Yw5ibibAm4tk4NhvNFh2JJibfy44bhKmodqInVQyibBibpQBYIthzctlKj1jY95SsrPaBM1yQGPA/640?wx_fmt=other&from=appmsg)

image-20251230221621625

选择刚刚运行的应用程序，看到的小程序文件名

![image-20251230221611700](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauMckTz9ZSm0iaPhlQ0J3L3jgKuYRzvKooZkYbPZQRG4MFeLDdpUjEEvmq4bicAmWRFs2BCfYCtav0ORZib3EDrYcc3Uk0WZ9xzqRg/640?wx_fmt=other&from=appmsg)

image-20251230221611700

这样就配置好了，确定。。。确定。。。确定。。。》》》

![image-20251230221748467](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauNzgeicuZgTEMlJHkLZqHZbcWTJTLgj0BXltNUFjeEqib4GKx7NsT64lSFAkjLzfjvWCjeJ9wZkyldPnqfv1IldXaBrkWZs5NiapM/640?wx_fmt=other&from=appmsg)

image-20251230221748467

## 四、验证抓包效果

在yakit就能正常抓包了（如果没有抓到，那么就刷新一下小程序就可以啦）

![image-20251230221842132](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauNiaoia5FaFeXcAIguykXdlCJWEqSLyg6FP5I51U1MNfZhHvvBsWYsacuGK7RjBPAFzciapgxUfyll2X0FnmsMsC5nr4gmelYZfk4/640?wx_fmt=jpeg)

image-20251230221842132

## 五、总结

本文运用“Yakit+Proxifier”组合来演示小程序HTTPS流量的抓取流程，主要分为3个部分：

1、**工具协同方式：**通过Yakit的代理拦截流量，利用Proxifier强制代理来解决小程序绕过系统代理的问题，通过两者的协同解决小程序封闭性问题；

2、**配置要点**：Yakit证书安装与信任，本地地址（127.0.0.1）和端口（8080），Proxifier指向小程序核心进程(Weappex.exe)，流量定向转发；

3、**实操注意点**：配置后未抓到包，通过刷新小程序触发流量；进程路径可通过任务管理器准确定位，避免因路径失效。

本方案兼顾稳定性与可操作性，新手基本按照步骤配置即可掌握小程序流量分析能力，为渗透测试、接口调试等提供应用支持。结合文末福利学习内容，可进一步扩充相关技术。

## 六、🎁文末福利

**分享本文到朋友圈，点赞+在看+关注，一键三联，可以凭截图找老师领取**

上千**学习资料+工具**哦

![22919c6e4ef945aa9a9cbf0f6df4f6ff](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauPR7dNweS0KsSNabg5gTZkMZlP6f3d0OZ6JC0viaa6AmWmpJeXQI4JbzUXI8sAZN9FRD5YhLZXGibk2CLFYEWa023pBMgqvibW4O4/640?wx_fmt=other&from=appmsg)

22919c6e4ef945aa9a9cbf0f6df4f6ff

**分享后扫码加我！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rYoibTlMQ1MpHdawUKrSwglIRtuj0JaKrsHFZKjEmiac6PBmXbWcK5fMZDnDJQHn3mlYHl0ibVEibUq8pKDspI0Qjw/0?wx_fmt=png)

智榜样网络安全学习中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rYoibTlMQ1MpHdawUKrSwglIRtuj0JaKrsHFZKjEmiac6PBmXbWcK5fMZDnDJQHn3mlYHl0ibVEibUq8pKDspI0Qjw/0?wx_fmt=png)

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