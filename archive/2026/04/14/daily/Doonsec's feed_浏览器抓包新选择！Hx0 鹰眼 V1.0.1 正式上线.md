---
title: 浏览器抓包新选择！Hx0 鹰眼 V1.0.1 正式上线
url: https://mp.weixin.qq.com/s/xBVAXULIKdJ_x7c8WEC5Sg
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:39:12.829588
---

# 浏览器抓包新选择！Hx0 鹰眼 V1.0.1 正式上线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rkE16nqDZNU7AN9VHOibxibMjicjQwpoc1ic4M0CCu7SoaHBaicdVKPQbpOnpUI7sgbibm61ypiaoibm2ldwlqmX0uMqNzvgibIFhpCibPeAkzvO9tVs0/0?wx_fmt=jpeg)

# 浏览器抓包新选择！Hx0 鹰眼 V1.0.1 正式上线

Hx0极客圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

鹰眼1.0.1-0414版更新日志：修复全部域名筛选异常；抓包列表支持列宽调节与持久化；优化302重定向抓包的去重；新增表头三态排序功能。

以下文章来源于Hx0战队
，作者asaotomo

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6DD0zVAtlbRibCymhumP4lrpWY1Hgr3GCqCQQU4JorEag/0)

**Hx0战队**
.

专业的网络安全服务团队，提供钓鱼演练、安全培训、渗透测试、漏洞扫描、风险评估、应急响应、HW支撑、等保咨询等安全服务。

大家好，作为一名WEB渗透测试工程师，日常安全测试是少不了的。

今天不聊虚的，直接给你们分享我最近在用的一个工具——Hx0 鹰眼V1.0.1 版。

项目地址：https://github.com/asaotomo/Hx0-HawkEye

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVPbGUGicjnA9qROrONfllGrpZx25hPkAJCEwWgbqcs3JdpT9tGc2znwib2qrTrOwmDyMQxjAXlA7kI2I1jfZqWnVgggPeukeAAg/640?wx_fmt=png&from=appmsg)

---

# 先说说我的痛点

不知道你们有没有这种感觉：

* 日常想看个XHR请求还得开代理、配证书...配置半小时，抓包5分钟
* 用Burp抓完包想重放测试，结果页面提示"登录失效"...又要重新登录
* 就想看个接口返回啥，地址栏旁边的小工具功能太弱，查个参数累死
* 做个简单测试要切换好几个工具：抓包→重放→解码→检测...烦

Hx0 鹰眼这个扩展，我用了段时间感觉挺香的，推荐给同路人。

---

# 它能干嘛？

一句话：在侧边栏里把抓包→筛选→看详情→重放→Fuzz→检测这些活全干了。

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVh583dDg3jNP6NoFTBFiaI24yLU8FPMMErVNQF5ia9A30jOsenicDdpVTaFFHdolmr9OYiaYHJrYibo4rgibmvdicecuyC0Ruicd4XSRY/640?wx_fmt=png&from=appmsg)

# 1. 抓包

* 直接劫持页面里的fetch/XHR，不用改系统代理

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNWWszSXiaDpchye4mu0cJ39UlygricX6t2mRogmNrTFyNnZbScPNWVxzu0SugZdTXDD4Dtxr5iaNQ37jwMQSJpylictaq2MbRtlF4I/640?wx_fmt=png&from=appmsg)

* 按域名/IP筛、按类型（XHR/Fetch/JSON/JS等）筛

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNV9zdjsq1Xg9sy1qeic5EdB55r85FVlqv12dH2GChTTicVInZwIJatUibTpuCiba3dMiaNccoVgOLAmFr9d1JiawoetUicMAxKicDDd5mM/640?wx_fmt=png&from=appmsg)

* 免证书、免配置，装完就能用

![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNWexzPcTy6LXicS2WtmNFMfoib2p5xYLwhdVXSJuic1bF1cPI7SuN1GgxSo7CuzFzLt0N7y1MicXtiaTTfhbFSgVCia8NdeQ7TGG3sxA/640?wx_fmt=png&from=appmsg)

# 2. 历史记录

