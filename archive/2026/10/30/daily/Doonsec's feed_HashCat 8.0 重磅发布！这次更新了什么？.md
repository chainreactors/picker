---
title: HashCat 8.0 重磅发布！这次更新了什么？
url: https://mp.weixin.qq.com/s/154jekUjTJXim--ztIeffg
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:44:24.514085
---

# HashCat 8.0 重磅发布！这次更新了什么？

# HashCat 8.0 重磅发布！这次更新了什么？

原创

大表哥吆
大表哥吆

kali笔记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 如果说有一款工具，能让安全从业者既爱又敬，那非 HashCat 莫属。作为全球最强大的开源密码恢复工具，它刚刚迎来了历史上最大的一次更新`8.0.0` 版本。

# ![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBorf6bnvc5HTxqxibEkHCBbmDRxu7Jia58tB9CTZiclibKh5h9yHu9EuQfibhc1YbDwrW7Nm5Co0wzkhib6gu9p4ibyw2nhknVrVp4AmdjI/640?wx_fmt=gif&from=appmsg)新版特性![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBordlvoUZyXibJ9Yx8CKaWeY5ic1fnOwGj8AQn2MQhMnqibkIlgOmJnoYKFicvqGu6icbnAOzMLCtiaRQft1rewCvqR1a9V4WmcEyJuH0U/640?wx_fmt=gif&from=appmsg)

这次更新最核心的突破，集中在三大「旗舰特性」上，再辅以四类全新安全测试模式与一系列深度优化。

![](https://mmbiz.qpic.cn/mmbiz_png/1N1JeeKBordnHj2fMBM1zZiatWetaZn2EGPjxKY2HyFtRLa0PqibXutjzsCB6qNNIuIqWO5EibMAVNqwyiaYddNWHtOvxWLkIqibtIuY4fpBibJK8/640?wx_fmt=png&from=appmsg)

#### 1. PCFG 概率安全测试：先试最可能的密码

这是作者本人点名的「最重要的特性」之一。PCFG（概率上下文无关文法）安全测试基于真实密码训练出的文法模型，优先生成最有可能出现的密码。过去它一直无法在 HashCat 中发挥全力，因为密钥空间无法「跳转」，也就没法拆分任务做分布式运算。如今，HashCat 不仅能统计候选数量，还能在密钥空间中任意定位——这让 PCFG 终于可以在分布式环境中运行，且可以用掩码收窄范围、注入针对某人的密码线索。在一块 RTX 4090 上，PCFG 找回 NTLM 的速度可达 18.7 GH/s，做到「比暴力找回更聪明」。

#### 2. 哈希配方：没有模式，也能找回

过去遇到没有对应哈希模式的密码方案，要么自己写内核，要么干等官方支持。现在，你只需在命令行用一行「配方」描述哈希逻辑，例如 `--hash-recipe 'md5(md5(salt) . pass)'`，HashCat 就会在启动时把它编译成 GPU 内核，速度几乎媲美内置原生内核。它支持 MD5、SHA 系列、BLAKE2 等数十种哈希函数、PBKDF2 与 AES/DES 加解密、十六进制与 Base64 解码、变量与循环。这意味着 HashCat 支持的哈希模式从「约 700 种」一跃成为「无限种」。

#### 3. FPGA 支持

这是 HashCat 首次支持 FPGA 硬件，可与 GPU 并肩运行。针对 GPU 上「跑不满」的 bcrypt 算法，FPGA 可以把整块芯片配置成专门的 bcrypt 核心，功耗低、效率高。目前已有 7 种板卡可用，两块 YPCB 板在 bcrypt cost 10 下可达 8.9 kH/s，比单块 RTX 4090 还快约 15%，让大规模找回的硬件选择更加多元。

#### 4. 四种全新安全测试模式，规则覆盖所有场景

* • **表安全测试（-a 5）**：经典的表安全测试回归，沿用 hashcat-legacy 的原始模式编号，用 Token 替换组合密码。
* • **掩码内嵌字典（-a 12）**：用 `?w` 在掩码任意位置插入主字典词，用 `?q` 插入第二个字典词，灵活性大增。
* • **账号关联安全测试（-a 9）**：直接从哈希文件中读取每个哈希对应的词，无需再手动构建字典。
* • **Feed 插件（-a 8）**：候选生成器以插件形式运行，完整支持密钥空间、任务分配、恢复与状态。

同时，`-r` 规则文件如今在组合安全测试、暴力找回、PCFG、表安全测试与混合安全测试中全部可用；新增的 `--lookup` 选项可一键查询某个密码在安全测试中的具体位置，无需真正跑一遍安全测试。

#### 5. 大规模与分布式全面强化

* • 字典可跳转：通过 seek 数据库让每个设备从自身区间启动，且支持 xz、zstd 压缩字典。
* • 多字典统一密钥空间：`--skip`、`--limit`、`--keyspace` 现在支持字典目录、掩码文件与 `--increment`。
* • 全新 brain 服务器数据库，可从早期安全测试填充 brain；500 万条加盐哈希加载仅需 1.2 秒（原 7 秒）。
* • 新增 `HASHCAT_DEVICE_MEM_LIMIT`、`HASHCAT_HOST_MEM_LIMIT` 环境变量，为共享机器设定每进程内存预算。

#### 6. 性能与平台的跃升

新 autotune 机制直接读取设备上报参数，200 个掩码文件从 243 秒缩至 4 秒；PKZIP 模式最高提速 13.8 倍，原始私钥模式提速 32 至 58 倍。平台方面，Apple Silicon 升级 Metal 4 并默认原生 arm64，AMD GPU 支持 Mesa 的 rusticl 开源驱动，核心重构为 libhashcat 共享库，让发行包体积缩小约 73%。

#### 7. 新增算法与升级须知

新增 146 个哈希模式（含 yescrypt、Kerberos 5 etype 3、FreeBSD GELI、KDE KWallet、OpenSSH bcrypt-pbkdf、BIP39 助记词、MSSQL 2025、iClass 等），其中 91 个为哈希配方带来的全新哈希函数，另附 8 个新提取工具。升级前需注意：brain 协议升级至 v2（客户端与服务器须同时升级）、`-w` 参数被忽略、mode 72000 已移除（改用 73000）、自定义插件需重新移植编译。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1N1JeeKBorfXibybR5g8X6QibWhEPOYKFRUAsdGMTpLlqYTMqbicaHx0tl5AnZVACGzbJg3VxNAULibDiabUhCPtlbwudic1vUe3hqSmicPWGU08ag/640?wx_fmt=gif&from=appmsg)结语![](https://mmbiz.qpic.cn/mmbiz_gif/1N1JeeKBordMfAtrG7ibiaRtpFRvabu9xuPcvLXRYCEwQibZAlwMyHNK08oiaRaLKcYC5lUbMBmbykrYGlFlqA7XJRTeoWcUNw49CvaRDwwHa2E/640?wx_fmt=gif&from=appmsg)

如果说过去 HashCat 是一把锋利的刀，那么 8.0 版则把它变成了一台可编程的瑞士军刀。无论是渗透测试、安全审计，还是密码学研究，这次更新都值得第一时间升级体验。

更多精彩文章 欢迎关注我们

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xb3L3wnAiatia2JZVpfzEcXsOV52zrUXfJ951pRnM6UK5ghiaE4iaicHYADqWZFQmlZicF01GdKdwg9hRKlhiceeibQuRQ/0?wx_fmt=png)

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