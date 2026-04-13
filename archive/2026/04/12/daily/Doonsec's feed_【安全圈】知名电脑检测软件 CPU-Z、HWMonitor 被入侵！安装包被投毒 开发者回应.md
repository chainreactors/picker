---
title: 【安全圈】知名电脑检测软件 CPU-Z、HWMonitor 被入侵！安装包被投毒 开发者回应
url: https://mp.weixin.qq.com/s/ZAXh0SjfS5dPMYM1Z7aiYw
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:54:46.837470
---

# 【安全圈】知名电脑检测软件 CPU-Z、HWMonitor 被入侵！安装包被投毒 开发者回应

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyESstgJPXReJAK3ZzFoCgB0ESD76YVOwYkng82tJms9gLCVRIoV9WQRh0OYHA0UcwMpDFhrd1rsvWnz8aQ3pmibTgicrclzcQXMg/0?wx_fmt=jpeg)

# 【安全圈】知名电脑检测软件 CPU-Z、HWMonitor 被入侵！安装包被投毒 开发者回应

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意木马

玩 PC 硬件的人，几乎没人不用 CPU-Z 和 HWMonitor。这两款装机、测硬件必开的软件，近日曝出了严重的安全事故。官方网站的下载链接被黑客篡改，安装包被植入了恶意木马。

这次入侵发生在 2026 年 4 月 9 日到 10 日之间，整个过程只持续了大约 6 个小时。

这两款工具都出自法国 CPUID 公司。这家公司专做系统工具，旗下的 CPU-Z 能精准读取处理器、主板、内存的全项参数，HWMonitor 能实时监控硬件温度、电压、功耗，是全球 PC 玩家公认的刚需工具。

CPUID 开发者 SamuelDemeulemeester 对外说明，问题出在网站的一个外部 API 被黑客攻破。黑客篡改了官网的下载链接，把 HWMonitor 1.63 版本、CPU-Z 2.19 版本的官方下载地址，换成了非官方的 Cloudflare R2 云存储路径。用户点击下载，拿到的就是被黑客 " 加料 " 的恶意安装包。目前官方已经完成网站修复，也向所有用户公开致歉。

后续调查确认，被篡改的安装包里，捆绑了恶意的 CRYPTBASE.dll 文件。这个文件原本是 Windows 系统自带的合法库文件，被黑客直接替换成了木马载体。

用户只要运行了这个被篡改的 .exe 安装程序，恶意 DLL 就会自动下载完整的木马程序，注入用户的电脑系统。木马激活后，会直接窃取用户浏览器里保存的浏览记录、账号密码、Cookie 等敏感信息，极易造成用户账号被盗、财产损失。

虽然整个劫持过程只有 6 个小时，官方也已完成修复，安全机构还是给出了明确提醒。如果用户在 4 月 9 日到 10 日的涉事时段里，下载过上述两个版本的软件，一定要立刻用杀毒软件对相关文件做全盘扫描。同时建议用户尽快修改浏览器里保存的各类平台账号密码，把安全风险降到最低。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyF5AKUxmQbicZRAfyVwqAsgWGFR0K6G9EepWTm7crTb4ibgvkhSuKITahXYzFUULicq8BWfmFUoSZXwHPUeZNFmDkI3GZ4ibaWt7dE/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

[【安全圈】久病成黑客？男子自学编程，与妻子合作“代抢”医院号源，涉案金额超57万元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075546&idx=1&sn=9a045324f1ff78774756b8efb57efde4&scene=21#wechat_redirect)

[【安全圈】加密货币 ATM 巨头 Bitcoin Depot 遭黑客入侵，损失 366 万美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075546&idx=2&sn=8876814d45a7894a0eec1623c4593149&scene=21#wechat_redirect)

[【安全圈】欧洲铁路公司 Eurail 数据泄露，30 万人受影响](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075546&idx=3&sn=d3863852a3157fbc5b9a5430b0b66768&scene=21#wechat_redirect)

[【安全圈】老板倒卖26万条客户信息获利600万](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075510&idx=1&sn=b41c183cb3e61e1068a583217c6e8b2d&scene=21#wechat_redirect)

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