* IndexedDB存着，实时记录插件抓取的数据包

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUxiavs3cE5rXJ2ZLbOqM5CdGZO07WOEDj46aIpRtL2iaNZicTVOE9wia2gjfj6Bto59wqVCA2h7UcQvIEmMqyDuTa5iaxLSlsaaKMY/640?wx_fmt=png&from=appmsg)
* 支持按域名、方法、状态码、关键词、敏感词、响应时间、数据包大小等进行数据包筛选

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWQtyaqcjKWVlvksdFJTVKr2dDNQ8uQIf48iboRWcayjaZD9VO19ksNTvaMCUIBFmQ21rFzdJeJ92MegpWVvLWRX3riaiaickcqibs0/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVNO4t8FiaRib5x7n2jX2pclXf37OZrNPDM5AdMuvSJXqKzQZSTnBpCgovDxYwlooMQpkTFogfWZDuVzBROibRsIQTU26nn7RvJsU/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXxgKGe8icCO4bF0EWBvgUJZVIwGb0QXwibCqKaY2l8ibiaicDceZibGNQTc0Rz2xsdFJPgwwiaCZWb9kd0hib44u7nswbOaO1TPXY8DaA/640?wx_fmt=png&from=appmsg)
* 插件默认显示当前页面数据包，当然也能看全部

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVcAKrxnDEmudfHjgMGXiawz4zibtLQjIGTzIsBrr0smHWEuYKjLFPwG1Xy8cjzpNnS6gCjV47qckSxSGmn3DfcbKLOJzXztWicqY/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVJf7NJ4a1frTHWcQib3pXFp9lvibvLiaDMTTys9KUhTmS0W8vZyNqdwZq3UjCSygMHuFnSj6Fo4SPOpWicqVzMpCXoYmnDhwj7doY/640?wx_fmt=png&from=appmsg)

# 3. 拦截改包

* 队列式暂停，可以在侧边栏里直接编辑、放行或丢弃
* 适合联调时改参数测边界![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNUpD2uXiaXH6tZia2tn45Yj1kW6VQGZRtCicZG0ewBSQohnibWaiajjhgBhDNm1Sic5quiav5qkIJvtomN5RDRgWmeM9iaiaIcubMpTBYuk/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUwrhu0p45Kf7ktnaiaHL86DqeFok7Butlib6Vmdr67pSe1OOicAia7gtvjVibYYHW0CL2ZeMIARcWRzHoPv8paFicPk2UzlGxonFEJM/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUyI2w0Iia6xFBhrwtjWlWibtYRuL581leaQRYageQeofJpMknys1JLGXXc92Nbp3h5sqzFSF3vria6bbtN0RSEyZ1r8iaEbqbGZQY/640?wx_fmt=png&from=appmsg)

# 4. 详情审计

* Pretty/Raw/Hex三种视图切换

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNX034y9pgAybqgOttA573vAcaJV0iaMn04maoNia2Jncc3eNGvZcPnLVvAo7WIzU12cybjY20ThfGcNBXF2zXq59USOmmyWrmlSY/640?wx_fmt=png&from=appmsg)
* 响应还能Render预览

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNV182HQHSMIRcwvtozzRctoxAzEL3RiaiaYp4Xep9LQRmuicWZWPsysicRh942ibj72dicxeQthECSx9mv7enDLiaf6Fnc3CuiarIbwy14/640?wx_fmt=png&from=appmsg)
* 敏感信息自动标红，点击请求标题能复制完整请求URL、点击响应标题下载请求和响应包原文![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNX1xdzicib63BhMMEX7mubibGaFPicbXWLZq77Sk0icF97UqZNDDhz2OMpDps4XKceiaZKHZy56uLRFNfMTLJbpWWOnObKFTfFZFd82I/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNUeXPX13lNCtoT8TjZ0BaXDookrJvIRTNwzfwmKZnohvtu4NLyTTjAbQaDkSBxcAAibOqqWZ2fKVKGVgXcHfuya18BdxPBOWic7M/640?wx_fmt=png&from=appmsg)

# 5. 重放工作台

* 编辑完报文直接重放

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXJy2JtxC4cJjZh3vnoFKMKplc0qmhAe1nQm1ADIxcu7EdAOD1Hiasx0S2aWhy9ON3v5iaeQ0XibseBUM88Q3SfPJicicq1ibKbRck4A/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWY88GsYGu6ZDzLuBIiaCooaXtyueTWpafkj9Hzba8l8LBIT2JGfgLibQzWE6dkx1pgWjbz2B2cfEJiadcKudmsQ6YBNibKnMTTvPQ/640?wx_fmt=png&from=appmsg)
* 支持"页面内重放"，有些WAF动态页也能过

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVlqmKDeo5qmLGVic00ZRAT9IIMu0PYa16YYGWeTibJjrQILiaClulRf3ialdMGVricOS7xXibjpRulLO0viapfHycyEIYicUFfljXPasU/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNWQhHPRNqtViblRyRpH8yybK2TkKqp4eSqhJ6V65hicRNAUzAQwUklukMmx7w35c4op5U8ibPibnbgZ84kVlDKPKC1bqC5oDrrxp4g/640?wx_fmt=png&from=appmsg)
* 还能让AI帮你生成测试用例

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVLmnRqmvFvKW3WCM2qGmkk9gWbI38jHF69mpTeu2pq7p2BAGGniaOyxZvZJ0KILd1wVB5pM6yYerZWsuGgjwUpmh09h4Y9gCeQ/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNUHo0PfDzdU5bU0mibZCMicUywt0icwfjcNoDk9ibYjzSS0y5yJqeBRjkl4EBZa6ibV8iaq870LFHg6Ot7GpW3YH90ahIWH7XDKMO6Ww/640?wx_fmt=png&from=appmsg)

