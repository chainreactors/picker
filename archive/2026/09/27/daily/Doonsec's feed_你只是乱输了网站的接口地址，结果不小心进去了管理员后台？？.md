---
title: 你只是乱输了网站的接口地址，结果不小心进去了管理员后台？？
url: https://mp.weixin.qq.com/s/v8px2MzDcqGkyxA4OWoEFQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:22.402941
---

# 你只是乱输了网站的接口地址，结果不小心进去了管理员后台？？

# 你只是乱输了网站的接口地址，结果不小心进去了管理员后台？？

沧海讲安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

你只是乱输了网站的接口地址，结果不小心进去了管理员后台？？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9Q91HlYssDrbUFGiaSsKsO3KyyXSYFaIcy8aYYSib9ibRmUviaBG45AGL1mrEqlEP08L1BUdXjogGJl8elFBWaqMuUvR5cT2F9dMJM/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0)

这就是我们今天要了解的**低门槛漏洞里赏金性价比最高的**未授权访问漏洞。

---

#### 一、什么是未授权访问？

说人话就是：没有钥匙，还想开门。

想象一下，你去住一家五星级酒店。正常流程是：你先办理入住，工作人员给你一张房卡，这张房卡就是你的授权，你能用它打开302房间的门。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9RP1uxpPOHu1brtMKt4CGibeMtTUYfpBdJ8r6iaiapsF6vKsZZJsQGy6YU34doNPU9prciagj80qbdPibOBwaibw0Efh9l3ngFiaDIlR8/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=1)

如果是未授权访问的情况，那就是这样：这家酒店的工作人员都睡着了，保安也不管你。你大摇大摆走到302房间门口，一不小心就推开了门进去——连钥匙都没用。不仅302，你还能推开303、304，甚至推开了经理办公室的门。一不小心看到了所有客人的登记信息和酒店的财务报表。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9R0ia2ENEbNAZf854g7tibbWiaSA5GBrgSQux3WraGDCr5Nx9wibNWpDuDOxsB3KXI7vWORFppeImEwLCibQ9tE98e9PQkQtevkjCKY/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

恭喜你，成功发现了裸奔的后端接口。

不用授权就能直接访问，这个酒店就是有漏洞的网站系统，前台就是网站的登录验证，能推开的房门就是没有做权限校验的页面。

---

#### 二、经典实战案例

为了让大家彻底听懂，我们来看看未授权访问中最经典的实战案例——利用裸奔的API接口直接看到数据。

回到酒店，聪明的你发现：房间的入口虽然放在了需要刷卡的电梯里（就像很多网站前端页面都做了登录限制，你不登录就看不到个人中心），但是楼梯间没锁，甚至客房的门都没关。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9Qe4ta6icibANkQibVeuYoHknGXXZXVDZDCFoXD3ictukArmYLLcicVB1SgEJB1XWDK1YicUuUNVKaBZWEfhLXWtHtryeX5HHvnYzbGs/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

就像网站背后的数据接口，可能都没做检查，直接就暴露在外。

于是，黑客会怎么做呢？

他打开抓包工具，发现当登录用户访问个人中心时，会请求这样一个接口。

```
xxx.com/api/user/info?uid=302
```

然后他退出登录，变成游客状态——这就好比你根本没办入住，是个路人。

于是他在浏览器地址栏直接输入上面的接口地址——这就好比你直接跑到前台，假装自己是302的房客，还让他把302的账单给你。

如果服务器是个铁憨憨，没有检查你是否持有房卡，直接就给你返回了用户302的账单和消费项目。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9Riadic4ZJyFFb2CZWmPK286CcaKibRLapSia5BFhWkz88jTf0kWhPDHXuAU0oww5ukzakn8Iv34ZTDu0LlUx68HXg2D1iaqnL6micAs/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

——也就是说，你直接访问那个接口地址，并不需要输密码，就直接进入到了302的个人中心。

恭喜你，成功走了一遍未授权访问的核心思路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CsKJlMFPH9R3rD72fVynd6pgrytibxuYPJyiaRic5diaGXa77t6lgsFnHs01nMLVrE1iazVgUibacOIuqBm1IeMQ32RSmKUlU6uUdzgMhrgm8sEyo/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

---

三、这个漏洞值多少赏金

很多人觉得未授权访问听起来简单，不值钱。恰恰相反，这类漏洞因为挖掘门槛低、危害直观，是新手最容易上手变现的漏洞类型之一。

**国内SRC平台赏金参考：**

* **中危**（如后台未授权访问、敏感接口绕过认证）：300～1000元
* **高危**（如能操作敏感功能、批量获取数据）：1000～10000元，部分云厂商核心资产的高危未授权访问可达1万～10万元

