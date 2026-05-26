---
title: 花了几天，研究了下自动化渗透
url: https://mp.weixin.qq.com/s/MKZO7gW22MBjrkFjqbuK_A
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:03:14.821339
---

# 花了几天，研究了下自动化渗透

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ESic8CuSnwLbiaSUwwNGbGoaGdeaKkOaU3FwR8Q0VOZhbNpcbREPrzlwmX8d67rgFcSvibtlxBkQCGxffDSccfTRA66061MbXBo0EZtiaylOgicw/0?wx_fmt=jpeg)

# 花了几天，研究了下自动化渗透

原创

xiaoxxx
xiaoxxx

稻草人安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

先写在前面，本文重点是探讨怎么去做自动化渗透agent，我的初衷也不是说就是写个简单的skills然后把所有扫描工具串起来，我是希望agent能过做到像人一样去点击操作目标系统进行渗透测试。

一年前用AI写了个工具，当时纯想着去验证AI编程的能力，顺带把自己的一些安全经验也融入进去，但是也是因为这几年的工作确实和网络安全没咋挂钩了，也是没有持续的去优化，这个工具其实最开始的构思是比较理想化的，大概能具备一些能力,想要的小伙伴可以后台私信，我会进行共享。

1、小程序反编译+LLM自动化审计，提供小程序hook平台，但是能力没做完

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLbY1Pl1tDX71r6GKaOJYyN75SzicXHzWKyXQOhafITSicKj0dDeuUJYFlBlRicwjiacvFJSt83ALX2uvjHOqD29yTPX00h43cPKTcU/640?wx_fmt=png&from=appmsg)

2、APK反编译+LLM自动化审计，内置一些脱壳的脚本和skill，支持动态调试抓包，但是差不多也就能解决二三代壳的样子，三代壳拖的还不完整

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLbJpHibib26AKJLL4RgRmILic45x5lo8TgvMuQP8IqRXnKtiaeFSbsc9xPdaXEmuxxhYwicgy7kCqla8RUoqjRjx9zcjVDH9dIIfQao/640?wx_fmt=png&from=appmsg)

3、敏感信息扫描，在此不多介绍，大家都会，我只不过用AI做了个算法，回归测试的测试数据也是AI生成的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLZbnyNEEibDsFuU303ncjSic8TgxQ3cy8UZroIDHsibKJJ1UjZ4xvXWs6359UA6lFgRzwxT1IVfcQTSOzHXk1iampbXZsnVwee54uE/640?wx_fmt=png&from=appmsg)

4、漏洞扫描，其实就是内置了开源的扫描工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLZU7iaiaLYkk7nSGvqTVfXyCictc101lIhr4unia9o5rft2ukFic9g76ibYZq8u7jUey7JcARRFOMzib0jejP7AKDZ3AL9fB9MVONpVRE/640?wx_fmt=png&from=appmsg)

5、资产探测，含web和小程序app的，主要掉用开源的或者企业的api能力，比如说hunter、企查查、github等

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLZb4W7ibV1QYHibzmth0TITQZRFQmtHywoRp2QHZxaLoOoML0ZORB75OmUeYicP6HKyXfNDNLyWpgrf7ibcAorOKUl70RqrXYWiaygo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLb4Q2kp683icJa81iaLqibNoLgABlByvPjTiaUjsH9uFGoJF9NKIJjJfyW2fFQjdcl35PJoIgUbmwoicj44Y7jAFPoT49wd8XIgJ1ic8/640?wx_fmt=png&from=appmsg)

6、代码审计&加解密分析，用的就是LLM的能力，可以自己自定义提示词

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLZlkCaSiakXRoAH3EEicIdTtviczdeqwC9CCu0TcycCF0qf7lE1v7icibwJNCmCBmqeubvuTIqUib8qsyAnwfoZibFbx8YNcib6PwJBnVQ/640?wx_fmt=png&from=appmsg)

