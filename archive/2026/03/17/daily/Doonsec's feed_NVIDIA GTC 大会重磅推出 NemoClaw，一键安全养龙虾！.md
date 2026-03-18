---
title: NVIDIA GTC 大会重磅推出 NemoClaw，一键安全养龙虾！
url: https://mp.weixin.qq.com/s/xhvIv7YFH--wTMQVOPZdcQ
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:18:36.465428
---

# NVIDIA GTC 大会重磅推出 NemoClaw，一键安全养龙虾！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mAf9IMALLwgNcGMV17ps6hlPPM2flOyyMAOlOGoiavSiaQTFD00uY4dWGYicjGSNy0SThv3fzQ3WzabdgBbsVCYCpPfP5KsLSkymIP2UnpJ2Ko/0?wx_fmt=jpeg)

# NVIDIA GTC 大会重磅推出 NemoClaw，一键安全养龙虾！

原创

糖果LUA
糖果LUA

AI安全运营

![]()

在小说阅读器中沉浸阅读

NVIDIA GTC 大会发布 NemoClaw，一键安全养龙虾来了！NVIDIA NemoClaw 于 2026 年 3 月 16 日在 NVIDIA GTC（GPU Technology Conference）大会上正式发布。在 Jensen Huang 的主题演讲中，NVIDIA 推出了这款开源工具栈，作为对爆火的 OpenClaw 自主 AI 代理平台的官方支持。它旨在解决 OpenClaw 在安全性和可控性方面的痛点，让普通开发者也能通过简单命令，安全地“养”起自主进化、始终在线的 AI 龙虾。OpenShell 介绍及其安全机制NVIDIA OpenShell 是 NVIDIA Agent Toolkit 中的开源运行时，专为运行自主 AI 代理而设计。它为 OpenClaw 提供了一个高度隔离的“安全沙箱”。核心安全机制包括：

* Landlock（文件系统细粒度限制）
* seccomp（系统调用过滤）
* netns（网络命名空间隔离）
* 声明式策略 + 隐私路由器

所有操作均受严格管控，未授权行为自动阻断或需人工审批，确保“龙虾”再聪明也跑不出笼子。NemoClaw、OpenShell、OpenClaw 与 Docker 容器之间的关系为了让大家更清楚四者的层级与协作关系，我绘制了以下关系图：

![](https://mmbiz.qpic.cn/mmbiz_png/mAf9IMALLwiaUWNWxoUAKJSf5D20jh4QLX87gt3ibSKpGrheEpo7ibNj9RI4Dq3rVVnCibT0pofjIzFXEOEFIKVKz3v1d9ejW2YDnI5YON8suac/640?wx_fmt=png&from=appmsg)

关系总结

* Docker 容器：提供基础运行环境（尤其 macOS 用户必须用它）。
* OpenShell：真正的安全牢笼（沙箱）。
* OpenClaw：住在牢笼里的“龙虾”（自主 AI 大脑）。
* NemoClaw：NVIDIA 官方送的“养虾工具包”，负责一键把龙虾安全装进牢笼并喂养（配置、策略、路由）。

主要特点与安全优势

* 使用 NemoClaw 沙箱运行 OpenClaw 显著更安全。
* 支持交互式 TUI 聊天和 CLI 操作。
* 支持策略热重载、远程部署等高级功能。
* 当前为 Alpha 阶段，适合尝鲜和学习。

前提条件

* 官方推荐 Linux Ubuntu 22.04 LTS 或更高版本。
* Mac 系统也可以安装：笔者已亲测通过 Docker Desktop 成功运行。
* Docker 已安装并运行。
* Node.js 20+（推荐 22+）。

安装方式

1. 官方推荐一键安装：

   ```
   curl-fsSL https://nvidia.com/nemoclaw.sh |bash
   ```
2. 手动安装（效果相同）：

   ```
   git clone https://github.com/NVIDIA/NemoClaw.git
   cd NemoClaw && ./install.sh
   ```

API Key 配置若想让本地龙虾连接 NVIDIA 云端推理服务，请务必前往 https://build.nvidia.com/settings/api-keys 获取 API Key，并在安装向导中输入。

---

安装过程

检测Docker安装OpenShell Cli，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAf9IMALLwhLqzW7JTTldDOicX5AiczKaks8e3iaawqXvo8U3JaJBvibJ3pbMAQJDRco4lAH90ErseibCnibyVGkTibJ75TIKus6KsKkicbzAzSzTxw/640?wx_fmt=png&from=appmsg)

---

检测Node环境，同时安装OpenShell Gateway,如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mAf9IMALLwjl9GjNIRfdX0saO5Y9CVCyMESclQpnbjPqCWzrPBwUN5r5svobICicWRX9BWHgg0vibyiaSTaAO4ZakOzhiaSHibCCibqysMPDfaCuY/640?wx_fmt=png&from=appmsg)

---

创建沙箱过程，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/mAf9IMALLwgojWczB9dnXFce9xu9OO2wvv0XbgkUrHg3MnkkfCZhGBibXUzDvUwCPFLRq1CGU0UK3ghpFH4pBMHRTnaqkwkomGOyebZnZtvM/640?wx_fmt=png&from=appmsg)

---

配置网关和策略 ，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/mAf9IMALLwjJvats6FFicytr1FgvuUZtohWuibEm1O0IPx7FqBSnkZeYHRgVPYOzL5uAxSOhcxy9Q1ESlIHnC1icmp14pjqa2AicBZKQOXq1PKQ/640?wx_fmt=png&from=appmsg)

---

显示沙箱状态信息，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/mAf9IMALLwjoMYTWVDYBKqJPILhTGicxM9bjkBwGVoZ7xsPuiaU0cUkbibcnicuiaCZQPnW57xwafMgHC2y8vkQ2RSBBmFCEpmpSrQwg1358TsHk/640?wx_fmt=png&from=appmsg)

---

显示部分策略信息，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/mAf9IMALLwhPwY6zZ5qbrDMfI6HQ1UQG7MsEDwbticYMiaoNJdONNlDoKjMeBCKgjH3zRP9S6UmutoCTs8SeOHbLCiciamH4530LJPmlHqSOs14/640?wx_fmt=png&from=appmsg)

---

在沙箱中启动OpenClaw，如下：

![](https://mmbiz.qpic.cn/mmbiz_png/mAf9IMALLwjO1YRgvUq2mNHOBJAtK3M82cfdmIIneUX3FlBgNWFr8QoQMmkfIBDqhjdWNtI2lVQlkpIaB55CevhYjg6au9Rp8MIwaP1osoU/640?wx_fmt=png&from=appmsg)

---

MacOS 用户特别建议使用 Docker Desktop使用Docker，暂时不要使用 Orb过程中有概率出现问题。安装 Docker Desktop 后，安装启动一个  容器根据安装脚本完成 OpenShell、NemoClaw 、OpenClaw 的安装。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

AI安全运营

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GibwsQ0cuT56QuCD7VUY4ibe7mGx7xRHwhuPIfeGGrLs3y9LwOQ0qjmm4amibTX3NibWeKP7jsSicCrXq6Czs3waALA/0?wx_fmt=png)

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