---
title: 微步云沙箱送上一大波高频IOC
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650181827&idx=1&sn=de46d954eb3668b3265cdc68a075e538&chksm=f4486b7fc33fe269ab8b83fb87feb8214b9314c8d436a19d3e19ae7e32e9e7662599d2ba8875&scene=58&subscene=0#rd
source: 微步在线
date: 2024-07-26
fetch_date: 2025-10-06T17:43:36.420513
---

# 微步云沙箱送上一大波高频IOC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0nBia1NyjiallTcZiaaXKFwXSzojKFwV436WUeomwslVQd87Nicib1tYMOJ2g/0?wx_fmt=jpeg)

# 微步云沙箱送上一大波高频IOC

原创

S云沙箱

微步在线

# ![](https://mmbiz.qpic.cn/mmbiz_gif/Yv6ic9zgr5hRYwmkFFVSsK0fQGJBGqwl6iaBoFgqTpPricWCuX7uIb4Rj7eibLo3ibOiaOtqo7vXEnibKhxuInrceOoibg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

每逢“佳节”倍思亲，思的什么亲？蓝队的父老乡亲！

在这个漫长的夏秋之交，微步云沙箱端出了超大杯更新，在漏洞利用、红队工具上都有了大提升，大家最关心的【CS马检测能力】和【重保2024】也有明显加强，文章结尾更有我们收集到的高频 IOC Hash 共35条，先转再看！

**5个行为检测角度，彻底看清漏洞利用行为**

我们上线了对高危漏洞（如Office和WPS的0day或1day）的静态检测和动态行为检测，动态行为检测可从漏洞利用行为、通用漏洞行为、文件相关行为、进程相关行为和网络相关行为第二个5个角度对漏洞利用行为进行检测。

拿一个开打第一天收到的样本来做例子：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0nQ1b953gkxMaux9te9G5sD3DJlLicXwXMXuEcRrZzTZdQ7OR3Y5oibKbg/640?wx_fmt=png&from=appmsg)

首先能看出，这是个存在漏洞利用行为的恶意文件；

其次，漏洞是个RCE漏洞，经评判具备【重保2024】标签；

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0nicB4ib0y8NhGeViac27XB37YWYn3pOLo8myRdIG5qBRFD6EcibBibMaUe4w/640?wx_fmt=png&from=appmsg)

静态引擎给出的结果能够精准定位到微步的漏洞编号：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0nokTUtjyOOaXPje6mXz6o9AqkwAfEibVU0iakjFUFNjeibnCqIeq5sN2kQ/640?wx_fmt=png&from=appmsg)

此外，近期还捕获了大量相关样本，不过暂未发现真实利用。看得出来，这位红队师傅应该只是侦查和攻击测试，尚未发起实际攻击。

以另一样本为例，在漏洞利用-动态行为检测中，能够检测到系统敏感操作、恶意行为特征、可疑的网络请求等，为漏洞利用的检测提供了完整佐证：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0n3FHEqWrTQmSjmKS9hyJuicj1NxwHC5PYna27nSmQbfSKMG3wpRez9Ag/640?wx_fmt=png&from=appmsg)

**红队工具检测前进一大步，覆盖80% T0-T1强度的工具家族**

为了提升云沙箱对红队工具的检测能力，我们进行了专项运营，目前已经支持数十个家族的精准检测，可以覆盖80%的常用红队工具，FRP、fscan、Mimikatz、Stowaway、BruteRatel等工具都在其中：

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0njnmlg6Fz2Zna9xZp84YHc66fOLWnt12j9Ks9fIBa7lMJLsGb3pvDbQ/640?wx_fmt=png&from=appmsg)

检出结果中能够清晰显示样本所对应的红队工具家族，以及其典型的恶意行为。

**CS马跑通率：高对抗场景下提升50%**

不得不说，红队师傅们反沙箱技术高超，但我们也没选择躺平，今年我们在CobaltStrike的跑通率上也做了专项运营，在高对抗场景下，CS马分析跑通率已经提升了50%，检出率自然也有了大幅度的提升，大家来试试看吧！

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0n2LIyVxYdMW5TnUYkrkLd59k232PB8CTIDD02Xs5auuKq3ynQK7LfmQ/640?wx_fmt=png&from=appmsg)

TDP：坏了，我成样本了

此外，云沙箱工作组在【重保2024】期间安排了专人全程值守、研判并不定期更新【重保2024】标签信息。

目前，微步云沙箱支持不限格式的文件分析（最大500M），支持同时分析多个环境，以及指定各种运行参数，快把微步云沙箱s.threatbook.com放进收藏夹吧！

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0nGx78ab2BPI4CM8CPs9AibKs9CNVwiboiaUUk12o09Uo8Gn8PTMgI9amkw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hRnG7Iv55CkHOzJQcQiaRD0nYqfpmEZMXOlDDNDziclOu7c81hN79Q3XYOfKT2Ycn0NtNeZMN1QZTuw/640?wx_fmt=png&from=appmsg)

**附录-IOC**

**样本Hash：**

dccc77558f6a4bb755c94b3e2e6839beec74dc901dcd7c5560677075c3e564ac

13d7483a1f1a0b72aaa09ec985797556eeb402c893013a5bc08b706300c5bb3d

