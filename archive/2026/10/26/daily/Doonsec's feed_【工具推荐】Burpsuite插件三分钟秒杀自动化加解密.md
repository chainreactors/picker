---
title: 【工具推荐】Burpsuite插件三分钟秒杀自动化加解密
url: https://mp.weixin.qq.com/s/1cyYqhUkWhgbjueDTNN7dg
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:02:46.629017
---

# 【工具推荐】Burpsuite插件三分钟秒杀自动化加解密

# 【工具推荐】Burpsuite插件三分钟秒杀自动化加解密

原创

猎洞时刻
猎洞时刻

猎洞时刻

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/d6JIQYCSTH9evFcNH31Pjh0f83GEqsibSQsGS8uUrBPLU6VJbjw8CTibOgsYYOhqqKpaQHb9BicrJcCOYhZG0tYOg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1)

**免责声明**

![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn6mG6TyJornrhz9JticBo3Nx4zhzUFXcggEDw1lkfzMI0KuLp7dW4dDCvbfgAKlLSX3yGmYg0gtXcw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

```
本公众号“猎洞时刻”旨在分享网络安全领域的相关知识，仅限于学习和研究之用。本公众号并不鼓励或支持任何非法活动。本公众号中提供的所有内容都是基于作者的经验和知识，并仅代表作者个人的观点和意见。这些观点和意见仅供参考，不构成任何形式的承诺或保证。本公众号不对任何人因使用或依赖本公众号提供的信息、工具或技术所造成的任何损失或伤害负责。本公众号提供的技术和工具仅限于学习和研究之用，不得用于非法活动。任何非法活动均与本公众号的立场和政策相违背，并将依法承担法律责任。本公众号不对使用本公众号提供的工具和技术所造成的任何直接或间接损失负责。使用者必须自行承担使用风险，同时对自己的行为负全部责任。本公众号保留随时修改或补充免责声明的权利，而不需事先通知。
```

前言

推荐一个网安师傅的BP插件cloudx，进行加解密方案处理非常方便。

去年就使用过这个加解密插件，当时还有一些小bug。目前最新版本的bp插件，已经解决了大部分的Bug，目前适配性还不错，对于一些普通的加解密场景，可以实现三分钟秒杀加解密，不用再写脚本！只需要写规则！

使用技巧

1、工具的所有行为均由规则驱动，规则是绝对的，它几乎能做到任何事，规则是从解密的角度配置的，这一点很重要！！！

2、项目拥有大量鼠标悬浮提示，按钮/节点处均可查阅

3、sign经常不参与运算，可使用表达式按钮减号(-)移除sign参数

4、如果动态密钥非服务器生成，尝试固定密钥，即可正常进行测试

5、不建议随意分割规则，推荐 AES( URL ( requestBody ) )，意为请求体先进行URL解码后再AES解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6kc9qaUjrtdynOeuU83km7zeMFcSzmCQOdONzO599fHWguPk7Tia4ds5K99SUHUgeY0GcDkECLd965l5TlKEvPbPqEvxpicSyuw/640?wx_fmt=png&from=appmsg)

实操使用-AES对称加密

网站-->加密数值-->BURP-cloudx插件解密-->burpsuite明文操作修改--->BURP-cloudx插件加密--->服务器

就以靶场 encrypt-labs来说，靶场下载地址：

https://github.com/SwagXz/encrypt-labs

第一个固定AES对称加密，是把明文的值进行AES加密，再进行URL编码发给服务器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6jLicDFsY0IPr1p2QI274Qts7JPLqXicXdibEhB24vRdoBC6W411UoRcibfichCVt3o9G8tvn6bIviauc6oo7edk3HTjVibiapQZ1zk9w/640?wx_fmt=png&from=appmsg)

我们抓包之后，就是加密的aes+url编码的值，无法修改。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup526NRiayiaST6vDl1P4AntWfSgGx8JLoQQ3J977jHModz5EkfLMermQzicVkc3NyG70sv5k9dH22FeMNEBz1jv3l17oNsWfRLypA/640?wx_fmt=png&from=appmsg)

寻找加解密的方案，可以看到这是一个aes-cbc模式，并且key个iv都是1234567890123456

知道了加解密的方案和密钥，我们就可以通过插件cloudx秒杀解决。

重新进入靶场，然后进行抓包，把加密数据包发给cloudx

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6KSP6s7b23yKZdQzYTY0SUuWB5Xo9tlZNII3QvAiatenuvYqcPibm6ZPoHCJ9e5gvjkOn9yCR2hiaJTKfx5dO2oO8hAXbJznJMZ8/640?wx_fmt=png&from=appmsg)

他会自动创建一个url编码和解码的规则，这个可以删除了，因为这个实际上是aes+url，不止url。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6eRTkRFoAHRjIaY0hYuVS4kHx0BZgdDNDxFEQyT3um1aIzHZlqA4XKQmj4K4KdSfO7dmonazo3P34iaYWNU0wohtldV4aLPvqg/640?wx_fmt=png&from=appmsg)

