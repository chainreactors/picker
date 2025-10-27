---
title: 深入浅出Joern（二）CPG与图数据库
url: https://buaq.net/go-175196.html
source: unSafe.sh - 不安全
date: 2023-08-24
fetch_date: 2025-10-04T11:58:51.264269
---

# 深入浅出Joern（二）CPG与图数据库

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/fd8925bd157f6a4f379975ad39bf20f3.jpg)

深入浅出Joern（二）CPG与图数据库

在上篇文章里，我们从Joern入手大致介绍了CPG(Code Property Graph)的设计理念和简单逻辑https://lorexxar.cn/2023/08/21/jo
*2023-8-23 21:10:3
Author: [govuln.com(查看原文)](/jump-175196.htm)
阅读量:51
收藏*

---

在上篇文章里，我们从Joern入手大致介绍了**CPG(Code Property Graph)**的设计理念和简单逻辑

* <https://lorexxar.cn/2023/08/21/joern-and-cpg/>

但实际上来说，如果想要更深入的了解Joern，**CPG和图数据库**是绕不开的一个话题。CPG作为一种**代码属性图**，就必须寻找一种图数据库作为载体，就像我们常用的数据和SQL数据库的关系一样。

旧版本的Joern使用的**Gremlin**，但后来的开发中换成了**OverflowDB**，在joern中也完全支持使用**OverflowDB的查询语法**。

* <https://github.com/ShiftLeftSecurity/overflowdb>

但属性图本身没有什么特异性，比较常见的比如**Neo4J，OrientDB**或者**JanesGraph**都支持CPG的表现形式。

但，在这之前，我们首先需要知道，**为什么是图？**

在上篇文章中，我在讲了CPG的设计思路时曾经提到过一些相关的内容。

如果说CFG(**control flow graphs**)相比AST来说最大的特点是**带有明确数据流向的流向**，在数据流分析**可能**更有优势。

那么CPG相比CFG来说有一个很大的特点就是**信息量大**，而图最大的特点也在于，就是**可以容纳信息量巨大的内容**。

假设我们有这样一段代码

|  |  |
| --- | --- |
| ``` 1 ``` | ``` a = new A() b = a.b c.a = b.a d.a = c c.b = d.c ``` |

这里简单的几行代码，其实展示了相当复杂的依赖链，abcd几个变量中有着复杂的互相指向关系，如果**用文字来表示abcd之间的关系我们可能需要拆分很多部分。**

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` a -> A() b -> A().b c.a -> A().b.a c.b -> .... ``` |

我甚至很难用文字的方式表达出他们之间的关系，而**图在这样的场景下就变得很有优势。**

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692605645328-0ebeba5b-1f53-43c2-aea3-10bc8d236a61.png)

当然这只是一个粗浅的例子，但已经很明显的能感觉出来图和文字之间的差距了，**图关系可以很轻松的表达出文字很难表达出来的信息量。**

Joern用了CPG来**储存代码的所有节点关系和属性数据**，由于CPG的信息量大，所以Joern甚至**提供了官方的生成AST、CFG等其他结构的接口**，对于C/C++甚至支持多种自定义的结构。

* Abstract Syntax Trees (AST)
* Control Flow Graphs (CFG)
* Control Dependence Graphs (CDG)
* Data Dependence Graphs (DDG)
* Program Dependence graphs (PDG)
* Code Property Graphs ([CPG14](https://www.sec.cs.tu-bs.de/pubs/2014-ieeesp.pdf))
* Entire graph, i.e. convert to a different graph format (ALL)

在Joern的命令行你可以直接**使用相应的命令生成对应的格式**

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` cpg.method($name).dotAst.l // output AST in dot format cpg.method($name).dotCfg.l // output CFG in dot format ... cpg.method($name).dotCpg14.l // output CPG'14 in dot format ``` |

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692606692896-ee663c85-77fc-4887-b05e-0b7d83d0a7cb.png)

有个很有意思的是，如果你的电脑装了**Graphviz**，Joern还可以调用Graphviz来绘图，虽然生成的图很难看。

* <https://graphviz.org/download/>

安装Graphviz之后我们可以通过命令来绘图

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` cpg.method($name).plotDotAst // plot AST cpg.method($name).plotDotCfg // plot CFG ... cpg.method($name).plotDotCpg14 // plot CPG'14 ``` |

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692607237756-6bbaab5a-1950-43ae-ac7a-45598be7de99.png)

说实话，不太实用，但是很方便

相比Graphviz这种仅仅用来临时展示图的应用来说，**Neo4J则是标准而且非常成熟的图数据库**，不但性能强，而且还实用。

* <https://github.com/neo4j/neo4j>
* <https://neo4j.com/>

你可以在官网下载免费的neo4j，其中包括服务端和客户端版本，服务端版本启动后会默认跑到7474端口上。

**Neo4j使用的查询语言叫做Cypher，这是一种声明式的图查询语言**，我个人觉得Cypher其实算是比较反人类的一种语言，具体的语法可以看对应的文档。

* <https://neo4j.com/docs/cypher-manual/current/clauses/>

简单来讲**Cypher中对应SQL的语句关系有几个比较特别的**，首先就是MATCH和where。

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ```  select Person from user where born = 'beijing'  MATCH (a:Person)-[:BORN]->(b:Location {city:'beijing'}) RETURN a,b ``` |

