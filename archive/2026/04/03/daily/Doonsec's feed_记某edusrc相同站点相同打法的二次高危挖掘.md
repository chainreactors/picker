---
title: 记某edusrc相同站点相同打法的二次高危挖掘
url: https://mp.weixin.qq.com/s/0P2-L6acwNt5fyrjOpsB0Q
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:12:38.637475
---

# 记某edusrc相同站点相同打法的二次高危挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboTVS5dtfxLL5icrcCKHjvRpcDK7MsVDcwbvU53PnUwAnRvkTLVHZBnr3q6mpvhP28mIGFAohI9EUg77e2icMK7n0zzVW1wiar0S0E/0?wx_fmt=jpeg)

# 记某edusrc相同站点相同打法的二次高危挖掘

原创

陌笙
陌笙

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

**前言**

```
接上篇文章
```

**漏洞挖掘**

昨天不是挖到一些东西，可以看上篇文章，既然是挖掘edu,肯定是要找通杀的，既然找通杀，肯定得看，网站的根目录，一般资产测绘引擎都只会收录根目录，下面的内容。

进行访问尝试

看到了很多接口，而且还有解释

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTBWwEGrN6IJ63jgbY2c6Xfe9PnAgHibfWpHUbbRBLyFRBnz9rOvPIgSmNRbeyibicR00JDoQGphstZGx0zcwnibCTrdCcGy1mljBk/640?wx_fmt=jpeg&from=appmsg)

不急，先找根目录下面的东西测绘一下

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboREIXk73xGdib5qhh7cWrvrQKUoVzBNJ2OMEkwtRKt0LN6J0OAsTFHStRwbKsTqUdUd5upt4s7ichprGudrQj3ZHibtH9r2l957E0/640?wx_fmt=png&from=appmsg)

只有两条还都是一个学校的，没法通杀，其他引擎就不截图了

回到刚才接口那里，继续看解释

看到一个登录接口

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR1kdlgnJKSnGIIm33WibKmq1Sll3GibuJUbYGnRZNvquFupHPDMObaegFCZ3gVzhnhCvHAIvjxtLKyUanRRpib3rK2vNFclQnyxM/640?wx_fmt=png&from=appmsg)

进行拼接访问

发现了一个登录口，使用上一篇文章的方法，拿到的账号

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ1oodz3w9cdzdNfGeDrJXAXjhHW5co8RL2LKJiaLfYYM6stoPADGaRCibUibA1iaopKDyMwMuqzq5NyRjpWlBXxcE3EnMS7Jd2ichM/640?wx_fmt=png&from=appmsg)

尝试登录,登录成功但是后台没有任何功能点

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQRF5RichuXHsXUpiamORMC9KIibKNv517Ih9wzV2YKZlSsEwbm4SfxC60b1C4nnBmM3dDIkRjFHza3pl66bM6FyHyHcKu6iay2FDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQSQlZtDh9YUAE3B9ANB2yRP6cEsDLVbfsFupq8wtFwibL4iasdYF7Nff8189awLxPluPlvHE9CoHEWhDXOyojwlxGk6LqGsOzHI/640?wx_fmt=png&from=appmsg)

这里我直接看接口

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRAkiad7URybsHptrPKplvNtwGJDMwUp4HknILIo3tmWwxTj1fIAOoicv0Zm1g5sXeOMqbU1yXBRicibkb3VLkj91WmVibL5Seyym8s/640?wx_fmt=png&from=appmsg)

然后开始点点点

发现了这个

https://xxxx.edu.cn:7101/#/xxxx/library\_door

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTVKWIzSkknr03wiaOE2eicAicejpicfnvmY8ib6SUZsvCRoibqaCzbicssVoOichuhRry8sFlcY2Vc0TiazzKibZJcPACEsicOwbOpt4WP2I/640?wx_fmt=png&from=appmsg)

看起来没东西，但是点击新增

可以看到14445条学生信息

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSYxJDXhyUa9jnCu4icsnHTIbPtgZjL1beJmxdFYIQicY1icWvoPbPoRvlj1R5xUNDvHJHVvGib7CLIDP0R3LkzwrIpgGuRjegU8ww/640?wx_fmt=png&from=appmsg)

