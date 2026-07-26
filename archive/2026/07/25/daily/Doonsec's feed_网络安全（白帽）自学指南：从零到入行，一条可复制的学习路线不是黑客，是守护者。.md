---
title: 网络安全（白帽）自学指南：从零到入行，一条可复制的学习路线不是黑客，是守护者。
url: https://mp.weixin.qq.com/s/RZZ1fhjBcUzS-2bl6nrADg
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:21:50.785282
---

# 网络安全（白帽）自学指南：从零到入行，一条可复制的学习路线不是黑客，是守护者。

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8cylv3yeUGag0zC2sdVFoBjtAnD16qicWtIGe8bu5L2HBiayuujpvliabRyCcsYviapG94DxOIXkUPk5nw4SBegO905YibELlyibEOialqkQV00Dzk/0?wx_fmt=jpeg)

# 网络安全（白帽）自学指南：从零到入行，一条可复制的学习路线不是黑客，是守护者。

龙哥网络安全
龙哥网络安全

龙哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多人对“网络安全”的印象，还停留在电影里戴着兜帽敲键盘、黑进系统的画面。但现实中的白帽黑客，更像是数字世界的医生、锁匠和保镖——他们用技术发现问题、修补漏洞，保护数据和系统安全。

如果你正考虑自学网络安全，却不知从何下手，这篇指南就是为你准备的。我会尽量把路径拆细，把资源说清，让你少走弯路。

一、先摆正心态：自学网络安全，这几点想清楚

在点开第一个教学视频之前，先把基础认知对齐。

· 这是一条长路，不是捷径。安全是计算机领域的交叉学科，需要扎实的底层功底。速成几乎不可能，但每一步都算数。

· 合法合规是底线。一切练习必须在授权环境下进行，别碰任何未授权的目标。守护者首先要遵守规则。

· 自学非常依赖动手。“看懂了”和“会做了”之间隔着无数次实验和报错。准备好一台能折腾的电脑，80%的时间都应该花在实操上。

· 英语和搜索能力是隐形必修课。最新的技术文档、漏洞报告大多是英文的，遇到问题要学会用精准的关键词检索。

二、自学路线图：六个阶段，稳步进阶

我把学习路径拆成六个阶段，每个阶段都给出了核心知识点、推荐资源和实践任务。你可以按部就班，也可以根据已有基础跳跃进行。

阶段1：基础IT素养（1-2个月）

没有这个底座，后面的安全技能都悬在空中。

核心内容：

· 计算机基础：二进制、内存、进程/线程

· 操作系统：Windows和Linux的日常操作、用户管理、权限、服务、进程查看

· 网络基础：OSI模型、TCP/IP协议栈、IP地址与子网划分、常见端口、HTTP/HTTPS、DNS

· 虚拟机使用：VMware或VirtualBox，学会搭建实验环境

推荐资源：

· 书籍：《计算机网络：自顶向下方法》《鸟哥的Linux私房菜》

· 视频：B站搜索“计算机网络微课堂”“韩顺平Linux”

· 动手：在自己电脑上装一个Ubuntu虚拟机，日常使用它一个月，强迫自己脱离纯图形界面

检验标准：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7cdvXdMEFuM0FCWcycNVpmUKPNU5jiaXNViarONgIYFZuu3WcYY9be9vKNhf6OnOGloAaHGgXia0UzibpbTtm5JfPufWx8z8YZZNSUIqLT9LH7U/640?wx_fmt=jpeg&from=appmsg)能说出打开一个网页的全过程（DNS→TCP→HTTP→渲染）；能在Linux下用命令行完成文件操作、安装软件、查看网络状态。

阶段2：编程与脚本能力（持续进行）

不必成为开发高手，但必须能读懂代码，能写自动化脚本。

重点语言：

· Python：首选，写扫描器、自动化漏洞利用、数据处理都靠它。重点掌握网络编程（socket、requests库）、字符串处理、文件读写。

· Bash/Shell：Linux下批量操作、日志分析、环境部署必备。

