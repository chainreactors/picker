---
title: 慢雾：公链安全审计指南全面升级，并新增 Layer2 安全审计方法
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499970&idx=1&sn=949d5a2fa1ce82709818e8fcc37ccad0&chksm=fddebe45caa9375310a4fccccd715ec76bb09b9ccfd7f0e692ae3dbca35b1ffdd6fec7138722&scene=58&subscene=0#rd
source: 慢雾科技
date: 2024-07-13
fetch_date: 2025-10-06T17:43:52.361583
---

# 慢雾：公链安全审计指南全面升级，并新增 Layer2 安全审计方法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLYTmsSAFEfd3G5rlLoNJeibGeUMvZ9yBeO7VlbfYkzMRguIblB5qdpZjUHCjn1MmxibkmiamHibV8ZibRg/0?wx_fmt=jpeg)

# 慢雾：公链安全审计指南全面升级，并新增 Layer2 安全审计方法

原创

慢雾安全团队

慢雾科技

随着区块链的普及，越来越多的用户在 Layer1 上进行交易，Layer1 交易速度变慢、交易费用变高的问题逐渐凸显。在这样的情况下，Layer2 被认为是在不影响 Layer1 的安全性和去中心化特性的情况下、增强区块链平台可扩展性和性能的一种解决方案。据 L2BEAT 统计，现在 Layer2 生态系统的总锁定价值达 395 亿美元，包含了各种具有独特特性的技术和框架。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLYTmsSAFEfd3G5rlLoNJeibGA8tLqycYmCHyFknQw4RoFakwI7icnicr39pibibt1f2J4RDctJLmxibAccQ/640?wx_fmt=png&from=appmsg)

(https://l2beat.com/scaling/summary)

经过多年的实战和安全研究，慢雾安全团队积累了大量公链主网安全审计的经验和深厚的漏洞挖掘技术，并向全行业公开了我们的主网安全审计方法，希望能共同打造一个更加安全的区块链生态。

安全没有止境，审计方案也需要与时俱进，不断满足行业的需求。慢雾安全团队持续关注行业的发展动向，了解当前区块链生态中突出存在的安全问题是什么，用户的安全需求是什么，以此为依据来制定和优化安全审计方案。近期，慢雾安全团队结合当前公链和 Layer2 的发展情况，适时升级公链安全审计指南，具体的安全审计方案内容如下：

**方案一 主网 & Layer2 项目安全审计**

在主网 & Layer2 项目安全审计中，慢雾安全团队采用“黑盒 + 灰盒”策略，以最接近真实攻击的方式对项目进行快速的安全测试，我们检查的漏洞包括：

* 私钥随机数熵不足
* 私钥种子转换精度损失
* 对称加密算法的理论可靠性评估
* 对称加密算法依赖库的供应链安全
* 密钥库加密强度检测
* 哈希算法长度扩展攻击
* 哈希算法的理论可靠性评估
* 签名算法的理论可靠性评估
* secp256k1 k 值随机性安全
* secp256k1 r 值重用私钥提取攻击
* ECC 签名的可塑性攻击
* ed25519 私钥提取攻击
* Schnorr 私钥提取攻击
* ECC 曲线攻击
* Merkle 树可塑性攻击(CVE-2012-2459)
* 原生特性虚假充值
* 基于合约调用的虚假充值
* 原生链交易重放攻击
* 跨链交易重放攻击
* 交易锁定攻击
* 交易费用未动态调整
* RPC 远程密钥盗窃攻击
* RPC 端口可识别性
* RPC 开放跨域漏洞导致本地钓鱼攻击
* JsonRPC 畸形包拒绝服务攻击
* RPC 数据库注入
* RPC 通信加密
* 过度的管理员权限
* 非隐私/非暗币审计
* 核心节点数量不足
* 核心节点物理位置过度集中
* P2P 节点最大连接数限制
* P2P 节点独立 IP 连接限制
* P2P 入站/出站连接限制
* P2P 变形攻击
* P2P 通信加密
* P2P 端口可识别性
* 共识算法潜在风险评估
* 区块时间偏移攻击
* 矿工磨矿攻击
* PoS/BFT 双重签名惩罚

**方案****二 源代码安全审计**

源代码安全审计是指采用“白盒”策略，对项目的相关源代码进行最全面的安全测试。白盒审计通常需要结合自动化静态代码分析和人工手动分析两种形式。

**静态源代码分析**

慢雾安全团队使用开源或商业代码扫描工具对代码进行静态扫描，并人工解析发现的问题，我们支持所有流行语言，如 C/C++/Golang/Rust/Java/Nodejs/C#。我们检查的静态编码问题包括：

* 未使用的变量或导入 - 声明但未使用的变量或导入模块
* 代码格式问题 - 缩进不一致、行长度过长等
* 资源未正确关闭 - 如文件、数据库连接等未关闭
* 魔法数字 - 直接使用数字常量而非命名常量
* 潜在的安全漏洞 - 如 SQL 注入、XSS 等安全隐患
* 整数溢出 - 当计算结果超出整数类型的范围时可能导致意外行为
* 浮点数精度问题 - 由于浮点数表示的限制，可能导致计算误差
* 死锁 - 多线程编程中，线程互相等待对方释放资源而陷入僵局
* 竞态条件 - 多线程或并发环境下，程序的行为依赖于不可控的执行顺序
* 内存泄漏 - 动态分配的内存未被正确释放，导致程序占用的内存持续增加
* 无限递归 - 递归函数没有正确的终止条件，导致栈溢出
* 字符串格式化漏洞 - 不安全的字符串格式化可能导致安全问题
* 除零错误 - 在除法运算中未检查除数是否为零
* 空指针解引用 - 试图访问空指针指向的内存位置
* 缓冲区溢出 - 向缓冲区写入超出其容量的数据，可能导致安全漏洞
* 类型转换错误 - 不当的类型转换可能导致数据丢失或不正确的结果
* 硬编码密钥或敏感信息 - 将密钥或敏感信息直接写入代码中，可能导致安全风险
* 代码复杂度过高 - 函数或方法过长，逻辑分支过多
* 代码重复 - 相同或相似的代码段在多处出现
* 命名不规范 - 变量、函数、类等命名不清晰或不一致
* 注释不足或过时 - 缺乏必要的注释，或注释与代码不符
* 耦合度高 - 模块间依赖关系复杂，难以维护和扩展
* 低内聚 - 模块或类的功能不够集中，职责不明确
* 异常处理不当 - 捕获过于宽泛的异常，或忽略异常
* 硬编码 - 直接在代码中使用常量值，而非配置参数
* 代码格式不一致 - 缩进、空格使用等不统一
* 性能问题 - 如不必要的循环、频繁的对象创建等
* 可测试性差 - 代码难以进行单元测试或集成测试
* 违反设计原则 - 如单一职责原则、开闭原则等
* 可读性差 - 代码结构混乱，难以理解
* 不安全的随机数生成 - 使用不适合安全用途的随机数生成方法
* 时间和状态问题 - 如 TOCTOU(Time-of-check to time-of-use) 漏洞
* 路径遍历 - 未正确验证文件路径，可能导致访问未授权的文件
* 依赖库过时 - 引入的库已失去维护或存在安全漏洞

**手动代码审查**

慢雾安全团队通过逐行检查代码，查找编码缺陷和逻辑错误，我们关注的漏洞范围主要包括：

* 加密签名安全
* 账号与交易安全
* RPC 安全
* P2P 安全
* 共识安全
* 业务逻辑安全

**方案三****应用链安全审计**

慢雾安全团队采用“白盒”策略，对项目进行全面的安全测试，寻找常见的编码陷阱，如：

* 重放漏洞
* 重新排序漏洞
* 竞态条件漏洞
* 权限控制漏洞
* 块数据依赖漏洞
* 函数显式可见性
* 算术精度偏差漏洞
* 恶意事件日志
* 异步调用安全

目前我们支持：

* 基于 Cosmos-SDK 框架的区块链审计
* 基于 Substrate 框架的区块链审计

**结语**

在过去几年里，已有近百个知名公链项目通过慢雾(SlowMist) 的不同类型公链安全审计，如 Prysm、TON、Mantle、Vision Network、Metis、Acala、Eden 等。慢雾(SlowMist) 也审计了多个知名 Layer2 项目，如 Morph、Bitlayer、Merlin Chain、RSS3 Network 等。欢迎有审计需求的项目方联系慢雾安全团队邮箱 team@slowmist.com 咨询合作 :)

