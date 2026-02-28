---
title: 【安全圈】Python 热门 ORM 爆出 9.8 分致命漏洞，数据库或被完全读取
url: https://mp.weixin.qq.com/s/fwAFzntu5JAHFsZyffhSFQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:52:03.892295
---

# 【安全圈】Python 热门 ORM 爆出 9.8 分致命漏洞，数据库或被完全读取

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFTiaBnCdzXib5LV4LhtxGN2oawa0GiaCKNDWZJs3CqBrGIRKfCVVGb6ZBkumvwESWaRduJzqBzrXJibXTGCkliaA8KIn17bqLrLEbc/0?wx_fmt=jpeg)

# 【安全圈】Python 热门 ORM 爆出 9.8 分致命漏洞，数据库或被完全读取

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyHZicpicHphIKSvAczBhFfnMjY2Fo5VGN2xib8wStQ6ytmNqSMXVxMLocqcdQiaJ68pY2xficynQFC0vuzGdfPVibey1CUsKoya4Q37E/640?wx_fmt=png&from=appmsg)

近日，Python 异步 ORM 库 **ormar** 被披露存在一项严重安全漏洞，编号为 **CVE-2026-26198**，CVSS 评分高达 9.8 分。该漏洞影响版本 0.9.9 至 0.22.0，波及范围广泛。

漏洞核心问题出现在聚合函数 min() 与 max() 的实现逻辑中。开发者在构造 SQL 语句时，将用户可控的列名参数直接传入 sqlalchemy.text()，且未进行任何校验或过滤，从而形成典型的 SQL 注入风险。攻击者可通过构造恶意字段名，注入子查询语句，读取与当前模型无关的数据库表内容，实现未授权数据访问。

由于 ormar 在 FastAPI 及异步 Python 应用中使用广泛，且官方示例代码常允许用户选择聚合字段，若接口直接将前端参数传入 Model.objects.min() 或 max()，即可成为完整的 SQL 注入入口。该攻击在 SQLite、PostgreSQL、MySQL 等主流数据库后端均已验证可行。

研究指出，该问题自 2021 年 3 月 12 日引入（v0.9.9）后从未被修改，持续存在近四年。

目前维护者已在 0.23.0 版本中完成修复。建议开发者立即检查依赖版本，尽快升级，同时审计所有涉及动态字段传参的聚合接口，避免将用户输入直接用于 SQL 构造。

***END***

阅读推荐

[【安全圈】大疆扫地机被曝安全漏洞，6700台设备可被远程控制](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=1&sn=09a467e0d06230cc6b463f9ca34e345f&scene=21#wechat_redirect)

[【安全圈】黑客利用 Facebook 广告投放假 Windows 11 更新窃取信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=2&sn=3fc8df9b9feb952b9682755651f3f845&scene=21#wechat_redirect)

[【安全圈】全球零售巨头电商遭植入支付窃取器：PrestaShop 商城被“二次下单”攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=3&sn=e9647e8fcf5b6a5981e64ebca7f1d0ad&scene=21#wechat_redirect)

[【安全圈】黑客将 Pulsar RAT 藏进 PNG 图片：NPM 再现供应链投毒](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652074198&idx=4&sn=25f3b263eaade2e01f72a50d49279106&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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