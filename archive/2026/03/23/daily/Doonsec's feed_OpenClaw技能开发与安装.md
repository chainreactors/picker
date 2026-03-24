---
title: OpenClaw技能开发与安装
url: https://mp.weixin.qq.com/s/msimubQn4jsuMSR97Nu0Ug
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:13:17.217421
---

# OpenClaw技能开发与安装

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BowImrBK4tLoSPkQGwnu6Ev8MfyjmEjGPHKOkXL8W8YOeAqRmEPO7ujMaWticZQ8Aomib1lohvLbFTnAPCia0rRNiaghstOGdpibbPibaRxa7Fj2A/0?wx_fmt=jpeg)

# OpenClaw技能开发与安装

原创

adra1n
adra1n

YY的黑板报

![]()

在小说阅读器中沉浸阅读

在 OpenClaw (Molt) 生态中，Python 技能（Skills）是扩展 AI 边界的核心方式。通过官方 **`skill-creator`**自动化开发，并采用 **文件夹直放**的方式，可以实现从创意到功能的快速落地。

### 一、 开发阶段：利用 `skill-creator`自动化

不再需要手动配置繁琐的 YAML 和文件结构，直接让 AI 帮你初始化：

1. **准备环境**：确保你的 OpenClaw 环境已加载官方 `skill-creator`技能。
2. **指令生成**：向 OpenClaw 发送指令：**“调用 skill-creator 帮我写一个 Python 技能，功能是 [上传 Markdown 到微信公众号]”**。
3. **产出结构**：AI 会在 `./workspace/skills/`目录下自动创建文件夹，包含：

* **`SKILL.md`**：核心元数据文件，定义技能名称、版本及 AI 触发指令。
* **`main.py`**：存放实际的 Python 业务逻辑代码。
* **`requirements.txt`**：列出 `requests`等第三方库依赖。

---

### 二、 安装阶段：加载本地技能

由于 `clawhub install`等旧版指令已废弃，现在的安装流程已简化为“文件即技能”：

1. **路径直放**： 将你的技能文件夹直接移动（或解压）到 OpenClaw 安装目录下的 **`./workspace/skills/`**目录中。
2. **热加载刷新**： 在 OpenClaw 的 TUI 界面输入指令 **`/reload`**（或直接重启服务进程）。
3. **验证状态**： 在对话框输入 **`/skills`**，确认列表中已出现你刚才创建的技能名称。

---

### 三、 本地测试阶段：通用 `.zip`格式

如果你需要将技能发送到其他本地端进行测试，直接将其打包为标准 **`.zip`**压缩包即可，无需特殊后缀。

#### Linux 命令行打包：

```
# 进入技能文件夹内部
cd upload-md-to-wechat
# 将内容压缩为 .zip 包（确保 SKILL.md 位于压缩包根目录）
zip -r ../upload-md-to-wechat.zip ./*
```

*注：接收者只需将该 `.zip` 解压到其 `workspace/skills/` 目录下即可完成安装。*

### 四、 发布阶段：上传到 ClawHub 社区

如果你想将技能分享给全球用户，可以将其发布到官方的 ClawHub 技能市场。

1. **登录账户**： 在终端执行以下命令（需关联 GitHub 账号）：

   ```
   clawhub login
   ```
2. **执行发布**： 进入你的技能文件夹所在目录，运行发布指令：

   ```
   clawhub publish ./upload-md-to-wechat
   ```

   *系统会自动完成打包、版本校验并将其同步至云端商店。*

---

### 四、 避坑与调试指南

* **手动补全依赖**：OpenClaw 不会自动执行 `pip`。安装技能后，请务必在技能目录下手动执行：`pip install -r requirements.txt`。
* **权限授予**：若 Python 脚本涉及网络请求（如调用微信 API），需在 Web 控制台的 **Permissions** 中确认已勾选 **Network Access**。
* **日志排查**：如果 AI 调用技能失败或无响应，可在终端输入 **`/logs`** 查看具体的 Python 运行时报错信息。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

YY的黑板报

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SvuJD1DySG2d6mQWxGEyagnIWESbzcu70bFm0XE7XrypIlcD3ic3MJ28Xibqic0Crfaltk51bVKOibr7Xg0fGASj9Q/0?wx_fmt=png)

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