---
title: 全球警报：Lua恶意软件攻击瞄准教育行业和游戏社区！
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787006&idx=1&sn=6a1294633f133c80bcae983dec1e194c&chksm=8893ba11bfe433072580939410d1f220f03f97f3ce0bc4baa344c1e5ad825a49f74dd40f9806&scene=58&subscene=0#rd
source: 安全客
date: 2024-10-10
fetch_date: 2025-10-06T18:53:44.257475
---

# 全球警报：Lua恶意软件攻击瞄准教育行业和游戏社区！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5ezFdRfvMys0CEXx2uXib6mvGeic4U1xw4Rtlpf484wO3s1DiaVJeswLqLIAOOEBPJq7ydkSFoZDDKg/0?wx_fmt=jpeg)

# 全球警报：Lua恶意软件攻击瞄准教育行业和游戏社区！

安全客

近期，Morphisec Threat Labs揭示了一场针对教育行业和游戏社区的新型恶意软件攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5ezFdRfvMys0CEXx2uXib6mxhkn1u445an7DfAElMEKibiaH1j6tZOP7UIrUszrGvsib2G0CzTcAxdXA/640?wx_fmt=jpeg&from=appmsg)

安全研究员Shmuel Uzan指出，这些复杂的恶意软件变种利用Lua这一广泛应用于游戏开发的脚本语言，通过GitHub等平台渗透系统。此次活动在全球范围内产生了影响，北美、南美、欧洲、亚洲和澳大利亚均报告了感染案例。

这种恶意软件的兴起与Lua的普及有关，尤其是在使用Roblox等游戏引擎的学生玩家中。报告指出，“用户在寻找游戏作弊工具时，常常会下载来自GitHub等类似平台的文件。”攻击者借此机会在看似无害的下载文件中嵌入恶意Lua脚本，从而侵入用户系统。

恶意软件通常通过ZIP压缩包传递，其中包含多个组件，包括Lua编译器、Lua DLL文件、混淆的Lua脚本和批处理文件。这些组件协同工作，一旦在受害者的计算机上安装并执行，将进行恶意操作。执行后，Lua脚本会与指挥和控制（C2）服务器建立通信，发送有关被感染系统的详细信息。

一旦恶意软件激活，C2服务器会向受感染机器提供指令，这些指令分为两种类型的任务：Lua 加载程序任务和任务有效负载。Lua加载程序任务负责保持持久性和隐藏进程，而任务负载则专注于下载其他恶意软件负载或应用新配置。报告解释道，“Lua加载器任务涉及保持持久性或隐藏进程的操作”，而负载旨在扩展恶意软件的功能。

为了逃避检测，Lua脚本使用Prometheus混淆器进行了混淆，该工具旨在保护底层代码不被逆向工程。这种程度的混淆使安全研究人员很难分析和理解恶意软件的全部功能。Uzan在报告中指出，“脚本经过Prometheus混淆器混淆后，使得研究人员分析和理解代码的难度显著增加。”

此外，为了防止研究人员反向分析或重新格式化代码，恶意软件还采用了独特的反逆向技术，当尝试美化混淆代码时会触发错误信息。该混淆器的功能包括通过检查执行过程中生成的错误消息的行号，检测代码是否被篡改。如果代码被修改，恶意软件将终止，并显示信息：“检测到篡改！”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb5ezFdRfvMys0CEXx2uXib6m0MqiaZqJdbweb74LJFexz5tBhPHjSibEhO1UECaQ4VaiaAyxuWf7BYKUQ/640?wx_fmt=jpeg&from=appmsg)

除了混淆，恶意软件还利用Lua的ffi（外部函数接口）库直接执行C代码。这种技术允许攻击者调用C函数并使用C数据结构，而无需编写C包装代码。这种Lua与C的集成增强了恶意软件操控系统级进程和执行更高级攻击的能力。

一旦恶意软件渗透到受害者的系统中，它通过创建定时任务和生成随机任务名称来保持持久性。恶意软件还会收集关于受害者计算机的广泛信息，包括用户的GUID、计算机名称、操作系统和网络详细信息，甚至会捕获被感染系统的屏幕截图，并将这些数据发送至攻击者的C2服务器。

报告强调，“脚本检索MachineGuid…并将收集到的数据连同屏幕截图发送给攻击者的C2。”这种数据收集的深度使得攻击者对被感染机器有了全面的了解，从而能够更有效地定制后续攻击。

一旦恶意软件成功收集所需数据，C2服务器将以被阻止消息或JSON响应的形式作出回应，提供进一步的执行任务或下载额外负载的指令。如果服务器响应被阻止，恶意软件将尝试从备用位置（如pastebin.com）检索新的地址，以确保与攻击者的持续通信。

该恶意软件传递的负载包括Redline Infostealers，这是一种用于收集受害者凭证和敏感信息的恶意软件。报告指出，Redline在网络犯罪领域的知名度日益上升，因为它能够窃取有价值的数据，随后被出售至暗网。Uzan警告道：“从这些攻击中收集的凭证将被出售给更复杂的团伙，以用于后续攻击阶段。”

文章来源：

https://securityonline.info/global-malware-campaign-exploits-lua-in-gaming-and-education-sectors/

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5ezFdRfvMys0CEXx2uXib6me2WzYl6dtAzxZayIFv9kSicTlwYJStoQEck24EMxxc9ppmOwMrssZEw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb5ezFdRfvMys0CEXx2uXib6mG0QBhTxYZxRkwWibia9Wwh9ZcVXBAaMn0iczsGx4jib6XaMnrr3OAf1L0g/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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