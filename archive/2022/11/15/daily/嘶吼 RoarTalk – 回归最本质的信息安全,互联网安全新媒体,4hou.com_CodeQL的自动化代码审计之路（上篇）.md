---
title: CodeQL的自动化代码审计之路（上篇）
url: https://www.4hou.com/posts/wgzz
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-15
fetch_date: 2025-10-03T22:43:41.237066
---

# CodeQL的自动化代码审计之路（上篇）

CodeQL的自动化代码审计之路（上篇） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# CodeQL的自动化代码审计之路（上篇）

盛邦安全
[行业](https://www.4hou.com/category/industry)
2022-11-14 15:19:45

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)153772

收藏

导语：本文主要研究基于CodeQL实现全自动的代码审计工具实现思路。

**0x01 前言**

最近关于CodeQL的概念很火，大家普遍认为这会是下一代的代码审计神器。网上关于CodeQL的文章已经有不少，但是多数文章还是在分析CodeQL的安装和简单使用用例。真正使用CodeQL来进行自动化代码审计的文章较少，本文主要研究基于CodeQL实现全自动的代码审计工具实现思路，预计文章分成三部分完成，目前是第一部分内容。

CodeQL（全称Code Query Language）,从其英文名称中可以看出这是一种基于代码的查询语言，其作用主要是通过编写好的语句查询代码中可能存在的安全隐患。学习CodeQL类似于学习一门全新的编程语言，语法类似于SQL，但是比传统SQL还是要难很多。目前CodeQL支持对多种语言，包括java、javascript、go、python、C、Csharp等，但是很遗憾的是不支持“世界上最好的语言”PHP。这大概是因为PHP实在是太灵活了，函数名是字符串变量这种调用方式确实很难从AST语法树中静态分析出问题，但这并不能阻碍我们学习CodeQL的兴趣。文章所有内容基本上围绕java语言展开，其他语言操作基本类似。

**0x02 环境准备**

网上关于CodeQL安装的文章已经很多了，本来不打算再说这个事情，但是因为本人在CodeQL安装过程中遇到不兼容mac m1架构的情况，我想还有很多小伙伴也会遇到这个问题的，这里主要以MAC的环境来说明安装过程。

CodeQL的安装主要分成引擎和SDK，新建一个目录CodeQL（~/CodeQL/）来保存后续所有的相关的工具和代码。

首先下载最新的引擎包，下载地址是：https://github.com/github/codeql-cli-binaries/releases

下载之后解压把codeql文件夹放在刚才新建的文件夹CodeQL中，添加环境变量。

```
vim ~/.profile
export PATH=/Users/用户名/CodeQL/codeql:${PATH}
```

使用source命令是环境变量生效，然后命令行中运行codeql，如图2.1所示。

![1668409224102247.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409224102247.png "1668409224102247.png")

图2.1 CodeQL引擎安装

然后需要下载CodeQL对应的sdk包，下载地址是：

https://github.com/Semmle/ql

下载之后也需要把ql文件夹复制到~/CodeQL文件夹中。

在CodeQL文件夹中新建databases文件夹，用于存放后续使用codeql生成的数据库，那么一切准备好了之后我们的CodeQL目录之下就会是三个文件夹，如图2.2所示。

![2.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409240187870.png "1668409240187870.png")

图2.2 CodeQL安装

后续我们就可以使用codeql database create命令来创建查询数据库，命令如下所示。

```
codeql database create /Users/xxx/CodeQL/databases/project_db_name --language=java --source-root=/Users/xxx/cms/project_path --overwrite
```

在windows环境中和以前的mac环境中确实没有问题，但是如果是在m1的环境中会报错，报错信息如图2.3所示。错误的原因是codeql官方提供的工具是x86架构的，不能直接在arm中使用。

![2.3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409246131615.png "1668409246131615.png")

图2.3 在MAC M1环境中codeql运行错误

从官网中找到了codeql对m1的支持情况，如图2.4所示。从图中可以明确看出codeql确实是支持m1架构的，但是需要依赖rosetta2和xcode。但是并没有给出具体的安装和使用步骤，必须吐槽官方一点也不人性化，说话说一半。

![1668409259756820.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409259756820.png "1668409259756820.png")

图2.4 CodeQL支持M1架构

后来慢慢摸索着装xcode和rosetta2，安装xcode是直接通过appstore来装的，安装rosetta2是使用下面的命令。

```
softwareupdate –install-rosetta
```

安装好了之后就可以使用下面的命令来生成数据库，与传统方式不同的是需要在命令前面增加arch -x86\_64，如图2.5所示。

