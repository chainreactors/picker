---
title: [工具推荐]全自动深度-收集各种响应中的API接口-API剑
url: https://mp.weixin.qq.com/s/V5DfCdJ9nZ-RrKYRu-zw8w
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:22:05.862706
---

# [工具推荐]全自动深度-收集各种响应中的API接口-API剑

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboRuanVG4eKjEKwWcHZx1aVxdVBgicYzjdpm33Cn7GrDDr5IKJa4637R8ibibPC4wYjc3rL2RTyTgGcZS2YNIoc0mrmnBjUpeal38g/0?wx_fmt=jpeg)

# [工具推荐]全自动深度-收集各种响应中的API接口-API剑

Sugobet
Sugobet

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

## 前言

这个插件结合了我近期的工作内容和此前我的4万美刀赏金微软账户漏洞api的部分经验，API剑开发者利用API剑已多次在项目上获得成果及通用0day，拥有此工具后，我再也没有手动从任何js里痛苦的查找任何接口、路径及参数。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRAjG20dbDOhAaO0siaylzbHZYcb835KDplhnO5ianTYx3QF5S0Dnu5UE2kwCJOxuIgAEibOoIp2sXkjZzLTA9YNt8GfI7CDnmqhk/640?wx_fmt=png&from=appmsg)

与众多JS Finder、URLFinder等比较火热的相关js、api挖掘工具类似，它们是非常优秀的工具，**而API剑凭借burp的特点而获得能力和优势。**

插件主页面截图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQGjWrSN3wkmW2FEkLEofyx4Orow11AqiaqxIVsysBjJB2pVRFAJBSzEX0YFF5SRLLjk3UkuAXuwOKAteiaWACsNHMSYtskmXXqI/640?wx_fmt=png&from=appmsg)

## API剑的主要功能

API剑 全自动防环路，从各种响应里提取指定范围内的api和js文件，然后递归深度提取api，主动请求api、js等有价值文件

api结果所见即所得，右边的窗口显示api的来源js，可以立刻从js里面获得api的参数信息，然后burp再ctrl + r一键过去测

它没有想象的那么复杂，API剑做的事情更多是为我们**减少了大量重复耗时且无趣的js、api、api参数搜寻工作。**

1. API剑捕获经过burp的范围内的流量，并从**http响应中提取绝大多数link**
2. API剑将对上一步提取的任意链接、路径进行清洗，并由**API剑判断后对API、JS等主动发起GET、POST请求**
3. API剑对上一步主动请求的响应进一步的处理，继续从响应中提取信息，并重复上一步的动作，**API剑具有防环路功能，无需担心死循环请求问题**
4. API剑对所有符合条件的API请求、响应，以及该API接口来源的js文件响应，全部推送到API剑的burp GUI中
5. API剑自动将所有相关请求添加至burp的target sitemap中，**您可在target的sitemap的分析等功能中尽情享受API剑带来的果实**

用户只需要启用API剑并设置一个“合理的范围”，接着在浏览器中继续点击web系统的各种功能，让所有流量经过burp，最终交给API剑做分析处理，API剑将会向您返回您想要的恶魔果实。

**考虑到opsec等操作安全风险，目前API剑不会主动fuzz参数，如果后续有需求再额外添加作为可选功能。**

## 如何使用？

```
注意：插件需要运行在2024.7版本以上的burpsuite；（对于低于2024.7的版本，则需要手动在插件的settings页面将“是否使用原headers”功能关闭）
```

API剑的使用非常的简单，

1. 将插件安装至burp 2024以后的版本，确保插件无任何报错
2. 为插件设置Scope
3. 打开浏览器确保浏览器的流量会通过burp
4. 进入目标网站，点击和测试任何在网站中看到的一切
5. 过一段时间后，从API剑的Sitemap检查果实

## API剑的设置

在Scope选项卡中，我们可以设置范围，范围可以是url、域名、ip

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQbBz0ctMNjS1xmOmZ3Xlsjtnw1vFQ3Qx3sqZKViczLmlmQcdW5bc99NQRqFqico5phmAajoHkNEE19PR3j1tAKeCibkFiaK0NXT10/640?wx_fmt=png&from=appmsg)