切换教职工又泄露了1973条

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTAPg0ZAeDojsa16djeMGEXVCibw8X5hGyXAN000GpDVoFYx7dXBIjIjJuuR4z56IlfQeVXnsOg9OSlNFRlrmDfYAAALS7vRJNI/640?wx_fmt=png&from=appmsg)

他们这里虽然只是泄露了姓名电话工号啥的，但是他们的工号是可以利用上篇文章的登录接口进行登录的，账号密码都是工号

继续选择访客可以看到泄露了24448条信息，而且有sfz

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQicaMWpWRunbfAFtZkvZNXicg69qwkpicicfzva1XsxXn2KfnAvCp0eGnAjuJYPcyxLGTE35pLubwz3hwATnCpS0nkaGQHxGxKMw4/640?wx_fmt=png&from=appmsg)

不仅有号，还有大头照，这个哥们，更是直接用这个进行申请

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQl2BZfVw7iaYXABuxhqYT0XuTOdGscgYckdyZnSnibz4OsPl5sq4O30x4BcdvAFq8tyDL7iamK44SjmqiaSoqKcz84p11F1mQ9O6c/640?wx_fmt=png&from=appmsg)

ok这里我们其实就已经，由弱口令到越权了

既然是越权一般可以交三个接口

继续点点点点

https://xxxxedu.cn:7101/#/xxxx/list?is\_all=1

发现了这个接口，这个接口对应的东西，更多

直接3w多条信息

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSNhF3hj06UGP3OwicXcvQHfh49nhxggnH5Z48OOdsGyibZlrqIvTQjMeeMIia5OSvdkY1brJJwbTQj1NRSQfkKrEW782Kia8p61OI/640?wx_fmt=png&from=appmsg)

而且都有身份证

且可以进行记录删除操作

找一条过期的进行测试，证明危害

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTG4Phudx6iaL5O0wEybMzI3J5tZzr5ua6b8DmwceqibaPqewIYwz0poBic7owMad34fVSTg8mpNDbUmxv7iaU3KgvwW9VSbhc1mLU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQuKtmQmYqDFsz8POe1ERJ2vF8sT2mEhXzKTELqv4H09BbovYnyhOrHiahZxl3pXibcnmLrVt9snozEHU2fmxIGICuupavbGlpJE/640?wx_fmt=png&from=appmsg)

然后继续，看刚开始的接口

发现一个新的登录框

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTb59Ey08wu2AGCEcic31gzeFlaOnmovO6c1iclSayGx3ASwWr8W1MCaicmD7JsLX9S0ekDOBjsianiaSnrNtDMBzy3okR65njyXcZI/640?wx_fmt=png&from=appmsg)

测试短信验证码相关问题

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS9ibxia4icfE6S9jS4liaBx9hNFicFXnQe8KdMN4D91apJUhhWN5E2hFpnStAnSIZPnNVXJVtsDCBzwyUhZAIxncgM0ib4BbyWq4KoI/640?wx_fmt=png&from=appmsg)

这下真有了

点击获取验证码进行抓包，发送到重放，可以无限获取，验证码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTZba29AXAo1U0gA3aQByOyZttPWoiagfqhp2FW0ZZFXkM732u0n0aSmiafHiaK13Z6bJaXjhU3sic54FzMmOMnVaJ3cwrqyqAjGVA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQtNho1w8JEAUTdQ7iaOlcDJZVHkicia5EPCs2QNBbEicStd5PB3BiahKPOtCNUiapeF9A8YrxibovSNYKIScQacib3Wibv59mMmmzKlSkE/640?wx_fmt=png&from=appmsg)

还有一些导出的接口以及其他的可以利用接口

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ4Qt2v8FhIWfTDmMMyG1s0sdtGzXdY6zJ8frDv4KKueoxibyvgzABxALjPP1JDiaSibibiagXjicaibg5DRma3gojGg4zkfeOPibIhpQU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboST11ObLiaRdgVdBDtndkMQooPt8dSzm3X0l1iaYCexfumcicNe4bGIOXy9RibBIHcu3oqlRAdaQ1Ymcqok3ibAYCySSu2FcWX2zygE/640?wx_fmt=png&from=appmsg)

依旧泄露一堆，这接口也可以，操作

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTS0F2eCan6U8IY4zyZkIN1BNrcmKCiaz0kqulia2wo1Maia1K382Y19uYGNfaclP8ol869iaib9Y6PMoeYFR4NU5ibLuQV43QtS40nY/640?wx_fmt=png&from=appmsg)

