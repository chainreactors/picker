---
title: 【安全圈】GitHub 上发现 Windows Wi-Fi 密码窃取恶意软件
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068120&idx=3&sn=a24961da5e35d85056d0ee9b767256d5&chksm=f36e7558c419fc4ed6acaac4039b5d7fe72cbd37cebf516199a466060e63df1ad3ea97bf190e&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-25
fetch_date: 2025-10-06T20:38:18.732300
---

# 【安全圈】GitHub 上发现 Windows Wi-Fi 密码窃取恶意软件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj2W21u1zFszjibSlH20IkofLcicLI6o1bjy3OZLcFShT28jlIKQFDeAOURDx2w3QBxQtu3CwrLo9sw/0?wx_fmt=jpeg)

# 【安全圈】GitHub 上发现 Windows Wi-Fi 密码窃取恶意软件

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![GitHub 上发现 Windows Wi-Fi 密码窃取恶意软件](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj2W21u1zFszjibSlH20IkofWBvBAXFw9exJSqwYEkfxicyOMrnA31g4nNTEmHvPwrdlB6eMia3v5onA/640?wx_fmt=jpeg&from=appmsg "GitHub 上发现 Windows Wi-Fi 密码窃取恶意软件")一个名为“Windows-WiFi-Password-Stealer”的 GitHub 存储库浮出水面，引起了网络安全专业人士的担忧。

该存储库由用户托管，提供了一个基于 Python 的脚本，能够从 Windows 系统中提取已保存的 WiFi 凭据并将其保存到文本文件中。

虽然该存储库声称用于教育目的，但其作为恶意工具的潜在滥用不容忽视。

## 窃取恶意软件详细信息

根据 X 上分享的 cyberundergroundfeed 帖子，该存储库包含以下关键文件：

* Password Stealer.py：执行凭证提取过程的主脚本。
* requirements.txt：运行脚本所需的 Python 依赖项列表。
* README.md：详细说明安装和使用说明的文档。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylj2W21u1zFszjibSlH20Ikof1Dt6AvT3XkmhGo7H7G7ZOtiapS2qR2LzT8zbOehLCwj0ZZySpQXjL8w/640?wx_fmt=png&from=appmsg)

该工具执行netsh wlan show profile合法的网络 shell 命令，以检索与系统关联的服务集标识符 (SSID) 列表。

对于每个 SSID，该工具都会运行netsh wlan export profile，生成包含配置详细信息的 XML 文件，包括纯文本的预共享密钥 (PSK)。

这些XML文件临时存储在系统的工作目录中，由Python脚本解析以隔离密码，随后被删除以逃避检测。

此方法利用 Windows 对 Wi-Fi 凭证的本机处理，这些凭证以加密格式存储在凭证管理器中。

该工具的简单性和开源特性降低了恶意使用的门槛。它用 Python 编写，需要的依赖项很少，可以使用 PyInstaller 转换为独立的可执行文件。

要使用该工具，需要指示用户安装以下依赖项：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylj2W21u1zFszjibSlH20IkofY2Qa7HDXKR1eCgzT1EyiahS8PpqzJpbACB0HQCEwQA5tFg93YSjeHrg/640?wx_fmt=png&from=appmsg)

此外，README 提供了使用 PyInstaller 将脚本转换为可执行文件的说明：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylj2W21u1zFszjibSlH20Ikofb9UMUeoFEgQymaM4jsoGkNTcp411HN0ZUBnePlBjdeuLyA4qNCOSng/640?wx_fmt=png&from=appmsg)

此功能简化了部署，使非技术用户更容易访问，并增加了其被滥用的可能性。GitHub 存储库提供了清晰的编译说明，即使是新手用户也可以生成针对特定攻击场景的负载。

在 GitHub 等平台上公开提供此类工具会带来重大风险。恶意行为者可以轻松重新利用代码来获取凭证，从而促进未经授权的网络访问或在受感染环境中进行横向移动。

组织还应强制对 Wi-Fi 访问进行多因素身份验证，并定期轮换 PSK，以减少凭证泄露的影响。

来源：https://cybersecuritynews.com/windows-wi-fi-password-stealer-github/

***END***

阅读推荐

[【安全圈】马斯克DOGE网站数据库存在漏洞，任何人可随意篡改内容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=1&sn=2aaad093096f88adba585911871847bd&scene=21#wechat_redirect)

[【安全圈】Atos旗下Eviden公司紧急发布安全公告：IDPKI解决方案曝出高危漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=2&sn=07ceda3a43b852c9147f82cc1ed039fa&scene=21#wechat_redirect)

[【安全圈】数据泄露警报拉响！2024 医疗行业成重灾区，远超金融行业](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=3&sn=feadbe596231da73575f5a1c17b7609a&scene=21#wechat_redirect)

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