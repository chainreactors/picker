---
title: 某国产路由器被远程植入恶意软件，官方建议尽快排查
url: https://mp.weixin.qq.com/s/ta_Ra094qQmE_ONRou8IcQ
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:42:57.928513
---

# 某国产路由器被远程植入恶意软件，官方建议尽快排查

# 某国产路由器被远程植入恶意软件，官方建议尽快排查

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vI437xjqWcNyOqqwqLp91PIWOUkeSJhzu6HT2QVMuiaugoC6icsQ5RLzAzjicgywHzBGad8lIpR6w1g/640?wx_fmt=jpeg)

国内流行的OpenWRT路由器品牌广联智通（GL.iNet）云平台遭攻击，攻击者利用更新通道下发恶意软件到用户的路由器和KVM设备上，据悉部分可能已达一年时间；

官方目前已修复云端漏洞，并发布了清理恶意软件的安全固件，但这并不能保证用户设备完全安全，用户需重新安装固件（会清理所有数据）才能彻底清理，或者手动检查清理（需要较高技术水平）。

前情回顾·国内网络威胁态势

* [国内群晖NAS设备遭勒索攻击，官方建议尽快排查更新](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516811&idx=1&sn=8ec8e6aac1f429accbd887ba2446ebc3&scene=21#wechat_redirect)
* [国产鱼缸智能插排遭黑客攻击断电：观赏鱼或大量死亡 官方致歉](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516691&idx=2&sn=fc1d9985b95b49b052db12a34667829a&scene=21#wechat_redirect)
* [意图窃取政务数据！针对国产信创平台的网络间谍活动披露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515311&idx=2&sn=122aa65ef4178f28463673169058a408&scene=21#wechat_redirect)
* [国内知名地图软件厂商8亿条核心数据遭非法爬取](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515053&idx=1&sn=dbdf90f9dfa35613ebe719eca5a98c87&scene=21#wechat_redirect)

安全内参11月24日消息，国内智能网关厂商广联智通（GL.iNet）近日警告客户，攻击者利用其云端远程管理服务中的漏洞，向部分路由器和KVM设备植入了恶意软件。

GL.iNet是一家总部位于深圳的网络硬件制造商，以便携式旅行路由器和Comet系列KVM设备闻名。用户可以通过该公司的GoodCloud平台对这些设备进行远程管理。

官方已发布修复固件，

但已感染设备仍需额外排查

11月20日，GL.iNet发现其远程管理服务中的一个漏洞被攻击者利用，随后修复了该漏洞。该公司表示：“目前，攻击者利用的攻击路径已被阻断。我们修复了云端漏洞，并封堵了此次事件中被利用的访问途径。攻击者已无法再通过这一途径感染新设备。但这些措施无法清除已经感染设备中的恶意软件。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wT9KAyOic0NDMwnjvNbfMIPsXJBZ7gGM7jibQ1cwedcJkza4tqqHPPyvVhZHV79cu3aq4etmsM5j5KHYx0ZNw5QicqeRpuEs8Q12ncuIOeldu0/640?wx_fmt=png&from=appmsg)

不过，漏洞修复并不意味着设备中的恶意软件也已被清除。受感染设备仍需安装单独发布的“安全固件”才能清除恶意软件。GL.iNet建议所有用户安装该安全固件，即使设备目前没有出现感染迹象。

目前，此次攻击的幕后黑手是谁、受影响设备有多少，仍不清楚。GL.iNet尚未披露攻击者具体如何利用其云平台，也未说明此次事件影响了多少客户，以及受感染设备中的信息是否遭到窃取。

此外，攻击者是否进一步入侵了与受感染KVM设备相连的计算机，目前也不得而知。由于植入的恶意软件可能让攻击者获得KVM所控制计算机的访问权限，GL.iNet建议KVM用户也检查这些计算机是否失陷。

该公司最初发布的排查指南建议用户检查设备是否存在以`crond -i /tmp/.log`命令运行的进程，并将该进程列为设备失陷指标（IOC）。此后，GL.iNet还在面向路由器和KVM设备的官方支持指南中，提供了一个由社区开发的检测与清理工具。

该工具可以进一步检查设备中是否存在已知恶意文件、可疑进程、遭篡改的系统工具，以及被修改过、用于让恶意程序持续运行的配置文件。它还能收集取证证据，并可按用户选择清除已知恶意软件组件。

不过，工具开发者提醒，该扫描工具无法检测出所有感染情况。对于已经失陷的设备，可能需要重新安装固件，且不能保留原有配置。原因在于，存储在配置目录中的恶意文件可能在常规固件升级后继续存在。

针对KVM设备，该公司建议用户采取以下预防措施：“检查是否存在陌生程序、浏览器扩展或用户账号，以及异常的启动项或计划任务；留意设置变更和网络活动是否存在异常；使用已更新至最新版本的安全软件进行全面扫描。”

可能在一年前就开始发起攻击

网络安全与服务厂商RemoteToHome Consulting管理着大量GL.iNet路由器。该公司分析相关代码后发现，攻击之所以得逞，是因为路由器上的GoodCloud软件会直接执行云端消息中的命令，却没有进行安全检查。

RemoteToHome还发现，GL.iNet的GoodCloud客户端可能存在一个命令注入漏洞，涉及用于AstroWarp/SD-WAN功能的处理程序。该处理程序会将云端传入的参数直接带入以root（系统最高权限）运行的Shell命令中，且未进行充分验证。不过，GL.iNet尚未确认此次攻击是否利用了这一漏洞，也未证实RemoteToHome披露的相关分析结果。

RemoteToHome表示，在其检查的近200台路由器中，大多数设备似乎都受到了影响，原因可能是此次新型攻击，也可能是感染了另一种较早出现的后门程序。该后门最早可能于2025年9月开始传播。

RemoteToHome对其自有或负责管理的183台路由器进行了分析，在其中152台上发现了可疑活动：24台设备存在具有root权限的反向Shell；47台设备感染了较早出现的持久性后门程序；81台设备存在攻击者下发的命令已被执行的迹象。研究人员强调，这些发现不一定能代表其他GL.iNet客户设备的实际情况，而且较早出现的后门感染未必与11月发生的攻击有关。RemoteToHome目前也不清楚该后门最初是通过何种方式植入设备的。

事件披露后，GL.iNet用户和安全研究人员陆续分享了更多证据，显示攻击者使用了专门针对GL.iNet设备开发的定制恶意软件，并在受感染路由器上植入了具有root权限的反向Shell。这些反向Shell会将受感染设备连接至IP地址`170.39.226[.]219`。

研究人员还发现，从部分GL.iNet设备中提取的恶意文件时间戳可追溯至2025年12月。这意味着，部分设备可能已经遭到入侵数月。不过，目前尚不清楚这些感染是否由同一批攻击者实施，或是否与11月20日披露的攻击事件有关。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过