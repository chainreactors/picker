---
title: 终于发新版了！
url: https://mp.weixin.qq.com/s/3aVJnc8cmxXGvQJET7YL2g
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:45:32.569174
---

# 终于发新版了！

# 终于发新版了！

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

铜锁8.5.0 正式版发布！

以下文章来源于铜锁密码学开源项目
，作者多次跳票的

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM681TIKtBBR37dMhpdVeYZH0lXtI0zOAjmr0hsgKyujDQ/0)

**铜锁密码学开源项目**
.

铜锁密码学开源社区的公众号。铜锁是开放原子开源基金会旗下的“孵化期”开源社区，包括铜锁开源密码学算法库，铜锁嵌入式版和RustyVault等核心开源项目。

面对Github上同学们满怀期待的问题：

![](https://mmbiz.qpic.cn/mmbiz_png/Wj0Rx0jU5jTxYbPt2YwlEO0NBplicGo5QKspxPujkSywaSibD4sjShKvx1N6n0KicMI2QZbacqicYWnxHw63ngaujO9kLsf1ibiagk9iakosP8rluw/640?wx_fmt=png&from=appmsg)

我们一边修bug一边只能：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wj0Rx0jU5jQvsjbaiagYWl8IxG2rFMycbDqEC0DTFibZIdXfOuZ6AMcxRnhNicbA7QAtibV58gBaQOfct1y7naDdiarMibN2hk98nqKl5Bia9XJftw/640?wx_fmt=jpeg&from=appmsg)

今天我们终于发布了铜锁8.5.0的第一个预发布版本（pre1）！

下载地址：

https://github.com/Tongsuo-Project/Tongsuo/releases/tag/8.5.0-pre1

铜锁8.5.0是一个大版本发布，目标是对齐OpenSSL 3.5.4，包含了对多种抗量子密码（PQC）算法、混合公钥加密（HPKE）算法、以及 TLS PQC密钥协商、QUIC、TCP fast open、raw public key 等协议特性的支持，并大幅提升了 AES-GCM、RSA、HMAC 等密码学算法和 TLS连接的性能（最多可达2x）。

重要更新包括：

* 基础代码迁移到OpenSSL 3.5.4
* 修复多个安全漏洞
* 优化AES-GCM、SM4-GCM、HMAC、CMAC、RSA等密码学方案以及TLS协议的性能，相较8.4.0最多可翻倍

* TLS连接的安全等级默认设置为2，禁用过低的协议版本（如TLS1.1）和安全强度低于112bit的密码算法
* 支持PQC算法ML-KEM、ML-DSA和SLH-DSA，支持PQC密钥协商机制curveSM2MLKEM768、X25519MLKEM768等
* 实现QUIC协议（RFC9000）
* 实现TCP Fast Open（RFC7413）
* 实现HPKE（RFC9180）
* 实现AES-GCM-SIV（RFC8452）
* 支持在TLS中使用raw public key（RFC7250）
* 支持使用brotli和zstd进行证书压缩（RFC8879）
* 支持在TLS1.3 ClientHello中包含多个keyshare
* 添加TLS round-trip时间测量功能
* SMTC Provider适配蚂蚁密码卡（atf\_slibce）
* 增加SDF框架和部分功能接口

* 随机数熵源增加rtcode、rtmem和rtsock
* speed支持测试SM2密钥对生成和SM4密钥对生成
* 增加TSAPI，支持常见密码学算法
* 增加SM2两方门限解密和签名算法
* 增加商用密码检测和认证Provider，包括身份认证、完整性验证、算法自测试、随机数自检、熵源健康测试；增加mod应用，包括生成SMTC配置、自测试功能

欢迎大家踊跃下载试用并在issue中提出意见！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

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