MATCH和where在两种查询语句中是类似的功能，其中的区别就是**MATCH匹配的是图中节点之间的关系。Cypher语法比较强调节点之间的关系**，比如-就是无方向关系，->就是有方向关系。

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` match    (node)-[relationship]->(node) where   （node  |  relationship) return      (node | relationship) ``` |

其他的比如创建节点、删除节点、创建关系、搜索匹配的节点以及关系等等就不赘述了，算是比较符合理解的语言逻辑。

而相对于普通的数据库来说，**图数据库有着可能是一种优势的特性，就是可以直接通过Neo4j的浏览器直接操作图内容以及结构。**

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692611086028-45813553-8ed8-4bbe-a9b6-e3edcf466eb5.png)

直接**用鼠标点击各个节点查看对应的属性以及它们之间的关系**，并且可以直接拖动他们。

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692611176176-ba4228f9-679e-404f-9427-3b805d72306c.png)

点击节点下面的按钮，可以直接**查看到节点连接到的其他节点**，很方便也很直观。

前面说了，**Joern使用了自己做的OverflowDBl来作为图数据库存储CPG**，但CPG本身没有什么特异性，也就意味着他可以在任意一种图数据库上导入。

而Joern本身是自带了这个功能的，就是joern-export。**它支持你导出Joern的CPG到neo4j , graphml, graphson 和 graphviz dot。**

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ./joern-export --repr=all --format=neo4jcsv ./joern-export --repr=all --format=graphml ./joern-export --repr=all --format=graphson ./joern-export --repr=all --format=dot ``` |

要使用joern-export导出数据的话，**需要指定CPG的位置**，这个东西会存在**Joern目录下的workspace**当中，并且需要指定output，默认是./out。

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692612074584-1dabd5b0-eb0d-4bcd-a335-d2f3463bf756.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692612106007-3353f4cb-a061-4190-8615-32bc3b82fdac.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692612120641-a4eb94e1-226a-4633-811e-2167699e9eed.png)

然后我们可以想办法**把这些csv文件导入到Neo4j当中**。当然你可以用一些自己的方式导入，但joern的这个图还挺麻烦的，主要是**neo4j导入复杂结构数据需要指定好各种csv文件的关联。**

但joern当然也给出了导入的办法，在生成文件的时候会**给出一个导入命令的范例**，照着范例就可以搞定了。

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692685954936-2ba4b2bf-6717-4651-9266-f7e9e72ef8d8.png)

首先joern导入数据是有限制的，**只能导入import目录下的文件**，这个import文件一般会在对应链接的server目录下面，如果你使用的是neo4j的desltop浏览器，那么你可以直接打开对应的import目录，并把文件复制过去。

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692686066774-fcd82322-c672-4036-bb1e-255fb8c2c9b4.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692686088202-c8437685-eea7-42e5-b448-ddd339e7c490.png)

除了文件以外，还有就是这个/bin/cypher-shell的位置，**这个脚本就在对应链接目录的bin下**

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692686293588-7f992135-6cf4-4b52-8549-fc0d78a4eec2.png)

然后构造对应的find命令生成执行导入即可，其实它的原理也比较简单，就是**依次执行\*\_cypher.csv文件中的命令，然后导入header和data。**

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692686369841-2877744a-e1ad-454e-aefa-d2ac3fc3fc59.png)

最终导入的数据就是这样的

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692686394254-27867c81-96d4-4637-ac60-5927deaf9985.png)

当我们把CPG导入到Neo4J上之后，理论上来说我们可以用cypher来完成我们在Joern中做的所有工作。

这里还是拿上篇文章中用到的RCE代码来举例子。

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692688121461-b1e506bc-a0dc-4e82-ab4b-e38200ed382c.png)

对应Joern的语句为

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` def source = cpg.method.where(_.annotation.name(".*Mapping")).parameter  def sink = cpg.call.name("exec") ``` |

首先匹配注解节点满足.\*Mapping的

|  |  |
| --- | --- |
| ``` 1 ``` | ``` MATCH (n:ANNOTATION) where n.NAME=~".*Mapping" RETURN n LIMIT 25 ``` |

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692688861730-ef39cec8-026b-4868-9c3c-55b4c35b4d77.png)

然后找这些对应节点关联的方法

|  |  |
| --- | --- |
| ``` 1 ``` | ``` MATCH (m:METHOD)-[:AST]->(n:ANNOTATION) where n.NAME=~".*Mapping" RETURN n LIMIT 25 ``` |

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692689267831-15c53e14-0fe0-4b34-ba8d-927d475cdf06.png)

然后找一下对应调用exec方法的节点

|  |  |
| --- | --- |
| ``` 1 ``` | ``` MATCH (n:CALL) where n.NAME="exec" RETURN n LIMIT 25 ``` |

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692690581420-4b2f173f-f613-4529-a7fb-84f769f9db40.png)

然后我们把两个节点连接起来，并查找最短路径，这里的[\*..10]表示最长不超过10个关系

|  |  |
| --- | --- |
| ``` 1 ``` | ``` MATCH (p1:METHOD)-[:AST]->(n:ANNOTATION),(p2:CALL),p=shortestpath((p1)-[*..10]-(p2)) where n.NAME=~".*Mapping" and p2.NAME="exec" RETURN p LIMIT 25 ``` |

![img](https://cdn.nlark.com/yuque/0/2023/png/26687441/1692693277175-15c4a463-4fa0-4120-b86f-83b93304c3f0.png)

这里范例算是比较简单的，所以用这个还算比较简单的语句就可以查询到结果，正好对应漏洞利用链。

文章来源: https://govuln.com/news/url/akpg
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)