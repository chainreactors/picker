---
title: 从源代码到漏洞清单，全程零人工干预-未来已来
url: https://mp.weixin.qq.com/s/z1yssac_jL8kNwx3uSzSCw
source: Doonsec's feed
date: 2026-06-19
fetch_date: 2026-06-20T06:12:57.432364
---

# 从源代码到漏洞清单，全程零人工干预-未来已来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/daL72iawRK2lD1BWU5QAGKjUgW7YFYDUmvGT6FYKNm9EaXbktwLUeO79srduWL2XXicf45W5ch2wJMicr7XfUFaRY2m3G5TUPj8NESMsjU7ep8/0?wx_fmt=jpeg)

# 从源代码到漏洞清单，全程零人工干预-未来已来

YNsec
YNsec

YNsec安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

点击蓝字

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/daL72iawRK2nfOS8utoJnu0uoEflTNo9Qa5HlyBeIEXWtozMbjLlQzrtyB7KYZSRgdeHe9eDtumhvNEDyIaTOMtz6EkbVBA3gr7rNwqDiceJk/640?wx_fmt=gif&from=appmsg)

关注我们

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/daL72iawRK2mKS4QGRY6Omh2JZK3mqaOsguZ1zvYLmuxPj8PTaLyGZpg1mFyvhZ4YdvS2vZofUwGWC76HI5eaKdticecJdW91PmjAswDO3H9k/640?wx_fmt=gif&from=appmsg)

**01**

DianXing (点星)

这是什么

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2nhSYskxWPla7TWp00volbbxeRyOCCXpoa0rkEic3fsDord68LjFNiblfoeUK8zPX4vAgBgGJ8NUE3K2CYsNCnoxVVh8g36NA1ko/640?wx_fmt=png&from=appmsg)

端

午

点星是一套 端到端 AI 自动化代码安全审计系统。上传源代码，系统自主完成漏洞挖掘与验证，输出精准的结构化漏洞清单 — 全程零人工干预，仅需单次运行。

点星不是规则扫描器。 它不依赖正则匹配或已知 CVE 模式，而是通过 AI 对代码进行语义级理解，发现认证绕过、越权访问、业务逻辑缺陷等 传统 SAST 工具无法触及的深层漏洞。

在实测中，点星已展现出令团队自身都感到警惕的能力边界 — 它能够 自主挖掘零权限 RCE 漏洞并完成从发现到远程控制服务器的完整攻击链验证，全程无需任何人工干预。部分被发现的漏洞已在目标项目中存在数年，历经无数次传统扫描工具的检测却从未被触及。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2lPHq3WfahAql8XPC47nK0UzvTH9uTqtCFjOogibBc1tENwibZ4YpdfrMbe1AYNloLokeMsZKedpzlBxyZvDoGF0PMjB5gu6UG28/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2k09EfDCJw8aFRQTIs36V8kAdFHMVUPzVvGShJV1Gic2JsCOrx7iacdIR1iayfDlia0kKCETfxibsnbphASB7Xd0uFILdGjYotPg3eA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2k3ib6EpMJUvQ4RqYmgdElVs6nibibSA10sVn59COc880BibgLpKVaO8KcsGXrmiaNZIHKRnibibMII4B84oWXRibd8yESoBG4ewoTXJfE/640?wx_fmt=png&from=appmsg)

传统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2nwgSZTgCNCwaziaMZ3KJmZiboibhteEbeB3mibHEoKVo5OtgvPdSkgXibTMqSUKZIJ3sRmV0PvPCQ8wib4ejJSKIKu3ic5VGQlv7Znias/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/daL72iawRK2kEGZud2oGkmBNUohWoQAo9ZltBj07icI5NfY6ORmFaO0Uct55HVwS4qCgka1w3dfYLHeJrpicIzsXPF5Lic8BcQ5iaVKJPCPl7oiaY/640?wx_fmt=gif&from=appmsg)

02

为什么不公开技术实现

这种级别的自动化漏洞挖掘能力一旦被无门槛释放，后果不堪设想 — 它不再需要攻击者具备安全专业知识，任何人只需上传一份源代码，就能获得一份可直接用于攻击的高危漏洞清单。这不是假设性风险，而是我们已经在靶机上反复验证过的现实能力。

正如 Anthropic 因安全考量选择不公开 Mythos 模型的完整能力，而是通过 Project Glasswing 与全球机构合作定向防御 — 我们同样选择不公开核心实现，转而通过可验证的审计数据和公开挑战赛来建立信任。 能力越强大，释放越需要克制。

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2n7bxERoqxVlElTsy289nD3p4STt3be1UbkKKNwopdnjrX4aNgVm8DgsNniauX0ItdvW9JY3Lmshod1NndZnE9MIJPiaAfs4OGvg/640?wx_fmt=png&from=appmsg)

