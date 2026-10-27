---
title: 扒一扒LiteLLM供应链攻击内幕：黑客是如何利用GitHub OAuth令牌留后门的？
url: https://mp.weixin.qq.com/s/htjG8StZIhW4o6nZa3rP1w
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:57.091221
---

# 扒一扒LiteLLM供应链攻击内幕：黑客是如何利用GitHub OAuth令牌留后门的？

# 扒一扒LiteLLM供应链攻击内幕：黑客是如何利用GitHub OAuth令牌留后门的？

原创

Hankzheng
Hankzheng

技术修道场

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/kBd83kxr9I7utKMzu0KYyxaJic1lO1OOcP97A6Kpia7fuuiaX7UqSe99lHnzuB8M0jPkWbJS4Wia9nDnI0kqCBv5mnkicnm10bFYVWnz7VSBPlEg/640?wx_fmt=png&from=appmsg)

大家好，如果你在项目中使用了大模型代理工具 LiteLLM，那需要马上去检查一下你的环境版本！

根据 SafeDep、Socket、StepSecurity 等多家安全机构的联合预警，大受开发者欢迎的 Python 包 **LiteLLM 遭遇了非常严重的软件供应链攻击**。黑客不仅植入了专门窃取凭证的木马，还留下了一个隐蔽的远程控制后门。

我第一时间去啃了这几家机构的安全报告，这波操作可以说是非常“脏”了。作为一名经常和各种开源包打交道的开发者，今天我就和大家拆解一下这次攻击的硬核技术细节，看看黑客是怎么一步步“偷家”的。

## 🔍 攻击入口：防不胜防的 OAuth 令牌劫持

这次被投毒的版本是 **LiteLLM 1.107.0**，受污染的包已经被分发到了 PyPI 的 wheel 文件和官方 Docker 镜像中。

黑客是怎么越过代码审查直接发布官方版本的？LiteLLM 的安全总监 Oliver Jensen 透露了一个细节：

> “黑客通过**窃取的三名工程师的 GitHub CLI OAuth 令牌**，接管了他们的 GitHub 账号。随后，利用其中一个账号触发了项目发布流程，再用另一个账号进行了审批。”

这招“左右互搏”直接绕过了安全审计机制。虽然官方目前已经撤销了所有涉事令牌，并将组织内除了一个未受影响的用户外的所有人移除，但这给我们敲响了警钟：**你的代码写得再安全，只要 CI/CD 管道的凭证泄露，防线就会瞬间土崩瓦解。**

## ☠️ 硬核拆解：黑客的投毒与驻留姿势

这次黑客不仅进来了，而且手段非常高明。他们利用了 Python 的一个冷门特性来实现恶意代码的无感自启。

### 1. 利用 `.pth` 文件实现“幽灵启动”

我们都知道，运行 Python 包通常需要主动 `import`。但这次黑客玩了个阴的——他们利用了 Python 的 `.pth`（path）文件机制。

恶意包中包含了一个名为 `cook.pth` 的文件，里面只有一行代码：`import cook`。

在 Python 中，`.pth` 文件会在解释器启动时被自动处理，这意味着**甚至在你还没有在代码里显式导入 LiteLLM 之前，只要 Python 环境一启动，恶意木马就已经在后台跑起来了！** 顺便提一嘴，今年 3 月 TeamPCP 供应链攻击中，黑客用的也是同样的套路。

### 2. Payload 1：数据吸尘器 "privcollect"

这个名为 `privcollect` 的载荷是一个无情的凭证收集器。只要它被激活，就会在你的服务器或开发机上疯狂翻找：

* 云服务凭证与开发者账号的私钥
* AI 开发工具相关的身份验证 JSON 文件
* Chromium 和 Firefox 浏览器的本地数据
* 系统的环境变量
* LiteLLM 代理中保存的模型配置和密钥

收集完毕后，这些数据会被打包成 GZIP 压缩的 TAR 文件，然后通过 HTTP POST 请求，明目张胆地发送到黑客控制的服务器 `litellm[.]dev/healthcheck`。

### 3. Payload 2：潜伏的后台远控 Daemon

除了偷东西，黑客还想长期白嫖你的算力或网络。第二个载荷会 fork 出一个后台守护进程，这个进程会**每小时**去检查一次 GitHub 上的一个“死信箱”（Dead Drop）。

它会读取 GitHub 仓库 `github[.]com/letters9813` 下的 `domain.txt` 文件。如果里面配置了域名，它就会向 `<domain>/codepy` 发起 HTTP GET 请求，并**直接执行返回的 Python 代码**。这种 C2架构非常灵活，随时可以让你的服务器变成肉鸡。

## 🛡️ 受影响范围与自救指南

目前已知的受污染文件涵盖了 Mac、Linux 和 Windows 的各大架构，甚至连 `tar.gz` 源码包里都被篡改了 `pyproject.toml`。受影响的 `.whl` 文件列表如下：

* `litellm-1.107.0-cp310-abi3-macosx_10_12_x86_64.whl`

  (及 arm64 版)
* `litellm-1.107.0-cp310-abi3-manylinux_2_28_aarch64.whl`
* `litellm-1.107.0-cp310-abi3-manylinux_2_28_x86_64.whl`
* `litellm-1.107.0-cp310-abi3-musllinux_1_2_aarch64.whl`
* `litellm-1.107.0-cp310-abi3-musllinux_1_2_x86_64.whl`
* `litellm-1.107.0-cp310-abi3-win_amd64.whl`

### 💡 避坑建议

* **立刻降级并锁死版本：**

  如果你最近拉取了新版本，建议立刻将其回退，并通过哈希值将版本严格固定在干净的 **1.106.2**。
* **紧急轮换凭证：**

  如果你不幸安装了 1.107.0，**必须假设你的所有云密钥、私钥、环境变量和浏览器数据都已经泄露**。请立刻在一个全新的、干净的环境中吊销所有旧凭证并重新生成。
* **排查构建管线：**

  检查一下自己项目的 GitHub OAuth 令牌权限，落实最小权限原则。

在 AI 基础设施日渐繁荣的今天，攻击者的目光早就盯上了这些处于基石位置的开源工具。写代码不易，防黑客更难，大家且撸且珍惜吧！

你的环境里部署 LiteLLM 了吗？欢迎在评论区分享你的排查经历！
觉得文章有用的兄弟，别忘了点个“在看”转发给团队的小伙伴，避免中招！

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/wWBwsDOJT48jXhr3LrlFvFZoevRic7DnQnTT7l1Xh2vwQZFg0EVXZj8AfvVs3uBFwDRS7JsuQ7NXlaCW0Iq6feA/0?wx_fmt=png)

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