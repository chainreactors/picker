---
title: Linux内核曝KVM高危漏洞，ARM64客户机可直接读写主机内存
url: https://mp.weixin.qq.com/s/NCFX8oJd47HnOTKvCgdIRQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:25.279799
---

# Linux内核曝KVM高危漏洞，ARM64客户机可直接读写主机内存

# Linux内核曝KVM高危漏洞，ARM64客户机可直接读写主机内存

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX2YOkAaCADNBNXWJiclibKg0yQTTTWdBP8pKjtOvsZoZxx8Z2OaCq4rYIlic9pELedibBFzRQdiaiad5tPiauULjSqVM4Qb1iaib9ywOBSE/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3icic73AfhptFnXQ8QWNP3WBqDExU4eTU9ibrYEyB3tdMg9K4ogGVeD7qk0CZrLfUic2GIrpWmxO6WefZxiaeoC0lffFq82SNcwKGA/640?wx_fmt=png)

研究人员近期披露一个编号为CVE-2026-89775的Linux内核漏洞，攻击者可利用该漏洞从ARM64虚拟机逃逸，直接访问底层宿主机系统。

该漏洞仅影响开启嵌套虚拟化功能的KVM/arm64环境，会对多租户云基础设施、允许非受信用户创建虚拟机的系统造成严重安全风险。

Part01

页表遍历存在类型截断

安全研究员Hyunwoo Kim指出，该漏洞源于KVM/arm64第一阶段页表遍历流程中的类型截断问题。该问题会干扰内核的内存区域大小计算逻辑，内核需要依据计算结果，将对应内存从虚拟CPU的伪TLB中失效。

正常流程下，内存映射发生变更后，KVM必须失效过期的内存转译条目，防止客户虚拟机继续访问宿主机内核已释放、移动或重新分配的内存。

但在存在漏洞的代码路径中，相关大小计算可能返回0值，该值原本的设计含义是内存大小未知。

VNCR伪TLB失效逻辑会错误将0值识别为有效的范围大小，进而生成空的失效范围。这会导致系统完全跳过必要的失效操作，最终让恶意客户机持续持有过期内存的访问权限。

Part02

攻击者可直接读写宿主机内存

根据漏洞披露信息，已释放的宿主机内存页可能仍映射在宿主机内核的固定地址，且保持可写权限。恶意客户机无需触发陷阱或虚拟机退出，就能获得该内存页的64位读写权限。攻击者可直接从客户机环境内部操纵宿主机内存。

该漏洞对采用ARM64基础设施的公有云部署威胁尤其突出。如果攻击者可以创建开启嵌套虚拟化功能的实例，就有可能从客户机系统渗透进入宿主机。

一旦攻击得手，攻击者会彻底打破客户虚拟机与云厂商底层基础设施之间的隔离边界。

该漏洞还可能引发本地提权风险。漏洞报告指出，包括Red Hat Enterprise Linux在内的部分发行版在某些配置下，会将/dev/kvm的权限设为0666，即全局可写。在开启嵌套虚拟化的前提下，本地无特权用户可利用该漏洞获取宿主机的root权限。

Part03

上游已发布漏洞修复补丁

2025年5月14日提交的commit 7270cc9157f47将该漏洞引入Linux内核代码，2026年8月6日上游提交的commit 8053393680d4已完成修复，目前Linux主线内核已集成该补丁。

管理员应在发行版厂商推送包含主线修复的内核版本后，第一时间完成升级。

运营ARM64 KVM主机的机构也应评估嵌套虚拟化功能的必要性。在补丁部署完成前，关闭非必要的嵌套虚拟化功能可以缩小攻击暴露面。

云服务厂商应优先修补共享基础设施，评估租户对嵌套虚拟化功能的访问权限。同时需要核查/dev/kvm的权限配置，降低本地攻击风险。

参考来源：

Linux KVM/arm64 Vulnerability Lets Attackers Escape Virtual Machines and Gain Host Access

https://cybersecuritynews.com/linux-kvm-arm64-vulnerability/

###

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