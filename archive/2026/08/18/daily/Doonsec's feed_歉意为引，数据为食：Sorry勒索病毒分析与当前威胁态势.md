---
title: 歉意为引，数据为食：Sorry勒索病毒分析与当前威胁态势
url: https://mp.weixin.qq.com/s/GpiopX0jHObgDVYzLF6aww
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:54:12.833908
---

# 歉意为引，数据为食：Sorry勒索病毒分析与当前威胁态势

![cover_image](http://mmecoa.qpic.cn/sz_mmecoa_jpg/w6Du02ZmtvEB4ic3ZnhwkfDw6DfMLeGmaVfEWZ13xV08YibNF1TtgzZZdltJtKNUz9C6UluRbMuh7OmulXsFXKcEBjTxeoppmEKwGOPxBLlFY/0?wx_fmt=jpeg)

# 歉意为引，数据为食：Sorry勒索病毒分析与当前威胁态势

VenusEye威胁情报
VenusEye威胁情报

VenusEye服务号

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**事件概览**

“Sorry”是2026年新近活跃的一款勒索病毒家族，因其攻击手法粗暴、传播速度惊人，短短数月间便在全球网络空间掀起巨浪。该病毒拥有极具辨识度的感染特征——所有被加密的受害文件均会被强制统一追加`.sorry`后缀，仿佛一封来自恶意攻击者的冰冷“致歉信”，实则是对数据主权与业务存续的赤裸挑衅。2026年8月10日，国家计算机病毒应急处理中心（CVERC）发布预警，通报我国境内已发现多起攻击事件，教育、金融、制造、医药、农业等行业均有受害。值得警惕的是，此次攻击并非局限于某一特定领域，而是呈现出明显的行业广谱性。这一跨行业、多节点的攻击态势，不仅暴露出当前关键信息基础设施面临的严峻挑战，也为全社会的数据安全防护体系再次敲响了警钟。

**核心事实**：

* **攻击****目标**：主要针对互联网暴露的Linux Web服务器（尤以cPanel/WHM托管环境为主），同时兼容Windows平台载荷；可有效感染国内主流Linux发行版及信创操作系统。
* **入侵双通道**：一是利用cPanel/WHM授权绕过漏洞CVE-2026-41940（CRLF注入，CVSS评分9.8，已在11.136.0.5及以上版本修复）实施远程入侵；二是通过SSH弱口令进行蠕虫式横向传播，扫描端口涵盖22、2222及22222。加密与传播逻辑在同一进程内并发执行，大幅缩短攻击响应窗口。
* **破坏****机制**：采用对称加密配合RSA-2048密钥封装，未持有攻击者私钥则无法恢复数据；系统在加密完成后覆盖删除原始文件，从根本上阻断常规恢复手段；同时窃取主机指纹信息并回传至攻击端。
* **波及范围**：全球范围，国内也发现有多起受害。
* **勒索****联络**：攻击者通过qTox（基于P2P协议的去中心化即时通信工具，无中心服务器）以TOX ID作为联络凭据，引导受害者在联系过程中经电商平台上的数据恢复公司进行中间转介，形成变通的赎金支付通道。

**发展变化**

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvGVL7EMqpqrOZK5HZopkYWVdKHbTn9Yxib8SBrIuszGw6go3ARibKTc3xD6vdszFMnu1ptK7icLxO7aq7QyBfibpILIvSIrJK2cUBo/640?wx_fmt=png&from=appmsg)

**演进趋势判断**：加密逻辑持续迭代、C2 按版本轮换、密钥按批次隔离——该威胁具备成熟的多平台构建管线与较强的 OPSEC 意识，后续需警惕 Rust 线补齐蠕虫传播能力。

**样本分析**

## Windows （Rust 实现）样本分析要点

##

|  |  |
| --- | --- |
| MD5 | 6c3f7b06fc86f26635709e2e6f69a336 |
| 针对平台 | Windows |
| 编译语言 | Rust |
| 家族归属 | sorry勒索 |

**功能分析：**

涵盖互斥体检测、枚举驱动器 、walkdir 遍历筛选、AES-GCM 加密 + RSA 保护密钥、 追加 .sorry 、覆盖删除原文件 、收集指纹、HTTP 外传 C2、投放 README.md 勒索信（威胁受害者用 qTox 添加 TOX ID 付款解密）等。

**单实例互斥**：`CreateMutexA`，创建互斥体，防止重复加密；已运行时提示 instance is already running。

**枚举驱动器**：枚举所有可访问驱动器作为扫描根，无可用驱动器时提示 `no accessible drives found。`

**目录遍历筛选**：`walkdir` 按扩展名白名单遍历（约百种，覆盖文档/数据库/代码/多媒体/压缩包/钱包文件）。

**文件加密**：逐文件随机生成 AES-GCM 会话密钥，AES-GCM 加密文件内容，会话密钥再用 RSA-2048 主公钥（PKCS#1 v1.5）封装——私钥仅攻击者持有，受害者无法自行解密；加密后追加 .sorry 后缀。值得注意的是：加密完全由 Rust  crate（aes-0.8.4、rsa-0.9.10）实现，不调用 Windows CryptoAPI，可规避针对标准加密库的 hook 检测。

**覆盖删除**：secure-delete 覆盖删除原文件，阻断文件恢复工具。

**容错机制**：加密失败自动回滚、文件大小变化则跳过。

**机器指纹收集**：USERNAME、PROCESSOR\_IDENTIFIER（CPU型号）、NUMBER\_OF\_PROCESSORS（处理器数量）、SystemDrive（系统盘符）、COMPUTERNAME、HOSTNAME。

