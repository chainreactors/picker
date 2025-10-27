---
title: langflow: AI产品AST代码解析执行产生的RCE
url: https://forum.butian.net/share/4316
source: 奇安信攻防社区
date: 2025-05-23
fetch_date: 2025-10-06T22:27:14.782923
---

# langflow: AI产品AST代码解析执行产生的RCE

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

### langflow: AI产品AST代码解析执行产生的RCE

* [漏洞分析](https://forum.butian.net/topic/48)

本文主要是对langflow这一AI产品进行了漏洞分析，同时通过阅读官方文档的方式对漏洞的利用方式进行了进一步的扩展利用，剖析在AST解析执行的过程中因为`decorator`或者参数注入的方式导致的RCE漏洞的姿势，后续也将其添加到codeql规则中，进行AI产品代码的批量检测与漏洞挖掘

Pre
---
本文主要是对langflow这一AI产品进行了漏洞分析，同时通过阅读官方文档的方式对漏洞的利用方式进行了进一步的扩展利用，剖析在AST解析执行的过程中因为`decorator`或者参数注入的方式导致的RCE漏洞的姿势，后续也将其添加到codeql规则中，进行AI产品代码的批量检测与漏洞挖掘
Env
---
其项目github链接如下
<https://github.com/langflow-ai/langflow>
![image-20250421200732258.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-82f3161262d034652dd340ba78bfe9338ce234cd.png)
Langflow 是一个基于 LangChain 的 AI 流程编排工具，其核心功能和主要用途如下：
1. \*\*核心功能\*\*
- 提供可视化界面来构建 LangChain 应用
- 通过拖拽方式创建 AI 工作流
- 支持实时预览和测试
- 可以导出/导入流程配置
2. \*\*主要用途\*\*
- 快速原型设计 AI 应用
- 无代码方式构建 LangChain 流程
- 可视化测试和调试 LLM 应用
- 构建复杂的 AI 工作流程
其项目总体分为前端-后端两个部分，其源代码均在`src`目录下
![image-20250421200812189.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d14ff723e0329a748e9bcc4427a0fe496e7e54d4.png)
### structure of backend
![image-20250421200949861.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-61495f2400cb963a50e153f2a207204102e4e4e4.png)
- `main.py`: FastAPI 应用程序的入口点
- `server.py`: 服务器配置和启动
- `worker.py`: 后台任务处理
- `middleware.py`: 中间件处理
### how to start
way1:
根据README文件的描述，可以通过pip或者uv进行包的安装
```bash
# 确保您的系统已经安装上>=Python 3.10
# 安装Langflow预发布版本
python -m pip install langflow --pre --force-reinstall
# 安装Langflow稳定版本
python -m pip install langflow -U
```
way2:
或者直接分别在根目录分别执行`make backend` `make frontend`进行源码层面的启动
![image-20250421201903020.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-d7d93387999588a3ff026dd671584470362fec61.png)
Analysis
--------
### CVE-2025-3248
#### version &lt; 1.3.0
该漏洞仅仅影响1.3.0以下的langflow应用
### reproduce &amp; analysis
这个漏洞核心是因为在执行动态代码时并没有在沙箱环境中进行执行，导致了远程命令执行的漏洞
作者也提及到了历史有关于`langflow`的相关漏洞都是身份认证后的操作，作者这里通过分析`pre-auth`的接口逻辑寻找到了一个未授权接口的RCE漏洞
![image-20250421210658847.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-423a1c2aff2a584c946460cd7783af82b91416e8.png)
#### Login logic
根据在`AUthSettings`中提及到的`Login Settings`，其通过JWT以及API\\_kEY进行登录认证
同时，默认情况下访问该应用将会进行自动登录super user，同时的同时，其默认账号密码为：`langflow/langflow`
![image-20250421211252358.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-52426a6c71651c6b8bdb942db81ad072b6ae16c8.png)
而该应用针对于用户管理相关的API集中在`api/v1/users.py`中
- 用户注册：POST /users/
- 创建新用户
- 设置密码哈希
- 创建默认文件夹
- 用户信息：GET /users/whoami
- 获取当前用户信息
- 用户管理（需要超级管理员权限）：
- 查看所有用户：`GET /users/`
- 更新用户：`PATCH /users/{user\_id}`
- 重置密码：`POST /users/{user\_id}/reset-password`
- 删除用户：`DELETE /users/{user\_id}`
而对于接口的权限校验，这里通过一个文件上传接口进行举例
![image-20250421212621915.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-be321c32ad327c258aa53897a769ce33b06573f9.png)
最后的核心是通过`services/auth/utils.py#get\_current\_user`进行权限的校验
![image-20250421212726811.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-3f861c186e521f3000eab4272c45d855316d7715.png)
JWT以及api\\_key两种方式进行二选一进行验证，优先进行JWT认证
#### ast module
在进行后续步骤之前我们先了解一下python的内置库ast，学习他的数据结构
<https://docs.python.org/3.13/library/ast.html>
![image-20250421213751622.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-22c3d5ae6edad5864fdc88107be9c5caffb79750.png)
我们通过一些例子进行理解
```python
# A simple decorator function
def decorator(func):
   def wrapper():
       print("Before calling the function.")
       func()
       print("After calling the function.")
   return wrapper
​
# Applying the decorator to a function
@decorator
def foo():
   print("echo Inside foo decorator")
​
print(1)
a = 1
if a > 3:
   print("xxx")
foo()
```
对于上面一段代码，将其进行AST抽取后的结果为
![image-20250421214921384.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-161d900f0a2d1cc1335d4be62629a6be6514220d.png)
其中
- `ast.FunctionDef`结点代表着函数的定义，这里指代的是decorator函数的定义
- 第二个`ast.FunctionDef`结点指代的是`foo`函数的定义，该函数存在有一个装饰器，在ast中其被抽象为`ast.Name`加入到结点的`decorator\_list`列表中
- 后续的`ast.Expr`为`print`语句的抽象
- 后面就是赋值的`ast.Assign`、if语句的`ast.if`、函数执行表达式的`ast.Expr`
#### ast.FunctionDef validate
在`api/v1/validate.py`下的路由API均不需要身份认证即可访问
![image-20250421213432148.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-36bae1a616878c66b8582bde37aaf2f781dba14f.png)
其中对于路由`/code`，其将会对传入的`code`代码进行有效性验证
![image-20250421213622711.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c84ef35d7c68dc5947cdb63461740199c7da33a0.png)
其验证的过程大致分成了三个步骤：
1. 使用python内置的`ast`库进行抽象语法树的解析
将python语言的各个代码部分抽象成独特的类：
![image-20250421213937312.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-0f300b6d8a4da291e0bd52b1b213da20d4d8615a.png)
2. 验证给定代码段的`import`语句是否存在错误
其会遍历AST抽象出的每一个node结点，而对于python代码中的`import`操作，这里将会通过调用`importlib.import\_module`对包进行导入，验证给定代码中的导入包是否可用
> 在这个过程中则会出现安全问题，在导入外部包的过程中，将会执行外部模块中的装饰器、表达式等等
>
> 例如存在有foomodule.py
>
> ```python
> def foo():
>    return "echo Inside foo decorator"
> ​
> print(1)
> ```
>
> 以及`main.py`
>
> ```python
> import foomodule
> ```
>
> 在执行过后将会执行`print`语句
3. 验证给定代码端的方法定义是否存在语法错误
其验证方法首先是通过内置的`compile`函数将方法定义的AST编译成python对象，以便于使用`exec`或者`eval`进行执行
![image-20250421221416062.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e2fd7880522df188f3eb951e7c2ddd145744da6c.png)
> 在这个位置将函数定义的ast还原成了python代码对象并在没有沙箱的环境下执行该代码，造成了source到sink的可控
#### exploit
这里作者是利用了在函数定义的过程中将会执行装饰器的函数调用的原理来构造的命令执行利用
如下利用POC
![image-20250421223230836.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-386fb0ff293fab071a797507ec012603f4460dc1.png)
![image-20250421223245163.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-254f4752f7a01a55d5fa0b37c43bc47bf3fb3f0a.png)
能够通过这种方式在服务端执行系统命令
### deep research
在上面分析的基础上，通过官方文档探索更多可以利用的姿势
可以将上面的漏洞代码抽象如下：
```python
source\_code = """
@\_\_import\_\_("os").system("echo Inside foo decorator")
def foo():
  return "echo Inside foo decorator"
"""
parsed\_ast = ast.parse(source\_code)
for n in parsed\_ast.body:
   print(ast.dump(n))
code\_objct = compile(parsed\_ast, filename="<string>", mode="exec")
​
exec(code\_objct)
```
其具体是执行了一个`ast.FunctionDef`对象，我们首先看看该对象的结构
![image-20250421224056933.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-34142b0d8a21423df96980c8a04fb4f54863e5b4.png)
上面核心是利用了装饰器进行命令执行
![image-20250421224406069.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-0c35c3eee7bbed8355fb21189de9d5e688d76c8a.png)
装饰器类的语法仅仅是一种语法糖，通过装饰器对修饰的函数进行进一步的包装
![image-20250421224741856.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-fcdf5b02dd132214cede4f05d97923f82cf59ea4.png)
上述文档中，也解释了当函数被定义的同时就会执行该函数存在的修饰器，同时也说明了，修饰器的调用原理是进行了一次表达式的执行，是`callable`的
则我们可以通过装饰器的方式执行任意的函数，包括有危险的`exec`以及`eval`函数
```python
import ast
import compileall
​
source\_code = """
@\_\_import\_\_("os").system("echo Inside foo decorator")
def foo():
  return "echo Inside foo decorator"
"""
source\_code1 = """
@exec("print('test')")
def foo():
  return "echo Inside foo decorator"
"""
parse\_ast = ast.parse(source\_code1)
for n in parsed\_ast.body:
   print(ast.dump(n))
code\_objct = compile(parsed\_ast, filename="<string>", mode="exec")
​
exec(code\_objct)
```
![image-20250421225417861.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-920de810750af1b076d9992618eb67e201a01482.png)
同时在[https://docs.python.org/3/re...