7、解密hook插件，主要是针对加密的网站hook获取密钥，测试了很多，能力基本没问题，当前支持自己去浏览器安装，也可以在当前工具内置使用

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLYJbPfvScc4ldERtu1awic0lFAQ6FLW7RBicicJ35qPB4fewnblpRDI4k7BeBKhaDiatwsCicuAJYrbeG3xEv7cj0tvUdTBiaxVJXM4E/640?wx_fmt=png&from=appmsg)

8、还有个就是当时做的时候想着和burp做联动，支持burp发送数据包到当前工具平台通过LLM做分析

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLaBxDdLh3btjKlyN52XSa76BuESkUZRM6R7NIjGC6j4YiaVvrysibJ47rHpkgsnSyicz2HfJT7F1iaesxZvVrDwdCea07MZYVkJBA0/640?wx_fmt=png&from=appmsg)

回到我们的重点：本次是想和大佬们分享和探讨自动化渗透agent的一些思路，去年5月的时候一直想做尝试，但只是想没去做。最近刚好看群里小伙伴在讨论这个事情，所以花了几天去搞了个这么东西出来，然后也有小伙伴在使用，大概的感受如下：

1、抓取的流量不全，会漏掉很多分析

2、能力完全依托LLM本身和skills能力，好的LLM用不起，差的LLM出不来效果

3、有些点的测试还是很全面的，比人工要强，用起来有点上瘾

4、自动化渗透风险过高，不能用于生产环境，哪怕有skills约束也不行

5、针对企业内部的测试环境的系统，至少是中级渗透水平了

6、token消耗量大，幸好dk便宜

确实瓶颈实打实的存在，但是使用简单，大概介绍下使用方法和当前的能力：

1、你输入目标就行，有账号密码可以提供账号密码，会做自动登录；有验证码的可以输入一个登录后的数据包或者cookie，也支持过程中用户自己手动去操作验证码登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLaztpdyyPeiaiaxO8qZCV204DqOZef0DjMkDE7hkNeHYqcWKib4adgSkpdlI6elYPBUGdmNO4ibhrQichcPMMmWFYAx1khgvicrUnQEs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLYay7fqTFmSoyD7DZtf6wGaapmricmbvWiabB81qgXbKBeJib1Eg9HvpnJeoVJGWnzriburEYxlgyhPFqAichCfJM3icZgic7wHOUUh8E/640?wx_fmt=png&from=appmsg)

2、支持skills管理，经验丰富强的师傅就把自己的经验写成skills就行，agent进行漏洞分析的时候会按照skills去执行，可修改、删除、控制开关等，修改马上生效

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLY59hT0CkMRESvIbnXvwpiaNDqOUjUREwiackbselfyD8R9RAvaZoGQZ4aEIqic4vhSoznhXqCVxEaBuzORkGMDUOgfVcm1Khpwpo/640?wx_fmt=png&from=appmsg)

3、参考了"爱马仕"的记忆经验实现原理，支持随时“纠错”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLbXtpLxV4CkficALcydA04TTic3UXGicuDVVTIpAFIv4hczqOLFgGGLMQQ0Jgo5Gmj8jcKgxs91G00IG53rBnmgeHicyt9Mbcz7Vibg/640?wx_fmt=png&from=appmsg)

4、简单的做了个流量管理，把爬虫和agent模拟点击抓到的功能、api、漏洞、检查项等做了个映射

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLZpTwbiaoXZtLkQ8ibKBvqpNfHJU4eI3y129cDCBCIY4sCnQBfrYloHXQPibobrMXM4ZGUUKEFibIicG9QFicOVLFuBRSiaIia0JXjIVoA/640?wx_fmt=png&from=appmsg)

能力差不多就上面这些，流量方面主要是爬虫和agent自己的模拟点击形成互补。

接下来我总体讲一下整体的设计思路和实现

1、能力图（其实不止图里面这些）

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLZCG8MO1NrqvCXkhAmvj3iavSKaomsaoyyPCTkHlIia6CcmFqqIN8Llia0DIku9CPILmKpJibvws7EWkd4pq2B9h8nPG5JibTczfyJo/640?wx_fmt=png&from=appmsg)

