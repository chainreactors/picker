---
title: 第97篇：对绕过2层waf的sql注入攻击语句的深入分析
url: https://mp.weixin.qq.com/s?__biz=MzkzMjI1NjI3Ng==&mid=2247486788&idx=1&sn=409fdf8714cc64036417e141e740c35c&chksm=c25fc23ff5284b29bedf2fafd5f743e9eaaacfedd2a4959810dc41b57b327e297681a3015406&scene=58&subscene=0#rd
source: 希潭实验室
date: 2024-07-01
fetch_date: 2025-10-06T17:41:22.967054
---

# 第97篇：对绕过2层waf的sql注入攻击语句的深入分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciafoAhx4ZrxW85QFtmsPlKxLWR7urmHJPo0VG24rHS52VHgAlJDTsJwQ/0?wx_fmt=jpeg)

# 第97篇：对绕过2层waf的sql注入攻击语句的深入分析

abc123info

希潭实验室

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

## **Part1 前言**

**大家好，我是ABC\_123**。最近几天的攻防演习蓝队分析中，同事发来一个绕过两层waf串联的sql注入语句，是一个通过折半法猜解数据的盲注，全程设备没有任何告警。我已经好久没见过sql语句在高防护情况下无任何告警的案例了，今天我们就着重分析一下这个语句。

**注：**分析这个数据包，需要基础知识的积累，还要有搭建各种测试环境的习惯。早年听一个APT师傅说的，遇到不懂不确定的知识，就要搭建测试环境。

**建议大家把公众号“希潭实验室”设为星标，否则可能就看不到啦！**因为公众号现在只对常读和星标的公众号才能展示大图推送。操作方法：点击右上角的【...】，然后点击【设为星标】即可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450Dq1Q8s4COc7InkMO0jIGjiaGho1fcJicpibWB4vzvIM1wAib9TiakVECbIM5S0mHCTTeGJJibWtCe25vXw/640?wx_fmt=jpeg&from=appmsg)

## **Part2 技术研究过程**

* **原始sql注入语句**

原始的SQL注入攻击语句截图如下，2层串联waf均没有告警。这个SQL注入攻击的语句，第一眼看上去比较头晕，不太容易看到攻击语句在哪里，新手朋友可能就直接跳过了；再仔细看看，发现了攻击语句的大致位置；再深入分析分析，发现有不少巧妙之处。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciaTLmE5j0wpRE57qMPF5icebnTd9g2HousegeKyLTRT1sMuricVGHstatw/640?wx_fmt=png&from=appmsg)

* ## **判断是oracle数据库**

首先，通过数据包中的**all\_tabl**、**rownum**关键字，根据经验初步判断是Oracle数据库的SQL攻击语句查询。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciaum4icN4SbDlicABCsQ3OuIaKmDnZzCEoRM2XSK9ibepricYecj0h53bH9g/640?wx_fmt=png&from=appmsg)

* ## **超大数据包脏数据掺杂**

接下来看一下这个数据包的起始部分和结尾部分，红队人员是在json数据包中以键值对的方式添加脏数据和填充超大数据包，猜想超大数据包应该会使2个串联WAF中的一个waf放行。印象中，java的json处理组件不一定支持这种键值对掺杂方式，所以这个方法不一定通用。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciacG15VQmqjJib0Lx8xZOaqWyw3aPnuXibUsicD9SMYtTYkM76icHX3OwfrA/640?wx_fmt=png&from=appmsg)

我猜想大概率后台处理json数据包的组件应该是fastjson，而不是jackson，或者是其它的JSON处理组件。为了验证这个想法，我编写了一个demo测试下。

* ## **Fastjson与Jackson数据解析的差异**

对于jackson组件，我编写了如下测试代码。添加脏数据字段**”test111”:”222”**之后，jackson提示找不到**test111**字段，这说明Jackson默认情况下是严格匹配JSON字段和Java类属性的，如果json数据包中含有不存在的字段，就会抛出UnrecognizedPropertyException异常。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuicia8juXY1jvCXD94l5WO7zHU6UsEVZ9gp7h4zsT5ucFpfhwTaN33hicicHQ/640?wx_fmt=png&from=appmsg)

对于Fastjson组件，我编写了如下测试代码。经过测试发现，无论在JSON数据包的前面、中间、后面添加脏数据，都没有任何报错，说明fastjson比较灵活，并没有严格配合；也进一步说明，fastjson组件支持这种掺杂键值对脏数据的方式。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuicia0teZqyibgh3xNMCqQfHH25vSibPuS5pe7kTqGFmYPjiczeQ5LguyhuiasQ/640?wx_fmt=png&from=appmsg)

