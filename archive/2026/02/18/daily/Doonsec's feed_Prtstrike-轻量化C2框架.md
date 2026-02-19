---
title: Prtstrike-轻量化C2框架
url: https://mp.weixin.qq.com/s/gHg3ufML96YcHaXzcv1kEw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:15:14.315496
---

# Prtstrike-轻量化C2框架

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SbtGVeibYWqsiaE9ibwakBGHpSREbaUEeiaJy1ptKunD8YS8ztDOTlkGO3FugKa7eNI4CbwtFe30fbj9FCQ6fC1jfotuk7ibHL3OUObuBVrM6kd4/0?wx_fmt=jpeg)

# Prtstrike-轻量化C2框架

原创

黄豆安全实验室
黄豆安全实验室

黄豆安全实验室

![]()

在小说阅读器中沉浸阅读

# PRTSTRIKE - Light Small Quick

项目地址:https://github.com/Team-intN18-SoybeanSeclab/prtstrike/

***Note：请务必完整看完此README.md再使用本工具。***

![](https://mmbiz.qpic.cn/mmbiz_png/SbtGVeibYWqv9rWr3tJ7B4K9qfEQKgbfCcdPHRoO7d24QPLHzM2j50tW4R4rwNyTO434TLKv2IAqJLIBhkVZJfIjNAnibgvO92RXXnq8YUthk/640?wx_fmt=png&from=appmsg)

## 0x01 Introduction

PRTSTRIKE，一个轻便、小巧、快捷的轻量化C&C框架，由**Go**编写，最快可**1分钟**部署完成。Build后大小仅**30MB**，***截至2026.2.18，微步0检出***。

## 0x02 Quick Start

部署命令：

```
git clone https://github.com/Team-intN18-SoybeanSeclab/prtstrike.git

cd prtstrike

go run .
```

目前，本工具支持如下功能：

1. 1. 隧道
2. 2. 屏幕截图
3. 3. 文件浏览器
4. 4. 生成Shellcode，EXE，ELF等形式的Payloads

## 0x03 Precautions

* • 当您首次使用本工具时，您需要运行如下命令换源:

```
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
```

* • 在使用本工具前，您只需下载Golang作为运行环境
* • 默认端口为**8083**，您可以在**main.go**中修改。
* • 默认账户为`Adm1nstr@t0r`，密码为`Pr3c1se5!@#$%`，务必部署后在Settings处修改。
* • 本工具隧道部分依赖Chisel，已放在tools目录中，不放心的师傅可以前往Chisel Github仓库自行下载

## 0x04 Disclaimer

1. 1. 您的下载、安装、使用或修改本工具及相关代码，意味着您对本工具的信任。
2. 2. 本工具在使用过程中可能对您或他人造成损失或伤害，若发生此类情况，我们不承担任何责任。
3. 3. 如果您因使用本工具而从事任何非法行为，您将自行承担一切后果，并且我们不承担任何法律责任或连带责任。
4. 4. 请在使用前，仔细阅读并充分理解所有条款，特别是关于责任免除或限制的条款，并自行决定是否接受。
5. 5. 除非您已经完全理解并接受所有条款，否则您无法下载、安装或使用本工具。
6. 6. 您的任何下载、安装或使用行为，均视为您已完全阅读并同意本协议条款。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfZGYGTCfkmoZAjWACD8SRcEPz9kMiasJSNMegN4rfJLBZWicE3jfCX2MQK74RNyibxbVFvD7F0nTHoEg/0?wx_fmt=png)

黄豆安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZLxicS8peicfZGYGTCfkmoZAjWACD8SRcEPz9kMiasJSNMegN4rfJLBZWicE3jfCX2MQK74RNyibxbVFvD7F0nTHoEg/0?wx_fmt=png)

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