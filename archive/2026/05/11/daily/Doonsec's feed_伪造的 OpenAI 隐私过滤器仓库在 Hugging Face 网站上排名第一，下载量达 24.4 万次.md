---
title: 伪造的 OpenAI 隐私过滤器仓库在 Hugging Face 网站上排名第一，下载量达 24.4 万次
url: https://mp.weixin.qq.com/s/Fj69oS5NyyGe1NTTKj5MnQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:35:03.738652
---

# 伪造的 OpenAI 隐私过滤器仓库在 Hugging Face 网站上排名第一，下载量达 24.4 万次

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7NNTIlrC0vJUicXCkBhpZdHSGibGyyticreMdbGm70fO9Wcv0ZkAicCwslDr9zmM4D1mWPRcVedD8bEhLnPcsC99TBXCFRU7c9JdpA/0?wx_fmt=jpeg)

# 伪造的 OpenAI 隐私过滤器仓库在 Hugging Face 网站上排名第一，下载量达 24.4 万次

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个名为 Hugging Face 的恶意代码库通过冒充 OpenAI 的 Privacy Filter 开源模型，向 Windows 用户提供基于 Rust 的信息窃取程序，成功跻身该平台的热门榜单。

该项目名为Open-OSS/privacy-filter，伪装成 OpenAI 上月底发布的合法版本 ( openai/privacy-filter )，甚至逐字复制了其全部描述，诱骗毫无戒心的用户下载。Hugging Face 已禁用对该恶意模型的访问。

Privacy Filter是人工智能 (AI) 公司于 2026 年 4 月推出的一项功能，旨在检测和编辑非结构化文本中的个人身份信息 (PII)，从而将强大的隐私和安全保护融入应用程序中。

HiddenLayer 研究团队在上周发布的一份报告中表示：“该存储库抢注了 OpenAI 的合法隐私过滤器版本，几乎逐字逐句地复制了其模型卡，并提供了一个 loader.py 文件，该文件会在 Windows 机器上获取并执行信息窃取恶意软件。”

该恶意项目指示用户克隆存储库，并运行 Windows 系统的批处理脚本（“start.bat”）或 Linux 或 macOS 系统的 Python 脚本（“loader.py”）来配置所有必要的依赖项并启动模型。

一旦启动，该 Python 脚本会触发恶意代码，该代码负责禁用 SSL 验证，解码托管在 JSON Keeper 上的 Base64 编码 URL，并使用该 URL 提取命令，然后将该命令传递给 PowerShell 执行。攻击者利用 JSON Keeper（一个公共 JSON 粘贴服务）作为死信箱解析器，无需修改存储库即可动态切换有效载荷。

PowerShell 命令用于从远程服务器（“api.eth-fastscan[.]org”）下载批处理脚本，并使用“cmd.exe”启动它。该批处理脚本作为第二阶段下载器，通过用户帐户控制 (UAC) 提示提升其权限来准备环境，配置 Microsoft Defender 防病毒排除项，从同一域下载下一阶段二进制文件，并设置一个计划任务来启动 PowerShell 脚本以运行可执行文件。

计划任务启动后，恶意软件会等待两秒钟然后自行删除。最后阶段是一个信息窃取程序，旨在截取屏幕截图并从 Discord、加密货币钱包和扩展程序、系统元数据、FileZilla 配置和钱包助记词等文件以及基于 Chromium 和 Gecko 渲染引擎的 Web 浏览器中窃取数据。

HiddenLayer解释说：“尽管使用了计划任务，但此阶段并未建立持久性：该任务在任何重启之前都会被销毁。它被用作一次性的系统上下文启动器。”

窃取程序还会进行检查以检测调试器和沙箱，确认自身未在虚拟机中运行，并尝试禁用 Windows 反恶意软件扫描接口 (AMSI) 和 Windows 事件跟踪 (ETW) 以逃避行为检测。窃取的数据以 JSON 格式泄露到“recargapopular[.]com”域。

据称，在被禁用之前，该模型在 Hugging Face 网站上曾登上热门榜首，18 小时内下载量约为 24.4 万次，点赞数为 667 次。有人怀疑这些数字是人为夸大的，目的是给该网站营造一种值得信赖的假象，从而吸引用户下载。

对该活动的进一步分析发现，还有六个代码库也使用了类似的 Python 加载器来部署窃取程序 -

* anthfu/Bonsai-8B-gguf
* anthfu/Qwen3.6-35B-A3B-APEX-GGUF
* anthfu/DeepSeek-V4-Pro
* anthfu/Qwopus-GLM-18B-Merged-GGUF
* anthfu/Qwen3.6-35B-A3B-Claude-4.6-Opus-Reasoning-Distilled-GGUF
* anthfu/supergemma4-26b-uncensored-gguf-v2

HiddenLayer 表示，他们还观察到“api[.]eth-fastscan[.]org”域名被用于提供另一个 Windows 可执行文件（“ o0q2l47f.exe ”），该文件会向“welovechinatown[.]info”发出信号，这是一个命令与控制 (C2) 服务器，此前曾被用于一项利用名为 trevlo 的恶意 npm 包来传播 ValleyRAT（又名 Winos 4.0）的攻击活动。

Panther上个月指出： “该软件包的 postinstall hook 会静默执行一个混淆的 JavaScript 加载器，该加载器会生成一个 base64 编码的 PowerShell 命令，该命令又会从攻击者控制的基础架构中获取并执行第二阶段的 PowerShell 脚本。”

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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