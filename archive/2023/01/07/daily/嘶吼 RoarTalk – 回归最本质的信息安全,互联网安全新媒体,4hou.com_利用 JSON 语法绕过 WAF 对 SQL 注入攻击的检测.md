---
title: 利用 JSON 语法绕过 WAF 对 SQL 注入攻击的检测
url: https://www.4hou.com/posts/q837
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-07
fetch_date: 2025-10-04T03:14:36.425226
---

# 利用 JSON 语法绕过 WAF 对 SQL 注入攻击的检测

利用 JSON 语法绕过 WAF 对 SQL 注入攻击的检测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 利用 JSON 语法绕过 WAF 对 SQL 注入攻击的检测

xiaohui
[技术](https://www.4hou.com/category/technology)
2023-01-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)161967

收藏

导语：Team82开发了一种通用的绕过行业领先的web应用程序防火墙(WAF)的方法。 攻击技术包括将JSON语法附加到WAF无法解析的SQL注入有效负载。

JSON 语法自 2012 年开始作为新特性被各类 SQL 数据库支持，目前所有主流数据库都已支持 JSON 语法，但目前的主流 WAF 并没有做相应跟进，从而可以被绕过。

Team82开发了一种通用的绕过行业领先的web应用程序防火墙(WAF)的方法。 攻击技术包括将JSON语法附加到WAF无法解析的SQL注入有效负载。

主要的WAF供应商在他们的产品中缺乏JSON支持，尽管大多数数据库引擎已经支持了十年。 大多数WAF可以很容易地检测到SQLi攻击，但是将JSON前置SQL语法使WAF无法检测到这些攻击。

使用这种技术的攻击者将能够绕过WAF的保护，并使用其他漏洞来窃取数据。

**简介**

Web应用防火墙(WAF)旨在保护基于Web的应用程序和API免受恶意外部HTTPs流量的影响，尤其是跨站脚本和SQL注入攻击，这些攻击危险似乎还未解除。

WAF的引入在很大程度上是为了应对这些编码错误。WAF现在是保护存储在数据库中的组织信息的关键防线，这些信息可以通过web应用程序访问。WAF也越来越多地用于保护基于云的管理平台，这些管理平台监督连接的嵌入式设备，如路由器和接入点。

能够绕过WAF的流量扫描和拦截功能的攻击者通常可以直接访问敏感的业务和客户信息。值得庆幸的是，这样的绕过并不常见，而且针对特定供应商的实现是一次性的。

目前，Team82引入了一种攻击技术，它是业界领先供应商销售的多个web应用程序防火墙的第一个通用绕过。该绕过适用于五个主要供应商销售的WAF: Palo Alto, F5, Amazon Web Services, Cloudflare和Imperva。目前，所有受影响的供应商都承认Team82的披露，并实施了修复，将JSON语法支持添加到其产品的SQL检查过程中。

Team82的技术首先依赖于理解WAF如何识别和标记恶意SQL语法，然后找到WAF看不到的SQL语法。这是JSON。JSON是一种标准的文件和数据交换格式，通常用于将数据从服务器发送到web应用程序。

在SQL数据库中引入JSON支持可以追溯到大约10年前。现在的数据库引擎默认支持JSON语法、基本搜索和修改，以及一系列JSON函数和操作符。虽然JSON支持是数据库引擎的标准，但WAF却并非如此。供应商在添加JSON支持方面一直进展缓慢，这使得Team82能够创建新的SQL注入有效负载，其中包括绕过WAF提供的安全性的JSON。

使用这种新技术的攻击者可以访问后端数据库，并使用额外的漏洞，通过直接访问服务器或通过云窃取信息。

这对于已经转向基于云的管理和监控系统的运行和物联网平台尤为重要。WAF提供了来自云的额外安全性的承诺，能够绕过这些保护的攻击者可以广泛地访问系统。

Team82在去年开发了这项技术，当时他们正在对Cambium Networks的无线设备管理平台进行不相关的研究，包括其内部或云端销售的cnMaestro无线网络管理器。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408656190342.png "1671408656190342.png")

Cambium Networks无线接入点

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408667187593.png "1671408667187593.png")

