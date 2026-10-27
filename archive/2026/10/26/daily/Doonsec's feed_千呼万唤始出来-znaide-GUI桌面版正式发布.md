---
title: 千呼万唤始出来-znaide-GUI桌面版正式发布
url: https://mp.weixin.qq.com/s/qFBzJ2FyVCENKzhlb0bCRw
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:00:23.038532
---

# 千呼万唤始出来-znaide-GUI桌面版正式发布

# 千呼万唤始出来-znaide-GUI桌面版正式发布

原创

zngeek
zngeek

蓝极战队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DM6Asdj5iafV4tUJTVeF2OzDsVXOdYicg1JicwJvoXJjay62fibuoz4Clu3cpCwLIctb9HxVRtt7RZejrgxZp8Vic5C0s5lEnoKUfV56qrQ0g1ak/640?wx_fmt=png&from=appmsg)

先说结论：**终端里的 znaide，现在有一个能双击打开的桌面版了。**它叫「修凡AI全能助手」，版本 V0.0.1，底层是 znaide 引擎 V1.1.0 —— 同一套 agent 循环、同一份配置、同一批会话记录，只是把交互从终端搬进了原生窗口。

Windows 有安装包（免管理员），Linux 有 AppImage，源码 AGPL-3.0 双端开放。

---

## 为什么又做一个桌面版

znaide 本来是纯终端工具：单文件、零运行时依赖，改文件、跑命令、查资料都在一个窗口里完成。对常年开着终端的人来说这很爽，但有两个现实问题：

1. **门槛**。想推荐给不写代码的朋友，第一句话就得教他"打开终端、cd 到目录、输入命令"。
2. **阅读体验**。模型回复里的表格、代码块、长文，在终端里只能算"能看"。

所以桌面版的目标很明确：**不改变引擎，只换一层壳**。所有能力仍然由 znaide 引擎提供，桌面版负责把它变成一个正常的桌面软件 —— 有窗口、有侧栏、有设置页、有安装包。

![](https://mmbiz.qpic.cn/mmbiz_png/DM6Asdj5iafWEbTc7LlhRABPFT7tb10kps6KtSOyGdGvuNDUD5QOUm0LicowRNKyTsIJMGcdKts4Gla5ghv0AoaDic1tqWpRekdLw6n929jFtQ/640?wx_fmt=png&from=appmsg)

---

## 它长什么样

* 左边是**会话侧栏**：搜索、新建、备注、删除，点一下就恢复。
* 中间是**对话区**：Markdown 渲染、代码高亮、流式输出。
* 顶栏是一排**状态胶囊**：权限档位、当前模型、人格、工作目录、上下文占用。
* 底部是输入框，`Enter` 发送，`Shift+Enter` 换行。

窗口是**系统原生 WebView**（Windows 用 WebView2、Linux 用 WebKitGTK、macOS 用 WKWebView），不是套壳浏览器，也不是终端模拟器。所以滚动、输入法、复制粘贴、字体缩放都是系统级行为。

---

## 功能详解

### 1. 工具调用全程可见

这是它和"聊天框套 API"最大的区别：znaide 会自己决定调用什么工具，而桌面版把每一步都摊开给你看。

* 卡片标题下有一行浅灰小字，显示**这次到底调了什么**（比如 `$ ls -la ~/Downloads/*.png`）。
* 执行过程中，卡片下方有**实时输出区**，命令在跑就能看到输出，不用盲等。
* 跑完保留结果；历史会话回放时，调用参数和结果同样成对展示，不会只剩一句"已调用工具"。

看到不对，直接按 `Esc` 中断。

### 2. 输入效率：`/` 和 `@`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DM6Asdj5iafVzbbMa9E2gz4V18FmlFGsGiaBtfMqZdwzMbybiaibGByVQLkbVSh1RdxgDPR0CBHlmSnqgtrcyox7ec1rYyCDMsZIkKBsXjIXyqA/640?wx_fmt=png&from=appmsg)

输入 `/` 弹出命令面板：内置命令 + 你装过的技能，边打边过滤，`↑↓` 选、`Tab`/`Enter` 采纳。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DM6Asdj5iafXkUcOstdU5sicuIbfAdmKR39raqzPjGA2Bkia6JzefWs5216yj4ibHicspiaw5zeibeY1ceic71gjKGHZvibiaAIOMjkAhbO3mfxPRH47c/640?wx_fmt=png&from=appmsg)

输入 `@` 弹出文件/目录补全：`@crates/` 可以逐层进去，选中即把文件内容（或目录清单）注入给模型。**带空格的路径**会自动写成 `@"我的 文件.txt"`，不用手动转义。

另外两个细节：

* **工作中输入会排队**，在下一个轮次边界插进对话，不会被丢掉；排错了可以撤回。
* 中文输入法下按 `Enter` 不会误发（判断的是组合状态）。

### 3. 会话管理

侧栏按时间列出历史会话，支持搜索、备注、删除。两个容易被忽略但很实用的点：

* **点击会话会自动切到它记录的工作目录**。昨天在 `/home/me/work/api` 里聊的项目，今天点回来，`cwd` 胶囊跟着变，`@` 补全也立刻对准那个目录。
* **当前会话始终在列表里**（哪怕刚新建、还没有消息），不会出现"切走了就回不来"。

会话文件和终端版完全共用，`--resume` 的片段匹配规则也一样。

### 4. 设置是一整页，不是一堆弹窗

