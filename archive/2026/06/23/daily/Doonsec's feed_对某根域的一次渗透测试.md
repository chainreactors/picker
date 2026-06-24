---
title: 对某根域的一次渗透测试
url: https://mp.weixin.qq.com/s/SiskzGbPfbOzhH3zmILmNA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:02:55.470327
---

# 对某根域的一次渗透测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboRBWBAYGLticzklKKGxF4LDfLkvSkvTJEuic8ABxagicN0cKLUlLYkhnJuyrFgrEfBEOnRsAKpTzbTdnUOPmhcTo84B6jsibSxETRw/0?wx_fmt=jpeg)

# 对某根域的一次渗透测试

bcloud
bcloud

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:bcloud原文链接:https://xz.aliyun.com/news/14463
```

# 前言

两个月之前的一个渗透测试项目是基于某网站根域进行渗透测试，发现该项目其实挺好搞的，就纯粹的没有任何防御措施与安全意识所以该项目完成的挺快，但是并没有完成的很好，因为有好几处文件上传没有绕过（虽然从一个搞安全的直觉来说这里肯定存在文件上传），那话不多说，进入正题吧。

# 步骤

拿到根域，简单进行一个子域名收集，利用360quake搜索，发现大量gitlab服务，我猜测是蜜罐并且很难从这一点进行利用，所以只是简单的使了几个弱口令和CVE历史漏洞，发现没什么利用点就找下一个去了

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRax0Xib4TIgHUbQVgVcARgU4lrlktoZ7AQY9YXEHiboib0adPGKVJPnnib5cd39WibemsgZxpHmWfRmhYuQgQSicerGKtKw9UwibUgOc/640?wx_fmt=png&from=appmsg)

然后这里也没有什么技巧，就一个一个子域名先访问一下，就这么简单的找到了好几个弱口令漏洞（心里暗想终于可以水一下洞了）

弱口令直接拿下

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQaCJy8Og0sOfibjXgE5zU8px9EJoml2Do9rGkzWsYuJ6CeEmrRRhjU8eOkvYyBYIvGSeZhKJ2Px5d5Jc8kUyIvdXYBDMI90tFM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR9wVfxYvwh8NjUZHjwjU0kRFBZBo8tlYKRW27ms5XuuRwiaq8kB1c1cHG7l6DUyQFOUVFrcCSWs6v4lSfCTKDWQEb2VSBLO168/640?wx_fmt=png&from=appmsg)

进入网站发现是thinkphp框架基础上搭建的thinkcmf内容管理系统，然后看了一下版本只有thinkphp存在，通过报错发现是5.1.40版本，去搜了下该版本是否存在历史漏洞，发现有，但是没利用出来，我想大概是修复了或者种种原因没有利用成功，那咱们也不浪费时间，先看其他的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSp65QEQxx5U3S4bJ5D0IgIE4UDKQDF8VzsgAx16vMMbQmTOsBxVfPgeCwV59yvWHC6ICZKzWPP5yylgNhRiaej23r4sVt1vCEg/640?wx_fmt=png&from=appmsg)

然后发现该网站泄露了邮箱账号等信息，我心想这不就有了嘛，但是没有登进去，我猜测大概是改了密码但是改处账号信息情况没有即使更改，但是也并不代表就完全没有其他用了，可以用来进行钓鱼等操作啊，而且该邮箱账号的发件人是公司财务部的邮箱

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQuFP7whWhuyV1uJl1XRyzE6GRd2IWN04Zjs1UVDzZLdwug95FCtOuVx8Nm7ibrp58nhNBibF8n70xXS48SrubgEXUANF0lYrg1s/640?wx_fmt=png&from=appmsg)

发现上传设置处可进行文件上传设置后缀名称，但是实际操作发现并不能成功上传，此后台有多出文件上传点都没有，而且这个cms版本是没有爆出过漏洞的，所以此处文件上传应该是比较难搞的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQoTOoUM2eDPwt6iaUBVK82OHyQ5x6BBzlDFf8e4hMZn5HSv46x5jDAOvJH63YuefCyIIEibTaOYratvm8sFcATUBc9BoQShWstM/640?wx_fmt=png&from=appmsg)

通过各种...发现七牛云存储的aksk泄露，这还得了，直接连上去看看是不是真的aksk啊，不仅发现能够连接，而且此云存储服务器还有此根域下面的其他子域名的文件等信息，我猜测所有子域名下的云文件都在该文件服务器上，仅仅一个域名就有高达50G左右的文件，其他两个文件也有10G左右

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboScx8kzNDTEUFyqQB0137B58icMWnFRj007Ub2ia7iaWYt7kyXHDhiapdF9EibIG1icN9wWXa9yGwDiaqPevs13eY46UX5VyTNV4p41bM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSxHCiak03USxxCfbM4rkC6iaAGQe0e5NRKtv9uibusWY4sGYkkqMazaZNS7NqNFB4qXPBjQwT4P7sMxNNm7oib6gLfXDB0hlicbMYg/640?wx_fmt=png&from=appmsg)

除了最重要的文件服务器aksk泄露以外，还有短信APPkey泄露，以及微信小小程序key泄露，可直接获取access\_token信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTPaVDPHSTHUfJQ88sw8jC7s8IATpibhaeH92GNJTicD0Bhp2VhRsKgKicuYRdC079m4p7yPyNnlFuObcfak0rPcabia1uX5iaj39JA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSQZAWTWuicAKQticcH5cicWGU8QdP8Fh92LVqN5tXWhACba8LYukc7M6gebkC7C3BASOItiaObDt9IPAIWnUdcOJDBwPKEod4aPDg/640?wx_fmt=png&from=appmsg)

发现该域名也存在弱口令并且也是使用的THINKCMF内容关系系统，和上面的模板一摸一样，但是弱口令密码不一样

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTA1fNM38Wj3zMuq3saib6fCEhvDxS7OHdXvxN9gaWZMiatIdGVz65zdUudDrpExuaY02N8xic0QHeyp6IMsPxXGhoYWS8NIKNCEI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSjLYa3XyZDPrOIBc9ROuYtbsRlia1TlMcJYpEPyNMu3J9FfYDbeO2ocialibPBD2t9K9PogmRibD4LerrQJdseB7IuKayGJNicj5CA/640?wx_fmt=png&from=appmsg)

资产管理系统弱口令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS8h1JCGVXl5d00fkY0mbp3eWEhbjBRD6ovVicAbt6r4grKzUqcQ5YVREfVvKyib3ZLpq6bdElEVY1GzWIw1PMA37qXTtYuuFneU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQicFickiaMRlJck2Zajq8nzpQt95mZHYClcxRjicPrOGEVMUHTpSHZdiakzjBOygG4RyR8CwNZC1MB2LrYHCqLzzOAVM7930kAib4gM/640?wx_fmt=png&from=appmsg)

发现使用的是laravel框架，但是该版本不存在漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRQBP4sQ0okABtvPEvMZFddWjZnz1Vxsb9ByRpRLNWw6D0T1LmIkbsf8bicBGUgTPvKTrPn6S0GmL9BVHurDYnRPVMtFtTbJHnw/640?wx_fmt=png&from=appmsg)

除此之外在文件上传处可进行文件上传还是，黑名单过滤，我使了很久发现可以上传php2后缀文件但是无法进行解析，没办法，实力太菜了没拿下来，只是简单的上传了一个html文件类型的XSS混个洞

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTF67cPOAgGkhKoG22LyicVuOMwOMYC78KJYJ20TG5ozoDteGlvfaepSoAwtD9zQno04PRibKIjO6uG4cAGKBa0ibG5ccIHTJq5wM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRZbjjqhlqdTQeI95xB2hIDeh9xxiayFMIymL3bXKn8RMFx7SN8ZicXkPzcHEibA7ic7XSuH6tconJeKKNx9roUfYZm8ZRpssia1s9Q/640?wx_fmt=png&from=appmsg)

发现该域名下也存在弱口令

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR7CvomBtXzfNeGoOjTzuRDZxTFyM9L4sheoCmDqtKoNnWkBqWZJgGEoGeUx4UQcG7Uk4bG2xfvrO7YhmTWn0gbGGfSpG4PZrE/640?wx_fmt=png&from=appmsg)

并且该文件可以进行文件上传，此处文件上传处是白名单过滤所以大概率也G了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGHuyCFVGSw5qG7TG6ps6sw3x7KfmlOZzAlo5aO6cicLO2LhYtCKCXGtEutbZgBtopquEVdG44YHibx4ibdX9bJPiaREHMKLIGtAY/640?wx_fmt=png&from=appmsg)

# 总结

大概流程就这样，其实大部分都是弱口令进去然后找功能处进行测试，然后的话后面还发现了许多弱口令和上面几处案例都大同小异就没贴出来，并且在后续的文件服务器中发现大量身份证等信息。其实该项目挺简单的，基本都是弱口零，而且很多cms，thinkphp框架还有laravel框架都报出过许多漏洞，奈何本人实力不够无法进一步利用。

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRALwXmgZ4mh2LW0RdicrKjBCP7P1iaF14G0Eq2v3KRnTJORpwXZlF58WEz6QicxLJpyJaA5iah5CF2rHjBz4JzOELFRaZTAKOQ2tQ/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRu8Gf849iaCkSBxLL8IlzJTRs185QicEe9l5UGI1dEVKISt2IGGveZynXBW9tIUsxNsz4adSTib7rib50uSJdjNfTvVRFrbPJhzL4/640?wx_fmt=png&from=appmsg)

云安全&AI安全

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ9qiavETNjaaX162czpNCqpw3uJqVpicbI15AXzhf5x8icmHxBdTGOgRgzNPGF3Aw2gglT4Fx09JGXYibQC6U7CQKVmoH08l3meia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQgcsjiaZ4S26TWowHfpBkhSeHf2pjrcDyicJuia3uqvRBauLEOicibibEMqibnBMtjopFL8No7UXNibbURvzeJ3dQHTibvGxRQGnorb4co/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
最新漏洞查看1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
`...