---
title: 【安全圈】苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064389&idx=1&sn=7a205baee5ce2be6ab3b75ba6a3c86c8&chksm=f36e66c5c419efd3d7b7824ab4d3b6ce965b4f87f2b86d1e236ffb7f3e3469f8b5e4e8cceefe&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-15
fetch_date: 2025-10-06T18:26:46.692493
---

# 【安全圈】苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht6MENTmWcsiadddKPA4stK0OVOOgVO3QPibuHx8XyeJhibwkIBC4NaQl3VQ/0?wx_fmt=jpeg)

# 【安全圈】苹果 Vision Pro 曝出严重漏洞，黑客可通过用户眼动输入窃取信息

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaNHjCO1dPBFMDocQfhIht61y4epuhzDzdG8KCVaHSXh4nBVwp03Me5anAoorB2iapg1zwGGtTKa1g/640?wx_fmt=jpeg&from=appmsg)

近日，苹果公司的 Vision Pro 混合现实头戴式设备曝出一个安全漏洞，一旦被黑客成功利用，他们就可以推断出用户在该设备的虚拟键盘上输入的具体数据。

该攻击活动名为 GAZEploit，该漏洞被追踪为 CVE-2024-40865。

佛罗里达大学的学者对此表示：这是一种新颖的攻击，因为攻击者可以从头像图片中推断出与眼睛有关的生物特征，从而重建通过注视控制输入的文本。GAZEploit攻击利用了用户共享虚拟化身时凝视控制文本输入的固有漏洞。

在该漏洞披露后，苹果公司在 2024 年 7 月 29 日发布的 visionOS 1.3 中解决了这一问题。据苹果描述，该漏洞影响了一个名为 “Presence ”的组件。

该公司在一份安全公告中说：虚拟键盘的输入可能是从 Persona 中推断出来的，其主要通过 “在虚拟键盘激活时暂停 Persona ”来解决这个问题。

研究人员发现，黑客可以通过分析虚拟化身的眼球运动或 “凝视”来确定佩戴该设备的用户在虚拟键盘上输入的内容，极易导致用户的隐私泄露。

假设黑客可以分析通过视频通话、在线会议应用程序或直播平台共享的虚拟化身，并远程执行按键推断，那么他们就可以利用这一点提取用户键入的密码等敏感信息。

攻击主要是通过对 Persona 记录、眼球长宽比（EAR）和眼球注视估计进行训练的监督学习模型来完成的，以区分打字会话和其他 VR 相关活动（如观看电影或玩游戏）。虚拟键盘上的注视方向会被映射到特定的按键上，以便确定潜在的击键方式，同时还考虑到键盘在虚拟空间中的位置。

研究人员表示：通过远程捕捉和分析虚拟化身视频，攻击者可以重建用户键入的按键。目前，GAZEploit 是该领域首个已知利用泄露的注视信息远程执行按键推断的攻击方式。

参考来源：Apple Vision Pro Vulnerability Exposed Virtual Keyboard Inputs to Attackers

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