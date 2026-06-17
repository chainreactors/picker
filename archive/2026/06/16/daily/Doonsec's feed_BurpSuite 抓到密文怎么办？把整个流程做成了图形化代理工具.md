---
title: BurpSuite 抓到密文怎么办？把整个流程做成了图形化代理工具
url: https://mp.weixin.qq.com/s/-zbqW_orLoGq66X9NMy6gQ
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:00:54.528044
---

# BurpSuite 抓到密文怎么办？把整个流程做成了图形化代理工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MIGLFDXRTiaR3UdfAzhQDmicPquffP2pELYzZZRVMub92vribqebIj4sk6NmXqq0o73lSrxTyWXV7MuOcZXKOyZ4xoISvosfNvVUwoLz5kib904/0?wx_fmt=jpeg)

# BurpSuite 抓到密文怎么办？把整个流程做成了图形化代理工具

原创

赛赛
赛赛

W啥都学

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

面向APP/Web 加解密逆向分析、渗透测试人员的可视化解密框架

## 演示

## ✨ 为什么选择 CipherBridge？

在 APP 逆向、安全测试和接口联调过程中，经常会遇到：

* • 请求体经过 AES / DES / SM4 等加密
* • 参数或请求头带有 MD5 / SHA256 / HMAC 等签名
* • Burp Suite 抓到的全是密文，无法直接改包重放

密桥就是为了解决这些问题而生的。

## 🚀 核心特性

* ✍️ AI 自动生成 mitmdump 插件代码
* 🔐 可视化配置 AES / DES / 3DES / SM4 / RSA 等加解密流程
* 🌉 Burp Suite 双向加解密桥接
* 🧩 支持扩展自定义 Python 函数
* 🤖 浏览器 Hook + AI 自动分析生成脚本
* 🧪 内置加解密测试工具
* 🔍 自动识别 Base64 / Hex / JWT 等编码
* 📦 项目导入导出（`.cbproj.zip`）
* 🎨 深色 / 浅色主题切换
* 🌍 支持 Windows / macOS / Linux

## 环境要求

* • Python 3.10+
* • Windows / macOS / Linux

## 安装

```
# 克隆仓库后进入目录
git clone https://github.com/CuriousLearnerDev/CipherBridge.git
cd CipherBridge

pip install -r requirements.txt

# AI 自动化分析使用浏览器采集时需要（可选）
playwright install chromium
```

启动 GUI：

```
python gui.py
```

## 代理拓扑

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTqtKInq2gMAcGianZoiafo48JkSuOkflnlAiaDcLlic8Y5cEfKqqc3uqePFNyFS0qQ85V1r82gbhJvfmepOBPAQdSricjagAHNRJ70/640?wx_fmt=png&from=appmsg)解密端收到密文，解密后交给 Burp；Burp 改完请求后由加密端重新加密发出 若只需单向解密调试，可只启动解密端

## 📸 界面预览

### 首页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaSsianBuDoMACMf9L0pp14uOR4mMZs9GbicwybRzHNwZS9sY84yy5e917A9ic31FFzoNOeoLQV0fsc1xdUbdPfS8BgwSxlCIy9v9A/640?wx_fmt=png&from=appmsg)

### AI 自动化分析

点击「启动」后会打开浏览器，自动采集页面 JS 以及请求/响应数据，并尝试按内置规则匹配加解密方式。若规则未匹配成功，可使用 AI 辅助分析。

![AI 自动化分析 — 启动浏览器](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaRjaWWLXHa1Cs39A3q5Z78yBgTJKkxk7ibjP8PftviaTibAIUH94F0fo8duvhicZjUkWgyHyePJKWhcKeiamn3HFpSBvhQxa8PDM0lQ/640?wx_fmt=png&from=appmsg)

AI 自动化分析 — 启动浏览器

默认不启用 AI 时，会先按内置规则识别使用的加解密算法：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaSI2uXCkzPQ5B1JdtVPZwv57Cic75XZO1o2hU6Nia6VlonJEbWBGtNvfHDl4dwLibbd3Tqy739Dmibic4DqGgicKia1LianfJSbibwUp8Z4/640?wx_fmt=png&from=appmsg)

