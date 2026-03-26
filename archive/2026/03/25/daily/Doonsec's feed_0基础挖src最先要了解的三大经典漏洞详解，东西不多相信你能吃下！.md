---
title: 0基础挖src最先要了解的三大经典漏洞详解，东西不多相信你能吃下！
url: https://mp.weixin.qq.com/s/4xdtc_uGeCtkGuaS01ATxA
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:28:36.774680
---

# 0基础挖src最先要了解的三大经典漏洞详解，东西不多相信你能吃下！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Siaf7AeeM2YgHmV5vEGox48jbYxPxW7uicfVgGnytNobaLEx6H0icE1WDKkibVIlbneKkAP6d9LGTy4tkCo9UBUAPrywiaecJ2S3Nc/0?wx_fmt=jpeg)

# 0基础挖src最先要了解的三大经典漏洞详解，东西不多相信你能吃下！

原创

周小粥
周小粥

周小粥讲安全

![]()

在小说阅读器中沉浸阅读

**关注**👆🏻公众号→回复“**1**”自取0基础攻防教程

今天给大家分享小白入门最先需要吃透的3个漏洞，东西不多相信你一定能吃得下。

---

第一「SQL注入」

它可以说是Web漏洞里的“常青树”，别看它简单且久远，年年都有网站因为这个被拖库。和其他漏洞不同，它不靠复杂的配置，就藏在登录框、搜索栏甚至URL参数里，一旦被利用成功就可以直接读写整个数据库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9R4HeVha0xBkSx2ibDnOkiagzV9OBA0Cfm2E7U5XTOrzGHIgQ8pUTyEWibc6kWz8DqlunZNONjykqo0icBxFlGas9lmEeKRHuTvt9w/640?wx_fmt=jpeg&from=appmsg)

搞懂这个漏洞就能让你理解前后端交互的底层逻辑，对新手建立安全思维特别有帮助。

---

第二「XSS：跨站脚本攻击」

它是GitHub上安全报告里出现频率最高的漏洞之一，有存储型、反射型、DOM型三种。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9SaKFsiceZwvUFBOorVyRup7zR8tgaVfLegfZBQXx1oIALyPkibNCsIbIV0ObHQkZoI25w1smd742kyuiceMMZpNsN2frE8NPED78/640?wx_fmt=jpeg)

刚学的时候可以从最简单的反射型入手，这个漏洞看起来“只是弹个窗”，但在真实场景里它不仅能偷用户的Cookie、劫持会话，甚至还能钓鱼。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9QUGrWbvEQdtibD2JjCrad7Xcht6omOUMoKUo3XCzKqxk4v6CpJ2GRBpRAMrmbMiapUk80fFjmZay2PehQDuV7icazBKBH6OQSsr0/640?wx_fmt=jpeg&from=appmsg)

我早期挖的很多中低危漏洞都是XSS，因为企业普遍重视，提交也容易过审。

---

第三「文件上传漏洞」

表面上它只是个普通的图片上传或者文件提交功能，实际上只要后端没校验文件类型和内容，黑客就可能塞进去一个恶意程序，然后在服务器上执行任意指令，当服务器最高权限被拿下的那一刻，你就能真正感受到，任何一个功能节点都有可能成为入侵的突破口。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9T6kicegtOOdFgHk3epppxutibRyyicJOcplanXxU24hHcwAgIib88B7Pyoabt8sfOkk2qibAjKELGicJ5l73R2M6PxfeXGknKoHT7JQ/640?wx_fmt=jpeg)

等你把这几个经典漏洞的复现和防御思路都跑通以后，后接触top10的其他漏洞也能很快上手。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RibIhEtXb1t0adGn1mYxkTyOGx8j9Pzu6YcZtq3fd3lVtibj3HF9x3wuUduLGY3Puk31oZT8H6NfOFzMw3Fyicc16XGyWtQyLy8Y/640?wx_fmt=jpeg)

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

---

如果你还需要其他学习思路可以去看一下我的往期文章：

