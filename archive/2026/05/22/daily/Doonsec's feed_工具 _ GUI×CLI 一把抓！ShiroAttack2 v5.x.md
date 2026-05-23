---
title: 工具 | GUI×CLI 一把抓！ShiroAttack2 v5.x
url: https://mp.weixin.qq.com/s/Hex1BJRa4-K0Dd_nrMkTzg
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:36:42.928403
---

# 工具 | GUI×CLI 一把抓！ShiroAttack2 v5.x

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JpU6JH8dicqVPlEnptqjGd44CNAFssL16icGDSjuCpvTZoKj15gKVVQbGHic6w24NFrZ4fQs61HIVGvDVGsicZHuAgPYYMt3N2icIUGn627ctLjI/0?wx_fmt=jpeg)

# 工具 | GUI×CLI 一把抓！ShiroAttack2 v5.x

原创

mimi3389
mimi3389

赛博生存指南

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **地址：** https://github.com/SummerSec/ShiroAttack2
> SummerSec 大佬持续更新的Shiro工具，有2.5K+star。

里面的key`3c6e0b8a9c15224a`是写死的，可以考虑生成动态生成的。部分页面的加载也可以用AI写成异步的。打算下回实战测试和 https://github.com/wyzxxz/shiro\_rce\_tool的实战区别。下面是cc测试的截图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqUrKulFibaMZiaibSiaCmyyJw7PWaq3Z7114RC4OSOMIF3y8jPZ10uMPlwnib8nCWrCdoqhpF442Y3C3Rqs0v49lAIVrZ4xIkKMD7fE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JpU6JH8dicqXBcazH1U7Kd0IZoPPiamabwz3XEwb22nSiaVZDNGOB14RsvqRwMIMclq3WffmsknxKGTQDG6hSNDricSbOfUZW1yvYVtpmvawnkk/640?wx_fmt=jpeg&from=appmsg)

## Shiro-550 为什么还能用

2016 年的洞，到现在还能用。不是漏洞本身多高级，而是三个很现实的原因叠在一起。
**第一，默认Key。**Shiro 1.2.4 及之前版本在 `CookieRememberMeManager` 里硬写了一个 AES Key：`kPH+bIxk5D2deZiIxcaaaA==`。十几年来的教程和脚手架代码一直在拷贝这个值。
**第二，Key换不掉。** rememberMe 要求客户端和服务端用同一个 Key。一旦 Key 写进了配置文件、Docker 镜像、源码仓库，要替换就得所有节点一起改。
**第三，利用成本足够低。**GUI 点几下就能拿 shell，CLI 可以直接嵌进脚本。

## 攻击流程

```
探测 ── 发 rememberMe=yes，看有没有 Set-Cookie: rememberMe=deleteMe
         Shiro 1.x 遇到非法 Cookie 一定会回 deleteMe
爆破 ── 用 SimplePrincipalCollection 序列化 + 候选 Key 逐个加密
         响应里没有 deleteMe 就是 Key 对了
Gadget ── 用确认的 Key 加密完整 Payload（Gadget 链 + TemplatesImpl 回显类）
命令执行 ── rememberMe Cookie 带着 Gadget Payload，命令写在 Authorization 头里
内存马 ── 同样的 Gadget 链注入 Filter/Servlet，不再依赖 rememberMe
Key 替换 ── 用内存马机制改掉 Shiro 的 AES Key，旧 Key 失效
```

## CLI 模式

5.0 之后增加了 CLI 模式。核心攻击逻辑 `AttackService`（1000+ 行）一行没改——通过继承 `TextArea` 拦截日志输出，利用 `ControllersFactory` 注册表注入假的 `MainController`，GUI 和 CLI 共用同一套攻击代码。CLI 不需要 JavaFX 窗口，启动时用一个 `JFXPanel` 初始化 JavaFX 线程即可。

```
# 启动 CLI
java -cp shiro_attack-<version>.jar com.summersec.attack.CLI.MainCLI <command> [options]
```

| 命令 | 用途 |
| --- | --- |
| `detect` | 探测目标是否为 Shiro 框架 |
| `crack` | 爆破或验证 Shiro AES Key |
| `exec` | 执行系统命令（自动探测 Gadget 链） |
| `memshell` | 注入内存马（哥斯拉/冰蝎/蚁剑等） |
| `changekey` | 替换目标 Shiro Key |
| `gui` | 启动 JavaFX 图形界面 |

`--json` 模式下输出分为两个通道：以 `{` 开头的是结构化日志，AI 或脚本可以按行 JSON.parse；不以 `{` 开头的是命令原始输出，`tail -1` 就能拿到结果。

AES 模式：`--cbc`（Shiro ≤1.2.4），`--gcm`（Shiro ≥1.2.5）。

Gadget自动探测优先尝试String/AttrCompare/ObjectToStringComparator 变体（无需 commons-collections），回退到依赖 `ComparableComparator` 的 CB 变体。

详细 CLI 用法见 @skills/shiro-attack-cli/SKILL.md（此文件是给 AI Agent 加载的 skill 描述，结构化为命令参数和排错规则）。

## 功能特点

* • JavaFX GUI + CLI 双模式，同一套攻击逻辑
* • 多版本 CommonsBeanutils gadget（1.8.3 / 1.9.2 / AttrCompare / ObjectToStringComparator）
* • 自动 AES 模式切换：CBC 和 GCM 各走一遍，哪个命中锁哪个
* • 内存马注入（Filter / Servlet / Interceptor / HandlerMethod / TomcatValve）
* • 回显类型：TomcatEcho / SpringEcho / DFS-AllEcho / ReverseEcho / NoEcho
* • 回显生成器（jEG）和内存马生成器（jMG）第三方集成，失败自动回退 Legacy
* • Shiro Key 替换（6 条注入路径，自动验证新旧 Key）
* • 自定义请求头、Cookie 合并、POST 型探测
* • `--json` 结构化输出，适合脚本化和 AI 调用
* • HTTP/HTTPS 代理（支持认证）
* • Key 生成器

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

赛博生存指南

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/W8BrFJicfTaicbd7kn2cZBgNIaLlk75yrMSYaKQVkia524P5J7BoEBsYWI1XEWOXqDdmMcIzOYWZAiaTaqoSuvZXfg/0?wx_fmt=png)

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