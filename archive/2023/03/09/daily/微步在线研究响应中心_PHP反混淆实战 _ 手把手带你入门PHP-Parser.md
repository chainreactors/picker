---
title: PHP反混淆实战 | 手把手带你入门PHP-Parser
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247500226&idx=1&sn=43b15aaf194d63a654887b442d1da6ea&chksm=cfcaa2d6f8bd2bc0f5276ce2527c2d854ef6c6ee4058d9902c6236a733a15153831c6ec24535&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2023-03-09
fetch_date: 2025-10-04T09:02:00.213566
---

# PHP反混淆实战 | 手把手带你入门PHP-Parser

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMJMdRf7aG71h2CfS9nsRW8Nysuoia3BLaqDN2twlsEQLmibRD1ZqXOwXFJTAYDqnQxibad3U4raPH98A/0?wx_fmt=jpeg)

# PHP反混淆实战 | 手把手带你入门PHP-Parser

原创

子推

微步在线研究响应中心

![](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMJasbTOEml0jviatLrkYy1A6NxWSic8LyMWIV3XiaIwhuEfBBeU85PnFkDpcfdWgSGrMXmLlRrTbqJIg/640?wx_fmt=jpeg)

1

**什么是PHP-Parser ?**

PHP-Parser是由Nikic开发的一款PHP抽象语法树（AST）解析工具。能够将PHP代码转换为抽象语法树，安全研究员可以通过生成的语法树对PHP样本进行控制流图生成、静态分析和污点检测等操作，同时其组合模式的设计使得每个节点操作的处理相互独立，后期维护十分方便。因此在PHP Webshell检测领域中被广泛使用。同时对于生成的抽象语法树也可以进行操作，从代码节点的角度对PHP文件进行修改，所以通过PHP-Parser进行代码的混淆和反混淆是十分方便的。在非安全领域，PHP-Parser也可以自动帮你补全单元测试框架、检查代码问题。

接下来从笔者从事相关工作的经验来探讨下通过PHP-Parser进行反混淆的方法，通过对某CTF混淆样本进行反混淆让大家初步掌握使用PHP-Parser反混淆的方法。

2

**PHP-Parser入门**

此章主要介绍PHP-Parser的创建过程以及在实战中需要用的方法、节点类型等。

**1.创建解析器实例**

要使用PHP-Parser，首先需要创建实例，在创建时选择解析的语言版本，声明格式如下：

```
use PhpParser\ParserFactory;$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);
```

其中ParserFactory的参数有以下四种：

|  |  |
| --- | --- |
| **参****数** | **效果** |
| ParserFactory::PREFER\_PHP7 | 优先解析PHP7，如果PHP7解析失败则将脚本解析成PHP5 |
| ParserFactory::PREFER\_PHP5 | 优先解析PHP5，如果PHP5解析失败则将脚本解析成PHP7 |
| ParserFactory::ONLY\_PHP7 | 只解析成PHP7 |
| ParserFactory::ONLY\_PHP5 | 只解析成PHP5 |

**2.解析PHP代码**

通过解析器的parse方法将PHP代码解析成抽象语法树：

```
<?phpuse PhpParser\Error;use PhpParser\ParserFactory;        require 'vendor/autoload.php';         $code = file_get_contents("./test.php");$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);try {    $ast = $parser->parse($code);} catch (Error $error) {    echo "Parse error: {$error->getMessage()}\n";}
```

**3.输出抽象语法树**

通过Node Dumping我们可以生成一个直观的AST，例如我们使用view.php来解析sample.php：

```
//view.php<?php
require 'vendor/autoload.php';use PhpParser\Error;use PhpParser\NodeDumper;use PhpParser\ParserFactory;//获取sample.php的代码内容$code = file_get_contents('sample.php');//初始化解析器$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);try {    //解析sample.php内容，转换为ast   $ast = $parser->parse($code);} catch (Error $error) {    echo "Parse error: {$error->getMessage()}\n";    return;}
$dumper = new NodeDumper;//优化ast并dumpecho $dumper->dump($ast) . "\n";
```

sample.php的解析效果如下：

```
<?php $a = 'a'.'ssert';$a($_POST['x']);=======array(    0: Stmt_Expression(        expr: Expr_Assign(            var: Expr_Variable(                name: a            )            expr: Expr_BinaryOp_Concat(                left: Scalar_String(                    value: a                )                right: Scalar_String(                    value: ssert                )           )        )    )    1: Stmt_Expression(        expr: Expr_FuncCall(            name: Expr_Variable(               name: a           )            args: array(               0: Arg(                    name: null                    value: Expr_ArrayDimFetch(                        var: Expr_Variable(                           name: _POST                       )                        dim: Scalar_String(                            value: x                        )                    )                    byRef: false                    unpack: false                )            )        )   )
```

**4.抽象语法树上的Node节点**

PHP-Parser解析成抽象语法树之后会存在140多种节点，主要有以下几类：

|  |  |  |
| --- | --- | --- |
| **节点表达式** | **节点类型** | **节点实例** |
| PhpParser\Node\Stmts | 语句节点，不存在返回值也不能进行表达式判断 | Namespace  Class |
| PhpParser\Node\expr | 表达式节点，即存在返回值的语言结构，可以进行表达式判断 | Variable  FuncCall  BinaryOP |
| PhpParser\Node\Scalars | 标量值节点，通常使用的字符串、数字或者魔术常量 | String\_  LNumber |

**5.AST转回PHP代码**