显然权限是比我们昨天访客等级更高的

继续探索了，看能不能找到管理员的号，梅开三度。。。。。

总结

细心一点。。。。

**后台回复加群即可加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子的价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

漏洞挖掘**1v1**指导,我给指定站,你测试之后出报告,我根据报告总结你不出洞的问题,以及看漏洞点和总结，当然你可以自己找站，我来帮你完善总结思路。（思路为主，主要针对小白，大师傅就没必要了，主打性价比，帮师傅们快速提升，挖到第一个**edu漏洞**，纠纠错误，找找感觉！！！）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRy3HPbHnToDrxicuGxBenqN2KMsnia6piaVqwQqWyYCXAFl5bicKuuxODtANtHHS0QxxAtUicG8rmrCSJL0SS7SGBibaTLSuNic3KcKM/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中）**

```
信息收集(会永久提供fofa-key助力)弱口令漏洞任意文件读取&删除&下载漏洞sql注入漏洞url重定向漏洞未授权访问漏洞挖掘XSS漏洞挖掘等等常见漏洞EDUSRC证书站挖掘案例分享SRC挖掘实战针对各种常见功能总结的常见测试思路等经典常见Nday漏洞复现等各模块不在一一介绍
```

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSWarKnFiaUicnq701hWQaiaA94FmgLNE8SVmrJiaJwluiavCE2VRvDV3ZYnwhib2pSNEpPp3Qp3beicPIAsVs3dS4A2MoYQXcsticwlqQ/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRD8gJdgFicMTaYcSMHydxPNJvagOaOrNbrM6S2tDPEcmjyECKacjmNJBCtwGAKMNdMes7tztJfWZGqjKxC7tkg99v4uDXDTpSE/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRPAemLYYSWRsc2cHYkwwxQicDQNf46MY8wUetFibPmetZdkicr4BNvPF0cBibqyS9emwayFf6njw9kjvBvWLoFDQJY5JQDMSUqh4E/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSxdcm5nYOYib6RQ9icEbL24CEdgW8picdlKScbf20oibpwVYewMyuhgZz1RMv7Vib8kr73PvErOKEm3MSEcVslJNUFEJ3OcDHXibKKw/640?wx_fmt=png&from=appmsg)

**陌笙****纷传****圈子介****绍**

```
1、src挖掘思维导图，信息收集思维导图，edusrc挖掘思维导图，以及后续的红队&面试思维导图&自己网安笔记等持续更新2、2025-2026的edusrc实战报告包含证书站和非证书站以及2025之前的各种优质报思路分享3、各种src报告思路分享（内部&外部）4、分享各种src挖掘&edusrc挖掘培训资料&视频5、不定期分享通杀、0day6、有圈子群可以技术交流以及不定期抽取证书&免费rank7.分享各种护网资料各家安全厂商讲解视频&精选实战面试题目8、各种框架漏洞技巧分享9、各种源码分享（泛微、正方系统、用友等）10、漏洞挖掘工具&信息收集工具&内网渗透免杀等网安工具分享11、各种ctf资料以及题目分享12、cnvd挖掘技巧&CNVD资产&src资产分享&补天1权重资产分享&fofakey共用13、免杀、逆向、红队攻内网防渗透等课程分享14、漏洞库&字典以各种内容不在一一说明15、cisp-pte/pts&nisp一级&nisp二级&edusrc证书内部价格15、如果有漏洞挖掘问题或者工具资料需求可以找群主(尽量满足)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSY2pbvbP3qGAlW8O43bRvAISCxZm4UDTRsaMVbJKTsjfTMTDlq6qNBcVs4tkl4UzgqGz5ag81baU1rusKE09J9T6cMVliaibibwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTrLRQpTicOR7bzyNiajiapVJgyMiaYlEDBVU87YXMnanOFWsCYN3cCVGsKkibzV9dMryvbFXBb4Z3472ib27RJ1Xq1HnKJIp5u49GYQ/640?wx_fmt=jpeg&from=appmsg)

**目前620多条内容，扫码查看详情，持续更新中。。**

**如果觉得合适可以加入，价格不定期会根据圈子内容和圈子人数进行上调。。**

![](htt...