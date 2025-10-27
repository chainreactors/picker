---
title: 编译原理 – DFA 简单实现
url: https://www.o2oxy.cn/4268.html
source: print("")
date: 2024-12-14
fetch_date: 2025-10-06T19:38:20.442574
---

# 编译原理 – DFA 简单实现

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

# 编译原理 – DFA 简单实现

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-13 22:22
阅读次数: 946 次

DFA 确定状态有限自动机

NFA 非确定状态有限自动机

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241213222053.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241213222053.jpg)

目标实现如下的简单DFA的实现

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/微信截图_20241213222157.jpg)](https://www.o2oxy.cn/wp-content/uploads/2024/12/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20241213222157.jpg)

代码如下：

```
'''
    DFA 的实现
    -->0 --a-->1 --a--> [2]
       b       b        a,b

表如下
---------------------------------
|状态\字符| a       |  b        |
--------------------------------
|0        | 1       |0          |
---------------------------------
|1        | 2       |1          |
---------------------------------
|2        | 2       |2          |
---------------------------------
'''
class DFA:
    def __init__(self):
        self.dfa={
            "0":{
                "a":"1",
                "b":"0"
            },
            "1":{
                "a":"2",
                "b":"1"
            },
            "2":{
                "a":"2",
                "b":"2"
            }
        }
        #接受的状态是
        self.accept_status=["a","b"]

        #当前状态
        self.start="0"

        self.accept="2"

    #读取状态转移到另外的状态
    def read(self,str):
        if str in self.dfa[self.start]:
            self.start=self.dfa[self.start][str]

    def is_accept(self):
        return self.start ==self.accept

def start_dfa(strs):
    dfa=DFA()
    for str in strs:
        dfa.read(str)
    return dfa.is_accept()

print(start_dfa("bbbbbbabca"))
```

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4268.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [jumpserver远程代码执行漏洞分析](https://www.o2oxy.cn/2963.html "jumpserver远程代码执行漏洞分析")
* [Centos7 sudo 提权脚本](https://www.o2oxy.cn/3736.html "Centos7 sudo 提权脚本")
* [CVE-2024-2961 glibc API Bug 利用](https://www.o2oxy.cn/4193.html "CVE-2024-2961 glibc API Bug 利用")
* [无eval 木马免杀人免杀D盾](https://www.o2oxy.cn/2716.html "无eval 木马免杀人免杀D盾")
* [一个好看的404页面](https://www.o2oxy.cn/1365.html "一个好看的404页面")
* [cobaltstrike keytool store 证书转换成nginx 所需证书](https://www.o2oxy.cn/3690.html "cobaltstrike keytool  store 证书转换成nginx 所需证书")
* [词法分析 |LL(1) 文法](https://www.o2oxy.cn/4342.html "词法分析 |LL(1) 文法")
* [openstack部署（Newton）](https://www.o2oxy.cn/297.html "openstack部署（Newton）")
* [CVE-2019-2725 绕过 复现](https://www.o2oxy.cn/2293.html "CVE-2019-2725 绕过 复现")
* [泛微OA前台GetShell 复现](https://www.o2oxy.cn/3508.html "泛微OA前台GetShell 复现")

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