![图片](https://mmbiz.qpic.cn/mmbiz_png/CsKJlMFPH9QkWLLgg6XdDumwYvg0xz3iaXQgXtMkSibibMn28ByZEUJS5d2vxSdexkEmgNfwQj5F6bIuwibk0cmpBwYjpWsNolCcibLwgFEGU9tc/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=6)

**国际平台赏金参考：**

* GitHub公开计划中，越权访问内部系统或敏感数据的最低赏金为3万美元
* 拳头游戏Vanguard反作弊系统中，未授权访问敏感数据最高可达7.5万美元

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9TGbwopiarzgDibibYu6uIGnH5Z1GIEAicXWibTFnvKZ0zN88vu6AZ2iba2vWxRsKFS0HhjIns0g76ljy47NuImPLfLiaicibKrgtbtmiadE/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=7)**

**真实案例：**

2026年9月，安全研究团队Hacktron AI通过未授权访问漏洞链，成功获取OpenAI员工账户权限并访问内部代码仓库，获得OpenAI支付的6500美元（约4.3万元人民币）赏金。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/CsKJlMFPH9RCIUpGHIPIlQ7lxorQ8V7qUBZNUVrZ1lyV5WicVCMCp3g6nrYy6wReFtqgiaEibJyBW1hTG4nZA5icgNLNv7XkpDVdSd1BLuQ3kqA/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=8)

---

---

「最后」

如果你真的想学好一门本事，首先就要考虑自己对这门技术的兴趣，没有天赋还能靠时间和努力去弥补，但如果没有兴趣加持，就很难坚持到最后。

你要是正打算尝试网安或者想努力一次，我把这些年用过的视频教程和学习笔记都梳理出来了，现在都无偿分享给大家，需要的找我拿就行（文末自取）。

现在哪个行业都不好走，如果没有学历也没有天赋，那就只有努力和坚持了，请相信相信的力量，共勉！

**沧海专属黑客/网络攻防技术资料**

@沧海讲安全：在安全圈待了十多年，已经积累了很多的技术教程，在计算机这个行业，如果不会主动学习，手里没点学习资料，注定是走不远的。我整理的这些资料包含了市场上主流的攻防技术，不说让你成为黑客大佬，帮助你从0到进阶网络安全技术问题不大。

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

**部分技术资料预览**

**01**

***视频教程***

从0到进阶主流攻防技术视频教程（包含红蓝对抗、CTF、HW等技术点）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcYaRKqWc1cxP8sBrX6KZasFTJEVibWmdyoGAuRO4AbzaVjUJ8guoWAzQ/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcCP8oaOCQm8Cp2qhpCxWiaOjzYrOoA1iac5eSafBicPxSQcpYtchyfVvxA/640?wx_fmt=jpeg&from=appmsg)

**0****2**

***书籍Pdf***

入门必看攻防技术书籍pdf（书面上的技术书籍确实太多了，这些是我精选出来的）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcUumOTUmUznuo7MzKl1JiaEQIeSh4ibkO6jxY68zVZz7iayrwGRtGu2bHw/640?wx_fmt=jpeg&from=appmsg)

**0****3**

*安装包/源码*

主要攻防会涉及到的工具安装包和项目源码（防止你看到这连基础的工具都还没有）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6KqcvsT9h4B1hS9VEPengMcOtNL24949kb4cibKLS9HkIb1k2htW8GYqzMQ/640?wx_fmt=jpeg&from=appmsg)

**0****4**

***面试试题/经验***

网络安全岗位面试经验总结（谁学技术不是为了赚$呢，找个好的岗位很重要）

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCVGRW5LEnoxPqDicoM3g6Kqcm6J0eAql29R6DIM8bJW4rweVBicM8ibGMOmLNFTpdcQ0gFvefMTOg9dA/640?wx_fmt=jpeg&from=appmsg)

***平台铭感，拿资料、学技术看⬇（无偿共享）***

![](https://mmbiz.qpic.cn/mmbiz_jpg/kWXbooRKsCW28TYVbicW1icR88lb2fLYfLS6ib2Mfic96c3gX0VBFarDLjM2sjicYFE6SVtcyF5DHLPwyUgE4lyzDxA/640?wx_fmt=jpeg&from=appmsg)

@沧海讲安全：只要你是真心想学黑客/网络安全技术，我这份资料就可以无偿共享给你学习，但是想学技术去乱搞的人别来找我，目前全球网络环境日益紧张，我国在这方面的相关人才比较紧缺，网络安全行业确实也需要更多的有志之士加入进来，我也真心希望帮助大家学好这门技术，如果日后有啥学习上的问题，欢迎找我交流。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kWXbooRKsCUic8In0GE4Hd6nTM7iclEUG0UewS479kicpBqGcfpOAaTibhgwsEsblvqe0EsP95XKBe2E90T9g02cQg/0?wx_fmt=png)

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