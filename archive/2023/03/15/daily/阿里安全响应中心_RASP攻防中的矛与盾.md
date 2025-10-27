---
title: RASP攻防中的矛与盾
url: https://mp.weixin.qq.com/s?__biz=MzIxMjEwNTc4NA==&mid=2652993159&idx=1&sn=2ebb41eb5d2c071399ff3b79f5648475&chksm=8c9ef9d0bbe970c61b3333a138cf3af31293a843a99e1122e3b08b22cfc1b35506063ce58992&scene=58&subscene=0#rd
source: 阿里安全响应中心
date: 2023-03-15
fetch_date: 2025-10-04T09:36:18.354778
---

# RASP攻防中的矛与盾

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tCS9QJPdcGcMBCvicr91Lu0df0E5zLN9AGPiaUhuAXAyZZG9Md4CZicCbkHcL7hxn22unV0yFicP6NsrU2ZDSSKjyg/0?wx_fmt=jpeg)

# RASP攻防中的矛与盾

阿里安全响应中心

## **引言**

随着第二期阿里云RASP挑战赛的圆满落幕，借此机会，我们今天想和大家聊一聊RASP攻防对抗的思路。

**SQL语义分析攻防探索**

### **防守方视角**

首先从“防”的视角而言，RASP不同于流量层检测产品，它能够通过Hook技术获取完整的执行的SQL语句，规避了传统流量层安全产品在语义分析上因为检测代码片段时造成的准确性问题，这也是RASP在语义分析上的技术实现上的一个巨大优势。

在拿到真实SQL语句和请求参数的前提下，语义分析需要做的事情便是判断用户输入是否导致了SQL语句发生了改变，正常业务场景下的用户输入几乎不会改变SQL本身语义，因此一旦SQL语义发生变化，那么无需依赖任何黑名单，RASP也能判断出当前的参数带有了“执行”的目的，而不是单纯的“数据”

**举例**

```
SELECT * FROM boy WHERE stuname = 'data'
```

当我们对该语句进行parameterize后就变成了

```
SELECT * FROM boy WHERE stuname = ?
```

而如果有用户输入了 data' and '1'='1，那么parameterize后的语句就变成了

```
SELECT * FROM boy WHERE stuname = ? and ?=?
```

那么其实即使该语句是不具备攻击性的，但是该输入使SQL语义发生了变化，无需依赖黑名单，基本就能判断该输入是一个SQL注入。然而SQL语义分析的语法并不能很好的兼容所有类型的数据库，往往通过对数据库特性的研究，找出数据库和语义分析能力的差异性能力，触发了语义分析报错，找出绕过的方式。那么从防御的角度来看，语义分析报错后的防护方案就显得非常重要。用户的输入直接导致了SQL语义报错本身其实已经是是否高危的行为，但往往考虑到业务环境的复杂性，需要结合词法分析和少量黑名单逻辑对该类场景进行二次确认，降低误报的可能性。

类似的检测思路还有词法分析，也是被RASP经常使用的检测方式，原理层面更为简单，核心关注点就是用户输入前后SQL语句的token数是否发生了改变。