端

午

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2nv50XqhicxNZEkXzYzDQdp6UGklVnAWD1nG0mibwJxQtwz9HHn51dpYibRfC0TnAmtIWfDlLxWv7iaibohZ9at3ibTsl5ZD68JsBxnc/640?wx_fmt=png&from=appmsg)

**我们选择怎么做**

Dragon Boat Festival

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2m6DGXxj81PZJcX5c89ptTj5LtSnujozhC7DlvpEU8PdaE9vSwgJJvJ0icMBLpAWUMliaIF3nYib7Tib9I20AYjRTxLDknlJAtcNTU/640?wx_fmt=png&from=appmsg)

公开数据，封存实现。 以下所有数据均来自点星系统对真实开源项目的实际审计产出，可独立验证。

我们还发起了 ⚔️ 漏洞猎人挑战赛 — 提前公开漏洞哈希表，用真金白银悬赏遗漏，以最直接的方式接受社区检验。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2nG8bTn086fzm3VBvR2BwaMMKTjeaZ0IWxK847Ff3vJTcPtBeEUMd0BDib2FQiax3nQfEibicQaxrvCAQvibyxib2W9rdRDITrPrCHuo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2llwrf0hAiauroR3PG2TkV2QXIm87KPZDJFgBvynxEYj1pXFqsO9ZVNUZxqPThuAosopF9u6YWulUK5HRribnBf1IiaXeUiarQ9x8U/640?wx_fmt=png&from=appmsg)

端

午

漏洞猎人挑战赛

我们提前公开漏洞哈希表，用真金白银悬赏遗漏 — 如果你能找到我们没发现的高危漏洞，奖金归你。

我们对系统的深层漏洞发现能力有充分信心 — 现在，我们把这份信心放到台面上接受检验。如果有我们未发现的漏洞，我们同样欢迎 — 每一个遗漏都是推动产品能力继续深化的真实反馈。

🔄 挑战机制

1. 团队公开审计目标 — 每轮由团队公开一个已完成审计的开源项目
2. 漏洞哈希提前公开 — 审计完成后，每个漏洞描述分别计算 SHA-256 哈希，在挑战窗口开放前 提前发布至本仓库，利用 Git commit 的不可篡改时间戳作为存证
3. 开放挑战 — 哈希表发布后开放挑战窗口，任何人均可提交其发现的漏洞

漏洞描述原文 → SHA-256 → 0x7a3f...b2c1 → Git commit 存证（含时间戳）

提交方式

* 💬 公开提交：在本仓库 Discussion 区发帖（仅描述漏洞类型与影响，不含利用细节），仓库地址：https://github.com/tianchong-zerotemp/dianxing
* 🔒 私密提交：发送至 tianchong-zerotemp@foxmail.com（适用于不宜公开的漏洞）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2ldcyCBmscbdI5EGznpKZIWN2L9t4sIPZFTibXx7KIGanCFOsrJL018Vw9bkdUs7VqXAibiaC97d0jrNDdp5Hc5mjQrfEqrBwXaib8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2kgNJ2pkoDyO069Np05DlWOXT3HhsichpweaiccDoGA4Rw4j0mxMu0qsFu8ibx55piaQzicwLgHA8MXxAicg1fNoPvH5pA1iavSms6V2U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2lia3G5eJQwtBDNSwmIEHicjNy6hyZS81CBHcOCAYnicpiaF5B1BLM6b7BH7ypHCDLoicDBDb52cWhywBM6jeTDx8yNNaxTopJK7xYs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2kfWsRCTkhYlqUqV7PxU0hBL5n6aIefibrKeM2NBrmNyQYQicgCp7Y1C8Ekr9SzJib0piaEM8ssgNacoicvgOvllJLfMpQj9Dic4zSqA/640?wx_fmt=png&from=appmsg)

挑战规则

Dragon Boat Festival

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2kwx3awzbfao4iaaxZvAuztsZLOLpradv0S5iaGRMg3Qbf7bJBtVADda60FrrDkj1BtVxgSKCH3Gjara0mVRwtmatts5glpbCBxc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2mhPib6SEapD2RY8uVB24WrQaOmrkO9cQbdQ9Htn06ickgBckoqKf1thqBibEFkdj0EbFZiczIogaJic20560YnqhdQ6v1nFr0ggpMQ/640?wx_fmt=png&from=appmsg)

