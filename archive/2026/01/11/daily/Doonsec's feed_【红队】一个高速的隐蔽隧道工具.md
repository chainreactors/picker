---
title: 【红队】一个高速的隐蔽隧道工具
url: https://mp.weixin.qq.com/s/WLi94l-orx4tx52HrPqgGw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:35:48.227935
---

# 【红队】一个高速的隐蔽隧道工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lcbWX2ticDCCpOtN295PG8PicFiawZjOBib2CibDN0pR2xUWjc1iaibPaX4ibkZZSUwLEl5w7Nwy8gwXRsOn5fiaSIZ7pAg/0?wx_fmt=jpeg)

# 【红队】一个高速的隐蔽隧道工具

purpose168

贝雷帽SEC

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

![](https://mmbiz.qpic.cn/mmbiz_gif/HVNK6rZ71oofHnCicjcYq2y5pSeBUgibJg8K4djZgn6iaWb6NGmqxIhX2oPlRmGe6Yk0xBODwnibFF8XCjxhEV3K7w/640?wx_fmt=gif&wxfrom=13&wx_lazy=1&tp=wxpic)

本公众号所提供的文字和信息仅供学习和研究使用，请读者自觉遵守法律法规，不得利用本公众号所提供的信息从事任何违法活动。本公众号不对读者的任何违法行为承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具介绍**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

smtp-tunnel-proxy 是一个高速的隐蔽隧道工具，主要通过伪装TCP流量为SMTP电子邮件通信以绕过深度包检测（DPI）防火墙。

## 功能特性

| 功能 | 描述 |
| --- | --- |
| 🔒 **TLS 加密** | STARTTLS 后所有流量使用 TLS 1.2+ 加密 |
| 🎭 **DPI 规避** | 初始握手模仿真实 SMTP 服务器（Postfix） |
| ⚡ **高速传输** | 握手后使用二进制流式协议 - 最小开销 |
| 👥 **多用户支持** | 每用户独立密钥、IP 白名单和日志设置 |
| 🔑 **身份验证** | 每用户使用 HMAC-SHA256 预共享密钥 |
| 🌐 **SOCKS5 代理** | 标准代理接口 - 适用于任何应用程序 |
| 📡 **多路复用** | 单个隧道支持多个连接 |
| 🛡️ **IP 白名单** | 按用户通过 IP 地址/CIDR 进行访问控制 |
| 📦 **简易安装** | 一键安装服务器并配置 systemd 服务 |
| 🎁 **客户端包** | 为每个用户自动生成 ZIP 文件 |
| 🔄 **自动重连** | 客户端在连接断开时自动重连 |

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐      ┌──────────────┐│ 应用程序     │─────▶│   客户端    │─────▶│   服务器     │─────▶│   互联网     ││  (浏览器)    │ TCP  │ SOCKS5:1080 │ SMTP │  端口 587   │ TCP  │              ││             │◀─────│             │◀─────│             │◀─────│              │└─────────────┘      └─────────────┘      └─────────────┘      └──────────────┘                            │                    │                            │   看起来像          │                            │   电子邮件流量      │                            ▼                    ▼                     ┌────────────────────────────────┐                     │     DPI 防火墙                 │                     │  ✅ 看到的是：正常的SMTP会话    │                     │  ❌ 无法看到：隧道数据          │                     └────────────────────────────────┘
```

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

**工具使用**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
工具配置详情可查看项目：🌐 配置您的应用程序将 SOCKS5 代理设置为：127.0.0.1:1080🦊 Firefox设置 → 网络设置 → 设置手动代理配置SOCKS 主机：127.0.0.1，端口：1080选择 SOCKS v5✅ 勾选"使用 SOCKS v5 时代理 DNS"🌐 Chrome安装"Proxy SwitchyOmega"扩展程序创建配置文件，设置 SOCKS5：127.0.0.1:1080🪟 Windows（系统级）设置 → 网络和 Internet → 代理 → 手动设置 → socks=127.0.0.1:1080🍎 macOS（系统级）系统偏好设置 → 网络 → 高级 → 代理 → SOCKS 代理 → 127.0.0.1:1080🐧 Linux（系统级）export ALL_PROXY=socks5://127.0.0.1:1080💻 命令行# curlcurl -x socks5h://127.0.0.1:1080 https://ifconfig.me# gitgit config --global http.proxy socks5://127.0.0.1:1080# 环境变量export ALL_PROXY=socks5://127.0.0.1:1080✅ 测试连接# 应该显示您的 VPS IP 地址curl -x socks5://127.0.0.1:1080 https://ifconfig.me
```

**下载链接**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

回复关键字【260112】获取下载链接

End

“点赞、在看与分享都是莫大的支持”

**工具精选**

![](https://mmbiz.qpic.cn/mmbiz_gif/4yJaCArQwpACMJuBxI11jPgvHCxQZFQxPrt5iaQRibgGl0aIzFo4hDCYcFuyViag6zhuqNEjjeasfMEAy1rkaOahw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

[【红队】Webshell 管理与后渗透平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494098&idx=1&sn=cb7bc8f3cc7f59e6f80f4b56e7d4c1f9&scene=21#wechat_redirect)

[【红队】BProxy - 多级 SOCKS5 代理工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494084&idx=1&sn=dbc658a17e6ddc0dcd7c7857c841478a&scene=21#wechat_redirect)

[【红队】攻击面管理平台 (ASM)](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494076&idx=1&sn=e9c2ff60ccd065dc223c71042515268d&scene=21#wechat_redirect)

[【红队】ParrotOS 7.0 正式发布 代号：Echo](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247494038&idx=1&sn=243e1105a439eb986fdc34534e6a8d19&scene=21#wechat_redirect)

[【红队】一款专为红队打造的主动资产指纹识别工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493898&idx=1&sn=3e395ade15061739c89f5d0a13645af4&scene=21#wechat_redirect)

[【蓝队】SamWaf开源轻量级网站防火墙](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493939&idx=1&sn=e56702a24dcae461024668aaea6aced3&scene=21#wechat_redirect)

[[蓝队] FastMonitor - 网络流量监控与威胁检测工具](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493925&idx=1&sn=a952c400c3ee63c8401ff57692745dd1&scene=21#wechat_redirect)

[【蓝队】漏洞全生命周期管理平台](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493803&idx=1&sn=10daa12b5a3523bf4a1ecc665890f917&scene=21#wechat_redirect)

[【蓝队】蓝队Ark神器 OpenArk v1.5.0](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493788&idx=1&sn=91a31e2d507cb9e0111c19dac98b315e&scene=21#wechat_redirect)

[【红队】矛·盾 武器库 v3.2](https://mp.weixin.qq.com/s?__biz=Mzk0MDQzNzY5NQ==&mid=2247493701&idx=2&sn=9cf7e304fee21328bac6d9bd97b81183&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/pM2klgicgT5dylTzXyrXBmex6dlAsZ0QJOQdzqcw2HpC49rnL0dTHNsWsOze4QmRYN7fPRoLdVK5MXs0DXtOvZw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

贝雷帽SEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lcbWX2ticDCAOTEpzWaKCrzpsFeD3icYkGgVtUujgdbvmcria9XiaA4DMcYYnPh5ic6aFXVQPX7lNH11yfUEicgicXIZA/0?wx_fmt=png)

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