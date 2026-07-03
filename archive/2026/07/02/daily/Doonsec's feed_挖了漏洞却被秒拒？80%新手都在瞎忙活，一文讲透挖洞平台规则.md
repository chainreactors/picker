---
title: 挖了漏洞却被秒拒？80%新手都在瞎忙活，一文讲透挖洞平台规则
url: https://mp.weixin.qq.com/s/tTKquKTRgUZTWxwxZgiN5A
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:45:51.272099
---

# 挖了漏洞却被秒拒？80%新手都在瞎忙活，一文讲透挖洞平台规则

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9Qs1ENelSfVuBWp61xMb0zfmEvxS8d7RScrEzDkeZPtqJgdFahL0pUn1fgTCZ0FwSUm9ExgS053e8oibxeFpJvibiba2F20sd2vyw/0?wx_fmt=jpeg)

# 挖了漏洞却被秒拒？80%新手都在瞎忙活，一文讲透挖洞平台规则

原创

周小粥
周小粥

周小粥讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**关注**👆🏻公众号→回复“**1**”自取0基础攻防教程

其实说实话，我觉得漏洞挖掘（俗称“挖洞”）确实算是一门比较吃细心和耐心的技术活，也是很多普通人能够单凭技术本身（不论学历、背景）赚到零花钱甚至实现职业转型的绝佳副业。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RVicgdO1dWreCW9ibDCaAyicPhLfVMqGXJ0dKUibl16uO5R0lyicy5gaMT0YErNeo2lcyGIsosUFBGbVvsXaIUN9ribWzBIXKqxPgWs/640?wx_fmt=jpeg&from=appmsg)

但是，我敢说80%的新手都没有搞懂平台审核规则，匆匆忙忙学了半年，然后瞎忙活一场。想要高效挖洞，选对平台、摸清规则才是关键！

---

选对平台 —> 新手起步的“练兵场”

对于刚入门的新手，优先推荐关注补天、漏洞盒子、CNVD以及各大厂商SRC。

以补天平台为例，浏览器搜索官网后进入“项目大厅”即可开始，其“项目大厅”主要分为三大板块，各有侧重：

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9Sib6Ym2MicfFqNHTSueqPYjBG4SNsicDMQPiarCibOZkDJpJaTtB5ndGM1oCnZI5k9rkVdnoUBYPibu0iaBjj4mSfmxoQARIVflCzz08/640?wx_fmt=jpeg)

* **专属企业SRC**：短期活动，开放周期通常为几天到几周，适合有特定目标的突击。
* 常规企业SRC：长期开放的“主战场”，可挖掘范围广，审核通过后直接发放现金奖励。
* 公益SRC：新手的最佳“新手村”。虽然不直接发钱，但结算的“酷币”（1枚约等值5元）可在商城兑换实物。这里漏洞难度较低，非常适合新手积累经验、建立信心。

无论选择哪个，你的报告都会经历“平台专家初审”到“厂商二次复核”的严谨流程，最终根据漏洞的危险等级定级发奖。

![](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TK2xR8tEDMEAoX0dpvliaibMfyTdFr5XtA2EnmnFJ6E5vwAbeWGoPIXmlofDv4RQDXO7BjAl4FoaJTWUdIrtvKPgtNYS1JORdiaw/640?wx_fmt=png&from=appmsg)

---

#### 摸清规则 —> 拒绝瞎忙活

很多新手最容易栽跟头的地方，就是对平台审核规则的无知。

以补天平台为例，目前在漏洞性质上**只接收以下两类漏洞**：

* **事件型**：指单个站点出现的具体安全问题（如网站被入侵、用户订单数据泄露等）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QaOmzhWxtBrlarM3Wj5P93w55tbLvCJtEG8o8VEsZXmJnwQgJEbXVo9O8DzbAA6WYM8dCbc9r70Ylpd7s9TacXvEJDS8CkSPU/640?wx_fmt=jpeg)

* 通用型：指PHP、CMS等第三方程序中普遍存在的共性漏洞。

