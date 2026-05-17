---
title: AI 驱动的红队免杀知识库 | Webshell 免杀、WAF/RASP/EDR 绕过、流量伪装等实战Tips
url: https://mp.weixin.qq.com/s/40xun7CtUT31EISAr98TMw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:46:54.050185
---

# AI 驱动的红队免杀知识库 | Webshell 免杀、WAF/RASP/EDR 绕过、流量伪装等实战Tips

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6O1Vbd2PnSEwz7HVzpbQkfoKzicsRYLrE09nFfwqDju8ZHsRrVFOGQ0eMvMOPwa4ePg75Y3zPSMSpLJngLBRWEkY5BtYZFW0qick/0?wx_fmt=jpeg)

# AI 驱动的红队免杀知识库 | Webshell 免杀、WAF/RASP/EDR 绕过、流量伪装等实战Tips

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## [![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6POcNFl23k1SSY97AuZmrzRD0rf1JaE5I9DzQf1JyFbjFAE8Or7uoQIFhfaxDTUEqvtBH6nTOOj0LwSfRbHKxtCl9A6oDTZxfI/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650617500&idx=1&sn=73c0634d23ef9a5a7ca009cf0e3b1929&scene=21#wechat_redirect)

## 这是什么

**AI Redteam Notes**这是一个 **AI 辅助生成** 的红队对抗技术笔记仓库。内容涵盖 Webshell 免杀、WAF/RASP/EDR 绕过、流量伪装等实战技术点。所有内容均由 AI 根据真实攻防经验整理、归纳、输出，再由人工验证后归档。作者：yunhai666

**核心理念**：不是堆砌工具和脚本，而是把每种绕过技术的**原理、适用场景、限制条件**讲清楚 — 让读者理解"为什么能绕过"而不是只会复制粘贴。

> 🤖 AI 驱动的红队免杀知识库 — 合法授权的渗透测试与安全研究
>
> 🛠️ Powered by **QwenPaw Desktop** + **DeepSeek V4 Pro**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNUiccOCrRuyuPRUOhFNtpqfyWkEPBCLiaSr9ib9LDLaVnAhiakibbwItj71ezA3FJq6sEGKzs0oAG1m33FiaLHC9toRADyYMsEuV9iac4/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=0)

## 当前内容

### 📄 PHP 免杀技术点清单

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNUrfTBb3x34QWibL5ia0TI8qTUic87qEwzUNIQ5ib0uwgfhliacABTFvtzyjYnxmDe3gdS0X3QQpgMqH3MNG2a5Aqo7lYSLSHcLyPrc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

PHP Webshell 生成的完整方法论，包含：

| 模块 | 内容 |
| --- | --- |
| **6 套技术方案** | gzip+base64 嵌套、动态函数名拼接、回调高阶函数、注释断裂+标签嵌套、RASP 专项绕过、协议上下文逃逸 |
| **组合策略** | 针对安全狗/云锁/长亭牧云/OpenRASP 的最优方案组合 |
| **哥斯拉 V3 微步 TDP 专项** | `include + tempnam` 替代 `eval`、左右追加随机字节、Header 验证、两阶段协议 MD5 前后缀避坑 |
| **实战踩坑清单** | 7 个典型翻车场景 + 根因 + 正确做法 |

每一步都标注了 **PHP 版本兼容性** 和 **绕过目标产品**。

### 📄 AdaptixC2 BOF 插件编写指南

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNXnVGzWN2koM0ntkBpRHATX9NBs9N58XNLlMN8bSMgXfIxSJiaMd2LYpsr0picAKY8cc1YoXTAEyZKtdNuBbswafXicptK2n5VUFs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

从 CS (Cobalt Strike) 移植 BOF 到 AdaptixC2 的完整教程，包含：

