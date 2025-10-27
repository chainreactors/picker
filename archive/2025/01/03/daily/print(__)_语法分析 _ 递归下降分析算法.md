---
title: 语法分析 | 递归下降分析算法
url: https://www.o2oxy.cn/4339.html
source: print("")
date: 2025-01-03
fetch_date: 2025-10-06T20:09:21.173712
---

# 语法分析 | 递归下降分析算法

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

# 词法分析 | 递归下降分析算法

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2025-01-02 21:37
阅读次数: 5,669 次

对于给定的文法G如下：

```
S -> N V N
N -> s
   | t
   | g
   | w
V -> e
   | d
```

可以简单的使用parse\_S  paser\_N parse\_V 这样的进行判断。例如：

```
class Parser:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.current_token = self.text[self.index]

    def match(self, token):
        if self.text[self.index]==token:
            self.index += 1
            return True

    def parse(self):
        return self.S()

    def S(self):
        if self.N():
            if self.V():
                if self.N():
                    return True
        return False

    def N(self):
        if self.match('s') or self.match('t') or self.match('g') or self.match('w'):
            return True
        return False

    def V(self):
        if self.match('e') or self.match('d'):
            return True
        return False

# 给定文法G
input_sentence = 'gds'

# 初始化解析器
p = Parser(input_sentence)

# 执行解析
if p.parse():
    print("句子 '{}' 可以被文法G正确解析。".format(input_sentence))
else:
    print("句子 '{}' 不能被文法G解析。".format(input_sentence))
```

稍微复杂一点就是对算术的一个计算了

例如：

```
E -> E + T
   | T
T -> T * F
   | F
F -> num
```

实现的方式如下:

```
class Parser:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.current_token = text[self.index] if text else None

    def match(self, token):
        if self.current_token == token:
            self.current_token = self.text[self.index + 1] if self.index + 1 < len(self.text) else None
            self.index += 1
            return True
        return False

    def parse(self):
        return self.E()

    def E(self):
        if self.T():
            while self.match('+') and self.T():
                pass
            return True
        return False

    def T(self):
        if self.F():
            while self.match('*') and self.F():
                pass
            return True
        return False

    def F(self):
        if self.current_token and self.current_token.isdigit():
            self.current_token = self.text[self.index + 1] if self.index + 1 < len(self.text) else None
            self.index += 1
            return True
        return False

# 给定文法
input_sentence = "3+4*1+1"

# 初始化解析器
p = Parser(input_sentence)

# 执行解析
if p.parse() and p.index == len(input_sentence):
    print("句子 '{}' 可以被文法正确解析。".format(input_sentence))
else:
    print("句子 '{}' 不能被文法解析。".format(input_sentence))
```

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4339.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [Java Tomcat内存马—入门到入土](https://www.o2oxy.cn/3930.html "Java Tomcat内存马—入门到入土")
* [网鼎杯第二场wp](https://www.o2oxy.cn/1688.html "网鼎杯第二场wp")
* [通过代码执行临时修改Shiro密钥](https://www.o2oxy.cn/3972.html "通过代码执行临时修改Shiro密钥")
* [CVE-2020-3091 lanproxy 目录遍历](https://www.o2oxy.cn/2885.html "CVE-2020-3091 lanproxy 目录遍历")
* [密码保护：新思路多句话过D盾、安全狗、阿里云等WAF 思路延长](https://www.o2oxy.cn/2224.html "密码保护：新思路多句话过D盾、安全狗、阿里云等WAF 思路延长")
* [PHP CGI Windows平台远程代码执行漏洞（CVE-2024-4577）复现](https://www.o2oxy.cn/4199.html "PHP CGI Windows平台远程代码执行漏洞（CVE-2024-4577）复现")
* [手把手教你把代码丢入github 中](https://www.o2oxy.cn/503.html "手把手教你把代码丢入github 中")
* [Windows10 安装Tensorflow2.3.0-cpu 踩坑记](https://www.o2oxy.cn/2780.html "Windows10 安装Tensorflow2.3.0-cpu 踩坑记")
* [webbench 使用详解](https://www.o2oxy.cn/1075.html "webbench 使用详解")
* [vCenter CVE-2021-22005](https://www.o2oxy.cn/3773.html "vCenter CVE-2021-22005")

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