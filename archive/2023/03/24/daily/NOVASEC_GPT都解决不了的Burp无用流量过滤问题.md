---
title: GPT都解决不了的Burp无用流量过滤问题
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247488798&idx=1&sn=6426cbfe877da8863e857e7157c226e5&chksm=fad4c809cda3411f2afcf772e8e2d21e8a4ab266cb197ff8f31380f07c32dab28b1d1bc45464&scene=58&subscene=0#rd
source: NOVASEC
date: 2023-03-24
fetch_date: 2025-10-04T10:32:39.316192
---

# GPT都解决不了的Burp无用流量过滤问题

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDrNwHEKT6HUJxjmCPAqAa8j3C3yI1gFIrTGZNMJwpBEtICqgBgpDYrA/0?wx_fmt=jpeg)

# GPT都解决不了的Burp无用流量过滤问题

原创

酒零

NOVASEC

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZD3vpyEbx2sfib5HhNEjuVXnoYe3M7qUXlIomNib7kfpduQSiaLbicprBPY3Ag6cTOYibxFhia2bTuzd0zQ/640?wx_fmt=png)

**目录**

0x01 老王的问题

0x02 一本正经胡说八道的ChatGPT

0x03 自动删除流量包的解决思路

0x04 基于Exclude Scope的解决思路

0x05 实现Exclude Scope API的BUG

0x06 通过操作项目配置文件的API实现

0x07 操作项目配置文件的API扩展

0x08 总结

***△△△点击上方“蓝字”关注我******们了解更多精彩***

**0x00 前言**

前段时间团队的数据安全工程师(老六)写了他利用ChatGPT打破数据安全壁垒的故事。

[打破技术壁垒！数据安全运营与ChatGPT联动的初探](http://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247488702&idx=1&sn=b3e79cb244ec8e61d211d6efb5595dc3&chksm=fad4c9a9cda340bf33effa0c4b49cc1a95e9bbb6d4258afee36dc127a3915720e13efe95eed7&scene=21#wechat_redirect)

我才算是看明白了，普通的数据分析工程师基本上就是把ChatGPT当成一个会自我总结的搜索引擎使用的。当然，也有高级的程序员会用ChatGPT来实现自动代码审计分析，真的厉害。

**0x01 老王的问题**

恰逢其会，老王（化名）问我有没有办法**解决****在Burp上存在很多和测试无关的流量的问题**。

开始没理解这个需求的作用，因为Chrome和Firefox浏览器下我平常都是通过**Proxy SwitchyOmega**等转发先做的一次域名过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiafZ0NB832oicPN70QPSkov6W7rur4zut8k27PiaicRFVmib9MTXrCsqBKbQ/640?wx_fmt=png)

```
FelisCatus/SwitchyOmega: https://github.com/FelisCatus/SwitchyOmega
```

随着过滤规则的增多，平常测试的时候已经很少能遇到影响测试的流量。

但是也有被忘记的情景**，SwitchyOmega**插件只适合PC上使用。

**如果遇到了APP渗透等非浏览器访问的场景下抓包的需求，就没有办法了。**

想起来以前也确实遇到过这个问题，但是没有成功找到好的解决方案，最后才使用的浏览器插件方案。

最终决定基于强大的ChatGPT找找解决方案。

**0x02 一本正经胡说八道的ChatGPT**

开始是想看看有没有办法，阻断某个域名的流量，并且不显示在历史流量窗口。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDsxdjYvW7AibnyrJkqwJ50VqIiaupfuibkGagzQvUb1P6rmpib2EHPUjjIQ/640?wx_fmt=png)

意思是拦截客户端请求设置里有个Drop选项

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDb5hIb5O25bawEaEqH92MeRFQ0yWbN3fo63RI8NibEUtP7sr1a6JPUhw/640?wx_fmt=png)

发现实际上规则匹配中并没有这个Drop功能。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDTAFbibzZExnzAGuEeQKv6zsCpBC7iavJ1JKy9QPEyezUO9tJlckFf3Tw/640?wx_fmt=png)

再问，ChatGPT说可以先把要抓的域名加入Scope，再在拦截页面通过手动Drop报文，这个时候就不会在历史流量模块记录。

这个回答比较鸡肋，手动删除每一个报文，哪里还有时间测试。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDxyAxrMHIYx6Xja40glP4kwsxtJ1DGN7Y8tSNapzgNTicznxSUI6OyHg/640?wx_fmt=png)

