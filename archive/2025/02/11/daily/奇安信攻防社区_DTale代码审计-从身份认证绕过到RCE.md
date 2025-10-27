---
title: DTale代码审计-从身份认证绕过到RCE
url: https://forum.butian.net/share/4127
source: 奇安信攻防社区
date: 2025-02-11
fetch_date: 2025-10-06T20:32:31.594003
---

# DTale代码审计-从身份认证绕过到RCE

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

### DTale代码审计-从身份认证绕过到RCE

* [漏洞分析](https://forum.butian.net/topic/48)

D-Tale 是 Flask 后端和 React 前端的组合，为您提供了一种查看和分析 Pandas 数据结构的简便方法，允许用户方便地浏览和分析数据，而无需编写复杂的代码。Dtale 可以在 Jupyter Notebook 中或者独立的网页中运行，使得分析过程更加直观和高效。该系统存在身份验证绕过和RCE漏洞

D-Tale 是 Flask 后端和 React 前端的组合，为您提供了一种查看和分析 Pandas 数据结构的简便方法，允许用户方便地浏览和分析数据，而无需编写复杂的代码。Dtale 可以在 Jupyter Notebook 中或者独立的网页中运行，使得分析过程更加直观和高效。该系统存在身份验证绕过和RCE漏洞
1、身份认证绕过
========
Dtale 提供了身份验证系统，由于Dtale的web服务基于Flask的。在 Flask 中，`SECRET\_KEY` 是一个非常重要的配置项，它用于对会话（session）数据进行加密和签名，以防止未经授权的篡改。如果攻击者知道了应用的 `SECRET\_KEY`，他们就能够伪造合法的会话并绕过应用的身份验证或其他重要的安全机制。
![image-20241030154833293](https://oss-yg-cztt.yun.qianxin.com/butian-public/f463f56a277af54acb2a98e3d3c2e19a1.png)
通过查看源码，发现`SECRET\_KEY`是被硬编码的，在 Flask 中，会话数据默认存储在客户端，通过一个名为 `session` 的 cookie 发送给客户端。在存储之前，Flask 会对会话数据进行序列化并加密，然后使用 `SECRET\_KEY` 进行签名。这样我们就可以通过`SECRET\_KEY`伪造session进而绕过认证系统
![image-20241030155029335](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa455d365aec96271da11d95147954866.png)
Flask Session 的组成结构主要由三部分构成，第一部分为 Session Data ，即会话数据。第二部分为 Timestamp ，即时间戳。第三部分为 Cryptographic Hash ，即加密哈希。
要伪造cookie，首先要知道session的格式，对于已经登录的系统，我们可以对其第一部分的 Session Data进行解密，它实际为base64编码后的结果，然后对其中的相关字段进行修改后再进行签名加密。对于不能登录的系统，可以分析其源码，以下为Dtale登录部分的逻辑
![image-20241030171613440](https://oss-yg-cztt.yun.qianxin.com/butian-public/f05789c0b4ce65db47d935c82fc4f33b3.png)
通过`/login`路由，会首先通过`authenticate`方法判断用户名密码是否正确，如果正确，然后使用`session` 来存储登录状态和用户名。所以session的格式为：`{'username':'asd','logged\_in':'true'}`。
然后使用[flask-session-cookie-manager](https://github.com/noraj/flask-session-cookie-manager)工具来伪造session
![image-20241030171929607](https://oss-yg-cztt.yun.qianxin.com/butian-public/f106544b93062c17a9adad7655c03a845.png)
最后替换session即可成功登录系统
![image-20241030172042715](https://oss-yg-cztt.yun.qianxin.com/butian-public/f597ad54b05f472d0eb31225865d5a0c1.png)
2、远程命令执行
========
在Pandas中，`query` 方法用于基于表达式对 DataFrame 进行筛选。它允许以更直观和简洁的方式编写查询条件。但实际上，`query()`方法内部实现依赖于Python的`eval()`函数，`eval()` 函数用来执行一个字符串表达式，并返回表达式的值。
理论上我们可以执行任意python代码，但经过实验发现并不行，并报错\*\*ValueError: "\*\*import\*\*" is not a supported function\*\*
![image-20241028153336458](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa4ccc6637072ae6f264279b2f1d52527.png)
这是因为`query`会首先会将其中的字符串转换为抽象语法树，由于`\_\_import\_\_`并不是当前上下文中本地变量里的，所以在访问时会报错`UndefinedVariableError`，进而进入下面的异常捕获的流程
![image-20241024145417150](https://oss-yg-cztt.yun.qianxin.com/butian-public/f6be8d8c32bec0ef685ffc03103c6e1a4.png)
在`FuncNode`中会判断该变量是否在`MATHOPS`中，在`MATHOPS`中定义了一些常见的numpy库筛选和计算的函数，显然`\_\_import\_\_`没在其中。
![image-20241024145521029](https://oss-yg-cztt.yun.qianxin.com/butian-public/faf5109458801f2c54b19fd626ece7a4b.png)
![image-20241024145618549](https://oss-yg-cztt.yun.qianxin.com/butian-public/f0d527dd5210c8922ad713b2873ea3ee2.png)
既然无法直接执行，那可以尝试反射的方法去调用`\_\_import\_\_`方法，进而包含任意库从而RCE
在query中可以使用`age > 30`这种基本用法外，还可以使用`@` 用于引用函数外部的变量，也就是说，当你需要在 `query` 表达式中使用当前作用域中的变量时，可以用 `@` 来访问。例如下面这个例子
```python
import pandas as pd
data = {'age': [25, 30, 45, 35],
'name': ['Alice', 'Bob', 'Charlie', 'David']}
df = pd.DataFrame(data)
# 定义一个外部变量
age\_threshold = 30
# 在 query 中使用外部变量
result = df.query('age > @age\_threshold')
print(result)
```
这样就可以灵活的使用程序中的变量进行筛选条件。
![image-20241028151805453](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa69e77a8deb5cc55541aaf5e044ff869.png)
既然可以使用`@`引用函数外部的变量，我们就可以通过`pandas`库中反射调用基类，进而调用`\_\_import\_\_`。这里可以搜索`builtins`，因为`builtins`是\*\*python的内建模块\*\*，且`builtins`中具有`\_\_import\_\_`方法
![image-20241031201524715](https://oss-yg-cztt.yun.qianxin.com/butian-public/f11925524ed93617005f36909a7dbf092.png)
![image-20241029154827941](https://oss-yg-cztt.yun.qianxin.com/butian-public/f5677b6676fbf896f32e7d6b983c9e011.png)
通过搜索在`pandas`库中有两处都引用了`builtins`，我们挑第一个来构造链，其路径在`core/common.py`下，所以构造链为
```php
@pd.core.common.builtins.\_\_import\_\_("os").system("calc")
```
接下来就是寻找如何触发`query`进而RCE。
进入后台后，可以可视化的分析Pandas 数据结构，但是这里我们使用筛选选择自定义过滤器时，这里会提示`Custom Filtering is currently disabled.`，并提示需要在启动代码中加入对应的配置项`enable\_custom\_filters=True`才可以使用。
![image-20241030175016911](https://oss-yg-cztt.yun.qianxin.com/butian-public/f317eb42e67ff7a27e17e7c02a66cdc8a.png)
首先查看对应的代码，搜索当前路由`/popup`，可以看到代码最终调用了`base\_render\_template`对模板进行渲染
```python
@dtale.route("/popup/<popup\_type>")
@dtale.route("/popup/<popup\_type>/<data\_id>")
def view\_popup(popup\_type, data\_id=None):
"""
:class:`flask:flask.Flask` route which serves up a base jinja template for any popup, additionally forwards any
request parameters as input to template.
:param popup\_type: type of popup to be opened. Possible values: charts, correlations, describe, histogram, instances
:type popup\_type: str
:param data\_id: integer string identifier for a D-Tale process's data
:type data\_id: str
:return: HTML
"""
...
return base\_render\_template(
"dtale/popup.html",
data\_id,
title=title,
popup\_title=popup\_title,
js\_prefix=popup\_type,
grid\_links=grid\_links,
back\_to\_data=text("Back To Data"),
)
```
在`base\_render\_template`下或获取当前配置中的各种参数，并将参数带入渲染模板
![image-20241031113130273](https://oss-yg-cztt.yun.qianxin.com/butian-public/f6579052430d6ec34df4c34fdd8fe1100.png)
![image-20241031113233809](https://oss-yg-cztt.yun.qianxin.com/butian-public/f782705f5c783c18cbbf471f99071d4b8.png)
所以说这里所有的配置参数的值最后都是渲染在了前端页面上，那我们就可以直接抓包修改返回包即可绕过。
![image-20241031135944133](https://oss-yg-cztt.yun.qianxin.com/butian-public/f1d5b2604681895e828590e0734c8f728.png)
但是当我们执行自定义的Filter时还是会被提示 not enabled!，通过查看该路由的后端代码，发现在后端也对`enable\_custom\_filters`的值进行了验证。
![image-20241031140050119](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa1a540dacb6a6c6d397846be91fc374f.png)
![image-20241031140933568](https://oss-yg-cztt.yun.qianxin.com/butian-public/fdd2349436168491a0043e29f5103f659.png)
但是我们找到了真正执行filter的地方时通过`run\_query`方法进而在该方法内用`query`执行传递的参数的。所以可以在这个文件内搜索`run\_query`看看那些地方还调用了该方法
![image-20241101170755929](https://oss-yg-cztt.yun.qianxin.com/butian-public/f6f1afb78684ad5331e9b08d10bab99e3.png)
最后找到这样一处，在这个方法下并没有二次验证`base\_render\_template`的值，直接从get请求中获取`query`的值带入`run\_query`方法。看到此路由信息为`/chart-data`，请求`http://127.0.0.1:40000/dtale/chart-data/1?query=@pd.core.frame.com.builtins.\_\_import\_\_(%22os%22).system(%22calc%22)`即可触发。
![image-20241101171104904](https://oss-yg-cztt.yun.qianxin.com/butian-public/fd842aed59e87cae8284ae6e8f49bd17c.png)
3、修复方法
======
在3.13.1中修复了身份认证绕过漏洞，将`SECRET\_KEY`的值设置成了随机数
![image-20241031202258040](https://oss-yg-cztt.yun.qianxin.com/butian-public/f86e7cf5b9225d979f84df80ea150a406.png)
在3.14.1中修复了RCE漏洞，增加了对`base\_render\_template`的验证
![image-20241031202626535](https://oss-yg-cztt.yun.qianxin.com/butian-public/f432b4f925a885803b29e0ce539eb326e.png)

* 发表于 2025-02-10 09:49:12
* 阅读 ( 25565 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)](https://forum.butian.net/people/77)

[中铁13层打工人](https://forum.butian.net/people/77)

79 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻...