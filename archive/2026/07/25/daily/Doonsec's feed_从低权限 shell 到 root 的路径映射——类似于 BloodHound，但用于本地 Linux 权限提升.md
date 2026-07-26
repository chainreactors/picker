---
title: 从低权限 shell 到 root 的路径映射——类似于 BloodHound，但用于本地 Linux 权限提升
url: https://mp.weixin.qq.com/s/cPvMrDQ1HUMpDe9Nj65Qog
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:21:24.313676
---

# 从低权限 shell 到 root 的路径映射——类似于 BloodHound，但用于本地 Linux 权限提升

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FbUo3a25icyIwttEzZFWWr9234UOicyRRy8cUeghPMZXiaTH5yBA7UmzYSicrYrtjvdSJTfib6ibvyxbLVB5V8cet5Ae6mLExM08KWQ/0?wx_fmt=jpeg)

# 从低权限 shell 到 root 的路径映射——类似于 BloodHound，但用于本地 Linux 权限提升

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

特征

* 攻击路径图——参见YOU → technique → ROOT，从左到右
* 🔴置信度着色——已确认的路径以红色显示，可能的线索以琥珀色显示
* 🖱️点击任意节点— 获取该节点的信息以及完整的滥用命令（可直接复制）
* 🔗多跳链— 发现跨越不同发现的路径（例如，可写脚本 → root cron → root）
* 🧠可编辑规则手册— SUID/SGID、sudo、权限、危险组、可写文件、NFS、PATH劫持以及内核/sudo CVE匹配
* 📴完全离线— 无依赖项，无需网络，单个独立的 HTML 输出

安装：

```
git clone https://github.com/roothound.git
cd roothound
# feed it LinPEAS output:
python3 roothound.py linpeas.txt -o report.html
```

选项 2 — 下载 ZIP： 点击上面的绿色代码按钮 →下载 ZIP，解压缩，然后运行它。

然后report.html用任意浏览器打开。

演示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0HaPjwWWayI8pDM2Zqt1dpq6yVHNklCxAqTHMpiaoQ7wz7x7T07ib8WNQRIKNuNWtLH9icc4aDe6dwXzaiciafLB76B9k7Ah45gP2js/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0FpeXd4NibxVF2M62ibQ1VbIGiasN1QaicI5tdTHyUic3HERPZxA7FquK20CiaM1kJXu9HZEvkRwwznIbq5icbRN2hTneCfFIaibt1S5RE/640?wx_fmt=png&from=appmsg)

项目地址：

https://github.com/Noz2/RootHound

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0H4BibCX3K7VGWtQqPbYJUjMib0L1QNoPJHgHvG00f0vyaq38C2eglYSeGHCia2bfL7gcD2QoAh5owv5Rl4SMHZAzvZT3w4ANkdXg/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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