而且，实际测试发现删除的包也会存在于历史流量中。

后面再询问ChatGPT就发现它的CPU烧坏了，开始忽悠我了。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDAoNBsmFx3EGlcQQRsT8dnusVNzEVmjQkYovICRCA9uiaSGmrgeDNMTw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzDKJYNXaxzebniaUX8SpKGlUSQg9p8icKKTWcqWkyJiaXtZib1qtjvlFSaKw/640?wx_fmt=png)

再查了查Burp的API，想看看有没有API操控这个流量记录，结果是**没有找到操控流量记录的API**。

兜兜转转发现确实没有办法直接解决 通过Burp的流量不在Burp历史流量记录中显示的问题。

**流量**来过**了就是来过了，Burp可以无情，但是确实没有办法无痕。**

**0x03 自动删除流量包的解决思路**

退而取其次，老王说他的主要目的就是能够 **在测试过程中不看到这个流量记录**，只要测试时看不到可以就当他没进来过。

所以就开始寻找 如何在流量历史隐藏无用流量 的方案。

历史模块中可以通过很多方案来过滤报文，但是大多都是针对性的过滤（如后缀、类型、状态码等），没有办法直接区分有用和无用域名的流量，不太通用。

看到其中有个隐藏无用响应的功能，如果**结合能自动删除指定域名的报文的插件，并且设置不显示无响应浏览，就能够实现无用域名流量的过滤**。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCsYuh4TfdEQibOnO2sbAQzD7oke8kADwnjZk8AIXaVqsZBD44nXdBCuNtnb1OXFDuWUkyicJS27PUQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiapW21icDy67bOicCc6cKxyKiaEGE2e8FGibdCib5XzicAvicnic5cdn6KpNkucg/640?wx_fmt=png)

刚好前段时间发文描述的Knife插件中有个dissmissed功能，可以自动删除指定域名的报文，结合起来刚好解决了这个问题。

```
bit4woo/knife: https://github.com/bit4woo/knife
```

Dismissed -> Drop Host：**自动drop后续来自当前Host的流量，不发送请求。可以配合History上方的过滤器"Hide items without responses" 使其不显示在History中**

**0x04 基于Exclude Scope的解决思路**

推荐给老王这个Drop方案以后，我觉得此事已经结束。但老王又提了一个BUG:

```
Drop以后我访问不了百度了，我要访问下百度，但是还不想看到百度的流量。
```

这就是Drop解决不了的问题了，又开始寻找新的解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaoXk2FoZby2TcNPhMvqvLJ3hlUzmLCQxqRZTSBFNNCcicmBocQcWLrtA/640?wx_fmt=png)

想到这个Show In-Scope这个从接触Burp至今都没怎么设置过的功能。

以前感觉这个功能很鸡肋，不能包含或者排除自己想排除的host，只能针对某一个URL来操作。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaibQvVOhovRJGYUK6SyAhT3CfS5dHGibaY6TEDhM5uzuRwydvicu0dNcKQ/640?wx_fmt=png)

Burp右键自带的的add to scope也是基于URL的快捷操作，实际测试感觉没什么用处。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaSJTFXw5xywUeKKMFVicpnOTOvDBibXJ3D8ahEvo7FjsWUjibdJTVVtAiag/640?wx_fmt=png)

**渗透测试时的操作都是基于域名来的划分范围的，只操作URL没有任何意义。**

打开Target ->Scope设置，发现**当前版本(2022.8.5)支持通过正则表达式来配置Include in Scope和Exclude from Scope。**

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaicvVFuts2P9ybVuxia5NxQFMiajZLDmyNwccSPp0eyU09akUIMqUEQMdg/640?wx_fmt=png)

不知道是什么时候出来的功能，但是测试发现 **能通过高级Scope配置来实现排除指定域名的功能。**

排除指定域名示例，如.\*.baidu.com：

```
配置Include in Scope 为 [.*]配置Exclude from Scope [.*\.baidu\.com]
```

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdia1oNhoviaicHHqtDVSSTG5KCMqaf32LgTnuibMkSCjJPv9FAWjdoicHgmmA/640?wx_fmt=png)

添加Scope规则

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaKnn4BYFAJ3ia45OqpGLC9qSJtwyLZI4icY0kBwr4uTYt0e3DFALic4YxA/640?wx_fmt=png)

