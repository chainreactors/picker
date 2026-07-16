---
title: Web3智能合约安全漏洞检测工具
url: https://mp.weixin.qq.com/s/ylUhqNEMjPDfS4lul9peig
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:57:02.037953
---

# Web3智能合约安全漏洞检测工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIv7nmxJn69Vd0x0ZtfT7zvLruJ9jh4ib3mkD7IxZw4jnIj1Agbyib7Sj4za7aF2ttjPrA9Lpo0scHSF9bdMibcddzscZyE3E5IdQ/0?wx_fmt=jpeg)

# Web3智能合约安全漏洞检测工具

EthanOK
EthanOK

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

SolidityDetection v1.1在 SmartCheck 理论研究基础上开发，该工具实现了对以太坊智能合约 Solidity 源码的安全漏洞检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMJcmMk4EmmibN60Y8hFg1RuGqTyytYUmicib8PH4sR0ibKdqKzFMFrkaGPgVa9IHYln2O762qpULhPia81LAsx8A8HAMibxHDuXIYXNk/640?wx_fmt=png&from=appmsg)

主要包括 XML 中间表示、XPath 规则库和漏洞匹配检测三大模块，定义了 26 个合约漏洞检测规则，共包含 56 个 XPath 检测模式。

## 功能介绍

> ⚠️ 本工具主要面向 Solidity 0.4 ~ 0.6 版本，**不支持 0.8 及以上版本**，对新版本语法的检测结果可能不准确。

### 漏洞检测规则

| Solidity 智能合约漏洞类型 | 风险等级 | 规则名称 | XPath 模式数量 |
| --- | --- | --- | --- |
| 可重入 | 3 | `SOLIDITY_Reentrancy` | 2 |
| 整数溢出 | 3 | `SOLIDITY_IntegerOverflow` | 4 |
| DoS 攻击 | 3 | `SOLIDITY_DOS_Gas` | 2 |
| 时间戳依赖 | 2 | `SOLIDITY_TimestampDependence` | 5 |
| tx.origin 依赖 | 3 | `SOLIDITY_Tx.Origin` | 2 |
| Gas 高消耗模式 | 1 | `SOLIDITY_OutOfGas` | 2 |
| 未检查调用返回值 | 3 | `SOLIDITY_UncheckedCall` | 2 |
| 随机数误用 | 2 | `SOLIDITY_MisuseOfRandom` | 2 |
| 不正确的 blockhash | 2 | `SOLIDITY_IncorrectBlockhash` | 1 |
| 账户冻结 | 2 | `SOLIDITY_FrozenEther` | 1 |
| 未检查 selfdestruct 权限 | 2 | `SOLIDITY_UncheckedSelfDestruct` | 1 |
| Div 检查 | 1 | `SOLIDITY_DivMul_Zero` | 2 |
| 代码语法规范 | 1 | `SOLIDITY_VersionNotFixed` | 1 |
| 2 | `SOLIDITY_Pragma0.4` | 1 |
| 2 | `SOLIDITY_VarInLoop` | 1 |
| 1 | `SOLIDITY_Incorrect_View` | 1 |
| 1 | `SOLIDITY_Incorrect_Pure` | 1 |
| 1 | `SOLIDITY_FunctionReturns_NoReturn` | 2 |
| 1 | `SOLIDITY_Address_BitWrong` | 3 |
| 1 | `SOLIDITY_InlineAssembly` | 1 |
| 1 | `SOLIDITY_SAFEMATH` | 1 |
| Solidity 新版本问题 (0.5–0.6.8) | 1 | `SOLIDITY_DeprecatedVersion0.5` | 9 |
| 2 | `SOLIDITY_FunctionExplicitVisibility` | 4 |
| 1 | `SOLIDITY_IncorrectStorageLocation` | 3 |
| 2 | `SOLIDITY_StructNull` | 1 |
| 1 | `SOLIDITY_CALL_NotDate` | 1 |

### 命令行参数

**漏洞检测**（`DetectionOne` / `DetectionAll`）：

| 参数 | 说明 | 备注 |
| --- | --- | --- |
| `-p` / `--path` | 待扫描的目录 | 必填 |
| `-r` / `--rules` | 指定规则库文件（xml） | 非必填，默认加载 `solidity-rules.xml` |
| `-o` / `--output` | 结果输出文件 | 非必填，仅 `DetectionAll` 使用 |

**辅助工具**：

| 工具 | 参数 | 说明 |
| --- | --- | --- |
| `TreeView` | `-p` / `--path` | 单个 `.sol` / `.vy` 源文件（ANTLR 图形树，需本地 Java） |
| `XmlView` | `-s` / `--source`、`-t` / `--target` | 源文件路径、输出 XML 路径（`xml-view/`） |
| **XML Tree Viewer** | — | **推荐** ：Cursor 扩展，IDE 内查看 XML 图形树 |
| `view-xml-tree.sh` | `[xml-view/xxx.xml]` | 备选：浏览器 D3 图形树 |

完整 CLI 一览见 查看语法树 与 ARCHITECTURE.md。

## 工具获取

点击关注下方名片进入公众号

回复关键字【260715】获取下载链接

## 往期精彩

[一款面向攻防演练、红蓝对抗和安全研究场景的高交互智能欺骗蜜罐平台

2026-07-14

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMJ82XT8EvZ6iaSvCVwC3QSraQJy48d1jVzszOicomO4vaKOR8pUBCOc2XD3KZKTyLcF0Oib93eDjTn4Q3oRWGC7ycc5NRJFPAELmE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497199&idx=1&sn=f4f3fb6762f2e957d25ec35eaebb73d6&scene=21#wechat_redirect)[Godzilla 深度二次开发的 WebShell 管理与红队后渗透平台 | MCP 服务、团队协作、RASP 绕过 + 字节码多态混淆、内存马注入

2026-07-13

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMLcta82ZlRID0boHh5NzpKsRbacoO2XomlY7iasfVsBJVrxgcibpn4X63wffkQLCzXYY9ca6O7K586FR8jicyiatM7vrHiaDDZrhE1c/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497194&idx=1&sn=73ecd97867963a43b393b5cd7f34f97e&scene=21#wechat_redirect)[Fuck Claude自测工具— 你是「Claude 中国用户」吗

2026-07-07

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMIWZpC5PTpcImtCQ8YyZg2MPQJ14ekNYLN9f7Pmbd2vlWynKILwHLescXVYVB9B4Xcd0f35VL9VsrxffsC3klO0R0RSpqRcQ4A/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497188&idx=1&sn=5a84923ffb86d07e75cff19f8fa5da28&scene=21#wechat_redirect)[H3C Router Security Scanner v1.0 — GUI路由器配置泄露检测工具

2026-07-06

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMIHwS69Jt7JBpQJVeJiaxL66B7OqmoR7dtJiabiaV4icFBteGqFPUTxcjiaQKr5t8ESuwdGHW3LdZ9iamNMSZTGckibL8yialxQGgWbicPA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497183&idx=1&sn=73696d8bfb15ee464bea982bd725c04e&scene=21#wechat_redirect)[若依 Vue 漏洞检测工具 | 支持若依(RuoYi-Vue)多种安全漏洞

2026-07-03

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMIBBHaWqNLuBicpKgsVxCLjxfibBial4Yobwv61TjvdII3oyoBXfP9894Sma4SEVl5ic7yibibiau5x4lBK06cyyDVDFsVhicKNFyNfEP4/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497178&idx=1&sn=73891e1a78d5df7decc653218a459701&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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