---
title: 词法分析 | DFA 的最小化
url: https://www.o2oxy.cn/4290.html
source: print("")
date: 2024-12-16
fetch_date: 2025-10-06T19:36:26.244077
---

# 词法分析 | DFA 的最小化

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

# 词法分析 | DFA 的最小化

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-15 14:34
阅读次数: 1,193 次

还是已获得的a(b|c)\* 为例子

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-3.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-3.png)

已经获取到了这样一个的DFA的。这样的一个DFA可以通过Hopcroft 算法得到更为简单的一个DFA

Hopcroft 算法初始化N 和A

A 代表是终态集合 就是接受集合

N 代表非终态集合 没有接受的集合

画个图可以更好的理解

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/最小化.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E6%9C%80%E5%B0%8F%E5%8C%96.drawio.png)

使用切分集合的方式进行最小化。例如上图的N 里面只有一个元素了。就没有办法分割了。

那么就可以分割A

那么A通过怎么样子的进行分割呢？

通过等价类是否一致的话。进行分割。如图

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/最小化.drawio-1.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E6%9C%80%E5%B0%8F%E5%8C%96.drawio-1.png)

因为q1 q2 q3 都是到了一个q4 等价类那么就可以合并成一个q5 如下：

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/合并.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%90%88%E5%B9%B6.drawio.png)

如果q1 q2 q3 指向不一样的情况下怎么分割呢？例如下图

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/aaaa.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/aaaa.drawio.png)

这里q3 输入d 指向了q4 那么就变成了如下

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/A的分割.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/A%E7%9A%84%E5%88%86%E5%89%B2.drawio.png)

例子2 :f(ee|ie)

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/合并.drawio-3.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%90%88%E5%B9%B6.drawio-3.png)

N : {q0, q1, q2, q4}

A : {q3, q5}

在 N 中 q0 和 q1 在接受 e 的条件下最终得到的状态还是在 N 的内部。所以可以将其根据 e 拆分成 {q0, q1}, {q2, q4}, {q3, q5}

对于 q2 和 q4 都可以接受 e ，而且最终达到的状态一致，所以不能再进行切分。

q0 和 q1 ，在接受 e 的时候， q0 最终得到还是在 {q0, q1}这个状态的结合中， q1 却会落在 {q2, q4} 的状态中，所以可以将 q0 和 q1 分为 {q0}, {q1}。

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/合并.drawio-4.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%90%88%E5%B9%B6.drawio-4.png)

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4290.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [Laravel 6.x/7.x的一条执行代码的反序列化利用链](https://www.o2oxy.cn/3588.html "Laravel 6.x/7.x的一条执行代码的反序列化利用链")
* [GitLab Graphql邮箱信息泄露漏洞 CVE-2020-26413](https://www.o2oxy.cn/3568.html "GitLab Graphql邮箱信息泄露漏洞 CVE-2020-26413")
* [Nginx\_lua 100参数绕过原理详解](https://www.o2oxy.cn/3303.html "Nginx_lua 100参数绕过原理详解")
* [fastjson1.2.24 漏洞分析](https://www.o2oxy.cn/3993.html "fastjson1.2.24 漏洞分析")
* [分享一个过狗过D盾的小马(过宝塔WAF)](https://www.o2oxy.cn/1483.html "分享一个过狗过D盾的小马(过宝塔WAF)")
* [用友NC6.5 复现](https://www.o2oxy.cn/3557.html "用友NC6.5 复现")
* [蓝盾CTF 第二场 WP](https://www.o2oxy.cn/1080.html "蓝盾CTF 第二场 WP")
* [Ubuntu16.04 的0day webshell 版本复现](https://www.o2oxy.cn/415.html "Ubuntu16.04 的0day webshell 版本复现")
* [通过宝塔面板搭建dns\_log 平台](https://www.o2oxy.cn/2250.html "通过宝塔面板搭建dns_log 平台")
* [cobaltstrike keytool store 证书转换成nginx 所需证书](https://www.o2oxy.cn/3690.html "cobaltstrike keytool  store 证书转换成nginx 所需证书")

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