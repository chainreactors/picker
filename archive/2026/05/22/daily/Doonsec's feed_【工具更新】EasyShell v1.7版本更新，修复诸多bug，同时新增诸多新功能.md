---
title: 【工具更新】EasyShell v1.7版本更新，修复诸多bug，同时新增诸多新功能
url: https://mp.weixin.qq.com/s/vfmqYs-BwhW-kC27CG3QyA
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:35:21.155305
---

# 【工具更新】EasyShell v1.7版本更新，修复诸多bug，同时新增诸多新功能

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfO0XCNPrNpCkzibLmnVkW6LzdsFV9lzopqIUyG39tFibCicnJ7JqknNcGLIwMVdEG7C6UIIqpkPc8vcKSHZYeSKMibbXPFTbIbWMSsJicb5Zzxg/0?wx_fmt=jpeg)

# 【工具更新】EasyShell v1.7版本更新，修复诸多bug，同时新增诸多新功能

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

听人劝，吃饱饭，师傅们说啥我加啥，经过一段时间的更新，新版本的EasyShell出来了，修复了诸多bug，同时也新增了诸多功能，在此进行一个更新说明。

1. 新增DNS监听协议，支持DNS协议上线
2. 优化客户端体积，将不必要的功能全部使用插件的方式进行实现（但是go写的，体积依旧不小，后面再进行迁移吧）
3. 整理EasyShell插件集合，主要新增了linux、mac常用的信息收集命令
4. 修复隧道代理偶尔失败的情况
5. 修复了文件上传过程中无反应的bug
6. 修复文件管理模块点击目录面包屑卡死的情况
7. 修复客户端生成win11黑框框的问题
8. 修复linux客户端无法后台运行的bug
9. 修复linux插件执行命令，插件日志显示混乱的bug
10. 修复前端插件执行时，插件日志面板遮挡部分按钮的bug
11. 修复交互式shell自动关闭的bug

## 展示

1. 新增DNS协议，点击监听器选择dns协议即可

dns协议不支持一键上线，需要自行手动选择dns监听器，然后进行生成

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqAzefGwtUTneUVstuFzsDMv9Nic9tFh6Bb4F5ZMQwyvfOvXXR67Q8qJLNWWgHfhJDA5xkC0EsGXee9EajFpl9qIsjGsWpniaVys/640?wx_fmt=png&from=appmsg)

2. 修复文件管理上传下载等导致客户端卡死的bug，现在采用后端异步进行操作，优化使用体验

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpyQjeAiawyt4wkicd215Ze3zzdUNEgdhgW7IHkD7n7sx2hr5t98a1fpJDEqpvk9JIj55U26hiaFDLdvRVa3GD95QlVYAKEVy8CmQ/640?wx_fmt=png&from=appmsg)

3. 更新之后的隧道代理修复了以往连接卡顿，偶尔断连的情况
4. EasyShell插件集支持根据目标主机自动加载对应的脚本进行调用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNpjdcj5I8Y3qwIHpxn86VyEHcAw1K41ubrsAgdxzGRB86SjQcicUEUQ1Qz2KNPiaOSqZH0kgmHMHibKBlpsiawaqj44DVLoUd1pdos/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpSuhOBx8Nah4amicEibTTjUTHEHLgiaV8nfMlvFVQpBic5ia7OiaPEPqbrt9w2ZO2FttWIVECydtS2jaRfXc6fApWxs4hy575fxbRXs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNo2l8PQ2qUQzX8mcdbsMwaMM3zbnrSTA15hjQ41sEPDWXdbZXNSggDYtLia208WvB0ROpGPB5RHCX4MNAAhdTB4UcIquibGhhOJo/640?wx_fmt=png&from=appmsg)

5. linux插件新增一键实现用户态的程序与网络的隐藏，效果还是比较明显的

未进行hook：

可以正常看见交互网络与应用进程

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpZIqUXFlfIIsyzcBuv6GdFR0RaHX7pvkZoibqVQEVWibQKFlcdliabzwcPN0tJX11Qzpj7cxHrJsdialyLX7GQM9hWKnlAd6sQ0fE/640?wx_fmt=png&from=appmsg)

使用插件进行hook，输入我们需要进行隐藏的应用pid，以及传输的ip地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNr8Cf2JFdVB0gNaMYyE4LibUemuiaZ5IbKWCo0p3uBDkQf5koX56bDe9cfKhK3oYvibC3NRG6xCKlKqOtDrCoCaa5PYLfOL0Bafiaw/640?wx_fmt=png&from=appmsg)

此时即可简单隐藏应用与交互流量

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqmg5Vv6gNQor3zlDVW8gFwS7OWwziby1dRGUxxlUsbMyrph5FFpaaFMKjLOqFTeIgVdBzDRAQ2AlhQSSWjBQIt2c3icTXRKUibWg/640?wx_fmt=png&from=appmsg)

并且不影响正常的ps ss等查询

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNoOfg1T6uFnIk1gcoUPicVO9KDOibpgxVd1vLwXricvlFEaqZ9VEW86NrQicpaN21W1G5Xf8iaoJGXUEXf1OABNlwu9fdE1lDDjuicas/640?wx_fmt=png&from=appmsg)

## 获取

欢迎各位关注渗透云记，加入鄙人的小圈子《叮叮当当》即可享用

ps：渗透云记博客会员与叮叮当当纷传圈子权益共享，目前均为99元/年，随便进入一个即可。

同时可以享受

1. 默连(morelian) Webshell管理工具、

2. EasyTools免杀版、

3. Webshell-Agent自动AI迭代生成绕过

等诸多平台的会员权益

历史旧版本直接后台私信回复：easyshell 即可，bug稍微有点多，优先推荐新版本哈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

---

鄙人的一个小博客 渗透云记，

官网地址：www.encenc.com

博客地址：b.encenc.com

目前已集成EasyTools渗透测试工具箱的登录，Webshell\_Agent AI自动生成平台的登录等，一个账号，多平台联动使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK5R6NYcibf6ADO4U7BvUHupNyYDu3RwMYRL9ickjZNUMoHeGcAS7fgF2zcyWaODWcOuqjqkeAibjkPQ/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

渗透云记

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