去已经配置的规则里面，把自动创建的规则删除。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup5uflXpbASKVMEa21Io5yQvO7y1rBl6YBMdbaCh7TLAmSzfia78xcFbrP0XJxedibmj2XKXhWiaiaMSvuIB4tmNJsc1T89sicRPpoD8/640?wx_fmt=png&from=appmsg)

然后我们选择请求体，选择参数encryptedData，然后对他创建AES加密解密配置。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4KxlmFOVU4etgWJHPC3JV410AxiaFvEhrHhNCXIfVqdts1qB1JrqTiaaLF6JTvic32QaSEyacibz6wgyhNfUMq37NCxGuiaMpaicKLg/640?wx_fmt=png&from=appmsg)

输入我们的key和iv，1234567890123456，然后解密。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup6U8C4XXZAfWDyBc7h7kv5CcEJcic0OlfQHr8RiaHOkwAQq31Ngd8n8gqnCGECiaMzJemnonXgMu56kKesPReeALZUZD0pCA0aJek/640?wx_fmt=png&from=appmsg)

解密成功！然后他自己生成了一个新的规则，这个规则才是我们所需要的规则！才是有效规则！直接点击添加即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup7YyysZXS6gtEWHGiaZa8wv2H8EDicmicOrM8fwtCjT94kqgerr3o96JalNvuSzSWfw58dicu034gHCw7ql3Mxo2PZLSljL4k0xAo8/640?wx_fmt=png&from=appmsg)

然后看到这里的规则已经创建成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup6HaFMiatEDYJqB0ZI5OoURe5pLKTePogZlXNmtbbL6JgF0zy6vBibOo3ebzZXNfJx0AQf3r1VjicKQvw72KpOutn2mE7ZBXU5F8w/640?wx_fmt=png&from=appmsg)

再次重新抓包，发现拿到的都是明文了！

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4a135aBzFeSicK4BuAMaXBa3Yeu0sgRNibZcbJ38IFGOgkibM07ia95ibiaPDWTNia4Ajlo3LBdO2gBicmaNMVgFD955ddZzYcoAI1k5Q/640?wx_fmt=png&from=appmsg)

然后可以对明文进行任意修改。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4XjsVb4QMhb8KgUmJqcaibRw8JaBXvH1zF0NqiavdiawGuj3jx44O0D0RIIMBKMykYyGkmR12pib67Dibkibpy2Kc1JlfaiaOJiaiaib44Q/640?wx_fmt=png&from=appmsg)

修改密码，发现登录成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup4p9svFDmp0keFrZXVzJ9MmW6Jl3sQys1CcO61WGmwJ2M7McRiaNEBq095ulk99B9D7iaWko8wJticSWM4icDANa1NiczYunIptzQkM/640?wx_fmt=png&from=appmsg)

还可以进行intruder爆破，都是可以的！

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup5zuMZtzg5vEEQOxQkKLwyoFx9DHDC1T3ANfzxQJdoF9wxric4cVFTkbU7P209sfo5OKcQIBUpea980d1q5ITibyOFeicHVo2o850/640?wx_fmt=png&from=appmsg)

最终爆破成功！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5yZe3AdYp4r75w6bp33EOjE9NqrfwBYahpCXtdweMC4OTjCwQ8zxk7IdnNMDB8kWuhyeYQwENyJo1hswicuar7b0Zc6lUvhH8g/640?wx_fmt=png&from=appmsg)

实操使用-签名sign破除场景

除了自动生成的规则，其他大部分规则需要自己手动写规则。

比如破解明文加签名，防止内容篡改，通过手写的规则，快速解决。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup5WJnibzCcSTBEh4Zxjypo8D5ILtMFiciaZT64K1swgklEpUa1PmFsuhCYq2HhQvbXLk88WvbJlJlbyYiaWHhnM2Dicw3eYpPcz7Aow/640?wx_fmt=png&from=appmsg)

比如下面的情况，随意修改密码，后端会直接提示签名失败，拒收。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4urXxpvVzu7J2fp4BxUQiaO0WSzrCZPLlSShCE8OAxs4ANuXeia6YR0oBxticqwhorQZAkZWSTAnJuwE7MbFmcHvrnQyKx5ZLLKI/640?wx_fmt=png&from=appmsg)

然后进行js逆向，快速定位加解密代码。

可以看到签名逻辑，是对下面四个参数进行拼接成字符串/

然后对新拼接后的内容直接hash，生成了签名，因此形成了防篡改。

新字符串 = username + password + nonce + timestamp

signature = HAMC-SHA256(新字符串)

你只要修改上面四个参数的任何内容，都会导致签名失败！

并且hash的方法已经给说了，是HMAC-SHA256 哈希算法，并且密钥也给出了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5Su6icd4fSmPP7vAW3aqibYRyJUfsnDich0nwicDLZZDgM72UfSW49unibGWaVdVdlahGF1ZWNXS5GOWYMIve0rGbAicc11o7gLalUw/640?wx_fmt=png&from=appmsg)

