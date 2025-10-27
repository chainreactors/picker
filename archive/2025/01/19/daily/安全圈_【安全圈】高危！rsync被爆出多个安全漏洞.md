---
title: 【安全圈】高危！rsync被爆出多个安全漏洞
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067460&idx=1&sn=7e41cdf5b76e20186089903f7171a588&chksm=f36e7ac4c419f3d2506b8a4fda50d186484d0b429b68fbc2c9fa6a6d793e423ec4e7374d18b2&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-19
fetch_date: 2025-10-06T20:09:07.645002
---

# 【安全圈】高危！rsync被爆出多个安全漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljvUKhLrdazZeNW748aFKwprTmHZ0qe0YWARDZK8dA3OYHWV0RNSSHM34lgjzDmxwCGW9WloQLCcg/0?wx_fmt=jpeg)

# 【安全圈】高危！rsync被爆出多个安全漏洞

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

近期，Unix 平台上广泛使用的文件同步工具 rsync 暴露出多项高危安全漏洞，安全专家已披露这些漏洞并提供修复措施。为了避免数据泄露和恶意代码执行的风险，所有使用 rsync 的用户必须尽快升级到 3.4.0+ 版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyljvUKhLrdazZeNW748aFKwpib1hPMvSUibHpIoVbd7ibNzDmHvSQtKt2Ot07DSw8icPygAJXFzPmGGd4g/640?wx_fmt=png&from=appmsg)

**漏洞风险一览：**

这些漏洞可以使攻击者通过控制恶意服务器，读取、写入任何已连接的客户端文件，包括但不限于提取敏感信息（如 SSH 密钥）或覆盖用户的配置文件（如 `~/.bashrc` 和 `~/.popt`），从而执行恶意代码。

具体漏洞包括：

* **CVE-2024-12084 (CVSS 9.8)：** 由于校验和长度处理不当，rsync 中存在缓冲区堆栈溢出漏洞，攻击者可通过此漏洞在受影响的系统上执行任意代码。
* **CVE-2024-12085 (CVSS 7.5)：** 堆栈内容未初始化，攻击者可通过此漏洞泄露系统敏感信息。
* **CVE-2024-12086 (CVSS 6.1)：** rsync 服务器可能泄露任意客户端文件，攻击者可利用此漏洞窃取文件。
* **CVE-2024-12087 (CVSS 6.5)：** 路径遍历漏洞，攻击者可绕过路径限制，访问非授权文件。
* **CVE-2024-12088 (CVSS 6.5)：** 使用 `--safe-links` 选项绕过路径遍历的保护机制，导致文件泄露。
* **CVE-2024-12747 (CVSS 5.6)：** 在处理符号链接时存在竞争条件，攻击者可利用该漏洞获取系统控制权。

**漏洞来源：**

上述漏洞的前五个由谷歌云的漏洞研究团队发现，第六个漏洞由安全研究人员 Aleksei Gorban 发现。幸运的是，这些问题已经在 rsync 3.4.0 版本中得到了修复，用户应尽快进行升级。

**有超过66万台公开暴露的Rsync服务器受六个新漏洞威胁。**

**最严重漏洞的影响：**

根据红帽产品安全部门的分析，最严重的漏洞（CVE-2024-12084 和 CVE-2024-12085）可以在 rsync 服务器运行的客户端上执行任意代码，攻击者仅需匿名读取公共镜像或其他镜像服务器，便可控制服务器并执行恶意操作。这对很多依赖 rsync 进行同步和镜像的网站、企业甚至政府机构构成了巨大的安全威胁。

**如何保护自己？**

红帽强烈建议所有 rsync 用户立即升级至最新版（3.4.0+）。如果暂时无法进行升级，用户可采取以下缓解措施：

1. **针对 CVE-2024-12084：** 通过使用 `CFLAGS=-DDISABLE_SHA512_DIGEST` 和 `CFLAGS=-DDISABLE_SHA256_DIGEST` 禁用 SHA 算法支持，降低该漏洞的风险。
2. **针对 CVE-2024-12085：** 在编译时使用 `-ftrivial-auto-var-init=zero` 参数，以确保堆栈内容清零，从而防止泄露敏感信息。

**下载链接：**

用户可通过以下链接下载修复版本：

https://github.com/RsyncProject/rsync/releases

**总结：**

rsync 作为一个被广泛应用的文件同步工具，其安全性不容忽视。此次漏洞的暴露提醒我们，任何网络工具都存在被攻击的风险，用户务必保持警惕，及时更新软件，并采取必要的防护措施。

***END***

阅读推荐

[【安全圈】支付宝P0级重大事故：整整5分钟所有订单打8折，官方回应：不向用户追款](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067425&idx=1&sn=c8e7e9e9cc66acce28dbc15174a86f30&scene=21#wechat_redirect)

[【安全圈】诈骗者利用加州野火，冒充消防救援服务](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067425&idx=2&sn=092aee43fca9933a220b6b98490fa3f3&scene=21#wechat_redirect)

[【安全圈】新的 UEFI 安全启动绕过漏洞使系统暴露于恶意 Bootkit](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067425&idx=3&sn=ca5d0f47ca765e96d6aca2175ef92b2a&scene=21#wechat_redirect)

[【安全圈】攻击者在图片中嵌入恶意代码传播窃密程序](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067425&idx=4&sn=2c28218b260cd8d931153faff41c94d8&scene=21#wechat_redirect)

[【安全圈】2024年12月涉国内数据泄露事件汇总](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067407&idx=1&sn=47291e4d3be4fe5aba124eaf42090def&scene=21#wechat_redirect)

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