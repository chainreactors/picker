---
title: [系统安全] 六十一.恶意软件分析 (12)LLM赋能Lark工具提取XLM代码的抽象语法树（初探）
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTM5ODU2Mg==&mid=2247501228&idx=1&sn=b09f8443148d480c875e52d77103988a&chksm=cfcf7561f8b8fc774623011fade9c0218ad64e57b3768912d4159b85716e79823aa0097bc495&scene=58&subscene=0#rd
source: 娜璋AI安全之家
date: 2025-01-17
fetch_date: 2025-10-06T20:11:42.200630
---

# [系统安全] 六十一.恶意软件分析 (12)LLM赋能Lark工具提取XLM代码的抽象语法树（初探）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZsNHASe6DP3DiaSxN59buE8y027HTbbmqMDBz5SPQOxiam2Fh6TnNaFpg/0?wx_fmt=jpeg)

# [系统安全] 六十一.恶意软件分析 (12)LLM赋能Lark工具提取XLM代码的抽象语法树（初探）

原创

Eastmount

娜璋AI安全之家

> 2024年4月28日是Eastmount的安全星球 —— 『网络攻防和AI安全之家』正式创建和运营的日子，并且已坚持5个月每周7更。该星球目前主营业务为 安全零基础答疑、安全技术分享、AI安全技术分享、AI安全论文交流、威胁情报每日推送、网络攻防技术总结、系统安全技术实战、面试求职、安全考研考博、简历修改及润色、学术交流及答疑、人脉触达、认知提升等。下面是星球的新人券，欢迎新老博友和朋友加入，一起分享更多安全知识，比较良心的星球，非常适合初学者和换安全专业的读者学习。
>
> ”

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDROJ1RoIEHfImJuJ7kV607koyCt0jxRGu7e9Yic09B3CmrBZ70xVJicDHicAK2icfWRXL561kJvJCY9zPw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**感谢读者2024年对本公众号的支持。新的一年继续分享干货，共同进步，感恩同行 ^\_^**

该系列文章将系统整理和深入学习系统安全、逆向分析和恶意代码检测，文章会更加聚焦，更加系统，更加深入，也是作者的慢慢成长史。漫漫长征路，偏向虎山行。享受过程，一起奋斗~

**前文介绍了APT攻击检测溯源与常见APT组织的攻击案例。这篇文章将尝试探索利用大模型辅助恶意代码分析，即LLM赋能Lark工具提取XLM代码的抽象语法树。在恶意代码分析过程中，大家会遇到各种各样的问题，如何结合LLM和GPT完成复杂任务，更好地为安全工程师合作至关重要。基础性探索文章，还请各位大佬多多指教，写得不足的地方还请海涵。希望您喜欢，且看且珍惜。**

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZH4iaOqYlib2ibxec8kflB3YYk94wib1b3AowH3XyvA2oxtwyLJ7SdEsjog/640?wx_fmt=png&from=appmsg)

文章目录：

* **一.抽象语法树**
* **二.Lark解析器**

+ 1.简介
+ 2.安装

* **三.Lark提取XLM代码的抽象语法树**
* **四.LLM赋能的抽象语法树提取**

+ 1.单样本处理
+ 2.批量处理

* **五.总结**

作者的github资源：

* 逆向分析：

+ https://github.com/eastmountyxz/

  SystemSecurity-ReverseAnalysis

* 网络安全：

+ https://github.com/eastmountyxz/

  NetworkSecuritySelf-study

作者作为网络安全的小白，分享一些自学基础教程给大家，主要是关于安全工具和实践操作的在线笔记，希望您们喜欢。同时，更希望您能与我一起操作和进步，后续将深入学习网络安全和系统安全知识并分享相关实验。总之，希望该系列文章对博友有所帮助，写文不易，大神们不喜勿喷，谢谢！如果文章对您有帮助，将是我创作的最大动力，点赞、评论、私聊均可，一起加油喔！

![](https://mmbiz.qpic.cn/mmbiz_jpg/0RFmxdZEDROZ0FiaQhr7u82U6dJibrM3VO0dUcD3EMLylohBICfH8ibt9D8T7r2jcvDCAFuf4VR5IhcypN5mvCSVg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

> 声明：本人坚决反对利用教学方法进行犯罪的行为，一切犯罪行为必将受到严惩，绿色网络需要我们共同维护，更推荐大家了解它们背后的原理，更好地进行防护。（参考文献见后）

---

# 一.抽象语法树

抽象语法树（Abstract Syntax Tree, AST） 是一种树状数据结构，用于表示源代码的抽象语法结构。与具体语法树（Concrete Syntax Tree, CST）不同，AST 去除了与程序语言语法无关的细节（如分号或括号），仅保留代码的核心语义信息。AST 是编译器和解释器在分析源代码时的重要中间表示，广泛用于代码解析、优化、代码生成和静态分析等场景。树上的每个节点都表示源代码中的一种结构，所以说是抽象的，因为抽象语法树并不会表示真实语法的每一个细节。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZ5QjAko119XDOYxU4ElJw625wLUAha4m6QiaSvYPiaapiazNmicoh47O9BQ/640?wx_fmt=png&from=appmsg)

