---
title: 【面试题】一些整理的JWT的面试题
url: https://mp.weixin.qq.com/s/1lVdJdI45FBw3_E2wmwGfg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:00.411720
---

# 【面试题】一些整理的JWT的面试题

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icCLY10D8tvLPu6nO6oEF7Jk5p5SqO3RfQJgibibDzYg6v8KSPuYApXwDiaHcDIkibUfBxK7PodqFUydhP6hGGAJKibmgNVK8ZP1gGicHWBWbgpwk0/0?wx_fmt=jpeg)

# 【面试题】一些整理的JWT的面试题

原创

小王
小王

好靶场

![]()

在小说阅读器中沉浸阅读

58.5

💡 好靶场

团队宗旨：我们立志于为所有的网络安全同伴制作出好的靶场，让所有初学者都可以用最低的成本入门网络安全。所以我们团队名称就叫“好靶场”。

我们承诺每天至少更新1-2个新靶场。我们要的是稳定更新，而不仅仅是堆叠数量。

* • 全球第一家以SRC报告为蓝图制作靶场的网络安全靶场平台。
* • 全球第一家引入AI靶场助教的网络安全靶场平台。
* • 14个不同方向靶场供你选择。
* • 代码审计+漏洞修复靶场全新上架。

* • 无门槛费，每次开启不扣除积分，不扣除金币，超级会员每天不限次数开启靶场。
* • 靶场独立，每个靶场环境完全隔离。

# 好靶场目前进度

815

靶场数量

210个

漏洞报告数量

# 概述

大家经过上面的内容应该已经对JWT相关问题有一个很深刻的认识，我们本节主要是针对JWT漏洞的一个整理和总结，以及一些常见的面试题。这些面试题会随着积累而增加。

# 漏洞例举

以下是目前整理出来的漏洞。具体的学习内容可以查看这个。

http://www.loveli.com.cn/chapter\_course\_list?course\_id=81

* • Signature未校验签名有效性
* • alg标签标记为none(无签名)
* • alg标签标记为空
* • JWT 对称加密弱密钥
* • JWT Tool 使用手册
* • JWT 默认密钥问题
* • JWT 头部注入绕过 JWT 身份验证
* • JKU远程公钥加载
* • KID 空文件绕过JWT 身份验证
* • KID 空文件绕过JWT 身份验证-变种1
* • JWT 公钥泄露+算法混淆
* • JWT 算法混淆 + 公钥推导
* • JWT 敏感信息泄露

# 面试题目

## 什么是JWT？它的结构是怎样的？

* • JWT（JSON Web Token）是一种用于身份验证和信息传递的**无状态令牌**，由Header、Payload、Signature三部分组成，格式为`Header.Payload.Signature`。
* • **Header**：说明令牌类型和签名算法（如`{"alg":"HS256","typ":"JWT"}`）
* • **Payload**：存放实际数据（用户ID、角色、过期时间等）
* • **Signature**：对前两部分的签名，防止篡改

**深度扩展**：

* • 对比Session认证：JWT无需服务器存储状态，适合分布式系统
* • 强调**Header和Payload仅是Base64编码，未加密**，敏感信息不应放在Payload中

## JWT的签名算法有哪些？对称与非对称的区别？

**标准答案**：

* • **对称算法**：HS256（HMAC + SHA256），使用同一个密钥进行签名和验证
* • **非对称算法**：RS256（RSA + SHA256），私钥签名，公钥验证
* • **其他**：ES256（ECDSA）、PS256等

**深度扩展**：

* • 解释**算法混淆攻击**的原理：服务器预期用RS256，攻击者改为HS256，并用服务器公钥作为HMAC密钥
* • 提及`alg: none`漏洞：早期JWT库支持无签名算法

## 列举常见的JWT攻击类型并简述原理

以下是目前整理出来的漏洞。具体的学习内容可以查看这个。

http://www.loveli.com.cn/chapter\_course\_list?course\_id=81

* • Signature未校验签名有效性
* • alg标签标记为none(无签名)
* • alg标签标记为空
* • JWT 对称加密弱密钥
* • JWT Tool 使用手册
* • JWT 默认密钥问题
* • JWT 头部注入绕过 JWT 身份验证
* • JKU远程公钥加载
* • KID 空文件绕过JWT 身份验证
* • KID 空文件绕过JWT 身份验证-变种1
* • JWT 公钥泄露+算法混淆
* • JWT 算法混淆 + 公钥推导
* • JWT 敏感信息泄露

