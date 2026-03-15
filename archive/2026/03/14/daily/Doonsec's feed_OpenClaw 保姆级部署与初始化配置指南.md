---
title: OpenClaw 保姆级部署与初始化配置指南
url: https://mp.weixin.qq.com/s/a-PriUzPR_zm2LtptNk4ng
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:29:31.873695
---

# OpenClaw 保姆级部署与初始化配置指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HmaGibWBicEEnWAXjl9NPVdia6BP6fo3mqialiao6bRF8VWyUZbYubLhJRn8jAWHibcWzNWdibaPic3pFesZa2zhCARfnkCbgm4gnvLc4ib390veJTEo/0?wx_fmt=jpeg)

# OpenClaw 保姆级部署与初始化配置指南

原创

ZKAFKA
ZKAFKA

网络安全研究站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HmaGibWBicEEm09x5u1LHl3yJYyQHgIJUYmKic6Ket8kJFhFlN0CrMiaApjPgWqduMxoJakXxlDXs1IgicrNfk7OwVeoRA6sNfhLbdFWrlTycags/640?wx_fmt=png&from=appmsg)

> 什么是OpenClaw？
>
> OpenClaw是一个开源的多渠道AI网关系统，它能够让你的AI助手同时在多个平台（如微信、QQ、飞书、钉钉、Telegram等）上运行，并且支持自定义智能体（Agents）来处理不同类型的任务。
>
> OpenClaw项目始于对AI助手多平台部署需求的探索。传统的AI助手往往只能在一个平台上运行，而OpenClaw通过模块化架构和插件系统，实现了真正的跨平台AI助手部署。当前最新版本为v2026.3.2，采用MIT开源许可证，完全免费使用。

一键安装

OpenClaw 官方提供了一键安装脚本，该脚本会自动检测你的操作系统，完成 Node.js 环境依赖的检查与安装（如需），并设置好 `openclaw` 命令行工具。这是最简洁、最推荐的安装方式。

安装下载

macOS / Linux / WSL2

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

Windows（PowerShell）