抽象语法树特性：

* 层次结构：AST 以树的形式组织，根节点表示程序的整体结构，子节点表示语句、表达式或其他语言构造。
* 抽象性：AST 省略了具体的语法细节，仅表示代码的逻辑结构。
* 语言无关性：尽管 AST 是为特定编程语言生成的，其结构可以通过特定规则跨语言映射。

抽象语法树在很多领域有广泛的应用，包括：

* 编译器设计
* 程序静态分析
* 自动化代码生成
* 代码语义优化
* 安全漏洞检测
* 恶意代码解析器
* 浏览器
* 智能编辑器

下面给出抽象语法树的简单示例。假设存在以下伪代码：

```
A1 = R12C34 + 5
```

抽象语法树表示：

```
start ├── assignment │    ├── cell (A1) │    ├── expression │         ├── cell (R12C34) │         ├── operator (+) │         ├── int (5)
```

根节点是 START，表示代码的起始点。ASSIGNMENT 是一个赋值操作，具有左值（CELL A1）和右值（一个表达式）。表达式由 CELL R12C34 和 INT 5 通过操作符 + 组成。通过AST，我们可以提取代码的语义结构，忽略具体的语法细节，如等号和空格，从而进行更深层次的代码分析。

---

# 二.Lark解析器

## 1.简介

Lark（鹂鸣）是一个Python实现的语法解析器，接受语法和文本，并生成表示该文本的抽象语法树。开源地址如下，推荐大家去Github学习：

* https://github.com/lark-parser/lark
* https://gitcode.com/gh\_mirrors/la/lark
* https://lark-parser.readthedocs.io/en/latest/json\_tutorial.html

> Lark is a parsing toolkit for Python, built with a focus on ergonomics, performance and modularity.
> Lark can parse all context-free languages. To put it simply, it means that it is capable of parsing almost any programming language out there, and to some degree most natural languages too.

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZI7FDLXYP8PhvLz5Xw8yMlEx2nvxWNiboKTrVANgD2gMib6zxSj4Rp4CQ/640?wx_fmt=png&from=appmsg)

Lark能做什么呢？

* Parse all context-free grammars, and handle any ambiguity gracefully
* Build an annotated parse-tree automagically, no construction code required.
* Provide first-rate performance in terms of both Big-O complexity and measured run-time (considering that this is Python 😉
* Run on every Python interpreter (it’s pure-python)
* Generate a stand-alone parser (for LALR(1) grammars)

Lark旨在构建解析器、编译器和解释器。它支持上下文无关语法的定义和高效解析，特别适合处理复杂的语言和抽象语法树 (AST) 的构建。Lark 在学术界和工业界广泛应用于自然语言处理、编译器设计、代码静态分析等领域。Lark的特性如下：

（1）支持上下文无关文法 (Context-Free Grammar)
Lark 支持完整的 BNF（巴科斯-诺尔范式）和 EBNF（扩展巴科斯-诺尔范式），允许用户定义灵活的语法规则。EBNF基本格式如下，terminal 是一个字符串或一个正则表达式。对于每条规则，解析器会通过顺序匹配它的所有项目，尝试每个备选方案。

```
rule_name : list of rules and TERMINALS to match          | another possible list of items          | etc.
TERMINAL: "some text to match"
```

例如，以下是一个简单的 EBNF 语法规则：

```
?start: expressionexpression: term (("+" | "-") term)*term: factor (("*" | "/") factor)*factor: NUMBER | "(" expression ")"%import common.NUMBER%import common.WS%ignore WS
```

（2）高效的解析器算法
Lark 默认使用 LALR(1) 算法解析上下文无关语言，具有高效性。此外，它还支持 Earley 算法，可以处理包含歧义的语法，适合解析自然语言。

（3）自动构建抽象语法树 (AST)
Lark 提供了一个可扩展的 Transformer 接口，用于简化 AST 的生成。用户可以直接定义树节点的转换规则，从而将解析结果转换为适合特定任务的数据结构。

（4）错误恢复和调试支持
Lark 提供了强大的语法错误处理和调试工具，使其成为教学和研究中演示解析器设计的理想选择。Lark擅长处理歧义问题。以下是解析短语"fruit flies like bananas"的结果：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZj1Kgx13K0175qNNiaRxnOHQKBISL83dQyfbPSBoia5GjobbibfamJzMww/640?wx_fmt=png&from=appmsg)

