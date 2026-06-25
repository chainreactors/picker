---
title: 你的信息可能早被扒光了：5款免费开源工具帮你自查暴露面
url: https://mp.weixin.qq.com/s/UN13M7gdXxAZEN7t0r9fuw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:07:01.120969
---

# 你的信息可能早被扒光了：5款免费开源工具帮你自查暴露面

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FxDqdf0BMhbQ3Wo5s2Tr27xjkkP8Mia6aPmKdbGRPBglYzyWIXwAeqoj6ZBP71ZC7pXDGNdblQToEYgYzcsYvM1uyM0UFbKCZhPGtBvWj5X0/0?wx_fmt=jpeg)

# 你的信息可能早被扒光了：5款免费开源工具帮你自查暴露面

原创

z释然z
z释然z

释然IT杂谈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **不要用来查别人，查自己，才是真正的安全第一步。**

你有没有想过—— 你多年前注册的一个论坛账号， 你随手填的同一个昵称， 你公司的一个域名， 甚至你家打印机的IP地址……

**可能早就被“扒”干净了。**

今天不讲黑客入侵，不讲APT攻击。**我们聊聊“暴露面”这件事**—— 一个人、一家公司，在网上到底留下了多少痕迹，你自己都不一定知道。

我整理了 **5款免费开源OSINT工具**， 覆盖**查用户名、查邮箱、查域名、查IP、查设备**的完整链条。

**全部免费，无需Key（除Shodan外），新手也能上手。**

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhYRhBpZfzNteY33BN8ouFEvmGCibQj6VdPQ4OsiaRBr27gyvP6uOicLicg071M5teaLWurzMxkjWvNbx0qooa2ESanSsb1DxYNxgVQ/640?wx_fmt=png&from=appmsg)

## 🛠️ 五个工具，各管一摊

### 🔍 Blackbird（⭐6300）

**场景：查一个用户名/邮箱在全网的账号**接入600+平台，自动搜索，生成AI画像，一键导出PDF报告。 适合**快速扫全貌**。

### 🕵️ Maigret（⭐33000）

**场景：深挖一个用户名，递归揪出所有马甲**覆盖3000+平台，核心能力：**顺着一个马甲，自动挖到另一个马甲**。 适合**挖地三尺**。

### 🌐 SpiderFoot（⭐18000）

**重炮：邮箱、域名、IP、手机号通吃**200+模块并行，能查数据泄露、暗网、子域名，出**可视化关系图谱**。 适合**全链路情报采集**。

### 📧 theHarvester（⭐16500）

**查公司专用：输入域名，批量扒员工邮箱、子域名、IP**从谷歌、必应、LinkedIn、DNS记录等40+数据源自动化收集。 适合**商业尽调 / 安全审计**。

### 🖥️ Shodan Python（⭐2800）

**查设备：全网暴露的摄像头、路由器、服务器、工控系统**官方Python库，自动化查询Shodan数据库。 适合**检查公司IT资产是否裸奔**。

## ✅ 正经用法：查自己，查安全

别总想着“查别人”。**以下场景，完全合法且极度推荐——**

### 🔐 场景一：查自己的数字足迹（避免信息泄露）

用 **Blackbird + Maigret** 查你常用的用户名和邮箱， 你会惊讶： “天呐，我大学时在××论坛注册的账号竟然还在，密码还是原始密码……”

**知道暴露了什么，才能有针对性地清理、注销、改密码。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FxDqdf0BMhau0qJaxXU4HHFZIEH6iaib35l4LulyWlGhCO8S0QOLSib3uI6LZ1JIahRy2Zs8Chq0iabWYpywjsnYceyy1b6KEdGG8NFOtU6ibDv0/640?wx_fmt=png&from=appmsg)

### 🏢 场景二：公司安全自检（ESG审计必备）

* **theHarvester** 查自己公司域名，看对外暴露了多少员工邮箱和子域名。
* **SpiderFoot** 深挖，看有没有在黑市数据泄露中出现。
* **Shodan** 扫IP段，看内部系统、摄像头、打印机是否暴露在公网。

**很多公司的NAS、打印机，出厂密码都没改，Shodan一搜一个准。**

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhb7QzUJYscuf6Ol8ISdrVtDAiaPZyib1zuWCRwcpa23biawS6E63Kva6QiafFHiamOZRIRGJAaoyRO7z4YCgBMFWkZRdapECd1Tbd24/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/FxDqdf0BMhbRUMpo17XaiccER6o3SCgrKNT9DpE1wM3OE9rNjqm0iaUrfHV1ng2mxbTRGuFyQLxZpgGZwTPoqLd58Lia75YHUbcA86bjqE4YB8/640?wx_fmt=png&from=appmsg)

### 📈 场景三：竞争对手技术架构分析（合规情报）

想知道竞争对手用哪家云？用什么服务器软件？有哪些子域名暴露了业务线？**theHarvester + Shodan** 搭配，从公开信息中还原技术栈。

这不是“黑客攻击”，而是**基于公开信息的情报收集**，很多安全团队都在做。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FxDqdf0BMharVcQndkyXlwZ1bW65d2aFDMB2Z0ibk8CmeAYjvquyoBYjZ5RumK0OTtUeU0pWh8hKp5VKZhpFywpo4nzrPa2pbuLR20ZPWyHg/640?wx_fmt=png&from=appmsg)

## ⚠️ 必须强调的法律红线

**这些工具本身是中性、合法的。**但**用法决定了性质**：

+ ✅ **查自己、查自己公司** → 安全自检，强烈推荐。

+ ❌ **爬取他人隐私信息、人肉搜索、非法调查** → 违法行为，千万别碰。

**本文只讲自检思路和保护方法。不提倡、不建议任何非法用途。**

## 🖥️ 安装方式（一行命令搞定）

```
# Blackbird
git clone https://github.com/p1ngul1n0/blackbird && pip install -r requirements.txt

# Maigret
pip install maigret

# SpiderFoot
git clone https://github.com/smicallef/spiderfoot && pip install -r requirements.txt

# theHarvester
git clone https://github.com/laramies/theHarvester && uv sync

# Shodan Python
pip install shodan
```

> **Blackbird、Maigret、SpiderFoot** 开箱即用，无需任何API Key。**theHarvester** 部分数据源需要Key（谷歌、Bing），基础功能免费可用。**Shodan** 需要注册免费账号获取API Key，日常额度够用。

## 💬 最后说一句

**一个人、一家公司，在网上能藏住的东西，远比他们以为的少得多。**

你以为删掉的账号， 以为没人知道的马甲， 以为没有暴露的服务器——**只要存在过，大概率能找回来。**

**知道自己暴露了什么，是保护自己的第一步。**

> 把这篇文章转发给你身边的IT运维、安全同事， 让他们也查一查自己的数字资产—— 查清楚了，才睡得踏实。

📎 项目地址：

+ github.com/p1ngul1n0/blackbird

+ github.com/soxoj/maigret

+ github.com/smicallef/spiderfoot

+ github.com/laramies/theHarvester

+ github.com/achillean/shodan-python

**关注我，持续分享实用的安全工具与自检方法。**

![](https://mmbiz.qpic.cn/mmbiz_png/3heAguJrdPwwb5AxgeyO4QBNh18Fn6zdHoLUI5icibB4ibJKHvDsZTm7oBibUMPBk2ccibiawFdUyRsxdwsHjdAVjYuw/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3heAguJrdPxL46gicFSARTgYJPz3TpN3INITJuS3sblUpVO0tTAX9pkc4ujQxP3KdnVgZHJQU1BJLFK4wiba2WRA/0?wx_fmt=png)

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