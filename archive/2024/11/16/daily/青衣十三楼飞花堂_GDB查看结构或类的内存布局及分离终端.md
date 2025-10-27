---
title: GDB查看结构或类的内存布局及分离终端
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487732&idx=1&sn=9e7e2ec905f0242b01f9ebdc5d4a5d6e&chksm=fab2d3cbcdc55addc024811a12349490612b1acdf7d11b4a65bd331bbc3bff46b8eb649ea5a1&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-11-16
fetch_date: 2025-10-06T19:17:59.057789
---

# GDB查看结构或类的内存布局及分离终端

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPP8xT8UDgmicAQTabgYehDt9ibP83KgicpHoiazc508iatNDJy5iaQAe8c6VIcLnh8sWJy70xEXmByiaiafoA/0?wx_fmt=jpeg)

# GDB查看结构或类的内存布局及分离终端

原创

沈沉舟

青衣十三楼飞花堂

```
创建: 2024-11-15 16:04
https://scz.617.cn/unix/202411151604.txt
```

因故需要了解std::string类型内存布局。以前没接触过，属于初次产生的需求。正常思路是，写测试程序，带调试信息编译，gdb调试，设法查看内存布局。绝大多数struct、class，若想了解其内存布局，首选方案即此。

```
/*
 * g++ -Wall -pipe -O0 -g3 -o stddbg stddbg.cpp
 */
#include <string>
#include <iostream>

int main ( int argc, char * argv[] )
{
    std::string input;

    std::cout << "Please enter a string: ";
    /*
     * std::getline会一直读取，直至\n
     */
    // std::getline( std::cin, input );
    /*
     * 读取到第一个空白字符(空格、制表符、换行符等)为止
     */
    std::cin >> input;
    std::cout << "You entered: " << input << std::endl;
    return 0;
}
```

gdb ./stddbg
start

断在main()入口时，查看input变量

```
(gdb) whatis input
type = std::string
```

whatis命令只会报变量类型，想看struct、class的成员，得用ptype命令。struct还好说，class有method，直接"ptype input"，输出中method占了大头。ptype有参数，只看类成员，不看类方法。此外，既想了解class内存布局，肯定想知道类成员偏移、大小等信息，ptype也有相应参数。

```
(gdb) ptype /rmtox input
(gdb) ptype /rmtox std::string
type = class std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > {
                             private:
/* 0x0000      |  0x0008 */    struct std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_Alloc_hider : public std::allocator<char> {
/* 0x0000      |  0x0008 */        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::pointer _M_p;

                                   /* total size (bytes):    8 */
                               } _M_dataplus;
/* 0x0008      |  0x0008 */    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::size_type _M_string_length;
/* 0x0010      |  0x0010 */    union {
/*                0x0010 */        char _M_local_buf[16];
/*                0x0008 */        std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::size_type _M_allocated_capacity;

                                   /* total size (bytes):   16 */
                               };

                               /* total size (bytes):   32 */
                             }
```

前述输出中，左侧第一列是偏移，第二列是长度。

可用ptype查看struct、class指定成员

```
(gdb) ptype /rmtox ((std::string *)0)->_M_dataplus
(gdb) ptype /rmtox std::string::_M_dataplus
/* offset      |    size */  type = struct std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_Alloc_hider : public std::allocator<char> {
/* 0x0000      |  0x0008 */    std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::pointer _M_p;

                               /* total size (bytes):    8 */
                             }
```

若是struct，只能用第一种办法，若是class，两种办法均可

若gdb支持Python，可自实现offsetof命令

```
import gdb

class Offset ( gdb.Command ) :

    def __init__ (self ) :
        super( Offset, self ).__init__ ( 'offsetof', gdb.COMMAND_DATA )

    def invoke ( self, arg, from_tty ) :
        arg     = arg.strip()
        stype   = gdb.lookup_type( arg )
        print( "%s %s" % ( arg, '{' ) )
        for field in stype.fields() :
            print( '    %s => %#x' % ( field.name, field.bitpos // 8 ) )
        print( '}' )

Offset()
```

(gdb) offsetof std::string
std::string {
    \_M\_dataplus => 0x0
    \_M\_string\_length => 0x8
    None => 0x10
}

结合前述调试信息，64位std:string内存布局如下:

```
std:string
{
    /*
     * 长度小的时候，_M_dataplus指向_M_local_buf[]
     */
    char               *_M_dataplus;        // +0x0
    unsigned long long  _M_string_length;   // +0x8
    char                _M_local_buf[16];   // +0x10
                                            // +0x20
}
```

windbg的dt，可查看指定结构，给定地址时，同时查看结构内存布局及各成员变量的值。gdb无法完全做到dt的效果，但下面这些命令比较接近:

```
p /address input
p -raw-values on -- input
p -raw-values on -- *(std::string *)($rbp-0x40)

$24 = {
  _M_dataplus = {
    <std::allocator<char>> = {
      <__gnu_cxx::new_allocator<char>> = {<No data fields>}, <No data fields>},
    members of std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_Alloc_hider:
    _M_p = 0x7fffffffe0f0 "scz_is_here"
  },
  _M_string_length = 11,
  {
    _M_local_buf = "scz_is_here\000\377\177\000",
    _M_allocated_capacity = 7520856799142634355
  }
}
```

顺便提一下gdb调试stddbg时如何分离终端。stddbg会与stdout、stdin打交道，gdb调试可能出现干扰。理想情况是，让gdb在终端A输入输出，让被调试的stddbg在终端B输入输出。

```
在终端B中

$ tty && tail -f /dev/null
/dev/pts/B

假设是这个输出，下面会用到
```

---

```
在终端A中

gdb -tty=/dev/pts/B ./stddbg
start

若不在命令行指定"-tty"参数，也可在(gdb)提示符下执行

set inferior-tty /dev/pts/B
```

终端B中的命令，属于奇技淫巧。gdb调试时，分离终端若无异常，则不必执行终端B中的命令，有异常时不妨一试。所谓异常是指，在终端B中的交互残缺，比如回显异常、换行异常等等。

gdb调试碰上分离终端的需求，可能用tmux更友好些，下面是相关操作:

```
tmux

Ctrl-B % (全松开后再按%)

    垂直分割

Ctrl-B " (全松开后再按")

    水平分割

Ctrl-B 方向键 (全松开后再按方向键)

    在分割的窗口间切换
```

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过