```
arch -x86_64 codeql database create /Users/xxx/CodeQL/databases/mvn_test --language=java --command='mvn clean install -DskipTests' --source-root=/Users/xxx/java/projects/mvn_test --overwrite
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/4yJaCArQwpB9frjDWssO86dhHJp8zFbPOnAibliaAqMuWZgnHEeibYzcNYmE3QFS6rZS4bYTtFTkXicMNTVuet3dWA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

图2.5 在M1中使用codeql生成数据库

**0x03 语法基础**

CodeQL是一门全新的语言，基础的CodeQL语法网上已经有很多文章。大家在学习之前可以首先参考链接，了解关于CodeQL的基础语法，重点掌握关于类和谓词的概念。

参考链接：https://longlone.top/%E5%AE%89%E5%85%A8/%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6/codeql/2.CodeQL%E8%AF%AD%E6%B3%95/

直接来学习语法是一件很枯燥的事情，我们这里只是总结一些CodeQL中重点的概念。关于语法详情在后续的实际案例分析中会有更深刻的体会。

1)  与Class相关的概念

与类直接相关的概念包括Class、Method、Field、Constructor，其代表的意义与java语言一致，通过其相互组合可以从数据库中筛选出符合条件的类和方法。

Demo1: 查询类的全限定名中包含Person的类，其中方法getQualifiedName代表获取类对应的全限定类名。

```
import java
from Class cwhere c.getQualifiedName().indexOf("Person") >=0select c.getQualifiedName()
```

Demo2: 查询所有字段Field，满足条件是字段类型是public，并且字段类型继承java.lang.Throwable。（Fastjson1.2.80漏洞利用链的查找方式）。

其中getASupertype代表获取类对应的父类，\*代表递归查找所有父类。

getDeclaringType代表获取字段对应的定义类型。

getAModifier代表获取字段对应的修饰符。

```
import java
from Class c, Field fwhere c.getASupertype*().hasQualifiedName("java.lang", "Throwable") andf.getDeclaringType() = c and f.getAModifier().getName() = "public"select c.getQualifiedName(),f.getName()
```

2)  与Access相关的概念

access代表对变量或者方法的调用，主要有VarAccess和MethodAccess。

Demo1：查询所有继承自java.util.list的变量及变量的引用。

```
import java
from RefType t,Variable v,VarAccess vawhere t.getSourceDeclaration().getASourceSupertype*().hasQualifiedName("java.util", "List") and    v.getType() = t and     va.getVariable() = vselect v,va
```

Demo2：查询所有InputStream类对应的readObject方法调用（遍历反序列化漏洞的基础）。

```
import java
from MethodAccess ma,Class cwhere ma.getMethod().hasName("readObject") and       ma.getQualifier().getType() = c and       c.getASupertype*().hasQualifiedName("java.io", "InputStream")select ma,ma.getEnclosingCallable()
```

3）与Type相关的概念

Type代表类型，是属于CodeQL中一个很重要的概念，Type类有俩个直接派生类PrimitiveType，RefType。

PrimitiveType代表Java中的基础数据类型，派生类有boolean, byte, char, double, float, int, long, short, void,, null。

RefType代表Java中的引用类型，有派生类Class、Interface、EnumType、Array。

Type多数情况下是和Acess相互使用的，其实在上面Acess的例子中几乎都用到了Type相关的类。

4）与Flow相关的概念

Flow是CodeQL中最重要的概念，代表数据流，与此对应的概念包括source和sink。

source代表可控的用户输入点，通常是指WEB站点中的URL中参数，例如

request.getParameter("name")。其他例如命令行参数args也属于source。在CodeQL中已经存在RemoteFlowSource类，在类中已经定义了很多常见的source点，可以满足我们做一般性代码审计的需要。但是如果我们是要做特定jar包漏洞挖掘，例如复现log4j2的远程命令执行漏洞，由于log4j2包中不包含常规的source点，就需要用户自定义source。

sink代表危险的函数，通常是指一些危险的操作，包括命令执行、代码执行、jndi注入、SQL注入、XML注入等。CodeQL虽然也预置了部分的sink点，但是远不能满足实际的需求，需要我们在不同的漏洞环境中自定义sink点。

在有了source和sink之后我们可以基于CodeQL提供的查询机制，自动判断是否存在flow可以连接source和sink，一个典型的用法如下，如图3.1所示。

![1668409339115374.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409339115374.png "1668409339115374.png")

图3.1 典型的flow利用方式

在图3.1所示的Flow中，自定义类继承自TaintTracking::Configuration，并且覆盖其中的isSource个isSink方法。这个是固定写法，后续的绝大部分的ql脚本都包含这样的代码。

其中isAdditionalTaintStep方法是CodeQL的类TaintTracking::Configuration提供的的方法，它的原型是：override predicate isAdditionalTaintStep(DataFlow::Node node1, DataFlow::Node node2) {}。它的作用是将一个可控节点A强制传递给另外一个节点B，那么节点B也就成了可控节点，如图3.2所示。

![1668409392552006.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409392552006.png "1668409392552006.png")

图3.2 isAdditionalTaintStep方法的连接作用

如果CodeQL不能自动连接node1和node2节点，就需要手动通过isAdditionalTaintStep来指定连接。

除此之外，在Flow中还有一个方法经常用到isSanitizer，用法如图3.3所示。这是官方提供的关于log4j2漏洞的查询脚本，其中定义了isSanitizer方法来限制flow流中的数据不能是基本数据类型PrimitiveType和BoxedType类型。这是一个特别常用的过滤机制，代表只要是常规的字符类型（Bool、int这些）则不再进行传递。

![1668409416594559.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221114/1668409416594559.png "1668409416594559.png")

图3.3 isSanitizer方法的过滤作用

**0x04 案例实践**

作为新手来说，要自己编写有效的CodeQL查询脚本是一件很难的事情，幸运的是CodeQL官方为我们提供了大量的demo。

参考地址：https://github.com/github/codeql/tree/main/java/ql/src/experimental/Security/CWE

我们可以直接使用这些demo来完成部分漏洞发现功能。

为了更加清晰的理解关于CodeQL的使用，通过具体案例来演示CodeQL的作用。若依RuoYi是国内使用量较大的后台管理系统，从网上下载到某版本的RuoYi的源码。

1）基于RuoYi的源码生成数据库

```
arch -x86_64 codeql database create /Users/pang0lin/CodeQL/databases/RuoYi --l...