2、整体架构图

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLbib6buISrheFcF5AMDcSDbXuwEl5YjpgXohaibiaic8xJAZImNxubbEPApfbAheFHfcj0PDIWCdeqGMDe9ysE5hT2qibHhJaXwPQeo/640?wx_fmt=png&from=appmsg)

3、agent的协作机制

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLaAwxgQDWZ8dacu4ZsxUJ5vHBDbAb6vJJQh4LRFdtZZJI3txm1MTCR97d0icx4GfBlcPfgUuGyqHHpiaZokOibMXGD7ZWlAhypeqk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLYOU1PWDCiaqPAmGiacIvaQfGiaxs0Oj9KT2icCRm3CHyCPibBrfWRjUhSibiaicjerBcHptcb9CodrISNiaowYPLoMgQGviakBhNz1VGBjM/640?wx_fmt=png&from=appmsg)

4、漏洞分析的流量的来源

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLbtDBYsQia64sUgKud8ac3On43Vnu7PtaMPC3lEePqvdmvpky13f9sy1Kib9IxFHc0Ssu9y9AXVNWDWIFycKQOXqiaQ92QLKYRiaTQ/640?wx_fmt=png&from=appmsg)

5、漏洞生成决策链

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLY4iazyY29ey2uDt2vfGI6gJK9hWNnt3uf4gytmqbVE0b4ibM2YlboCZzKa11Q3HAaQDKgBOH2oQ2ibmRzBDlRoreWicGuGyYYKy7I/640?wx_fmt=png&from=appmsg)

6、一些我认为比较关键的点

1）对目标系统业务的理解

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLb4tb5QPpuual0jIsLDk4SQ7k2c2PCXbw0w1HqQsyVDV6Ul2DdKDTzO2mxUz64zP2xlCEDVFXPLUwIyOackamciaXYicuRWyyY4s/640?wx_fmt=png&from=appmsg)

2）agent的爬虫流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLaUJLkHhqClIaTNxZ2mkibJcpIdudPriatlbsiaTS8jA2xSXUIp3QkOo7qv82vlswnkLblhichoSePOf61lNze6g0pYLGvHoZmqqU8/640?wx_fmt=png&from=appmsg)

3）智能并行调度策略

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ESic8CuSnwLZZEvdibibQiczHfiacM0HPFicjtaGE42cwVrSZ0eqUlJDsXfOeWKKFWyOrN7Jkp96kXM7IWE8yVt7UibJueocnX0bl2Yt8H86vqaf7E/640?wx_fmt=png&from=appmsg)

4）漏洞发现到报告的端到端追踪

![](https://mmbiz.qpic.cn/mmbiz_png/ESic8CuSnwLbSRun7dZNQicuX6V2Foaro4dKjYoSK7rMfoicY26fArqYbAdBBdHoGNGmIbUd6dghTfV6t7I4XHfYuicQbKaw42nauEYjB2UhPlI/640?wx_fmt=png&from=appmsg)

细节点还有很多，最核心的能力点就是要解决怎么保证获取的流量全，靠爬虫是远远不够的，主要还是要靠agent自己的模拟点击，而这里取决LLM的能力。（省token、降幻觉等问题我觉得当前还好）

在开始设计的时候我就想了要考虑LLM的能力问题，要保证能力一般的LLM也要能够工作，实测dk-falsh和dk-pro，同一个系统，用dk-pro抓到的流量和api计划是dk-flsh的一倍。

以上就是本次的简单分享了，欢迎各位大佬一起讨论，把当前的遇到的瓶颈一起讨论，也期待更多的开源的自动化渗透agent，希望通过这种方式能够取长补短，把能力做大做强。（考虑各种原因，暂时agent的源码不做分享，后面会分享出来。）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gv0KFFo8icCQ46wOibrGtlon3gpFl1P9UTpia0Atia9icu3Jffkq7WQWrMKiaQotCOJu3ye0ZV1H0SEwbn9w9tav05RQ/0?wx_fmt=png)

稻草人安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gv0KFFo8icCQ46wOibrGtlon3gpFl1P9UTpia0Atia9icu3Jffkq7WQWrMKiaQotCOJu3ye0ZV1H0SEwbn9w9tav05RQ/0?wx_fmt=png)

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