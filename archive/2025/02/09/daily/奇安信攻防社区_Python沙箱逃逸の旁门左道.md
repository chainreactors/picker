---
title: Python沙箱逃逸の旁门左道
url: https://forum.butian.net/share/4114
source: 奇安信攻防社区
date: 2025-02-09
fetch_date: 2025-10-06T20:33:45.440907
---

# Python沙箱逃逸の旁门左道

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

### Python沙箱逃逸の旁门左道

* [漏洞分析](https://forum.butian.net/topic/48)

本文结合CTF真题和作者对Python底层的理解，贡献了不一样的PyJail的绕过手法

开篇
==
本文会带你了解一些绕过Pyjail的高级技巧，其实绕过过滤无非就是两种操作:\*\*替换\*\*和\*\*通过更加底层的手段在实现\*\*,所以，我们先来了解一下Python这门语言的底层特性并且以此来展示对应的Pyjail绕过手法
全局变量
====
这是基础知识，`globals`顾名思义就是公共的变量空间，里面包括你定义或者系统自带的全局变量，而由于函数也是特殊的对象变量，所以像是`\_\_builtins\_\_`里面的基础函数如`len`,`print`,`eval`这些的可以看作特殊的全局变量
```py
>>> dir(globals()['\_\_builtins\_\_'])
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '\_', '\_\_build\_class\_\_', '\_\_debug\_\_', '\_\_doc\_\_', '\_\_import\_\_', '\_\_loader\_\_', '\_\_name\_\_', '\_\_package\_\_', '\_\_spec\_\_',
'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>>
```
这个就是所有Py3.12的内置函数了。
Blue Team:消除对应的高危的函数
--------------------
例如我在一个执行数学计算的python环境中，我并不需要像是`getattr`,`\_\_import\_\_`,`map`这些设计到代码执行的高危函数，所以为了保证安全我完全可以把这些内置函数给消除。就像这样:
```py
>>> expression='a'
>>> context={'a':123}
>>> eval(expression, {"\_\_builtins\_\_": {}}, context)
123
>>> expression='\_\_import\_\_("os").system("ls")'
>>> eval(expression, {"\_\_builtins\_\_": {}}, context)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<string>", line 1, in <module>
NameError: name '\_\_import\_\_' is not defined
>>>
```
这样就去除了所有的内置方式，只保留了基础的数学计算的功能，但其实这个还是不够安全的
Red Team:
---------
例如我可以通过不断回溯上一个`\_\_class\_\_`并且通过`\_\_subclesses\_\_`查找子类，最终通过`\_wrap\_close`类就能够实现最终实现提取到全局变量重获`\_\_builtins\_\_`了
```py
[ x.\_\_init\_\_.\_\_globals\_\_ for x in ''.\_\_class\_\_.\_\_base\_\_.\_\_subclasses\_\_() if x.\_\_name\_\_=="\_wrap\_close"][0]["system"]('ls')
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-af622edd7f2c05f66cbdf9ac4219a6191e7e0cff.png)
还有比如
### \*\*mro\*\*
在 Python 中，\*\*MRO（Method Resolution Order）\*\* 指的是类继承层次结构中搜索方法或属性的顺序。
可以通过类的 `\_\_mro\_\_` 属性查看其方法解析顺序。`\_\_mro\_\_` 是一个元组，包含了类继承层次结构中从当前类到最高父类（通常是 `object`）的所有类。在拿到父类之后就可以通过subclasses故技重施了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-640615fc6fed30f0ebb54a1384a2a79cbad9b978.png)
这个就是flask的jinja2的ssti经典攻击思路了
其实开发者还可以使用AST沙箱来进行防御比如:
```py
import ast
class SafeEvaluator(ast.NodeVisitor):
"""
AST 节点访问器，用于检查表达式的安全性。
禁止所有属性访问（如 obj.attr）以及其他潜在危险的操作。
"""
def \_\_init\_\_(self):
super().\_\_init\_\_()
self.allowed\_nodes = (
ast.Expression,
ast.Call,
ast.Name,
ast.Load,
ast.BinOp,
ast.UnaryOp,
ast.Constant, # 对于 Python 3.8 及更高版本
ast.List,
ast.Tuple,
ast.Dict,
ast.BoolOp,
ast.Compare,
ast.IfExp,
)
self.allowed\_operators = (
ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod,
ast.Pow, ast.BitXor, ast.USub, ast.UAdd,
ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
ast.And, ast.Or, ast.Not,
)
def visit(self, node):
if not isinstance(node, self.allowed\_nodes):
raise ValueError(f"不允许的节点类型: {type(node).\_\_name\_\_}")
return super().visit(node)
def visit\_Attribute(self, node):
# 禁止属性访问
raise ValueError("禁止属性访问")
def visit\_Call(self, node):
if isinstance(node.func, ast.Attribute):
raise ValueError("禁止通过方法调用执行函数")
self.generic\_visit(node)
def visit\_Name(self, node):
if node.id.startswith("\_\_"):
raise ValueError(f"禁止访问名称: {node.id}")
self.generic\_visit(node)
def visit\_BinOp(self, node):
if not isinstance(node.op, self.allowed\_operators):
raise ValueError(f"不允许的操作符: {type(node.op).\_\_name\_\_}")
self.generic\_visit(node)
def visit\_UnaryOp(self, node):
if not isinstance(node.op, self.allowed\_operators):
raise ValueError(f"不允许的操作符: {type(node.op).\_\_name\_\_}")
self.generic\_visit(node)
def visit\_BoolOp(self, node):
if not isinstance(node.op, self.allowed\_operators):
raise ValueError(f"不允许的布尔操作符: {type(node.op).\_\_name\_\_}")
self.generic\_visit(node)
def visit\_Compare(self, node):
for op in node.ops:
if not isinstance(op, self.allowed\_operators):
raise ValueError(f"不允许的比较操作符: {type(op).\_\_name\_\_}")
self.generic\_visit(node)
def visit\_IfExp(self, node):
self.generic\_visit(node)
def secure\_eval(expression, context=None):
"""
安全地评估表达式，禁止属性访问和其他危险操作。
:param expression: 要评估的表达式字符串
:param context: 提供给表达式的上下文（变量和函数）
:return: 表达式的计算结果
"""
if context is None:
context = {}
# 解析表达式的 AST
try:
tree = ast.parse(expression, mode='eval')
except SyntaxError as e:
raise ValueError(f"无效的表达式: {e}")
# 检查 AST 的安全性
SafeEvaluator().visit(tree)
# 编译并安全地执行表达式
try:
compiled = compile(tree, filename="<safe\_eval>", mode="eval")
return eval(compiled, {"\_\_builtins\_\_": {}}, context)
except Exception as e:
raise ValueError(f"表达式评估出错: {e}")
# 示例使用
if \_\_name\_\_ == "\_\_main\_\_":
context = {
"name": "Alice",
"age": 25,
"greet": lambda name: f"Hello, {name}!"
}
expressions = [
"greet(name)", # 安全: 调用允许的函数
"age + 5", # 安全: 简单计算
"\_\_import\_\_('os').system('ls')", # 不安全: 尝试访问 \_\_import\_\_
"name.\_\_class\_\_", # 不安全: 尝试属性访问
"greet.\_\_globals\_\_['os'].system('ls')", # 不安全
]
for expr in expressions:
try:
result = secure\_eval(expr, context)
print(f"表达式 '{expr}' 的结果: {result}")
except ValueError as ve:
print(f"表达式 '{expr}' 被拒绝: {ve}")
```
但是也有对应的绕过办法，留给下一篇博客吧
CodeObject
==========
其实上文也有提及，python中万物接对象，包括正在执行的字节码对象(\*\*codeobject\*\*)。为了将脚本代码转化成可以被PVM（Python虚拟机）执行的字节码，Py开发者专门保留了compile函数来完成脚本代码到字节码对象(\*\*codeobject\*\*)的转化。所以，但凡涉及到动态代码执行的节点，都会调用compile函数：包括但不限于:`exec`,`eval`,`map`,`\_\_import\_\_`...Blue Team 通过禁用compile，就能杜绝大部分通过动态执行绕过黑白名单的操作了，比如:`eval('pop'+'en("ls")')`
但不是所有。
函数即obj
------
例如在这里我可以通过如下这个函数实现查看：
```py
def check(obj):
"""
检查对象的非魔术属性和方法，并打印详细信息。
"""
from inspect import ismethod, isfunction
print...