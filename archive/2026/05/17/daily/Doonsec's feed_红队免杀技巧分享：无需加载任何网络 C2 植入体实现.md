---
title: 红队免杀技巧分享：无需加载任何网络 C2 植入体实现
url: https://mp.weixin.qq.com/s/p2xHul1iM_Kf6agWGGp_hQ
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:08:44.718191
---

# 红队免杀技巧分享：无需加载任何网络 C2 植入体实现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GEVYW8ofHic30x4FObLicTNB30HoFgM0gDficZEQjopDCyWxdbicCqn8znIc4ib3nAMrXndjqKu7waavCGKOJeGNVJ09aNQjetib4XBwP2CAFKcZI/0?wx_fmt=jpeg)

# 红队免杀技巧分享：无需加载任何网络 C2 植入体实现

原创

老鑫安全
老鑫安全

老鑫安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic31HlrPtl053opUMsopMF13L0HLQgkC9WwUVxCZHL3NvZLiavl6W8eySdmr73hT3MAYHvABick8MibDerjfc0XrrnpwqIRsMohaSQ/640?wx_fmt=png&from=appmsg)

##

## 技术原理

### 并非新鲜事物，早在很多年前著名的外挂论坛就有实现代码了（其实终端对抗很多技术都是从外挂界转来![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_42@2x.png) https://www.unknowncheats.me/forum/c-and-c-/500413-native-tcp-client-socket.html ![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic2bjWn8OpKOJibCBFBoPJPttoeDyZvj9zU44QKT4GfYRDL3ibIICnlzr3VYD1Bu5FibxbumJGMwHBt2IBjGQibYqmdxZpcl3M8X6Pk/640?wx_fmt=png&from=appmsg) 注：帖子基本上只有代码，没有任何解释，复制下来运行会大量报错 如何构造IOCTL，参考这篇帖子：https://leftarcode.com/posts/afd-reverse-engineering-part1/。

### Nt宏定义：https://github.com/winsiderss/systeminformer/blob/master/phnt/include/ntafd.h

### 正常网络通信路径（EDR 可感知）

text

```
应用层 (WinHttp.dll / ws2_32.dll)    ↓Windows Sockets API (Winsock)    ↓Winsock 内核接口 (mswsock.dll → afd.sys)    ↓TCP/IP 驱动栈 (tcpip.sys)    ↓NDIS 网络接口
```

用户态的 EDR、抓包工具等，通常在 `WinHttp.dll`、`ws2_32.dll` 层面做 hook，监控 `connect/send/recv` 等 API 调用。

### 该后门的通信路径（完全绕过用户态网络 API）

text

```
后门进程 (Ring 3)    ↓ntdll!NtDeviceIoControlFile (直接 syscall)    ↓afd.sys (Ancillary Function Driver)  ← 直接在内核层处理网络    ↓TCP/IP 驱动栈 (tcpip.sys)    ↓NDIS 网络接口
```

**关键点：**

* **不加载** `ws2_32.dll`、`winhttp.dll` 或任何网络库
* ![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic2mhjHKFicsOmplGyNOicua6QpkKEKIYOYnJm7WKIJp6ic8XOXQic3UpqNicCibicrnicy32ic87f0mVYA9gaLhG2HmGN5usCTiarvHutxaI/640?wx_fmt=png&from=appmsg)
* **不调用** 传统的 `socket/connect/send/recv` API
* 直接通过 `NtDeviceIoControlFile` 向 `\Device\Afd` 设备发送 IOCTL
* AFD.SYS 是 Windows 的核心网络驱动，正常情况下 `ws2_32.dll` 在底层也是通过它来通信，但该后门把中间的用户态网络组件全部剥掉，自己实现了一套“裸”的网络客户端

