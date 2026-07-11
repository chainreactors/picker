---
title: 5步带你从0开局拿下漏洞赏金！1700讲透白帽src的所有核心基础和赏金思路！
url: https://mp.weixin.qq.com/s/LepGxY4j_gtwHcT_rm7PSw
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:58:24.947761
---

# 5步带你从0开局拿下漏洞赏金！1700讲透白帽src的所有核心基础和赏金思路！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9SDicepzxjMODSOnyEznVMqjia3bNQYepWziavHqX6tD2OiaJRBs4m87fsu2uIpgicJW71jicMzdXtOI0l4bZbvfXAgoUsZcib7w9nB68/0?wx_fmt=jpeg)

# 5步带你从0开局拿下漏洞赏金！1700讲透白帽src的所有核心基础和赏金思路！

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

你会选择送外卖跑滴滴一天赚200，还是选择坐在电脑前花两小时拿下一笔漏洞赏金？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Qq7qgtMTr8z8vBA45yWfqQ3kgZTr2slCvRFUzkZFEbE9pj4Bh2bPZbgpL3WvPFzYnRXLC0kqX5ujxpicSGO883nAvxnUunb3VE/640?wx_fmt=jpeg&from=appmsg)

不是说你不行，这中间的差距其实就是信息差。

接下来，我把从0拿下白帽SRC的关键五步给你完整讲透，但凡你真能听进去，拿下第一个漏洞只是时间问题。

---

第一步：先治好你的代码焦虑和工具迷信

这是很多新手的误区，其实挖漏洞前期根本用不着写代码，也不需要你去死磕一堆复杂工具。SRC上大部分能换钱的漏洞，靠的是你找问题的思维逻辑。

* 前期你只需要花两天搞懂浏览器是怎么跟服务器交互的就行，只需要明白什么是URL、什么是参数和cookie，以及get和post有啥区别，这就够了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9QFcxl84bQ5Uzej1iaUSX4ict1jTqfnePkCTFO9g7yC8mpHQNbM591aBl9OJ9W5ic3nJ7wm7r1R1FOZia5VyCrMeZ3ZEPMYkUOrSgg/640?wx_fmt=jpeg)

剩下的边做边学，别被那些专业术语吓跑，咱们是来技术变现的，不是来考研的。

---

第二步：死磕两样核心工具

学的多不如用的好。

* 一个是Chrome浏览器装上FindSomething插件，主要用来改改参数；
* 另一个是BurpSuit，前期的重点武器。等你配置好以后，可以尝试用BP截获一个请求，然后修改参数再发送，如果服务器返回了不同结果，你就成功了一半。

![](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9TncNJROicOsyOxedQLTonGIeX8zibBRzMt0KUP7q9UTqvE0DMEuoK4sHK1ynWe3yDB0iagrg9njxcWSK4mvCM3nEEicQXIrWs0Aa8/640?wx_fmt=png&from=appmsg)

---

第三步：搭建本地靶场练实战手感

先玩DVWA，难度调到低和中，把里面的SQL注入、XSS、文件上传每个都手动复现三遍。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9RMbTNwH4MibVozEYkJUaVIHPcfQ7b8F5FDIibclVkXzNzcusuuzJfL7Rx74sk8DIpsx7KJRcH3wgva1PeQ78ITG7wLqTax7uNII/640?wx_fmt=jpeg)

注意是手动，不是抄命令，你要搞清楚为什么这里能注入，每个payload的作用也要铭记在心。

搞懂了原理再去玩Vulhub，里面的环境更接近真实业务。

![](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9RxnQ5TXj4ENKQkTQfmpH4aT5HXYPCseTmrym7icKaYOsVvqevOIR8U53Aw77jw8Ton51VnSJ3ZZX5Z7d9j4kkSIb9HKzibjf2KE/640?wx_fmt=jpeg&from=appmsg)

这时候你可能会很挫败，明明教程都能行，你就不行，多半是cookie没带对或者参数名拼错了，不用着急，调试的过程本身就是在长本事。

---

第四步：尝试挖真实的漏洞

平台推荐补天和漏洞盒子这类众测平台。

* 前期你就认准公益SRC，虽然没钱，但能攒积分、熟悉流程；

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Q6ZErsg4LY23VKsTg3mdfXIqeMTVCRQsicYBDhWhbEC9oJlMFIKxicL2wyqhPUuYre3XQWMHa7yQvhpNiaLYorHoLLt5V3MxicAb4/640?wx_fmt=jpeg)

* 或者去找那些刚接入平台的小厂商和排名靠后的企业，他们的防护相对弱，审核也没那么严，别想着一上来就盯着阿里、腾讯这种大厂，那是神仙打架的地方。

哪怕被拒收也别灰心，大不了多改几次再提交，这也是漏洞提交的关键历练，新手普遍要7到10天才能整出第一个有效漏洞，别着急，这将是你赏金之路的开端。

---

第五步，专注能拿赏金的漏洞

至少要把八成的精力放在逻辑漏洞上，这玩意儿不需要你懂多深的代码，只需要你像个刁钻用户一样思考业务流程里的问题。

* 比如越权访问，你登录A账号，不小心改了一下ID参数，要是能看到别人的信息，那就是存在水平越权漏洞。整个过程可能不用半小时，拿一个也能有300到800左右的赏金。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CsKJlMFPH9QXhh75Rnb11CqFNCAAfksEhkcp0UibP1PicyWjTn644rEcAfiaNlCmwyia0AeFdP11PAVju9AC9DBrWblRGqx8fPZz4zgOVcLX3PE/640?wx_fmt=png&from=appmsg)

* 再比如密码重置，抓包看看能不能跳过验证码，或者验证码能不能爆破。如果能发现单个账户可被重置，赏金就是500到1000左右；要是给你碰上任意用户密码都可被重置，那甚至能到5000。
* 还有信息泄漏漏洞，试试在域名后面加些参数，说不定就能捡到漏。虽然普遍的信息泄漏都在50到200不等，但是剩在量大管饱。

这些漏洞扫描器扫不出来，全靠经验和积累。等你把主流的漏洞案例积累足够了，每个月出个四五千都是很普遍的水平。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9TSB2XmPtC69TpwYLicuTgXpCaXL3gUDcibtohZZicRTorI2HMdYE39QiaibzqWOVAw9hApf34x0mo6ia0axgiaA1ibRH5RpAvfTlxSNMs/640?wx_fmt=jpeg)

说句实话，那些成天抱怨挖不到洞的人，不是光说不练，就是一些基本的漏洞复现都没有亲自去跑通过。

你要是真能跟着我这五步死磕下来，拿下漏洞赏金真不是件什么难事，干就完了！

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

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/k50nYicZntqR4H6FKAtmlHiawLFfTaYRrF5VvoZNx5u8soCxHxq9s1Pem6MbcqeBP9e54DaBsxia1YicvHeGJibgShQ/640?wx_fmt=png&from=appmsg "un...