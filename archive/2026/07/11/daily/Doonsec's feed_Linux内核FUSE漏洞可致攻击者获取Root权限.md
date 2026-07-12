---
title: Linux内核FUSE漏洞可致攻击者获取Root权限
url: https://mp.weixin.qq.com/s/V5d0xAb4WC_nWXIidIexfQ
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:38.664353
---

# Linux内核FUSE漏洞可致攻击者获取Root权限

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0acTfgT4qtZicJ7kgfzwnulRpOjl418bUKpibNEkLhX0PIj5QN58iaDhqjhbeFLmZn0yOrVnl5P54zgop8sPDZToKhV8ibcDibhic0g/0?wx_fmt=jpeg)

# Linux内核FUSE漏洞可致攻击者获取Root权限

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX14lHoEzOLlubEgic9JDPT1zP943iaYsiar8VibYUGvsf8v0UuhxaxpN4iaODPe8gEuBibGob4xfawlT7G6mEqwclJ9neTdtnmTXZ1hY/640?wx_fmt=gif)

![Linux内核FUSE漏洞配图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX06UqSoicU5oVpBBqwqzgveBarlwFxLyn2xgWWdibYwpTZRXC4fAkcibuJxKCH32enVsahMtsKIfppaHATdnpRziabkJGic1RgyDv3E/640?wx_fmt=jpeg)

Linux内核FUSE（用户空间文件系统）子系统存在一处漏洞，本地攻击者可利用该漏洞，通过用攻击者控制的目录条目填满页缓存，从而获取root权限。

Part01

漏洞概述

该漏洞编号为CVE-2026-31694，影响内核缓存FUSE readdir结果时所使用的代码路径。FUSE允许用户空间文件系统通过/dev/fuse与内核通信，内核可缓存目录条目以加速后续读取操作。

Bynario的分析显示，漏洞位于fuse\_add\_dirent\_to\_cache()函数中。该函数根据服务器提供的文件名长度计算目录条目大小，然后将条目复制到单个缓存页面中，但并未事先检查该条目本身是否大于一个页面的大小。

问题的关键在于，恶意FUSE服务器可以返回一个序列化大小为4120字节的目录条目（在4KiB页面大小的系统上），这比单个页面多出24字节。当内核将偏移量重置为零并强行复制该记录时，额外的字节会溢出到下一个内存页面中。危险之处不仅在于内存损坏，更在于被破坏数据的具体位置。

Part02

漏洞技术细节

在已报告的验证中，攻击者利用该溢出破坏SUID二进制文件（例如/usr/bin/su）中的缓存字节，将可执行代码的开头替换为一个简短payload，该payload在正常流程继续前调用setuid(0)和setgid(0)。一旦这些身份更改系统调用在root所属的程序中成功执行，攻击者便可绕过常规身份验证检查，生成一个root shell。

Part03

攻击场景与影响

该攻击为本地攻击，因此攻击者需要具备挂载或运行FUSE文件系统的能力——这通常可通过无特权用户命名空间或fusermount3实现。据Bynario称，此漏洞可在具有较大readdir缓冲区的新内核上利用，且仅影响使用4KiB内存页面的系统。使用更大页面大小的系统不受此特定溢出大小的影响。

Part04

修复与缓解措施

修复方法很简单：在缓存任何目录条目之前，拒绝那些超出单个页面大小的条目。管理员还可以通过限制FUSE的使用、在不需要时移除fusermount3的setuid位，以及适当限制无特权命名空间来降低暴露风险。

参考来源：

Linux Kernel FUSE Vulnerability Lets Attackers Gain Root Privileges

https://cybersecuritynews.com/linux-kernel-fuse-vulnerability/

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

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