---
title: edusrc小程序通杀找找资产方法
url: https://mp.weixin.qq.com/s/9zF0VlC1ngBPndlm7VKYeA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:34:07.204394
---

# edusrc小程序通杀找找资产方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQYmp8WEfCMJmtQx1icqM1UemjPdZJGDIjic2SibNKiaCicrKkBcZelY9hclRPF15zA7BpFDlhqvIcuAEn65vXOTWKaHHV93iajUSwJY/0?wx_fmt=jpeg)

# edusrc小程序通杀找找资产方法

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

漏洞挖掘

依旧小程序起手

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRQJTRJ5OFP11Ov4fv9DQR29HlVOfBGqObHOGsuGiaytV9KOfyhenia5LNUz6AddnIF935a4dyyuvJok7pXrhXaUqgbROSz0Ppf8/640?wx_fmt=png&from=appmsg)

点击水电缴费，直接来到登录页面

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSN9ZBawtejV2g2TWcN0Xxu45PnJJWLG29qxx1IO3zXTr2XbibSZ1wxBPviashgyNV5Zd8ibpiaHR6O2JjlJ7PicFaWibLGhvxbfzseA/640?wx_fmt=png&from=appmsg)

常见登录框思路

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSjbsGA91nDYIBwFlrjiaxrF2GeaboOWu8Qtmng58KicyznxyCatAnuSMvxibSIficTrYTzIMfTyyMcKlRsqIqfE7Be6O8GprYDSxs/640?wx_fmt=png&from=appmsg)

随便输入看看啥情况

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQlZC23et7uLTd1EcnfFUc5BKRUCfgibrKCv6v3OkL1YAAFib3FI6NiaQiadkTmp2WEiah4icxzgJdvPvsNLJVduuTAXm3OjEPU23NnY/640?wx_fmt=png&from=appmsg)

应该是存在用户名枚举

固定密码123456对用户进行爆破

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRP2HfAXwQvnNsvRX55gBwaR9ibBkcH6TvSsbbpZH7ptbcMZcGNribPjMvFvfeQNJQw068VopSJsQUrs7ym1xAicLa8dldJ28iadr4/640?wx_fmt=png&from=appmsg)

根据返回长度进行判断

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRMafH65C1O3AeZD0JSt1Tv3W0YSqajaXrpUWuOCytia4QrGX8ZpF3OKpiaXjlnicW0bVRELzFDU8L2Vxroh8fqQuO5pC00zxrNHk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRyATZzJFVVibVicDqYD9y5JErMgeGlDLUq9VGY4777rosE3FWmI0bYsHngXbxyUQBCa9BPxOLupMUSTjnZhL0LhoLIlvjHkP0wM/640?wx_fmt=png&from=appmsg)

成功枚举出一个用户

对枚举出的用户使用top9000密码进行爆破

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTVd6dZ3H0F1bY2gHuPLsf1ibIJek1D0V3rrzshDByicupZNGtwryxicGPbcEx4rjZgEYHbBOtn4PyZMpsaQd8aVfteH00rSuQ3Hk/640?wx_fmt=png&from=appmsg)

根据返回结果也是成功爆破出来了密码

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSntIqlInhiaEsRxZJI5KfgicZ7MErgliaTOgsmCy7GowHeFAx1Qdlmibg5bG63ibXIg4GiccWicXNxLyV7yRjic7LGIfKW7ZhAhAFUmRM/640?wx_fmt=png&from=appmsg)

使用账号密码进行登录

138xxxxxxxx /000xxx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSNCzt25BJyVaHROTstLmHmGJOicEHs6I8JGibB4qPJP2yZOmy7XOrlic87hRsS9O9Giaibh335XKL7P5QicEfMwRh1ORy60ZfND8JWk/640?wx_fmt=png&from=appmsg)

成功登录别人账号

对后台功能进行简单测试

发现有越权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTTFuSN9I9bLYSZlJzhSY918Jf3Pag7FCf9oPRnTGgYDHN4UbAeQSd1aQvrQZ6Fg5S8SeLchfhKFTz6jL415wgq2g4cYicjVmJ0/640?wx_fmt=png&from=appmsg)

通过遍历usercode可以查别人的账单信息但是没有铭感信息没啥用

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRTOrb1tDBibzCYFnrW2Dm4IibxIclhAsxU4TwRrNqP7LibLFVNLYP0v3PiaCydazicGtGI2y27nccmkpoyWZQMfm4WMXc0Od9kWcvc/640?wx_fmt=png&from=appmsg)

