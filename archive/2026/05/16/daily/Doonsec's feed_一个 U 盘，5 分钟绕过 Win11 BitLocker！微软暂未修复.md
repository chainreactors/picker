---
title: 一个 U 盘，5 分钟绕过 Win11 BitLocker！微软暂未修复
url: https://mp.weixin.qq.com/s/W4tzMKYhgYb07y04sAd2sg
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:01.533220
---

# 一个 U 盘，5 分钟绕过 Win11 BitLocker！微软暂未修复

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aj4fOOkmqMLVEwhp9B5OG41iaz0HfCFqpsZFxWsG70IibZtsQEaCGoka68Fqb5NQDB3Oy6kb0RU7uKdHwJ39XFfVHL9CAUzCGhDW1aO4j4oOQ/0?wx_fmt=jpeg)

# 一个 U 盘，5 分钟绕过 Win11 BitLocker！微软暂未修复

原创

ralap
ralap

网络个人修炼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近，安全研究员 Nightmare-Eclipse 因对微软漏洞修复流程不满而公开了一个名为 **YellowKey的零日漏洞。该漏洞可直接穿透 Windows 11 默认配置下的 BitLocker 加密。**

其核心风险在于：攻击者只需**物理接触**你的电脑，用一个普通 U 盘和几个按键操作，就能直接解锁加密硬盘，获得系统最高权限（SYSTEM），进而读取所有数据。

**目前微软官方尚未发布任何安全公告或修复补丁。**

---

## 一、影响哪些系统？

* **受影响：** Windows 11（专业版/企业版/教育版）、Windows Server 2022 / 2025。
* **不受影响：** Windows 10 及更早版本。

---

## 二、漏洞原理

漏洞位于 Windows 恢复环境（WinRE）的一个特殊组件中。

攻击者通过一个特制的 U 盘，可以触发 WinRE 进入一个错误的执行路径。系统会误以为处于安全状态，自动调用 TPM 芯片中的解密密钥解锁硬盘，并**直接为你打开一个拥有系统最高权限的命令行窗口**。

整个过程不涉及对加密算法的“破解”，而是操作系统将解密后的硬盘直接交给了操作者。因此，研究员指出，这“不像一个漏洞，更像一个预留的后门”

---

三、操作步骤

**⚠️仅限合法用途**：以下操作**只能**用于你自己拥有合法所有权的设备。任何未经授权访问他人电脑的行为都是违法的。

1.把 FsTx 放入U 盘的：System Volume Information\FsTx

2.在目标电脑插入 YellowKey U 盘，开机按住 Shift 点重启 后，把手指从 SHIFT 键上移开，按住 CTRL，切勿松开，如果操作成功，则会自动弹出 解锁后的X:\> SYSTEM 命令行。

此时，被 BitLocker 加密的系统盘（通常为 `C:`）已处于可读写状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMIicbZU2KGxiaEnFClnqkuBsGYXdq8I0IHDApqEMzru30hk7eibDQS1RsDK8bkic91diblEbfBiazHicIRpD6VwNYeuEav4d69V5AmxHg/640?wx_fmt=png&from=appmsg)

---

个人觉得对于忘记windows登录密码又开启了bitlocker,这个漏洞刚好能作为救急的‘后门’使用。😄

**只要你的电脑一直处于你自己的物理掌控之下，YellowKey 对你而言就等于不存在**

---

参考链接

[1]https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html

[2]https://github.com/Nightmare-Eclipse/YellowKey

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

网络个人修炼

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

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