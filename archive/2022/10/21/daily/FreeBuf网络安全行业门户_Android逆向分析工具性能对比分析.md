---
title: Android逆向分析工具性能对比分析
url: https://www.freebuf.com/sectool/347405.html
source: FreeBuf网络安全行业门户
date: 2022-10-21
fetch_date: 2025-10-03T20:30:35.197778
---

# Android逆向分析工具性能对比分析

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Android逆向分析工具性能对比分析

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

Android逆向分析工具性能对比分析

2022-10-21 09:41:12

所属地 广东省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

## 前言

本次测试对比是为了呈现incinerator与PNFSofteware出品的JEB以及国内出品GDA在Android逆向工程能力的对比，从而让大家更好更直观的了解相关的详细信息

**本次测试对比的产品信息如下：**

Incinerator： 1.0.0

JEB：3.19.1.202005071620

GDA：3.9.0

**注：文章编写日期与发布时间有一定时间间隔，所以以下内容并不代表各产品的后续性能指标。**

## 反编译器对循环结构的还原能力测试

### Test1

第一个测试中，设计了循环头和锁节点都为二路条件循环结构，为了测试循环结构化分析能力，多嵌套了几个if语句（代码标号为基本块号）。程序简单如下：

`public void test1(int y, int a) {
while(y > 0) {
if(a <= 0) {
a = a + 1;
y = y + 1;
} else {
if(a > 10) {
if(a > 100) {
a = a * 5;
break;
} else {
y = y / a;
}
}
}
}
}`

