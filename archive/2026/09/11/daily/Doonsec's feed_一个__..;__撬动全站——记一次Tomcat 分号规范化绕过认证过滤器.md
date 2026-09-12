---
title: 一个\"..;\"撬动全站——记一次Tomcat 分号规范化绕过认证过滤器
url: https://mp.weixin.qq.com/s/dK9vecoZ9TxDgb8MB7gZfQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:44:03.664173
---

# 一个\"..;\"撬动全站——记一次Tomcat 分号规范化绕过认证过滤器

# 一个"..;"撬动全站——记一次Tomcat 分号规范化绕过认证过滤器

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

**千元稿费！还有保底奖励~（  https://bbs.zkaq.cn   **）****

# 一、侦察

某大学教师发展系统，依旧开局一个登录框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKpDzrafjDoeBibA1TL9CXbPjTm0tnvRWibA5QmGoleyedMerkibw1ODODXEBnnUxxXGEJue352lbcIrdAIO4nsia8L6U6akoocODA/640?wx_fmt=png&from=appmsg)

    看起来基本就是若依改，所以自然就是常规的弱口令、路径探测，但是事情自然是没那么容易的，因为系统存在全局认证过滤器。

    全局认证过滤器把所有未匹配路径 302 → `/redirect.jsp`（含不存在路径、Tomcat 原生 manager/status/druid/actuator 共 12 条探测路径全部同响应，无差异化信息）。响应面极干净，任何路径探测都拿不到东西，那么打法必须转向"过滤器本身"。

# 二、正文

过滤器绕过：8 变体序列，7 负 1 正

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJBXtIW99DKPBfiaR7sspKia7ibKm0qKYRk9khp0JHhX3cDSdn0IsQ7iazrricBdCUlr00ER2Txicut0c9aanCia2tS5EvDBYWOrRdvZ0/640?wx_fmt=png&from=appmsg)

    总共试了以上常规的八种，好在是过了一个，嗯，狗运还在。

然后针对 js 中找到接口测试了一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJMdTd6rFDibZGp1SzKJIjLERLBEdxzwGJAxMwEicfztXFPXHWab1IIHPM1gwclI2Lb4aMLymYiaqK38nWibcM9wP4ch6ic9ePWndPY/640?wx_fmt=png&from=appmsg)

200 {"msg":"用户不存在","success":false}    ← 服务端真的处理了请求

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI3nJFwAL6FmkccdHGSdu65WOE9aMqfPUjeqpib9uWqOiaU38o3S2muLU0splqA9K1fxV9rzxfrVAOfgrDVUVy0uOEulUzWicmVLE/640?wx_fmt=png&from=appmsg)

**\*\*根因\*\*：过滤器白名单含 `/我是路径/` 前缀；过滤器按\*\*原始 URI\*\* 前缀匹配放行，Tomcat 路由时把 `..;` 规范化为上级目录 → 实际到达受保护 servlet。\*\*"先匹配、后规范化"的顺序缺陷\*\*。**

也是成功进入后台了。

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIYghjWTnxbWthiaQCWTSleneiablJFskzR4br540fUlTntyAPgpdO4ZEBoYTQyAK0lM0CiaenAd8skdEesPk8ArE37HrTv3gTezk/640?wx_fmt=png&from=appmsg)

# 三、前台SQL注入

虽然已经进入后台了，但是既然绕过了认证过滤器，自然要试试有没有前台注入，狗运时刻又发力了，还真有，不过也是没那么简单。

大概有两点，第一，有缓存过滤器，相同的 SQL 短时间内不会执行第二次，第二，select 被禁了

整体的测试流程如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJT2Bwlyec6FywibqqlbFzmObjov06lnxrbvXjUdjY5eN4UY2N4CbjWmSYH4hUt79gsLyQcic2n05uOzPShu1qUO3NfJuVvwMicUk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJl46jsjCSRGR3sHRQVlp9tAH1BwWc2b3KXKFGibqZDa5XdWfZqu6hHPPjkJTK4jZpunGu5M9ps8t2dLT6KibhN50WEcicuT39ibLI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoK5pKVzPRjvNI8zDKA1bbianeAMg7tgsvJoiaqveKzsoH8wiciaEV3UTNJS43RL9UwrtJYyY3XpFc9xtnVfWJFGCickP3TYz8715x4Y/640?wx_fmt=png&from=appmsg)

