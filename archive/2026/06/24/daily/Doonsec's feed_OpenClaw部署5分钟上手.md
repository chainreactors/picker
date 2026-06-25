---
title: OpenClaw部署5分钟上手
url: https://mp.weixin.qq.com/s/lcmj66gIN8guXxSTbB1fLw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:12.160559
---

# OpenClaw部署5分钟上手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N46S2sKsyICmGIHYNhBUPf6NqBP3ib8UaCcQavM1gmafDdsTnjI7AYRPvXJBXltXHB73HFPasb2CRUa50HJeLqGeBXRa4ib6wJ9monoDnCE2g/0?wx_fmt=jpeg)

# OpenClaw部署5分钟上手

原创

ladon
ladon

306Safe

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

OpenClaw（小龙虾）是2026年最火的开源AI智能体平台之一，核心定位是多渠道消息网关+AI任务执行。相比Hermes侧重"自进化记忆"，OpenClaw更擅长"多端互联+消息聚合"——它可以把微信、飞书、钉钉、Telegram等20+平台的消息统一接入，由AI自动处理和分发。

环境要求

| 依赖 | 要求 |
| --- | --- |
| Node.js | >= v22.14.0，推荐Node 24 LTS |
| Git | 源码安装必须，一键脚本可自动按需安装 |
| 网络 | 需访问npm/GitHub，国内建议配镜像加速 |

方案一：一键安装脚本（新手首选）

**macOS / Linux / WSL2：**

```
# 原版官方脚本 curl -fsSL https://openclaw.ai/install.sh | bash  # 国内社区加速脚本（推荐国内用户） curl -fsSL https://open-claw.org.cn/install-cn.sh | bash
```

**Windows PowerShell（管理员）：**

```
# 原版 iwr -useb https://openclaw.ai/install.ps1 | iex  # 国内加速版 iwr -useb https://open-claw.org.cn/install-cn.ps1 | iex
```

方案二：npm手动全局安装

```
# 校验Node版本 node --version   # 必须 >= v22.14.0  # 配置国内npm镜像（解决安装卡顿） npm config set registry https://registry.npmmirror.com  # 全局安装 npm install -g openclaw@latest  # 初始化配置向导 openclaw onboard
```

方案三：Docker容器部署（服务器首选）

```
# 拉取官方镜像 docker pull openclaw/openclaw:latest  # 启动（持久化配置+端口映射） docker run -d \   --name openclaw-gateway \   -p 18789:18789 \   -v ~/.openclaw:/root/.openclaw \   --restart always \   openclaw/openclaw:latest  # 进入容器初始化 docker exec -it openclaw-gateway openclaw onboard
```

常用命令速查

```
openclaw start            # 启动网关服务 openclaw stop             # 停止服务 openclaw logs --follow    # 实时查看日志 openclaw configure        # 重新配置（API密钥、机器人渠道） openclaw update           # 一键升级到最新版 openclaw doctor           # 环境自检排错
```

启动后浏览器打开 `http://localhost:18789` 即可访问Web管理面板。

初始化配置流程

2. 选择大模型服务商：OpenAI / Claude / 通义千问 / Ollama本地模型 / OpenRouter等
4. 填入API Key，按需配置接口代理
6. 配置消息渠道：Telegram、Discord、企业微信、Web控制台等
8. 设置访问白名单、管理员权限、安全密码
10. 完成后自动常驻后台运行

常见问题排坑

**openclaw命令找不到**：npm全局路径未加入系统环境变量，执行 `npm config get prefix` 查看全局路径，手动添加至系统PATH。

**端口18789被占用**：`lsof -i :18789`（Mac/Linux）或 `netstat -ano | findstr :18789`（Windows）查占用进程，kill或换端口 `openclaw start --port 18790`。

**依赖安装超时**：全程使用淘宝npm镜像，克隆源码用Gitee替代GitHub。

**Node版本过低**：用nvm管理多Node版本：

```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash source ~/.bashrc nvm install 24 nvm use 24 nvm alias default 24
```

OpenClaw vs Hermes怎么选？

| 维度 | OpenClaw | Hermes Agent |
| --- | --- | --- |
| 核心定位 | 多渠道消息网关 | 通用自进化智能体 |
| 记忆系统 | Markdown手动维护 | 五层自动记忆 |
| 自进化 | 手动创建技能 | 完整闭环自动沉淀 |
| Windows原生 | 支持 | 需WSL2 |
| 适用场景 | 跨设备AI入口 | 企业数字员工、长期协作 |

**建议**：如果你主要需要"多平台消息统一接入"，选OpenClaw；如果你需要"一个越用越懂你的AI同事"，选Hermes。两者还可以搭配使用——Hermes专注智能决策，OpenClaw负责消息分发。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rvkyDDyx4sv53bdQHLc9aiaciaqqxoojmXlic5HzYKRWCHnibkX1MXkqzL652lJpPoacJ8owSC6fuxHgnIgcWDVMIg/0?wx_fmt=png)

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