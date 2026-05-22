---
title: AICryptoProxy：AI 驱动的 JS 逆向分析渗透测试自动化代理框架
url: https://mp.weixin.qq.com/s/l6YxR4KQkCS-_0BojVJWRA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:58:45.366089
---

# AICryptoProxy：AI 驱动的 JS 逆向分析渗透测试自动化代理框架

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L9cic5ql9ODy2r5aDicarErZJB0gS8Mf1TcxVvT2aIfSK9J3odXP8JQOMlYpdbkLewLicS5hRP2WApoEdY7aqG01RLAuCyZgbibibOACIWHficqn0/0?wx_fmt=jpeg)

# AICryptoProxy：AI 驱动的 JS 逆向分析渗透测试自动化代理框架

原创

0x八月
0x八月

0x八月

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# AICryptoProxy：AI 驱动的 JS 逆向分析渗透测试自动化代理框架

⚠️

    请勿利用文章内的相关技术从事**非法渗透测试**，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。**工具和内容均来自网络，仅做学习和记录使用，安全性自测，如有侵权请联系删除。**

⚠️注意：现在只对常读和星标的公众号才展示大图推送，建议大家把"**0x八月**"设为星标⭐️"否则可能就看不到了啦,点击下方卡片关注我哦！

**💡项目地址在文章底部哦！**

## 📖 项目/工具简介

  AICryptoProxy 是一个基于 Claude Code + MCP 的智能渗透测试框架，通过 AI 自动完成前端 JS 加密逻辑逆向，**一键生成可用的 mitmproxy 加解密代理**。

## 🚀 一句话优势

  输入目标 URL，几十秒自动完成前端加密逆向，**在 Burp 中操作明文请求**。

## 📋 核心能力速览

| 功能 | 说明 |
| --- | --- |
| 自动 JS 逆向 | AI 通过 MCP 自动搜索脚本、断点追踪并提取 Key 与算法参数 |
| 代理脚本生成 | 自动生成下游解密和上游加密的 mitmproxy 脚本 |
| 双模式支持 | 直接加解密模式 + JSRPC 零逆向桥接模式 |
| 一键启动 | AI 输出完整启动命令，无需手动调试代理脚本 |
| 动态 Key 适配 | JSRPC 模式让浏览器原生处理动态 Key 生成逻辑 |

## ✨ 核心亮点

### 1. AI 驱动的 JS 加密逻辑自动逆向

  传统前端加密分析需要手动搜索脚本、下断点、追踪调用链，耗时数小时。AICryptoProxy 通过 Claude Code 的 MCP 技能系统，在几十秒内自动完成：搜索脚本中的加密关键字（encrypt、AES、RSA 等），在断点处自动提取 Key、IV、算法参数，并生成完整的 mitmproxy 加解密脚本。整个流程**从“手动定位”变为“AI 自动追踪”**，大幅降低前端加密分析的门槛。

### 2. 双模式兼容：直接加解密 + JSRPC 零逆向

  框架提供两种互补的工作模式。**模式 A（Direct Crypto）** 适用于标准算法、Key 固定的场景，AI 直接提取 Key 并生成 Python 加解密代码。**模式 B（JSRPC Bridge）** 适用于算法复杂、混淆严重、Key 动态生成的场景，AI 自动生成 jsrpc\_inject.js 注入脚本和 jsrpc\_client.py 调用封装，让 *浏览器原生 JS 环境处理加密*，通过 WebSocket 桥接至 mitmproxy 脚本。两种模式由 Skill 自动判断并选择，无需人工干预。

### 3. 完整的 Burp 明文操作链路

  框架构建了一条从浏览器到服务器的完整加解密链路：浏览器 → 下游 mitmdump 自动解密 → Burp Suite（操作明文请求）→ 上游 mitmdump 自动加密 → 服务器。配置好浏览器代理为 8082（下游解密）和 Burp 上游代理为 8083（上游加密）后，测试人员**在 Burp 中看到的全是明文请求**，可自由修改和重放，而服务端收到的仍是合法的加密数据包。

## 🛠️ 技术优势

| 技术/特性 | 说明 | 优势 |
| --- | --- | --- |
| Claude Code + MCP | 通过 js-reverse MCP 连接浏览器调试 | AI 可自动搜索、断点追踪 JS 加密逻辑 |
| mitmproxy 脚本 | 生成 downstream 和 upstream 双代理脚本 | 实现浏览器到 Burp 的自动加解密流转 |
| JSRPC 桥接 | 通过 WebSocket 桥接浏览器原生 JS 环境 | 天然适配动态 Key 和高混淆场景 |
| PyCryptodome | 标准算法库支持 AES/RSA/SM4 等 | 直接加解密模式下保证算法兼容性 |
| Skill 工作流 | 交互式引导配置 + 一键执行 | 首次使用自动检测 .env，路径配置只需一次 |

## 📖 使用指南

① **准备工作** 确保环境满足 Python 3.12+，执行 `pip install mitmproxy pycryptodome requests` 安装依赖。下载并安装 Claude Code（https://claude.ai/code）和 js-reverse MCP 服务。首次运行 Skill 时，AI 会自动检测 `.env` 配置文件，并引导填写 **Chrome 浏览器路径**（模式 B 还需配置 JSRPC 服务端路径），AI 会验证路径有效性并保存。

