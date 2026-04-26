---
title: 985–edu证书案例之有意思的报告
url: https://mp.weixin.qq.com/s/UgPglbf_I7jhW-DCpEKXXQ
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:00:02.496017
---

# 985–edu证书案例之有意思的报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EuISttNu98kVy8sAXdgBAfovmTFueJaYuBV6tO0BG04qk6ZQUmF5GlfV7XsMcnynwyJVn79PXo7v0X7Ir2hSSt8WicgjZ2v305E/0?wx_fmt=jpeg)

# 985–edu证书案例之有意思的报告

金陵王--黑子哥
金陵王--黑子哥

湘安无事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

## **前言**

故事的开始也是黑子哥随意出手（ps：黑子哥是src大牛，而且单身），准备帮团队做点贡献，于是乎瞅准了证书站直接开干。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tlibgKYKL9EuraIRiahKIpaJXzoJicusrRHiavVkIr2MHH3ggKfB0Crhbs72wJ9rRTOmxuzvaX6tsZn5noyiaxwtFrJecaD4Yia0pVYHe3KengPME/640?wx_fmt=other&from=appmsg)

## 信息搜集

信息收集相关url，此处一定要注意各种站点都得看看，有些302的搞不好跳转去薄弱资产:

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EusE1ibWlW08KjWtusDCzRmf3M6fCeo3bhplxib4MKeploG8rzMNcV8kklzia3XcD5n67CwUn5vsn1NTHmCKolPN3drx9ksDMShqw/640?wx_fmt=png&from=appmsg)

通过信息收集，发现一个测试账户，test\_app 以及该账户邮箱test\_app@qq.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtEJhbZkDUa8EhJ0Fjvpwe9yb5mSrBQfpkyticZj8TVoACU8IzRh2PNzBHT0fJDCmFaXiabDwCRA6yEjQj0icbCPurF6l5VfumKl4/640?wx_fmt=png&from=appmsg)

## 具体挖掘过程

edu挖掘过程一定要瞄准大批量信息泄露、越权、sql等危害等级高的漏洞。这样给的分多。接下来就看黑子哥装逼，如何拿到其泄露的信息。

这里我们点击忘记密码：

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvtLibcWgTGyAVGdibUujxJXa7Kf07ssmG7ricbUsW5S9zpyibMW5Wl5ekJ5EvWa9QXw90ibugmqFLbbK4deezcuC6gCzJ2wQ7nUAwA/640?wx_fmt=png&from=appmsg)

同时把自己的qq 设置为接收密码的邮箱：test\_app@qq.com

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvMoaCYxUdia0HWRVYaCicS345ukTr4vQRI2GQCsxsBfibYiaY1wTQDCia1ricriaeZVbLPPvW5jHVZzuTJa0ST2Htv1M4zKXPGdiaw3BI/640?wx_fmt=png&from=appmsg)

点击重置密码即可：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtS5NZOfF2js6xuLSvTy5K02ZUSnpyhmCtoEsicedfonegcNUzzTHWm0NbJKZgnX0IQy9zQtLGaMzhebkT7PP9zgzGrC58pHfng/640?wx_fmt=png&from=appmsg)

这里看到邮箱已经收到重置密码的邮件了。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Etic2WEbEp4sgKQVlTiahLADoYPmJfD6sXxV6ubMnHlF0BibSGYINerfQpWfRAG9dIl7uW6mccBUOoErfLeHqJKB3oTAzQnnFHRPI/640?wx_fmt=png&from=appmsg)

点击重置密码的url，即可修改test\_app账户密码。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsuWxJJsW4TAsX0QdDWyqzqA7ZoRTzqEasopu6iboZGniaF3EAOEb45xs4QZ20nWsqb2dM52SJqiawJ8jvcpbJfQqib4ic47sic56Fto/640?wx_fmt=png&from=appmsg)

将密码修改为Test@135!

登录验证，发现泄露大量教职工项目信息：

这里泄露近2200个课题组敏感信息。

这里有导出Excel 高危操作。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Et0Iuo7jF21D70ZSaicfNcQBXe0RSiaD1ru7p7LBUpMIVMDfCc8QG2lBpzrdRicWyQXTjtBntVSbSPuPjOPibrmUKAQMNpP0Uvf0Qg/640?wx_fmt=png&from=appmsg)

这里的public为公共文件夹：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvLgicCGEpUlud0AeDK6d7j7pomqAtWk9ocnwcniatQneckM4FichvdeDyRN2soyYJPx3k3X5ZUooa47zgibfBxvRppeiak8VcvVDSo/640?wx_fmt=png&from=appmsg)

可以利用test\_app进行【增】【删】操作，危害较大！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Et7x2amHpNiaYs0KLslS3Ol4f72DejiboFkotmaywkC0bQl9Fqv0G929JUrIwYKkG6kcibNhVZrS2tAJQWGUb4SCZiaiaxiaYrM9WTng/640?wx_fmt=png&from=appmsg)

点击【文件系统】点击【public】：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Ev7Rg1vJIIyHZJRr381Hd4InFXXpLbicEA3awASnYwD3HyFn3JLHp0JUcEEhvnMtgmJwicOSuicyqJmjfL86FIZ1TfXoRYtRjdejs/640?wx_fmt=png&from=appmsg)

下载完成后，以txt格式打开，发现该文档泄露大量敏感信息：

如数据库名，版本，以及内网真实地址，同时泄露该网站所有用户密码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EudYCibJaic2ia28ZAwopD7Tgd4J5gaWGYn0ZVwqazXWS6wib0SNvtUD4Fibtj83XsWFrViceiagOc63QaJGcqnRGwAb6Kj9EsonSXcOU/640?wx_fmt=png&from=appmsg)

