---
title: 记一次梦游渗透从jmx到rce
url: https://mp.weixin.qq.com/s?__biz=MzI2MzA3OTgxOA==&mid=2657165474&idx=1&sn=076b28cf8913b7e1034e1de3f7b0c25a&chksm=f1d4d247c6a35b513c4e2adf94aad5b75dd2a68728a3cbc56c1164be0895d8dbbaa3d4a222d5&scene=58&subscene=0#rd
source: 暗影安全
date: 2024-05-12
fetch_date: 2025-10-06T17:16:35.422282
---

# 记一次梦游渗透从jmx到rce

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PrTu58FA79bFULX2micBEXR4Io2K3tN6Jo6fdV7pvGxicxibfzk6sV2b7yxzYoicwiaXuPxy0kofPT1TKiafSgHicpic6Q/0?wx_fmt=jpeg)

# 记一次梦游渗透从jmx到rce

y4er

暗影安全

渗透过程

发现了一个集成的环境，开了jmx服务

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJksIqjCmiab455xgzL7c522MlgnYDgHcq8uDSCsTB3cHdxf4T1mkGiadg/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

`service:jmx:rmi:///jndi/rmi://1.1.1.157:9003/jmxrmi` jconsole连上去之后发现一些敏感的账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJQJg4Gr65ibry6Hibg8bDFAptHvkmibN0VTTAKgENK0MMrd4hnWGjicyjsQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

在http://localhost:8983/solr 发现了solr，但是历史洞都打不了，log4j是高版本的jdk，并且不出网，所以整个思路就围绕在jmx的利用上。

jmx已知的利用方式有`javax.management.loading.MLet`加载远程类rce，但是目标不出网必须用其他方式了。

考虑到tomcat，想起来陈师傅写过的《几个Jolokia RCE 的“新”利用方式》

通过tomcat的createStandardHost配合AccessLogValue进行rce。

利用如下

先创建Host为test.com `Catalina:type=Host,host=test.com`

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJGbXNg5d6wJJHb0KD8hiblib4Xp3NoZwv76sfJhDxib6FP3G6iaFwtgaUcA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

然后tomcat的valve中就有了test.com的部署之后的结果

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJuh0e8sib2LqbMiaNibRMicicw9v93pibI2lsECwTGeXDMZG9qsgU1l3F9aVQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

修改host为test.com之后就可以访问根目录下的任意文件

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJRmibQezlVSqL41I9LCLeQntToQxMrFSuiafcbKTeibQNrDnYbibr77Xx8Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)那么只需要写入一个jsp文件就可以getshell了。写入文件需要用AccessLogValue

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJzhysErsyUlONNXbeIaqpHias0qJHT6CQsXfoY7q0ew8CoxwYarF5wwg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

修改AccessLogValue的属性

```
suffix .jspprefix aafileDateFormat .yyyy-MM-ddpattern %h %l %u %t "%r" %s %b "%{Referer}i" "%{User-Agent}i"directory /tmp/
```

最终文件路径为`/tmp/aa.2022-09-20.jsp`

pattern会进行格式化，`%{User-Agent}i`表示引用请求头中User-Agent字段

然后发包写入日志文件

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJOM9JHSAG2o9HKCoaL5t1KT81LOK24tLORyFP7W9r6esG5eAX7DmOibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

然后访问shell即可

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJQJ4jicpVrvausHjX7k7p6yuFrTLehypSIFhZ72E6V9KLth5dGmJmvEw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

如果访问shell不存在可以执行一下`AccessLogValve#rotate()`重新格式化日志文件名，确保日志文件名修改为我们想要的值。

![](https://mmbiz.qpic.cn/mmbiz_png/ewSxvszRhM4UU95wvgaUY1WBuRznG6RJxjDlQ46rDNk1S4sz3uMuczK3KGtCW17hlq7aXCT8vumbsXVP99OYbw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

打完记得把配置属性改回去，不然日志文件会越来越大，访问shell比较卡。

# **参考**

看起来简单，但是实际上涉及的知识点很多。比如陈师傅的文章中是在Jolokia中利用，jmx和Jolokia大同小异。另外陈师傅提到的jfr和vmLog写文件在实际环境中不存在，所以用到了spring4shell中的一环即AccessLogValue。

具体不详细写了，直接看参考链接吧。

1. https://articles.zsxq.com/id\_h4mjj2ktw352.html
2. https://sec.lz520520.com/2022/04/714/
3. https://xz.aliyun.com/t/11450
4. https://www.cnblogs.com/0x28/p/15685164.html

```
作者：通过原文地址：https://y4er.com/posts/from-jmx-to-rce/
```

声明：⽂中所涉及的技术、思路和⼯具仅供以安全为⽬的的学习交流使⽤，任何⼈不得将其⽤于⾮法⽤途以及盈利等⽬的，否则后果⾃⾏承担。**所有渗透都需获取授权**！

如有侵权，请联系删除

![](https://mmbiz.qpic.cn/mmbiz_jpg/PrTu58FA79bwwicW0Lg5LyzhwsucDdaP0hr0FHcjJAFUFsXjCHqia5BbgavliabU5SlZ6icq5jNN3VoDoGgRQTJFRw/640?wx_fmt=jpeg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PrTu58FA79arIQGU74rJvbDtBoicQlQ8rMIzfax1Ol2RY5YnbsN82PLkvicB9FLHxFibrF5k7x2N7VXicectIVucibg/0?wx_fmt=png)

暗影安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PrTu58FA79arIQGU74rJvbDtBoicQlQ8rMIzfax1Ol2RY5YnbsN82PLkvicB9FLHxFibrF5k7x2N7VXicectIVucibg/0?wx_fmt=png)

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