PHP-Parser中的“PhpParser\PrettyPrinter“类用来打印AST转换之后的代码，在我们对抽象语法树进行修改之后可以使用其生成新的PHP代码：

```
$prettyPrinter = new PrettyPrinter\Standard;$prettyCode = $prettyPrinter->prettyPrintFile($ast);echo $prettyCode;
```

**6.节点遍历**

节点遍历是PHP-Parser提供的最关键的接口，它为我们提供了遍历语法树节点的方式，通过编写特定的操作我们可以还原指定的代码。所有的Visitor都需要实现

“PhpParser\NodeVisitor“接口，该接口定义4个遍历方法：

```
//方法在遍历开始之前调用public function beforeTraverse(array $nodes);//在遍历子节点之前调用public function enterNode(\PhpParser\Node $node);//在离开当前节点时调用public function leaveNode(\PhpParser\Node $node);//在遍历之后调用一次public function afterTraverse(array $nodes)
```

3

**PHP-Parser实战**

这部分将从最基础的还原拼接字符串入手，一步步分析语法树特点，编写还原操作；然后尝试对函数进行编码解码，最后通过CTF赛题实战完整的解混淆一个文件，加深对于PHP-Parser的掌握。

**1.字符二元操作符还原**

针对字符串的异或、拼接、与或非等操作进行还原，基础样本如下：

```
<?php     $a = 'a'.'s'.'s'.'e'.'r'.'t';    $a($_POST['x']);?>
```

首先输出AST进行查看。

```
array(    0: Stmt_Expression(        expr: Expr_Assign(            var: Expr_Variable(                name: a            )            expr: Expr_BinaryOp_Concat(                left: Expr_BinaryOp_Concat(                    left: Expr_BinaryOp_Concat(                       left: Expr_BinaryOp_Concat(                            left: Expr_BinaryOp_Concat(                                left: Scalar_String(                                    value: a                                )                                right: Scalar_String(                                    value: s                                )                            )                            right: Scalar_String(                                value: s                            )                        )                        right: Scalar_String(                            value: e                       )                   )                   right: Scalar_String(                        value: r                    )                )                right: Scalar_String(                   value: t                )            )        )    )    1: Stmt_Expression(        expr: Expr_FuncCall(            name: Expr_Variable(               name: a            )            args: array(                0: Arg(                   name: null                    value: Expr_ArrayDimFetch(                        var: Expr_Variable(                            name: _POST                        )                       dim: Scalar_String(                            value: x                        )                    )                    byRef: false                    unpack: false                )            )        )    ))
```

这个例子比较单一，连接节点为“Node\Expr\BinaryOp\Concat“,且左右都为”Scalar“类型的节点，可以直接进行拼接操作，所以我们可以编写Visitor类如下，使用”leaveNode“或者”enterNode“将左右节点连接并返回：

```
class BinaryOpReducer extends NodeVisitorAbstract{   public function leaveNode(Node $node) {        if ($node instanceof Node\Expr\BinaryOp\Concat && $node->left instanceof Node\Scalar\String_ && $node->right instanceof Node\Scalar\String_) {            return new PhpParser\Node\Scalar\String_($node->left->value . $node->right->value);        }    }}
```

代码考虑的比较简单，没有对左右节点为其他变量类型的情况作限制，这样可以把连接操作符的字符串还原，效果如下：

```
<?php        $a = 'assert';$a($_POST['x']);
```

因为变量的还原涉及到作用域、存储结构等问题，这里不做探讨。

**2.字符串编码解码**

这部分尝试将字符串替换为`base64`加密之后的结果，思路如下：

* 判断当前节点是否为”Scalar\String\_”；
* 将节点的”value”值进行“base64\_encode“编码；
* 替换原节点为“FuncCall“类型；

代码如下：

```
class Base64Reducer extends NodeVisitorAbstract
    public function leaveNode(Node $node) {        if ($node instanceof Node\Scalar\String_) {            $name = $node->value;            return new Expr\FuncCall(                new Node\Name("base64_decode"),                [new Node\Arg(new Node\Scalar\String_(base64_encode($name)))]            );        }    }}
```

效果如下：

```
<?php              $str = "Threatbook";?>                  --After parser:--
$str = base64_decode('VGhyZWF0Ym9vaw==');
```

**3.CTF混淆文件还原实战**

经过上面两个例子，已经掌握了PHP-Parser的基础运用，接下来通过还原混淆文件深化一下对于节点的理解，样本是2020年高校战“疫”网络安全分享赛中Hardphp题目的混淆文件，我们将从WriteUP逆向推导出反混淆思路，混淆文件如下：

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIDK90OExv0IlAnvFickuAPCLgTs7DqScibcUz724FU8ibjqpHiaoavMBJHnYXBnOSK7TlTCGiaF9aw3gA/640?wx_fmt=png)

首先观察可以发现，混淆文件通过“unserialize(base64\_decode(“的方式将字符串解码结果赋值给”GLOBALS“数组，然后通过数组值进行运算。

由于存在部分乱码的变量名，首先将所有的乱码变量批量重命名。思路如下：

* 筛选所有“Variable“类型的节点；
* 通过正则表达式匹配出乱码变量，这种变量名中不会出现字母数字等字符；
* 通过一个数组存放重命名的变量名，如果某个乱码变量再次出现，通过数组查询新的变量名进行替换。

代码如下：

```
// 变量重命名class ReNameVariable extends NodeVisitorAbstract{
    public $Count = 0...