相关配置信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EsZGlVpxiaHiahZJWF85AD42kC0UAgCibc5ibXNicpib1hhTuFVh3FtxJPxRWGS10fRGdcR526QFSKaYJVYWr9qBMUlkSAh0nO7FaGu0/640?wx_fmt=png&from=appmsg)

相关表信息：

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EsJIPSQPmSEQVB9scTo9D5fePVtzoGndrLRhia5bZRHY4jHibZiabNQNN678xfAoPxGxvWszHiasnguRTmPfMS6NTuOv8AbicQ74zGs/640?wx_fmt=png&from=appmsg)

用户密码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvDNVrpH7P36ylkQznV2xZN5budFOMguia4ye1H6B0evP4jhJSmWnl7x3gFfcQ8ib1373V8GWnTKibIDXry1wyQPohPLK5aLtiaslk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Ev9lQwOQZsj4g09vvmVqBXurCK2nxQiao9ZPtjLMrUwbfhCFWfWb8oymCdc0WfJJicjiayvYGkB7xibdpvx69kDOe1ScGSSxH62De4/640?wx_fmt=png&from=appmsg)所有用户，注册时的手机号以及邮箱：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvBWatPAQZUpIEFZJEia7pLdoAjQpFLCjia8evKvylxdX6kJHZ1upliatdCKz9H9FKlFGTot3LnpTuqqgMYkB7bghtPvjDNib5iaQibw/640?wx_fmt=png&from=appmsg)

至此证书到手已经是稳稳当当了，灰常感谢黑子哥漏洞分享，听说最近黑子哥在憋大招，关注公众号敬请期待

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtlVUIOoug0avz63hXfsAb9e647utia17ralrsvztLibp6n9OdXvyhPMSOHvibcbQianOftfq3sZqj2l4OBF6l7QicMH5skibSZDYnso/640?wx_fmt=png&from=appmsg)

往期文章

[记母校漏洞测试一次waf绕过经历](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494963&idx=1&sn=a3402602ab048ef32c1bc7f36d702dde&scene=21#wechat_redirect)

[Codex-AI 道德审查绕过进行js逆向](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494987&idx=1&sn=7344cac0a26228596f0e267793aca865&scene=21#wechat_redirect)

[究极无敌的srcAI-xss手法（快看过来）](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247495003&idx=1&sn=fcd19fb5f7f950a3e7a15785577cd738&scene=21#wechat_redirect)

[记一次差点进编制的漏洞测试](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494898&idx=1&sn=9f9c5a3527c8330f2e4312eadf0ce863&scene=21#wechat_redirect)

[新版微信强开f12和新版本微信反编译](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494896&idx=1&sn=ac8ebcaecd5e18d45f79c7b6d8e3b10c&scene=21#wechat_redirect)

[湘安无事2025团队和培训总结-福利抽奖](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494849&idx=1&sn=a7084a23faa401c4fbcb06af4650846a&scene=21#wechat_redirect)

[985证书漏洞越权成为教授 + EDU/RCE漏洞实战解析｜湘安内部平台月榜 TOP3 案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494786&idx=1&sn=9ee660a005413f34e6d89f728df59803&scene=21#wechat_redirect)

[服务号存在注入之有意思的edu漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494659&idx=1&sn=e357db59d806c93f3a5a36b5c312b335&scene=21#wechat_redirect)

[湘安无事之湘潭大学冬令营总结](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494727&idx=1&sn=1d17ba9ee9bcd5fc4cfabe12d463e4da&scene=21#wechat_redirect)

[赏金src报告分享&&edu证书站漏洞分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494759&idx=1&sn=65084c580bb13fa31f82985721147e7e&scene=21#wechat_redirect)

[edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494702&idx=1&sn=5f0d05b6bea8550eda36ed2ce8ddbf7a&scene=21#wechat_redirect)

[学员投稿之edu漏洞的JS逆向解密导致任意密码重置](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494634&idx=1&sn=7cc83a90badea88d7d7d25583bd0c419&scene=21#wechat_redirect)

[最近学员小灶总结之双十二特惠](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494604&idx=1&sn=80f030c8114ee3287036586c670289c9&scene=21#wechat_redirect)

[卡顿页面导致三本edu证书现世之学员案例分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494572&idx=1&sn=14c21f1cae87dbdbf2ca5c4b10533f5d&scene=21#wechat_redirect)

[看完这场EDU通杀刷屏，连我自己都沉默了](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=1&sn=113dd5e17065def94a5dacad361176b3&scene=21#wechat_redirect)

[edu证书站挖掘之学员分享案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494524&idx=1&sn=bff39f27ea27bccb884e832603acda92&scene=21#wechat_redirect)

[如何快速挖掘低微漏洞-项目挖掘总结版](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494500&idx=1&sn=2da7aa0d40075b462eb27695f2da9e83&scene=21#wechat_redirect)

[公众号接管漏洞之偷偷加](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)[小姐姐微信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)

[辅助学员审计案例-php代码审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=1&sn=2feaf2786717c2c577fe0b5230cbc58f&scene=21#wechat_redirect)

[学员-补天800赏金报告分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=2&sn=c54ea91e0b3dc79f48f54f931df413c0&scene=21#wechat_redirect)

[从js逆向到sql注入waf绕过到net审计-edu证书漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494171&idx=1&sn=0d589d01dfbb068e53f9ad9c22676d7a&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞-再次绕过](https://mp.weixin.qq.com/s?__biz=MzU3Mjk...