![1665978135_634ccf17ecbcf23ced8bb.png!small?1665978137918](https://image.3001.net/images/20221017/1665978135_634ccf17ecbcf23ced8bb.png!small?1665978137918)

编写testdemo将代码段生成apk后，并分别使用JEB、GDA、Incinerator来进行反编译操作，从而进行代码可读性和语义准确性上的对比，如下图所示：

![1665978254_634ccf8eb95cc7eb947fb.png!small?1665978256490](https://image.3001.net/images/20221017/1665978254_634ccf8eb95cc7eb947fb.png!small?1665978256490)

test1

通过上述对比可以看出

在语义准确性上，JEB发生了语义错误，在a > 100时，丢失了a \*= 5的代码块，Incinerator与GDA保持了语义的准确性。

在代码可读性上，三者相差不大可读性都很好。Incinerator在if-else上做了相应的优化，可读性略有提升。

在代码还原度上，Incinerator做了对应优化，GDA重复声明了a、y变量，其他方面最为接近源码。而JEB存在代码块丢失。

| 反编译器 | 语义准确性 | 代码可读性 | 代码还原度 |
| --- | --- | --- | --- |
| Incinerator | ✓ | 高 | 高 |
| JEB | × | 高 | 中 |
| GDA | ✓ | 高 | 高 |

### Test2

接下来看看他们对双层循环的结构化分析的能力，设计一个双层循环，在内层循环break出外层循环，实际上基本块5即if(a > 10)，不仅会是内存循环的锁节点，也会是外层循环的锁节点。并且该锁节点为二路条件节点，其一个分支路径回到内层循环，另外一个分支结构回到外层循环。一般对循环结构算法都是循环头-锁节点一一对应，因此处理过程中可能会复杂化该类结构。代码实现非常简单如下：

```
public void test2(int y, int a) {
        while(y > 0) {
            while(a > 0) {
                if(a <= 0) {
                    a = a + 1;
                    y = y + 1;
                } else {
                    if(a > 10) {
                        break;
                    }
                }
            }
        }
        attachBaseContext(this);
    }
```

重新编译apk后，再进行反编译后，如下图所示：

![1665978273_634ccfa11d2dd07d13d4a.png!small?1665978275066](https://image.3001.net/images/20221017/1665978273_634ccfa11d2dd07d13d4a.png!small?1665978275066)

test2

通过上述对比可以看出

在语义准确性上，Incinerator、JEB保持了语义的准确性，都识别除了双重循环，GDA仅有函数声明，丢失了整个函数的代码块。

在代码可读性上，Incinerator优化了if-else组合，JEB在if中加入continue省略else语句，两者可读性都很好。

在代码还原度上，Incinerator、JEB除了各自在if-else上的优化，还原度都很高。

| 反编译器 | 语义准确性 | 代码可读性 | 代码还原度 |
| --- | --- | --- | --- |
| Incinerator | ✓ | 高 | 高 |
| JEB | ✓ | 高 | 高 |
| GDA | × | 低 | 低 |

### Test3

这一段代码在退出循环的”if(a>10)”语句中内嵌了另外一个if语句，这会导致内层循环的锁节点发生变化，并且给内层循环添加了一个跟随节点，另外代码做了稍稍的改动。如下：

```
public void test3(int y, int a) {
        while(y > 0) {
            while(a > 50) {
                a = a + 1;
                y = y + 1;
                if(a > 10) {
                    if(a > 100) {
                        a = a * 5;
                        break;
                    } else {
                        y = y / a;
                    }
                }
            }
            this.attachBaseContext(this);
        }
    }
```

继续编译成apk，再进行反编译操作，如下图所示：

![1665978296_634ccfb8406808adc3df5.png!small?1665978297950](https://image.3001.net/images/20221017/1665978296_634ccfb8406808adc3df5.png!small?1665978297950)

test3

通过对比可以看出

在语义准确性上，Incinerator、JEB仍然保持了语义的准确性，GDA重复声明了a、y变量，并且继续丢失函数内部的代码块。

在代码可读性上，Incinerator、JEB保持很好的代码可读性，JEB使用了continue来分割嵌套的if。

在代码还原度上，Incinerator最为接近源码，JEB改为使用continue来分割嵌套的if。

| 反编译器 | 语义准确性 | 代码可读性 | 代码还原度 |
| --- | --- | --- | --- |
| Incinerator | ✓ | 高 | 高 |
| JEB | ✓ | 高 | 高 |
| GDA | × | 低 | 低 |

### Test4

在内层循环的第一个if-else结构上添加一个后随节点，并且最后break出内层循环到外层循环。并且将a=a\*5语句后的break改成continue。代码如下：

```
public void test4(int y, int a) {
        while(y > 0) {
            y++;
            while(a > 50) {
                a = a + 1;
                y = y + 1;
                if(a > 10) {
                    if(a > 100) {
                        a = a * 5;
                        continue;
                    } else {
                        y = y / a;
                    }
                }
                y = a * y;
                break;
            }
            this.attachBaseContext(this);
        }
    }
```

同样编译成apk后再反编译，如下图所示：

![1665978304_634ccfc065f243a22562d.png!small?1665978306137](https://image.3001.net/images/20221017/1665978304_634ccfc065f243a22562d.png!small?1665978306137)

test4

通过上述对比可以看出

在语义准确性上，Incinerator在a \*= 5; 后面丢失了continue，在y \*= a; 后面丢失了退出循环的break；JEB保持了语义的正确性；GDA重复声明变量，也丢失了函数内的代码块。

在代码可读性上，Incinerator、JEB可读性都很好。

在代码还原度上，Incinerator与源码最为相似，但是丢失了continue、break；JEB使用continue分开了if-else，将else后面的y /= a，与y \*= a合并为新的 y = y / a \* a，并加入break，还原度上有了一定的改变。

| 反编译器 | 语义准确性 | 代码可读性 | 代码还原度 |
| --- | --- | --- | --- |
| Incinerator | × | 高 | 中 |
| JEB | ✓ | 高 | 中 |
| GDA | × | 低 | 低 |

### Test5

这次在“if(a>10)”内部加入switch，在a为11、12时，执行“a = a \* 5”，并continue返回内循环while，a为13时，执行“a = a \* 6”，继续往下执行，并不退出，a为14时，执行“a = a \* 7” 退出switch， 与default中加入if-else，代码如下：

```
public void test5(int y, int a) {
        while(y > 0) {
            y++;
            while(a > 50) {
                a = a + 1;
                y = y + 1;
                if(a > 10) {
                    switch(a) {
                        case 11:
                        case 12:
                            a = a * 5;
                            continue;
                        case 13:
                            a = a * 6;
                        case 14:
                            a = a * 7;
                            break;
                        default:
                            if(a > 100) {
                                a = a * 5;
                                continue;
                            } else {
                                y = y / a;
                            }
                    }
                }
                y = a * y;
                break;
            }
            this.attachBaseContext(this);
        }
    }
```

最后编译成apk后反编译，如下图所示：

![1665978351_634ccfef0610ab844ca1d.png!small?1665978352757](https://image.3001.net/images/20221017/1665978351_634ccfef0610ab844ca1d.png!small?1665978352757)

test5

通过上述对比可以看出

在语义准确性上，Incinerator在switch将a为11、12、default中的continue错误表达为break，丢失了y \*= a后面退出内循环的break；JEB保持了语义的正确性在，但在label\_18的break之后，多了两句无用的代码a \*=8;continue；GDA没有识别出内循环，使用if与goto做处理，switch中a为11、12时多了break，没有识别出a=14，且在default中，执行完y=y/a后继续执行"a = a \* 7"。

在代码可读性上，Incinerator识别出双循环、switch-case可读性上最好，JEB、GDA多次出现goto，在代码可读性上存在一定的影响。

在代码还原度上，Incinerator与源码最为相似，但在节点的退出上存在一定的问题，JEB、GDA在代码的还原度上膨胀比较大。

| 反编译器 | 语义准确性 | 代码可读性 | 代码还原度 |
| --- | --- | --- | --- |
| Incinerator | × | 高 | 中 |
| JEB | ✓ | 中 | 中 |
| GDA | × | 中 | 低 |

## 调试能力测试

逆向工程工具针对Apk可调试，对于研究人员来说有着极大的帮助，而对于已经发布后的应用再进行调试的话，可调试的前提条件会比较苛刻，如：设备是否root、调试属性是否开启、能否重打包等，这些因素都会影响着是否能够调试，而影响调试功能的好坏、支持与否，取决于：能否stepover、stepinto、breakpoint，能否获取/修改变量值等，这些因素都体现着调试器是否好用。所以我们从上述多个维度，对Incinerator、JEB的调试做下简单对比，但因GDA不支持调试，所以下面的内容无法针对GDA进行测试对比。

这里直接使用Android Studio自带的example：Login Activity进行对比，如图1-2所示：

![1665978376_634cd00894898303330f8.png!small?1665978378243](https://image.3001.net/images/20221017/1665978376_634cd00894898303330f8.png!small?1665978378243)...