```
iwr -useb https://openclaw.ai/install.ps1 | iex
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/HmaGibWBicEEl6n04ib7pcx7Hia22TaGBWficDEub2v2hOZkrf4Xf1ibLzma3KEj4VYkAF2PsflDTKnrCnaFdP1ibxERkiaHfDPE1MWiaIv1gJjCvn1s/640?wx_fmt=png&from=appmsg)

运行安装向导

```
openclaw onboard --install-daemon
```

详细安装指引请参考下文第三节 初始化配置向导

检查运行状态

```
openclaw gateway status
```

打开控制界面

```
openclaw dashboard
```

如果以上操作安装失败/网速缓慢或想尝试手工安装，请参考下方手工安装指南。

---

1 环境准备与依赖安装

### 1.1 系统要求

* **操作系统**：Windows 10/11（64位）、macOS 12+、主流Linux发行版
* **硬件配置**：CPU 2核心以上，内存 2GB以上，可用磁盘空间 10GB以上
* **网络环境**：需能正常访问国内镜像源（本文提供国内源配置）

### 1.2 核心依赖：Node.js 安装

OpenClaw 基于 Node.js 运行，要求版本 **22.0.0 或更高**。

#### Windows 环境

1. 访问 Node.js 官网 下载 LTS 版本（如 v22.14.0）安装包。
2. 运行安装程序，按默认设置完成安装。**务必确保安装过程中勾选“Add to PATH”选项**。

   ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HmaGibWBicEElrEucmrn6yzWicS2d5MAB1ksYicmwkR9ArJXwK0RzQvFbaEY3YwKJ3g7WBC0DJNISMWttiaF6jr9QtC2SAvT7yRg9fN8iaBKFYIwM/640?wx_fmt=other&from=appmsg)
3. 安装完成后重启系统，打开命令提示符（cmd）执行验证：

```
node-v
```

若输出类似 `v22.14.0` 的版本号，则安装成功。

#### macOS 环境

推荐使用 Homebrew 安装：

```
/bin/bash -c"$(curl-fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"brew installnode
```

#### Linux 环境（以 Ubuntu 为例）

```
curl-fsSL https://deb.nodesource.com/setup_22.x | sudo-Ebash -sudoapt-getinstall-y nodejs
```

## 2 OpenClaw 核心程序安装

### 2.1 配置国内镜像源（可选但推荐）

为加速下载，可将 npm 源切换至国内镜像：

```
npm config set registry https://registry.npmmirror.com
```

2.2 全局安装 OpenClaw

执行以下命令安装最新版本：

```
npm install-g openclaw@latest
```

安装过程通常持续1-2分钟，无额外交互。

2.3 验证安装

```
openclaw -v
```

### 成功输出版本号（如 `1.2.0`）即表示安装完成。

### 如果中途出现报错，类似这种的红色提醒，直接截图发给DeepSeek，能解决90%的问题。

## 3 初始化配置向导

通过内置向导可完成基础配置，包括模型选择、工作区设置、后台守护进程等。

### 3.1 启动向导

执行命令并附带 `--install-daemon` 参数以安装后台守护进程（确保服务在终端关闭后持续运行）：

```
openclaw onboard --install-daemon
```

3.2 向导步骤详解

向导启动后将依次呈现以下配置项，用户需使用键盘方向键选择并回车确认。

#### 步骤1：安全确认

* **界面**：显示安全风险提示，询问是否继续。
* **操作**：选择 `Yes` 确认。

#### 步骤2：配置模式选择

* **选项**：`QuickStart`（快速开始） / `Manual`（手动）
* **推荐**：选择 `QuickStart`，该模式采用预置合理参数，避免手动配置失误。

#### 步骤3：AI 模型提供商选择

* **列表**：包含 Anthropic、OpenAI、Qwen、Moonshot、GLM 等主流模型。
* **操作**：

+ 若已获取 API Key，选择对应提供商（国内用户建议选 Qwen、Moonshot 或 GLM），按提示粘贴密钥。
+ 若无 API Key，可选择 `Skip for now` 暂不配置，后续可通过配置文件补充。

#### 步骤4：具体模型版本指定

* 若上一步选择了提供商，此处需指定模型版本（如 `qwen-max`、`moonshot-v1-8k`）。
* 若跳过了提供商，可任选一个临时模型，后续可覆盖。

#### 步骤5：通讯渠道配置

* **列表**：飞书、Telegram、Discord 等。
* **操作**：选择 `Skip for now` 跳过，避免因渠道配置复杂导致流程中断。

#### 步骤6：扩展技能（Skills）安装

* **询问**：是否立即安装技能。
* **操作**：选择 `No`，后续按需添加。

#### 步骤7：启动方式选择

* **选项**：

+ `Hatch in TUI`：终端界面使用
+ `Open the Web UI`：打开网页控制面板（推荐）
+ `Do this later`：稍后手动启动

* **操作**：选择 `Open the Web UI`。

### 3.3 完成初始化

向导执行完毕后，终端将输出控制面板访问地址，格式如下：

```
Dashboard running at: http://127.0.0.1:18789/?token=your_secret_token
```

将该地址复制到浏览器中打开，即可进入 OpenClaw 网页控制面板。

> **注意**：URL 中的 `token` 参数是登录凭证，需妥善保管。若遗忘，可通过 `cat ~/.openclaw/openclaw.json` 命令查看。

## 4 界面汉化

OpenClaw 原生界面为英文，可通过语言包实现汉化。

1. **下载中文语言包**（需可访问 GitHub）：

```
git clone https://github.com/openclaw-cn/openclaw-lang-zh.git ~/.openclaw/lang
```

2. 修改配置文件

编辑 `~/.openclaw/openclaw.json`，添加以下内容：

```
"lang":{"default":"zh_CN","path":"~/.openclaw/lang"}
```

3. 重启服务

```
openclaw gateway restart
```

刷新浏览器，重新打开控制面板即可显示中文界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HmaGibWBicEEnv7icKLDUx25atcOXKib5mR61PyS4nYn1eqibLj4qHhKn8elo8vY745FBbwNK1HZWiaSl8OQkoyBgicUiahib1icJMwb7CCSeUMIcFDCw/640?wx_fmt=other&from=appmsg)

## 5 初次使用：添加模型并开始对话

### 5.1 通过控制面板添加模型

1. 在浏览器中打开控制面板（地址见3.3节）。
2. 导航至“设置” → “模型提供商”。
3. 点击“添加提供商”，选择所需模型（如 Moonshot），填写：

* **API Key**：从模型官网获取的密钥。
* **模型名称**：如 `moonshot-v1-8k`。
* **Base URL**（可选）：部分模型需指定，通常默认可留空。

4. 保存配置。

### 5.2 发起首次对话

1. 进入“聊天”界面。
2. 在顶部模型下拉菜单中选择已配置的模型。
3. 输入消息并发送，观察模型返回结果。

## 6 常见问题排查

| 现象 | 可能原因 | 解决方案 |
| --- | --- | --- |
| 安装卡顿或超时 | npm 默认源速度慢 | 执行 `npm config set registry https://registry.npmmirror.com` 后重试 |
| `openclaw` 命令未找到 | Node.js 未正确添加到 PATH | 重新安装 Node.js 并勾选“Add to PATH”；或手动将 Node.js 安装路径加入系统环境变量 |
| 控制面板无法访问 | Gateway 服务未启动 / 端口被占用 / token 错误 | 执行 `openclaw gateway start` 手动启动；检查端口18789是否被占用；核对 token 是否与命令行输出一致 |
| 模型返回“Invalid API Key” | API Key 错误、过期或权限不足 | 重新从模型官网获取有效 Key，并在控制面板中更新；检查账户余额 |

