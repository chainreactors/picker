---
title: BugHunter-AI：智能自动化渗透测试助手
url: https://mp.weixin.qq.com/s/LQ_Cig0jY3kRu1FEwhJvUg
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:03:37.978175
---

# BugHunter-AI：智能自动化渗透测试助手

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJxJ2MCvcpFxiaCeQNluGZTWEZQ9R2MhSbwQHkXYYJibBB7Y4XQyzaqoAvhgktpuwsJKibz3p8jTS1N371U5AlicI0Ia0b4HtDafxs/0?wx_fmt=jpeg)

# BugHunter-AI：智能自动化渗透测试助手

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Hack Scanner --自动化黑白盒扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487782&idx=1&sn=46b4c0dd663f3dc334bd08c72fdc131a&scene=21#wechat_redirect)

·[Firefox‑Reverse：网页版AI自动化逆向算法工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487775&idx=1&sn=fae88a160aa85ae5e0a4cd6e4bb4c95e&scene=21#wechat_redirect)

·[K8sPenTool：一款面向Kubernetes集群的综合渗透测试评估平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487757&idx=1&sn=34e2084e5d8e8dee47faddcffb2d3c61&scene=21#wechat_redirect)

·[CTF²: 推荐一个比较全面的CTF靶场](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487722&idx=1&sn=f12056918c209179a318d1f904d05210&scene=21#wechat_redirect)

·[Bug Hunter：一个代码安全审计的skills](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487714&idx=1&sn=b02dcacd5efb02443bd0a213b80ef99e&scene=21#wechat_redirect)

·[NextWQ：一款QQ小程序安全测试分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487701&idx=1&sn=91f799ebe8d87bb92f33a04230e5814c&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJ2q1iaXClIugLruBAYWwnflaHjgxOQgVhBu0Jeg2QvyrOPO9gmT4fl1BVfMtldYYAeQzAEwiaKcLudsDKek7dBTJ39tibyn6AL6s/640?wx_fmt=png&from=appmsg)

    BugHunter-AI 是一款面向安全测试人员的自动化渗透测试代理工具，它将传统的漏洞扫描与前沿的 AI 技术深度融合。

    工具内置了资源感知型任务队列系统，能够根据主机的 CPU 和内存使用情况智能调度测试工具的并发执行，避免因资源耗尽导致系统卡顿或测试中断。其 Tkinter 构建的图形界面采用“赛博朋克”视觉风格，集成了资源监控面板、任务队列管理器和实时控制台，让测试人员能够直观地掌控每一次扫描的进度与状态。

    无论是 NMAP 端口扫描、SQLMap 注入检测，还是 Nikto 网页服务器扫描，BugHunter-AI 都能以轮次为单位有序调度，并自动生成结构化的报告供后续分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**工具获取**

GitHub地址：

```
https://github.com/ARESHAmohanad/BugHunter-AI
```

    下载并快速启动：

    克隆项目：

```
git clone https://github.com/ARESHAmohanad/BugHunter-AIcd BugHunter-AI
```

    安装环境：

```
python3 install_dependencies.py
```

启动：

```
python3 AIlinuxV2.py
```

即可在弹出的窗口中启动该项目，可以开始使用：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLuzUIu5MqgtNY29BE0QAU2AGTKBCtkeVPxahbJllOmNngJI7hk0ffjBRUwb4LmBA9kibRLeFGtfwwar3Pul3E9dVB2PLe6jYt0/640?wx_fmt=png&from=appmsg)

配置api：

在AIlinuxV2.py 文件的第 24-31 行，可以根据自己使用的模型更换api：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIic5CGY4uUS20ScYdIPiaibqXtrJUBSa8rcvdKYxhibjmLcLIw8mO5IuRvKibRLFNRNG5XEo3ibO22E1SJzcNjEOia7RC7FNPRBgJcwM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**功能介绍**

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicLdAiaPyceQbMNTwnCdsX9zkBNmI47tfqKuZmXCFbiabtapXdxBBxZlvtT2ejacLzicyI7BKTs4FliaaCaSncefic7xEGl9qIiaOMPlQ/640?wx_fmt=png&from=appmsg)

    根据打开的界面，可以看到左侧有四个模块：

1.最上面的是Target 输入框，输入目标 IP 或域名

2.第二个是扫描操作，开始，停止，和导出结果

3.第三个是相关设置，同时运行的最大工具数（1-3）、CPU 使用率阈值、内存使用率阈值，都支持手动调节

4.第四个是工具选择复选框，按 5 个类别分组勾选要使用的工具

    右侧面板是监控区：

1.最上面是资源监控器，实时显示 CPU 和 RAM 使用率

2.然后是工具执行队列，显示 ⚡运行中 / 📋排队中 / ✅已完成 / ❌失败 的工具

3.神经控制台，彩色日志输出，显示扫描过程中的所有信息

4.扫描指标，显示当前轮次、工具数量、发现的 CVE、状态

    在Target输入框中输入想要扫描的目标IP或者域名后点击INITIATE SCAN 按钮就可以开始扫描了：

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicK6R7YdoM0Fpw8EBOOfSia8dnIe0NuhMWPDSCnl1cAvIDLucyRGX8TSS8AGwyuR2MGoXlZurNfE883ITPNOasK6NGBd7G1ZunTY/640?wx_fmt=png&from=appmsg)

    工具选择：

```
侦察（RECON）：nmap, masscan, amass, sublist3r, theHarvester, whatweb, wafw00f 等枚举（ENUM）：enum4linux, nbtscan, smbclient, crackmapexec 等目录枚举（DIR_ENUM）：dirb, dirsearch, ffuf, gobuster, wfuzz漏洞扫描（VULN）：nikto, wpscan, sqlmap, nuclei, xsser 等漏洞利用（EXPLOIT）：hydra, medusa, john, metasploit, searchsploit 等
```

    开始扫描后平台将自动进行最多 5 轮扫描：

```
第 1 轮：执行你勾选的所有工具，资源感知队列管理器会自动调度结果汇总：每轮结束后合并所有工具输出为 report.jsonAI 分析：将报告发送给 AI，AI 返回下一轮要执行的命令和工具CVE 提取：自动从报告中提取 CVE 编号重复：直到 AI 决定停止或达到 5 轮上限
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**交流群**

我们创建了交流群，一起来交流吧！！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicIVPcMibxohRr7OrSVKrSGbEy8XKJHJKYqHzgWxPH8hWNu6nG7VRahUho2hSMZCghm2mH0DWHe6SDb8uoKfcicr51xt02fB19Mew/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicJVRBMdib7K3ZtqZv8Yl8uRmgwoJjcDRPibW9TfdiaaibJnTboUxTXo5C0iacxMHS0JnjVbGextpYnIfUquG9E3icJmibOWcPSVNJOOIk/0?wx_fmt=png)

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