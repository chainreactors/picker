---
title: 用Arybo进行混合布尔运算分析
url: https://blog.nsfocus.net/%e7%94%a8arybo%e8%bf%9b%e8%a1%8c%e6%b7%b7%e5%90%88%e5%b8%83%e5%b0%94%e8%bf%90%e7%ae%97%e5%88%86%e6%9e%90/
source: 绿盟科技技术博客
date: 2025-09-04
fetch_date: 2025-10-02T19:36:52.795881
---

# 用Arybo进行混合布尔运算分析

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 用Arybo进行混合布尔运算分析

### 用Arybo进行混合布尔运算分析

[2025-09-03](https://blog.nsfocus.net/%E7%94%A8arybo%E8%BF%9B%E8%A1%8C%E6%B7%B7%E5%90%88%E5%B8%83%E5%B0%94%E8%BF%90%E7%AE%97%E5%88%86%E6%9E%90/ "用Arybo进行混合布尔运算分析")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 408

创建: 2025-08-12 17:22

————————————————————————–

目录:

☆ 背景介绍
☆ 环境搭建
1) 安装
2) 测试
☆ Tutorials
1) Symbloc evaluation of a complex function
2) Dirac function
2.2) 等价简化形式
2.3) 不合要求的等价简化形式
2.4) 快速识别Dirac函数
☆ 若干MBA分析示例
1) ~(a + b)
☆ 参考资源

————————————————————————–

☆ 背景介绍

MBA(Mixed Boolean Arithmetic)是一种将布尔运算和算术运算混合的技术，常用于
代码混淆。

参[1]，Arybo是一个Python库，可用于混合布尔运算分析，常用于逆向工程、反代码
混淆。

本文翻译Arybo入门教程。

☆ 环境搭建

1) 安装

建议在Python3虚拟环境中安装，最简安装方案

pip3 install arybo

后期测试时遭遇异常

AttributeError: module ‘numpy’ has no attribute ‘int’

升级networkx模块解决之

pip3 install –upgrade networkx

2) 测试

$ iarybo 8
…
These variables have been set for you:

mba = MBA(8)
x, y, a, b, c, d = 8-bit vars
…

意思是已经初始化过若干符号变量，可在提示符中直接使用

In [1]: x | 0x7f
Out[1]:
Vec([
1,
1,
1,
1,
1,
1,
1,
x7
])

位向量中x0对应LSB，x7对应MSB。意思是符号变量x按位或0x7f，结果只有最高位x7
可控。

☆ Tutorials

1) Symbloc evaluation of a complex function

————————————————————————–
def f ( x ) :
v0 = (x & 0xff) \* 0xe5 + 0xf7
v0 = v0 & 0xff
v3 = (((((v0 \* 0x26) + 0x55 ) & 0xfe) + (v0 \* 0xed) + 0xd6) & 0xff)
v4 = ((((((-(v3 \* 0x2)) + 0xff) & 0xfe) + v3) \* 0x03) + 0x4d)
v5 = (((((v4 \* 0x56) + 0x24) & 0x46) \* 0x4b) + (v4 \* 0xe7) + 0x76)
v7 = ((((v5 \* 0x3a) + 0xaf) & 0xf4) + (v5 \* 0x63) + 0x2e)
v6 = v7 & 0x94
v8 = ((((v6 + v6 + (-(v7 & 0xff))) \* 0x67) + 0xd))
res = ((v8 \* 0x2d) + (((v8 \* 0xae) | 0x22) \* 0xe5) + 0xc2) & 0xff
return (0xed \* (res – 0xf7)) & 0xff

print( f(255) )
————————————————————————–

假设有个函数f(x)，接受8位整数作参数，经过一系列眼花缭乱的MBA运算，返回另一
个8位整数。f(x)实际做了一个简单异或运算，(x^0x5c)。

下面用Arybo研究f(x)

————————————————————————–
import arybo.lib

