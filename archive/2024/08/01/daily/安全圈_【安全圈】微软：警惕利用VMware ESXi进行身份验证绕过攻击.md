---
title: 【安全圈】微软：警惕利用VMware ESXi进行身份验证绕过攻击
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063225&idx=2&sn=b3c27fd599e28e32fff5e9e88252e853&chksm=f36e69b9c419e0af291869b8a0c139316b54de8a2a445e7382162ff75fe586135ef60489111f&scene=58&subscene=0#rd
source: 安全圈
date: 2024-08-01
fetch_date: 2025-10-06T18:05:05.506050
---

# 【安全圈】微软：警惕利用VMware ESXi进行身份验证绕过攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliakke3Sicz40hwdQH3Ip9FUc6R5SBw9KW11iaLwGB3CMjya9YDCHxKCXShabOFIFNUrZdxaLLIZjwkA/0?wx_fmt=jpeg)

# 【安全圈】微软：警惕利用VMware ESXi进行身份验证绕过攻击

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

勒索软件

微软于7月29日发布警告，称勒索软件团伙正在积极利用 VMware ESXi 身份验证绕过漏洞进行攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliakke3Sicz40hwdQH3Ip9FUciaItD4IWA4DxKZ4iawXZ9wf5fysFoDPskgjIADdym3ic7lWn1qNt1iao7w/640?wx_fmt=jpeg&from=appmsg)

该漏洞被追踪为 CVE-2024-37085，由微软安全研究人员 Edan Zwick、Danielle Kuznets Nohi 和 Meitar Pinto 发现，并在 6 月 25 日发布的 ESXi 8.0 U3 更新中进行了修复。

研究称，该漏洞能让攻击者将新用户添加到由他们创建的“ESX 管理员”组中，并自动获得对 ESXi 虚拟机监控程序的完全管理权限。

虽然成功实施攻击需要对目标设备和用户交互具有高权限，但微软表示，已有几个勒索软件团伙利用漏洞完全掌控了管理员权限，窃取存储在托管虚拟机上的敏感数据，在受害者的网络中横向移动，并加密 ESXi 虚拟机管理程序的文件系统。

微软已确定至少三种可用于利用 CVE-2024-37085 漏洞的策略，包括：

* 将“ESX Admins”组添加到域并添加用户。
* 将域中的任何组重命名为“ESX Admins”，并将用户添加到组或使用现有组成员。
* ESXi 虚拟机管理程序特权刷新（为其他组分配管理员权限不会将其从“ESX 管理员”组中移除）。

到目前为止，该漏洞已被被追踪为 Storm-0506、Storm-1175、Octo Tempest 和 Manatee Tempest 的勒索软件运营商在野外利用，并在攻击中部署了Akira和Black Basta勒索软件。例如，Storm-0506 在利用 CVE-2024-37085 漏洞提升权限后，在一家北美工程公司的 ESXi 虚拟机管理程序上部署了 Black Basta 勒索软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliakke3Sicz40hwdQH3Ip9FUcDsZyibWCB0Ee3yHC1uS1EJCbBbZZGAkapsk6dcNLxuFsZs46YNeUdsA/640?wx_fmt=jpeg&from=appmsg)以Storm-0506为例的ESXi 攻击链

由于 ESXi 虚拟机 （VM） 具有高效的资源处理能力，目前已有许多企业开始使用该产品来托管关键应用程序和存储，这也导致针对企业组织的 ESXi 虚拟机管理程序的攻击趋势越来越明显。微软警告称，在过去三年中，针对 ESXi 虚拟机管理程序并对其造成影响的微软事件响应（Microsoft IR）事件数量增加了一倍多。

攻击者一旦攻破虚拟机，不仅可以对企业正常业务开展造成巨大破环，还能将存储在虚拟机管理程序上的文件和备份进行加密，从而严重限制企业恢复数据的能力。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzMpiawrG56u6yj3PM65KQDxYPoRp9dibODE5XJubgM8ibhNTuOGEXtuodA/640?wx_fmt=jpeg)[【安全圈】五男子使用“AI换脸”技术破解平台认证篡改系统数据牟取暴利被判刑](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=1&sn=41e4599574d805efa935881e461bbd5f&chksm=f36e69a7c419e0b1f87b23bba461c5353d6cb89b17dd55a3a49a799451ace1753eedc1300520&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzianBW3hxpjIFQch2g2L0lgJJabFXq6EmYIcUjnzdLzM5WFufcOAFmuA/640?wx_fmt=png)[【安全圈】Chrome漏洞致1500万Windows用户密码丢失！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=2&sn=790e8e8c9ee504d963cf86d34278d612&chksm=f36e69a7c419e0b1b7ed716da65cb03c6b7660637b8ba41dc8874cf578159d9ed7294a7d9d5e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzdNkWZN1NzkKfhIl0yInnPaCwXFUvlWCTmIhbHs400xRvCEDgIhH71w/640?wx_fmt=jpeg)[【安全圈】防不胜防：黑客可利用 AI 通过 HDMI 线远程窃取屏幕信息](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=3&sn=778a5a174d446786aff7e6f1ba6d31d3&chksm=f36e69a7c419e0b15f39843961a43d4bf2afb964368adfb789068814bb214f5c9c04de2e0bda&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgTTuYibxDr5sTw6UZTOEkmzQhfTTiawhJHxicXB2RwjiakURH6L3Rlt4h58lDLicJUxugoLaVSTXjHDnQ/640?wx_fmt=png)[【安全圈】黑客攻击 HFS 服务器以投放恶意软件和 Monero 矿工](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063207&idx=4&sn=22e9ea970a9deefd91fd06ebe5efca00&chksm=f36e69a7c419e0b1172ae40c23acd17b4dbbbd2b00b6064452063ba627d8893008a7827e88a2&scene=21#wechat_redirect)

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