---
title: Axios投毒事件：阿里云安全复盘分析与关键防护建议
url: https://mp.weixin.qq.com/s/tLBU500ur-kAvLe1CJcQ6g
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:25:07.071842
---

# Axios投毒事件：阿里云安全复盘分析与关键防护建议

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/X4coLUhcXJFGPX3ddlk1jArnQ7aSBkbr0ibFBFcBSE9cDbzJ9AFxlhMk1Q510cKaicaGXd9HtSibJLHVG11hswr12MDiaECdp3gfBrVgpoNRsIA/0?wx_fmt=jpeg)

# Axios投毒事件：阿里云安全复盘分析与关键防护建议

阿里云安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/X4coLUhcXJH0oJazmWQSzyVyLOyrqSr1qf5eiaf4UI7WdMCDQw57Acv49bDAhqAOplRiaunnopIun1wLGycNMH67TWBml6iahNklmyWIvk9MrE/640?wx_fmt=gif&from=appmsg)

**事件核心概述**

阿里云安全团队一直持续跟踪分析供应链攻击，在近期一起Axios事件中，我们主动发现并阻断了攻击。当前云安全中心的所有付费客户已经能够检测、阻断该类型攻击。Axios是一个基于promise网络请求库，在Axios的0.30.4和1.14.1版本中存在恶意依赖plain-crypto-js。安装受影响版本的安装包后会下载攻击者指定的远控木马并执行。

本次攻击并非通过常规的代码合并（Pull Request）污染开源代码库，而是一起典型的开发者凭据劫持事件。攻击者直接利用窃取的高权限npm账号，发布了包含后门的官方版本。

* **受影响组件**：`axios`
* **恶意版本号**：`1.14.1` 和 `0.30.4`
* **投毒方式**：绕过GitHub Actions等官方CI/CD流程，直接向npm Registry推送篡改后的包
* **恶意载荷**：通过引入名为`plain-crypto-js`的隐蔽依赖，静默投放跨平台远程访问木马（RAT）
* **攻击目标**：开发者的本地机器以及企业自动化构建服务器（支持MacOS、Linux、Windows平台）

**攻击链路与技术剖析**

攻击者的手法非常老练且极具隐蔽性。整个攻击过程可拆解为以下三个关键阶段：

**凭据劫持与越过CI/CD**

攻击者首先获取了Axios核心维护者的npm账号发布权限。在正常的开源项目迭代中，代码需经过GitHub Actions流水线的自动化测试与构建才能发布。为了避免在GitHub公开仓库的提交历史中留下痕迹并触发代码审查，攻击者选择在本地构建恶意的发布包，并使用被盗凭据强行推送到npm仓库。

**隐蔽的恶意依赖注入**

在篡改发布的axios@1.14.1和0.30.4版本中，攻击者并没有去修改Axios原本的核心逻辑文件，而是直接修改了package.json文件。他们向其中注入了一个全新的依赖项：plain-crypto-js@4.2.1。

这个依赖在Axios的任何源代码中都**没有被实际引入（import/require）**。其唯一存在的目的，就是作为后续恶意脚本的载体。

**利用postinstall触发跨平台RAT**

当不知情的开发者或自动化服务器执行npm install下载受感染的Axios版本时，npm包管理器会自动解析并下载该隐形依赖。随后，plain-crypto-js包内部的postinstall钩子脚本会被静默触发，执行一个名为setup.js的脚本。

该setup.js脚本充当了一个跨平台的恶意软件释放器（Dropper）即，会根据受害者的操作系统类型，自动下载并植入远程访问木马。为了对抗安全排查，恶意程序在执行完毕后具备自毁机制，因此事后直接检查node\_modules目录往往难以发现明显的残留源码。

**IOCs与系统影响**

一旦木马驻留成功，攻击者便能在受害者机器上建立持久化连接，进而窃取敏感数据（如环境变量、源代码、云服务凭据、SSH 密钥等）或执行任意系统命令。不同操作系统的具体后门释放路径如下表所示：

![1.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X4coLUhcXJG58p7VuPro12MRfnqOHSEGYia8YdRTffQKVU7GibReInoMdbwjyNWu6XDkxvtPvAMkZcq9aicxORMCRgviad9zDT26rPdTecYkVbM/640?wx_fmt=jpeg&from=appmsg)

