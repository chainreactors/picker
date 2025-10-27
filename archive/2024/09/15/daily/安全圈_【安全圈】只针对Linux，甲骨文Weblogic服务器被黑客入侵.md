---
title: 【安全圈】只针对Linux，甲骨文Weblogic服务器被黑客入侵
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064389&idx=2&sn=2bbfa07185363b94c2132b8620da381f&chksm=f36e66c5c419efd3976c784ae290b6ee1d3e0538ce9f6f050d5a320499ad2216f6894fae848a&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-15
fetch_date: 2025-10-06T18:26:48.021883
---

# 【安全圈】只针对Linux，甲骨文Weblogic服务器被黑客入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht65yMlu4YdSUAEqFsa8Lic0pZicqichIUjvmz3u2Z4CkoUj0IzRz0oyYbxg/0?wx_fmt=jpeg)

# 【安全圈】只针对Linux，甲骨文Weblogic服务器被黑客入侵

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

数据安全

网络安全研究人员发现了一场针对Linux环境的新恶意软件活动，目的是进行非法加密货币挖矿和传播僵尸网络恶意软件。云安全公司Aqua指出，这项活动特别针对甲骨文Weblogic服务器，旨在传播一种名为Hadooken的恶意软件。

该恶意软件利用的是Oracle Weblogic中的一个已知漏洞，即CVE-2020-14882。该漏洞允许攻击者获得对Weblogic服务器的未经授权访问，并执行任意代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht69Y8p4CMT6GlXRUic9ciaqPcNs0SH48lvbn22F7ZnnFfCHJTsvhjEXPDQ/640?wx_fmt=jpeg&from=appmsg)

安全研究员Assaf Moran表示，“当Hadooken行动被执行时，它会释放一种名为Tsunami的恶意软件，并部署一个加密货币挖矿程序来获取加密货币，如门罗币（XMR）。”

攻击链利用已知的安全漏洞和配置错误，例如弱密码，以获得初始立足点并在易受攻击的实例上执行任意代码。这是通过启动两个几乎相同的有效载荷来完成的，一个用Python编写，另一个是shell脚本，两者都负责从远程服务器（“89.185.85[.]102”或“185.174.136[.]204”）检索Hadooken恶意软件。

Morag进一步表示，“shell脚本版本试图遍历包含SSH数据（如用户凭据、主机信息和秘密）的各种目录，并利用这些信息攻击已知服务器。然后它在组织内或连接的环境中横向移动，以进一步传播Hadooken恶意软件。”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6vkcMn2iaofxRy6YbLIWtlXXfYwu1atkAD0NcC4633TkyTeALTKmS2cw/640?wx_fmt=jpeg&from=appmsg)

Hadooken勒索软件内置了两个组件，一个加密货币挖矿程序和一个名为Tsunami（又称Kaiten）的分布式拒绝服务（DDoS）僵尸网络，后者有针对部署在Kubernetes集群中的Jenkins和Weblogic服务的攻击历史。

此外，该恶意软件还负责通过在主机上创建cron作业以不同频率定期运行加密货币挖矿程序来建立持久性。

Aqua指出，IP地址89.185.85[.]102在德国注册，隶属于托管公司Aeza International LTD（AS210644），Uptycs在2024年2月的先前报告将其与8220 Gang加密货币活动联系起来，该活动滥用Apache Log4j和Atlassian Confluence Server及数据中心中的漏洞。

第二个IP地址185.174.136[.]204虽然目前处于非活动状态，但也与Aeza Group Ltd.（AS216246）有关。正如Qurium和EU DisinfoLab在2024年7月强调的，Aeza是一家在莫斯科M9和法兰克福的两个数据中心都有业务的防弹托管服务提供商。

研究人员在报告中说：“Aeza的运作方式和快速增长可以通过招募与俄罗斯防弹托管服务提供商有关联的年轻开发者来解释，这些提供商为网络犯罪提供庇护。”

参考来源：https://thehackernews.com/2024/09/new-linux-malware-campaign-exploits.html

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccHv6u9KrSpvq29PNagJll5hNGOzLAbxdyydCGW5fmibrvpP05TOfibDlw/640?wx_fmt=jpeg)[【安全圈】新型 Vo1d 恶意软件曝光，超130万台安卓电视设备已中招](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=1&sn=86872ba5c7fd0a8fb03d84febaa490d2&chksm=f36e6633c419ef2582f41f7358b5a94ec9e1ea409cbd54a4e4038c81e4f7ee545452d86a80ca&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccwgHI6ds7LRyGAxHH65BGRIicoyrib1ADicuTbN0zNqz29mCVgRNC5tw0w/640?wx_fmt=png)[【安全圈】天翼云盘主域名遭微软报毒拉黑 目前Microsoft Edge会自动拦截访问](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=2&sn=9c6331bd04185788e03156e723c86aba&chksm=f36e6633c419ef255b39135c006f3d38b741d9c8a4e855bf8fa5e646b10097ea01536887ee14&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0cc8Victdkjliaiabp79icS3ucppL0Ok6LPGVTGnicLQJ9IPR7Bl4EE5UtcUicA/640?wx_fmt=png)[【安全圈】网络安全软硬件开发商飞塔(Fortinet)泄露约440GB客户相关的数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=3&sn=f978ad9b352ecb4006ea727e1d181157&chksm=f36e6633c419ef2503fda40defd9a7dbec8f80967a704f4e9c017c684beff17192e2ce836029&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliaQMtdXVyG0mKxE0UORZ0ccT1lic86Mh3JWP1gwibcNKYchKuP7Gq21gKs7LZcQ9volJtyicr2MHdutA/640?wx_fmt=png)[【安全圈】Windows 11 22H2版将在下月结束支持 微软从10月8日起开始强制更新](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064371&idx=4&sn=463256c6b4a84c7f835c4ac8d4e9add2&chksm=f36e6633c419ef2584a9d72c9ee174a113221b71c6bf04386e34a5a1be07a81daef4426f791e&scene=21#wechat_redirect)

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