* ## **注释的混淆视听**

第一眼看到这个数据包中的感叹号**/!12345\*/**，还以为是类似于Mysql数据库的内联注释，但是想想Oracle数据库应该不支持的；又看了看**/\*!/\*W1x2Y3z4tf7T6s/\*!12ef34/\*5gg\*/**这个注释，怀疑Oracle是否能正常解析执行。带着疑问，我们本地虚拟机搭建一个Oracle环境测试下。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciaeWtK82ia1SB6RmMPzCcjQr843tR8aPwBmrSD1aOg0ibrwhhzO6spxKCQ/640?wx_fmt=png&from=appmsg)

经过测试我们发现，**/\*!/\*W1x2Y3z4tf7T6s/\*!1234/\*5gg\*/**是可以正常执行成功的。在一个语句段内，Oracle数据库对注释的处理，应该是匹配的左边第1个/\*及右边的第1个\*/，而中间无论添加多少个/\*都不会有任何影响。猜测攻击者制造多个/\*，也可能为了绕过waf的正则匹配规则。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciakwm9KlEhGR9L1MBibZQkDI6MYMAdmXLq5MWeTJnV5JiasbCpBrDyQ2ew/640?wx_fmt=png&from=appmsg)

接下来对上述sql语句中的超大数据包和注释语句进行剥离，变成如下形式，我们也可以大致看到这个sql语句了。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciatiblbUcPcmFHSWXroXiaicjudm3qNOWoWkPqgtDVp6GFuTvv1uAPlntpA/640?wx_fmt=png&from=appmsg)

* ## **unicode编码及关键字替换**

在绕waf过程中，对一些敏感字符进行unicode编码是常规操作。这里作者对**when**改成了**wh\u0065\u006e**这种形式，使得蓝队分析人员肉眼难以辨别。这里我还想深入思考一下，这个unicode编码是在哪一层被解码的？是tomcat中间件解码，还是fastjson组件给解码的呢？

本地搭建环境测试，使用fastjson组件处理json数据，将属性名**name**进行unicode编码变成**\u006e\u0061\u006d\u0065**，程序运行之后，发现name对象提示正确，也就意味着，fastjson组件在这里的处理是支持unicode解码的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciaUhxQcALqmCRENS7chQ5thfKAMSBU47W9vmQ4GlYkq4mZXibaneaFMtw/640?wx_fmt=jpeg&from=appmsg)

接下来将fastjson的属性值进行unicode编码，发现还原的Person对象的name属性的值是正常的，说明这里支持unicode解码。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciagNaWxialI6EkD4KtBusiaW2r2jJ5hRSuImIDzGj384qEHbq4eBnf1icEQ/640?wx_fmt=png&from=appmsg)

对于Springboot和tomcat的unicode解码问题，我本地搭环境写代码还在测试，需要花点时间，后续写文章再讲吧。经过unicode解码之后，oracle的一个sql语句完整暴露出来了。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciaJT7oVLJcpwJcQUE3Dq6FHeaZOA1paXnmLRicADMZR9uUSiaob4bfBKQw/640?wx_fmt=png&from=appmsg)

* ## **全角空格替换绕过waf规则**

这里还有一个关键点，\u0020是半角空格，而\u3000是全角空格，作者使用全角空格\u3000来分隔关键字，以绕过基于空格的WAF过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450CsniaMhDaDAc2S5pJxHfuiciaxhy3WiblKonSMPhqptV1t0FXWDbQkF885JlNjI7N0Tic8M4tJRANFBhQ/640?wx_fmt=png&from=appmsg)

## **Part3 总结**

**1.** 超大数据包掺杂、脏数据掺杂，结合了fastjson键值对不严格匹配的特性。这里应该是绕过了一层waf，其它的绕过waf手段应该都是为了绕过第2层waf。

**2.** 利用了oracle的注释并且深度混淆，一方面让研判人员难以辨别，另一方面绕过waf的检测规则。

**3.** 掺杂unicode编码，将when等关键字伪装成wh\u0065\u006e的样子，使肉眼难以分辨。

**4.** 使用全角空格的unicode编码，绕过waf规则。

**5.** 使用了case when语句，实现了对sql注入折半法盲注利用。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**公众号专注于网络安全技术分享，包括安全咨询、APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**(replace # with @)**

预览时标签不可点

个人观点，仅供参考

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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