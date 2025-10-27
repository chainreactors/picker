---
title: NFA转换为DFA 构造子集算法
url: https://www.o2oxy.cn/4285.html
source: print("")
date: 2024-12-15
fetch_date: 2025-10-06T19:37:29.200049
---

# NFA转换为DFA 构造子集算法

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

# NFA转换为DFA 构造子集算法

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-14 20:36
阅读次数: 1,216 次

如果需要将NFA转为DFA 需要如下几个步骤

1、消除ε-跃迁

2.在单个输入字符上从一个状态进行多次转换。

##### NFA状态的操作

| 操作 | 说明 |
| --- | --- |
|  |  |
| --- | --- |
| ε-closrue(s) | 仅在ε-跃迁上从NFA状态s可到达的NFA状态集。 |
| ε-closrue(T) | 仅在ε-跃迁上从T中的一些NFA状态可到达的NFA状态集。 |
| Move(T,a) | 输入符号a从T中的某些NFA状态转换到的NFA状态集合。 |

首先使用NFA  a(b|c)\* 为例子

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-2.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-2.png)

从n0开始，我们需要输入一个a之后能不消耗任何输入的情况下移动到哪里

这形成了一个新状态：n1, n2, n3, n4, n6,n7,n8, n9

可以组合成如下的子集

q1= {n1, n2, n3, n4, n6, n9}

q2 = {n5, n8, n9, n3, n4, n6}

q3 = {n7, n8, n9, n3, n4, n6}

DFA的转换表Dtran

|  |  |  |  |
| --- | --- | --- | --- |
| Dstates | a | b | c |
| q0 | q1 |  |  |
| q1 |  | q2 | q3 |
| q2 |  | q2 | q3 |
| q3 |  | q2 | q3 |

如图

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-3.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-3.png)

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4285.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [词法分析 | DFA 的最小化](https://www.o2oxy.cn/4290.html "词法分析 | DFA 的最小化")
* [Apache2.4 模块开发初探](https://www.o2oxy.cn/3417.html "Apache2.4 模块开发初探")
* [Apache CVE-2021-40438](https://www.o2oxy.cn/3750.html "Apache CVE-2021-40438")
* [Spring Cloud Function 漏洞复现](https://www.o2oxy.cn/4029.html "Spring Cloud Function 漏洞复现")
* [qqqq](https://www.o2oxy.cn/2113.html "qqqq")
* [常用java 利用工具](https://www.o2oxy.cn/2909.html "常用java 利用工具")
* [CVE-2021-26855 Exchange Server RCE 复现](https://www.o2oxy.cn/3169.html "CVE-2021-26855 Exchange Server  RCE 复现")
* [Centos7 搭建openstack ocata 版](https://www.o2oxy.cn/917.html "Centos7 搭建openstack  ocata 版")
* [Yapi远程命令执行漏洞复现](https://www.o2oxy.cn/3611.html "Yapi远程命令执行漏洞复现")
* [Bugku welcome to bugkuctf 引发的思考](https://www.o2oxy.cn/1877.html "Bugku welcome to bugkuctf 引发的思考")

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