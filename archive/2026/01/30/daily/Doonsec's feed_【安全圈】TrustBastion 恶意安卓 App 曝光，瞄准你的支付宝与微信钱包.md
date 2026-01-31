---
title: 【安全圈】TrustBastion 恶意安卓 App 曝光，瞄准你的支付宝与微信钱包
url: https://mp.weixin.qq.com/s/Vh0ANE6Ya9ZWrFow17qxXQ
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:02:20.676397
---

# 【安全圈】TrustBastion 恶意安卓 App 曝光，瞄准你的支付宝与微信钱包

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48U2CgkzibTf8Z1etX7fQGibRBANw7AaRiauZdVG4Yx8RPEoYmP1ibribnJibg/0?wx_fmt=jpeg)

# 【安全圈】TrustBastion 恶意安卓 App 曝光，瞄准你的支付宝与微信钱包

安全圈

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

网络安全公司 Bitdefender 昨日（1 月 29 日）发布博文，**报道称有黑客利用 Hugging Face 分发安卓恶意软件，窃取用户的支付宝、微信等金融凭证。**

注：Hugging Face 是全球知名的开源社区和平台，供开发者托管、共享和协作开发人工智能模型、数据集和演示应用，可以视为 AI 界的 "GitHub" 或 " 应用商店 "。由于其信誉度高，常被安全软件列为白名单。

本次攻击主要针对安卓用户，通过恐吓式广告，谎称用户设备已感染病毒，诱导其下载名为 "TrustBastion" 的诱饵应用。

用户安装后，TrustBastion 会立即弹出一个伪装成 Google Play 风格的强制更新提示。实际上，该应用并不直接包含恶意代码，而是连接服务器，将用户重定向至 Hugging Face 的数据集仓库，下载真正的恶意 APK 载荷。

TrustBastion 为了对抗杀毒软件，采用了复杂的 " 服务端多态性 " 技术，每隔 15 分钟就会自动生成一个新的载荷变种，改变代码特征以逃避特征码扫描。

调查显示，涉事仓库在短短 29 天内就提交了超过 6000 次代码更新。即便原始仓库被封禁，攻击者也迅速更名为 "Premium Club"，更换图标后继续利用相同代码作恶。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48WeXWRwo8OAJcqoCvoXdNMD2fUmiapNhicsYMmKZojX15umqOicCAk4tHQ/640?wx_fmt=jpeg&from=appmsg)

恶意载荷一旦植入，便会以 " 安全需要 " 为由，强行请求安卓系统的 " 辅助功能服务 "（Accessibility Services）。获得该权限后，恶意软件即可完全接管手机：它不仅能监控屏幕内容、执行滑动操作，还能阻止用户卸载该应用。更危险的是，它会全天候连接命令与控制服务器（C2），实时上传窃取的数据。

该恶意软件的核心目标是金融盗窃。它通过监控用户活动，在用户打开支付宝、微信等金融应用时，覆盖一层伪造的登录界面，诱骗用户输入账号密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI48cfJXSGKWib5RRp6AbllGAbNeJ5meUfTYXMUdZhiaS1O4icTC0ribpssgUg/640?wx_fmt=jpeg&from=appmsg)

此外，它还会尝试窃取手机的锁屏 PIN 码。Bitdefender 目前已向 Hugging Face 通报了相关情况，恶意数据集已被移除，但专家建议用户切勿通过第三方渠道下载应用，并需警惕应用索取的不合理权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljgSmB9m0MJslT2lQTzcI482Y5Op2xIqk2SyicTYqznQRQRicibrLZJ51KL3kWzeqQYh5dFoibSnqObicw/640?wx_fmt=jpeg&from=appmsg)

***END***

阅读推荐

[【安全圈】抖音崩了](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=1&sn=b745a686b245684c9bdd345d1b77afb8&scene=21#wechat_redirect)

[【安全圈】恶意 VS Code 扩展"ClawdBot Agent"伪装AI助手传播木马](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=2&sn=3ed01239d8e66b938f373a2a52c32bc0&scene=21#wechat_redirect)

[【安全圈】PyTorch "安全"模式被严重RCE漏洞攻破，可执行任意代码](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=3&sn=ad2665e9be5ec05d1f5f1bcdabcfa2d4&scene=21#wechat_redirect)

[【安全圈】Chrome 发布安全更新，修复后台 Fetch API 漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652073915&idx=4&sn=cc70511df2d49f4ff6dd41538bf3b02a&scene=21#wechat_redirect)

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