也可使用 AI 辅助分析加解密逻辑：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaQ0T4k4MfMgornygiapk1j3cHnw4vQkgJDibn1xNPnb4KpxXRHSrY1MTp5ibkzrKpNFWMic6UMqfhMXceciczXAdfrZefezVdjeFhec/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaQhWhhqDFhUIrLBB3KZ8J6ibr8shNSibxeWrh5No7CJC5dBEw5HdtEwClWx1aIZyRPWyhYX3aTJh320k6ptLmVeTQbtnNwia0gFwU/640?wx_fmt=png&from=appmsg)

分析完成后，可一键自动生成加解密代理代码：

![分析完成 — 生成代理](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaTy4eE5skA5fO0ic9xUSOFf9es0HJWmq0EFTIzmX2KmvmafwreleK0lJL1Kk5BIxwbKMgLwQEs6iajhqRibZ64K4W6mxJSKCAppuU/640?wx_fmt=png&from=appmsg)

分析完成 — 生成代理

生成的插件代码示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaTWIzIUCNmic3fXnKjQOP0RuIV02pnib9GOa8vS3icsNHAcPlaC3F7oxUhwrCT1aPZ08PuejLh4hHPOZ5ic3wmjibX8ciaaINa6Y7z14/640?wx_fmt=png&from=appmsg)

生成的步骤与代码会同步到「请求解析器」和「可视化构建器」：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaRD2Fxc727XMcj4VSDgaicqEtQohe1VjwiccMpQEfakM4g4OC21AibBzjc3kP5YNpXPUoqb1sqq6JURhHPmic9V7AEPGpqnA6MUwGM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaSabEB2oJYdLM52FY1QGQdR7KCPcgBLV2X2a6m1VGx2kpEibaVQFRSk853UGJyJ18nHr9gODCoxuSrS7eB2kVa37gfYsFl7YLoQ/640?wx_fmt=png&from=appmsg)点击左侧流量列表时，请求/响应详情显示在「请求/响应」Tab，不会覆盖 AI 分析结果。

### 请求解析器

粘贴请求/响应报文后点击「解析」，再点击需要解密的密文字段：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaQJT1xZ4afuUKralAHCSWwAkkia86ZwVBNWcBt3dCBrVrxjib4MOVf8M162ods6WmNCWW6ra2LFaFMlGiaeYib83Jhm0kSohKGbhsE/640?wx_fmt=png&from=appmsg)

选择解密方式并填写密钥等参数：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaRyhPFFJ923O0McShiaxJ26XicpgZk5qKiaonVWVpdohg7XPhk3PrtichWGicianCWJFOveUG2zmicxtEdsVxHksIN4oHX0kdr5rNZ7PU/640?wx_fmt=png&from=appmsg)

测试解密成功后点击「确定」：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTo7SC0Nc1gByEAQoKuTG5TI84nCczcsCV7OMeic8Fvmria4Eic0ywunGl5s4jlgdbLU1X4miaa4qvNxEEiaqzLibgr97wpDQic3icS74Q/640?wx_fmt=png&from=appmsg)

右侧会自动生成插件源码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaSTrrU40EgRG4iaMwcnYmr5ka2liaBsDKF3Z5NCSqXQAV0RcmnWN0Fj18eMHWwTnKt2licWsHlzmQrQhRkbht9fzm3sFia4hMKOVV0/640?wx_fmt=png&from=appmsg)

### 可视化构建器

无需粘贴报文，可直接通过步骤列表构建加解密流程，并提供 6 个通用案例模板：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MIGLFDXRTiaSPcr3ibLMN6IJWFJtCvf7OrdJ9jGVVw5oPic9S8k5mhmyWZ3HmEZ3TOUDw48kOwn8GVkhJ1ErsDY6Q82jWyqdVl7cadyJDXUbick/640?wx_fmt=png&from=appmsg)

### 插件编辑器

部分接口逻辑较复杂（如字符串反转、前后缀拼接、每次请求远程服务器获取签名字段等），可通过「插件编辑器」编写自定义 Python 函数：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaRnteibW7zKGJvjwpicyyKBiaKw4JHibTICAtOWnOG0hnHC3Flfuic4icgUgBhsXOwkfSP5WEgI8dsNCUsOBfCpXaOgxqAvdxfF26MUM/640?wx_fmt=png&from=appmsg)

编写并保存的扩展函数，可在配置加解密步骤时从下拉列表中选择调用：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaSUtQdBv2j1ZW8dsQceyxB6cMuJyoaKzaYaibD8At37evpXTrBGxRYT8HDKwbyZWyTBkeiaHmUSPdraOj3MZvAnPcSy2VgocgzwE/640?wx_fmt=png&from=appmsg)

