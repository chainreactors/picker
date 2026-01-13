---
title: 【安全圈】新型网络犯罪工具 ErrTraffic 实现 ClickFix 攻击自动化 伪造网站故障诱骗用户中招
url: https://mp.weixin.qq.com/s/fBsaqEzrb0-cnLUlrEVdzw
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:29:48.175455
---

# 【安全圈】新型网络犯罪工具 ErrTraffic 实现 ClickFix 攻击自动化 伪造网站故障诱骗用户中招

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jYa5DIkJSAjA3eZkjG3ujlVibsZPtmyjn5SjkTxFuafGQfeUhLGCpqAUg/0?wx_fmt=jpeg)

# 【安全圈】新型网络犯罪工具 ErrTraffic 实现 ClickFix 攻击自动化 伪造网站故障诱骗用户中招

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络犯罪工具

最近，一款名为 ErrTraffic 的新型网络犯罪工具可助力威胁组织实现 ClickFix 攻击的自动化操作，其原理是在已入侵的网站上生成 " 虚假故障 "，以此诱骗用户下载恶意载荷或执行恶意指令。

该工具宣称攻击转化率最高可达 60%，并能识别目标设备的系统类型，投放与之兼容的恶意载荷。

ClickFix 是一种社会工程学攻击手段，攻击者会编造看似合理的借口（如修复技术故障、验证用户身份等），诱骗目标在自身设备上执行危险命令。

自 2024 年起，这种攻击手段的使用率持续攀升，尤其是在今年，因其能够有效绕过常规安全防护措施，已被网络犯罪分子和有国家背景攻击组织广泛采用。

**ClickFix 攻击自动化实现方案**

据悉，ErrTraffic 是一款全新的网络犯罪工具，由一名化名 LenAI 的用户在俄语黑客论坛上首次推广。该工具本质上是一套自托管流量分发系统（TDS），专门用于部署 ClickFix 攻击诱饵，采用一次性付费模式，售价为 800 美元。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jYSIXFQ3tMQcSJDajQNus8rnNsMJ3BXTX0DYlWVAOVvEuvwy6AhLNPrg/640?wx_fmt=jpeg&from=appmsg)

黑客论坛上推广的恶意服务

安全研究人员对该平台开展了技术分析，发现其配备了操作便捷的控制面板，不仅提供多项配置选项，还支持查看攻击活动的实时数据。

攻击者需预先控制一个可接收受害者流量的网站——或已向某个合法网站植入恶意代码，随后通过嵌入一行 HTML 代码，即可将 ErrTraffic 集成到目标网站中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jY8rdKEm0iaHMIP5eBvIyibaltLpmjElrRz6nhCRtwS0Tg4icmGuD78ib3ww/640?wx_fmt=jpeg&from=appmsg)

主面板

对于不符合攻击条件的普通访客，网站的显示和功能完全正常；而一旦访问者的地理位置与操作系统指纹匹配预设条件，网站的文档对象模型（DOM）就会被篡改，呈现出各种视觉故障。

这些故障表现形式多样，包括文本乱码或无法识别、字体被替换为符号、伪造 Chrome 浏览器更新提示、系统字体缺失报错等。

网站 " 故障 " 的假象会营造出问题场景，进而诱导受害者按照提示采取 " 解决措施 "，例如安装浏览器更新、下载系统字体、在命令提示符中粘贴指定代码等。

一旦受害者执行相关操作，一段 PowerShell 恶意命令就会通过 JavaScript 代码自动复制到剪贴板。受害者运行该命令后，设备便会下载并执行恶意载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jY4EVicyx2kk62FJPhnxhYTsygibqib5C4jtkwtmLf8NPGLCcHb7tCW0KDA/640?wx_fmt=jpeg&from=appmsg)

ClickFix 交付机制在 ErrTraffic

安全研究员明确指出，该工具针对不同系统投放的恶意载荷各不相同：Windows 系统为 Lumma 和 Vidar 信息窃取器，安卓系统为 Cerberus 木马，macOS 系统为 AMOS（原子窃取器），Linux 系统则为未明确命名的后门程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgwhJF6ibC1GNiczyHBMOn0jYL0LMqiax0bYNKicl4Uta8ticYTaX935ib1OiaLdVoAceqnb9rywKR9cM8kw/640?wx_fmt=jpeg&from=appmsg)

定义每个操作系统的有效负载

ErrTraffic 的使用者可针对不同架构的目标设备自定义恶意载荷，并指定实施攻击的目标国家和地区。值得注意的是，工具内置了对独联体（CIS）国家的访问排除机制，这一特征或可暗示 ErrTraffic 开发者的地域背景。

在绝大多数情况下，攻击者会将窃取到的用户数据在暗网市场出售，或利用这些数据进一步入侵更多网站，再次植入 ErrTraffic 恶意脚本。

***END***

阅读推荐

[【安全圈】BreachForums论坛数据库32.4万个账户泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073661&idx=1&sn=47a2ea7b05c99c8d23e9b8e6fb8ab229&scene=21#wechat_redirect)

[【安全圈】Meta澄清Instagram“密码重置风暴”非发生数据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073661&idx=2&sn=23f8372e701cf483b7cf976c0b207268&scene=21#wechat_redirect)

[【安全圈】恶性 Chrome 扩展盗窃用户信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073661&idx=3&sn=b285a1738ee7ba582e9647f76afac35a&scene=21#wechat_redirect)

[【安全圈】2025年中国十大宕机事件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073647&idx=1&sn=16fab3921adf37bcd4042f3c44594ffc&scene=21#wechat_redirect)

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