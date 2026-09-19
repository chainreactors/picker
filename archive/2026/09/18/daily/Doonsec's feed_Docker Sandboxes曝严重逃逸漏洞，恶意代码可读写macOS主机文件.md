---
title: Docker Sandboxes曝严重逃逸漏洞，恶意代码可读写macOS主机文件
url: https://mp.weixin.qq.com/s/ok6WTTCgN2L3QPgsvmQVDg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:53:20.029838
---

# Docker Sandboxes曝严重逃逸漏洞，恶意代码可读写macOS主机文件

# Docker Sandboxes曝严重逃逸漏洞，恶意代码可读写macOS主机文件

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3hAyzB5e5CDicV8kLdebzN1xpMJAiag4kAhrDlWsxTMYv89tdLJStNvhH3aIqyW5NEt6GCv7yDc9tFPU6s9rK6iavN2w36ib8qNA4/640?wx_fmt=gif)

![Docker Sandboxes漏洞示意图](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1TC5dxMPBIMgKqwls7pIMTUxLsuYoubAIQicaNRdaibohiaS03movAtTd5aOonc345DETKiaz0rwAY4Pjc1E9HFluNtcV5YTzlYyk/640?wx_fmt=png)

Part01

沙箱隔离存在缺陷

9月15日，Docker发布安全公告称，macOS平台上运行的Docker Sandboxes虚拟机内若存在恶意代码，可逃逸至已共享的项目目录之外，读取或修改主机上任意位置的文件。

这类逃逸行为的权限，与运行该虚拟机的主机账户权限完全一致。该漏洞编号为CVE-2026-77179，Docker将其评级为严重，影响macOS平台0.28.0及以上、0.42.0以下版本，Docker已于9月7日发布的0.42.0版本中修复该漏洞。

Docker Sandboxes会为每个AI coding Agent分配独立的轻量虚拟机，仅将项目目录共享至虚拟机内部。可触发逃逸的代码包括虚拟机内运行的任意程序，比如被诱导背叛用户的coding Agent，或是Agent安装运行的恶意程序。

Docker目前未监测到任何在野利用案例。CISA在CVE条目中补充的评估信息显示，目前暂无该漏洞的在野利用记录；截至9月16日发布的KEV目录版本，CISA也未将该漏洞纳入已知被利用漏洞目录。

该漏洞的触发前提是沙箱内部存在恶意代码，而沙箱的核心作用就是保护主机不受Agent运行内容的影响。Agent会在虚拟机内安装软件包、使用sudo执行命令，Docker的隔离文档明确说明，虚拟机监控程序边界“才是隔离控制的边界，而非虚拟机内部的权限分离机制”。

Docker表示，逃逸路径存在于virtio-fs主机服务端——也就是Mac与虚拟机之间文件共享功能的主机侧组件，该组件在通过存储路径重新打开已被删除的文件时，会跟随符号链接跳转。

Docker表示，Guest（即虚拟机内运行的任意程序）可将父目录替换为符号链接，随后以VMM用户（即运行虚拟机监控器的主机账户）身份读取或修改文件，“可能导致主机上的代码执行”。

Docker自3月起就在文档中说明，系统不会跟随指向工作区（Docker对共享项目目录的称呼）外部的符号链接。

本次版本更新还修复了第二个漏洞CVE-2026-79994，Docker将其评级为高危，CVSS评分为8.7。该漏洞存在于中继组件中，这类组件的作用是允许沙箱连接授权工作区内的Unix域套接字。

Docker表示，该中继组件会先校验套接字路径是否位于工作区内，再通过路径名重新建立连接。如果Guest在校验完成到建立连接的间隙，将路径上的某个目录替换为符号链接，就能让主机连接到工作区外的任意AF\_UNIX套接字，“导致该套接字提供的数据或主机侧能力暴露”。

该漏洞影响0.37.0至0.41.9版本，0.42.0版本不受影响。Docker明确标注第一个漏洞仅影响macOS平台，但未说明第二个漏洞的影响平台；目前Docker Sandboxes可运行在macOS、Windows、Linux三类主机上。CISA对第二个漏洞的评估同样显示暂无在野利用记录，该漏洞也未被纳入KEV目录。

Part02

官方给出具体升级与缓解方案

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3lEtml9uDiaiadPicrMQF8ILaT1WulAklVe2TKH7jcicgASqWMFv2PzEBJV4CzmiavkzYt6cfXn9K0sAJ4FbujQXfRVjEHBq0v4ibcM/640?wx_fmt=png&from=appmsg)

针对两个漏洞，Docker给出了统一的修复建议：

升级至0.42.0及以上版本。截至9月17日，最新正式版本为9月15日发布的0.43.0。

若暂时无法完成升级，可使用克隆模式，避免添加具备读写权限的主机挂载。

默认情况下，sbx run命令会以读写权限将当前目录共享至沙箱。克隆模式仅支持Git仓库项目，且需要在创建沙箱时设置，因此已创建的沙箱需要删除，再添加--clone参数重新创建。

Docker文档说明，克隆模式仅能防止仓库文件被修改，无法阻止文件被读取。采用该模式时，系统会将仓库以只读模式挂载到/run/sandbox/source路径，.env等未被Git跟踪的文件在沙箱内仍可被读取。

Part03

补丁发布8天后披露公告

Docker于9月15日发布CVE记录与安全公告，距离0.42.0版本正式发布间隔8天。

截至9月17日，GitHub与Docker文档站点上的0.42.0版本发布说明，均未提及上述两个CVE编号。在常规修复条目中，有一条提到“修复了沙箱内进程可诱导守护进程打开主机D-Bus传输通道、在主机上执行任意命令的问题”，Docker并未说明该修复对应哪一个CVE。

CVE-2026-79994的最初记录曾标注0.41.0为首个修复版本，还附上了不存在的0.41.0版本发布页面链接。9月15日记录发布约1小时后，Docker将两处错误信息更正为0.42.0。

Docker在公告中致谢了漏洞发现者：CVE-2026-77179由accomplish.ai的Oren Yomtov发现，CVE-2026-79994由ThreatNotify的Jurre van Bergen发现。

今年4月，Cyera Research Labs曾披露同类风险：基于Docker的沙箱内运行的coding Agent若遭提示注入攻击，可能被诱导利用Docker Engine的独立漏洞攻击主机。

参考来源：

Critical Docker Sandboxes Flaw Lets Malicious Guest Code Read and Modify macOS Host Files

https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0XsTyO4SuMuGUvEh6HBoZLXPa9xnn1UsveAZRjUSfAKwT77dFfrwAPbRgSe6l66sYOBiaFSfWMn3DL4IfDrDmexoxCYLftaleo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651346509&idx=1&sn=71e02ef8b6a2ed67fdc94aa19b152171&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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