没发现其他漏洞，但是账户信息这里可以对用户密码进行修改，多少有点危害

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQQrf3QMTT8aaYxB6cMpvD6ib0ee1bCzm4t89pW0GtvWPtFxCYs6VKAib8ib5ZCQT19kUCsfHWRAicbpsYaQbU5Uv56yiaBj2qZ50X8/640?wx_fmt=png&from=appmsg)

测试xxe相关漏洞,这个没怎么打过，太局限了。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR2SOhYEA1Kmia3FsMdVtsRNELd4TLaoKewk0E2ykLhQmHNPicPspfqTOfsUOola3TgYrPO3vrb0cIn5JueHOiaNhWGdUfvPxn2PE/640?wx_fmt=png&from=appmsg)

测试到这里，没啥好测试的了

会到登录口使用密码继续爆破其他用户

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ0yLibPabpXvxMBICF16K9kF6ADDp3iaNZR2vou59EZNu8EqiaH4vYCoCehPz6Vic3PJ3aLsGckFucDOwANI4ERmEYt70bJgfFD0I/640?wx_fmt=png&from=appmsg)

成功爆破出来几个

登录上去也是同样的功能不在一一截图

打包提交估计有点危害，不知道能不能过

重点来了

这种充电费的程序，肯定不是xx职业学院可以开发出来的

我们看看能不能找的到其他同样用了这套系统的学校

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbwMhic2yO7jbpuYXxFbwrVlFXwZXmKfkhk0G75w4Hiak5r0J5Woraez7icIgObHdAf4u3gFyZ2txtN82TvIBTdWZTA0SM6eOHOQ/640?wx_fmt=png&from=appmsg)

复制地址浏览器访问，直接就是404，中间件应该是tomcat，扫扫看，确定了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ4UdSB5WQPwjUvWbbOUleGoichLZiboicpIBaZbyScX6FbnCqoLjBIdvGkJqVZVC4Ksias92uyLbB1TapOOnvZvgoAlmg33GdJKiaQ/640?wx_fmt=png&from=appmsg)

没啥东西，扫目录看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTkzeicyCDT4mBxDcrmE68YpWh7hnxLmRknJ7BiaFFe1namEmYhrCrYnH0l0ZmJdiaPFxP3hBSJHXE3hJWtRBuLW8pxwCh7W8zI7Y/640?wx_fmt=png&from=appmsg)

访问发现这个spring的报错页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSXDVcxYqVHXLCV3eHpKgDPz19UicEYVgicQyiciarnOBxznfotIDzDvNh72WarJ1khFytWIvRVXdUU3R27zkClEz6c16qHc3gbnf8/640?wx_fmt=png&from=appmsg)

用对应spring工具扫描看看

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSMtRU6Y5PkjguTbicTafic70AXQQcsXQ6hV1MH9KpHtiaE0PXr42etiaceQicRFfXibc5YWTiagTicOiaMq9hVpzfpklVbEhOYO9wybmLI/640?wx_fmt=png&from=appmsg)

扫了一下啥都没有

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQiavSK1OmwfVcBNneuicb1xZoVcz7IcjGtkibMnbpHkFq4icog2k1VzY1mr2LnuiaGsJSP8eOOPTnWRAxVPlFIGZg1oHHV9eVmAba4/640?wx_fmt=png&from=appmsg)

啥接口也没有，盲猜路径，拿个ico,去找一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSCyLqtu5t00DYvCt6YiaSQ8ZpnJgVq6jI4aj8xg06wWt0NUl1o8B2E5fw2jUk29bkDsCJOrbaQAYmefFKiaVffBdEgq7w014B2k/640?wx_fmt=png&from=appmsg)

找到了一些内容

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTvfcW9TCmXtS8BYpWkRRtcj8h73EBPv61BiaFSADcsQxowDBKI5fH7q0ODibGpvibonsHa4uacuRpNXDI8RicUuTPb5pE9NBTRfiag/640?wx_fmt=png&from=appmsg)

对资产点点看

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTd8eBnlRPjwnp5kjOLAhuMsnoxh5noWiacpmkYXkVl00hTJT27Lfwbzzqo3HuTSV2NBDvvSnCp216ELHhdw4DRdWPsic0ZCdTYg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTKia3qicBQMBwDdicyHU3ic11lFDrdSFWQzONqLiaC2EaTSibXeoaW6km5ovhT05ATPKEt8ibHUUvwysZWdCWOh31xGk5aiahoWR6mwGQ/640?wx_fmt=png&from=appmsg)