· C语言基础：理解内存管理、指针、缓冲区溢出原理，了解就好，不必精通。

· PHP/JavaScript基础：做Web安全时，必须能看懂后端和前端的代码逻辑。

推荐资源：

· Python：《Python编程：从入门到实践》

· 练习：用Python写一个端口扫描器，写一个简单的HTTP请求发送工具

阶段3：网络安全通识与基础攻防（2-3个月）

开始接触“安全”本身，建立攻防思维。

核心内容：

· 常见攻击类型：SQL注入、XSS、CSRF、文件上传漏洞、命令注入、暴力破解

· 渗透测试流程：信息收集、漏洞扫描、漏洞利用、权限提升、后渗透、报告编写

· 安全工具初识：Burp Suite（抓包改包）、Nmap（端口扫描）、Wireshark（流量分析）、Sqlmap、Metasploit基础

推荐资源：

· 靶场平台：DVWA（必装，低门槛漏洞练习）、sqli-labs（专练SQL注入）、Upload-labs（专练文件上传）

· 教程：B站“小迪安全”的入门课程、Youtube“HackerSploit”系列

· 必读：OWASP Top 10，了解最关键的Web风险

学习方式：

在虚拟机里搭靶场，用工具和手工结合的方式逐个击破漏洞。每做完一种漏洞，尝试自己总结利用条件、检测方法和修复方案。

阶段4：纵深方向切入（选择你的第一专长）

安全领域很宽，先从一个方向深入，再横向扩展。以下是最常见的入门方向。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7cdvXdMEFuNP8YXYh2E6EExmDg6ASrWatzTItFbLPtrkU474qUUJYr3evQaicHU881JUBRUjnIRDYQricssENS0q6icX9aeOgbNf2OPx4nkWB0/640?wx_fmt=jpeg&from=appmsg)方向A：Web安全（渗透测试）

· 深入HTTP协议、各种Web中间件（Tomcat、Nginx、IIS）特性

· 逻辑漏洞挖掘：越权、支付篡改、验证码绕过等

· 进阶工具：Burp Suite高级用法、Xray、Nuclei、自定义脚本

· 靶场：PortSwigger Web Security Academy（免费且高质量）、Vulhub（一键部署漏洞环境）

方向B：二进制安全（逆向/漏洞利用）

· 需要较深的C/C++/汇编功底

· 调试工具：GDB、WinDbg、x64dbg、IDA Pro、Ghidra

· 学习栈溢出、堆利用、格式化字符串漏洞

· 入门平台：Microcorruption（嵌入式固件逆向）、ROP Emporium

方向C：网络与内网安全

· 内网信息收集、横向移动、域渗透

· 工具：Mimikatz、Cobalt Strike（仅限授权测试）、BloodHound

· 搭建域环境自行练习

方向D：安全开发与自动化

· 写自己的扫描器、POC验证框架

· 掌握Docker，用于快速搭建环境和部署工具

· 学习代码审计思路，使用Semgrep、CodeQL等辅助工具

阶段5：实战升级——打靶场、挖SRC、做项目

脱离纯理论，向真实环境靠拢。

1. 综合靶场

· HackTheBox (HTB)：环境最全，难度递增，社区活跃

· TryHackMe (THM)：新手友好，学习路径清晰，有引导式房间

· VulnHub：下载虚拟机镜像直接打，适合零成本练习

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7cdvXdMEFuPN9tTpdjicGsHqAOs6hw76J7wz69UZUFUiaJ8eWUictic4XFNhaxltALPpXrDH7kWNfmUMHmH7NpicGhyUnEUDEib5vhc11ibCELmk1o/640?wx_fmt=jpeg&from=appmsg)2. 漏洞响应平台（SRC）

当你有了一定能力，可以尝试在合法平台提交漏洞：

 补天、漏洞盒子、各大企业自有SRC（腾讯、阿里、百度等）

· 从边缘业务、低危漏洞开始找，感受真实系统的复杂度

· 注意：初期受挫是常态，重点是阅读别人的公开漏洞报告，学习思维

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/7cdvXdMEFuPLAgKOvTOLr9CnCapiaMJIr36Z5vZ6kvufGLDSZ7RHt0iaocR7wqWavnnHLrJ3atjo97niaE0TsB7JmcMgxJyQlq6NvK9mFkfOpI/640?wx_fmt=jpeg&from=appmsg)3. 搭建个人实验室

用家里的旧电脑或云服务器，搭一套包含Web应用、数据库、内网多台机器的环境，自己从外网打穿到内网。

阶段6：持续学习与圈内成长

安全知识更新极快，自学是终身的事。

· 关注信息源：FreeBuf、安全客、先知社区、Twitter上的安全研究员、各大安全厂商的博客

· 参加CTF：从新生赛、线上赛开始，以赛代练，结识同伴

· 复现漏洞：紧盯最新公开的高危漏洞（如各种RCE、反序列化漏洞），在本地搭建环境复现一遍，这是能力跃升的捷径

· 输出倒逼输入：写技术博客，在安全社区分享，哪怕只是个人笔记，也能在整理中固化知识

三、自学资源工具箱（精选，够用）

书籍（按阶段看）：

· 入门：《白帽子讲Web安全》《Web安全攻防：渗透测试实战指南》

· 内网：《内网安全攻防：渗透测试实战指南》

· 二进制：《0day安全：软件漏洞分析技术》《加密与解密》

· 代码审计：《代码审计：企业级Web代码安全架构》

在线平台：

· 系统性学习：PortSwigger Web Security Academy、TryHackMe

· 实战靶场：HackTheBox、VulnHub、PentesterLab

· 练习单项：Root-Me、OverTheWire（带游戏性质的Linux基础闯关）

必备工具清单（慢慢装，用啥学啥）：

· 环境：VMware/VirtualBox、Kali Linux

· 抓包：Burp Suite Community、Wireshark

· 扫描：Nmap、Nessus（社区版）、Nikto

· 注入测试：Sqlmap

· 漏洞利用框架：Metasploit

· Python库：requests, pwntools, scapy

四、关于求职：从自学到拿到Offer

如果你志在以此为职业，这些建议或许能帮到你。

作品集比简历更会说话：

. 维护一个技术博客，详细记录攻克过的靶场、复现过的漏洞、自己写的工具

· GitHub保持活跃，哪怕是小工具、学习笔记，也能体现持续学习的习惯

· 参与SRC并提交有效漏洞，哪怕等级不高，也是一线实战证明

证书的实际作用：

证书是加分项，不是敲门砖。初入行时，CISP-PTE（偏实操渗透）或OSCP（国际认可度高，难度大费用高）能证明动手能力。理论类如CISP/CISSP更适合后期晋升。

城市与圈层：

安全岗位集中在一线及新一线城市。多参加线下的安全沙龙、会议（如KCon、看雪峰会），内推往往比海投高效得多。

五、写在最后：保持敬畏，享受破壳的乐趣

自学网络安全，你会经历无数个“为什么不行”的深夜，也会在弹出Shell的那一刻激动到握拳。这条路不轻松，但它给你的回报，不只是技能和薪资，更是一种看待数字世界的深邃视角。

你会开始注意每一个输入框，会思考一个链接背后的跳转逻辑，会对隐私和数据产生近乎本能的敏感。这是这个领域给你的馈赠。

想，都是问题；做，才是答案。

现在就建个虚拟机，装上DVWA，开启你的第一次“合法入侵”吧。

如果你觉得这篇指南有帮助，欢迎分享给同样在自学路上的伙伴。有问题也可以留言，我们会尽力解答。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8cylv3yeUGba71jyNZOROicD2iaG1usnv8rWclnlekQKw5jaNLiaQdIB5uevVuAgMbxHqOGz3BaoNzvm88s5mgKlaw4s2L4mLoaEcChAw6Gosk/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7O8nPRxfRT7NHG7rzgsoLIZoUNftOgFkUvw7cg5pYj1cC5HG9Au30Xd3tbUySlm1gsrt7B2sehicBlb3mFmNLFw/0?wx_fmt=png)

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