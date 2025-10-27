---
title: 【安全圈】尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064138&idx=1&sn=53220a217e6d037a4a2660176faf81c0&chksm=f36e65cac419ecdc21d88b0b992bc733d43a72cfdf95554403ccb9531d4f08c9ffaf2906559c&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-05
fetch_date: 2025-10-06T18:27:11.832815
---

# 【安全圈】尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LML1mZzicUfhZ7r3vFHeqJu3icYn2JSiankak3uWiccRqD7l7NOzxbsQFGJZQ/0?wx_fmt=jpeg)

# 【安全圈】尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

安全漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LMLd1J7Mo5ib7eoshUTHSKnZzHA26iaKlfk3EzCIicJhLzl2xk4b1L5Yo8ag/640?wx_fmt=jpeg&from=appmsg)

近日，Zyxel 发布安全更新，以解决影响其多款商用路由器的关键漏洞，该漏洞可能允许未经认证的攻击者执行操作系统命令注入。

该漏洞被追踪为 CVE-2024-7261，CVSS v3 得分为 9.8，是一个输入验证故障，由用户提供的数据处理不当引起，允许远程攻击者在主机操作系统上执行任意命令。

Zyxel 警告称某些 AP 和安全路由器版本的 CGI 程序对参数 “host ”中特殊元素的中和不当，可能允许未经认证的攻击者通过向有漏洞的设备发送伪造的 cookie 来执行操作系统命令。

受 CVE-2024-7261 影响的 Zyxel 接入点 (AP) 如下：

* NWA 系列：NWA50AX、NWA50AX PRO、NWA55AXE、NWA90AX、NWA90AX PRO、NWA110AX、NWA130BE、NWA210AX、NWA220AX-6E | 7.00 之前的所有版本都存在漏洞，请升级至 7.00(ABYW.2) 及更高版本、NWA1123-AC PRO | 6.28 之前的所有版本易受攻击，请升级至 6.28(ABHD.3) 及更高版本、NWA1123ACv3、WAC500、WAC500H | 6.70 之前的所有版本易受攻击，请升级至 6.70(ABVT.5) 及更高版本
* WAC 系列：WAC6103D-I、WAC6502D-S、WAC6503D-S、WAC6552D-S、WAC6553D-E | 6.28 之前的所有版本易受攻击，请升级至 6.28(AAXH.3) 及更高版本
* WAX 系列：WAX300H、WAX510D、WAX610D、WAX620D-6E、WAX630S、WAX640S-6E、WAX650S、WAX655E | 7.00 之前的所有版本都存在漏洞，请升级至 7.00(ACHF.2) 及更高版本。
* WBE 系列：WBE530、WBE660S | 7.00 之前的所有版本都存在漏洞，请升级至 7.00(ACLE.2) 及更高版本

Zyxel 表示，运行 V2.00(ACIP.2)的安全路由器 USG LITE 60AX 也受影响，但该型号已通过云自动更新到 V2.00(ACIP.3)，其中实施了 CVE-2024-7261 的修补程序。

## 更多 Zyxel 修复

Zyxel 还针对 APT 和 USG FLEX 防火墙中的多个高严重性缺陷发布了安全更新。摘要如下：

* CVE-2024-6343：CGI 程序中的缓冲区溢出可能导致通过身份验证的管理员发送伪造的 HTTP 请求，从而导致 DoS。
* CVE-2024-7203：验证后命令注入允许通过伪造的 CLI 命令执行操作系统命令。
* CVE-2024-42057：在 IPSec VPN 中的指令注入，允許未認證的攻擊者在「使用者為本-PSK」模式下，利用偽造的長使用者名稱執行作業系統指令。
* CVE-2024-42058：取消引用空指针可通过未认证攻击者发送的伪造数据包导致 DoS。
* CVE-2024-42059：身份验证后命令注入允许身份验证的管理员通过 FTP 上传伪造的压缩语言文件执行操作系统命令。
* CVE-2024-42060： 認證後指令注入漏洞，令已認證的管理員可透過上載精心製作的內部使用者協議檔案，執行作業系統指令。
* CVE-2024-42061：dynamic\_script.cgi "中的反射 XSS 允许攻击者诱骗用户访问伪造的 URL，从而可能泄漏基于浏览器的信息。

上述漏洞中 CVE-2024-42057 值得特别关注 ，它是 IPSec VPN 功能中的命令注入漏洞，无需验证即可被远程利用。

利用漏洞所需的特定配置要求会降低其严重性，包括在基于用户的 PSK 身份验证模式下配置设备，以及用户的用户用户名长度超过 28 个字符。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LMLnJazzLiccysvTzLJbSjDhonseT66C0iaEPvV9u531U5BxFO5APTdxhjA/640?wx_fmt=jpeg&from=appmsg)

图源：Zyxel 官网

有关其他受影响的防火墙更多详细信息，可具体查看 Zyxel 公告。

参考来源：Zyxel warns of critical OS command injection flaw in routers (bleepingcomputer.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LMLvYicDaeRQnPmibSvg5w9nWiaBeSMDGvrsNPtS8EMdDo87aIgkaK2ExkJA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LMLt2vVbZA7MDULjoxpyCnnaYGNJFelyGev1umWPuCs5w61RuqekzK0cw/640?wx_fmt=jpeg)

[【安全圈】网络身份证是强制，会影响正常上网？公安部详细回应](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652063868&idx=2&sn=e0e51cc3262a54328e4fee1482c882f1&chksm=f36e643cc419ed2a36eb00a524a91605bcd28b782d15ab7fb662c206140dca0df3a38bac1c1a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LML5aYWDHREPbtC8FRK433hVpyxo7P99JgIicBAibT0DhmqM7EicreETM42Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhuVBWzBFpEzH5a90hN7LMLj587o1vRBia5y6AKwaibnwspv1JATA1geq6w7mMLT0zREMI2f6Wx8BfQ/640?wx_fmt=jpeg) [【安全圈】美国媒体巨头考克斯媒体集团宣称通过监听用户手机麦克风收集信息投放广告](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064118&idx=4&sn=82073eee169a9d857c0e826941a809e9&chksm=f36e6536c419ec207ac664248fd35bd40b7379e4c539b0e1af129e76d22d0a895d0b6e9ff87e&scene=21#wechat_redirect)

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