找到了一样ico的后台

这个要是能打进去应该可以看到所有他提供服务的学校

但是太水了没打进去

换一种思路直接搜这个公司

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQJqUTSWdUxXaOOQkNXSvsMhn1nLI1Hw3CWqOLu9VkP93icqFIuibrq3ich8Y16NbQmcMmRFJKnFtt4ZIIpPpThjFzha9xQ4zfhxs/640?wx_fmt=png&from=appmsg)

浏览器直接搜这个公司

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSE67lSYEXmuVytVGWbfRRtEyqriaylEkUdPeNZAKZVlfguUDpIWB0JQWxSXYmibsP0yupQvYUE1qcajC0YegNYze07oTJ92a3cI/640?wx_fmt=png&from=appmsg)

点点点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQCrrVcExN84L4Jb1Pk8pvYcVkw4ia55vNBcxWpf8wNMyiag2J4lunVkMp784uC8t78NACRbibMoCmw2f4tb240ibv1AdJl6IBEPRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTooGoRDrCHibeWs5FKd8Om9dK2hL0cjLoFM2wprybtJ9Bxx049HvWpeubnFqIfgxSloay5WglIa6sIfwYsAwVib009pFm940WB4/640?wx_fmt=png&from=appmsg)

直接看到了，他给哪些学校提供服务的案例

拿着学校去找小程序

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQfzbxmYQSuLDEuEciaKcxJhC7eklF8Il4JdOHMT9QFEG442TiaeGGBOWawMBX12Fp3frhtfWABarZ647xsdWbvsMQWXNIJWwgoY/640?wx_fmt=png&from=appmsg)

可以找到一些相关的有同样功能的小程序。

思路分享，漏洞危害但是不大，但是如果遇到了，可以使用这个思路找一些，同类型的资产。

交流群

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTK9XL3n9rx1ntXfFnAsQdvia4hmiarCs0P4lyrL0xzWxfoLt0pvzVev66m708JYS21sZunDbWcVaVkk51KqRkQSdWdkgemnggy0/640?wx_fmt=jpeg&from=appmsg)

广告：  cisp pte/pts &nisp1级2级低价报考。

陌笙安全交流圈子+陌笙src挖掘知识库+陌笙安全漏洞库介绍 （加入圈子送知识库+漏洞库）

如果觉得合适可以加入,圈子的价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。。

圈子福利

漏洞挖掘1v1指导,我给指定站,你测试之后出报告,我根据报告总结你不出洞的问题,以及看漏洞点和总结，当然你可以自己找站，我来帮你完善总结思路。（不包过，思路为主，主要针对小白，大师傅就没必要了，主打性价比，帮师傅们快速提升，挖到第一个edu洞。）

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboR7v3GgENCXPfzwrkTKCyTu5CqOHyDR8OYWSXCfN1PmCjibjGpF1eMPfTuyXy3Am2v80V9c2JPI24C22dZq7KamHjG1XDzVmndw/640?wx_fmt=jpeg&from=appmsg)

陌笙src挖掘知识库介绍（内容持续更新中）

```
信息收集弱口令漏洞任意文件读取&删除sql注入漏洞各种逻辑漏洞url重定向漏洞命令执行漏洞反序列漏洞未授权访问漏洞挖掘XSS漏洞挖掘CSRF漏洞挖掘dns域传送漏洞SSRF漏洞挖掘EDUSRC挖掘案例分享经典常见漏洞复现等各模块不在一一介绍
```

edusrc

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQnu4nW2B6yibZw9xtCZV3mz9T0RiaegrnQbrkPN9K6MmuOEgVAyGxNvYQbP8ibmpsv7vQrkZDQFEnBvMiasFAMDFAicJAIyvcCrHic4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQnuBhAKicDz7O0I514LJKMNpZDlJQIIGvfib7HKWheKRfmZdzMzbn68CnEvadbtJwgtficShGARp4wQM5j5UhvMje1mlGPStB58U/640?wx_fmt=jpeg&from=appmsg)

src挖掘基础知识

![](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboT4ibkLJNNa0HA9o4BLCmlqTG1cia8XbBuX35VU3PD8ellIA2GcQQScjaBFPHVbMKqGibZrgUdLpyHbMLl51Yencpic1AL4G3g8a5o/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQkY3kQH91B4gYTGY4En9NWc7Rw1P8AEKoPib0pafSCvGSqEfSUd71WLACV7ibkJPMubI2PzzPggB5kobfJDjodUam1WWtO2v4Rk/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic....