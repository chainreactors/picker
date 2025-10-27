---
title: 【安全圈】速更新！GitLab发布更新修复CVSS满分漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064581&idx=1&sn=a8d25f47e9142354cddaccee15a9e264&chksm=f36e6705c419ee130f4d3f0e49710c74c10402ee7aa922bcf4c208d71d1956c64caa923497ee&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-22
fetch_date: 2025-10-06T18:25:52.739277
---

# 【安全圈】速更新！GitLab发布更新修复CVSS满分漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhAK7Fv8oWpNiaXrhevHW8p66B4E79VEKI8IQOczRDHeuoPSeQr3J9bhmdnSkiaTxwmj9NdXXRhVviaQ/0?wx_fmt=jpeg)

# 【安全圈】速更新！GitLab发布更新修复CVSS满分漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

GitLab

**一、 漏洞介绍**

GitLab发布社交媒体版（CE）及企业版（EE）的17.3.3、17.2.7、17.1.8、17.0.8、16.11.10版更新，其中修补CVSS风险程度达到满分（10分）的漏洞CVE-2024-45409，这项漏洞能用于绕过SAML身份验证机制，存在于Ruby SAML程序库组件Ruby-SAML，攻击者可在未经身份验证的情况下，利用漏洞访问已由身份验证提供者（IdP）签署的SAML文件，进而伪造SAML的回应。

这项漏洞发生的原因，在于Ruby-SAML无法正确验证SAML回应的签章，影响1.13.0至1.16.0版，以及12.2版以下的Ruby-SAML。对此，GitLab在公告中指出，IT人员应套用上述新版，或是手动将相依组件进行更新：omniauth-saml升级为2.2.1版、ruby-saml升级为1.17.0版，就能缓解漏洞带来的危险。

**二、 基本情况**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhAK7Fv8oWpNiaXrhevHW8p6Jia3Hwk33vItibB0nsEpsd5micxjKWtT0JVbG8C921hzSFw8j9ibXNoCAA/640?wx_fmt=jpeg)

GitLab是一个用于仓库管理系统的开源项目，其使用Git作为代码管理工具，可以通过Web界面访问公开或私人项目。SAML（Security Assertion Markup Language，安全断言标记语言）是一种基于XML的标准，用于在不同的安全域之间交换认证和授权数据，它被广泛应用于单点登录（SSO）解决方案。

**三、 漏洞描述**

GitLab中修复了一个SAML身份验证绕过漏洞（CVE-2024-45409），该漏洞的CVSS评分为10.0。

OmniAuth-SAML和Ruby-SAML库在GitLab中用于处理基于SAML的身份验证，由于这些库/工具无法正确验证SAML响应的签名，导致存在SAML身份验证绕过漏洞（CVE-2024-45409），威胁者可以制作恶意 SAML 响应从而绕过SAML身份验证并获得对GitLab实例的访问权限。

**四、 影响范围**

GitLab CE/EE 17.3.x < 17.3.3

GitLab CE/EE 17.2.x < 17.2.7

GitLab CE/EE 17.1.x < 17.1.8

GitLab CE/EE 17.0.x < 17.0.8

GitLab CE/EE 16.11.x < 16.11.10

OmniAuth-SAML和Ruby-SAML依赖项：

omniauth-saml <= 2.1.0

ruby-saml <= 1.12.2

1.13.0 <= ruby-saml <= 1.16.0

**五、 修复建议**

目前该漏洞已经修复，受影响用户可升级到以下版本：

GitLab CE/EE 17.3.x >= 17.3.3

GitLab CE/EE 17.2.x >= 17.2.7

GitLab CE/EE 17.1.x >= 17.1.8

GitLab CE/EE 17.0.x >= 17.0.8

GitLab CE/EE 16.11.x >= 16.11.10

或将OmniAuth-SAML和Ruby-SAML依赖项升级到以下修复版本：

omniauth-saml：升级到2.2.1、2.1.2、1.10.5或更高版本

ruby-saml：升级到1.17.0、1.12.3或更高版本

下载链接：

https://about.gitlab.com/

**六、临时缓解方案**

对所有用户启用GitLab双因素身份验证且不勾选SAML双因素绕过选项。

**七、 参考链接**

https://about.gitlab.com/releases/2024/09/17/patch-release-gitlab-17-3-3-released/

https://github.com/SAML-Toolkits/ruby-saml/security/advisories/GHSA-jw9c-mfg7-9rx2

https://github.com/omniauth/omniauth-saml/security/advisories/GHSA-cvp8-5r8g-fhvq

***END***

阅读推荐

[【安全圈】Meta、YouTube等巨头被曝长期监视未成年用户，牟利数十亿美元](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064540&idx=1&sn=99778e36ee612653f5f5f8b428c60f3c&chksm=f36e675cc419ee4a6c4e48b7bb46fd8008e622293d8a050c836508852dffc45d163a471a25fa&scene=21#wechat_redirect)

[【安全圈】洋葱路由(Tor)也并不是完全安全的 执法机构利用时序分析追溯特定用户](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064540&idx=2&sn=c868e30d049834e40d4f0075e151e954&chksm=f36e675cc419ee4adf60a1a660705f764d3e5c9fa1b0c8800579e1b863aa7432edfb3f20c28e&scene=21#wechat_redirect)

[【安全圈】黎巴嫩再发生爆炸事件，这次是对讲机](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064524&idx=1&sn=e19e457b99625444d2c6db745d8eecc1&chksm=f36e674cc419ee5af5719eb9602d03de297a482a04198bb5e857862378e7b482579b2e960c2f&scene=21#wechat_redirect)

[【安全圈】小米摄像头里惊现陌生男子说话!小米回应来了](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064483&idx=1&sn=a23aa7b778084750615f37c245eed619&chksm=f36e66a3c419efb560f8dca0735fa5afe955f8a8da16e00a89b8f7e96c77d5ef9781a249e6ec&scene=21#wechat_redirect)

[【安全圈】115 网盘回应故障：服务器遭遇恶意网络攻击，“终止服务”系谣言](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064483&idx=2&sn=59205321bd49a843db7e6335dac27647&chksm=f36e66a3c419efb5c75343945fa0943a8701784408de8eb6cbc1a8bfd08d966da277f8106b13&scene=21#wechat_redirect)

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