Show In Scope过滤前

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaacLPKseOkUJeL1iad0B8ynby4mjBhUeugqWdOUz4fjEp96BUsHKSlibA/640?wx_fmt=png)

Show In Scope过滤后

测试发现成功排除了baidu.com的所有流量，并且其他流量都在Scope范围内，也不影响主动扫描Scope等操作。

但是**高级Scope设置操作过程都是手动的**，如果能够通过右键实现是最好的。

打开Knife插件，发现它右键有个[**Add Host To Scope**]**功能，能将当前选中的所有请求的HOST都加入到Include Scope当中。**

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaR0NcCNuh03k4lVD2cXXqtPdPeeCnaIKk65KeT8Gwibe91a6VJKFoV5g/640?wx_fmt=png)

研究发现是使用Burp的includeInScope API来实现的:

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaBHHicLU8BgXhNjYgR1S6fTsHnNxUfqOFMibqmNVmvicpricJxP5tY6eexg/640?wx_fmt=png)

knife add host to scope源码

通过处理URL为 短URL格式（根目录），来实现包含某个主机的域名范围。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaibVghuXX8dc6lXLu8ibDJSuGlhL3icBxq75rTb6cy8PNjLTXG6mI2BuKQ/640?wx_fmt=png)

knife add host to scope效果

另外发现Burp还有个excludeFromScope API,同理可以实现将主机的短URL排除掉。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaOiawctBkiaxTGsrAdo5qQMU2eyefqIFgVbUC5BGMKSW7licw7GYkpnYEw/640?wx_fmt=png)

通过拷贝代码逻辑，成功在knife中添加了一个右键功能[Add Host To ExScope] 将域名添加到排除范围。

（不得不说，Knife在扩展性这块很友好）

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaMj3I1ja3QE2WMnw23bQia8pwh1Gu3DjMcFC95of2T4AYmOyG6QmjasQ/640?wx_fmt=png)

**0x05 实现Exclude Scope API的BUG**

测试发现这块还是有较大的瑕疵。

如果只添加了排除Scope，默认不会设置设置包含Scope为 [.\*]号:

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaPibqeA9YCBWSxvTibCNiavsc2rpzqYNsZUHtL4wcFBEKbDSwnySWgl6pw/640?wx_fmt=png)

注：这里因为操作前手动开启高级模式，所以显示的是正则，默认普通模式是显示过滤前缀.

实际使用InScope过滤时会发现一个流量也不显示：

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdia3l8Xmtib9sBdEsq4P3PDwwmibEZExK6h7vxvKVdO3ZbrwJLxMMrQwvwQ/640?wx_fmt=png)

因此，**需要在发现InScope为空时，添加[.\*]到包含Scope，但是发现没有判断Scope为空的API,并且API不能够添加 [.\*] 域名**。

只有一个判断URL是否在Scope内的函数[isInScope]，而且也只能基于URL操作，不能操作[.\*]和[http://.\*]。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiaZxat8eROrxXC8OhvjG3I5b2WhxpWbCYWSVX0haibpg70tpNibOWsyptQ/640?wx_fmt=png)

尝试在添加完排除范围后在自动设置一个[.\*]到Scope，发现URL这里就不可行。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiamqVH4PtLKtx1tvumCUeVEBfAd3BnncRaysyrymjXTOzOLV8MlaoFIQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiap0bxl7lgKOwQNPnKuDAJOohf1Wsyl1nIgl248ak3GQvNzoWSMqGqhg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiavg5g6nAibx9kcbOu4vqnKdpCkkQxc18ricdKbHTDoc1aohEf8Lib4R2fg/640?wx_fmt=png)

需要通过其他的方案来实现 **添加通配符域名[.\*]**。

**0x06 通过操作项目配置文件的API实现**

查找了很久的API发现两个比较有用的API：

```
String saveConfigAsJson(String... configPaths);获取当前项目配置文件的Json格式
```

```
void loadConfigFromJson(String config);将Json格式的配置文件导入到当前Burp项目结构中。
```

另外发现**Scope设置也在项目配置中**、并且配置是实时生效的。

![](https://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZCSozDUB6ichjKeN7pIfEVdiadauPicbYLG0jJlpHyHWQFcshh06qfQzhiaLf2XIPgE...