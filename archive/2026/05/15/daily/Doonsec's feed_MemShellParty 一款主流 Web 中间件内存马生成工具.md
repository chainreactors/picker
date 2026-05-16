---
title: MemShellParty 一款主流 Web 中间件内存马生成工具
url: https://mp.weixin.qq.com/s/MPiJzxFE93W9xfR_InsDgw
source: Doonsec's feed
date: 2026-05-15
fetch_date: 2026-05-16T05:09:07.448564
---

# MemShellParty 一款主流 Web 中间件内存马生成工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1E8ULvdwpfOReeBLWGrXsSpffsc3uOxcXbEbvkDOpYfjJI1gicoR5OMH8wYTOJhY62lB2nbm3fCxFQO8fULUmVFH5AtQYldHWIglKKoKk6nI/0?wx_fmt=jpeg)

# MemShellParty 一款主流 Web 中间件内存马生成工具

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于泷羽Sec
，作者仙草里没有草噜丶

![](http://wx.qlogo.cn/mmhead/Hp9HAaP9GFBKneKn5ryBUs0PRR7YFdhjkVm1EtmTw39DFXQog0cNn1NibPUo2tbPL2mH1HymCVxM/0)

**泷羽Sec**
.

B站：泷羽Sec，团队专注于网络安全领域的内容创作与分享，为网络安全而战。来自一个从零开始学习网安的见习生。很菜，不喜勿喷。

> 白小羽
>
> 本工具仅供安全研究人员、网络管理员及相关技术人员进行**授权的安全测试、漏洞评估和安全审计**工作使用。使用本工具进行任何未经授权的网络攻击、渗透测试等行为均属违法，使用者需自行承担相应的法律责任。

## 工具简介

MemShellParty 是一款专注于主流 Web 中间件的内存马快速生成工具，专为安全研究人员与红队攻防人员打造，核心目标是简化内存马载荷的生成流程，大幅提升漏洞验证与攻防实战的工作效率。

项目地址：https://github.com/ReaJason/MemShellParty

![常规内存马生成界面](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOj28HB3SNBviadQB9Zd4wQDYvFJA8kKpWo0VBvicfMdBF8Zibxk7Wib4q47FmsEBWPZdz3tGhiaPndLwdE8XSzCgHP7jwILJoayWoA/640?wx_fmt=other&from=appmsg)

常规内存马生成界面

## 核心特性

### 全场景强兼容

全面覆盖攻防场景下各类常见中间件与框架，JDK 版本适配范围覆盖 JDK6 ~ JDK21，可满足不同环境下的实战使用需求。

### 高可用稳保障

针对所有支持的中间件与框架，搭建了完整的自动化测试矩阵，严格保障每一次生成的载荷都具备极高的可用性与稳定性，最大程度杜绝实战场景中的不确定性。

### 极致轻量化优化

基于深度优化的字节码生成策略，MemShellParty 实现了内存马体积的大幅缩减：常规内存马体积相较于 JMG 等传统工具缩小 \*\*30%\*\*，Agent 内存马通过 ASM 技术实现了 **80%** 的体积优化。

### 无侵入无干扰

生成的内存马对目标中间件的正常业务流量无任何影响，即使同时注入十几个不同类型的内存马，也不会干扰目标服务的正常运行。

### 一键化傻瓜操作

内置针对主流表达式注入、反序列化、SSTI 等常见漏洞的载荷生成能力，系统可自动适配 Java 模块限制绕过配置，动态生成最优攻击载荷，实现常规漏洞载荷的一键生成。

### 高灵活自定义扩展

原生支持哥斯拉、冰蝎、蚁剑、Suo5、NeoreGeorg 等主流工具的内存马生成；同时提供高度灵活的自定义内存马上传能力，可将任意定制化载荷融入 MemShellParty 的生成体系，打造贴合自身战术需求的攻击平台。

![Agent内存马生成界面](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfNVVkl7RQkaib7Nt0iagV8sx7rROC9mo5t07Apn9gGS2zxlSD7yiatwfZHGJuaKzLKI57IBC9QAKZht2eRAL6VSEcT4E2hWd8T7ek/640?wx_fmt=other&from=appmsg)

Agent内存马生成界面

## 快速使用

### 使用前必读

工具内置的探测马已完成服务类型的一一对应，探测所得的服务类型即为可生成对应内存马的服务类型（非中间件原生类型，例如 Apusic10 探测结果为 GlassFish，因其基于 GlassFish 进行二次开发）。

![DNSlog探测界面](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfNbfbFZ8icP0vLiciaZHjqjhTb1oyymrwJCnw5wbfkoBqaqzgUFkAkUKf59b0zGVbvQkeg03urhy828Y2SPJwgBnyjrGZicICibR5Tc/640?wx_fmt=other&from=appmsg)

DNSlog探测界面

### 在线尝鲜

> 白小羽
>
> 提示：仅限尝鲜使用，对于公网暴露的非官方服务请谨慎使用，避免生成的内存马被植入后门。

* 正式稳定版（master 分支）：https://party.mem.mk ，每次 Release 都会自动部署最新镜像。
* 开发预览版（dev 分支）：https://dev-party.mem.mk ，可抢先体验正在开发的新功能。

### 本地部署（推荐）

适合内网环境或本地测试使用，可通过 Docker 一键启动服务，部署完成后访问 http://127.0.0.1:8080 即可使用。

```
# Docker Hub 源，拉取最新镜像
docker run --pull=always --rm -it -d -p 8080:8080 --name memshell-party reajason/memshell-party:latest

# Github Container Registry 源，拉取最新镜像
docker run --pull=always --rm -it -d -p 8080:8080 --name memshell-party ghcr.io/reajason/memshell-party:latest

# 国内网络优化，南大 Github Container Registry 镜像源
docker run --pull=always --rm -it -d -p 8080:8080 --name memshell-party ghcr.nju.edu.cn/reajason/memshell-party:latest
```

![关于页面](https://mmbiz.qpic.cn/sz_mmbiz/1E8ULvdwpfOvAxUDffCeal8UFMAfdVibLkT00pI9k0SjXI8RxCxazABpeKTSEqhNkEvxchUiaqa1mfC2QZsicZjhW2nCL6zSS3wyImp0lk5zy8/640?wx_fmt=other&from=appmsg)

关于页面

## 广告时间

[![](https://mmbiz.qpic.cn/mmbiz_png/1E8ULvdwpfMnHmibL6J0gNXvicr2VMibj5qw7wUMYjUSrjvtCNX5DdKpcwEyk4SNmrEAA9Wa0yZk1VoU7DzmC0CERJ1d7RFwQvsv1NnUYSicoew/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=Mzg2Nzk0NjA4Mg==&mid=2247502572&idx=1&sn=42a9853381a099fc7c074230c39824a3&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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