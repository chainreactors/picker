---
title: 密评专栏丨什么是IPsec？
url: https://mp.weixin.qq.com/s/T_bBG3ia2NBLPWXb-zJZkw
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:07:35.378155
---

# 密评专栏丨什么是IPsec？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTzbaSmiamjNJ9df9599qqoKDJictuEicYBdNbib1Z8jkyNT2th7V4HFS3cJ8Fo476TCKXBdHkdUDmRJcl6kQ1MM8zpdfeXFQ6PZttc/0?wx_fmt=jpeg)

# 密评专栏丨什么是IPsec？

创信华通

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 一、IPsec 到底是什么？

**IPsec（Internet Protocol Security）是一套工作在网络层（三层）的安全协议族，给 IP 数据包加 “加密 + 防篡改 + 身份认证 + 抗重放” 保护，让原本裸奔的 IP 流量在公网上能像走专线一样安全。**

* 位置：OSI模型的第三层（网络层）
* 保护对象：**所有 IP 流量**（TCP/UDP/ICMP/ 路由协议都能保护）
* 典型用途：**IPsec VPN（站点间、远程办公）**
* 对比 TLS：TLS 是四层 / 应用层，只保护特定应用；IPsec 是三层，**全网无感知加密**

---

## 二、为什么需要 IPsec？——IP 天生不安全

原始 IP 协议只有寻址和转发，没有任何安全能力：

1. **明文传输**：抓包就能看到全部内容
2. **易篡改**：中间人改几个比特，接收方无法发现
3. **源地址可伪造**：IP 欺骗攻击很常见
4. **无抗重放**：旧包重发，系统会重复处理

**IPsec 的核心目标：给 IP 补上四大安全能力**

* **机密性 Confidentiality**：加密，窃听也看不懂
* **完整性 Integrity**：防篡改，改了就校验失败
* **真实性 Authentication**：确认对方身份，不被冒充
* **抗重放 Anti-replay**：旧包不能重复使用

---

## 三、IPsec 三大核心组件（AH、ESP、IKE）

### 1. AH（Authentication Header，认证头，协议号 51）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dqQlX2VCwTzuEVbXmIYdlTqTEsKnYmdwUffpxvMIic1PCWVnu0UQCibgyXGrsdr5pibFnxOp96ERoltU0ECCYBdBJrB4R2Y9O56LA6Yjwiaxnp0/640?wx_fmt=png&from=appmsg)

只做**认证 + 完整性 + 抗重放，不加密**。

* 保护范围：**整个 IP 包（部分可变字段除外）+ 数据**
* 特点：强认证，但**不支持 NAT 穿越**（NAT 改 IP 头会破坏 AH 校验）
* 现状：**基本被 ESP 取代**，很少单独用

### 2. ESP（Encapsulating Security Payload，封装安全载荷，协议号 50）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dqQlX2VCwTwV9SYu3D4V4HhsPe9NfH4JmhN06GhWHet9LIKmUWpOZFH3aPahFdo0ibHbKDKJSftCHGpAtXEDUe5Y7Rfw13W8o9DX0pp32ykY/640?wx_fmt=png&from=appmsg)

**加密 + 认证 + 完整性 + 抗重放全功能**，IPsec 主力协议。

* 加密范围：**IP 数据（传输模式）或整个原始 IP 包（隧道模式）**
* 认证范围：**ESP 头 + 加密数据 + 部分外层 IP 头**
* 优势：**支持 NAT 穿越、加密能力强、灵活**
* 格式概览（隧道模式）：

```
外层IP头 | ESP头 | 内层IP头 | 原始数据 | ESP尾 | 认证数据
```

### 3. IKE（Internet Key Exchange，密钥交换协议）

**负责自动协商密钥、算法、SA，建立安全通道**，分两个阶段：

* **IKE SA（第一阶段）**：双方先认证身份（预共享密钥 / 证书），协商加密 / 认证算法，生成一个**安全的控制通道**（Parent SA）
* **IPsec SA（第二阶段）**：用 IKE SA 保护，协商**数据通道**的加密算法、密钥、SA 生命周期，生成**双向 IPsec SA**（Child SA）
* 特点：**密钥自动更新、动态协商、减少手工配置**IETF

> 简单记：**IKE 管 “握手和密钥”，ESP/AH 管 “数据保护”**

---

## 四、两个核心模式：传输模式 vs 隧道模式

### 1. 传输模式（Transport Mode）

在传输模式中，AH头或ESP头被插入到IP头与传输层协议头之间，保护TCP/UDP/ICMP负载。传输模式不改变报文头。

![](https://mmbiz.qpic.cn/mmbiz_png/dqQlX2VCwTzW73HnyZoAa7TnydLBN1uibRH6qUUvMibhNMCTzicmRRVT70KSHnn4MJz9avY0hNlX4TgyfScfgmibuwDHHLocNF0CdRZtlPoHyjM/640?wx_fmt=png&from=appmsg)

* 传输模式下，AH协议的完整性验证范围为整个IP报文。ESP协议验证报文的完整性检查部分包括ESP头、传输层协议头、数据和ESP报尾，但不包括IP头，因此ESP协议无法保证IP头的安全。ESP的加密部分包括传输层协议头、数据和ESP报尾

### 2. 隧道模式（Tunnel Mode）—— 最常用

在原IP头部之前插入ESP/AH头部，同时生成新的IP头部 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dqQlX2VCwTwiaJRb7kyFXCY8SZicXiaMGDvibUouyTMqBFMRNnrJyCIWuTBLxTmFUiamosfiay0D7WEH7kMdDrJZ84cvicjpSV1SibDrL0eFg48zMDY/640?wx_fmt=png&from=appmsg)