这个范围特别重要，建议谨慎考虑，否则容易扫到外太空去。

设置好范围后我们再看Setting选项卡

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQAcKhbGLJqyr39mHzMtYjz81hlgONlPLxsMj22drFwn2UVouodmCwwqpnzRRh5PxELOmLUNZlrFTNmF0Ces5d5gm1W8ibUAmCA/640?wx_fmt=png&from=appmsg)

    1.允许主动对API请求

这个选项默认开，不建议关，否则API剑无法更深层提取数据

    2.  是否使用原headers

默认开，如果想专门测试未授权api接口，可以把这个选项关掉，关掉后不会携带任何cookie或session等信息

   3.立即停止发送所有请求

默认关，避免遇到突发情况想暂停，用来刹车的，建议搭配第一个选项一起使用

   4.清除当前SiteMap所有数据

这个按钮用于清除API剑的Site Map中的所有站点数据

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSaMbicAUziaJdd1iam6zRGiaRFfvE6g3rcULGWibqLWYNnHY7vz72B492nKbsNkp4fSxVaHKUkrNXYM7nUHTmejibiaicZ1f8Qvy0OfLA/640?wx_fmt=png&from=appmsg)

5.启用主动http请求速率限制每个请求的间隔时间

6.是否在主动请求时额外添加自定义路径请求

   启用该选项后，API剑会在拼接前为主URL添加指定的自定义路径后再进行拼接

7.过滤掉非200的自定义响应码

8.允许API剑主动从响应中寻找baseURL并主动对baseURL进行路径拼接

9.添加自定义header字段：（自动覆盖已有的header字段）

10.启用绕过危险接口访问(接口包含字符串则跳过)

11.保存范围及所有设置

12.是否在API接口后、参数前额外添加自定义路径

13.线程数量控制

工具链接

```
https://github.com/Sugobet/API_Sword
```

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

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbZ1HYm7R7YEiaxRVQibGWyricx9l7HpGjS4ZfWRdlft8iacwkpzYyZfmYEkWdJgYRORPkNFR6dADR5MyE524tWX6cAwN8MmrCZu0/640?wx_fmt=png&from=appmsg)

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
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFBRMa8XwYxfcZMyXicx94xSKxawPcqFia2rJKOL7fSLYXiccwHc868XxNGIQ5z7ibiaI1MNAGRrK7U6wXJTsZOCAu2I5XV1boTAL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBzdakI9XI33ReAm2dxO8vgzw3JicQmUuWCb5ayBlKR1PoQHEHFETteBnicyupwU0mXvXibfrDoyg8nSWBGoK1p2YXY3ElhcvOQ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目绿盟笔试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**POC库****&&更新适配afrog&&nuclei&&dddd的POC&1day/Nday等&&******dddd二开******工具[助力渗透测试&&红蓝攻防]**

**工具截图**

**![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRLmmY4kF0AaQjAJUQzH1sAExGoE7AmDJZXcEgdnKuRkpgZ9xYflY0UxtVkrP4HicDfvCWibXY86fAjH1E0TDJ5YqatD9fjZrUYk/640?wx_fmt=png&from=appmsg)**

**实战效果**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSKqLXNcOPE07xOwOUCjRGuFphopPumW9RaticmNCuEUXu52GtdTTfpTUicrBj80kMcZzJsnps3abyvXIvLHEIhvMoXUApOqZCe4/640?wx_fmt=png&from=appmsg)

**poc库【后续持续更新】**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTG9Lyp44aFffUOxQKtHjToGfqFWTjswYft0VtAPINtV5MqmrTTj8GWrVb6yowvHURubPgOqdribmibWEb0Fcj3YdN4iahUwItcxE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRAMJIIvexOOJa5KhrsKmlsx8bkwib9SPoK72Q0OSPWR5qx67yvl8scMQ5bg8caBXZH01kM39RDnKpnWSaTicgobRmLygERGFWls/640?wx_fmt=png&from=appmsg)

**AI赋能-****skill辅助****漏洞挖掘（免责&&慎用）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR3Dib0RVxVhUOzS6ibC6BvkfulXQAclic...