### 加密分析

自动识别数据可能的编码类型（Base64 / Hex / JWT 等），基于本地规则匹配：

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaSR6zeBibsNo4CrXDQ8P1R5kibianG3ElOV7LGaBllcmjORKFEf9VfEwPxdCdT4gvFjgWalj5DLWSTd9zsQQgRf8Y59zyCKmkBQmM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaTRlac7zYVXfTHyk4qAE0K7WkfW7KrclkDX0Kgw0lOqvJMl2DXG9oNMvHibcstqqnKIJQeAYFhQCprmged4Wiaf5Yyu4ib6Cl6Wz8/640?wx_fmt=png&from=appmsg)

### 导入导出

若需长期对同一目标做安全测试，或需与他人协作，可使用项目导入/导出功能。左侧项目选择旁的 **⋯** 菜单 →「导出项目…」/「导入项目…」。

每个加解密方案 = 一个独立项目：

```
profiles/{name}.yaml     # 项目配置（名称、角色、匹配规则）
plugins/{name}/
├── plugin.py            # 生成的 mitmdump 插件（mitmdump -s 直接加载）
└── state.json           # 可视化步骤与解析器状态（自动保存，git 忽略）
```

**`.cbproj.zip` 包内文件**

| 文件 | 内容 |
| --- | --- |
| `manifest.json` | 格式版本、导出时间 |
| `profile.yaml` | 项目配置 |
| `plugin.py` | 加解密插件代码 |
| `state.json` | 可视化步骤（可选，有则包含） |

![](https://mmbiz.qpic.cn/mmbiz_png/MIGLFDXRTiaQw1icsic68BCC3u3sH4kicdeq7WOFl9icO0jibfIW4oq0QZRCCq9ibz5Hhk88lCOKtZ85APibtgFCYL7Em586BZHf1WQ7IaD1GB7heIo/640?wx_fmt=png&from=appmsg)

## HTTPS 证书

解密 HTTPS 流量需要信任 mitmproxy 根证书：

1. 1. 左侧解密端区域查看证书状态
2. 2. 点击「HTTPS 证书」或「设置」→「安装 HTTPS 证书」
3. 3. Windows 支持一键安装；macOS / Linux 会打开证书文件，需手动导入系统信任
4. 4. 重启浏览器后访问 `https://mitm.it` 验证

## 加载方式

「设置」中可选择 mitmdump 加载方式：

| 模式 | 说明 |
| --- | --- |
| **plugin.py 直接** （默认） | `mitmdump -s plugins/{name}/plugin.py` ，改代码后重启即生效 |
| **main.py 框架** | `mitmdump -s main.py` ，通过环境变量 `PROFILE` 加载，含匹配 / 日志钩子 |

## 配置

| 文件 | 说明 |
| --- | --- |
| `config/settings.yaml` | 界面主题（`dark` / `light`）、默认端口等 |
| `config/ai.yaml` | AI 自动化分析 API Key（复制 `config/ai.yaml.example`） |

主题切换：左侧「设置」→「界面主题」→ 保存，即时生效。

## 命令行启动（无需 GUI）

```
# 直接加载生成的插件
mitmdump -s plugins/myapp/plugin.py -p 8080

# 框架模式
set PROFILE=myapp          # Windows
export PROFILE=myapp       # macOS / Linux
mitmdump -s main.py -p 8080
```

## 目录说明

```
gui.py                 # GUI 入口
codegen.py             # 步骤 → 插件代码生成
sdk/                   # 加解密 / 签名 / 编码纯函数库
extensions/            # 自定义扩展（可在构建器中选用）
core/                  # 主题、项目 IO、证书、AI 等模块
profiles/              # 项目配置
plugins/               # 各项目生成的插件
hooks/                 # 浏览器 Hook 脚本（AI 自动化分析）
```

关注本公众号，回复关键字：解密 获取下载链接！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/b76VA5DEYFCiaFsTqv9xdrLthbcH4mXXCMWzKCib9LbsicaiauSk1FjDOumJb8LSbghnKZDPcWpbPR5uSZnoJ6UkhQ/0?wx_fmt=png)

W啥都学

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/b76VA5DEYFCiaFsTqv9xdrLthbcH4mXXCMWzKCib9LbsicaiauSk1FjDOumJb8LSbghnKZDPcWpbPR5uSZnoJ6UkhQ/0?wx_fmt=png)

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