**HTTP 外传**：单向外传 C2；硬编码 http://209.97.175.77/favicon.ico/，仅解析 WSASocketW / connect / send / select，不解析 recv 与任何 DNS API——纯单向只发不收的遥测外传，规避基于回包的检测。

**勒索信投放**：在受影响目录生成 `README.md`。勒索信正文使用自定义 XOR 混淆**，**密钥流由字符串哈希函数生成，勒索信内容：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvHibD51ex1a3MagNGLj7Hxv8w7V06txcZHLnib7f0PL59rFt0B2CzBHTlAvhYYibiaENC8L95Ve1AxAr7V95NpATzfWl2MLKHJ0CdE/640?wx_fmt=png&from=appmsg)

**危害特点**：文件读写直接调用 NtOpenFile / NtReadFile / NtWriteFile 等底层 NTAPI，绕过用户态 EDR 监控（“盲区加密”）；覆盖删除 + 无私钥不可逆，双重阻断恢复路径。匿名收款（采用 qTox 的 TOX ID 而非加密货币钱包地址）有效规避区块链资金追踪。

**影响面**

截至 2026 年 8 月 17 日，本团队基于内部诱捕系统近三个月的监测数据发现：针对 cPanel/WHM 管理端口（2082/2083/2086/2087）的攻击活动呈现显著上升趋势。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvGuuT14ay27wOAVqJeSaTXS2wZVTbtHbTdjbc7aMZ4mReGNJpW4trwmYHeDE4OuoI3g2FofMyGIgPBP83551vGOm52Oy5hqL9Q/640?wx_fmt=png&from=appmsg)

**攻击链与 TTPs 分析：** 基于 TOP 20 探测路径分布，完整还原出该蠕虫的四阶段提权利用链及后渗透行为：

四阶段提权攻击链（4 Stages）：高达 41.0% 的 Web 根路径探测并非通用测绘，而是核心的漏洞注入环节。

1、获取预认证会话：通过 `/login/?login_only=1` 索取初始会话凭据（占比 0.7%）。

2、会话文件污染：向根路径（`/`，占比 41.0%）及空路径（占比 11.3%）发送附带 CRLF 注入的恶意载荷以污染会话。（包含部分扫描）

3、触发缓存刷新：发起 `/scripts2/listaccts` 等请求强制刷新缓存使污染生效。

4、权限验证与接管：通过高频指向 `/cpsessXXXXXXXXXX/login/` 路径（占比 19.8%）提取令牌验证 Root 权限。该硬编码的会话 ID来自于诱捕设置，是识别该蠕虫变种的强特征。

**失陷主机与基础设施画像：** 地域呈境内外混合（境外美/荷/德居多，境内川/港/豫为主）。威胁源头部集中效应显著（TOP 20 节点占总攻击量 27.2%），聚类为两类战术角色。

TOP20节点：蠕虫自发传播节点（15 个），非中心化脚本驱动。系已被感染的肉鸡利用内置蠕虫模块，自发向公网发起的无差别横向扫描，精准执行上述 4 阶段提权攻击，呈滚雪球式蔓延。前置测绘集群（5 个），全部归属荷兰同一机房的 `/24` 连续网段，行为同构。判定为其他活跃攻击组织（或 IAB）控制的纯侦察集群，建议执行成段封禁。

**防守与处置建议**

1. **断网隔离**：确诊后立即断开网络连接以阻断蠕虫扩散，切忌关机或重启以保留内存证据。
2. **修补漏洞**：强制升级 cPanel/WHM 资产至安全版本，阻断 CVE-2026-41940 初始入侵。
3. **重置凭证**：打补丁后必须强制注销并清空所有历史会话和 API 令牌，防止后门利用。
4. **收敛边界**：严禁管理面板公网直达，全面收敛至 VPN 或堡垒机并强制启用 MFA。
5. **加固 SSH**：全面禁用密码登录，强制使用密钥认证，更改默认端口防范蠕虫爆破。
6. **审计会话**：重点排查 `/var/cpanel/sessions/raw/` 目录下带有 CRLF 注入的异常文件。
7. 监控异常：利用 EDR/HIDS 严密监控 /tmp/.sorry\_\*隐藏进程及 .sorry文件创建。
8. 彻底重建：因攻击者易留多重持久化后门，强烈建议直接废弃失陷系统并从干净镜像重建。

**IOC**

6c3f7b06fc86f26635709e2e6f69a336

43e19a8c4babe9edd0981e19d035b694

51663fdfbb2fdd807a628c26b23ecff9

11fb4f39b50b44e37d9412e1e1373ed6

5f171c166012b74365bf930102a1fa40

051d2a8fdde39eedba5321f3ec01a81e

fc9ffa0137e0c447745749178afd1fc6

73cae44b0a9e4a315285c50c2f3cd14d

b45ad1457e10d44db4e965fdb7f9b630

9d0f3c6771b5ee3b1fc1af5f308196ad

209.97.175.77

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/fO5Mfy7Ke96ibRADV6dibibhaC7pBoXfIo2TmTDseuS3GKaYt6V6shDnSq3DzzONkxnPx2G8pnTQwnP4G9rtbic3eA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=23)

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

![作者头像](http://mmecoa.qpic.cn/sz_mmecoa_png/fO5Mfy7Ke97LllgyoyyJDws0WRUK7csYmyHH8Z6PnC79gibotNt7ibwYTvHFeb5LnrY3Kic1V55yicCgfk918gIqbw/0?wx_fmt=png)

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