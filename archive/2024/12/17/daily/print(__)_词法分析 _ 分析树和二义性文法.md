---
title: 词法分析 | 分析树和二义性文法
url: https://www.o2oxy.cn/4320.html
source: print("")
date: 2024-12-17
fetch_date: 2025-10-06T19:39:49.697269
---

# 词法分析 | 分析树和二义性文法

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

# 词法分析 | 分析树和二义性文法

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-16 22:57
阅读次数: 1,421 次

### 分析树

1、推导可以表达成树状的形状结构 （和推导的顺序无关）

2、特点

    一、树中的每个内部节点代表非终结符

    二、每个叶子节点代表终结符

    三、每一步推导代表如何从双亲节点生成它的直接孩子节点。

例子1

如果G为

```
E--> num
E--> id
E--> E+E
E--> E*E
```

推导出5+6\*7 为如下图

### 第一种推导方式

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/分析书.drawio-1.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%88%86%E6%9E%90%E4%B9%A6.drawio-1.png)

### 第二种推导方式

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/二.drawio-1.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E4%BA%8C.drawio-1.png)

他们的结果完全不相同。

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/三.drawio-1.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E4%B8%89.drawio-1.png)

这就导致了二义性的产生。正确的应该是第一种的方式。

那么基于存在二义性的问题。可以通过三种解决方案：

###

### 二义性的消除

```
1、将二义文法改成非二义文法；
2、规定二义文法中符号的优先级和结合性；
3、改变语言的结构或书写方式。
```

### 使用第一种方法

需要引入新的终结符，且新引入的非终结符

```
E -> E + T
   | T
T -> T * F
   | F
F -> num
   | id
```

5+6\*7的推导过程

```
 E -> E + T
   -> T + T
   -> F + T
   -> 5 + T
   -> 5 + T * F
   -> 5 + F * F
   -> 5 + 6 * F
   -> 5 + 6 * 7
```

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/四.drawio-1.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%9B%9B.drawio-1.png)

### 使用第二种方法

引入优先级的

```
E -> T | E + T | E - T
T -> num | T * num | T / num
```

这样的一个推导过程

```
E -> T
E -> E + T
E -> T + T
T -> T * num
T -> num * num
E -> 5 + T
E -> 5 + T * F
E -> 5 + F * F
E -> 5 + 6 * F
E -> 5 + 6 * 7
```

还有更多的方式可以参考如下的链接

<https://www.jianshu.com/p/2d55d50f8bc4>

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4320.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [PHP CGI Windows平台远程代码执行漏洞（CVE-2024-4577）复现](https://www.o2oxy.cn/4199.html "PHP CGI Windows平台远程代码执行漏洞（CVE-2024-4577）复现")
* [宝塔面板数据从系统盘迁移到数据盘](https://www.o2oxy.cn/1375.html "宝塔面板数据从系统盘迁移到数据盘")
* [SonicWall SSL-VPN 未授权RCE漏洞 复现](https://www.o2oxy.cn/3032.html "SonicWall SSL-VPN 未授权RCE漏洞 复现")
* [密码保护：新思路多句话过D盾、安全狗、阿里云等WAF 思路延长](https://www.o2oxy.cn/2224.html "密码保护：新思路多句话过D盾、安全狗、阿里云等WAF 思路延长")
* [致远OA 任意文件上传](https://www.o2oxy.cn/2891.html "致远OA 任意文件上传")
* [django 中间件 缓存 信号](https://www.o2oxy.cn/1627.html "django 中间件 缓存  信号")
* [密码保护：由xss 引发的一场钓鱼之旅](https://www.o2oxy.cn/1854.html "密码保护：由xss 引发的一场钓鱼之旅")
* [网鼎杯第三场wp](https://www.o2oxy.cn/1753.html "网鼎杯第三场wp")
* [蓝盾CTF 第二场 WP](https://www.o2oxy.cn/1080.html "蓝盾CTF 第二场 WP")
* [CVE-2020-11651 SaltStack漏洞复现](https://www.o2oxy.cn/2642.html "CVE-2020-11651 SaltStack漏洞复现")

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