def f ( x ) :
v0 = (x & 0xff) \* 0xe5 + 0xf7
v0 = v0 & 0xff
v3 = (((((v0 \* 0x26) + 0x55 ) & 0xfe) + (v0 \* 0xed) + 0xd6) & 0xff)
v4 = ((((((-(v3 \* 0x2)) + 0xff) & 0xfe) + v3) \* 0x03) + 0x4d)
v5 = (((((v4 \* 0x56) + 0x24) & 0x46) \* 0x4b) + (v4 \* 0xe7) + 0x76)
v7 = ((((v5 \* 0x3a) + 0xaf) & 0xf4) + (v5 \* 0x63) + 0x2e)
v6 = v7 & 0x94
v8 = ((((v6 + v6 + (-(v7 & 0xff))) \* 0x67) + 0xd))
res = ((v8 \* 0x2d) + (((v8 \* 0xae) | 0x22) \* 0xe5) + 0xc2) & 0xff
return (0xed \* (res – 0xf7)) & 0xff

mba = arybo.lib.MBA(8)
x = mba.var(‘x’)
ret = f(x)
print( ret )
————————————————————————–

执行上述代码，得到

————————————————————————–
Vec([
x0,
x1,
(x2 + 1),
(x3 + 1),
(x4 + 1),
x5,
(x6 + 1),
x7
])
————————————————————————–

位向量中x0对应LSB，x7对应MSB。人工识别出，f(x)等价于(x^0x5c)。

可用Arybo找出0x5c这个常量

————————————————————————–
app = ret.vectorial\_decomp([x])
print( hex(app.cst().get\_int\_be()) )
————————————————————————–

执行上述代码，得到

0x5c

此处有些反直觉，得用get\_int\_be()，不要用get\_int\_le()。

检验f(x)等价于(x^0x5c)

————————————————————————–
all(f(x) == (x^0x5c) for x in range(0x100))
————————————————————————–

应该返回True。

2) Dirac function

Dirac函数在其定义域上只有一个特定值处的函数值非常见值，定义域其余位置的函
数值均为常见值。这种函数很有趣，逆向工程师在尝试暴力破解时，可能会在一段时
间后误以为它总是返回常见值，这可能导致逆向工程师生成错误的代码，或者减缓TA
对代码逻辑的理解进程。

————————————————————————–
def f ( y ) :
t = ((y + 1) & (~y))
c = ((t | 0x7afafa697afafa69) & 0x80a061440a061440) + \
((~t & 0x10401050504) | 0x1010104)
return c

print( hex(f(0)) )
print( hex(f(100)) )
print( hex(f(0xfffffffffffffffe)) )
print( hex(f(0xffffffffffffffff)) )
————————————————————————–

上面这个f(y)是一个Dirac函数，在其定义域上函数值只有一个偏离，其余均为常见
值0xa061440b071544。无法用all()来检查f(y)，其定义域是64位整数，可接受时间
内无法穷举。

可用Arybo证明Dirac函数在其定义域上并非常量，进而找出使函数值偏离的自变量值。

————————————————————————–
import arybo.lib

def f ( y ) :
t = ((y + 1) & (~y))
c = ((t | 0x7afafa697afafa69) & 0x80a061440a061440) + \
((~t & 0x10401050504) | 0x1010104)
return c

mba = arybo.lib.MBA(64)
x = mba.var(‘x’)
ret = f(x)
print( ret )
————————————————————————–

执行上述代码，得到

————————————————————————–
Vec([
0,
0,
1,
…
0,
((x0 \* x1 \* … \* x62) + (x0 \* x1 \* … \* x63))
])
————————————————————————–

上述位向量的MSB是变化的，其余位则是常量，这表明Dirac函数在其定义域上并非常
量。

用Arybo进一步研究f(y)。绝大多数时候，f(y)的MSB是0，用Arybo找出使MSB为1的自
变量:

————————————————————————–
solutions = arybo.lib.boolean\_expr\_solve(ret[63], x, 1)
print( len(solutions) )
print( hex(solutions[0].get\_int\_be()) )
————————————————————————–

执行上述代码，得到

1
0x7fffffffffffffff

只有一个x使得MSB为1，此x为0x7fffffffffffffff

————————————————————————–
print( hex(f(5)) )
print( hex(f(0x7ffffffffffffffe)) )
print( hex(f(0x7fffffffffffffff)) )
————————————————————————–

