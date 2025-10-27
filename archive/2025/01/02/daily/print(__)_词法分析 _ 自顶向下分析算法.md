---
title: 词法分析 | 自顶向下分析算法
url: https://www.o2oxy.cn/4334.html
source: print("")
date: 2025-01-02
fetch_date: 2025-10-06T20:08:42.903102
---

# 词法分析 | 自顶向下分析算法

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

# 词法分析 | 自顶向下分析算法

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2025-01-01 23:22
阅读次数: 5,727 次

首先我们给定文法G如下：

```
S -> N V N
N -> s
   | t
   | g
   | w
V -> e
   | d
```

需要推导出句子s如下：
g d w

使用图演示一下具体的过程

[![](https://www.o2oxy.cn/wp-content/uploads/2025/01/自下.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2025/01/%E8%87%AA%E4%B8%8B.drawio.png)

使用一个脚本来演示类似的算法

```
class Parser:
    def __init__(self, grammar):
        self.grammar = grammar  # 文法规则，以字典形式存储

    def parse(self, sentence):
        stack = []  # 初始化栈
        productions = self.grammar['S']
        for production in productions:
            stack.append(production)
        index = 0
        tmp_n=0
        tmp_v=0
        index2=0
        access_list=[]
        while stack:
            if index2>=len(stack):
                index2=int(len(stack)-1)
                if index2<0:index2=0
            top = stack[index2]
            del stack[index2]
            if top in self.grammar:  # 非终结符
                if top=='N':
                    stack.insert(index,self.grammar[top][tmp_n])
                    tmp_n+=1
                if top=='V':
                    stack.insert(index,self.grammar[top][tmp_v])
                    tmp_v+=1
            else:
                if top!=sentence[index]:
                    stack.insert(index,self.grammar['S'][index])
                else:
                    access_list.append(top)
                    tmp_n=0
                    tmp_v=0
                    index+=1
                    index2+=1
            #break
        return "".join(access_list) == "".join(sentence)  # 所有符号匹配成功

# 定义文法
grammar = {
    'S': ['N','V', 'N'],
    'N': ['s', 't', 'g', 'w'],
    'V': ['e', 'd']
}

parser = Parser(grammar)
sentence = ['g','d','w']

print(sentence[0])
if parser.parse(sentence):
    print("句子", sentence, "符合文法")
else:
    print("句子", sentence, "不符合文法")
```

上述自上而下的方式太过于消耗性能，可以改为如下的方式

[![](https://www.o2oxy.cn/wp-content/uploads/2025/01/自下-的副本.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2025/01/%E8%87%AA%E4%B8%8B-%E7%9A%84%E5%89%AF%E6%9C%AC.drawio.png)

例子如下：

```
class Parser:
    def __init__(self, grammar):
        self.grammar = grammar  # 文法规则，以字典形式存储

    def parse(self, sentence):
        stack = []  # 初始化栈
        productions = self.grammar['S']
        for production in productions:
            stack.append(production)
        index = 0
        access_list=[]
        while stack:
            top = stack.pop()
            if top in self.grammar:  # 非终结符
                flag=False
                for i2 in self.grammar[top]:
                    if i2 == sentence[index]:
                        index+=1
                        access_list.append(i2)
                        flag=True
                if not flag:
                    return False

        print(access_list)
        return "".join(access_list) == "".join(sentence)  # 所有符号匹配成功

# 定义文法
grammar = {
    'S': ['N','V', 'N'],
    'N': ['s', 't', 'g', 'w'],
    'V': ['e', 'd']
}

parser = Parser(grammar)
sentence = ['g','d','w']

if parser.parse(sentence):
    print("句子", sentence, "符合文法")
else:
    print("句子", sentence, "不符合文法")
```

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4334.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [coremail poc](https://www.o2oxy.cn/2287.html "coremail poc")
* [Linux 抓取密码](https://www.o2oxy.cn/3771.html "Linux 抓取密码")
* [湖湘杯WEB题解](https://www.o2oxy.cn/2018.html "湖湘杯WEB题解")
* [Nginx\_lua 100参数绕过原理详解](https://www.o2oxy.cn/3303.html "Nginx_lua 100参数绕过原理详解")
* [docker代理配置 pull 加速](https://www.o2oxy.cn/3011.html "docker代理配置 pull 加速")
* [HTTP2.0 拦截爬虫的tips](https://www.o2oxy.cn/3518.html "HTTP2.0  拦截爬虫的tips")
* [Hprose for php 初探](https://www.o2oxy.cn/3511.html "Hprose for php 初探")
* [通过宝塔面板搭建dns\_log 平台](https://www.o2oxy.cn/2250.html "通过宝塔面板搭建dns_log 平台")
* [宝塔面板数据从系统盘迁移到数据盘](https://www.o2oxy.cn/1375.html "宝塔面板数据从系统盘迁移到数据盘")
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