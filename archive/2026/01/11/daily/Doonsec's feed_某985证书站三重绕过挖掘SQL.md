---
title: 某985证书站三重绕过挖掘SQL
url: https://mp.weixin.qq.com/s/-IivJLaX8UOcKsTvF4nkIw
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:24.687754
---

# 某985证书站三重绕过挖掘SQL

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv1zcTU2jeJ23D7ZcpaEcjibICfhhlribnSvv9zVoSWeRDZyX3zgn8aicvRA/0?wx_fmt=jpeg)

# 某985证书站三重绕过挖掘SQL

原创

夜子

夜子安全Sec

![]()

在小说阅读器中沉浸阅读

小生不才，愿得自身的一己之力能集齐证书18铜人。通过不断地深入学习到SQL注入时，发现自身在绕waf这方面有着众多的经验以及思路，大部分的证书站基本都是sql注入居多，这次的案例也是非常有意思的，该证书站有着很多限制，导致我考虑了众多SQL语句下，成功拿下该学校的中危漏洞，话不多说，来一起看看这波案例。

![](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv1qFEujw6jEuXNZr09d34niaNX4ToTVtLd6OMaezU4Oq9iaLzPxmKASosg/640?wx_fmt=png&from=appmsg)

依旧通过微信的一些资产进行一个切入点，可以看到这边存在一个目的地和初始地的地址查询，一般这块区域可能存在sql注入，我们通过进行一个抓包的查询递进。

![](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv100VXnZNqcIR0v8kPjZX6JvAghs4ECKibSnOOC6fNPyUSuDuGBZXnGpA/640?wx_fmt=png&from=appmsg)

可以看到这个数据包中不存在任何传参点，没有用户控制的参数传递，我们直接忽略掉此数据包，下到另一个查询点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv1fzfhoG6HowiaJF1CsXSYdbTx7iaBVe2jNhRlCCAoTT27UYUGV6ad2cuA/640?wx_fmt=jpeg&from=appmsg)

这个页面有意思的点就是，他是个班车，你得在特地的地方包括特地时间才能会有该页面的数据包以及数据的传输，否则只有空页面返回并且不带任何的数据包传递。由于我写文章复现的时候已经是晚上了，所以已经不存在该班车的站点。只能说这个资产有点阴间，一般的师傅可能拿不下这个站点。

![](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv1Zj59TkdeNIH9U4LgIHZvpiaaZibYWY7ab0vMuCKSulNtp93JNGOwhWicg/640?wx_fmt=png&from=appmsg)

这是在工作时间段的班车的页面，该页面存在sql注入的数据包。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv1RaVygyuchq321ezNHUV2aZVr91CwibWBomicxrLhYgbPDicHmvhtnbLOQ/640?wx_fmt=jpeg&from=appmsg)

前期下，我们通过数据包中的my\_station值进行一个注入，发现存在我们的常规判断，单引号报错404，双引号正常回显，如果有师傅不放心的话们可以在加到3个单引号报错和4个单引号，观看返回包的内容进行一个判断。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv1s10d51CQmEH9JGbRmaZl8iaGbzgxc2lh4WOqoPJWboyriaPkiatftVuZw/640?wx_fmt=jpeg&from=appmsg)

依旧常规的闭合，发现直接存在waf，看着有点像云waf。不清楚哪家的

![](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv147q6Q4LVOZYCib1AL038ZNr8y0XSBsGuf6lKM7BCibganiavwYcc2XbwA/640?wx_fmt=png&from=appmsg)

通过脏数据，不断地去干扰waf判断，最终使得waf疲惫，直接插入一堆%0a 再加单引号 and '1'='1,成功地闭合返回数据。自此我们成功地绕过了第一层的waf判断，接下来我们就美滋滋地去判断该数据库是什么类型的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv11uRFdWsic0NIbWJrD9XtRWxr0lIrrggVic0OgemqYEoGjH70RhDujDIg/640?wx_fmt=jpeg&from=appmsg)

当我利用 and 1=2 或者or之类的进行判断布尔，发现页面始终是如上图一样，没有任何的变化。这样使得我们判断难上加难。最终我通过 and 1=1/0 使得一个布尔值的分母滞空，发现页面返回404，看来可以通过这种方式进行一个布尔的判断，但是我们现在还是不清楚是什么类型的数据库，接下来我通过一些特征函数进行判断，发现页面始终是404返回。

![](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv1ZEQ9uGg8EJMoIib11WL92jkkdyuKTxn4WkDBgERYUnktTibFaicy9PP8A/640?wx_fmt=png&from=appmsg)

例如我使用length函数以及len函数，页面依旧404，这让我不得不想到是否存在函数过滤，常规的函数肯定是行不通的，什么延时包括截取字符串的函数都行不通，不管是冷门还是热门的延时函数全部过滤，过了一难又一难。从waf到页面判断再到函数过滤的绕过，这不得不让我火热了。最终，我通过该payload，成功使得页面有正常回显。看样子可能是mssql或者oracle，不过必须要存在另一对的布尔值才能返回正常否则404，进而可以排除oracle，只能是mssql数据库的特征了。

payload：and 1=1/ascii(user) and '1'='1

![](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv1aibv3yGxP2EpvibbDIcibmibo8qBsYQ8K62m1Ebtee8eMVFicIeicsVBT9jg/640?wx_fmt=jpeg&from=appmsg)

由于大量的函数被过滤了，我只能通过right和left函数提取ascii再判断分母值，但这样只能提取出两个ascii值，接着我通过审核师傅的对话，也是了解该方法也是能通过的。

![](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv1HTrW0y9GHx4TPSdAgjybeDoJNnU6IPoZibOkMZFBCkV6vlXibQBH3YKw/640?wx_fmt=png&from=appmsg)

最终payload：

一堆%0a ' and 1=1/(ascii(right(user,1))-\* and '1'='1

一堆%0a ' and 1=1/(ascii(left(user,1))-\*) and '1'='1

![null](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv1pibIpYIhYBeeUGyb2niaiatVENDSeeibzlAovPE3VwhKSvpvSXbbVSb9Fw/640?wx_fmt=png&from=appmsg)

![null](https://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSu8SSMjUjNMJzz6In27NIv1ssbozXY2FMBB4X0IjAckJX70OG1uE2xeV5O6v7jHy2zDd1BsiajiaYdA/640?wx_fmt=png&from=appmsg)

成功拿下此证书站，该站点适合在阳间时间打，阴间时间挖掘的师傅可能就错过该漏洞点

![](https://mmbiz.qpic.cn/mmbiz_jpg/zELLsYstVSu8SSMjUjNMJzz6In27NIv1ECkuHfPtGbMRK3noo1YzzCWCLRQk95ibVgupibRDVCCgLz7Nicx4SFMwQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSse9raZficWiaml7ckOvRB2m29hIrQf5JVyickflqiapnibz5r5nyIsWhj4LqjV8Qrn8fFAT5lhx6AMoDw/0?wx_fmt=png)

夜子安全Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zELLsYstVSse9raZficWiaml7ckOvRB2m29hIrQf5JVyickflqiapnibz5r5nyIsWhj4LqjV8Qrn8fFAT5lhx6AMoDw/0?wx_fmt=png)

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