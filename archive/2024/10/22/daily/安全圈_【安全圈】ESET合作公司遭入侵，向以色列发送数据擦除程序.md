---
title: 【安全圈】ESET合作公司遭入侵，向以色列发送数据擦除程序
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065399&idx=3&sn=dacaf2f4ee866d214c7f7b0faa72c698&chksm=f36e6237c419eb2114883fd8867dd3cfd654f569b15b7cebaea0859b3f35e53cafe3a995117f&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-22
fetch_date: 2025-10-06T18:52:50.298475
---

# 【安全圈】ESET合作公司遭入侵，向以色列发送数据擦除程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgI6NFB4tz8wk9MAV6SQslXO2P8kibz04bGdEYmzDasBkFpiaKEESBN1wpX7E5YhOyAmysdyibIgfu8w/0?wx_fmt=jpeg)

# 【安全圈】ESET合作公司遭入侵，向以色列发送数据擦除程序

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络钓鱼

据BleepingComputer消息，有黑客入侵了 ESET 在以色列的独家合作公司，并向以色列企业发送网络钓鱼电子邮件，其中暗藏数据擦除器以进行系统破坏性攻击。

据观察，这一钓鱼活动从10月8日开始，这些邮件带有ESET 徽标且从合法的 eset.co.il 域发送，表明以色列分部的电子邮件服务器在攻击中遭到破坏，ESET 告诉 BleepingComputer，他们位于以色列的分销商由Comsecure 运营。

这些电子邮件显示来自ESET 高级威胁防御团队，警告收件企业由政府支持的攻击者正试图以他们的设备为目标。为了帮助保护设备，ESET 提供了一个名为“ESET Unleashed”的更高级防病毒工具来抵御威胁。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgI6NFB4tz8wk9MAV6SQslXX20ibABEjoenRYwq3xClaBP5pWkibib4uUzalczzjDeicBVdW8NTiblDCDA/640?wx_fmt=jpeg&from=appmsg)钓鱼邮件正文

从网络钓鱼电子邮件标头中，BleepingComputer 已确认该电子邮件来自合法的邮件服务器 eset.co.il，并通过了 SPF、DKIM 和 DMARC 身份验证测试。为了进一步增加攻击的合法性，下载链接托管在 eset.co.il 域的 URL 上，目前已被禁用。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgI6NFB4tz8wk9MAV6SQslXc6JkREP7bEcFfNUO2pgbib8qlic0MH1Qsy4reUSBibJK6r9gEgE7ABiasw/640?wx_fmt=jpeg&from=appmsg)分析显示钓鱼邮件通过了身份验证检查

下载的ZIP 存档包含4个由 ESET 的合法代码签名证书进行数字签名的 DLL 文件和1个未签名的 Setup.exe。这4个 DLL 是作为 ESET 防病毒软件的一部分分发的合法文件。但是Setup.exe 实为恶意数据擦除程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgI6NFB4tz8wk9MAV6SQslXveynMYI1krNXBNCGIqicqAT0IVp8DDLhWVibOc3YKdDeoxAcHDo9nrWA/640?wx_fmt=jpeg&from=appmsg)包含数据擦除器的 ESET Unleashed 文档

BleepingComputer 尝试在虚拟机上测试擦除器，但可执行文件会自动崩溃。网络安全专家凯文-博蒙特（Kevin Beaumont）则在实体 PC 上成功运行了该擦除器，他发现，该恶意程序使用了多种技术来规避安全检测，并调用了各种恶意程序。

目前尚不清楚有多少以色列企业成为此网络钓鱼活动的目标，也不知道 ESET 的以色列分销商 Comsecure 是如何被入侵的。

虽然这次攻击没有被归咎于任何特定的黑客或组织，但数据擦除器长期以来一直是攻击以色列的流行工具。2017年，一个有反以色列和亲巴勒斯坦背景的数据擦除器IsraBye在对以色列组织的攻击中被发现；2023 年，以色列企业遭受了一波BiBi 擦除器攻击，包括教育和技术部门。

参考来源：ESET partner breached to send data wipers to Israeli orgs

***END***

阅读推荐

[【安全圈】黑客贩卖“思科机密文件”？网络信息安全再响警钟！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065379&idx=1&sn=426a360899dcd0db1b898d29d6c9a157&chksm=f36e6223c419eb35ba5c71775b60d22aba48f67dd6d49adeb3a87f7a4cccc94f9705e4677449&scene=21#wechat_redirect)

[【安全圈】福州警方打掉一利用虚拟币洗钱团伙！](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065379&idx=2&sn=3cd7d199549f21e5c523c2bdd013c464&chksm=f36e6223c419eb3564e212a46410a425c7cee66c650fd1281753f8f2ed435c994ebad143db3f&scene=21#wechat_redirect)

[【安全圈】离职后“另立门户” 抄了前东家的小程序还翻录了课：真“刑”](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065379&idx=3&sn=6b2c6731c63cc6bc7b68183c43a3c6e0&chksm=f36e6223c419eb357547a500fcd293ed116c07693dacad14d3b1a8a90d77c5833f9a4d4bf7f4&scene=21#wechat_redirect)

[【安全圈】美高梅国际酒店集团证实黑客在网络攻击中窃取了客户的个人数据](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065379&idx=4&sn=afe8eee832395bbfce424995be4eebab&chksm=f36e6223c419eb355dbb5df89229036eafc69e9dfb385262f2eee9df527813ddad9279e87c9e&scene=21#wechat_redirect)

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