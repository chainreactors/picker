---
title: 星球更新：一条 pre-auth 0day 链，从 XSS 到终端 RCE
url: https://mp.weixin.qq.com/s/R3D8BFUVxH6ph3ZW__ZZwg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:44:45.675695
---

# 星球更新：一条 pre-auth 0day 链，从 XSS 到终端 RCE

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eMTyD09PvaZ37jUzk8WuHhV5bBEK0la8diaGYovUar4vWjOrVDIn9Hez6oLru9bnMH9wPyNIbPuSBnC8VrVGVJ9ib9SLib4kX37yiaNyKcwdfKM/0?wx_fmt=jpeg)

# 星球更新：一条 pre-auth 0day 链，从 XSS 到终端 RCE

原创

whoami0002
whoami0002

SecurityPaper

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 星球更新：一条 pre-auth 0day 链，从 XSS 到终端 RCE

> 本文仅作安全技术交流，所有测试请在授权环境内进行。

---

## 开门见山

知识星球最近更新了一条**完整可用的 0day 利用链**。

目标：某主流**企业终端安全管控平台**（内网常见部署）。

特点：

•**pre-auth**，无需事先持有账号•存储型 XSS 只是入口，不是终点•最终可拿到**管理员权限**，并向**全网终端**下发指令

完整复现、脚本、请求包、截图证明——**只在星球内公开，公众号不写细节**。

---

## 为什么值得看？

企业终端管控系统，管的是整网终端的策略、补丁、分发和日志。这类 0day 的价值，不在于「又找到一个 XSS」，而在于：

**一条链跑通，从 Web 入口到终端 RCE。**

很多人测 XSS 停在弹窗；这份 Writeup 展示的是：**0day 怎么设计、怎么验证危害、怎么写到能交差的程度。**

---

## 星球里有什么？（不含公开细节）

•完整 0day 发现与验证过程•从漏洞入口 → 权限提升 → 扩大影响的**全链路**•可直接参考的脚本与调试方法•关键步骤截图与踩坑记录

**具体产品名、接口、Payload、利用细节——进星球才能看。**

---

## 适合谁？

•红队 / 渗透测试，手里有洞但不知道怎么把危害做满•主攻企业安全产品、终端管控、运维平台的攻防选手•想收藏**可复现思路**的 0day Writeup，而不只是 POC 截图•做 SRC 挖洞，需要把漏洞链写到能交报告的程度

---

## 为什么必须进星球？

**0day 不适合发公众号。**

发多了，别人分析出来，价值就没了。

星球 = 小范围更新、持续补充、可讨论：

•新 0day / 1day 案例•完整 Writeup 与脚本•同类产品的攻击面梳理

**早加入，早看到**

---

## 加入方式

👇 扫描下方二维码**，加入知识星球，获取本条 0day 完整内容** 👇

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eMTyD09PvaardibOVF9rNnFK39OCqtXs1yr5R35kLTibzSUl0ib45oxWicfg5cYK6qydM0OoCjm02nk9ctzh5PZjR65E1DoU3zibIFwpNbQU99QA/640?wx_fmt=png&from=appmsg)

---

## 免责声明

本文内容仅用于合法授权的安全测试、学术研究与防御建设。请遵守相关法律法规，**严禁对未授权目标进行攻击**。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

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