## JKU注入和JWK注入的区别？

**标准答案**：

* • **JWK注入**：直接在JWT Header中嵌入`jwk`字段，包含攻击者的公钥
* • **JKU注入**：在Header中设置`jku`字段，指向一个URL，服务器从该URL获取JWKS公钥集
* • **关键区别**：JWK是内联公钥，JKU是远程获取公钥集

**深度扩展**：

* • 攻击条件：服务器未验证JKU来源的合法性
* • 防御：限制JKU域名白名单、不信任用户提供的JKU

## 如何有效防御JWT漏洞？

**标准答案**：

1. 1. **强制算法白名单**：只允许预期的算法（如只接受HS256）
2. 2. **严格过滤Header参数**：不信任客户端传来的`alg`、`kid`、`jku`等
3. 3. **实施零信任后端验证**：

* • 始终验证签名，即使`alg`为`none`
* • 密钥与算法绑定（HS256用对称密钥，RS256用非对称密钥对）

4. 4. **安全配置**：

* • 使用强密钥，定期轮换
* • 设置合理的过期时间（`exp`）
* • Payload不存放敏感信息

## 你在实战中如何检测JWT漏洞

1. 1. **识别JWT**：在Cookie或Authorization头中寻找`eyJ`开头的字符串
2. 2. **解码分析**：用`jwt.io`或Burp插件查看Header和Payload
3. 3. **测试点检查**：

* • 修改`alg`为`none` → 空算法漏洞
* • 修改Payload数据（如`role:admin`）→ 未验证签名
* • 查找公钥端点（`/jwks.json`）→ 算法混淆可能
* • 检查`kid`/`jku`参数 → 注入漏洞
* • ...这里参考上述漏洞

4. 4. **工具辅助**：Burp的`JWT Editor`插件、`jwt_tool`

## 如果发现JWT使用弱密钥（如"secret"），如何利用

1. 1. 使用字典爆破密钥（工具：`hashcat`、`jwt-cracker`）
2. 2. 爆破成功后，用该密钥重新签名伪造的Payload
3. 3. 实现越权访问（如普通用户→管理员）

## 描述一次你利用JWT漏洞的实际经历

**标准答案框架**：

* • **情境**：在XX渗透测试/CTF比赛中
* • **任务**：需要获取管理员权限
* • **行动**：

1. 1. 发现JWT存储在Cookie中
2. 2. 解码发现`alg: HS256`，Payload有`role: user`
3. 3. 尝试修改`role: admin`，签名无效
4. 4. 找到`/jwks.json`端点，获取公钥
5. 5. 实施算法混淆攻击，成功提升权限

* • **结果**：获取管理员后台访问权限，报告漏洞

> 这里注意你可以把上述所有的JWT漏洞全部念一遍

# 总结：

一般的情况下，最爱问的就是JWT有哪些漏洞，解释原理以及攻击方式，然后就是你遇到过的哪些JWT实际案列。

# 好靶场介绍

零基础入门不迷茫！专属网络安全从零到一体系化训练——配套完整靶场+精选学习资料，帮你快速搭建网安知识框架，迈出入门关键一步！

全场景实战全覆盖！聚焦Web渗透工程师核心能力，深度拆解TOP10逻辑漏洞，精通PHP代码审计、Java代码审计等核心技能，从基础原理到实战攻防，覆盖行业高频应用场景！

真实漏洞场景沉浸式体验！src训练专题重磅上线——1:1还原真实漏洞报告，让你亲身感受实战挖洞流程，积累符合企业需求的实战经验！

有宝子就问了，主播主播，这么好的靶场怎么用：

首先关注好靶场

然后发送bug，可以点击链接直接登录

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvve2xib0I0O5XTibibicpcNb2b3lFm6AtzAT4Zl3icT2ticC7icP7kLJahMmgPKc0ecuNcq373kXXsyibplw/640?wx_fmt=png&from=appmsg)

#### 福利1：

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvXVIibapFtib6OxTy5TW0HJdlhE9EIicfBe4AsJUQIJ7IRUs9SB0503rHe4ia5P80habCuCPlUQjEGjA/640?wx_fmt=png&from=appmsg)

找到个人中心，邀请码输入0482d6d28539424c，白嫖14天高级会员。

#### 福利2：

