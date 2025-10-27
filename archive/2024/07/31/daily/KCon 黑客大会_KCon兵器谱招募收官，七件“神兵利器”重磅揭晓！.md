---
title: KCon兵器谱招募收官，七件“神兵利器”重磅揭晓！
url: https://mp.weixin.qq.com/s?__biz=MzIzOTAwNzc1OQ==&mid=2651137704&idx=1&sn=2d56f1a4ec06051fab22ee5d59bb5647&chksm=f2c127c8c5b6aedeaf1d50503922078afe51833797c17b88792879e9559b2417688d40ef4698&scene=58&subscene=0#rd
source: KCon 黑客大会
date: 2024-07-31
fetch_date: 2025-10-06T17:44:27.156402
---

# KCon兵器谱招募收官，七件“神兵利器”重磅揭晓！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbLc2DypAaGP61h5XCF1W0COa6NgvATBq5jicD2FTYfabxhM7lDDMPmQruQxXHtfuicPhXoIEicdTXmg/0?wx_fmt=jpeg)

# KCon兵器谱招募收官，七件“神兵利器”重磅揭晓！

KCon 会务组

KCon 黑客大会

![](https://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIbLc2DypAaGP61h5XCF1W0Cc492zOFFnzicTOyQq9LkvSxr8QmrkiaajIGaIHVQZrIfdyunTF2FHm3Q/640?wx_fmt=png&from=appmsg)

为了鼓励国内安全自动化工具的发展，展示更多安全人员们的安全自动化研究成果，自2016年起，KCon黑客大会便引入「兵器谱」展示环节。

过去几届 KCon 黑客大会现场，已有七十多件“安全神兵利器”受到千余名参会者的观摩与试用，并获得媒体朋友们的广泛关注。

今年，我们为大家精心挑选出了7件安全江湖的“神兵利器”，将于KCon舞台尽情探索与展示！

**（以下排名不分先后）**

**CaA**

**作者：key**

简介：CaA是一个基于BurpSuite Java插件API开发的流量收集和分析插件。它的主要作用就是收集HTTP协议报文中的参数、路径、文件、参数值等信息，并统计出现的频次，为使用者积累真正具有实战意义的Fuzzing字典。除此之外，CaA还提供了独立的Fuzzing功能，可以根据用户输入的字典，以不同的请求方式交叉遍历请求，从而帮助用户发现隐藏的参数、路径、文件，以便于进一步发现安全漏洞。

**Pillager**

**作者：簞純**

简介：Pillager是一款适用于后渗透期间机器敏感信息收集的一键化工具。从浏览器数据到聊天软件，从远程管理软件到机器基本信息，考虑了渗透测试的后渗透阶段收集机器信息的常见需求。特点：

1.使用C#开发，易于二开，且通过魔改的Donut工具避免了C#的版本兼容问题。

2.适配了System权限执行，无需手动降权执行。

3.收集浏览器信息全面，不局限于密码cookies等，可以接管插件及Local Storage。

4.配套的bof可以直接用于CobaltStrike，可以根据需求手动执行或自动执行。

**十大集权设施攻击及检测工具**

**作者：thinkerabc**

简介：攻防演练中，防守方涉及资产多，基础设施种类多，存在配置不当、历史漏洞遗留的问题。如果仅仅依靠安全防护设备进行被动的防御，往往不能够起到很好的防御效果。同样道理，对于红队来说，目标存在各种基础设施，存在的利用工具多，各种工具相对分散。由于时间紧迫，一款高效的红队攻击工具必不可少。因此，网星安全推出了十大集权设施攻击及检测工具，它能够帮助蓝队在HVV前期进行多场景的基线检测和漏洞自查，检测不合理的配置、存在的历史漏洞，也能够帮助，也能够成为红队攻击利器，因为它集成了基于集权设施的、多场景的利用工具，旨在让红队专注于漏洞利用。

**JYso**

**作者：QI4L**

简介：

1、基础链版本的覆盖，和持续更新链子；

2、利用方式的填充：添加了多种利用方式，并支持执行自定义任意代码；

3、利用链探测：本项目在 URLDNS 中添加了利用链的探测；

4、内存马：本项目在利用时，支持一键打入 Spring/Tomcat/Jetty/JBoss/Resin/Websphere 内存马功能，内存马支持命令执行、冰蝎、哥斯拉、WebSocket 四种利用方式；并支持 Tomcat 回显命令执行、Tomcat Websocket 内存马、Tomcat Executor 内存马、Tomcat Upgrade 内存马、RMI 内存马等，支持不落地的Agent写入方式；

5、MSF/CS 上线：配合远程 Jar 包一键上线 MSF/CS 的功能；

6、使用去除编译类字节码行号、Javassist 动态添加父类、接口、重写方法等多种技术缩小反序列化 payload；

7、可以同时当作ysoserial与JNDIExploit来使用；

8、支持JNDI 路由隐藏或加密与JNDI 高版本Bypass；

9、动态生成混淆的类名。

**Yawf**

**作者：yns0ng**

简介：Yawf 是一个开源的 Web 漏洞自动化检测工具，能够帮助发现一些常见 Web 漏洞，包括：XSS、SQL injection、XXE、SSRF、Directory traversal、Log4Shell 和 JSONP 敏感信息泄露等。

**侦查守卫**

**作者：三米前有蕉皮**

简介：侦查守卫是由rust语言编写服务和Web应用指纹识别工具

1. 基于yaml编写探针，匹配规则和提取器

2. 支持服务和Web应用版本识别

3. 使用nvd标准通用平台枚举 (CPE) 命名规范

4. 社区化指纹库和nmap服务探针，通过github工作流自动关联指纹和漏洞验证插件

5. 集成 Nuclei 验证漏洞

**ERH**

**作者：饭饭**

简介：智能网联汽车、手机中有大量的APK文件，APK文件之间存在着错综复杂的调用关系。创新提出通过构建可视化、可交互的调用关系分析工具。通过分析APK包之间的调用关系，生成实体关系图。通过查看箭头的流向，能够直观的看到调用关系。使用此工具已识别出车机中数十个工程模式的调用链，通过对调用发起者的逆向，成功唤起工程模式，为车机渗透提供了分析入口。

在线 DEMO 只有全局概览，下载本地运行，交互性更强。通过双击可以过滤只与特定目标相关的。

**KCon**

![](https://mmbiz.qpic.cn/mmbiz_jpg/e5by8a5GzIbLc2DypAaGP61h5XCF1W0CrrPkgt1Q0k95HoA6r5TWK3xe5QsRDXhOgJicfiaO9LLfr81Pk88rgHiaA/640?wx_fmt=jpeg&from=appmsg)

**余额告急**！

**KCon早鸟票权益仅剩1天**

**（截止至8月1日）**

早鸟8折福利即将结束

赶快登陆线上售票通道购票吧！

购票网址：

https://www.4hou.com/tickets/eERv

![](https://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIbLc2DypAaGP61h5XCF1W0CWal73yezOC9c5G583w8Yb0rEy4gl8vsU9ZutGviaLGC1bUDjkQF9KAg/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIYvJeWfDicggbpjWluw8URLyM4jux7SrsiaqupEy9mdqQOmoib3ickpxdfTEyhqwttmlX8kmX6MNxwpMw/0?wx_fmt=png)

KCon 黑客大会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/e5by8a5GzIYvJeWfDicggbpjWluw8URLyM4jux7SrsiaqupEy9mdqQOmoib3ickpxdfTEyhqwttmlX8kmX6MNxwpMw/0?wx_fmt=png)

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