**可惜使用System infromer依然能监控到流量，这是由于内核ETW（事件跟踪）的 `Microsoft-Windows-Kernel-Network` 提供器，内核级别的事件追踪，可以捕捉到 AFD 的 Socket 创建和数据传输事件，可供Ring3使用。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GEVYW8ofHic2tRLAaUh5eBDURMVTnZlsib59QVG4mdPLQJwVuFiaQsGcvcT3qX07tIWampTRcMctHzr2v3Kias2u8L8hKViatVD72EiaLf9d1t1w0/640?wx_fmt=png&from=appmsg)

**绕过**

### 方法 1：Patch EtwEventWrite 调用链

定位 `ntdll!EtwEventWrite` 并直接 patch，让用户态 ETW 上报失效。但这只影响用户态 ETW，内核 ETW 提供程序不受影响。

### 方法 2：Hook 内核 ETW 提供程序注册（Ring 0）

用内核驱动在 `EtwRegister` 时拦截特定的 Provider ID，阻止安全软件的 ETW 消费者订阅 `Microsoft-Windows-AFD` 等提供程序。

### 方法 3：把流量寄生在已有连接上

最实用的方法：**不创建新连接，直接注入到系统进程，复用它们已经建立的 Socket。** 这样 AFD 层没有新的 IOCTL 调用，自然不会产生新的 ETW 事件。

![](https://mmbiz.qpic.cn/mmbiz_jpg/GEVYW8ofHic3ZmYeUgaRb36ibahlWXiaUpHE2T9velWUAq7ibdkff30WQIgqXmVkmKB2MOpdB5XKTzyFvYJHDJ4RAiaT7pSTOoskBfDUuniacicw0Q/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GEVYW8ofHic2LtvhAhIvSXevEN0AXgfWgGwQmceDyVDGRNUwTA44RoNibajiafHXKN0rAfzqh9mS66oqVUxZt2O3gFvSYJBnasliaL6opuQ24yA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/GEVYW8ofHic2IvRL6ItZ20Y41EQSfGRGMfB9DHo7KLIfFn1r8iaBk2MGo1ce9iaoibZyHlbqEaqju8ArgC0u9k1ab0ESW3oMxjcGicmVPozxiaSNQ/640?wx_fmt=jpeg&from=appmsg)

免杀培训：

[【五一优惠】|  2026老鑫安全0基础培训](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488862&idx=1&sn=eaac9a8d6019630d1fdaeec9e33e8dee&scene=21#wechat_redirect)

往期技巧分享：

[红队免杀技巧分享：躲避现代检测系统的命令执行](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247487857&idx=1&sn=d884699b9103af848b9618c881780d1b&scene=21#wechat_redirect)

[红队技巧分享：看看二进制漏洞研究与免杀相结合](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488573&idx=1&sn=215619cd9851e79ec75408196ad92916&scene=21#wechat_redirect)

[银狐二开特征码定位：从“玄学注释”到“字节级精确制导”](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488792&idx=1&sn=de4fdd492fd456e8283a0ea163e9e83b&scene=21#wechat_redirect)

**[免杀Loader设计：精准打击EDR盲区，拒绝技术堆砌](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488597&idx=1&sn=1191f10bc2b95cfaf96b3e86ec963388&scene=21#wechat_redirect)**

**[自研C2不可缺少的模块-多态恶意软件的艺术，终结基于特征码的扫描](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488813&idx=1&sn=03ba4e48da9df741db055dbca9923c35&scene=21#wechat_redirect)**

**[二开C2中睡眠混淆的内存隐蔽艺术与应对分析](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488774&idx=1&sn=b5bdae5a3fce1bbd0358baacd9256690&scene=21#wechat_redirect)**

**[告别流量拦截！手把手教你配置哥斯拉动态特征](https://mp.weixin.qq.com/s?__biz=MzU0NDc0NTY3OQ==&mid=2247488532&idx=1&sn=1d459ce58b89f242536887c1447d94f1&scene=21#wechat_redirect)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

老鑫安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/bkcWdoIicx2ceUKiaEJfG0L5ZJtpCjuISeOmHuvZZbpibNciacvzGib2W6jibSJPwQnuibB9SIic18Eiafy2LZicYLiarnFtA/0?wx_fmt=png)

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