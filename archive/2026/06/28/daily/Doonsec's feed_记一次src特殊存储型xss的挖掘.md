---
title: 记一次src特殊存储型xss的挖掘
url: https://mp.weixin.qq.com/s/hrrDa28AwcK73xoQp542NQ
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:33:17.760508
---

# 记一次src特殊存储型xss的挖掘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboTBSJLzQOlxWYNYJy49dgONJ1iaNX1KJuLSibJFQtUic2Xib1CATibztughN9daNx8Agx9pyzRDb6YrSh9ahLmibbTjkklYO5LPKSBZ0/0?wx_fmt=jpeg)

# 记一次src特殊存储型xss的挖掘

FreeBuf\_318700
FreeBuf\_318700

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
作者:FreeBuf_318700原文链接:https://www.freebuf.com/articles/web/320220.html
```

## 0x00前提

星期天在家没事的时候，意外间看到了某src冬天送卫衣的活动，卫衣好好看，决定冲一波

## 0x01确定范围

首先呢，挖之前。要先确定方向。之前从来没挖过该src的漏洞，然后一看该src15,16年就运营了，就决定放弃核心资产了，毕竟估计已经被弄的透透的了。

在看了小蓝本和极致数据后，发现资产大多是app,可我对app漏洞挖掘，不是很熟。而且一看还有5天活动就结束了。于是决定从一些公众号和小程序入手，看看能不能发掘一些漏洞

## 0x02发现目标

快速对公众号和小程序进行测试，对各种地方一顿抓包分析，最后发现该公司的招聘主站有一个搜索职位部分很可疑，还有历史记录，随便输入了一个aaaaaa，发现返回的前端代码的地方有三处，分别在input标签value属性值内，lable标签的值，以及a标签的javascript伪协议。

```
<input type="search" class="searchInput" id="kWord" name="keyWord" value="aaaaaa" placeholder="请输入职位关键字">
<label class="weui-label"><i class="icon-time"></i>aaaaaa</label>
<a class="weui-cell weui-cell_access" href="javascript:searchHistory('aaaaaa');">
```

## 0x03绕过测试

测试双引号，尖括号，发现服务端对双引号、尖括号进行html实体编码并返回到前端。例如<>被转义成了<>

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQkPDHQ0NNJZ384u13aI8anZMKZtczTuljQn5qAK7myDyIGSArLna4ONW92gicr75JVibK0zy0sdLzQqQ1F0LPdEZLRJp3YR5WcQ/640?wx_fmt=png&from=appmsg)

这种情况下，熟悉相关编码的同学会知道。前端html解析器只会将其当成数据还原，而无法起到特殊符号应有的作用，比如双引号的闭合作用;

除此之外，我还对尖括号和双引号进行了两次url编码，发现该服务端正常检测，说明服务端是对url进行了**两次解码**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTiaHR6cXOctua7kPOLwjQYLiatcxLYZwRibjJjmykVceBlMbqQI4xRsZPOaBUNajkvJvFauv2fNUqVbrugtPZmKiah9593EhzTOgY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTJbriaflvs4emd8oG1KMugibMf4hu0ibG8IomgHdfB4aqWkthy1HaP3XfWmmDqbunIItrFATwqapjLibw5Nquib8kYiaV3q5E4GAsmw/640?wx_fmt=png&from=appmsg)

但是柳暗花明，我发现**单引号**没有被过滤

**所以测试了一下，'alert(1)测试，结果返回到前端的数据变成了'alert(1)。**

而在a标签的javascript伪协议中，代码是**href="javascript:searchHistory('')**;函数使用的是单引号闭合；这意味着我可以用单引号对函数进行闭合了，perfect,于是在burp中将post数据包中的参数改为');alert(1);(';返回到前端，点击a标签指向的历史记录后，就会成功弹窗。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRljvYjPhwWpYjt9Aia0vb0aqySdA6EhtUfWjnMtlI4XJ8fvqPxHZEyuC9g3T5aT04LbZ6dWf1gUOd1iaB93l5jyT6liaticj0oO7o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTsyWvCeiajhZWqbcSxF3tIzuZoGQibzyjapDoz5TPbQgzxB8oVc91RVE8CxY3rsicXF9nAia7tzibXLln7M5ZCIjQnfg32RD0GpCZw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRcmzSH7JyerPwC31JPFNQ4m4egVRtQm4htUFTWibpXap0w0q3gL5oJvCdOX35BYmQAiaSfMHwzqX9jtOaz0k5xpwibsOX14LMsiag/640?wx_fmt=png&from=appmsg)

## 0x04 确定类型为self-xss

触发后，我悲剧地发现它目前只是一个**self-xss**。因为所有的数据都是通过post传递的，而且参数众多，意味着我无法将恶意代码注入到链接中，去进行传递。

但这个好歹也是个存储类型的xss。因为只要访问该招聘网站，网站就会分配sessionid，并将你的搜索记录存储在服务端，每次点击搜索页面，无需在提交恶意代码，服务端就会返回带有a标签恶意代码的html返回到前端。

因为历史记录类的xss好多都是dom型，为了确定不是dom，我在返回包中的html看到了含有恶意代码的a标签，确定是存储类型的xss

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR7on5Vur652YVKhpgOT25g8Z51pKk1BQBr6WCXDDCK43rUQWE2vPMIWJzmb5XSUCFUfT6ofWZST9Fp5OWr9n4PQZSwsIB0fhQ/640?wx_fmt=png&from=appmsg)

这个时候看了一下src的规则，吆喝。规则中写该src还收self-xss，只是当做低危；于是提交结果扯了半天皮，说是src从来不收self-xss，**但将漏洞做到可以将恶意xss代码注入到链接中后**，**按照中危处理**；行吧，那就试试吧

## 0x05摆脱self-xss

重新审视数据包，从提交搜索记录的包开始，到最后收到含有恶意代码的html代码的数据包，这期间有数个包在交互，最后锁定两个包，即最开始提交搜索记录的数据包，以及最后返回历史记录页面的数据包。这两个数据包最关键，而且巧合的是，参数都一样，只是链接不一样。

这里首先使出change requset method大法，对这两个包请求变化方法为get，这里运气很好又很差；好的是变换方法请求成功，说明可以支持get方法；坏的是没想到网站对post方法参数数据中的单引号没做过滤，但竟然对get参数进行了单引号过滤。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTmCBpPkn2v9qrCQ8iaOfqd99gNR239TbA0VtfwkhMAfT9Oib5SpMyyeoHcpFkh5w3eXX5tZ7fY0j67DibKKyQhpiaqxjExAGFUicyA/640?wx_fmt=png&from=appmsg)

**于是尝试绕过，这里奇葩的事情出现了，原始payload');alert(1);'(和正常的get请求的一次url编码payload%27%29%3Balert%281%29%3B%28%27都被拦截，但是二次url编码的数据却绕过了，因为服务端是对url解码两次，所以直接返回到前端的数据就是两次解码后的payload');alert(1);('**

除此之外，编码绕过的方式有很多；

在xss相关编码中，html文档再返回客户端后，会按照html解码->url解码->js解码的顺序去解码；对于每一个html代码，并不是所有的解码都会进行；这里面的知识点很多，想要了解的朋友推荐看一下lemonSec的文章[xss编码绕过原理以及从中学习到的几个例子](https://mp.weixin.qq.com/s?__biz=MzUyMTA0MjQ4NA==&mid=2247518227&idx=1&sn=6a133f114d53a6fc39bd0ace0912d8a8&scene=21#wechat_redirect)；

这里举个简单的绕过例子吧，就拿这个漏洞来说，在a标签的href的javascript伪协议中，html解析器、浏览器的url解析器以及js解析器会先后进行解码，在js解码前，会对payload进行再一次url解码。**因为服务端会对url参数值进行两次解码后并返回，所以，这里其实还可以对原始的payload ');alert(1);('进行三次url编码，那么经过服务器的两次url解码后，服务器最终会将一次编码的payload %27%29%3Balert%281%29%3B%28%27返回到前端**在执行时，会先进行html解码和url解码，在url解码后，payload其实变成了');alert(1);('。所以虽然在前端页面显示的是%27%29%3Balert%281%29%3B%28%27，但在js解析器执行的时候，实际上执行的');alert(1);('。因此最后还是成功闭合且执行了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQDcg19522GsWp6ESgT6yXUKriak31foKqAlLfBkxq0UQJHVaexKZ05oWOZEAcxHPvGSr5s8gspo3U410xQxHwyuLpfQV08quaM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTPNf9yR2FwNX9PmcuPViaia0HTwoEfWicGcgfeHQrYMufrR2ibJFRX9ELHOuLrUyVM0ibPPAAJjiaibOAK2uicdIWWPxdaiboD3M68gibsI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSllumaaAc1xmibT3pBA9eiaCUerVpbNqDzY5aRN0YAYUG3HmMfSA71LNjsXpZSCxrlxCMGa12TpVmBiaBvYPUj2T2rOQic8RVvB28/640?wx_fmt=png&from=appmsg)

从以上描述可以看出，编码的结合其实非常多；

言归正传，所以此时可以构造恶意url了，这里将payload的内容换成了弹cookie;而且因为恶意链接在浏览器中访问时会自动进行一次url编码，所以对恶意链接只需对payload进行一次url编码即可

```
https://recxxx.xxx.xxx.com/xxx/xxx/mobweb/v8/position/list?keyWord=java开发工程师%2527%29%3Balert%28document.cookie%29%3BsearchHistory%28%2527
```

ok，至此。漏洞就不是只能由用户自己输入恶意payload，用户自己触发，然后不能注入恶意代码到链接中影响他人的self-xss了，而是可以由攻击者可以构造，可以传播了。

总结一下，该漏洞现在已经成了非self-xss的存储型漏洞，即用户点击上面搜索记录的恶意链接后，恶意代码就会存储在链接

```
https://recxxxx.xxx.xxx.com/xxx/xxx/mobweb/v8/position/selectKeyWord?operational
```

的页面中，此时用户点击a标签所代表的的历史记录就会触发的xss。如果再给payload前面加点正常职位，最终的结果就会变得正常很多，对于许多安全意识不强的人，由于点击恶意链接后，以后每次搜索都会出现这个历史记录，不留意的情况下，很有可能就会上当

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRhU4KJZrUU1FmPqicJia5Fb8KREI9WD4I3iaKJYuGUx9kAmfwXbAfXRk0nZM9pW7lrx6GnBhwmr8wAb4Eo1bicETpjmKWXJr1gP0Q/640?wx_fmt=png&from=appmsg)

## 0x06争议

再次提交。看到结果后。人傻了。审核仍然说不收。

首先审核仍然觉得该漏洞仍然是self-xss漏洞，而且不算存储型xss漏洞。他认为这个漏洞是需要用户点击恶意链接后，再点击历史记录，才能触发的，相当于最后还是要用户触发，所以算是self-xss。

至于前面最开始他所说的，要将恶意脚本代码注入链接中才收的xss，是要这2个步骤合并为1个步骤，即变成构造成一个网页地址，用户访问网页地址即可触发的XSS;

最后呢，他认为招聘者不会傻到点击这个历史记录来攻击自己，无实际危害产生。所以拒收

但是呢，我这边坚持我的看法，这不是self-xss，是存储型xss。因为首先这是用户点击外部恶意链接作为前提的，而不是说自己输入恶意代码，自己触发；且该链接已经可以大量传播并影响到其他人了，很明显网站存在xss问题。我这边就以某百科的定义作为参考

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSWXqCOPhA7TgoZk1xmOdjOjoRicv37JWBxjqwd6tyHaNa46wV8Dmo435bvicDsEeoM0bCKv8WKcLcdm0X78kv3dVpTqA7uO1UDg/640?wx_fmt=png&from=appmsg)

其二，这就是存储类的xss，数据存储的页面都存在，无需一直提交恶意代码，便可以一直触发

其三，至于会不会有人傻到点击该历史记录，我认为并不是所有人都是安全工程师，在每次搜索都会出现的情况下，这种概率还是不小的

这期间呢，发生了很多。最后呢，要求src请第三方安全人士判断。我这边最后只看到了所谓的友商下结果的截图，结果是这个漏洞成了存储型的self-xss。询问是哪家友商，还不能说。据理力争下，按照低危收了。至此结束

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=ap...