Cambium的cnMaestro云架构允许用户从云端远程配置和控制他们的AP Wi-Fi设备

为了了解平台是如何构建的，以及它的许多内部API和路由，Team82从Cambium的网站下载了cnMaestro内部部署的开放虚拟化格式虚拟机。

Team82了解到cnMaestro是由许多不同的NodeJS后端服务构建的，这些服务处理用户对特定路由的请求。这些服务都有轻微的混淆，使得研究平台变得困难。为了将每个请求代理到正确的服务，Nginx被用来通过所请求的URL来传递请求。

cnMaestro提供了两种不同的部署类型:

本地部署：创建一个由用户托管和管理的专用cnMaestro服务器。

云部署：位于Cambium Networks云基础设施上的cnMaestro服务器，cnMaestro的所有此类实例都以多租户架构托管在Cambium组织下的Amazon AWS云上。

**云部署**

托管在亚马逊AWS上的cnMaestro云部署包括一个cnMaestro的主要实例(托管在https://cloud.cambiumnetworks.com上)，它处理登录、设备部署，并将大部分平台数据保存在主数据库中。

任何注册到cnMaestro Cloud应用程序的用户都会获得一个个人Amazon AWS实例，其中包含个人URL (Cambium主云的子域)和组织标识符。这有助于在多租户设计中分离不同的用户。为了访问你的cnMaestro实例，将按照以下方案生成一个唯一的URL：https://us-e1-sXX-XXXXXXXXXX.cloud.cambiumnetworks.com

在Team82对Cambium cnMaestro的研究结束时，他们发现了7个不同的漏洞，可以在这里和Team82的披露仪表板上看到。然而，一个特别的漏洞让Team82陷入了一个巨大的兔子洞，导致Team82发现并开发了这项新技术。

**很难利用的零日漏洞**

Team82发现的一个特殊的Cambium漏洞被证明更难利用：CVE-2022-1361。该漏洞的核心是一个简单的SQL注入漏洞，但实际的开发过程需要Team82跳出思维定式，创建一个全新的SQL技术。利用这个漏洞，Team82能够窃取用户的会话、SSH密钥、密码哈希、令牌和验证码。

此漏洞的核心问题是，在这种特殊情况下，开发人员没有使用准备好的语句将用户提供的数据附加到查询中。他们没有使用将用户参数附加到SQL查询并清除输入的安全方法，而是直接将其附加到查询中。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408681192384.png "1671408681192384.png")

Team82在CVE-2022-1361中滥用的SQL注入汇点

正如我们在上面的汇点中看到的，应用程序接受用户提供的数据（在本例中为a.serialNo或a.mac），并将其附加到SQL查询中。我们使用此漏洞的目的是过滤存储在数据库中的敏感数据。然而，虽然这看起来很简单，但在快速分析了该漏洞后，我们意识到它有三个关键漏洞/限制：

Team82只能检索作为返回行的整数 ；

返回的行按随机顺序返回；

在每个请求中，Team82只能返回有限数量的行。

让我们深入分析这些限制。

**限制1：Team82只能检索整数**

第一个限制只返回整数，而不返回字符串。由于原始请求返回整数，我们将使用的任何联合语句也必须返回整数。在SQL中，如果执行联合操作，则必须确保两列的类型相同，并且由于一方获取整数，因此我们也必须返回整数。由于我们要过滤的数据很可能是字符串（会话令牌、SSH密钥等），因此我们必须以某种方式获得过滤字符串的能力。

通过将想要过滤的任何字符串转换为整数数组，并将每个字符作为单独的行返回，可以轻松克服这一限制。为此，Team82使用了stringarray和ASCIISQL函数。

![4.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408694198966.png "1671408694198966.png")

![4.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408703302816.png "1671408703302816.png")

一个SQL查询，返回字符串作为其字符的整数列表

**限制2：返回的行按随机顺序返回**

第二个限制是，当Team82返回多行时，web服务器将以随机顺序返回给Team82。当Team82查看漏洞后执行的代码时，Team82看到对于SQL查询返回的每一行，服务器将执行一些其他异步操作(这可以通过调用async.parale函数看到)。这意味着返回行的原始顺序将不会被保留，相反，该顺序将是异步操作完成的顺序。