* 隧道模式下，AH协议的完整性验证范围为包括新增IP头在内的整个IP报文。ESP协议验证报文的完整性检查部分包括ESP头、原IP头、传输层协议头、数据和ESP报尾，但不包括新IP头，因此ESP协议无法保证新IP头的安全。ESP的加密部分包括原IP头、传输层协议头、数据和ESP报尾。

对比表：

| 模式 | 保护范围 | IP 地址 | NAT 穿越 | 典型场景 |
| --- | --- | --- | --- | --- |
| 传输模式 | 端到端 | 原 IP 暴露 | 不支持 | 主机间通信 |
| 隧道模式 | 站点到站点 | 内层隐藏，外层可见 | 支持 | VPN、远程接入 |

传输模式和隧道模式的区别在于： 从功能来讲，传输模数主要用于主机之间通信、隧道模式主要用于站点间通信；从安全性来讲，隧道模式优于传输模式。它可以完全地对原始IP数据报进行验证和加密。隧道模式下可以隐藏内部IP地址，协议类型和端口。 当安全协议同时采用AH和ESP时，AH和ESP协议必须采用相同的封装模式。

## 五、安全关联 SA：IPsec 的 “安全规则表”

**SA（Security Association）是通信双方协商好的一套安全参数集合，定义了 “如何保护数据”。**

* 核心参数：

+ 协议：AH 或 ESP
+ 加密算法：AES-256、3DES
+ 认证算法：HMAC-SHA256
+ SPI（安全参数索引）：**32 位唯一标识**，用于查找 SA
+ 源 / 目的 IP、模式、生命周期

* 特点：

+ **单向**：A→B 一个 SA，B→A 另一个 SA
+ 由 IKE 自动生成，或手工静态配置
+ 数据收发时，通过 **SPI + 目的 IP + 协议** 定位 SA

---

## 六、IPsec 完整工作流程（隧道模式为例）

1. **感兴趣流触发**：路由器 / 防火墙识别需要加密的流量（如内网 10.0.0.0/24 到对端 10.1.0.0/24）
2. IKE 第一阶段（主模式 / 野蛮模式）：

* 双方交换策略、认证身份（PSK / 证书）
* 协商 IKE 加密 / 认证算法，生成共享密钥
* 建立 **IKE SA（控制通道）**，后续协商加密进行

3. IKE 第二阶段（快速模式）：

* 用 IKE SA 保护，协商 IPsec 策略
* 生成 **IPsec SA（数据通道）**，双向各一个
* 协商密钥、算法、SA 生命周期

4. 数据加密传输（ESP 隧道模式）：

* 原始 IP 包（内层）→ 加 ESP 头 → 加密 → 加外层 IP 头 → 发送
* 接收方：剥外层 IP → 解密 → 校验认证数据 → 还原原始 IP 包 → 转发

5. **SA 维护与销毁**：生命周期到期或流量超时，IKE 自动重协商或删除 SA

   **- END -**

   供稿：杨老师

   编辑：小   鱼

   审核：王老师

   点击回顾往期精彩

   ![](https://mmbiz.qpic.cn/mmbiz_gif/dqQlX2VCwTxMuWIZJIIawtUSXg4qNPXWE1AtRgKIkYntL5ZowsH2uJwOEtKIVYYTFvqTG8PlvWVAiayC0qa3pAKWrGLln3IiahKsNM1RQmOl0/640?wx_fmt=gif&from=appmsg)

   [《网络数据安全风险评估办法》正式发布，重要数据处理者迎来年度"必答题"](https://mp.weixin.qq.com/s?__biz=MzUxNTQxMzUxMw==&mid=2247528545&idx=1&sn=f64f22c66bfa1f885cc2605d72b3851c&scene=21#wechat_redirect)

   [网络安全漏洞通告（2026年6月）](https://mp.weixin.qq.com/s?__biz=MzUxNTQxMzUxMw==&mid=2247528533&idx=1&sn=b630daef422fa3029ebec8e38b26e404&scene=21#wechat_redirect)

   [当创信人走近“来自星星的孩子”：守护网络安全，更守护童心](https://mp.weixin.qq.com/s?__biz=MzUxNTQxMzUxMw==&mid=2247528391&idx=1&sn=fb352d7ad857a9624fec44080cde2391&scene=21#wechat_redirect)

   **成都创信华通信息技术有限公司**

   成都创信华通信息技术有限公司是川内首家同时拥有“等保”与“密评”双资质的网络安全合规检测服务商，以**“等保测评+密码测评+软件测试+信息系统工程监理+数据安全服务+网络安全服务”**为主的**“6+N”**服务模式，已成功为党的二十大、中国共产党成立100周年、北京冬奥会、第31届世界大学生运动会、第12届世界运动会等大型活动提供等保、密评、网络安全应急保障服务。

   公司以“竭尽全力为国家网络安全保驾护航”为使命，凭借多年积累荣获四川省“专精特新”企业、四川省新经济100强企业、四川省数字经济100强企业、成都市网络信息安全产业影响力TOP30企业等。

   期待与您的合作！

   ![](https://mmbiz.qpic.cn/mmbiz_jpg/dqQlX2VCwTwbtPDZ3FMhSFQE7DLenuHm9sQKOHFc3Q0bBFpCyooXcYv0NzIRquDVIHbIrRTA91EA7x6oUYvP86rsh2Q4orswmEbrfsliafDw/640?wx_fmt=jpeg&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/d50Fbx4g7hYqneiahxyj0YwhCDshjoHwVy8yM7HOicibibIL0p3SWtMvBl0MdGoDKLrlQUlibBgAsKG8UeOkmsoGvkg/0?wx_fmt=png)

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