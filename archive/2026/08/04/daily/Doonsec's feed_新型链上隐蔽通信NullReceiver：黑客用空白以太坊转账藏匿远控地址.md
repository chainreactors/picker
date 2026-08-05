---
title: 新型链上隐蔽通信NullReceiver：黑客用空白以太坊转账藏匿远控地址
url: https://mp.weixin.qq.com/s/iw9rl6C5PYeEaf46rR4TyA
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:55:24.219933
---

# 新型链上隐蔽通信NullReceiver：黑客用空白以太坊转账藏匿远控地址

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqIMqN28hck17VlhnUnfaRzLQIUr6jutYGp3wpH3HUILmTWkTliaz1xOyZticySZfceMlxVnUQMDteBPKHwFn7p6v9diaLYIMBZS4/0?wx_fmt=jpeg)

# 新型链上隐蔽通信NullReceiver：黑客用空白以太坊转账藏匿远控地址

白帽子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于黑鸟
，作者黑鸟

![](https://wx.qlogo.cn/mmhead/X4XEGYefSBSxrDYncLtKiacf7vZpHQnuLDMVc1rQjZsw9xYSM6kSCezibImssYuBjTibclnyop737M/0)

**黑鸟**
.

一介草民，深耕威胁情报领域多年，自封威胁分析师，APT狩猎者，战略忽悠分析师。 专注推送一切前沿高科技/人工智能、网络安全分析、敌我战略分析、数据挖掘、情报扩线、网络武器分析、社会工程学、一切开源情报、军事分析忽悠等。

网络安全厂商 OpenSourceMalware 在 2026 年 8 月 2 日发布深度分析报告，披露一款名为 NullReceiver 的新型区块链 C2（命令与控制）隐藏技术，该技术归属朝鲜 Contagious Interview 攻击活动，通过两款仿冒 Tailwind CSS 插件的 npm 恶意包完成传播，它针对此前黑客常用的 EtherHiding 技术短板完成全面改良，隐蔽性大幅提升，会成为后续同类供应链攻击的主流通信手段。

opensourcemalware.com/blog/nullreceiver-dprk-c2-technique

## 一、事件全貌：两款仿冒前端库暗藏远控后门

本次威胁的传播载体是 npm 生态内两款高度高仿的 UI 工具包，分别为 bianira-ui@1.27.0 与 fluid-type-ui@2.0.8，二者均复刻正规 Tailwind CSS 插件功能，开发者安装后项目可正常运行不会触发直观报错，恶意代码会在后台静默执行 Node.js 远控木马 RAT。

整个攻击团伙属于 Lazarus Group 关联的 Contagious Interview 行动，团队长期利用开源软件供应链投毒窃取开发服务器、本地设备内的运维密钥、项目源码与企业敏感数据。安全团队全程仅对 npm 安装包做静态代码分析，未执行任何恶意程序，所有链上数据均通过只读查询公开以太坊账本获取，分析结论具备完整可溯源依据。

传统木马会把 C2 服务器 IP 或域名硬编码写入程序文件，安全设备只需匹配特征就能快速拦截阻断，黑客为规避这种检测逐步转向区块链充当数据死信箱 dead-drop。区块链账本全网同步无法单方面关停篡改，恶意程序运行时实时从链上读取通信地址，大幅拉长防御方的检测溯源周期，NullReceiver 就是这套隐蔽思路的迭代产物。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoNGKx5SMeiaO3fDpbsDQgZqFME6UHp4uf9xE96TFmCPnSXOf2PQFayom9c4aFlgeKp3FfCzia4Yu1BarNvVQ8T8c6xdf41ia1iarQ/640?wx_fmt=png&from=appmsg)

先理清以太坊转账的基础结构，每一笔链上转账都会包含 from 转出钱包地址与 to 接收钱包地址，类比日常填写支票，from 是付款人，to 是收款账户，正常转账里 to 地址只用来接收代币不存在附加功能。

NullReceiver 完全颠覆这个设计逻辑，黑客不会向 to 地址转入任何资产，交易金额为零同时不携带任何附加数据 input 字段值固定为 0x，这一笔空白转账唯一作用就是把接收地址本身当作加密存储载体。

整套运行逻辑分为五步全部内置在恶意 npm 包代码中：

1. 恶意程序内置固定攻击者以太坊钱包地址 0xa322e5f3d311d3080e6f0121063e9adc2490ef1a
3. 程序调用eth.rpc.org、1rpc.io/eth 两类以太坊 RPC 节点接口查询该钱包最新一笔向外转账记录
5. 提取这笔零金额空白转账的 to 接收地址完整字节串
7. 截取地址前四段十六进制字节转换为 IPv4 地址，本次样本解码结果为 166.88.134.62
9. 木马主动向该 IP 的 80、443 端口建立连接接收黑客下发的控制指令

本次捕获的样本转账接收地址完整字符串为 0xa658863ea658863e68656c6c6f6970626f742121，除去解码 IP 的前 4 段字节，剩余字节转换 ASCII 字符会输出 helloipbot!!，这段字符是黑客团队专属指纹标识，能够串联起该团伙所有使用 NullReceiver 技术的攻击样本。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDr5icZkaia7LjNWjJTmqlUPaZ1PWBxkEYwo4dngSjBx2OicxSXC1kaIibPI3mlknnTd8Wia5icnDPlOamofqxpquMk3vsUAyTuKStFgg/640?wx_fmt=png&from=appmsg)

恶意代码关键特征标记 A10-npm3! 也在源码中明确留存，代码内仅保留查询链上数据、解析地址、发起网络请求的极简逻辑，无多余混淆冗余代码，降低静态审计人员的排查门槛。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqgZI6GfXORD6EURC80QKNeMoffbY7qeJ7VUm8ibAfEbubHEadjGicjC7Js7ib3kTxFmYpU4icHp8qLQM9lbLkfuwQS5KTuBibLxNicg/640?wx_fmt=png&from=appmsg)

EtherHiding 是谷歌威胁情报 GTIG 在 2025 年 10 月披露的同类链上 C2 技术，同样被朝鲜黑客团伙使用，核心实现逻辑和 NullReceiver 有本质区别。[黑客利用区块链构建恶意软件的C2基础设施](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451183033&idx=1&sn=e755ff7f0d0000c0be16865da0d77fe3&scene=21#wechat_redirect)

EtherHiding 会把 C2 网址、完整恶意脚本等大容量数据存入交易 calldata（调用数据）字段，所有交易统一发送至全网知名销毁地址 burn address0x000...dEaD，这个地址的用途是永久销毁代币不会产生任何资产流转，天然成为安全设备重点监控的链上地标。

这套方案有三个无法规避的短板

1. 固定目标地址极易监控，防御方只需持续观测销毁地址所有流入交易，出现携带自定义 calldata 的异常转账就能快速告警
2. 交易成本更高，以太坊会按照 calldata 字节长度收取 gas 手续费，携带长文本数据的转账开销会显著提升
3. 异常特征过于明显，正常流向销毁地址的转账几乎不会附加自定义数据，带载荷的交易一眼就能识别异常

EtherHiding 的优势在于承载数据容量更大，完整 URL、小型脚本都能嵌入，适合下发全套恶意载荷，而 NullReceiver 仅能存储 4 字节 IPv4 地址，定位仅做木马心跳 beacon（心跳上报）使用，二者适用攻击场景完全区分。

对比 EtherHiding，NullReceiver 在隐蔽性、成本、规避检测层面实现全方位升级，也是安全团队判断它会成为团伙默认链上通信方案的核心依据。

### 无固定可监控地标地址

EtherHiding 全程复用同一个公开销毁地址，相当于黑客每次传递信息都寄往同一个知名邮局，防御方蹲守邮局即可拦截。NullReceiver 每一次更新 C2 地址都会生成全新一次性 to 接收地址，不存在任何长期固定观测目标，在未定位攻击者钱包前安全系统无法设置持续监控规则。

### 不存在可供匹配的特征字段

EtherHiding 依赖 calldata 字段存储信息，该字段的非空内容就是核心检测指纹，现有链上安全检测工具均针对该字段设计识别规则。NullReceiver 的转账 input 值固定为空 0x，没有任何附加数据字段可供特征匹配，传统针对链上载荷的检测规则会完全失效。

### 链上行为完全符合普通用户转账特征

零金额无附加数据的钱包互转是以太坊网络中最常见、手续费最低的交易类型，海量正常用户日常都会产生同类转账行为，混在海量正常链上活动中几乎无法区分，不会像携带长 calldata 的交易那样一眼凸显异常。

二者唯一共通短板是转出钱包地址长期复用，bianira-ui 与 fluid-type-ui 两款恶意包共用同一个攻击者以太坊钱包，安全团队一旦标记该钱包地址，就能持续追踪它发出的所有空白转账记录，只是定位钱包需要先捕获恶意样本逆向分析，不像销毁地址可以无样本提前监控。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqp6RnvhiaHyEkfn7Wiaal1C5yhgc0ZpiamGebO33I1q4I56pQlIqUyibRW5gnKoibwHLyv5iaE0YNe4Eo0y19xBEC7ibE6XxHwu2tKwo/640?wx_fmt=png&from=appmsg)

朝鲜黑客在 npm 供应链攻击的技术迭代存在清晰固定规律，只要某一类恶意手法被安全厂商公开完整拆解并发布 IOC（妥协指标）清单，该技术的使用周期就会快速缩短，下一批恶意样本会精准修复暴露检测漏洞。

早期硬编码域名、普通字符串混淆、EtherHiding 都遵循这套淘汰逻辑，NullReceiver 精准解决 EtherHiding 最核心的暴露点也就是固定销毁观测地址，契合团伙一贯的技术迭代思路。安全团队预测未来半年内该团伙发布的所有 npm 恶意包都会切换至 NullReceiver 链路，EtherHiding 会逐步被淘汰，仅在需要下发大容量恶意脚本的特殊场景少量留存。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/2dMzopbOicLibMplBZwCuQE2bMW3MP0GqZsRm1iaMYBL5dP8CfNuJwnEdFkXzbeJxcFJcPam8qQIv2TA6cCvLUMTA/0?wx_fmt=png)

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