![](https://mmbiz.qpic.cn/mmbiz_png/DM6Asdj5iafVlXtXYwh5YBCjAibO7jLialqt9c7qyz25qgSDNER4ojWuoN2GpROeHT3rbhpOorCdxBc8Tq5fIsnHUUqCdYia9eelby1uRmeTzKc/640?wx_fmt=png&from=appmsg)

七块内容，全部落盘到 `~/.znaide/config.json`，和终端版共享：

| 分块 | 能改什么 |
| --- | --- |
| 服务商与模型 | 内置 ollama / dashscope / deepseek / openrouter / zai，也能填任意 OpenAI 兼容端点；自动拉 `/models` 列真实模型 |
| 上下文与预算 | 上下文窗口（留空 = 按模型名自动查表）、单条消息轮数上限、弱网重试次数 |
| 网络 | 代理三档：跟随环境变量 / 强制直连 / 手动指定；可加自定义请求头（网关计费、审计用） |
| 人格 | 选预设或自己写一份，全局生效 |
| 技能 | 列出三层目录里的技能，可编辑正文（内置只读） |
| 记忆 | 全局 / 项目两级，新建、编辑、删除 |
| MCP | 直接编辑 `mcp.json`，保存前校验 JSON |

改完保存立即生效，不用重启。

### 5. 权限与安全

沿用引擎的四档权限：**询问 / 编辑放行 / 全自动 / 超级**，顶栏胶囊随时切。

危险命令不是靠关键词匹配，而是先做词法切分、解析出真正的目标路径再判断：目标是根目录、家目录、当前工作目录或其上级、块设备，或者**判不出来**，就弹红色确认框，只允许单次放行。`rm  -rf /`（多打空格）照样命中，`rm -rf /tmp/123` 正常放行。

还有两个兜底：改文件前自动快照（`undo` 可回滚），以及长对话的上下文压缩。

### 6. 更新走独立通道

桌面版和终端版的版本线是分开的：

* 终端版：`v1.x` 标签，资产名 `znaide-*`
* 桌面版：`gui-v*` 标签，资产名 `xiufan-*`

结果是：**桌面版更新永远不会把终端版换掉**，反之亦然。窗口里「设置 → 关于与更新」点一下就行，装在自己的用户目录，不需要管理员权限。

---

## 安装

### Windows（推荐安装版）

| 文件 | 说明 |
| --- | --- |
| `xiufan-windows-x64-v0.0.1-setup.exe` | 安装版。装到 `%LOCALAPPDATA%\Programs\修凡AI全能助手`，**不弹 UAC**；带开始菜单/桌面快捷方式，可在"设置 → 应用"里卸载 |
| `xiufan-windows-x64-v0.0.1.exe` | 绿色版。单文件双击即用，不写注册表 |

两个注意点：

1. 需要 **WebView2 运行时**。Win10/11 一般自带；缺失时安装程序会问一次要不要打开官方下载页（约 2MB）。缺运行时的表现是**窗口空白**，不是报错。
2. 目前**没有代码签名**，首次运行会看到 SmartScreen 提示，点「更多信息 → 仍要运行」即可。
3. 卸载默认**保留** `%USERPROFILE%\.znaide`（会话、配置、记忆都在里面），只有当场选"是"才连数据一起删。

### Linux

```
chmod +x xiufan-linux-x64-v0.0.1.AppImage
./xiufan-linux-x64-v0.0.1.AppImage
# 没有 FUSE 时:
./xiufan-linux-x64-v0.0.1.AppImage --appimage-extract-and-run
```

需要系统装 `webkit2gtk-4.1`（Debian/Ubuntu：`libwebkit2gtk-4.1-0`）。也可以下 `tar.gz` 解包直接用里面的二进制。

### macOS

这一版**没有**提供 `.app`：WKWebView 的产物必须在 macOS 本机构建。想自己来：`make package-gui-macos`。

### 和终端版共存

两者共用 `~/.znaide`。终端里聊到一半，关掉终端打开窗口，侧栏里能接着聊；反过来也一样。装一个不会影响另一个。

---

## 已知限制（如实写）

* 所有平台都**未签名**：Windows SmartScreen、macOS Gatekeeper 会拦一次。
* macOS 暂无产物，需在 Mac 上自行构建。
* 只有 x64（Windows / Linux）；macOS 构建脚本支持 arm64。
* Windows 安装版只做"当前用户安装"，不写 `Program Files` —— 这是为了让应用内更新不需要提权。需要全机器安装的话，目前只能自己放绿色版。

---

## 下载与源码

**源码（AGPL-3.0，商用/闭源集成需商业授权，见仓库 COMMERCIAL.md）**

* GitHub：https://github.com/twowb/znaide
* Gitee：https://gitee.com/brother-ershui/znaide

**桌面版 V0.0.1（Windows 安装包 / 绿色版 / Linux AppImage / tar.gz）**

* GitHub Releases：https://github.com/twowb/znaide/releases/tag/gui-v0.0.1
* Gitee Releases（国内直连）：https://gitee.com/brother-ershui/znaide/releases/tag/gui-v0.0.1

**终端版（想要纯命令行的话）**

* 最新是 v1.1.1：https://github.com/twowb/znaide/releases/tag/v1.1.1
* 国内：https://gitee.com/brother-ershui/znaide/releases/tag/v1.1.1

两端发布的是**同一份文件**，sha256 完全一致，可以按网络情况就近下载。

---

## 最后

这是一个 0.0.1：功能已经能用，但细节肯定还有毛刺。用起来哪里别扭、哪里该有却没有，欢迎直接提 issue：

* https://github.com/twowb/znaide/issues
* Gitee 侧同样可以提：https://gitee.com/brother-ershui/znaide/issues

如果它帮你省下了几次"打开终端 → cd → 敲命令"的时间，那就值了。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ib5EIMWjNGUvyWgtD2MBDJv4LPiciaibpul3zMBowvr4zesS7A6lekoABh9ichkjyX9xVUiad3Cy1jzT2jjyLxzcMfSg/0?wx_fmt=png)

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