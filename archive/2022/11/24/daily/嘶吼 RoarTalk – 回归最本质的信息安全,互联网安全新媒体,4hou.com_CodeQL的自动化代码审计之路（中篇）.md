---
title: CodeQL的自动化代码审计之路（中篇）
url: https://www.4hou.com/posts/pVvy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-24
fetch_date: 2025-10-03T23:36:50.099648
---

# CodeQL的自动化代码审计之路（中篇）

CodeQL的自动化代码审计之路（中篇） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# CodeQL的自动化代码审计之路（中篇）

盛邦安全
[行业](https://www.4hou.com/category/industry)
2022-11-23 10:36:59

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)156607

收藏

导语：本次分享主要关注第二阶段的内容，假设我们已经有了CodeQL数据库之后，下一步基于数据库的自动化查询。

**0x01 前言**

在上一篇文章中，我们已经了解了关于CodeQL的基本语法，从实际案例角度来体验了CodeQL在代码审计中的作用。从这篇文章开始，我们将开始真正打造基于CodeQL的自动化代码审计工具，由于这仅仅是来自于个人兴趣的研究，并非来自成熟项目，所以在文章中可能缺陷，各位大佬如果有更好的意见建议，请私信。

CodeQL的代码审计整体过程可以分成两个部分，如图1.1所示，分别是从源代码解析成CodeQL数据库和从数据库中查询出安全隐患。本次分享主要关注第二阶段的内容，假设我们已经有了CodeQL数据库之后，下一步基于数据库的自动化查询。

![1669107334860801.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108184534504.png "1669107334860801.png")

图1.1 CodeQL代码审计过程阶段

为什么我们最终结果得到的是安全隐患，而不是漏洞呢？这是因为CodeQL并不是万能的，它只能帮我们找到可能的安全隐患，而不能一定确认漏洞存在，这在后面的文章中会说到原因。

当前的自动化代码审计工具将采用python3开发，针对的目标语言是java，后续如果有时间，也会陆续支撑其他语言。目前代码还不是特别完善，后期后继续对代码进行优化，见github地址：https://github.com/webraybtl/codeql

**0x02 工具设计**

基于CodeQL的自动化代码审计工具流程其实和传统的漏洞扫描工具相似，所以我们还是按照传统漏扫的思路来设计工具。关于第一阶段源码转化为数据库的部分在下一篇文章来详述，这里还是只关注第二阶段数据库查询的内容，如图2.1所示。

![1669107433125869.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108184106217.png "1669107433125869.png")

图2.1 自动化工具设计流程

其实从流程中可以看出，工具的主要功能是基于ql插件的遍历，对插件结果的格式化输出。首先需要解决的问题是关于ql插件来源的问题，在上一篇文章中，我们有提到CodeQL官方给我们提供了很多测试用的demo实例https://github.com/github/codeql/tree/main/java/ql/src/experimental/Security/CWE。

官方按照CWE提供了多个不同类型的ql插件，部分插件是可以直接来用的，但是有的插件涉及到自定义qll库，需要进行一定的转化才能使用，如图2.2所以，FilePathInjection.ql脚本就是典型的有自定义库的脚本。

![1669107465133842.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108185180921.png "1669107465133842.png")

图2.2 使用了qll自定义库的ql脚本

在我们设计的自动化工具中，为了方便会只查询单个ql脚本，需要把ql脚本中调用的qll库进行转化。转化的方式是显示的把qll库中定义的类和谓词直接定义到ql脚本中，我已经把官方提供的全部脚本都转化了一遍，后续会将完整的代码分享到github。

为了方便统一的对结果进行格式化输出，我们期待每一个ql文件最终返回的结果都是统一格式，所以还需要对每个ql文件最终的返回结果进行约束，典型的demo如下所示。其中select后面的值是ql脚本最终返回的数据。

```
from DataFlow::PathNode source, DataFlow::PathNode sink, BeanShellInjectionConfig conf
where conf.hasFlowPath(source, sink)
select source.toString(),source.getNode().getEnclosingCallable(),source.getNode().getEnclosingCallable().getFile().getAbsolutePath(),
sink.toString(),source.getNode().getEnclosingCallable(), sink.getNode().getEnclosingCallable().getFile().getAbsolutePath(), "BeanShell injection"
```

表2.1 ql脚本输出规范约束

![1669107506172118.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108186679198.jpeg "1669107506172118.jpeg")

由于CodeQL官方并不对引擎开源，我们只能直接使用官方编译好的版本，官方编译好的引擎并不支持python这些语言，只能从命令行进行调用，如图2.3所示。其中-d参数用于表示待查询的数据库路径，最后跟的是要查询的ql脚本路径。

![1669107548398904.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108187197048.png "1669107548398904.png")

图2.3 通过命令行调用codeql查询

由于CodeQL每次查询都需要使用ql脚本文件路径，如果每次查询都需要先生成一个文件，然后查询结束之后再删除文件，代码显得怪怪的。好在python给我们提供了tempfile库，可以稍微优雅的解决这个问题，如图2.4所示。这是一段我项目中检查环境是否准备好了的代码，通过tempfile生成临时的ql脚本，临时脚本在运行结束之后会自动自动删除。

