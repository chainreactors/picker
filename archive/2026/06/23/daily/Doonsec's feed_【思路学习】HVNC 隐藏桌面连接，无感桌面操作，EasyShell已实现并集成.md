---
title: 【思路学习】HVNC 隐藏桌面连接，无感桌面操作，EasyShell已实现并集成
url: https://mp.weixin.qq.com/s/Rptw5TDBZRBtZ1Dx9Mwr6A
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:19.621017
---

# 【思路学习】HVNC 隐藏桌面连接，无感桌面操作，EasyShell已实现并集成

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfO0XCNPrNpFrQ6cp1EmeYm3A8eE3r7KHgGjzXU41HHstttfcRZ3mG9pjicfERMewCNup9hcFtoqWzAVMod13dWmw6T3PCIhl1deUjrJ1L2Q/0?wx_fmt=jpeg)

# 【思路学习】HVNC 隐藏桌面连接，无感桌面操作，EasyShell已实现并集成

原创

沐寒
沐寒

渗透云记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJZJ4pVQHOicqtkQntqLduTfPaVvVnZ4iaGc0DaBeQqNoicYUrzzyOpIsJWbSgNUqV3SodRwKFOIq3Lw/640?wx_fmt=png&from=appmsg)

欢迎关注本公众号，长期推送技术文章

## 前言

感谢各位师傅们分享的诸多优秀项目，经过几天的折腾研究，挑其中感兴趣的hvnc进行分享一下学习，做一篇备忘录

## 一、HVNC

什么是HVNC技术呢？

**HVNC = Hidden Virtual Network Computing，隐藏式虚拟网络计算**，是基于标准 VNC 改造、依托系统多桌面机制实现**无感知隐蔽远程控制**的技术，主流运行在 Windows，也有 macOS 变种。

普通 VNC 直接操作用户正在使用的可见桌面，鼠标、窗口、弹窗都会被受害者看见；HVNC 单独开辟一套**独立、不可见虚拟桌面**，攻击者操作全程隔离，终端使用者完全无法察觉。

## 二、核心实现原理（Windows）

1. 创建隐藏桌面  调用 Windows 原生 API，新建独立虚拟桌面，系统默认只有可见桌面，新建桌面后台静默存在，显示器不输出画面。
2. 进程绑定隐藏桌面   将恶意 / 运维线程挂载到新建隐藏桌面，所有绘图、键鼠输入仅作用于该桌面，不会同步到用户前台。
3. 跨进程消息转发  通过窗口子类化、钩子劫持键鼠消息，把隐藏桌面的点击、输入映射到系统全局输入子系统，实现后台操控文件、浏览器、注册表等程序。
4. VNC 画面单独回传  攻击者客户端只接收隐藏桌面的帧缓冲画面，受害者显示器始终显示自己正常桌面，无任何异常光标、弹窗。

## 三、HVNC vs 普通 VNC 关键区别

| 对比项 | 标准 VNC | HVNC 隐藏 VNC |
| --- | --- | --- |
| 操作桌面 | 用户前台可见桌面 | 独立后台隐形桌面 |
| 可见痕迹 | 光标移动、弹窗、窗口全部可见 | 前台无任何画面、光标变化 |
| 察觉难度 | 极易被发现 | 普通用户完全无感 |
| 系统依赖 | 通用图形会话 | 依赖 Windows 多桌面 API |
| 典型用途 | 公开远程协助 | 静默运维、恶意隐蔽操控 |

## 四、技术研究学习

目前EasyShell已实现HVNC插件的调用与展示，不过仅限用于学习演示，不会外发。

登录EasyShell,点击屏幕截屏模块，可以发现存在物理桌面与HVNC两种方式

物理桌面就是传统的方案，所有操作客户端均会实时同步

为了对比研究，这里用双屏的方式进行桌面查看

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNrKpTdkkoyLMRvvbjiaPWAxicMkrmHibBVMc2Dicc8Okhow3cFCz4LVVkiaf9WGeJbk60joCotsAUqZ3oDb46P9tBoD1zQV5c2Sia9eA/640?wx_fmt=png&from=appmsg)

具体演示，可以查看以下视频

测试过程中还发现一个有趣的情况，即目标主机已锁屏，然后点击下发HVNC，惊奇的发现，可以直接进行控制，无需解锁桌面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNoZvxnW9YPuWCeJcK2ib0l0qUIicICQu94CoXe9Kzlh3pre177DS5x1mkdTszbRjYs4ictYxGQHeH4TUpKpt1rP0YOopFzbiaPZOjY/640?wx_fmt=png&from=appmsg)

## 五、安全检测与防御手段

### 1. 终端检测特征

1. 枚举系统所有桌面：`EnumDesktops` 发现非默认陌生隐藏桌面；
2. 检索进程线程绑定异常桌面（`SetThreadDesktop` 行为）；
3. 排查窗口钩子、全局键鼠消息劫持程序；
4. 流量监控：陌生出站 VNC/RFB 协议流量、非常规端口远程画面传输。

### 2. 防御方案

1. EDR 终端检测：监控`CreateDesktop`、`SetThreadDesktop`敏感 API 调用并告警；
2. 组策略限制非授权程序创建新桌面；
3. 禁用未授权全局钩子、远程画面传输出站；
4. 定期查杀 RAT、银行木马类恶意样本；
5. 服务器禁用 Session 0 交互，阻断后台隐蔽会话。

## 总结

最好的学习就是看各种开源项目，站在巨人的肩膀上，看清前行的路，然后一步一步走过去。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

[【工具更新】EasyShell v2.1 版本更新，新增https与doh协议上线，新增键盘监听小功能，修复分组分页切换错误等诸多bug](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484909&idx=1&sn=dd2a1603aa327f2dc70e0af2d55ad4df&scene=21#wechat_redirect)

[EasyShell Extensions 脚本菜单 — 用户使用手册](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484902&idx=1&sn=4f9096c77e3e2417eded3a064529a4b9&scene=21#wechat_redirect)

[【工具更新】EasyShell v2.0 版本更新，新增网络拓扑探索，优化内网多级网络上线，修复shellcode无法加载等诸多bug](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484898&idx=1&sn=5a39f358de3b7e7be791cc76a6c95fa8&scene=21#wechat_redirect)

[【工具更新】EasyShell v1.9版本更新，修复存在的bug，提高程序稳定性与免杀能力](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484879&idx=1&sn=6176e276171325ea1ab307f427745a28&scene=21#wechat_redirect)

[新型社工钓鱼伪装技术之WinGet配置文件+Lnk文件](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484822&idx=1&sn=0fa45b08197bfcdfa862f150adf32e36&scene=21#wechat_redirect)

[默连(morelian) 简简单单的webshell管理工具(支持常规的代码执行，文件管理等，默认支持http与socks代理，支持gui与浏览器两种运行方式)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484811&idx=1&sn=cb2d380da6d800639e7a1227c2473a40&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.2.2更新(1.新增云上安全，支持oss存储桶扫描、云存储管理与云服务管理;2. 修复数据库连接bug )](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484786&idx=1&sn=f5e7954a9de25cf2439d2a88de364383&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

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