最终构造手写的规则：

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4xbOCZMOhOeLVyOuicyhQfYVYxkXKoibNDmqMCEV9KE3zUQZbOFqdT9ZHQrArhvevgYE60YBkSkDX3NliaOx0O7jRHBktNzynsSk/640?wx_fmt=png&from=appmsg)

使用规则生效之后，重新抓包，可以对账号密码进行任意修改，不再出现签名失败的问题，比如下面是登录失败。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup4v5MbvFf8pkdmtSoHl5zkOjugrrfecribBibVRvUd19QzFQZbrXy01KDkc86yfKR1qBLMu33ppPV7972abr1uOquo1PYAW8e9Xw/640?wx_fmt=png&from=appmsg)

下面是登录成功。

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup7YXH24lDBSJ0KtcwKFic4LWEFTJxcVQ9OfRuHcnflYuVFhiampMtN4mjs54cXHQlzMhtZvy9gliaKxiaZkRia1RV64ut5uwVWmI0ick/640?wx_fmt=png&from=appmsg)

后台回复【261026】获得工具下载链接

网安交流学习欢迎加群！

![](https://mmbiz.qpic.cn/mmbiz_png/ucA3HFqtup4icZk2sHUdJ1lnprJMXNfz2iczPc7wAwnZzN5rPwzk8k28cfn3r6XuibLVTnSsgcDKA5TK62nhJUK0xawTNGy01Gicge2z1oxRcf4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/doerbbgECwpeFnACfhfnjV0KRib0wx8dSYibBibXfvnlSJKZjVwqDkT4p8w3YR3kE9V23USEQoTLWyuxElcVuDohMJ7XibHRYDiaKjomSfhbOx7A/640?from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/PRjdmUELtVDZsOJib3BlegVyicZrfRqrkUKQ2sIP9mwxpzUymkzJrv7ZbXh9rJdWGeAJdlkFtQGCBgd5XmaqJdMEzusgnCkyPeGYrn75kcKc0/640?from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/G0iaFtEibWU95PS1s38UE9icpFGHNBvGE8hBeZwkn4LbnvYJfIezdAS9Xqibfaot7vGRRkl21iaBHcKQCxzWCSm3nLpMIGlqCib7xqnZwVrGERtek/640?from=appmsg)

挖洞、赏金和入职实战班

![](https://mmbiz.qpic.cn/mmbiz_gif/IpAzibH6mLiaXTmWkTA7SecLb1jwcPkGLUTxdh3RrsOTpfbeDAhJDpYx84YbCPRO1jVVbTez7icvxTkJeCPTYtkQ6dLVxded0jzsl2bGy417cA/640?from=appmsg)

NEW JOURNEY IN TECHNOLOGY

AI赋能挖洞培训

![](https://mmbiz.qpic.cn/sz_mmbiz_png/n4yj6uk7icAClBAquKgcqEdUm6z5bsKzGicqXtoX1Om6N3yP4QmZal5V9M19efUWMunG6pdHiaUfVzmTmGoFfn3PgDvic3d8HyDTSuqLMpjgAlk/640?from=appmsg)

网安新人应该做什么？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ne7st7osWQv1cP0Rq7A6Kc0LuuWKCz4UWxGAAlcibvibYSPOEbrMmjCSzYAgtHlBoEuEpBwOczupW4VKQOgphRoQCmPdjKpIfallIqhgQ4SwE/640?from=appmsg)

经常有新人问我，我明明自学了那么多网安技术，B站也学了很多，一两年了为什么迟迟在实战无法上手？只能去打靶场？ 那是因为你没经过系统化实战训练，你学的技术全是碎片化的，今天学Web漏洞，明天学python，后天被抖音的人忽悠学Kali，今天靶场明天又实战，实战挖洞还不会，硬要学内网渗透，最后技术存在断崖鸿沟，这样学一辈子难以入门，更有垃圾网安培训，全程只有靶场，根本就没有带学员去实战挖洞培训。

其次还有些新人，大三大四了还不会实战挖洞，只会点DVWA靶场，完全走的是学校老师的路线，太慢了！很多大学老师到大三才开始教学漏洞原理和靶场，而你的同龄人已经早已去大厂实习了，所以说别幻想学校老师能教会你什么。是不是温水青蛙，自己学的水不水，你自己清楚，别再欺骗自己了！

只有真正的实战挖洞能力，永远都是你在网安这个行业的核心竞争力！挖洞足够强，无论是就业大厂，还是实现SRC赏金，都是水到渠成！这些远比其他的更重要！

如果有挖洞入职培训咨询、网安考证、扩列等，欢迎加我。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ucA3HFqtup5CibqjOAgcKHNZ1YnlPjWTibMUQunqC46C4icblvvlKhPyWwhPiba6ibW5ZUG4HWSQiccN3Ka9HhtwrMzt5WrAoAcCwfYb42MkiaojCk/640?wx_fmt=png&from=appmsg)

猎洞时刻团队介绍

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ne7st7osWQv1cP0Rq7A6Kc0LuuWKCz4UWxGAAlcibvibYSPOEbrMmjCSzYAgtHlBoEuEpB...