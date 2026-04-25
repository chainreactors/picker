---
title: 【IETF125参会记录】详解 X3DH 算法、双棘轮算法和 MLS 协议
url: https://mp.weixin.qq.com/s/sGTrH-kOIDPG_9e0Yst_CA
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:35:39.155544
---

# 【IETF125参会记录】详解 X3DH 算法、双棘轮算法和 MLS 协议

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kGhLgo0BUA42hURNDcIYWqlL4aKBudX4BKm6icEkMJfdD75G410icPpwzsIDrCkib51tdTsrnV2AomZygc7Pxs8WkG4LIxq9SZaqcraibVwZxkI/0?wx_fmt=jpeg)

# 【IETF125参会记录】详解 X3DH 算法、双棘轮算法和 MLS 协议

原创

crackme.net
crackme.net

crackme安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

参会日期：2026-3-18 星期三
参会时间：14:00 - 16:00
参会地点：Hebei
会议领域：SEC（安全）
会议名称：Messaging Layer Security（MLS）

# 安全声明

本文章内涉及的软件（Signal、Telegram 等）不受中国法律法规监管，其服务器位于境外，数据流向不可控，且缺乏有效的内容审核与监管机制，存在大量违法违规内容。使用此类软件不仅面临极高的个人信息泄露风险，更可能因接触或意外参与非法活动而触犯国家法律

本文仅从计算机科学与密码学学术角度，对 X3DH 密钥协商协议及双棘轮算法的底层设计原理进行**技术性**分析与探讨，绝**不推荐、不鼓励、不引导**任何个人或组织下载、安装和使用 Signal、Telegram 等未经中国国家有关部门批准的境外即时通信软件

# Signal 即时通信软件

在公民的数字隐私日益受到侵犯的今天，Signal 被公认为全球最安全的即时通信软件之一（斯诺登严选的含金量）

Signal 的安全承诺，并非来自其商业公司的道德约束（说的就是 Telegram，Telegram 并没有互联网吹嘘的那么厉害，以后有机会本公众号也会写文章分析 Telegram 的 MTProto 协议），而是来自其开源的、经过严格审计的密码学协议。该协议的核心由两个关键算法组成：**X3DH**（用于密钥协商，建立初始连接）和**双棘轮算法**（用于维持会话安全）

## X3DH 密钥交换算法

https://signal.org/docs/specifications/x3dh/

X3DH（Extended Triple Diffie-Hellman，扩展三重迪菲 - 赫尔曼）是一种密钥协商协议，为两个参与方在异步通信环境中建立共享密钥。该协议由 Moxie Marlinspike 和 Trevor Perrin 设计，提供强大的前向安全性和可否认性

X3DH 的核心指标如下：

* • 支持异步密钥协商：意味着 Alice 可以离线时发布公钥信息，Bob 在线时获取这些信息并发起加密通信，无需双方同时在线
* • 提供前向安全性：即使长期密钥泄露，过去的会话密钥也不会被破解
* • 提供可否认性：只要 Bob 不承认，Alice 无法证明这些消息是 Bob 发送的（Alice 知道这些消息确实是 Bob 发送的，但无法向外界证明）
* • 提供双向认证：Alice 知道对方是 Bob，Bob 知道对方是 Alice

### 角色与密钥定义

协议仅涉及三方角色：**Alice**（发起者）、**Bob**（接收者）和 **服务器**（用于存储和转发预密钥）

协议涉及四种密钥，定义如下表所示：

| 密钥 | 简写 | 说明 |
| --- | --- | --- |
| 身份密钥 | IK（Identity Key） | 双方的长期公钥，用于标识身份，不经常更换 |
| 签名预密钥 | SPK（Signed PreKey） | Bob 的中等期限密钥，用身份私钥签名，定期更换以平衡安全性和效率 |
| 一次性预密钥 | OPK（One-Time PreKey） | Bob 生成的一组密钥，每个仅使用一次用完即扔，前向安全性的核心保障 |
| 临时密钥 | EK（Ephemeral Key） | Alice 在发起密钥协商时临时生成的密钥，同样用完即扔 |

### 协议流程

**第一阶段：Bob 发布密钥（离线准备）**

Bob 将以下信息上传到服务器：

1. 1. 身份公钥 `IKB`
2. 2. 签名预公钥 `SPKB` 及其签名 `Sig(IKB, SPKB)`
3. 3. 若干个一次性预公钥 `OPKB`

`IKB` 只需上传一次，`SPKB` 定期更新，`OPKB` 随用随补

**第二阶段：Alice 发起会话（发送初始消息）**

1. 1. Alice 从服务器请求 Bob 的预密钥包，包含 `IKB`、`SPKB`、`SPKB`的签名，以及一个可用的 `OPKB`（如果有）
2. 2. Alice 生成临时的 `EKA`
3. 3. Alice 执行多次 DH 运算，根据是否有可用的 `OPKB`，计算方式略有不同：

* • 情况 A：有可用的`OPKB`，执行 4 次 DH 运算

1. 1. `DH1 = DH(IKA, SPKB)`
2. 2. `DH2 = DH(EKA, IKB)`
3. 3. `DH3 = DH(EKA, SPKB)`
4. 4. `DH4 = DH(EKA, OPKB)`
   最终共享密钥：`SK = KDF(DH1 || DH2 || DH3 || DH4)`

* • 情况 B：无可用的`OPKB`，执行 3 次 DH 运算（前三次和情况 A 一致，省略 `DH4`）

4. 4. Alice 删除临时私钥和中间 DH 值，构建关联数据 `AD`（包含双方身份标识）并使用共享密钥 `SK` 加密初始消息。发送给 Bob 的内容包括：`IKA`，`EKA`，`SPKB`的索引，以及加密后的初始消息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA5kXXzReMjtS3daHhsKWY5dCnmGAGB1QfGFJhPKBCiaZ7vblkIUK7pawNNg2ImcpXNqLC21mbSCV5NMSOZ3hRZ0dOfFQwkRQBRw/640?wx_fmt=png&from=appmsg)

**第三阶段：Bob 接收并处理**

1. 1. Bob 收到消息后，加载自己的身份私钥、对应的签名预密钥私钥，以及对应的一次性预密钥私钥（如果使用了）
2. 2. Bob 使用收到的 `IKA` 和 `EKA`，结合自己的私钥，重复第二阶段的 DH 运算过程，计算出相同的 `SK`
3. 3. 如果使用了 `OPKB`，Bob 必须立即删除该一次性预密钥的私钥，以确保前向保密性

### 简单的安全性分析

#### 双向认证性

`DH1` 和 `DH2` 确保了双向认证性，因为只有拥有正确长期私钥的人才能计算出正确的共享密钥

#### 前向安全性

`DH3` 和 `DH4` 确保了前向安全性

* • 如果使用了 `OPKB`，即使 Bob 的 `IKB` 私钥和 `SPKB` 私钥未来被泄露，只要 `OPKB` 私钥已删除，过去的会话密钥 `SK` 依然安全
* • 如果没有使用 `OPKB`，那么前向保密性则依赖于 `SPKB` 的轮换频率

#### 可否认性

由于 `EKA` 是临时的且任何人都可以伪造（因为它没有签名），且共享密钥的计算涉及双方的私钥混合，没有任何一方能生成只有对方才能生成的“证据”。第三方无法区分真实的通信记录和一个模拟生成的记录（前提是双方私钥未同时泄露）

#### 抗重放攻击

一次性预密钥 `EKA` 防止了初始消息的重放，因为该密钥仅用一次用完就扔，而后续消息的抗重放机制依赖双棘轮算法

## 双棘轮算法

双棘轮算法是一种用于安全通信的加密协议，提供了强前向安全性（FS）及妥协后安全性（PCS）保证

双棘轮算法的核心指标如下：

* • 前向安全性：即使攻击者获取了当前的会话密钥，也无法解密过去的消息
* • 妥协后安全性：即使攻击者获取了当前的会话密钥，也无法获取未来的会话密钥，无法解密未来的消息
* • 乱序消息处理：能够处理网络传输中可能出现的消息丢失或乱序问题

在机械工程中，“棘轮”（Ratchet）是一种齿轮装置，仅允许齿轮向一个方向自由转动，但阻止其向反方向转动，在密码学中被借用来形象地描述"密钥演进的单向性"

### 棘轮组成

既然称为“双棘轮”，那么肯定是由两条棘轮组成的，分别是

* • 对称密钥棘轮：基于 KDF 链，每发送或接收一条消息就更新一次密钥
* • DH 棘轮：基于非对称密码，在双方交替发送新公钥时更新根密钥和链密钥

将在下文详细解释这两棘棘轮的原理及如何搭配获得 FS 和 PCS 安全

### 算法原理

#### KDF 链

KDF 链是双棘轮算法的核心概念。它通过一个密钥派生函数（比如 HKDF），输入一个密钥和一些数据，输出一个新的密钥和一部分作为消息密钥，特性如下：

* • 弹性：即使攻击者控制了输入，只要不知道 KDF 密钥，输出看起来也是随机的
* • 前向安全性：如果攻击者获得了当前的 KDF 密钥，无法推导出过去的输出密钥
* • 可恢复性：如果攻击者获得了当前的 KDF 密钥，但后续输入了足够的熵（通过 DH 棘轮），那么未来的输出密钥也会恢复安全性

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA5fCweicu4aticaMVKAfgQ2fm2DNnYfKFrjiaSrtJCtd9yX6X5UzZMmKpXhiahpGicVFBVSz2dic60WBTgve5uAd4pbyWWPziar9muDAw/640?wx_fmt=png&from=appmsg)

在双棘轮中，每个参与者维护三条KDF链：

* • 根链：用于混合 DH 计算结果，生成新的链密钥
* • 发送链：用于生成发送消息的密钥
* • 接收链：用于生成接收消息的密钥

#### 对称密钥棘轮

每发送或接收一条消息，发送链或接收链就会向前“转动”一步，使用当前的链密钥（Chain Key）和一个常数作为输入，通过 KDF 生成一个新的链密钥和一个消息密钥（Message Key）

每条消息都有唯一的加密密钥，消息密钥使用后应立即删除，确保了前向安全性

但是，由于常数是公开的，所以单条对称密钥棘轮**不具有**妥协后安全性

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA7EDBx5GTWIx6criabufsH6WAwacmr0ibwfxI5nQbNibkF7LesIYJoQLkcqib89C9icgiac9p7O8PicZabnd3iaEF0NOv7LGFvmzM2IKvc/640?wx_fmt=png&from=appmsg)

#### DH 棘轮

为了提供妥协后安全性，双棘轮算法引入了另一条 DH 棘轮来注入新的熵，通信双方轮流生成新的 DH 密钥对，并将公钥附带在消息头中发送给对方

1. 1. 当收到对方的新公钥时，触发 DH 棘轮步骤
2. 2. 使用本地的私钥和对方的新公钥进行 DH 计算，得到一个共享密钥
3. 3. 将这个共享密钥输入到根链中进行更新
4. 4. 根链输出新的发送链密钥和接收链密钥
5. 5. 本地生成一个新的 DH 密钥对，替换旧的密钥对

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA4RvOVAteBicsD6U2v9g1A0kYq6AU2RcmCgwrzZ4OFshElU8E68WYmyrF2ibkXELcMm0x2YlpanI2VibKXjXosambn0vzEJrFicEDM/640?wx_fmt=png&from=appmsg)

即使攻击者窃取了某一时刻的链密钥，一旦双方完成一次 DH 棘轮交换，新的链密钥将依赖于攻击者无法获得的 DH 共享密钥，从而恢复安全性（PCS）

DH 棘轮步进发生在“发信者身份轮切换时”，意思就是

* • 对话是交替进行的
* • A 连发多条消息：A 使用当前的发送链密钥加密，不需要每次都进行 DH 棘轮步进
* • B 开始回复（发信者身份切换），生成一个新的 DH 密钥对，执行 DH 棘轮步进

如果一直不切换，那么就没有妥协后安全性，但这不是设计的缺陷，而是无法实现真正意义上的“强妥协后安全性”

从信息论的角度看，在封闭系统中，熵是守恒或递减的，绝不会凭空出现、自动增加，如果攻击者掌握了系统当前的所有状态（密钥、内存、算法代码），那么对于攻击者来说，系统的“不确定性”为 0，意味着该系统未来的任何输出（新密钥）都是确定性的

双棘轮算法中的“交互”（发信者身份切换），其核心作用就是打破封闭系统，从外部引入新的熵。因为对方系统的密钥对，对于本系统来说，是无法预测的“黑盒”，对攻击者来说，就是提高了系统的不确定性

### 乱序消息处理

为了支持乱序消息，消息头还需要额外包含当前 DH 公钥、前一个发送链的消息数（PN）、当前消息在链中的序号（N）。接收方根据 PN 和 N 计算出跳过了多少条消息，预先计算这些消息密钥并暂存，直到对应的乱序消息到达

为了防止拒绝服务攻击，通常会限制暂存的跳过密钥数量

# MLS 协议

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kGhLgo0BUA4rpBTfU5zibzrkM8HQib5tV0iaTzfPKmUichvrkfdrAROibIicLsbUl3mHNyursCenFff1Zfxmakszqibul477Bs2Pxmfr4TLCwCvkkM/640?wx_fmt=png&from=appmsg)

~~MLS协议好复杂，原文章写的有点乱，以后有时间润色一下再重新发公众号吧，这里小小留个坑先（~~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/f2j8DeXVicRQ9KGpr3vDNkdIwyasHFEWCmJibCSicITuAqbVgkygYicev0lUCVEj7B2XfSpnEhs6o7mVylZW5gzorA/0?wx_fmt=png)

crackme安全实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/f2j8DeXVicRQ9KGpr3vDNkdIwyasHFEWCmJibCSicITuAqbVgkygYicev0lUCVEj7B2XfSpnEhs6o7mVylZW5gzorA/0?wx_fmt=png)

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