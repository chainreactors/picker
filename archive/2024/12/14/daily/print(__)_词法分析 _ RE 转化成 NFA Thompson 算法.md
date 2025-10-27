---
title: 词法分析 | RE 转化成 NFA Thompson 算法
url: https://www.o2oxy.cn/4273.html
source: print("")
date: 2024-12-14
fetch_date: 2025-10-06T19:38:19.396311
---

# 词法分析 | RE 转化成 NFA Thompson 算法

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

# 词法分析 | RE 转化成 NFA Thompson 算法

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2024-12-14 00:03
阅读次数: 946 次

## Thompson 算法

```
基于对 RE 的结构做归纳
对基本的 RE 直接构造
对复合的 RE 递归构造
```

如图。举例出5种方式

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/Thompson-.drawio.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/Thompson-.drawio.png)

如a(b|c)\*  这样的怎么构造呢？

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-1.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/NFA.drawio-1.png)

(b|c)\*ad

[![](https://www.o2oxy.cn/wp-content/uploads/2024/12/Re_NFA.drawio-2.png)](https://www.o2oxy.cn/wp-content/uploads/2024/12/Re_NFA.drawio-2.png)

使用代码实现a(b|c)\*   实现

```
#状态类
class State:
    def __init__(self, is_accepting=False):
        #接受状态
        self.is_accepting = is_accepting
        self.transitions = {}

    def add_transition(self, input_symbol, target_state):
        self.transitions[input_symbol] = target_state

    def __str__(self):
        return f"State {id(self)}: Accepting={self.is_accepting}"

class NFA:
    def __init__(self):
        self.states = []
        self.start_state = None
        self.accept_states = []

    def add_state(self, state):
        self.states.append(state)

    def set_start_state(self, state):
        self.start_state = state

    def set_accept_state(self, state):
        self.accept_states.append(state)

    def add_epsilon_transition(self, from_state, to_state):
        from_state.add_transition(None, to_state)

    def add_symbol_transition(self, from_state, input_symbol, to_state):
        from_state.add_transition(input_symbol, to_state)

    def __str__(self):
        return "\n".join(str(state) for state in self.states)

    def accepts(self, input_string):
        current_states = [self.start_state]
        for char in input_string:
            new_states = []
            for state in current_states:
                for symbol, target_state in state.transitions.items():
                    if symbol is None or symbol == char:
                        new_states.append(target_state)
            if not new_states:
                return False
            current_states = new_states
        return any(state.is_accepting for state in current_states)

# 创建NFA
nfa = NFA()

# 创建状态
state0 = State()
state1 = State(is_accepting=True)

# 添加状态到NFA
nfa.add_state(state0)
nfa.add_state(state1)

# 设置开始和接受状态
nfa.set_start_state(state0)
nfa.set_accept_state(state1)

# 添加转换
nfa.add_symbol_transition(state0, 'a', state1)  # a -> state1
nfa.add_symbol_transition(state1, 'b', state1)  # b -> state1
nfa.add_symbol_transition(state1, 'c', state1)  # c -> state1
nfa.add_epsilon_transition(state1, state1)     # ε -> state1

# 测试NFA
input_string = "abbbbbb"
if nfa.accepts(input_string):
    print(f"The NFA accepts the input string '{input_string}'")
else:
    print(f"The NFA does not accept the input string '{input_string}'")
```

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4273.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [phpweb 前台任意文件上传漏洞复现和分析](https://www.o2oxy.cn/2582.html "phpweb 前台任意文件上传漏洞复现和分析")
* [Cobalt Strike使用](https://www.o2oxy.cn/2361.html "Cobalt Strike使用")
* [CVE-2019-16278](https://www.o2oxy.cn/2538.html "CVE-2019-16278")
* [Flask debug模式下的 PIN 码安全性](https://www.o2oxy.cn/2728.html "Flask debug模式下的 PIN 码安全性")
* [django ORM 多对多的主机管理](https://www.o2oxy.cn/1582.html "django ORM 多对多的主机管理")
* [PHP 7.1-7.3 disable\_functions bypass](https://www.o2oxy.cn/2479.html "PHP 7.1-7.3 disable_functions bypass")
* [Spring Boot Actuator H2 RCE复现](https://www.o2oxy.cn/2656.html "Spring Boot Actuator H2 RCE复现")
* [苹果CMS V8 绕过前台RCE](https://www.o2oxy.cn/2578.html "苹果CMS V8 绕过前台RCE")
* [记一次目录遍历到后台](https://www.o2oxy.cn/2676.html "记一次目录遍历到后台")
* [CNVD-C-2019-48814 复现](https://www.o2oxy.cn/2204.html "CNVD-C-2019-48814 复现")

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