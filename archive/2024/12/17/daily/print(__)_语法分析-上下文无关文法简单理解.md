---
title: 语法分析-上下文无关文法简单理解
url: https://www.o2oxy.cn/4312.html
source: print("")
date: 2024-12-17
fetch_date: 2025-10-06T19:39:50.159226
---

# 语法分析-上下文无关文法简单理解

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# 语法分析-上下文无关文法简单理解

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-16 21:28
阅读次数: 1,440 次

一个上下文无关文法包括：

一个字符集、一个变元集合以及一个产生式集合，并且变元集合中有一个变元被称为初始变元。

所谓产生式就是 S→aSb 这样的，由一个变元变成变元和字符组成的串的式子。

举个例子:

```
自然语言中的句子的典型结构
主语 谓语 宾语
名词 动词 名词
例子：
名词：{羊， 老虎， 草， 水}
动词：{吃， 喝}
句子：
羊 吃 草
羊 喝 水
老虎 吃 老虎
草 吃 老虎
```

那么也可以套用如上的。

对这个例子，我们进行形式化分析：

（S 表示句子， -> 表示推出， N 表示名词， V 表示动词）

```
S -> N V N
N -> s(sheep)
   | t(tiger)
   | g(grass)
   | w(water)
V -> e(eat)
   | d(drink)
```

我们将其中的大写符号叫做非终结符：{S, N, V}

将小写的符号（名词+谓词）叫做终结符：{s, t, g, w, e, d}

开始符号是：S

## 上下文无关文法

上下文无关文法 G 是一个四元组：

G = (T, N, P, S)

```
其中 T 是终结符集合
N 是非终结符集合
P 是一组产生式规则
每条规则的形式： X -> β1 β2 ... βn, n >= 0
其中 X ∈ N, βi ∈（T ∪ N）
S 是唯一的开始符号（非终结符）
S ∈ N
```

```
G = {N, T, P, S}
非终结符号：N = {S, N, V}
终结符号： T = {s, t, g, w, e, d}
开始符号：S
产生式规则集合：
{ S -> N V N,
N -> s,
N -> t,
N -> g,
N -> w,
V -> e,
V -> d}
```

那么可以使用代码来演示一下

```
grammar = {
    'S': ['N', 'V', 'N'],
    'N': ['s', 't', 'g', 'w'],
    'V': ['e', 'd']
}

# 文法推导函数
def derive(symbol, input_string):
    if symbol not in grammar:
        return False
    #推导函数
    count=0
    for production in grammar[symbol]:
        #从左到右推导  第一位是N
        if production not in grammar:
            continue
        #判断是否在文法中
        if input_string[count] in grammar[production]:
            count+=1
    return count == len(input_string)

#随机生成文法
def run_derive(symbol):
    ret=""
    if symbol not in grammar:
        return ''
    #读取文法规则
    for production in grammar[symbol]:
        if production in grammar:
            name=grammar[production]
            #随机长度

# 使用推导函数
input_string = "set"
print(derive('S', input_string))
```

