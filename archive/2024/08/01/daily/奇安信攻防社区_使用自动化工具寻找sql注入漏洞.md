---
title: 使用自动化工具寻找sql注入漏洞
url: https://forum.butian.net/share/3644
source: 奇安信攻防社区
date: 2024-08-01
fetch_date: 2025-10-06T17:59:17.095693
---

# 使用自动化工具寻找sql注入漏洞

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

### 使用自动化工具寻找sql注入漏洞

* [漏洞分析](https://forum.butian.net/topic/48)

对某开源cms进行代码审计 ，发现虽然该cms虽然对参数参数进行了过滤，但是过滤有限，依然可以通过其他方法绕过进行sql注入，本文将将通过正则匹配的方式，并通过自动化查找工具，寻找某cms中存在的sql注入漏洞

对某开源cms进行代码审计 ，发现虽然该cms虽然对参数参数进行了过滤，但是过滤有限，依然可以通过其他方法绕过进行sql注入，本文将将通过正则匹配的方式，并通过自动化查找工具，寻找某cms中存在的sql注入漏洞
1. 漏洞分析
=======
由于该cms过滤了引号，那这里我们寻找的拼接的地方主要是以括号，反引号和直接拼接的。
首先寻用括号包裹的sql语句，可以使用正则进行查找`=.\*?".\*?\("\s\*?\.\s\*?(\$\w+)`或者``=.\*?".\*?\("\s\*?\.\s\*?(front::)`。这里简单解释一下正则的意思，首先sql语句存在的地方一般是一个赋值语句，所以需要有等号：`=.\*?`，然后需要匹配左括号加引号，然后使用`\s\*?\.\s\*?`匹配连接变量的`.`然后使用`(\$\w+)`匹配变量
![image-20240613172513760](https://oss-yg-cztt.yun.qianxin.com/butian-public/f8f4022fc606b977e760096eead344145.png)
我们找到这样一处
![image-20240607095958252](https://oss-yg-cztt.yun.qianxin.com/butian-public/f0697b67c9ff7d90f107e7cac92184188.png)
这里的参数被两个括号包裹，并且没有被引号包裹，所以这里只需要使用后括号对语句进行闭合而不需要引号。
![image-20240607100251224](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa8e203e0f38a14cbb401519f0038e50d.png)
然后一路向前追溯`$cids`的来源，发现他是通过`$sons`以`,`为分隔符的得到的，然后向前一路追溯最终发现是可以通过`front::post('search\_catid')`的得到，即这里的传参可控。由于中间的参数需要以`,`为分隔，所以注入的语句中不能出现逗号，这里很好操作，有很多方法可以绕过，这里使用`from` `for`绕过
2.路由分析
======
该cms是一个典型的MVC架构的web应用程序。
在初始化方法中，通过GET请求取`case`和`cat`参数分别
![image-20240607173809220](https://oss-yg-cztt.yun.qianxin.com/butian-public/f0772ba11be66bd50a1179c7324b57d24.png)
然后在main函数中调用`dispath`方法，首先会判断如果同时满足为admin，case值不为`admin`和`install`，则会将case的值加`\_admin`，如不满足则加`\_act`作为控制器名，接着将传入的方法`$cat`后添加`\_cation`作为方法名。最后使用`$case->$method()`进行调用
![image-20240607172150906](https://oss-yg-cztt.yun.qianxin.com/butian-public/f4b0d09d9eb7a105ba57c0ccc1ac04b32.png)
3.漏洞复现
======
上面分析的代码在`archive\_cat.php`文件中的`search\_action`方法，所以路由为`index.php?case=archive&act=search`
![image-20240607144159024](https://oss-yg-cztt.yun.qianxin.com/butian-public/fa4e338b6f03f4cae6a552e6477c34710.png)
![image-20240607144216098](https://oss-yg-cztt.yun.qianxin.com/butian-public/f1861696006f390c3f6d91320bccf0bbd.png)
4.自动化查找
=======
通过分析漏洞的实现，实际上就是先用正则匹配相关语句，然后向上溯源参数在赋值和传递的过程中是否可以抵达可控点，如果未数字型的sql注入，还需要排除变量或参数被`intval()`强转的情况，被既然是这种重复和相同的工作，那么当然可以通过简单的脚本来进行批量查找。
这里使用python语言写了一个脚本用来批量查找，使用该脚本有三个前提：
1. 目前自动查找的语言只支持php语言
2. 需要自己设置需要匹配漏洞点的正则和可控点函数的正则
3. 溯源的参数与可控点在同一函数内
```python
import os
import re
folder = r"D:\code"
regex = re.compile(r"""=.\*?".\*?\("\s\*?\.\s\*?(\$\w+)""") # 需要匹配的正则
input\_func = re.compile('front::[$]\*[g|p]') # 可控点函数正则
vuln\_code = ''
def find\_php\_files(directory):
for root, dirs, files in os.walk(directory):
for file in files:
if file.endswith(".php"):
yield os.path.join(root, file)
def check\_regex(file\_lines):
for line\_number, line in enumerate(file\_lines):
match = re.findall(regex, line)
if match:
yield line\_number, match[0], line
def get\_func\_line\_range(php\_code, code, code\_line\_number):
function\_pattern = re.compile(r'function\s+(?P<name>\w+)\s\*\((?P<params>[^\)]\*)\)\s\*\{', re.DOTALL)
matches = function\_pattern.finditer(php\_code)
# 遍历所有匹配项
for match in matches:
function\_name = match.group('name')
parameters = match.group('params')
start\_pos = match.start()
start\_line = php\_code.count('\n', 0, start\_pos) + 1
# 用于追踪嵌套的堆栈
brace\_stack = []
function\_body\_start = match.end()
function\_body\_end = function\_body\_start
brace\_stack.append('{')
for i in range(function\_body\_start, len(php\_code)):
if php\_code[i] == '{':
brace\_stack.append('{')
elif php\_code[i] == '}':
if brace\_stack:
brace\_stack.pop()
if not brace\_stack:
function\_body\_end = i + 1
break
end\_line = php\_code.count('\n', 0, function\_body\_end) + 1
function\_body = php\_code[function\_body\_start:function\_body\_end]
if code in function\_body and start\_line < code\_line\_number < end\_line:
yield [start\_line, end\_line]
def retrack\_input\_func(file\_lines, line\_range, var, file, code, code\_line\_number):
# 定义匹配参数赋值的正则表达式，捕获所有变量和函数
assignment\_pattern = re.compile(var.replace('$', '\$') + r'\s\*=\s\*(?P<source>[^;]+);')
source\_extraction\_pattern = re.compile(r'(\$\w+[\->\w+]\*)')
for line in range(line\_range[1] - 1, line\_range[0], -1): # 从下到上遍历
for match in assignment\_pattern.finditer(file\_lines[line]):
source\_code = match.group('source').strip()
# print(source\_code)
if 'intval(' in source\_code:
continue
if re.findall(input\_func, source\_code):
global vuln\_code
if vuln\_code == code.strip(): # 排除因为溯源路径不同而产出的相同结果
continue
vuln\_code = code.strip()
print(file)
print(f'第{line + 1}行参数点可控', file\_lines[line].strip())
print(f'第{code\_line\_number + 1}行可能存在漏洞', vuln\_code)
print('----------------------------------------------')
return True
sources = source\_extraction\_pattern.findall(source\_code)
for source in sources:
new\_line\_range = [line\_range[0], line]
retrack\_input\_func(file\_lines, new\_line\_range, source, file, code, code\_line\_number) # 递归调用
else:
return False
def main():
for file in find\_php\_files(folder):
with open(file, encoding='utf-8', errors='ignore') as f:
file\_content = f.read()
file\_lines = file\_content.splitlines()
for code\_line\_number, var, code in check\_regex(file\_lines): # 使用正则匹配出语句所在位置
if not var:
continue
for line\_range in get\_func\_line\_range(file\_content, code, code\_line\_number): # 判断该语句所在的函数范围
retrack\_input\_func(file\_lines, line\_range, var, file, code, code\_line\_number) # 向上追溯是否能找到可控点函数
pass
if \_\_name\_\_ == '\_\_main\_\_':
main()
```
用不到100行的代码即可实现该功能，该脚本的主要流程会在main函数中，首先会遍历该文件夹下的所有php函数，然后使用正则匹配出语句所在的位置，同时为了在同一函数中向上追溯，还需要确定该变量或参数所在的是哪个函数，确实该函数的位置，然后进行向上追溯看是否存在可控点。
代码逻辑流程主要总结为以下四个方面
1. \*\*遍历文件\*\*
- `find\_php\_files` -&gt; 返回 PHP 文件路径列表
2. \*\*检查正则匹配\*\*
- `check\_regex` -&gt; 返回匹配到的行号、变量、代码行
3. \*\*确定函数范围\*\*
- `get\_func\_line\_range` -&gt; 返回代码所在函数的行号范围
4. \*\*追溯变量赋值\*\*
- `retrack\_input\_func` -&gt; 检查变量赋值是否包含可控点函数调用，输出结果
从main函数来看，首先使用`find\_php\_files`方法来遍历指定目录及其子目录，找到所有以 `.php` 结尾的文件，并返回它们的完整路径。然后读取每个php文件的内容，然后使用`check\_regex`方法来使用我们预设的正则逐行匹配php文件中找出符合条件的代码行及匹配到的信息，如果为未匹配到，则使用`continue`跳过这次循环匹配下一个文件。如果匹配到，则使用`get\_func\_line\_range`方法来确定该行代码所在的函数的行号范围，因为我们向上追溯变量时只能在同一函数下追溯。
```python
def get\_func\_line\_range(php\_code, code, code\_line\_number): # 确定函数行数范围
function\_pattern = re.compile(r'function\s+(?P<name>\w+)\s\*\((?P<params>[^\)]\*)\)\s\*\{', re.DOTALL)
matches = function\_pattern.finditer(php\_code)
# 遍历所有匹配项
for match in matches:
function\_name = match.group('name')
parameters = match.group('params')
start\_pos = match.start()
start\_line = php\_code.count('\n', 0, start\_pos) + 1
# 用于追踪嵌套的堆栈
brace\_stack = []
function\_body\_start = match.end()
function\_body\_end = function\_body\_start
brace\_stack.append('{')
for i in range(function\_body\_start, len(php\_code)):
if php\_code[i] == '{':
brace\_stack.append('{')
elif php\_code[i] == '}':
if brace\_stack:
brace\_stack.pop()
if not brace\_stack:
function\_body\_end = i + 1
break
end\_line = php\_code.count('\n', 0, function\_body\_end) + 1
function\_body = php\_code[function\_body\_start:function\_body\_end]
if code in function\_body and start\_line < code\_line\_number < end\_line:
yield [start\_line, end\_line]
```
以上是确定函数行数范围的代码，由于函数体不好用正则取匹配，但我们又知道php的函数体都是通过大括号包裹起来的，所以我们可以寻找到`function xxx()`之后的第一个`{`，然后将其入栈，之后每匹配到一个`{`都会入栈，匹配到`}`则会出栈，并且判断栈是否为空，如果为空则代表完整的包裹了整个函数体。并且记录下来当前的行号即为结束行号，匹配到所有函数体后只需要判断匹配到的代码在哪个函数体内即可返回对应函数体所在的行数范围了。
```python
def retrack\_input\_func(file\_lines, line\_range, var, file, code, code\_line\_number):...