② **核心操作** 在项目目录中启动 Claude Code，输入指令。模式 A：`"用 mitm_proxy 技能帮我分析 https://target.com 的加密逻辑，生成加解密代理"`。AI 会自动启动浏览器导航到目标，搜索加密代码，提取 Key 和算法参数，生成 `downstream_decrypt_proxy.py` 和 `upstream_encrypt_proxy.py`。如果浏览器弹出确认弹窗，**需要手动点击确认**，否则会卡住。模式 B：输入 `"用 jsrpc-mitm-auto 技能为 https://target.com 设置 JSRPC 加解密代理"`，AI 会生成 jsrpc\_inject.js 注入脚本，需手动在浏览器 Console 中粘贴执行。

③ **结果查看** AI 分析完成后，项目目录下会生成：`proxy_scripts/downstream_decrypt_proxy.py`（下游解密代理）、`proxy_scripts/upstream_encrypt_proxy.py`（上游加密代理）和 `ANALYSIS_REPORT.md`（加密分析报告）。AI 会输出完整的 **三个终端启动命令**：第一个启动 Burp Suite，第二个启动下游解密代理（`mitmdump -s ... --mode upstream:http://127.0.0.1:8080 -p 8082`），第三个启动上游加密代理（`mitmdump -s ... -p 8083`）。配置浏览器代理为 127.0.0.1:8082，Burp 上游代理为 127.0.0.1:8083，即可在 Burp 中操作明文请求。

## 📖 项目地址

```
https://github.com/hzhsec/AICryptoProxy
```

## 💻 技术交流与学习

如果师傅们想要第一时间获取到**最新的威胁情报**，可以添加下面我创建的**钉钉漏洞威胁情报群**，便于师傅们可以及时获取最新的**IOC**。

    如果师傅们想要获取网络安全相关知识内容，可以添加下面我创建的**网络安全全栈知识库**，便于师傅们的学习和使用：
覆盖渗透、安服、运营、代码审计、内网、移动、应急、工控、AI/LLM、数据、业务、情报、黑灰产、SRC、溯源、钓鱼、区块链等  方向，**内容还在持续整理中......**。

⚠️打广告的勿进，会直接踢掉！！！

| ![](https://mmbiz.qpic.cn/mmbiz_png/L9cic5ql9ODzDcbialtDJB2iauRibULjWbzQk2oeHEyuNcGjibhWw6SpJia0RYGY3D7UhMASYr1QPAicb1LaSL1XlDrVowaibjeB41IKYSBHE8z9sN8/640?wx_fmt=png&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODwMu4dL9ZhibwZKibzwdD01Btq6ia2183uH0ibzaGibkr1aribDe1jicrtW0px8pd6Rz1kT7QpTtzfdmicibiaFZHSqI40srWZhLQ9HpR1JY/640?wx_fmt=png&from=appmsg) |
| --- | --- |

### 推荐阅读

✦ ✦ ✦

| [渗透测试人员必备武器库：子域名爆破、漏洞扫描、内网渗透、工控安全工具全收录](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485592&idx=1&sn=818004a6d625c4c4112ce73b83433854&scene=21#wechat_redirect) |
| --- |
| [AI驱动的自动化红队编排框架(AutoRedTeam-Orchestrator)跨平台支持，集成 130+ 安全工具与 2000+ Payload](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485309&idx=1&sn=292afbe37fb95c64f33470f915b0c54e&scene=21#wechat_redirect) |
| [JS逆向必备：这款插件能Bypass Debugger、Hook CryptoJS、抓取路由](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247486181&idx=1&sn=3ace47da643c72cec0d615aeccb955ac&scene=21#wechat_redirect) |
| [上传代码即审计：AI 驱动的自动化漏洞挖掘与 POC 验证平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485488&idx=1&sn=a37acb031febe69db608de53ddee5732&scene=21#wechat_redirect) |
| [AI 原生安全测试平台(CyberStrikeAI)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485208&idx=1&sn=b5181181c1e0800124e3e099706ef2ef&scene=21#wechat_redirect) |
| [多Agent智能协作+40+工具调用：基于大模型的端到端自动化漏洞挖掘与验证系统](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485805&idx=1&sn=8f374a239135f6a753d5cce887f8318b&scene=21#wechat_redirect) |
| [基于DeepSeek的代码审计工具 (Ai-SAST-tool.xjar)](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485314&idx=1&sn=56082cd314311ffc15cc0bcf03a395e2&scene=21#wechat_redirect) |
| [基于AI的自主渗透测试平台](https://mp.weixin.qq.com/s?__biz=MzE5ODgwNzgzMA==&mid=2247485127&idx=1&sn=b5eb3fdc1cc23976011e2bca396c1bc7&scene=21#wechat_redirect) |

✦ ✦ ✦

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnAqueibZX8s1IJDIlA8UJmu3uWsZUxqahoolciaqq65A30ia93jCyEwTLA/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJniaq4LXsS43znk18DicsT6LtgMylx4w69DNNhsia1nyw4qEtEFnADmSLPg/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnev2xbu5ega5oFianDp0DBuVwibRZ8Ro1BGp4oxv0JOhDibNQzlSsku9ng/640?wx_fmt=gif&from=appmsg)

**点在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/AXRefkPRWsEZqurn2l5WTaTjyicrUtIJnwVncsEYvPhsCdoMYkI6PAHJQq4tEiaK3fcm3HGLialEMuMwKnnwwSibyA/640?wx_fmt=gif&from=appmsg)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

0x八月

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/L9cic5ql9ODxEb9kj2s0xfj49wycWpJlJYYzMflMiarFrZv4k6FxVzwtic65opL9vO55NibibVYyicXOeerVCRrxPicpxGm4dyAyPbmaciaaia0RFgms/0?wx_fmt=png)

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