这里有三个关键认知：①"无效值"和"布尔假"都落在\*\*空集态\*\*（`TBL\_NOTEXIST\_9` 与 `AND '1'='2` 同响应），而"报错"单独一类——三态分离证明响应差异来自 SQL 执行结果而非前端固定文案；②布尔位 = 空集态(0) vs 数据态(1)；③错误态是"payload 是否真的执行了"的探针

绕过

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKrL72OhEU4JBhTfnf0QMFqUQ3uRkjBoXNN6RUDak7Bw5IlXLLYKiagurwglBFbeqgQu7tme8hZM8UZTE5QibbQyshbQ8Vict6IG8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJiaPcrRdXbNiaQfWJ53qMjOVwd8tqTt376iaictr0EgCkyMMRN8wrGKozJQkArjsTXFa32qM2Ydic6UZCKym1ZA242bqPExIEC42VQ/640?wx_fmt=png&from=appmsg)

布尔盲注的注入位在 WHERE，被拦的是"**子查询表达式**"这个语法形态，不是"所有函数"。Oracle WHERE 里不依赖子查询的判定积木全是单 token 函数/伪列/字面量——不出现 `(SELECT`、不需要 FROM、不触碰 UNION：

' AND SUBSTR(USER,1,1)='E' AND 'a'='a 响应正常为真

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI24ia6L2XQqloytyibGT7smFqj44ic3tsCnbdkYsmE6o3yX6fza03TElnGYX5gxgMU3KWdt5uptm2trKIhGN1tCxMGbIAkxm4NKY/640?wx_fmt=png&from=appmsg)

' AND SUBSTR(USER,1,1)='e' AND 'a'='a 响应不正常为假

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL3D4CDUiaicSfGve8rAq4ErzdqtFsjQoOJ7cMeYQw4nc3u7JfTL0KNl0oibAXdIATulxibzPVnmcxyP3zWfvsB9omIbIDgW6Rd0Hg/640?wx_fmt=png&from=appmsg)

所以这样就能成功注出库名证明危害了。

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=34)

**没看够~？欢迎关注！**

**分享本文到朋友圈，可以凭截图找老师领取**

上千**教程+工具+交流群+靶场账号**哦

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=35)

**分享后扫码加我！**

**回顾往期内容**

[网络安全人员必考的几本证书！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247520349&idx=1&sn=41b1bcd357e4178ba478e164ae531626&chksm=fa6be92ccd1c603af2d9100348600db5ed5a2284e82fd2b370e00b1138731b3cac5f83a3a542&scene=21#wechat_redirect)

[文库｜内网神器cs4.0使用说明书](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247519540&idx=1&sn=e8246a12895a32b4fc2909a0874faac2&chksm=fa6bf445cd1c7d53a207200289fe15a8518cd1eb0cc18535222ea01ac51c3e22706f63f20251&scene=21#wechat_redirect)

[重生HW之感谢客服小姐姐带我进入内网遨游](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247549901&idx=1&sn=f7c9c17858ce86edf5679149cce9ae9a&scene=21#wechat_redirect)

[手把手教你CNVD漏洞挖掘 + 资产收集](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247542576&idx=1&sn=d9f419d7a632390d52591ec0a5f4ba01&token=74838194&lang=zh_CN&scene=21#wechat_redirect)

[【精选】SRC快速入门+上分小秘籍+实战指南](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247512593&idx=1&sn=24c8e51745added4f81aa1e337fc8a1a&chksm=fa6bcb60cd1c4276d9d21ebaa7cb4c0c8c562e54fe8742c87e62343c00a1283c9eb3ea1c67dc&scene=21#wechat_redirect)

## [代理池工具撰写 | 只有无尽的跳转，没有封禁的IP！](http://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247503462&idx=1&sn=0b696f0cabab0a046385599a1683dfb2&chksm=fa6bb717cd1c3e01afc0d6126ea141bb9a39bf3b4123462528d37fb00f74ea525b83e948bc80&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/BwqHlJ29vcqJvF3Qicdr3GR5xnNYic4wHWaCD3pqD9SSJ3YMhuahjm3anU6mlEJaepA8qOwm3C4GVIETQZT6uHGQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=36)

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