# 6. 微型Fuzz

* 用§...§标记注入点就能跑

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNWSlTGJaRyU86ttYjShU15EcWwe7YttVGLSmQvyPc4FubQj5bwOxR5CozkzwtswSkxEicFzrzcibLic6UK6ZelvG7KGt3zBlsD8t8/640?wx_fmt=png&from=appmsg)
* AI还能自动生成智能Payload

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXnSIGMuO1xK9VCl3IdiauMHg2UrHc4zjLOiaSHPEfIj4EXKxzpxLOOq2kfjjYavX6JwxVyw1yuOkf6A5YqJDzRutyKC285XwPc0/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNUkaqpDic3dWo9kuibfOibUGqWibQCbNF9jZL0tTvK2ByO4IYUDo22ib9fjckbLXbWvOzs3YzImXLunOvnSh2ssE92j1iauwHIy2LBU8/640?wx_fmt=png&from=appmsg)

# 7. 暗链检测

* 对静态页面做规则扫描

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVzCGwfQKLibQJGN87K4MqbLVtt1WgLphH6gVicia4edTu0qLPx5KxGI8TeMxsZN6Oj6C1AzfqhTWNtribzf0QVxSmkyZicyJicxcYEQ/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXcib6C3JGN5vfWduUyYlKAjQUN6qznt0YOVhUApiaY2brjMiapLDGNAumeHJQtuWoVQ9Vm696F4RIPUlmMdehpqYBJ2jEpiaeWZOQ/640?wx_fmt=png&from=appmsg)
* 可以配置高信誉顶级域降噪

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNUzwlucSpGiaVxPhqIcnpMbGrd5HYCicWEULc3FklJKLeqibia4YHmXdcRLcPLKkbuAhExQSBPhMLkTpkSOKIFYKjtKQhVZysUu00o/640?wx_fmt=png&from=appmsg)
* 报告能导出

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNUK0AiaIBu4iavuhS0rlv2s2vpjIJDVyjJVCmZaj9CK1Y5qyfy1lskAFI4denM9icyXbggwyaa1BLDCriaF8Mjlf5LD4MAtQxdQYXk/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVvib9ibq6bV3RZ6lpiawS6o0iaFC9d0kLzM8Zuq301rWwxRzghvvh0eYqko3cGn7A9batsA9EFVIVm6icRvoHmodSWiaR9ZLbKTdyKo/640?wx_fmt=png&from=appmsg)

# 8. 编解码

* 基础的MD5、SHA、Base64、URL、Hex都有
* 专业的还有SHA-512、HMAC、JWT解析、时间戳转换

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNVCudTWb4OJ1ic7aGfs2XGq0HDhwy3KYnkd4lWib3MNqUMOnicVNfx1cCAqpCCTUGdPFK0GLvkOGHibM4Xpkp2gO0R2xlIdLZUUm5g/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNW6ehibIoX1aNlKxJaiaZ5PeugDIPfIXb4AOMvGy1xf3MSf1IAyyz2oMawUsbEn5dUvmGNsTERFibnvLIZLRNHnE7s8EES2dbh4hk/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/rkE16nqDZNXJQHyhdibRjLHSgZ1T3Wd1wFAYMSl4P414NicMdYLCZ7olSRzfWBJQsHtjTXsNVibMZpUgN633PlJOFogYLFYcGaqWKjGJM4Giao4/640?wx_fmt=png&from=appmsg)

  ![](https://mmbiz.qpic.cn/mmbiz_png/rkE16nqDZNVZDjZIfXeTOt9UrpVWK8icsBMQ7XzDib3Z3x823eDmrKrTBcwBgrMga7fiasgbOamg3qUzQDSQDocQQM0Iw67qhRhJvnfj93RzoU/640?wx_fmt=png&from=appmsg)

# 9. 敏感信息匹...