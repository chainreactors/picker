---
title: GDB查看结构或类的内存布局及分离终端
url: https://blog.nsfocus.net/gdb/
source: 绿盟科技技术博客
date: 2024-11-20
fetch_date: 2025-10-06T19:18:06.583672
---

# GDB查看结构或类的内存布局及分离终端

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

# GDB查看结构或类的内存布局及分离终端

### GDB查看结构或类的内存布局及分离终端

[2024-11-19](https://blog.nsfocus.net/gdb/ "GDB查看结构或类的内存布局及分离终端")[绿盟科技](https://blog.nsfocus.net/author/nsfocuser/ "View all posts by 绿盟科技")

阅读： 741

因故需要了解std::string类型内存布局。以前没接触过，属于初次产生的需求。正常思路是，写测试程序，带调试信息编译，gdb调试，设法查看内存布局。绝大多数struct、class，若想了解其内存布局，首选方案即此。

————————————————————————–
/\*
\* g++ -Wall -pipe -O0 -g3 -o stddbg stddbg.cpp
\*/
#include <string>
#include <iostream>

int main ( int argc, char \* argv[] )
{
std::string input;

std::cout << “Please enter a string: “;
/\*
\* std::getline会一直读取，直至\n
\*/
// std::getline( std::cin, input );
/\*
\* 读取到第一个空白字符(空格、制表符、换行符等)为止
\*/
std::cin >> input;
std::cout << “You entered: ” << input << std::endl;
return 0;
}
————————————————————————–

gdb -q -nx -x ~/src/gdbinit\_x64.txt -x ~/src/gdbhelper.py ./stddbg
set debuginfod enabled on
start

断在main()入口时，查看input变量

(gdb) whatis input
type = std::string

whatis命令只会报变量类型，想看struct、class的成员，得用ptype命令。struct还好说，class有method，直接”ptype input”，输出中method占了大头。ptype有参数，只看类成员，不看类方法。此外，既想了解class内存布局，肯定想知道类成员偏移、大小等信息，ptype也有相应参数。

(gdb) ptype /rmtox input
(gdb) ptype /rmtox std::string
type = class std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> > {
private:
/\* 0x0000 | 0x0008 \*/ struct std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::\_Alloc\_hider : public std::allocator<char> {
/\* 0x0000 | 0x0008 \*/ std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::pointer \_M\_p;

/\* total size (bytes): 8 \*/
} \_M\_dataplus;
/\* 0x0008 | 0x0008 \*/ std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::size\_type \_M\_string\_length;
/\* 0x0010 | 0x0010 \*/ union {
/\* 0x0010 \*/ char \_M\_local\_buf[16];
/\* 0x0008 \*/ std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::size\_type \_M\_allocated\_capacity;

/\* total size (bytes): 16 \*/
};

/\* total size (bytes): 32 \*/
}

前述输出中，左侧第一列是偏移，第二列是长度。”/rmtox”的具体意义可”help ptype”了解。ptype指定多个选项时，不能写成”/r /m /t /o /x”，只能写成”/rmtox”，这什么病？

可用ptype查看struct、class指定成员

(gdb) ptype /rmtox ((std::string \*)0)->\_M\_dataplus
(gdb) ptype /rmtox std::string::\_M\_dataplus
/\* offset | size \*/ type = struct std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::\_Alloc\_hider : public std::allocator<char> {
/\* 0x0000 | 0x0008 \*/ std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::pointer \_M\_p;

/\* total size (bytes): 8 \*/
}

若是struct，只能用第一种办法，若是class，两种办法均可

(gdb) ptype /rmtox std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::pointer
type = char \*

(gdb) ptype /rmtox std::string::\_M\_string\_length
type = unsigned long

若gdb支持Python，可自实现offsetof命令

————————————————————————–
import gdb

class Offset ( gdb.Command ) :

def \_\_init\_\_ (self ) :
super( Offset, self ).\_\_init\_\_ ( ‘offsetof’, gdb.COMMAND\_DATA )

def invoke ( self, arg, from\_tty ) :
arg = arg.strip()
stype = gdb.lookup\_type( arg )
print( “%s %s” % ( arg, ‘{‘ ) )
for field in stype.fields() :
print( ‘ %s => %#x’ % ( field.name, field.bitpos // 8 ) )
print( ‘}’ )

Offset()
————————————————————————–

(gdb) offsetof std::string
std::string {
\_M\_dataplus => 0x0
\_M\_string\_length => 0x8
None => 0x10
}

结合前述调试信息，64位std:string内存布局如下:

————————————————————————–
std:string
{
/\*
\* 长度小的时候，\_M\_dataplus指向\_M\_local\_buf[]
\*/
char \*\_M\_dataplus; // +0x0
unsigned long long \_M\_string\_length; // +0x8
char \_M\_local\_buf[16]; // +0x10
// +0x20
}
————————————————————————–

windbg的dt，可查看指定结构，给定地址时，同时查看结构内存布局及各成员变量的值。gdb无法完全做到dt的效果，但下面这些命令比较接近:

p /address input
p -raw-values on — input
p -raw-values on — \*(std::string \*)($rbp-0x40)

$24 = {
\_M\_dataplus = {
<std::allocator<char>> = {
<\_\_gnu\_cxx::new\_allocator<char>> = {<No data fields>}, <No data fields>},
members of std::\_\_cxx11::basic\_string<char, std::char\_traits<char>, std::allocator<char> >::\_Alloc\_hider:
\_M\_p = 0x7fffffffe0f0 “scz\_is\_here”
},
\_M\_string\_length = 11,
{
\_M\_local\_buf = “scz\_is\_here\000\377\177\000″,
\_M\_allocated\_capacity = 7520856799142634355
}
}

顺便提一下gdb调试stddbg时如何分离终端。stddbg会与stdout、stdin打交道，gdb调试可能出现干扰。理想情况是，让gdb在终端A输入输出，让被调试的stddbg在终端B输入输出。

————————————————————————–
在终端B中

$ tty && tail -f /dev/null
/dev/pts/B

假设是这个输出，下面会用到
————————————————————————–
在终端A中

gdb -q -nx -x ~/src/gdbinit\_x64.txt -x ~/src/gdbhelper.py -tty=/dev/pts/B ./stddbg
set debuginfod enabled on
start

若不在命令行指定”-tty”参数，也可在(gdb)提示符下执行

set inferior-tty /dev/pts/B
————————————————————————–

终端B中的命令，属于奇技淫巧。gdb调试时，分离终端若无异常，则不必执行终端B中的命令，有异常时不妨一试。所谓异常是指，在终端B中的交互残缺，比如回显异常、换行异常等等。

gdb调试碰上分离终端的需求，可能用tmux更友好些，下面是相关操作:

————————————————————————–
tmux

Ctrl-B % (全松开后再按%)

垂直分割

Ctrl-B ” (全松开后再按”)

水平分割

Ctrl-B 方向键 (全松开后再按方向键)

在分割的窗口间切换
————————————————————————–

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/microsoftnov-3/)

[Next](https://blog.nsfocus.net/weeklyreport202446/)

### Meet The Author

绿盟科技

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)