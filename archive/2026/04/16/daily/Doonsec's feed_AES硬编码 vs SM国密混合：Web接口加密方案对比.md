---
title: AES硬编码 vs SM国密混合：Web接口加密方案对比
url: https://mp.weixin.qq.com/s/TlJs_EOyDo0rHUvMNUD7ew
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:43:39.821614
---

# AES硬编码 vs SM国密混合：Web接口加密方案对比

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nX68dP9Wa1Z1VO0AMWKiaIKezPazmtqCDNdibZh1uCN2TGJa60qaHfAIhp6xlNLWTgiarUesoib15kLDpd70QVlSBfRZvm60X4ne7zqzNssyM0I/0?wx_fmt=jpeg)

# AES硬编码 vs SM国密混合：Web接口加密方案对比

原创

我真tm厉害
我真tm厉害

黑客茶话会

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Web接口加密方案深度对比

AES-ECB 对称加密 vs SM2+SM3+SM4 国密混合加密

HTTPS就够了？企业级应用往往需要在应用层再加一层加密。但加密方案选错了，可能比不加密更危险。本文通过两个真实渗透案例，拆解两种典型接口加密方案的架构差异和安全后果。

一、为什么需要应用层加密？

很多人觉得上了HTTPS就万事大吉，但现实没那么简单：

|  |  |
| --- | --- |
| 🔓 | **中间人解密** — 企业部署根证书后，Burp Suite直接抓明文 |
| 📋 | **日志泄露** — 服务端Nginx/网关日志可能记录完整请求体 |
| ⚖️ | **合规要求** — 医疗、金融行业法规要求传输和存储均需加密 |
| 🔧 | **API暴露** — 第三方调用、开放平台场景，HTTPS只保护传输链路 |

二、方案A：AES-ECB 对称加密

▸ 加密流程（5步）

|  |  |
| --- | --- |
| ① | 前端构造明文JSON请求体 |
| ② | JSON字符串 → UTF-8字节数组 |
| ③ | AES-128-ECB模式加密 |
| ④ | Base64编码密文 |
| ⑤ | Base64字符串作为请求体发送 |

▸ 密钥管理

patchKey = 'qwertyuiopasdfgh'
realKey = patchKey.substring(0, 16) // AES-128密钥

密钥直接硬编码在前端JS代码中，浏览器F12即可获取。前后端共享同一把固定密钥，永远不变。

▸ 安全问题清单

|  |  |
| --- | --- |
| ✗ | **ECB模式** — 相同明文块→相同密文块，密码学基本错误，可分析密文模式推断明文 |
| ✗ | **硬编码密钥** — 前端源码直接暴露，等于"把钥匙放门垫下" |
| ✗ | **无签名验证** — 无法检测请求篡改，无法验证响应真实性 |
| ✗ | **ZeroPadding** — 非标准填充方式，解密边界模糊 |
| ✗ | **单一密钥** — 泄露一次，全部历史数据可解密 |

三、方案B：SM2+SM3+SM4 国密混合加密

▸ 架构：双层加密 + 签名验证

**外层 SM2 非对称加密**（保护整个数据包）
└─ **内层 SM4 对称加密**（保护业务数据）
    └─ **SM3 哈希签名**（验证完整性）

▸ 请求加密流程（7步）

|  |  |
| --- | --- |
| ① | 随机生成sm4Key（10~20位，大小写字母+数字） |
| ② | SM4-ECB加密JSON请求体 → 密文content |
| ③ | SM3哈希{content, timestamp} → 请求签名sign |
| ④ | SM2公钥加密sm4Key → 加密后的密钥字符串 |
| ⑤ | 组装内层JSON：{content, sm4Key, sign, timestamp} |
| ⑥ | SM2公钥加密整个内层JSON → 最终密文 |
| ⑦ | 最终密文 → Hex字符串 → 发送请求体 |

▸ 核心伪代码

sm4Key = randomString(10~20)
content = SM4\_ECB\_Encrypt(jsonBody, sm4Key)
sign = SM3({content, timestamp})
encryptedKey = SM2\_Encrypt(sm4Key, publicKey)
innerData = JSON({content, sm4Key: encryptedKey, sign, ts})
finalCipher = SM2\_Encrypt(innerData, publicKey)
requestBody = finalCipher.toHex()

▸ 安全优势

|  |  |
| --- | --- |
| ✓ | **动态密钥** — 每次请求独立sm4Key，泄露仅影响单次 |
| ✓ | **双层加密** — 内SM4保护数据，外SM2保护整个数据包 |
| ✓ | **请求签名** — SM3哈希验证请求完整性和真实性 |
| ✓ | **响应验签** — SM2签名验证响应来源，防中间人篡改 |
| ✓ | **国密合规** — 符合国内医疗、金融等行业合规要求 |

▸ 仍需改进

⚠ SM4仍用ECB模式 — 建议改CBC或GCM

⚠ SM2公钥硬编码 — 建议通过接口动态获取

⚠ 双层架构复杂 — 对开发人员密码学素养要求高

四、核心差异对比

|  |  |  |
| --- | --- | --- |
| 对比维度 | 方案A：AES-ECB | 方案B：SM国密混合 |
| 加密算法 | AES-128-ECB | SM2 + SM3 + SM4 |
| 密钥类型 | 固定对称密钥 | 动态随机密钥 |
| 密钥管理 | 前端硬编码 | SM2密钥交换 |
| 签名验证 | 无 | SM3签名 + SM2验签 |
| 密钥泄露影响 | 全部历史数据暴露 | 仅影响单次请求 |
| 抗篡改能力 | 无任何保护 | 完整双向认证 |
| 合规性 | 基础 | 国密标准认证 |
| 实现复杂度 | 低 | 高 |

五、加密方案最佳实践

▸ 算法选择

|  |  |
| --- | --- |
| **对称加密** | AES-GCM 或 SM4-GCM，坚决避免ECB |
| **密钥交换** | RSA-OAEP / SM2 非对称加密 |
| **签名摘要** | HMAC-SHA256 / SM3 |
| **填充方式** | 统一PKCS7，禁止自定义填充 |

▸ 密钥管理

🔑 实施动态密钥交换，禁止硬编码

🔑 密钥定期轮换，设置生命周期

🔑 使用KMS（密钥管理服务）统一管理

🔑 前端只存公钥或临时令牌

▸ 架构设计

🏗 "非对称交换密钥 + 对称加密数据"混合架构

🏗 增加请求签名 + 响应验签

🏗 添加timestamp + nonce防重放

🏗 HTTPS + 应用层加密 = 纵深防御

▸ 开发红线

🚫 不要自己实现加密算法，用Bouncy Castle或OpenSSL

🚫 不要用ECB模式，永远不要

🚫 不要在前端硬编码对称密钥

🚫 不要跳过安全评估和渗透测试

总结

方案A（AES-ECB硬编码）是典型的"看起来加密了，实际等于没加密"。ECB模式 + 硬编码密钥 + 无签名，在渗透测试面前毫无抵抗能力。

方案B（SM国密混合）体现了专业安全设计：动态密钥保证前向安全，双层加密提供纵深防御，SM3签名确保数据完整性，SM2验签实现双向认证。

**核心原则：**用混合加密体系代替单一对称加密，用动态密钥代替固定密钥，用签名验证代替盲目信任。

黑客茶话会 · 安全技术分享

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

黑客茶话会

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XCnU3W0ibv6wxwenPYokRNMKjlj60e9AfziaFLIaibO8hjXTFKE3zKTKnst388z1Tz7Kia3KicOMOnicGh1fNiaH6uJxw/0?wx_fmt=png)

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