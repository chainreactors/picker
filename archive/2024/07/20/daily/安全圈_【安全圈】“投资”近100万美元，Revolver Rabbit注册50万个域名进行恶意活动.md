---
title: 【安全圈】“投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062936&idx=3&sn=4301647b64ec19cc712ca69b2ebe81df&chksm=f36e6898c419e18e386cd662e50c792e695ac6ab8028fc77e5016b88383dfd4bdf26dd9789e4&scene=58&subscene=0#rd
source: 安全圈
date: 2024-07-20
fetch_date: 2025-10-06T17:43:50.947728
---

# 【安全圈】“投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiaGRoeRYguZSAKjtJu64uTzInmvTQ9DxOMiacKcoylx9QhDauA4FUDqeg/0?wx_fmt=jpeg)

# 【安全圈】“投资”近100万美元，Revolver Rabbit注册50万个域名进行恶意活动

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

恶意攻击

近日，专注于 DNS 的安全厂商 Infoblox 的研究人员发现，一个名为 Revolver Rabbit 的网络犯罪团伙注册了 50 多万个域名，通过散布一种叫 XLoader（Formbook 的后继者）的信息窃取恶意软件，收集 Windows 和 macOS 系统的敏感信息或对其执行恶意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylg6026oDdia0zibXxlXXXtaeiaag8MFDJRlGMpW8Dbf45yxxvia7yx73NsMVARteebYvUaOAcCI8k8MJA/640?wx_fmt=jpeg&from=appmsg)为了以如此大的规模开展行动，该威胁行为者依赖于注册域名生成算法（RDGAs），这是一种可以在瞬间注册多个域名的自动化方法。RDGAs 类似于恶意软件中的域名注册算法 (DGAs)，网络犯罪分子利用这种算法创建潜在的指挥与控制 (C2) 通信目的地列表。

两者之间的一个区别是，DGAs 嵌入在恶意软件中，只有部分生成的域名会被注册，而 RDGAs 则保留在威胁行为者手中，所有域名都会被注册。

研究人员可以通过分析 DGAs 并对其进行逆向工程，以了解潜在的 C2 域名，但 RDGAs 是保密的，这就让找到生成要注册域名的模式变得更具挑战性。

Infoblox 称，Revolver Rabbit 控制着 50 多万个 .BOND 顶级域名，这些域名被用来为恶意软件创建诱饵和实时 C2 服务器。考虑到一个 .BOND 域名的价格约为 2 美元，Revolver Rabbit 在其 XLoader 业务上的 “投资 ”接近 100 万美元，这还不包括过去在其他顶级域名上购买的域名。

Infoblox 表示："这种威胁行为者最常用的 RDGAs 模式是一系列一个或多个字典单词，后面跟着一个五位数的数字，每个单词或数字之间用破折号隔开。”

这些域名通常很容易阅读，似乎专注一个特定的主题或地区，显示出广泛的多样性，示例如下：

* usa-online-degree-29o[.]bond
* bra-portable-air-conditioner-9o[.]bond
* uk-river-cruises-8n[.]bond
* ai-courses-17621[.]bond
* app-software-development-training-52686[.]bond
* assisted-living-11607[.]bond
* online-jobs-42681[.]bond
* perfumes-76753[.]bond
* security-surveillance-cameras-42345[.]bond
* yoga-classes-35904[.]bond

研究人员说，“最近几个月的跟踪，他们发现 Revolver Rabbit RDGAs 和一些已知的恶意软件有联系，这凸显了 RDGAs 作为威胁行为者工具箱中的一种技术的重要性”。

Infoblox 追踪 Revolver Rabbit 已近一年，但直到最近才弄清楚他们的真实面目。虽然过去也观察到过类似的活动，但没有意识到它们背后有这么大的操作。

参考来源：https://www.bleepingcomputer.com/news/security/revolver-rabbit-gang-registers-500-000-domains-for-malware-campaigns/

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmkkAPfB37l9kuvJwPeIj3M2HPo6EqUv8YiaxAez2icXYq3tZkq3u65IlQ/640?wx_fmt=jpeg)[【安全圈】Cisco 再曝超严重漏洞，黑客可修改管理员密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062916&idx=1&sn=2f7a7da6edfcb8aa7c22e2e6f2afc7c9&chksm=f36e6884c419e192ad50833230d55041291038463f39103ea2f958c640b7db02eb183e9445bc&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmibB3GD6iaNBbs0L0OA2X1H5BibicFPCnLbkcSibESZczEdcKfhM7ia7oibibaA/640?wx_fmt=jpeg)[【安全圈】FIN7 黑客组织在暗网上大肆推广反EDR系统工具](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062916&idx=2&sn=36112144daca3fc114f4a8dac895382e&chksm=f36e6884c419e192a0efa7723cfec1d9a23f0bc0cb68c9b7377e28bbca147c1a879ab4fc77aa&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmzFL32jQmbjYal3cpaopjjqN4NUJ8OibpoiaKN3EpcCJY9Wo9pRXUTSnw/640?wx_fmt=png)[【安全圈】新加坡要求银行三个月内淘汰一次性密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062916&idx=3&sn=d0f3cfef85f8e2ac1b5c07812f9c3b45&chksm=f36e6884c419e192fb33660afb03e17311e3b54a818d01cd27ec0ede526c9658ad21787b9c69&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhEa6M1AIDFKXVZYkvibHolmA51qtiaeTciahSlHAuBunhsFO8YLZriboDPG7icn7OeZzkJxkgk4iavFnicw/640?wx_fmt=jpeg)[【安全圈】科技巨头被曝未经授权用 YouTube 内容训练 AI，苹果、英伟达在列](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652062916&idx=4&sn=320b04e041e86a1907c39453a528416f&chksm=f36e6884c419e19281c3f04e7415caf77720532af8701028529d05e35bfff68e8590378b3932&scene=21#wechat_redirect)

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