[0基础该如何转行网络安全？值得吗？](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484313&idx=1&sn=e62e92639b5b1577ad802a3129f11ad0&chksm=c2fc9043f58b195548dd0009fdf1fdeccd2b3bd68e144ae4a42c78bde7d5ead281c2a53f8287&scene=21#wechat_redirect)

[【工具/案例篇】神仙级渗透测试入门教程(非常详细)，从零基础入门到精通](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484278&idx=1&sn=2475864a18fd158f1100b0d7e3dd33e3&chksm=c2fc90acf58b19ba8bfe9f656831d79ceb6529807de784998bc2b0afe2fa40f0b5361521b298&scene=21#wechat_redirect)

[网络安全自学（超详细）：从入门到精通学习路线&规划，学完即可就业](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484267&idx=1&sn=2e6844ce1608081cee498900169e3e7b&chksm=c2fc90b1f58b19a7eb633cfe7e082652d2adac80e2a815100762b531691baa759fc5560577d9&scene=21#wechat_redirect)

**周小粥专属网络攻防技术资料**

@网络安全-周小粥：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTiclOnwqZc9T2SWU4Ytbgk67F5oS2kibMC7iaiaHAPzvfCiaD5Gdv9PWR1c3SzvGpyZJ5NbDuic8rENeHQ/640?wx_fmt=png&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPImCly50KaFibfumchg6t3hk80lTboia0MsbqLDgRF7A5YtSGkQzWVibQA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPQVyePJAlTHZictVmp6jI3HrNINrNbKMiaeKHApiaRia6dcMPGBAaibc97hw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPqpnzbQ88VdkICMtKibDRGxFb7nPvnsQlRsmKCzOLYULcB1GoACicGuag/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPaE8RXBicH1Y4T7aeddwLNrKpPcuS4JsGicOic6dXr3aoKK3nIuvu1lMVg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPiaKcFwOp5adPyCbWpj9JDe49cOOZ0YxAhqCQYwt0ldrKtwFeKJ8Utgw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTiclOnwqZc9T2SWU4Ytbgk67F5oS2kibMC7iaiaHAPzvfCiaD5Gdv9PWR1c3SzvGpyZJ5NbDuic8rENeHQ/640?wx_fmt=png&from=appmsg)

@网络安全-周小粥：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTk5CbPZbQltff81fWAianO5baZC5UyfUVPsKfCPia0F1VlvLicw5hHbiaPbPibbxOCn6tg1B8x8OneWVw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**往期精彩**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTk5CbPZbQltff81fWAianO5baZC5UyfUVPsKfCPia0F1VlvLicw5hHbiaPbPibbxOCn6tg1B8x8OneWVw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqRG5oB85wG66TXpUc6CG5d6wKyMGDIMYUf0pfHWfnSZtPU3Psys58XC5mlg8dl1zK8OtMJlGic1kaA/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484337&idx=1&sn=7440b757243bc5120af4c08bcc4d104c&chksm=c2fc906bf58b197d6aeaf924627838dcf7dd1a35a88109a50e8d57fd5478974cc95881d8b9d1&scene=21#wechat_redirect)

**光挖漏洞每月就有1w+？？！这也就是网安人才能感受的到吧**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTnMJW3olNLHDb9oP5XTz7PvshbbCFlFlZlHRaLblcDia4VK62scgVLibibJuicYrstDcO1DicxhkwaDpw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)](https://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484267&idx=1&sn=2e6844ce1608081cee498900169e3e7b&scene=21#wechat_redirect)

**网络安全自学（超详细）：从入门到精通学习路线&规划，学完即可就业**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqR4H6FKAtmlHiawLFfTaYRrF5VvoZNx5u8soCxHxq9s1Pem6MbcqeBP9e54DaBsxia1YicvHeGJibgShQ/640?wx_fmt=png&from=appmsg "undefined")](https://mp.weixin.qq.com/s?__biz=MzkzODU5MTkyNQ==&mid=2247484313&idx=1&sn=e62e92639b5b1577ad802a3129f11ad0&scene=21#wechat_redirect)

**0基础该如何转行网络安全？值得吗？**

**点击图片即可跳转**

***【免责声明】版权归原作者，如有侵权，请联系我进行删除。***

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPb3IUhP4mQSwfsLiaVSsTM1GEltIG7wPkmmn2UNIHyB4W5VhZum4T12Q/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**点分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPvCskTcp6Zf7awicY7eIOoIVIggCV4RQVVSiakEFhcuFF9d1BiaDmib2hQg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**点收藏**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPnM8PX9hqO0fWbCBc9ianDKuLazdYbibLy8icM2DYB4Fjo3EsicicMaQFUXQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**点在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPu0zYaTqkBIq9L98XZ18y1N7pgaXN6wowp9ibSNHr1iahlt7ia8gC4YWJg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**点点赞**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPx87VoQsZ7eg9ia8FhcG9zJiaibTO1rRt1vbNBk4SSVWnhgwvgV4Sj48bA/0?wx_fmt=png)

周小粥讲安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPx87VoQsZ7eg9ia8FhcG9zJiaibTO1rRt1vbNBk4SSVWnhgwvgV4Sj48bA/0?wx_fmt=png)

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