![1669107589108491.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108187170396.png "1669107589108491.png")

图2.4 使用tempfile生成临时文件查询codeql

本来想自己封装了一个类来调用调用CodeQL运行，但是突然看到网上已经有大佬写好了一个相应的类https://github.com/AlexAltea/codeql-python，其实现思路和我之前的想法差不多，本质上还是从命令行调用的CodeQL。然而我直接运行大佬的代码却运行不成功，主要原因还是在于生成的临时文件必须要在ql sdk所在测试路径，路径下必须有正确配置的qlpack.yml文件。所以我在原代码的基础上修改了一下，主要是固定sdk路径为配置好的路径。

这之后我们一个简易的基于CodeQL的自动化代码审计工具雏型就差不多了，后续会陆续在这个框架的基础上优化功能。

**0x03 插件优化**

官方虽然提供了大约59个java的ql查询插件，但是实际上还远不能满足我们的需求，我们希望有更多的白帽子参与进来提供更多的ql查询插件。当前阶段，我按照自己日常漏洞挖掘过程补充一些ql查询插件，如下所示，相关插件均在plugins/java\_ext目录。

表3.1 新增的Java常见漏洞查询ql脚本

![1669107655169855.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108188164929.jpeg "1669107655169855.jpeg")

本次新增只是一个开端，并不能覆盖全部，自知还相差很远。但是不断的优化，总归会有好的效果。由于部分小伙伴对与CodeQL的语法了解甚少，我们用一个简单的脚本Unserialze.ql来说明完整的CodeQL脚本的写法。

反序列化漏洞是java中常见的漏洞，典型的漏洞代码写法如下。这是一段从某应用中提取的真实漏洞的部分代码。

```
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException {    ObjectInputStream objin = new ObjectInputStream(request.getInputStream()); //这里是获取用户输入    response.setContentType("application/x-download");    ServletOutputStream out = response.getOutputStream();
    try {        String dsName = (String)objin.readObject(); //这里是反序列化的点        System.out.println(dsName);    } catch (Exception var11) {        var11.printStackTrace();    }
    out.close();    objin.close();}
```

其中最关键的是用户可控的source点为request.getInputStream()，最后的危险操作sink点为objin.readObject()。也就是说外部传入的postdata直接进行了反序列化操作，则可能导致反序列化漏洞。对于CodeQL中，可以编写对应的查询脚本如下。

```
import javaimport semmle.code.java.dataflow.FlowSourcesimport semmle.code.java.dataflow.TaintTrackingimport semmle.code.java.dataflow.DataFlow
class UnserializeSink extends DataFlow::Node {    UnserializeSink(){        exists(MethodAccess ma,Class c | ma.getMethod().hasName("readObject") and                 ma.getQualifier().getType() = c and                 c.getASupertype*().hasQualifiedName("java.io", "InputStream") and                 this.asExpr() = ma        )    }}
class UnserializeSanitizer extends DataFlow::Node {     UnserializeSanitizer() {      this.getType() instanceof BoxedType or this.getType() instanceof PrimitiveType    }  }
class JavaUnserialize extends TaintTracking::Configuration {    JavaUnserialize() { this = "Java Unsearialize" }      override predicate isSource(DataFlow::Node source) { source instanceof RemoteFlowSource }
    override predicate isSink(DataFlow::Node sink) { sink instanceof UnserializeSink }
    override predicate isSanitizer(DataFlow::Node node) { node instanceof UnserializeSanitizer }     }
from DataFlow::PathNode source, DataFlow::PathNode sink, JavaUnserialize confwhere  conf.hasFlowPath(source, sink)select source.toString(),source.getNode().getEnclosingCallable(),source.getNode().getEnclosingCallable().getFile().getAbsolutePath(),       sink.toString(),source.getNode().getEnclosingCallable(), sink.getNode().getEnclosingCallable().getFile().getAbsolutePath(), "Potential JAVA Unserialize Vulnerability"
```

其中source点直接使用CodeQL预定义的类RemoteFlowSource，而sink点则是通过下面的代码实现。判断的逻辑是存在一个方法名为readObject的调用，并且调用的主体继承自java.io.InputStream类。注意这些说的是反序列化漏洞，不涉及利用链，不一定就真的能导致RCE效果。

```
exists(MethodAccess ma,Class c | ma.getMethod().hasName("readObject") and
ma.getQualifier().getType() = c and
c.getASupertype*().hasQualifiedName("java.io", "InputStream") and
this.asExpr() = ma
)
```

单独执行对应的脚本，则可以发现程序中可能存在的反序列化漏洞，如图3.1所示。

![1669107755147799.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221122/1669108189200174.png "1669107755147799.png")

图3.1 单独运行Unserialize.ql脚本的效果

其他脚本就不再依次讲解，如果有小伙伴感兴趣，非常期待小伙伴能为我们提供插件。如果小伙伴不知道怎么编写CodeQL脚本，可以把有漏洞的代码逻辑给私信我，由我来转化为CodeQL插件。

**0x04 工具使用**

回到工具本身，当前完整的代码我已经放在github，使用方式如下所示。

使用之前应该首先安装CodeQL,并配置conf...