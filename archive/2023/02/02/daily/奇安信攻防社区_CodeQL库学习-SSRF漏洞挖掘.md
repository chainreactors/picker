---
title: CodeQL库学习-SSRF漏洞挖掘
url: https://forum.butian.net/share/2117
source: 奇安信攻防社区
date: 2023-02-02
fetch_date: 2025-10-04T05:26:42.084352
---

# CodeQL库学习-SSRF漏洞挖掘

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### CodeQL库学习-SSRF漏洞挖掘

* [安全工具](https://forum.butian.net/topic/53)

CodeQL 是 GitHub 开发的代码分析引擎，用于自动执行安全检查。通过使用该工具，可以快速地发现代码中存在的一些潜在问题。有很多知名漏洞都是通过这款工具发现的。因此对这款工具进行学习和使用对漏洞挖掘是很有帮助的。CodeQL中内置了很多规则，本文通过对CodeQL官方规则中针对SSRF的规则进行学习和研究以及在实战中的使用，从而学习一些该工具的用法。

### 规则分析
SSRF的常见代码表现形式：（HTTP SSRF）
```go
URL url = new URL(imageUrl);
HttpURLConnection connection = (HttpURLConnection) url.openConnection(); --> sink
connection.setRequestMethod("GET");
return connection.getResponseMessage();
```
sink函数中并没有外部参数，检测sink需要和前面的代码联系，需要判断URL 对象在构造时是否外部可控。
因此分析ql库中对SSRF漏洞是如何检测的：
Config路径：ql/java/ql/lib/semmle/code/java/security/RequestForgeryConfig.qll
#### isSource
```go
source instanceof RemoteFlowSource and
// Exclude results of remote HTTP requests: fetching something else based on that result
// is no worse than following a redirect returned by the remote server, and typically
// we're requesting a resource via https which we trust to only send us to safe URLs.
not source.asExpr().(MethodAccess).getCallee() instanceof URLConnectionGetInputStreamMethod
```
source使用了常见的RemoteFlowSource，覆盖常见的远程请求，同时作为Method的source调用中，不能包含URLConnectionGetInputStreamMethod类型的调用
```go
/\*\* The method `java.net.URLConnection::getInputStream`. \*/
class URLConnectionGetInputStreamMethod extends Method {
URLConnectionGetInputStreamMethod() {
this.getDeclaringType() instanceof TypeUrlConnection and
this.hasName("getInputStream") and
this.hasNoParameters()
}
}
```
即如下的Source：
```go
java.net.URLConnection.getInputStream()
```
这种不认为是SSRF的Source，可能是因为连接的数据是否可控不能确定
#### isSink
```go
override predicate isSink(DataFlow::Node sink) { sink instanceof RequestForgerySink }
abstract class RequestForgerySink extends DataFlow::Node { }
private class UrlOpenSinkAsRequestForgerySink extends RequestForgerySink {
UrlOpenSinkAsRequestForgerySink() { sinkNode(this, "open-url") }
}
predicate sinkNode(Node node, string kind) {
exists(InterpretNode n | isSinkNode(n, kind) and n.asNode() = node)
}
```
其中使用到了ExternalFlow.ql中的sinkNode谓词，该库中表示，该库为内部使用API，处理csv格式的数据，sinkNode(Node node, string kind)属于一个接口，从Node中找符合sinkModelCsv或者SinkModelCsv子类的Node数据，其中最后一个参数用于标识Sink的类型，每一列参数的含义在ExternalFlow.ql中有详细讲解，这里简单介绍几个常用的参数，在RequestForgeryConfig中使用的是sinkNode(this, "open-url")
1. package 包名
2. 类名
3. 是否跳转到子类
4. 方法名
5. 签名列，限制选择方法名
6. ext 不太懂
7. input 输入的位置
8. kind 当前sink的类型
就是匹配所有open-url类型的数据类型。
sinkModelCsv谓词数据如下：
```go
private predicate sinkModelCsv(string row) {
row =
[
// Open URL
"java.net;URL;false;openConnection;;;Argument[-1];open-url",
"java.net;URL;false;openStream;;;Argument[-1];open-url",
"java.net.http;HttpRequest;false;newBuilder;;;Argument[0];open-url",
"java.net.http;HttpRequest$Builder;false;uri;;;Argument[0];open-url",
"java.net;URLClassLoader;false;URLClassLoader;(URL[]);;Argument[0];open-url",
"java.net;URLClassLoader;false;URLClassLoader;(URL[],ClassLoader);;Argument[0];open-url",
"java.net;URLClassLoader;false;URLClassLoader;(URL[],ClassLoader,URLStreamHandlerFactory);;Argument[0];open-url",
"java.net;URLClassLoader;false;URLClassLoader;(String,URL[],ClassLoader);;Argument[1];open-url",
"java.net;URLClassLoader;false;URLClassLoader;(String,URL[],ClassLoader,URLStreamHandlerFactory);;Argument[1];open-url",
"java.net;URLClassLoader;false;newInstance;;;Argument[0];open-url",
// Bean validation
"javax.validation;ConstraintValidatorContext;true;buildConstraintViolationWithTemplate;;;Argument[0];bean-validation",
// Set hostname
"javax.net.ssl;HttpsURLConnection;true;setDefaultHostnameVerifier;;;Argument[0];set-hostname-verifier",
"javax.net.ssl;HttpsURLConnection;true;setHostnameVerifier;;;Argument[0];set-hostname-verifier"
]
}
```
其他还有很多SinkModelCsv的子类，包含了一些第三方库的sink函数。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2023/02/attach-e200b781edd1ea9751ae8dcb5509b3bcf43f9771.png)
#### isAdditionalTaintStep
前面提到，SSRF漏洞不同于JNDI注入或者SQL注入，它的sink检测需要联系sink之前的代码，判断sink的Method调用方是否外部可控。ql库中通过实现isAdditionalTaintStep(DataFlow::Node pred, DataFlow::Node succ)方法进行功能的实现。该谓词的作用是将两个原本不相连的Node强行连在一起
```go
override predicate isAdditionalTaintStep(DataFlow::Node pred, DataFlow::Node succ) {
any(RequestForgeryAdditionalTaintStep r).propagatesTaint(pred, succ)
}
private class DefaultRequestForgeryAdditionalTaintStep extends RequestForgeryAdditionalTaintStep {
override predicate propagatesTaint(DataFlow::Node pred, DataFlow::Node succ) {
// propagate to a URI when its host is assigned to
exists(UriCreation c | c.getHostArg() = pred.asExpr() | succ.asExpr() = c)
or
// propagate to a URL when its host is assigned to
exists(UrlConstructorCall c | c.getHostArg() = pred.asExpr() | succ.asExpr() = c)
}
}
```
这里相对有点抽象，举个例子去进行理解
```go
@RequestMapping(value = "/one")
public String One(@RequestParam(value = "url") String imageUrl) {
try {
URL url = new URL(imageUrl);
HttpURLConnection connection = (HttpURLConnection) url.openConnection();
connection.setRequestMethod("GET");
return connection.getResponseMessage();
} catch (IOException var3) {
System.out.println(var3);
return "Hello";
}
}
```
此处按照正常的逻辑，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2023/02/attach-ce161d7990db4dfc39412e7580e2cf796bf034cb.png)
由于url不被认为是污点，因此没有继续向后寻找，isAdditionalTaintStep的作用是：当存在`URL url = new URL(imageURL)`，且`imageURL`为污点时，认为 `url`也是污点。
接着分析它是如何实现的，在函数中，pred代表的是污点，在SSRF中就是用户指定的URL字符串，succ则是代表类似URL(url)这种方法调用或者是对象的实例化。实现中的意思为，\*\*succ是一个UriCreation 调用或者一个UriConstructorCall调用，它的getHostArg方法返回的表达式等于污点node\*\*。其中UriCreation和UriConstructorCall的定义都在Networking.ql中，不做过多的分析。总的来说，它们匹配new URL()、URI.create()，并且其中url地址对应的参数需要是外部可控。满足上述条件的，我们认为它也是一个污点。从而成功的把url→new URL(url)链接起来。
#### isSanitizer
```go
override predicate isSanitizer(DataFlow::Node node) { node instanceof RequestForgerySanitizer }
private class PrimitiveSanitizer extends RequestForgerySanitizer {
PrimitiveSanitizer() {
this.getType() instanceof PrimitiveType or
this.getType() instanceof BoxedType or
this.getType() instanceof NumberType
}
private class HostnameSantizer extends RequestForgerySanitizer {
HostnameSantizer() { this.asExpr() = any(HostnameSanitizingPrefix hsp).getAnAppendedExpression() }
}
```
该方法用于净化污点，去除一些误报。PrimitiveSanitizer 是常见的方法，不匹配基础类型、数字类型的节点。重点是第二个HostnameSantizer，HostnameSanitizingPrefix继承自InterestingPrefix，该类在Stringprefixes.qll中，该文件的注释中讲解了该类的作用，简单来说就是可以定义一个字符串前缀，并提供一个getAnAppendedExpression函数，用来匹配任意该前缀+ 污点字符串的节点，简单演示如下，其中suffix标识会被匹配到的节点
```go
\* "foo:" + suffix1
\* "barfoo:" + suffix2
\* stringBuilder.append("foo:").append(suffix3);
\* String.format("%sfoo:%s", notSuffix, suffix4);
```
HostnameSanitizingPrefix 用一个正则定义前缀
```go
HostnameSanitizingPrefix() {
exists(
this.getStringValue()
.regexpFind(".\*([?#]|[^?#:/\\\\][/\\\\]).\*|[/\\\\][^/\\\\].\*|^/$", 0, offset)
)
}
```
该正则匹配字符串中`？`、`#`等符号之后的部分，用来解决如下情况的误报：
```go
URL url = new URL("http://127.0.0.1?x="+imageUrl);
```
此时，imageUrl无法指定目标访问任意的地址，也就不算是SSRF漏洞。
### 规则实战
使用microserviceseclab进行测试，该项目中的SSRFController.java包含了常见的5种SSRF漏洞。首先直接运行该检测QL，可以发现3处漏洞
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2023/02/attach-cb31b8ef61a576687e45965485792d3c3bc25963.png)
漏洞代码如下:
```go
@RequestMapping(value = "/one")
public String One(@RequestParam(value = "url") String imageUrl) {
try {
URL url = new URL(imageUrl);
HttpURLConnection connection = (HttpURLConnection) url.openConnection();
connection.setRequestMethod("GET");
return connect...