![2.jpg](https://mmbiz.qpic.cn/sz_mmbiz_jpg/X4coLUhcXJFuAwO7ZZsA5cR4OB7e9SefHzXeZ9qMwhCZdnZZibRo2QakGicTSXT9QZUyVOCjibib3sgaTiayfFdHm9gDkes7egiaJNexMoqibgpqicw/640?wx_fmt=jpeg&from=appmsg)

**排查与修复指南**

鉴于该恶意载荷的自毁特性以及极强的破坏力，安全团队和开发者需要立即采取以下步骤进行排查：

**项目依赖排查**

检查项目的依赖文件（如`package-lock.json`、`yarn.lock`或`pnpm-lock.yaml`等）

* 确认是否曾引入过Axios恶意版本（`1.14.1、0.30.4`）。

+ 执行命令查看是否安装了被投毒的版本：`npm list axios`
+ 直接检索包管理锁文件：`grep -A1 '"axios"' package-lock.json`

* 检查是否存在后门依赖目录：`ls node_modules/plain-crypto-js`

**系统后门排查**

如果在项目中发现了上述恶意版本，立即检查文件系统中是否存在木马：

* **MacOS**：执行`ls-la/Library/Caches/com.apple.act.mond`
* Linux：执行ls-la/tmp/ld.py
* **Windows (CMD)**：执行 `dir "%PROGRAMDATA%\wt.exe"`

**应急阻断与修复建议**

1. **物理与网络隔离**：立即将疑似受感染的开发机或服务器从内部网络中隔离，防止内网横向移动。
2. **凭证轮转**：彻底吊销在该机器上存放或使用过的所有敏感凭据，包括但不限于npm Token、GitHub PAT、AWS/GCP/阿里云访问密钥等。
3. **版本回退与锁定**：在绝对安全的环境中，将项目中依赖的`axios`降级至安全的稳定版本，重新生成并提交lock文件。
4. **持续监控与建设**：企业在日常开发中不能盲目信任官方来源的包版本更新，必须加强对锁文件的版本变更审计，并引入自动化工具来扫描第三方依赖中的隐蔽投毒与异常 `postinstall` 行为，以建立更为纵深的供应链防御体系。

**阿里云安全响应**

阿里云云安全中心和云防火墙已在第一时间完成以下响应：

**检测策略上线**：云安全中心已上线针对`Axios1.14.1`/`0.30.4`的恶意包检测规则，支持自动识别受影响主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJG4TfPmSXadmzdVibmibhFia95qmVwNohkPlpMyEExtKQyVsavItj121aJX35XYAtEUZy2AUleBFl9tBwWas2aoqAsxTGatrBLIMU/640?wx_fmt=png&from=appmsg)

**入侵检测告警**：阿里云云安全中心已经支持相关投毒文件的检测，如果发现相关告警，请使用产品功能进行处置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJGoMU5JloX6SI0LISw3UAtwl5MwI9yMXk2U2y6JY0ca2a46V6sxtM7xIqPahL90FzMhbOBPaj2oyiauTlteOxwiaguwmQFEJfibias/640?wx_fmt=png&from=appmsg)

**网络流量拦截**：阿里云云防火墙已阻断`sfrclak.com` C2域名的出站连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/X4coLUhcXJFBqZ2xwmWEZAn1dITUoZlTtaPCiaFhp8rjricaVhic17MMvD4aDG7wZSfag8NSHHTdUYXlW2qGjNSnkAiagujgDkia00GS1LgvMn34/640?wx_fmt=png&from=appmsg)

**事件调查：**Agentic SOC事件调查AI Agent天然支持Axios供应链风险自动化排查，关联多源日志精准定位失陷资产并生成事件溯源图和可执行处置建议，并支持下载事件调查技术报告。

![](https://mmbiz.qpic.cn/mmbiz_png/X4coLUhcXJHr7Tcp1ndHRW5T1hdlztJOf5ic8wbiaRnHp4jJwyfLK60F5Oh3Gd7JRjqyic00YF4Du3rnsQ4m6icFQEVgXjStQadJ6upvm6KuFI8/640?wx_fmt=png&from=appmsg)

如需了解更多或申请体验，欢迎体验：

**云安全中心**https://www.aliyun.com/product/security-center。

**云防火墙**，https://www.aliyun.com/product/cloud-firewall。

点击“阅读原文”了解更多。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XXR4zia5yICHPGgzZ5JhLCo6qFCD9ogdgADkr9cxv7yb3mKhJntlEtQS8lr6o0FUT1j3TwySxHLcDM1fs8VhCLw/0?wx_fmt=png)

阿里云安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XXR4zia5yICHPGgzZ5JhLCo6qFCD9ogdgADkr9cxv7yb3mKhJntlEtQS8lr6o0FUT1j3TwySxHLcDM1fs8VhCLw/0?wx_fmt=png)

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