完整内容已在 GitHub 开源(https://github.com/slowmist/Cryptocurrency-Security-Audit-Guide)，欢迎点击阅读原文跳转至 GitHub 阅读。

**往期回顾**

[慢雾：安全审计检查项之账户抽象钱包](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499961&idx=1&sn=c443ff0b1d639a5c022697db117f4652&chksm=fddebe3ecaa9372839c97a4d00dc57e9cb903326a933528fe5927149d065ecfb025128655d86&scene=21#wechat_redirect)

[慢雾：2024 Q2 MistTrack 被盗表单分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499939&idx=1&sn=9a19ea41c058d225c6ccbb21736f8923&chksm=fddebe24caa93732fab9dc5b29801e718e4a72db379f53db6a5b0532d4f22e957f6221946f2f&scene=21#wechat_redirect)

[慢雾出品 | 2024 上半年区块链安全与反洗钱报告](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499923&idx=1&sn=e075b86887cefa622b8a8318be269d49&chksm=fddebe14caa937024e5926e5524ace12fd4413510f51c8d8bdab1b01db4f16239b2cf8735a73&scene=21#wechat_redirect)

[「区块链黑暗森林自救手册」阿拉伯文版正式发布](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499898&idx=1&sn=e69f4409d60a42166cdfabae8a778436&chksm=fddebefdcaa937eb36e93c2d5fc126c5c9be7d0650cf108710b858941ad8fdf68912cd2a5b19&scene=21#wechat_redirect)

[慢雾：UwU Lend 被黑分析](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247499891&idx=1&sn=25f3885531c260de8c37ec6212fd5480&chksm=fddebef4caa937e2bcdcba85424fed82bfd9ba3165ab07cd2efc01d117712bdb0d9dc8b74bb1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLazKt6yZQQvqiccDeUu8Togv4VUdq4r7iak19Hta2pfbzPrGohPNR71WxPKrBoK9nyibPVL7ssCuW3yA/640?wx_fmt=png)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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