## 7 进阶配置参考

### 7.1 配置文件位置

主配置文件位于 `~/.openclaw/openclaw.json`，可手动编辑调整各项参数。

### 7.2 国内大模型配置示例（以 Moonshot 为例）

在配置文件中添加以下 providers 段：

```
"models":{"mode":"merge","providers":{"moonshot":{"baseUrl":"https://api.moonshot.cn/v1","apiKey":"your-moonshot-api-key","api":"openai-completions","models":[{"id":"moonshot-v1-8k","name":"Moonshot 8K"},{"id":"moonshot-v1-32k","name":"Moonshot 32K"}]}}}
```

修改后需执行 `openclaw gateway restart` 使配置生效。

### 7.3 飞书机器人对接概述

1. 在飞书开放平台创建企业自建应用，开启机器人能力。
2. 配置应用权限（消息读写、群组等）并发布。
3. 安装 OpenClaw 飞书插件：

```
openclaw plugin install @openclaw/channel-feishu
```

4. 通过 `openclaw configure` 进入渠道配置，选择飞书并填写 App ID / Secret。

5.重启网关后，将机器人添加到飞书群即可使用。

---

本文档旨在提供清晰、无歧义的安装指导，所有操作均基于 OpenClaw 最新版本（截至2026年3月）验证。若遇到未涵盖的问题，建议查阅官方文档或检查社区更新。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWyloZOSdbGl9MB8Ef3JM0WKdpiazPppKm6z0UMEQO2de0DIa0BkfoTp2HeyVjPuMxN5MXXW5tmzvEu1jQ/0?wx_fmt=png)

网络安全研究站

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/15HGVMWyloZOSdbGl9MB8Ef3JM0WKdpiazPppKm6z0UMEQO2de0DIa0BkfoTp2HeyVjPuMxN5MXXW5tmzvEu1jQ/0?wx_fmt=png)

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