关注好靶场bilibili。拿着关注截图找到客服，领取5积分或者7天高级会员。

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBtNhnwsibMqDG31CpA7qQKa81Ym01iamwlkmxPzLsI73ptEwJ3D0S7ZKTFRDlIrM3iaIiaYcyVtGbMnLw/640?wx_fmt=png&from=appmsg "null")

# ~ 每日限免 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wWnCm40UQo3upJtdZDSSpMQoxM02icLjFT7FzZzkVMVelrlEDibev1EDaPbiaSTHojEJxOvlvu3Qa6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

    为了能让更多的宝子可以免费的开启会员靶场，我们会在工作日随机开放一些靶场的限免，还请加群关注。我们会以如下的方式在群里通知。

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvDtuNKem9kEYXZPnR8icGAXbdy4ibHbWM9Oa1zWDaFBYIribtRB8KQdrAYuYjMxiae2UFx7W8yFsUuGA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvDtuNKem9kEYXZPnR8icGAXDCGrKBD8iaCpACtAn87ncaxPJjhukOmrbQ8F6S7rnLKRsAbMdBgjp7g/640?wx_fmt=png&from=appmsg)

# **~** 内部群 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wWnCm40UQo3upJtdZDSSpMQoxM02icLjFT7FzZzkVMVelrlEDibev1EDaPbiaSTHojEJxOvlvu3Qa6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

加群不收费哈！！！交流群里会每天更新限免靶场，以及免费学习资料。

进一个群就可以，所有的通知都会通知到位

进交流群，请加我好友

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBs73DYicxITQPQsBVqHAu48icqickaJDCvv6zqQdibzakNgCA7NyKdfvJjETfibNQqX9vuPGUUuklGoRQQ/640?wx_fmt=png&from=appmsg)

喜欢玩QQ的宝子们可以加这个QQ群

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvP29u5t2iaAicTeGA9f2DicBU9Fxt45RyGTdjibCHCNIIvwsRrTTL7gLrO9iamaZBtgVibYSFpHsz7uwZQ/640?wx_fmt=png&from=appmsg)

**~**

AI客服内测ing

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ELQKhUzr34wWnCm40UQo3upJtdZDSSpMQoxM02icLjFT7FzZzkVMVelrlEDibev1EDaPbiaSTHojEJxOvlvu3Qa6w/640?wx_fmt=png&from=appmsg&watermark=1&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

可以完成简单的客服能力，以及靶场推荐

![](https://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBsOqIxrNhIgec8tYziaickpVF3bHRTPAyaBaMgRPngTVJRmCpApOeNiaiaagJXZXmqRR5WNBbdJTrDtfA/640?wx_fmt=png&from=appmsg)

# 会员订阅

首先点击会员订阅

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvL0lia2u1nNacRPsGManicYyYENDcXMK8JvRKxnLMQ5fRF89GuvgyxnFIcuZBS0SKEFsI0cTo1j9YERW9qad7SjVW1QXqU9o21wQ/640?wx_fmt=png&from=appmsg)

##

## 然后选择对应的套餐

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icCLY10D8tvLZDZP0Aibbr9vaJNcWYkLrhjG6mx2nIlnIVFU4rdQrIZgUx3FjQXMqnCTMRhg5CQmuaAJgSD5X6FkFU5sgj7eNI9wG0tEdSIws/640?wx_fmt=png&from=appmsg)

##

## 选择去支付

##

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvL9MiabG0hFP2WApianrv99EPjziabzLlTt85cW3LTW22jo6HgZibksG59ibwO1F2t2n4Dn5pJO4UbskHnQVjmhCQib7vicCcvsrmjSKA/640?wx_fmt=png&from=appmsg)

##

## 支付完成后即可会员到账

##

![](https://mmbiz.qpic.cn/mmbiz_png/icCLY10D8tvLiazKvfyEZOMyk1YxDbLU2ZUgLA3vU4W6KOqUiashYibBhzzAt39Z4Or66R7kjUhibXApNUbGaKV60dniaUuCA7edzn1b8Zd2c6duk/640?wx_fmt=png&from=appmsg)

有什么好的建议可以在留言区评论哦

##

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvK2C7klp7wKKhoR7iamhAw3AVsjpcIvpHzC5YZWjhMSQ6s5sWRLqawfkh3SXcMGw99vGgwRBMkGeA/0?wx_fmt=png)

好靶场

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h1AzajLJTBvK2C7klp7wKKhoR7iamhAw3AVsjpcIvpHzC5YZWjhMSQ6s5sWRLqawfkh3SXcMGw99vGgwRBMkGeA/0?wx_fmt=png)

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