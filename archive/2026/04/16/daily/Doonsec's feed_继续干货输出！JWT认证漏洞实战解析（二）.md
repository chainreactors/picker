---
title: 继续干货输出！JWT认证漏洞实战解析（二）
url: https://mp.weixin.qq.com/s/J0Wjj_WR1GDyxw9ydBVMDw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:45:22.921186
---

# 继续干货输出！JWT认证漏洞实战解析（二）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eDXiba58htLciaicu7qF8pV7AusVgE1wlOfN32UzYzXADAHqb32Qia56CQsic35EAsfOzjkrzER0iadyZsV4Qic5qqft52eC88VhickexAL7aIm2FicE/0?wx_fmt=jpeg)

# 继续干货输出！JWT认证漏洞实战解析（二）

原创

洞悉安全攻防团队
洞悉安全攻防团队

洞悉安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击上方

**蓝字**

关注我们～

Part 01

![](https://mmbiz.qpic.cn/mmbiz_gif/zEUqu7mKQjBohI0v26MRG0XHiaBjRhnU5ywswsDWQZ3TfjQY1IWEPibiboqBtD8RoLx9oscsicyB1D94BmuRVicibsYe5mdZYj1jCX37Ara0XkDAU/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/vmHNWaef13CRUash8WLcW8hpceS5yhanSKjIuJrFWeGSBeqLYS00icdQuiajjQIhPQsAciam49QWXUbuKSoDKQJwf19oU8obH1maEe2wtDZXBk/640?from=appmsg)

通过 JWK 头注入绕过 JWT 认证

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UxfuWGC2h883TnCYz8FJbVVia7ml9Fz8zanzNOicrK8EF00LNicSepKWKJUZyXIibe0saqkTwGyu5tSNVNHkX5Vpkw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/eDXiba58htLdBvvVibAvz2mibzGbh6sb7XoNHNFvpyDDZcibMdgaXz3IbTWMrDCibW9Vwdur2uyNMrtmq2eeJia8SggJZ3BzZ2mm7RDicibHpBMmmW8/640?wx_fmt=gif&from=appmsg)

1. 漏洞原理

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLc2lNvN201fh2GToy3iaL6g8lHFWkCRic1QSAd9FcxMz1AwsB7upK8Fv8Vw3aebHCp5vqyUpKdvUwepAzhNs8x1xicJdzxF8XLhCE/640?wx_fmt=gif&from=appmsg)

JWK（JSON Web Key）是 JWT 头部（Header）中用于存储公钥的字段，主要用于 RSA 等非对称签名算法场景。

    正常情况下，服务端应使用本地预设的可信公钥验证 JWT 签名；若服务端未严格校验 JWK 字段的合法性，甚至直接信任 JWT 头部中携带的 JWK 作为验证公钥，攻击者即可在 Header 中注入自行生成的公钥，让服务端用攻击者的公钥验证签名，最终通过对应私钥伪造任意权限的合法 JWT，实现认证绕过。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/eDXiba58htLdkm5va0yaLtic0jiaibnTJMjiaH71XpLwIEE8F3BmVG5AIxJI7NAGBv79NeHZV35v0ElNRa6pujNcUticya38xpnrDqU6ViaqMWKRuY/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UxfuWGC2h883TnCYz8FJbVVia7ml9Fz8zanzNOicrK8EF00LNicSepKWKJUZyXIibe0saqkTwGyu5tSNVNHkX5Vpkw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/eDXiba58htLcicox4Mcb32yBRQHrTFJRV16TjFbUIWnkF42coSL9NcSPwzxdZD6WMhV1CaBDibfFEkia0CCqZMtwTV1UY9e5MvLibYmTnlDFm2Wc/640?wx_fmt=gif&from=appmsg)

2. 前置知识

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLcIWaBhaGQmKZibcZ7k9qPUpAkFdHkOsrbWNj4qA0IlNBZS1MLXTiaCY36jKOlbkwvzoiaPFZpo7InMYX6sIj6DdgUicXeueokHV5Y/640?wx_fmt=gif&from=appmsg)

JWK 标准结构：包含kty（密钥类型，RSA 场景固定为RSA）、use（密钥用途，签名场景为sig）、alg（签名算法，如RS256）、n（公钥模值，Base64URL 编码）、e（公钥指数，通常为AQAB）、kid（密钥 ID，可选）等核心字段。

    非对称加密逻辑：RSA 算法中，私钥用于签名，公钥用于验签；攻击者需自行生成密钥对，用私钥签名 JWT，用公钥注入 JWK 欺骗服务端验签。

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLdyiahLP2ghr2Be4ce3YKPrdpRDd9ib7eSBGhpeKtAODKLIO7hh6SZdsFxSibYpphuk184t7SF52KzkjIJjRFyNsmJcIQrz2V1PFw/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UxfuWGC2h883TnCYz8FJbVVia7ml9Fz8zanzNOicrK8EF00LNicSepKWKJUZyXIibe0saqkTwGyu5tSNVNHkX5Vpkw/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLdiaC0mlX5F0ibsm0qbgvNuYlRpBv9SymR65tBa7KlD3WFsZjH4q4iaHusyDmIZIX0O3p23TXOrqLG36mzjjgoudYFE5bBoRoxNms/640?wx_fmt=gif&from=appmsg)

