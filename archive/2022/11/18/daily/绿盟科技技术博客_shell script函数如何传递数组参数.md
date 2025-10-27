---
title: shell script函数如何传递数组参数
url: http://blog.nsfocus.net/shell-script/
source: 绿盟科技技术博客
date: 2022-11-18
fetch_date: 2025-10-03T23:07:12.360901
---

# shell script函数如何传递数组参数

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

# shell script函数如何传递数组参数

### shell script函数如何传递数组参数

[2022-11-17](https://blog.nsfocus.net/shell-script/ "shell script函数如何传递数组参数")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,032

给BASH函数传递数组参数的幺蛾子真多，测试整理了几种方案，其他方案大概率是这几种方案的变种。不得不说，BASH变得跟Perl一样离谱。

————————————————————————–
#!/bin/bash
#
# For bash 5.1.16
#
# ./arraytest.sh
#

#
# Passing arrays as parameters in bash – [2009-06-30]
# https://stackoverflow.com/questions/1063347/passing-arrays-as-parameters-in-bash
#
# How to pass an array as function argument – [2015-09-15]
# https://askubuntu.com/questions/60218/how-to-add-a-directory-to-the-path
#
# How to pass an array as function argument but with other extra parameters – [2022-02-14]
# https://unix.stackexchange.com/questions/690603/how-to-pass-an-array-as-function-argument-but-with-other-extra-parameters
#

function test\_0 ()
{
#
# 甚至可以不显式引用”${@}”
#
# for e in “${@}”
#
for e
do
echo “${e}”
done
}

##########################################################################

function test\_1 ()
{
while [ “${#}” -gt 0 ]
do
echo “${1}”
shift 1
done
}

##########################################################################

function test\_2 ()
{
#
# help declare
#
# 若需要indexed array，必须指定-a
#
local -a arr=(“${@}”)
#
# “${#arr[@]}”
#
local -i len=”${#}”
for ((i = 0; i < len; i++))
do
echo “${arr[$i]}”
done
}

##########################################################################

#
# 传引用，要求 bash 4.3+
#
function test\_3 ()
{
while [ “${#}” -gt 0 ]
do
local -n ref=”${1}”
for e in “${ref[@]}”
do
echo “${e}”
done
shift 1
done
}

##########################################################################

#
# 可传任意多个数组参数进来
#
function test\_4 ()
{
while [ “${#}” -gt 0 ]
do
#
# The ! in ${!1} expands the arg 1 variable
#
# ${!parameter} is called indirect reference or sometimes double
# referenced, this means that instead of using $1’s value, we use
# the value of the expanded value of $1
#
for e in “${!1}”
do
echo “${e}”
done
shift
done
}

##########################################################################

function test\_main ()
{
local arr\_0=(“1 one” “2 two” “3 three”)
local arr\_1=(“4 four”)
local arr\_2=(“5 five… 5” “6 six\_\_\_ 6”)

#
# 数组会被展开再传参
#
echo test\_0
test\_0 “${arr\_0[@]}” “${arr\_1[@]}” “${arr\_2[@]}”
echo

echo test\_1
test\_1 “${arr\_0[@]}” “${arr\_1[@]}” “${arr\_2[@]}”
echo

echo test\_2
test\_2 “${arr\_0[@]}” “${arr\_1[@]}” “${arr\_2[@]}”
echo

#
# 传引用
#
echo test\_3
test\_3 arr\_0 arr\_1 arr\_2
echo

#
# array are passed as names and are expanded in the function. Thus no
# $ is needed when given as parameters.
#
echo test\_4
test\_4 arr\_0[@] arr\_1[@] arr\_2[@]
echo
}

##########################################################################

test\_main
————————————————————————–

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/dynamorio-9/)

[Next](https://blog.nsfocus.net/weeklyreport47/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)