（5）语言无关性和易用性
Lark 的语法定义和解析逻辑是语言无关的，可以用于解析多种编程语言、自然语言和领域特定语言 (DSL)。

下面展示了其性能比较。

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZvn1thQS2EX0rWpq5O6Q2r5Eh8UDFbIK5sJJ7sxP6IVbCK1z4gd1NHQ/640?wx_fmt=png&from=appmsg)

---

## 2.安装

Lark安装过程比较简单，使用pip命令即可。注意，需要确保您已经安装了 Python 3.6 或更高版本。

```
pip install lark-parser
```

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZpXMGLicghEj3yDLKL6HtguOVuoVX5zwKVGvNXjnsvMVqsJ8lVF83XXg/640?wx_fmt=png&from=appmsg)

下面给出官方的示例：

```
from lark import Lark
l = Lark('''start: WORD "," WORD "!"
            %import common.WORD   // imports from terminal library            %ignore " "           // Disregard spaces in text         ''')
print( l.parse("Hello, World!") )
```

输出结果如下所示：

```
Tree(start, [Token(WORD, 'Hello'), Token(WORD, 'World')])
```

请注意，在最终的树结构里未出现标点符号。Lark会自动过滤掉这些符号。

---

# 三.Lark提取XLM代码的抽象语法树

下面给出其它示例供大家学习，具体用法请读者结合具体需求进行实践。学习文档如下：

* https://lark-parser.readthedocs.io/en/latest/json\_tutorial.html

（1）运算解析

```
from lark import Lark
# 定义文法grammar = """    start: expr    expr: term (("+"|"-") term)*    term: factor (("*"|"/") factor)*    factor: NUMBER | "(" expr ")"    NUMBER: /\d+/    %import common.WS    %ignore WS"""
# 创建 Lark 解析器parser = Lark(grammar, start='start')
# 解析表达式expression = "3 + 5 * (10 - 2)"tree = parser.parse(expression)
print(tree.pretty())
```

输出结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZ2YIkxC4nWJtTWe2mGl6dbMNW0K70LCMTBJlictS75IQVSMDU42FO6oQ/640?wx_fmt=png&from=appmsg)

（2）Json解析

```
from lark import Lark
json_parser = Lark("""    value: dict         | list         | ESCAPED_STRING         | SIGNED_NUMBER         | "true" | "false" | "null"
    list : "[" [value ("," value)*] "]"
    dict : "{" [pair ("," pair)*] "}"    pair : ESCAPED_STRING ":" value
    %import common.ESCAPED_STRING    %import common.SIGNED_NUMBER    %import common.WS    %ignore WS""", start="value")
text = '{"key": ["item0", "item1", 3.14, true]}'t = json_parser.parse(text)print(t.pretty())
```

输出结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZHBuicQuUTicrMZvI60HG3SL3cKNIFiaFJZjUWvlcgXjjHVfGXaq1hd2uw/640?wx_fmt=png&from=appmsg)

（3）XLM宏代码解析

```
from lark import Lark
# 定义 XLM 宏代码的语法规则grammar = """    start: statement+    statement: formula_fill | goto    formula_fill: "FORMULA.FILL" "(" ESCAPED_STRING "," worksheet ")"    goto: "GOTO" "(" cell_ref ")"    ESCAPED_STRING: "\"" /[^"]+/ "\""    worksheet: /[a-zA-Z0-9_!]+/    cell_ref: worksheet? INT    INT: /[0-9]+/
    %import common.WS    %ignore WS"""
# 初始化 Lark 解析器parser = Lark(grammar, start='start', parser='lalr')
# 定义需要解析的 XLM 宏代码xlm_code = '''FORMULA.FILL("=CHAR(R[3508]C[-87])",k0OzKZKXou2wBZX44T!)GOTO(k0OzKZKXou2wBZX44T!14)'''
# 解析代码ast = parser.parse(xlm_code)
# 打印解析结果print(ast.pretty())
```

关键代码结构如下：

![](https://mmbiz.qpic.cn/mmbiz_png/0RFmxdZEDRNZSkJZhyaFuuJ0QswWsHUZ7gO0AQMNNzoNYvpDd4dE...