3. 实战利用步骤：

1

登录普通用户，抓取合法 JWT

1. 使用普通账号登录系统。
2. 在 Burp Suite 中抓取携带 JWT 的请求包，复制 JWT 字符串。

2

在 Burp 中生成 **RSA****密钥对**

1. #### 打开 **JWT****Editor** 插件 → 切换到 **Keys**面板
2. #### 点击 **New****RSA****Key**，自动生成一组 RSA 公钥 / 私钥。
3. #### 保存该密钥对，用于后续注入与签名。

####

3

将生成的**公钥****注入****JWT****头部**

1. #### **在 Burp Repeater 中选中 JWT，右键选择 **JWT Editor → Edit**。**
2. #### **在 Header 区域添加 / 替换为自己的 JWK 公钥信息。**
3. #### 插件会自动将公钥填充到 `jwk` 字段中

   ####

4

篡改 Payload 为**管理****员****权限**

1. #### **在 Payload 区域修改关键字段：**
2. #### 修改用户 ID、角色等权限标识。

   ####

5

使用**私钥****重新签名并发送**

1. #### **点击****Sign** 按钮，选择刚才生成的 RSA 私钥。
2. #### 插件自动生成新签名，拼接为完整恶意 JWT。
3. #### 发送请求，服务端使用头部注入的公钥验签，成功通过。

   ####

6

成功获取**管理员****权限**

#### **响应返回管理员接口数据、后台入口或敏感信息。**

案例演示：

![](https://mmbiz.qpic.cn/mmbiz_png/v8yrCQN46lGibnfXztFesYNPLQKoYfVFK8VW5TOEhXbAHKkMkLnv7iazSic32VwJqfhUss0jcGeWJY1RlqCS3xCow/640)

1.登录普通用户：

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdcouTZfj2CB0t0UMlrdG67z8SQPfZ5p3qWRcHVlvfCPN8wGEjeOicibXu8h86GbvCkIp7XrSwTqJWTORZxjLSiaBHmibbZEhmxeU0/640?wx_fmt=png&from=appmsg)

2.使用jwt editor获取新的rsa密钥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfEQ8s7GiceXlzztqMgZqYAecW7cdENVDE3viaicIV2IRrUhLj6worzzh8icbExBywS28SzyxdiaWTmSI8NLQQBNgsvtbicGt9wEknLk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdPia1Riaem1Wfa0z4HgxGNogNMuCOTIp5SokXUMutFpJYY7hCqfCbczGPXNC7TCXnAzkyXm44MkOtE0bxNAiaH5DpichnqMC7OrW8/640?wx_fmt=png&from=appmsg)

3.使用burp的jwt插件，注入刚刚生成的rsa密钥

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdJBPSSgwV2QWp4ENLyxvd5Y4RBvPMqcMzUPstUiaabLgwqvY3G0R8rmOrJGxFr5rcZspXQAspiceQJicZlzibfrt16Ec6jQTmcibNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLdx3lB88nRxxBAcPHczKxjmhEo2PQtPK50aKiaW1SaotoJCucicCeibX1u0iceMLa4APD5P1EHGwc7IUXnwsC7auECwovBxqtBXn4M/640?wx_fmt=png&from=appmsg)

4.修改用户为管理员，并点击重新生成sign

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLcRTPZpe7Cx0JkH6IwBmP0K1leRWYfic2u7s06te2hGgvb5jicy3RGlGVPPmL5TaTLwibWHG8M2c8IdsBAYHUV24ZMQ5olgE4ibHjA/640?wx_fmt=png&from=appmsg)

5.成功接管管理员账户：

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfjHfx6iaOA2YEhVTZUoiaLHP40IIr5oz80L4YNRkMQeeTT48ozuSYbfxmWITH52Hx4Qx973pt2rRZpIdWXTpKlpDkiaTpxlsubLw/640?wx_fmt=png&from=appmsg)

Part 02

