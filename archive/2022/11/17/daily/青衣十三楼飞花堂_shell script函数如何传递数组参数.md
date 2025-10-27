---
title: shell script函数如何传递数组参数
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247486312&idx=1&sn=25e77e5ce821b02c2c42a0ee41c7dcc3&chksm=fab2c857cdc541416ae5c8fcdcaf3f57d71af9826bdb438f25fe4779a7414381e310acee94e7&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2022-11-17
fetch_date: 2025-10-03T23:01:22.424321
---

# shell script函数如何传递数组参数

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPO5gQk293lR7g1TILyfZXhoaTgKBNrs7K0DlK563HiaQUba08MQicKY3hxEY3amajvM8B4Q2Zp8vmgw/0?wx_fmt=jpeg)

# shell script函数如何传递数组参数

原创

沈沉舟

青衣十三楼飞花堂

20.37 shell script函数如何传递数组参数

```
http://scz.617.cn:8/unix/202211161222.txt
```

A: scz 2022-11-16

参看《20.26 $0 ${1+"$@"}什么意思》

给BASH函数传递数组参数的幺蛾子真多，测试整理了几种方案，其他方案大概率是这几种方案的变种。不得不说，BASH变得跟Perl一样神经病。

```
#!/bin/bash
#
# For bash 5.1.16
#
# ./arraytest.sh
#

#
# Passing arrays as parameters in bash - [2009-06-30]
# https://stackoverflow.com/questions/1063347/passing-arrays-as-parameters-in-bash
#
# How to pass an array as function argument - [2015-09-15]
# https://askubuntu.com/questions/60218/how-to-add-a-directory-to-the-path
#
# How to pass an array as function argument but with other extra parameters - [2022-02-14]
# https://unix.stackexchange.com/questions/690603/how-to-pass-an-array-as-function-argument-but-with-other-extra-parameters
#

function test_0 ()
{
    #
    # 甚至可以不显式引用"${@}"
    #
    # for e in "${@}"
    #
    for e
    do
        echo "${e}"
    done
}

##########################################################################

function test_1 ()
{
    while [ "${#}" -gt 0 ]
    do
        echo "${1}"
        shift 1
    done
}

##########################################################################

function test_2 ()
{
    #
    # help declare
    #
    # 若需要indexed array，必须指定-a
    #
    local -a arr=("${@}")
    #
    # "${#arr[@]}"
    #
    local -i len="${#}"
    for ((i = 0; i < len; i++))
    do
        echo "${arr[$i]}"
    done
}

##########################################################################

#
# 传引用，要求 bash 4.3+
#
function test_3 ()
{
    while [ "${#}" -gt 0 ]
    do
        local -n ref="${1}"
        for e in "${ref[@]}"
        do
            echo "${e}"
        done
        shift 1
    done
}

##########################################################################

#
# 可传任意多个数组参数进来
#
function test_4 ()
{
    while [ "${#}" -gt 0 ]
    do
        #
        # The ! in ${!1} expands the arg 1 variable
        #
        # ${!parameter} is called indirect reference or sometimes double
        # referenced, this means that instead of using $1's value, we use
        # the value of the expanded value of $1
        #
        for e in "${!1}"
        do
            echo "${e}"
        done
        shift
    done
}

##########################################################################

function test_main ()
{
    local arr_0=("1 one" "2 two" "3 three")
    local arr_1=("4 four")
    local arr_2=("5 five... 5" "6 six___ 6")

    #
    # 数组会被展开再传参
    #
    echo test_0
    test_0 "${arr_0[@]}" "${arr_1[@]}" "${arr_2[@]}"
    echo

    echo test_1
    test_1 "${arr_0[@]}" "${arr_1[@]}" "${arr_2[@]}"
    echo

    echo test_2
    test_2 "${arr_0[@]}" "${arr_1[@]}" "${arr_2[@]}"
    echo

    #
    # 传引用
    #
    echo test_3
    test_3 arr_0 arr_1 arr_2
    echo

    #
    # array are passed as names and are expanded in the function. Thus no
    # $ is needed when given as parameters.
    #
    echo test_4
    test_4 arr_0[@] arr_1[@] arr_2[@]
    echo
}

##########################################################################

test_main
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