![](https://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGcMBCvicr91Lu0df0E5zLN9AoN8iaYxEOEkNfNb9eFtYLxgKr9xnUquTqz9r2bXLARxVDYCKp8QhXGg/640?wx_fmt=png)

### **攻击方视角**

聊完了“防”的视角，那么再来谈谈“攻”的思路。首先我们知道语法分析是在词法分析的基础上分析Payload是否符合SQL语法规则。那问题来了，MySQL、MSSQL、Oracle和PostgreSQL等不同的数据库有着各自不同的语法特性, 开发者如果想全面覆盖不同的数据库需要很大的代价，往往会出现顾此失彼的现象。所以尝试利用特性或者罕见语法知识就有可能绕过这一层面的检测逻辑。

不同的RASP在检测逻辑的实现上也存在着差异，例如有的会有多个检测逻辑的分支，当语义分析无法检测出payload时，可能就会面对强大的黑名单检测，而这一阶段就需要考验对数据库的深入理解和实时分析能力，当然还需要具备极强的耐心。

## **RCE攻防探索**

### **防守方视角**

RCE漏洞的防护往往是RASP的优势检测场景。原因是在RCE场景下，RASP可以通过执行代码的入口，恶意行为出口等多个维度进行hook，从而形成一个纵深的防御体系，达到更高的防护效果。

但毫无疑问，一旦执行代码的入口点被突破，那么防守者就势必面对“代码执行”与“恶意行为”（实际上远不止命令执行一种）之间存在灰色空间的问题，因此执行代码入口的覆盖广度才是RASP检测中最关键的点。

### **攻击方视角**

同样在聊完RCE场景的防御思路后，我们也聊聊“攻”的问题。很明确的事情是在RCE场景下，针对Java反序列化、命令执行的绕过非常困难，因为Java语言下，最终达到命令执行的方式无外乎JNDI注入、各种exec、远程类加载等，将已知的危险点都hook后，基本变得无懈可击。

而通常的检测思路分为两类，一类是对表达式本身的语法进行的安全校验，让某些危险的类在表达式层面根本无法实例化，另一类是绕过表达式层校验后对命令执行等底层操作进行校验。首先达到命令执行的效果最直接的方式肯定是调用exec，但很明显这种方式在实际环境中很难突破检测。我们往往退而求其次，尝试寻找任意文件写入的方法，例如：可以写计划任务或者覆盖jar包达到RCE的效果。为了更高效更准确的找到目标类，我们可以使用CodeQL辅助发现。同时为了最大程度的避免表达式层面的检测，这里查找了公有静态方法中对文件写操作的调用

```
import javafrom MethodAccess c, Callable cbwhere c.getCaller().isStatic() and c.getCaller().isPublic() and cb.hasName("newOutputStream") and cb.getDeclaringType().hasQualifiedName("java.nio.file", "Files") and c.getMethod() = cbselect c.getCaller()
```

![](https://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGcMBCvicr91Lu0df0E5zLN9AyJ0nyiaOBQv0m5709be88U6f27I9BY7u7OFyAxJRCluVwMk6LEmJhcQ/640?wx_fmt=png)

在得到查询结果后，接着去分析下源码，进行相应的代码构造，便有机会能够发现防御逻辑的漏网之鱼；当然还有一些其它场景下的思路，比如：文件内容可控但文件名不可控的情况，对于这种情况可以考虑去搜索下类加载的调用，通过写入jar包后再进行类加载，那么可以通过ClassLoader来加载本地jar包的方法，尝试达到RCE的目的。

## **总结**

随着0day的不断高频爆发，RASP这款产品开始走出当年的实验室产品的理论，一步一步走向安全人员视角。凭借云上的大量及复杂的业务场景，为阿里云RASP的稳定性提供了最佳实践，但基于RASP攻防相关的经验却很难依靠内部的一己之力实现大力的提升，尤其在RASP刚刚展露头角的今天，RASP攻防还未成为一个黑客们重点研究的课题，通过挑战赛中不断的攻防对抗积累为RASP提供攻防场景下的最佳实践具有巨大的意义。

在这里再次感谢两届RASP挑战赛中的每一位参与的白帽子，尤其感谢两位白帽子：皓月和yemoli提供的攻击方视角分享。

阿里云RASP挑战赛也会不断举行该类赛事，并发表相关内容，提升RASP攻防领域的交流与提升。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc4qyoL5yEDEwCA3qymRyXXXWS4kTrduhg01ASfv6cwXQU0e1Td0XuJ63HMLCUrYDhaBchiawDpRxg/0?wx_fmt=png)

阿里安全响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc4qyoL5yEDEwCA3qymRyXXXWS4kTrduhg01ASfv6cwXQU0e1Td0XuJ63HMLCUrYDhaBchiawDpRxg/0?wx_fmt=png)

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