| 模块 | 内容 |
| --- | --- |
| **基础概念** | BOF/Beacon/AxScript 是什么、AdaptixC2 对 CS BOF 的兼容边界 |
| **项目结构** | 标准目录布局 + BOF 命名规范 |
| **AxScript 全解** | 命令注册、参数打包、PreHook/PostHook 编写、右键菜单 |
| **CS → AdaptixC2 映射表** | `bof_pack` 类型对照（`Z`→`wstr` 等）、API 一一对应 |
| **BOF 参数打包** | 5 种类型的含义与选型、字符串乱码根因与修复 |
| **踩坑清单** | Command not found / 用户名乱码 / menu.add() 报错 等经典问题 |
| **完整模板** | 可直接复用的 `.axs` 脚本骨架 |

配套实战案例：AddUser-BOF（NetUserAdd + SAMR 双路径）的完整移植。

### 📄 Java 免杀技术点清单 ⚠️ 未测试

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVBnmed8sgLHaOomTbaDtV70zAZg8JmHoVRnoOOuEYEGFicRibuMr1nUXRszaI4RP2ricwoicVs7k7QOSNQxUsPpepsXzbZ5vok2vw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)
> ⚠️ **注意：本清单为 AI 生成的技术框架，尚未经过各 JDK 版本 + 中间件组合的逐一实测验证。**
>
> Java 生态版本碎片化严重（JDK 8 / 11 / 17 / 21 × Tomcat 7-10 / Jetty / Spring Boot 2.x-3.x），全量兼容性测试工作量巨大。以下内容请在本地环境自行验证后再用于实战。

Java Webshell + 内存马的技术框架，包含：

| 模块 | 内容 |
| --- | --- |
| **5 套 Webshell 方案** | 多层嵌套反射 + 动态类名拼接、BCEL 字节码加载、URLClassLoader 远程加载、AES 混淆解密、JSPX XML 注入 |
| **5 种内存马** | Filter 型 / Servlet 型 / Listener 型 / Controller 型（Spring）/ Valve 型（底层） |
| **高阶对抗** | 类加载器隔离、反射链混淆、内存特征抹除、动态触发条件、环境感知、反调试检测 |
| **方案组合** | A+B 三重叠加 / A+C 远程加载 / D+Filter 内存马 / Controller+Valve 双绕过 |

每项标注了 **JDK 版本差异** 和 **目标中间件适配**，但未逐版本验证。欢迎提 PR 补充实测结果。

### 📄 Ghost Bits (Cast Attack) 技术总结

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNWbYgUOGBTiax7hHxs0Kfn5P7vqmkLZNW00Fll7JYnSG3vhrFwsbwgt0GrTnuQowzYWBaxszOGicdeOKEYvc8zoHa4V7e1MMFcCQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)
> 来源：Black Hat Asia 2026 — 浅蓝 @ AlibabaCloud

Java `char` 是 16 位，但大量 API 只取低 8 位，**高位被静默丢弃**——利用这个特性可构造不同解析器看到不同内容的攻击。涵盖：

| 模块 | 内容 |
| --- | --- |
| **9 种攻击技术** | BCEL ClassLoader 绕过、Jackson SQLi、Fastjson `\u`/`\x` 转义、Tomcat 文件上传、全角 URL 路径穿越、JDK Base64 解码、GeoServer RCE 绕过、Jetty 二次编码、SMTP 协议注入 |
| **Ghost Bit 字符映射表** | 10 组 Unicode → ASCII 的单向映射（`.``/``0`-`9``e``j``%` 等） |
| **4 个 CVE** | CVE-2025-41242 (Spring)、CVE-2025-7962 (SMTP)、CVE-2026-21933 (JDK)、CVE-2024-36401 (GeoServer) |
| **渗透实战** | 立即可用的 Payload 模板 + 自动化扫描脚本 + 代码审计关注点 |
| **供应链发现** | ActiveJ / Lettuce / XMLWriter / Jodd 等组件的 Ghost Bits 漏洞 |

## 为什么叫 "AI Redteam"

* **生成方式**：所有文档均由 AI 根据安全研究经验生成初稿，人工审核修正
* **迭代速度**：AI 能快速穷举绕过思路的变体，人负责验证和筛选
* **可复现**：Prompt 即方法论 — 同样的提示词框架可以迁移到其他语言/场景

这本质是一套 **"人定策略，AI 出内容"** 的安全知识生产流水线。

## 工具下载

```
https://github.com/yunhai666/ai-redteam-notes/tree/master
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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