---
title: 【安全圈】VPN正在成为企业入侵的关键路径
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066249&idx=1&sn=c8eb4e218d2e6d7fd61aac243bb505d9&chksm=f36e7d89c419f49f7b61e6ea42f88847733c94ea11650af312cec6742f9eb93c97c96aa15dd7&scene=58&subscene=0#rd
source: 安全圈
date: 2024-11-28
fetch_date: 2025-10-06T19:20:33.563549
---

# 【安全圈】VPN正在成为企业入侵的关键路径

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhqDPOFswIOmibtyefhG5bOOaztGia45gfiaUhNKTVHBvdn6TBQ2KVuMfJVI3ZEib3e0L1rlygrjSsChA/0?wx_fmt=jpeg)

# 【安全圈】VPN正在成为企业入侵的关键路径

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

安全漏洞

研究人员发现了Palo Alto Networks（CVE-2024-5921）和SonicWall（CVE-2024-29014）企业VPN客户端更新过程中的漏洞，这些漏洞可能被利用来远程执行代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhqDPOFswIOmibtyefhG5bOOUibU1FEPz3ABB8lDECjribnbrQD96RbdMHXkEg3vRfiagiaCqpSk9ibG5sg/640?wx_fmt=jpeg&from=appmsg)

## CVE-2024-5921

CVE-2024-5921影响Palo Alto的GlobalProtect App在Windows、macOS和Linux上的多个版本，起因是认证验证不足。

该公司确认，这使得攻击者能够将GlobalProtect应用连接到任意服务器，并且指出这可能导致攻击者在终端安装恶意根证书，随后安装由这些证书签名的恶意软件。

AmberWolf研究人员Richard Warren和David Cash解释说：“GlobalProtect VPN客户端的Windows和macOS版本都容易受到远程代码执行（RCE）和权限提升的影响，这是通过自动更新机制实现的。虽然更新过程要求MSI文件必须签名，但攻击者可以利用PanGPS服务安装一个恶意信任的根证书，从而实现RCE和权限提升。更新执行时具有服务组件的权限级别（Windows上的SYSTEM和macOS上的root）。”

“默认情况下，用户可以在VPN客户端的用户界面组件（PanGPA）中指定任意端点。这种行为可以被利用于社交工程攻击中，攻击者诱骗用户连接到恶意VPN服务器。这些服务器可以捕获登录凭证，并通过恶意客户端更新破坏系统。”

Palo Alto表示：“这个问题在GlobalProtect应用6.2.6及所有后续的6.2版本中已修复。”该公司还引入了一个额外的配置参数（FULLCHAINCERTVERIFY），应该启用以加强对系统信任证书库的证书验证。

根据PAN的安全咨询，目前还没有针对macOS或Linux版本的应用的修复。

不过，有一个权宜之计/缓解措施，即在端点上为GlobalProtect应用启用FIPS-CC模式（并在GlobalProtect门户/网关上启用FIPS-CC模式）。

AmberWolf研究人员表示，还可以实施基于主机的防火墙规则，以防止用户连接到恶意VPN服务器。

## CVE-2024-29014

CVE-2024-29014影响SonicWall的NetExtender VPN客户端在Windows版本10.2.339及更早版本，当处理端点控制（EPC）客户端更新时，允许攻击者以SYSTEM权限执行代码。该漏洞源于签名验证不足。

有几种利用场景可能导致这种情况。例如，用户可能被诱骗将他们的NetExtender客户端连接到恶意VPN服务器，并安装假冒的（恶意的）EPC客户端更新。

AmberWolf研究人员解释了另一种方法：“当安装了SMA Connect代理时，攻击者可以利用自定义URI处理程序强制NetExtender客户端连接到他们的服务器。用户只需要访问恶意网站并接受浏览器提示，或打开恶意文档，攻击就可以成功。”

SonicWall在今年早些时候已经在NetExtender Windows（32位和64位）10.2.341及更高版本中修补了这个漏洞，并敦促用户升级。

AmberWolf建议：“如果立即升级不可行，考虑使用客户端防火墙限制对已知合法VPN端点的访问，以防止用户无意中连接到恶意服务器。”

VPN在许多场景下被视为不可或缺的工具，它提供了加密通道，使得用户可以在公共网络上安全地传输数据，同时也能绕过地理限制访问被封锁的内容。例如对于需要远程工作的员工，VPN提供了安全访问公司内部网络的能力，确保了数据传输的保密性和完整性。但不可否认的是，VPN的存在也给企业带来了更多的攻击面，并且成为黑客攻击的跳板。

参考来源：https://www.helpnetsecurity.com/2024/11/26/vulnerabilities-corporate-vpn-clients-cve-2024-5921-cve-2024-29014/

***END***

阅读推荐

[【安全圈】微软又全球宕机11小时，多项核心服务无法使用](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=1&sn=c19f13229d6729fcaba6459e32b28d5a&scene=21#wechat_redirect)

[【安全圈】慎用，知名压缩工具7-Zip存在严重漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=2&sn=778f80b7b5c35162dd41acacfbd17148&scene=21#wechat_redirect)

[【安全圈】微软给Windows 11添加新选项允许打开任意文件夹最终都在新选项卡中打开](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=3&sn=eda307d1af237cfd16d170e9ffa459af&scene=21#wechat_redirect)

[【安全圈】Ubuntu 20.04 LTS版即将5年主流结束 除非订阅ESM否则明年4月将无法更新](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066233&idx=4&sn=0490cbd0d910ca903dcdf33af3bd1057&scene=21#wechat_redirect)

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

阅读原文

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