执行上述代码，得到

0xa061440b071544 // 常见值
0xa061440b071544 // 常见值
0x80a061440b071544 // 偏离值

2.2) 等价简化形式

————————————————————————–
import arybo.lib

def f ( y ) :
y -= 0x7fffffffffffffff
s = ~((y | -y) >> 63) & 1
return (s << 63) ^ 0xa061440b071544

mba = arybo.lib.MBA(64)
x = mba.var(‘x’)
ret = f(x)
print( ret )
————————————————————————–

2.3) 不合要求的等价简化形式

————————————————————————–
import arybo.lib

def f ( y ) :
return (int(y == 0x7fffffffffffffff) << 63) ^ 0xa061440b071544

mba = arybo.lib.MBA(64)
x = mba.var(‘x’)
ret = f(x)
————————————————————————–

这是人类最易理解的等价简化形式，但此实现不合要求，无法对f(y)传递符号变量，
“ret = f(x)”会抛异常。

2.4) 快速识别Dirac函数

————————————————————————–
import arybo.lib

def f ( y ) :
return y ^ y ^ 0xa061440b071544

mba = arybo.lib.MBA(64)
x = mba.var(‘x’)
ret = f(x)
print( ret )
————————————————————————–

若f()始终返回常量，ret的位向量中将全是常量，没有变量，反之则是Dirac函数；
无需分析app。

————————————————————————–
app = ret.vectorial\_decomp([x])
print( app )
————————————————————————–

若非要看看app，会注意到App NL、AffApp matrix全零。

☆ 若干MBA分析示例

1) ~(a + b)

尝试用Arybo化简下面的e变量

————————————————————————–
import arybo.lib

#
# 4位的代表性足够了
#
mba = arybo.lib.MBA(4)
a = mba.var(‘a’)
b = mba.var(‘b’)
e = ~(~(a ^ b) – 4294967294 \* (b | a) + 1)
print( e )
app = e.vectorial\_decomp([a,b])
print( app )
————————————————————————–

执行上述代码，得到

————————————————————————–
Vec([
(a0 + b0 + 1),
((a0 \* b0) + a1 + b1 + 1),
((a1 \* b1) + (a0 \* a1 \* b0) + (a0 \* b0 \* b1) + a2 + b2 + 1),
((a2 \* b2) + (a1 \* a2 \* b1) + (a1 \* b1 \* b2) + (a0 \* a1 \* a2 \* b0) + (a0 \* a1 \* b0 \* b2) + (a0 \* a2 \* b0 \* b1) + (a0 \* b0 \* b1 \* b2) + a3 + b3 + 1)
])

App NL = Vec([
0,
(\_0 \* \_4),
((\_1 \* \_5) + (\_0 \* \_1 \* \_4) + (\_0 \* \_4 \* \_5)),
((\_2 \* \_6) + (\_1 \* \_2 \* \_5) + (\_1 \* \_5 \* \_6) + (\_0 \* \_1 \* \_2 \* \_4) + (\_0 \* \_1 \* \_4 \* \_6) + (\_0 \* \_2 \* \_4 \* \_5) + (\_0 \* \_4 \* \_5 \* \_6))
])

AffApp matrix = Mat([
[1, 0, 0, 0, 1, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 1, 0]
[0, 0, 0, 1, 0, 0, 0, 1]
])

AffApp cst = Vec([
1,
1,
1,
1
])
————————————————————————–

打印e，不太容易直接看出结果，除非特别熟悉某些知识。尝试分析app，逼近结果。

最终结果的数学形式是:

(非线性部分) ^ (仿射变换矩阵 \* 输入) ^ (常量部分)
(App NL) ^ ((AffApp matrix) \* [a, b]^T) ^ (AffApp cst)

T表示转置，将拼接后的行向量转置成列向量，否则无法进行”矩阵 \* 向量”的运算。

“AffApp matrix”是两个拼接的单位矩阵(I)。在GF(2)域的矩阵乘法中

[I | I] \* [a, b]^T = (a ^ b)

于是有

(仿射变换矩阵 \* 输入)=(a ...