教程地址：<https://www.bilibili.com/video/BV1m7411d7iS>

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4312.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [CVE-2021-21978：VM View Planner RCE 漏洞复现](https://www.o2oxy.cn/3213.html "CVE-2021-21978：VM View Planner RCE 漏洞复现")
* [Java 基础-傻傻分不清楚的文件操作类](https://www.o2oxy.cn/3077.html "Java 基础-傻傻分不清楚的文件操作类")
* [Centos7 sudo 提权脚本](https://www.o2oxy.cn/3736.html "Centos7 sudo 提权脚本")
* [宝塔面板数据从系统盘迁移到数据盘](https://www.o2oxy.cn/1375.html "宝塔面板数据从系统盘迁移到数据盘")
* [密码保护：钉钉V6.3.5 and 向日葵11.0 RCE 复现](https://www.o2oxy.cn/4013.html "密码保护：钉钉V6.3.5  and  向日葵11.0  RCE 复现")
* [Spring Boot Actuator H2 RCE复现](https://www.o2oxy.cn/2656.html "Spring Boot Actuator H2 RCE复现")
* [ThinkPHP5 远程代码执行高危漏洞](https://www.o2oxy.cn/2046.html "ThinkPHP5 远程代码执行高危漏洞")
* [ThinkCMF RCE](https://www.o2oxy.cn/2562.html "ThinkCMF  RCE")
* [蓝盾CTF 第二场 WP](https://www.o2oxy.cn/1080.html "蓝盾CTF 第二场 WP")
* [python3 爬补天公益src 厂商名称和url](https://www.o2oxy.cn/1165.html "python3 爬补天公益src 厂商名称和url")

标签云

[Apache2.4.50](https://www.o2oxy.cn/tag/apache2-4-50)
[Apache ShenYu](https://www.o2oxy.cn/tag/apache-shenyu)
[APISIX](https://www.o2oxy.cn/tag/apisix)
[APISIX Dashboard](https://www.o2oxy.cn/tag/apisix-dashboard)
[cc5](https://www.o2oxy.cn/tag/cc5)
[CNVD-2021-49104](https://www.o2oxy.cn/tag/cnvd-2021-49104)
[CNVD-2022-60632](https://www.o2oxy.cn/tag/cnvd-2022-60632)
[CobaltStrike](https://www.o2oxy.cn/tag/cobaltstrike)
[CobaltStrike xss](https://www.o2oxy.cn/tag/cobaltstrike-xss)
[CommonsCollections5](https://www.o2oxy.cn/tag/commonscollections5)
[Confluence CVE-2021-26084](https://www.o2oxy.cn/tag/confluence-cve-2021-26084)
[CVE-2017-18349](https://www.o2oxy.cn/tag/cve-2017-18349)
[CVE-2021-4034](https://www.o2oxy.cn/tag/cve-2021-4034)
[CVE-2021-37580](https://www.o2oxy.cn/tag/cve-2021-37580)
[CVE-2021-41277](https://www.o2oxy.cn/tag/cve-2021-41277)
[CVE-2021-41773](https://www.o2oxy.cn/tag/cve-2021-41773)
[cve-2021-42013](https://www.o2oxy.cn/tag/cve-2021-42013)
[CVE-2021-43798](https://www.o2oxy.cn/tag/cve-2021-43798)
[CVE-2021-44228](https://www.o2oxy.cn/tag/cve-2021-44228)
[CVE-2021-45232](https://www.o2oxy.cn/tag/cve-2021-45232)
[CVE-2021-45232 RCE](https://www.o2oxy.cn/tag/cve-2021-45232-rce)
[CVE-2022-22954](https://www.o2oxy.cn/tag/cve-2022-22954)
[CVE-2022-22965](https://www.o2oxy.cn/tag/cve-2022-22965)
[CVE-2022-39197](https://www.o2oxy.cn/tag/cve-2022-39197)
[CVE-2023-28432](https://www.o2oxy.cn/tag/cve-2023-28432)
[Django](https://www.o2oxy.cn/tag/django)
[E-Office](https://www.o2oxy.cn/tag/e-office)
[grafana](https://www.o2oxy.cn/tag/grafana)
[keytool store](https://www.o2oxy.cn/tag/keytool-store)
[log4j2](https://www.o2oxy.cn/tag/log4j2)
[MetaBase](https://www.o2oxy.cn/tag/metabase)
[ONE Access](https://www.o2oxy.cn/tag/one-access)
[python](https://www.o2oxy.cn/tag/python)
[python爬虫](https://www.o2oxy.cn/tag/python%E7%88%AC%E8%99%AB)
[socks5](https://www.o2oxy.cn/tag/socks5)
[socks5搜索](https://www.o2oxy.cn/tag/socks5%E6%90%9C%E7%B4%A2)
[store 证书转换成nginx](https://www.o2oxy.cn/tag/store-%E8%AF%81%E4%B9%A6%E8%BD%AC%E6%8D%A2%E6%88%90nginx)
[VMware Workspace ONE Access](https://www.o2oxy.cn/tag/vmware-workspace-one-access)
[ysoserial](https://www.o2oxy.cn/tag/ysoserial)
[代理池工具](https://www.o2oxy.cn/tag/%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7)
[宝塔面板](https://www.o2oxy.cn/tag/%E5%AE%9D%E5%A1%94%E9%9D%A2%E6%9D%BF)
[泛微](https://www.o2oxy.cn/tag/%E6%B3%9B%E5%BE%AE)
[畅捷通](https://www.o2oxy.cn/tag/%E7%95%85%E6%8D%B7%E9%80%9A)
[畅捷通漏洞](https://www.o2oxy.cn/tag/%E7%95%85%E6%8D%B7%E9%80%9A%E6%BC%8F%E6%B4%9E)
[通达OA](https://www.o2oxy.cn/tag/%E9%80%9A%E8%BE%BEoa)

×

#### 打赏支持

![print](http://www.o2oxy.cn/wp-content/uploads/2018/09/zhi.jpg)![print微信钱包](http://www.o2oxy.cn/wp-content/uploads/2018/09/wei.jpg)

扫描二维码，输入您要打赏的金额

2017-2099 **print("")**

赣ICP备16012687号-2