端

午

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2m2I9pazmZAEZHT30icrvgfuBic8xDs4hfNYEJk9Twwz6M8pnzWYXKPkVcutspJfIqDvmxsJ24j2rPHthiavTgiaZ1hHEX9ia3Pp7oI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2nBicLqVghYXBlD8j6rXXIoXOCyQJ94uMczR73agSnR3F55GMjAdJzKjU3AA5t8xxY1a0MXqedxLZhPuUUiaH7KLaM73Qv2hoTTg/640?wx_fmt=png&from=appmsg)

匹配判定与奖励

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2ldkNXFEkLIAT7icoSnGHY0OspEAdia9Pg25otEAFcYUDOrj1VBvy7JlCtrNgAAceSibZcVS8IKOCCibWWhvOTxofln9f8nrbicdlI4/640?wx_fmt=png&from=appmsg)

端

午

点星是 漏洞审计工具，其产出为独立的漏洞点位发现（代码缺陷定位），而非完整的利用链组装。利用链编排属于万破平台的另一条产品线。因此匹配判定分为三级：

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2mej6mLqGWvAPfuVTWEiakUdaunLpibic7mNZ4tkRhWibONoSwl9wJXVqKN15s1aDLGRiaJ9cprgbyOTwTqWiclDicVfLRoEZwkwUuJlA/640?wx_fmt=png&from=appmsg)

为什么区分"组件覆盖"与"完全未覆盖"？ 一个漏洞利用链通常由多个独立的代码缺陷串联而成。审计工具的职责是发现每一个缺陷点位 — 如果利用链中的各组件均已被独立覆盖，说明审计能力完整，只是利用链组合（攻击编排）属于不同的安全能力域

完整赛制详见https://github.com/tianchong-zerotemp/dianxing/blob/main/CHALLENGE.md

Dragon Boat Festival

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2lneO0tSR00hYfEHHXhQGV2mVvZYibqhLIwxsCI1Jo5Il5rCD1uFJXgkjk9kuaAJiaITZRx7Q35YScRdQPXV8CCPW7da77icRljug/640?wx_fmt=png&from=appmsg)

后续点星正式版发布，本公众号将同步送出邀请码和积分，届时欢迎在后台私信关键词“联系方式”获取邀请码

本次漏洞赏金赛采用奖池累减制，第一位提交并验证成功的师傅将独揽奖池的三分之一，祝各位师傅在这端午佳节收获满满

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2kwFSyzcuzh6ibgCGKrHM1c9ITNHpGm740R5dPZdrNOtDlSpvlO1e8DLsqiaF6ulTsCOvWjiaMhbq1mBJM8SL8GtZcLqaCxZBjuq4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/daL72iawRK2lHFbBw7OWBEtxhraviaJ65C1BTHZNZkJYSCbTcdmBb0HnYeIYN9OcvXH3Pph8a74kU6kwNw0rFEho4eUA3K9d19tYia5CmVUTPE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2lCFwKibEyZU82xgaJ7sVE8NOdMV27yBKEr4rcmBNKTUeVtnN6c6Kic2iatUUGXKgXc7UmNhcLhnFCTv2m5oUmPL4DzhgNTViampwA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2mwDmRk6JIRy1tdHhxiauBXXHp3icgxInC5D0H5dg8IVwX6T1PMibYibkIscm7v5XTelTRr6nxqe0teib44RLiawKcGwgcnNElooayCU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2nn6FuI8ia3FRft8icREHWtiasMC9tpplfCh6ME7qGsI46GhPJuVtCibZNcXfF0TYwibXs1RyGPZGI3yg2hpLpAy3u2mKAmicTQWY4ZU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/daL72iawRK2mu50pib8s7AOT3iaYmyNejrfSbOowib4TxY0icIdsU4e528oMic8iaC1sKwR8E7nl6cWMCbve6qrrpmh4RwPVkBcOwfSZ5f3BSbWw90/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Uzia3lCRCbBE6FMtLakKgM9ReNq8A01Y9HQrR8gdAU0d4FicFanlUibllvBxX3Ufq0PaLO1ibHZ9uRJbYlicCVkNQFA/0?wx_fmt=png)

YNsec安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Uzia3lCRCbBE6FMtLakKgM9ReNq8A01Y9HQrR8gdAU0d4FicFanlUibllvBxX3Ufq0PaLO1ibHZ9uRJbYlicCVkNQFA/0?wx_fmt=png)

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