**⚠️ 避坑提示**：如果你提交的是普通无敏感权限的弱口令，或者是早已被修复的老旧漏洞，补天会直接驳回。

  相比之下，漏洞盒子等同类平台在这些基础漏洞的审核门槛上会稍低一些，通过率更高。

  动手前务必提前了解各平台的差异化规则，避免做无用功。

---

#### 进阶认知 —> 渗透思维标准化

要想在挖洞的道路上走得更远，你需要建立起标准化的渗透测试思维。

如业内通用的PTES框架：一个完整的测试流程包含了  前期交互、信息收集、漏洞扫描与探测、漏洞利用、后渗透测试以及报告生成  这六个阶段。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Sy3GQgJy7ic71Y3EZuhy9BK1z4sUb5wqBMdQPicW50mKYFrliamHoPs3L61XPmbA2YO3IVEf2ll9H9HB9blqSN0ywWicp4Gvr8fyw/640?wx_fmt=other&from=appmsg)

新手往往只盯着“漏洞测试”这一环，却忽略了前期的信息收集，这个阶段通过公开渠道收集目标的基础信息（如服务器IP、编程语言、框架版本等），能帮你迅速“缩小范围、找准突破口”。

---

夯实基础 —> 踏实前行

不可否认，挖漏洞是个不错的副业，但前提是“技术过关”。如果你目前感到迷茫，不妨从最基础的计算机网络、操作系统原理学起，逐步掌握XSS、SQL注入等核心实战内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9RkZlXicDhOG6XQrkS7kCgyA7z1Sz4Fwyxq6gWAJNd7sHfeJ7zNKiaDsiaNLSH80ibLZ6szJDtOVf8QSRj0Bv3d8ibgia139mV6iblyibc/640?wx_fmt=jpeg)

跟着学、踏实练，相信大家都能学有所成，拿到属于自己的收获！

---

### 「最后」

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

**视频教程**

和360一起研发，覆盖从入门到进阶的***全套视频教程***（从零到精通：基础攻防→渗透测试→应急响应→CTF实战，5大模块200+课时）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqQQAbb583x7rnkuAgtzeXYDGUNCYrkQxccs2iadybesPicVXxBFuklPVnrw0afJoIEBZibMgrHH15ibQQ/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPQVyePJAlTHZictVmp6jI3HrNINrNbKMiaeKHApiaRia6dcMPGBAaibc97hw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**0****2**

**学习路线**

***2026详细网安学习路线***（包括各类技术的学习顺序和学习时长、学完技术后的发展方向和建议等）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPXGjfl2TiaQ05ZIPFMznOLcr76aP8V4ibDSp5SjxMTdORLaak23mgP3gw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPSEZicfjyPtnILjb076LOEmkPbFa2ffk6jSIX7lWgwg1hyoObwt6Wufw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**0****3**

**书籍Pdf**

99+入行网络安全必看的书籍和文章的Pdf（市面上的技术书籍确实太多了，这些是我精选出来的）

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CsKJlMFPH9QpA8gfIqwuchDXRn63kzLVaDicoIohnpLTHkIzZKw3PKaeYq4vDA2PgpP5YEbZQCnMKR9AHERPBrBJ2RqdKHDr74GsuyibDmM8Y/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**0****4**

**安装包/靶场**

所有视频教程所涉及的***工具安装包***和***靶场项目***等

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TOmGf5saFdTXDvCmMAGPdMUoALy6OgqrhoQZ18O8YnQCxk11toibkvq5MQZ9iag1qEfZYaHMwlq2YtqkmkHJy7iaMWJkwsgeEpss/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9SKrvGiaA0T3xhgdcD31dgfpm1tSfbt3SnutdQCZ40dbpD7WQsRg7o5Nq8nibLRPXX5K7CBVJhzwJ1JbEFphI4KRtb2KKlunyakI/640?wx_fmt=jpeg)

**0****5**

**面试试题/经验**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPiaKcFwOp5adPyCbWpj9JDe49cOOZ0YxAhqCQYwt0ldrKtwFeKJ8Utgw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/k50nYicZntqTHQCDW7I0r4CHr0HhOR6WPvCskTcp6Zf7awicY7eIOoIVIggCV4RQVVSiakEFhcuFF9d1BiaDmib2hQg/640?wx_fmt=gif&from=appmsg&wxfrom=5...