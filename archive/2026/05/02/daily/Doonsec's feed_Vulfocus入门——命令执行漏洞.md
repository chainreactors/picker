---
title: Vulfocus入门——命令执行漏洞
url: https://mp.weixin.qq.com/s/ghNa_MLRQiCVIO9mG-K7zA
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:24:29.641654
---

# Vulfocus入门——命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eQs5ycicWaynibV1QYA3v2OSfgxuERFTbsRyCVK9eIO2YkpBs6Hw4wcgoklk8od4iaiapXUxibalEaIlMZenLEXo0HusaaNw1icTVX2vWYyFMqv8w/0?wx_fmt=jpeg)

# Vulfocus入门——命令执行漏洞

原创

L×K@y
L×K@y

Quest安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

* 命令注入漏洞的核心成因：

**应用程序在调用外部系统命令时，将用户可控的数据（如输入、参数等）直接拼接到命令中，且未进行充分的验证或过滤。**

具体可分解为以下几个关键点：

1. **未过滤/转义用户输入**：程序直接使用了用户通过表单、URL参数、Cookie、HTTP头等提供的输入，作为系统命令的一部分。
2. **危险函数调用**：代码中使用了执行系统命令的函数，例如PHP中的 `system()`、`exec()`、`shell_exec()`，Java中的 `Runtime.exec()`，Python中的 `os.system()`、`subprocess.call(shell=True)` 等。
3. **拼接命令字符串**：直接将用户输入拼接到命令字符串中，没有使用参数化（类似SQL注入的预编译）或安全的API进行隔离。
4. **未使用安全编程模式**：没有遵循“白名单验证”、“转义特殊字符”、“限制命令执行权限”等安全实践。

**一个典型的漏洞代码示例（PHP）：**

php

```
// 危险：用户输入的filename直接拼接到ls命令$filename=$_GET['filename'];system("ls /uploads/".$filename);
```

攻击者可以提交：`?filename=; rm -rf /`，最终执行的命令就变成了：

bash

```
ls /uploads/;rm-rf /
```

**导致漏洞的常见场景：**

* **用户上传文件后的处理**：如调用 `convert`、`ffmpeg` 等外部工具。
* **系统诊断功能**：如Ping、Traceroute、NSLookup等网络工具调用。
* **压缩/解压功能**：调用 `tar`、`zip`、`unzip`。
* **发送邮件**：调用 `mail` 或 `sendmail`。
* **服务状态检查**：调用 `systemctl`、`service`。

**根本性原因总结：**

**信任了用户的输入，并将其作为代码（命令）执行，而不是仅作为数据处理。** 这是典型的“注入类”漏洞（包括SQL注入、XSS等）的共同根源——未将“数据”与“代码”进行有效隔离。

---

* 如题所示：

![](https://mmbiz.qpic.cn/mmbiz_png/eQs5ycicWaylaYuLCmoiaRHj4sULqcAPrdicI5DPtDlI7trF43spBFQzulP6o6mST9a7d3BWpaNmIbOXeiagKObAjEficuK0fL5NGcB3CRvcrLGU/640?wx_fmt=png&from=appmsg)

参数cmd可控，利用参数调用系统命令。

在 Linux 系统中，`/tmp` 是一个**临时文件目录**，全称为 `temporary`。

`ls` 是 Linux 系统中最基础、最常用的命令之一，英文全称是 **list**，用于**列出目录内容**。

![](https://mmbiz.qpic.cn/mmbiz_png/eQs5ycicWaynlMQLEribQhMm004iaMwvwXVBRXunXcnrScVKMQ8cibrqrSTZnLJTqC9f4puphr6NpmOicVrmwCOePHo2oRRibWGEMwJXHtyO5TKNU/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/HhKWtOygby9AOqkgGmBJufyXQuKHkic54gAWia2jNlgr42TmMSfMiakvMH5ia910kQ8PicMAc2H6jtqe0Xd3zp45T4g/0?wx_fmt=png)

Quest安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/HhKWtOygby9AOqkgGmBJufyXQuKHkic54gAWia2jNlgr42TmMSfMiakvMH5ia910kQ8PicMAc2H6jtqe0Xd3zp45T4g/0?wx_fmt=png)

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