这意味着，如果Team82将字符串作为整数数组进行过滤，就会丢失字符顺序，从而使过滤变得无关紧要。

Team82通过添加行索引来克服这一限制，行索引使用row\_number SQL函数将字符串中字符的索引转换为返回的整数。因为Team82只返回ASCII字符，所以每个字符的值被限制为128。通过将索引号乘以1000 (i \* 1000)并将其附加到结果中，Team82总是可以通过简单的除法和模块操作来确定字符索引。

![5.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408716129815.png "1671408716129815.png")

![5.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408726124381.png "1671408726124381.png")

一个SQL有效负载，返回字符串中每个字母的ascii值，加上字符的索引乘以1000

在检索到过滤的数据之后，Team82可以简单地将每个返回行除以1000，以了解字符索引。Team82还可以通过对返回值使用模块操作来恢复原始字符ASCII值。

**限制3：在每个请求中只能返回有限数量的行**

最后一个限制是最难克服的：超时问题。对于返回的每一行，服务器都执行了一些其他操作，包括另一个SQL查询和数据操作。当我们试图检索大量行时，请求超时。更糟糕的是，API端点相当慢，因此每次检索一行非常耗时。

Team82的解决方案实际上非常高级，Team82不是为每个字符返回一行，而是从许多行中构造一个整数。这是可能的，因为整数和字符之间的字节大小不同。在PostgreSQL中，一个整数是4字节长，而Team82试图过滤的字符是1字节长(只要是ascii字符)。这意味着通过执行简单的字节操作，Team82可以在每个整数中容纳四个不同的字符。此外，如果Team82在union命令中将整数转换为BIGINT，这在PostgreSQL中是可能做到的，Team82可以将每行扩展为8字节。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408739213410.png "1671408739213410.png")

PostgreSQL类型大小

这意味着，如果要为Team82过滤的每个字符附加8个字节，并将其附加到BIGINT中，Team82可以在每个请求中过滤7倍多的字符(1个字节保留给字符索引)。

![7.1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408752160091.png "1671408752160091.png")

![7.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408760739400.png "1671408760739400.png")

一个SQL查询，它接受一个字符串，并每隔几个字符创建一个BIGINT

使用这种方法，Team82能够在每个请求中提取多达8倍的数据。这减少了Team82窃取大量数据所需的时间，并使攻击场景变得可信。

**构建有效负载**

在Team82绕过所有三个限制之后，Team82就得到了一个大的有效负载，允许提取任何Team82选择的数据:。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408773558721.png "1671408773558721.png")

事实上，当Team82使用这个有效负载时，Team82设法窃取了存储在数据库中的敏感信息，从会话cookie到令牌，SSH密钥和哈希密码。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408788598618.png "1671408788598618.png")

使用SQLi有效负载提取的数据示例

**云端漏洞**

在成功利用了云部署漏洞后，下一步是在Cambium的云端尝试相同的漏洞。很快，Team82就找到了相应的云路由，并成功确认它也容易受到同样的漏洞的攻击。然后Team82尝试了一个安全版本的有效负载，并收到了这样的响应。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408803897666.png "1671408803897666.png")

对SQL注入漏洞的响应，可以看到Team82的请求被释放了，返回一个403 Forbidden

接下来，我们注意到了包含awselb/2.0的HTTP服务器，这意味着，应用程序并没有停止Team82的请求，而是AWS WAF释放了Team82的请求，因为它可能将其标记为恶意请求。

**对AWS WAF 的研究**

为了研究AWS WAF，我们首先创建了自己的设置，在其中控制所有的活动部件：应用程序、客户端和WAF设置和日志。我们在AWS云上创建了一个简单的设备，并设置了AWS WAF来保护应用程序免受恶意请求(Team82设置了WAF)。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408816108855.png "1671408816108855.png")

用于配置WAF规则集的界面

然后，Team82创建了一个带有SQLi漏洞的web应用程序，并将其托管在AWS上。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221219/1671408828169677.png "1671408828169677.png"...