282ff7e6f0e856a2220f8ec8c95c4b3d949e91c3e5f1579a69341917137dfdd9

36f92ac5e2ec70d8fb965f74bb823f883d3f48085667df299b3e4d95c59a521d

02bbeb4d9d6f13fe1db44a0a2da572b1596d9ff59b79376e8afaeab0ba76a1d6

ae7f7d1b1a2da2479d99de5e0d37d71786f81936fbff919a61fdb4b0d4f8bd47

8ff575dcb6e37945bf8d635f9b3575473882956e397d84be1b8d2d9ed1be2029

3f3cb10b9eb096a4f6aeb74ab44487d9b7d4b88cf6cdb14bc7364b3263e79f10

0cd9f7b34ef5d21a908660989a83dc916a483d823656a2970c4e44555591d816

fff3ec09026f873f39b73111556454163a16f18e23d1c2a80b5e5a3f5d54e599

8a69270b966cf1a8d713f295c748a028154d1ea2e012d1a7fb89cd9d47d295d3

ce88a5fc38c909dc7903037e0439ed378af5058459edfa5668e31dfa3baaf09a

dd84024be0c4c78b2db197a8139ffec67941724168753946f216af9ac4765f2e

4dd82e7cf887db647e2562381825fd070125787830fef937fe845616dd4ef6ab

6eeb368818f97dd9dc4e0c1bbfbdae34ac5d3e9bcd9824e07803a388ff0fe7fa

8d72a453c3ab1b7471f87d3ebe4d5b194dca1c8857f05f2852992be2dfe55a04

24588385fc894c2176c52a276a32dc47ba5d4133c15b1d580dcd051f390ac4ad

ae3af47eb61dd05f6255222cd3a9d3ac2a7c65d1acaad520cc7bca33d8dc7534

daa5dafd697e76d85bb5d36e6c4425b41ca07c849117df10f9f1285f0235b5f4

ce023affa9339e438d9e66eddabbe0a27bdd5f84f1fdafea2a3990d258f995a5

ae9f32666fd46672b502a7c946a8bd09bbdd910f42168a62ba87aefe77a52a29

d3cf90433e96a46b8aee6da223caf20271fd9f861a10d9f3b194bfc55f88163b

e500a848f5c8f20cf5264d79ab478fbc93649030f1af51ed7ca62ddd2c1eaee8

5f66fc49e855540fef3dd0e44b3be9702dd586a630ddbca8aef85e073b311417

0a4db606002775476e53cc6d8bc1096c501470f53ce0fb7341d2dfeebc623b33

9bc04393f713e8d0506b0b9cca542e3cfe96697e04fd0682a7928efef8181416

b8482ce5063a6c61234784e5c4c519ac8ebf9e40405cc9e29019007ed4b5fb7e

8f52a7edb8e8332a30384e85519ca54cb950ea4e4f859ca526f63e88f4eb7c40

42bec1f82061726a850accf18f3be1c5ec04a92ff840e202917e4bafc04b0ffa

1c237abb44c6a0056d76cf67e4bbb2c73ae023e8badbda4a6ca904a590c87fcf

297a9c584a57b09392431350a2878156cd9bed51c231b0599622fe7ffeb31202

54393723d5ec1eca0c77dcaf75ae9c405080c902a8f45617d489718684510802

46e15f97970fc241586ab738414b8d629895f15a0a8d6d21322b00d6e6acb252

065cdc8e2d1c702ce7c2bf37c81e565a61340a2966e0a2673f27831af3a04d69

**样本主题：**

化工项目现场安全员+刘\*+17318684723.zip

测试tdp (2).zip

刘\*-地质勘查-西北大学.exe

社会招聘+数据分析+\*宁.zip

中\*共享服务（天津）有限公司社会招聘报名登记表.exe

应聘贵公司-投资开发部主管-杨\*峰pdf.exe

东\*电子采购平台数字签名服务补丁升级包v2.1.exe

东\*电子采购平台数字签名服务补丁升级包安装说明.exe

中国\*能电子采购平台数字签名服务补丁升级包安装文件.rar

安全补丁0722.exe

国家\*\*投资集团改革深化提升行动重点任务考核落实.zip

问题描述1.exe

相关材料-0723.zip

海\*\*场安全风险分级管控和隐患排查治理双重预防工作机制实施细则制度宣贯.exe

重大安全隐患判定标准解读-运输机场 .scr

应\*\*理部保留CITRIX权限人员名单.exe

骨折照片 .exe

附件1、表格KM1监管并表关键审慎监管指标.zip

汪\*-上海交大硕士-应聘系统安全岗20240722转换pdf.exe

个人简历.exe

中山大学-罗\*婷-博士申请.rar

华\*医药商业报销.PIF

高温补贴通知单.exe

刘\*诗简历.rar

安全手册.exe

哈尔滨\*\*集团有限公司整改“回头看”专项审计报告.exe

情况说明.zip

附件1：中\*正版化软件更新.zip

music.ico

defender.exe

wechat.exe

zabbix.exe

Phone.exe

java\_agent

· END ·

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSA5A4iaspRVClFku4KVwkOUriclTaohLibE2oQKMTrQ8hvSFFHevq88eibd7mstuZbeNLm5U1tPJT3xQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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