![](https://mmbiz.qpic.cn/mmbiz_gif/zEUqu7mKQjBohI0v26MRG0XHiaBjRhnU5ywswsDWQZ3TfjQY1IWEPibiboqBtD8RoLx9oscsicyB1D94BmuRVicibsYe5mdZYj1jCX37Ara0XkDAU/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/vmHNWaef13CRUash8WLcW8hpceS5yhanSKjIuJrFWeGSBeqLYS00icdQuiajjQIhPQsAciam49QWXUbuKSoDKQJwf19oU8obH1maEe2wtDZXBk/640?from=appmsg)

通过 kid 头路径遍历实现 JWT 认证绕过

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UxfuWGC2h883TnCYz8FJbVVia7ml9Fz8zanzNOicrK8EF00LNicSepKWKJUZyXIibe0saqkTwGyu5tSNVNHkX5Vpkw/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLeEsibRR9GHaxf51ibibzfLicbjue0JfT73DemztnaxnO1uSwO6yeYIVfIbXib5ll9Z7eXmBYxujWDiamesSjc6pwbBON3quSloSCbPM/640?wx_fmt=gif&from=appmsg)

1. 漏洞原理

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLfAOIK2GQbSR9Tdj786HuqnMoWck15vicluJ6xxG4LRh0x55EQP21WP2zibsWIhRcq3z5z25A0ZuoPWKhcfQic22M1XwH8Nq18Hiao/640?wx_fmt=gif&from=appmsg)

kid（Key ID）是 JWT 头部中用于指定签名密钥的字段，常用于多密钥场景（如不同业务、不同用户对应不同密钥）。

    正常情况下，服务端应根据kid从预设密钥列表中匹配对应密钥；若服务端未对kid做路径校验，直接用kid拼接本地文件路径读取密钥（如/keys/{kid}.pem），攻击者可通过路径遍历（../）读取服务器上的任意文件，甚至指定空密钥、静态文件作为验证密钥，最终绕过签名验证。

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLe6RCx5vcOq1HgPe5V7PRHU5Cn7wB3sGLrPv9HVXH55MjS891pFwcwVrB7VnkQ9MTYWicXxnJMN9VqicYRVQ4CFh4GkE2MZACSRE/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UxfuWGC2h883TnCYz8FJbVVia7ml9Fz8zanzNOicrK8EF00LNicSepKWKJUZyXIibe0saqkTwGyu5tSNVNHkX5Vpkw/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLelHF3vFd7fXVR2UbyXOWbrTjZddnjmSjAzFib81n43UgOtVIggWYQ1zLiaHaI2Gaia5wddsZq4EZmwPJib6ys1F7hvlia5lDh3aibWs/640?wx_fmt=gif&from=appmsg)

2. 前置知识

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLfOv910Sr6ZUhjmdJ3FnLZdicuibJNRtBsE2uicQpzVbCD13ozzArAxwI2ONmX2mhjBgmaOoZY7KD5w270TGArEGTP3Ly1bIEBZXY/640?wx_fmt=gif&from=appmsg)

常见利用场景：服务端从文件系统读取密钥，kid直接作为文件名拼接路径，未做过滤。

![](https://mmbiz.qpic.cn/mmbiz_gif/eDXiba58htLdvZ6G8YLAhXtV3Pcopusvd8JnDz8pvCCXqx4YfLYbzOV4ruj114kkFiaSUEZkgRJeDooZ2TTuTf7FIgQ0OPv0JlwTBFvOdIdro/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/UxfuWGC2h883TnCYz8FJbVVia7ml9Fz8zanzNOicrK8EF00LNicSepKWKJUZyXIibe0saqkTwGyu5tSNVNHkX5Vpkw/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/eDXiba58htLfSVCajWYIHOyWs1XX61rrIhcZ4JzhYH3VW1Zv3tlXZNzUQCibSQuZE2UytcbmCaB24Bct6v3HVZh5zdicJvhR2R4gtzrzicSGI0Q/640?wx_fmt=gif&from=appmsg)

3. 实战利用步骤

###

步骤 1

分析服务端密钥读取逻辑

通过接口测试、报错信息等方式，确认服务端的密钥读取逻辑：

* 若服务端返回`文件不存在`类报错，可确认`kid`用于拼接文件路径；
* 常见路径式：`/app/keys/{kid}.pem`、`/etc/jwt/keys/{kid}.key`等。

步骤 2

构造恶意kid字段

根据服务端路径格式，构造路径遍历 payload

常见 payload 如下：

+ 读取空文件（Linux 系统`/dev/null`，内容为空，可用于空密钥签名绕过）：`../dev/null。`
+ `读取系统静态文件（如``/etc/passwd`，用文件内容作为密钥签名）：`../etc/passwd。`
+ `路径深度适配：根据服务端路径层级调整``../`数量，如`../../../../dev/null`

构造的 JWT Header 如下：

```
```
{  "alg": "HS256",  "typ": "JWT",  "kid": "../dev/null"}
```
```

将上述 JSON 进行 Base64URL 编码，得到 JWT 的第一段。

步骤 3

篡改 Payload 并签名

1. 解码目标合法 JWT 的 Payload，修改权限字段，重新 Base64URL 编码得到第二段。
2. 用遍历到的文件内容作为密钥（如`/dev/n...