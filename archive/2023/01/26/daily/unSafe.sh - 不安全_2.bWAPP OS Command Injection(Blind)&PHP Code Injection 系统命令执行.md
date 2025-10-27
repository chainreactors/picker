---
title: 2.bWAPP OS Command Injection(Blind)&PHP Code Injection 系统命令执行
url: https://buaq.net/go-146696.html
source: unSafe.sh - 不安全
date: 2023-01-26
fetch_date: 2025-10-04T04:50:05.273622
---

# 2.bWAPP OS Command Injection(Blind)&PHP Code Injection 系统命令执行

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

![](https://8aqnet.cdn.bcebos.com/d7a132ea2f10c3674bc22aeb43934292.jpg)

2.bWAPP OS Command Injection(Blind)&PHP Code Injection 系统命令执行

LDAP Injection (Search)LDAP 全英文：Lightweight Directory Access Protocol，翻译过来就是轻量级的目
*2023-1-25 15:22:0
Author: [xz.aliyun.com(查看原文)](/jump-146696.htm)
阅读量:39
收藏*

---

## **LDAP Injection (Search)**

LDAP 全英文：Lightweight Directory Access Protocol，翻译过来就是轻量级的目录访问协议。其实就是访问目录，浏览目录。有很多企业存储一些数据信息，例如部门信息，部门里成员的信息，公司的可用设备信息等，这些信息单独放在类似于网站的那种数据库中的话，会显的有点大材小用，而把它们放在目录中，文本中最合适。好比在文档中搜索指定的内容，在目录中搜索指定的文件一样。 LDAP 也有自己指定的语法，也可理解为它是一个存储信息的数据库，为了搜索方便，很多网站提供了其查询的接口，和普通的搜索框无异，对于指定的搜索内容，在没有严格过滤的情况下，便可以造成LDAP 注入。

## **Mail Header Injection (SMTP)**

通常的做法是网站实施联系表单，反过来将合法用户的电子邮件发送给消息的预期收件人。大多数情况下，这样的联系表单将设置SMTP标头From，Reply-to以便让收件人轻松处理联系表单中的通信，就像其他电子邮件一样。

不幸的是，除非用户的输入在插入SMTP头之前被验证，否则联系表单可能容易受到电子邮件头插入（也称为SMTP头注入）的攻击。这是因为攻击者可以将额外的头部注入到消息中，从而指示SMTP服务器执行与预期不同的指令。

## **OS Command Injection**

漏洞url：<http://range.anhunsec.cn:82/commandi.php>

### **Level：low**

payload：www.nsa.gov;whoami

![](https://img-blog.csdnimg.cn/c62d3ef7650646998ebfa2b42bcbba90.png)

原理：在DNS查询之后再执行dir命令

### **Level：medium**

查看源码

![](https://img-blog.csdnimg.cn/c232ed8bf06d4679aa6b32d19f5d27a4.png)

commandi\_check\_1是把&和;替换了，还可以使用|

构造payload：www.nsa.gov | whoami

![](https://img-blog.csdnimg.cn/41387cc1700e4e23a5087a607cb0b3bb.png)

### **Level：high**

查看源码

![](https://img-blog.csdnimg.cn/e4e03b8be36240808de5d2ed1ee76c7b.png)

escapeshellcmd()函数用来跳过字符串中的特殊符号，防止恶意用户通过不正当方式破解服务器系统

## **OS Command lnjection - Blind**

漏洞url：<http://range.anhunsec.cn:82/commandi_blind.php>

命令盲注就是注入后没有返回信息，要根据反应时间判断命令是否成功执行

输入127.0.0.1

![](https://img-blog.csdnimg.cn/1b32aa2040a146459707251c52d778b8.png)

输入

```
||whoami `sleep 5 `
```

![](https://img-blog.csdnimg.cn/857d2fc6e1c44db78797049ce078a5ec.png)

## **PHP Code Injection**

漏洞url：<http://range.anhunsec.cn:82/phpi.php>

### **Level：low**

构造payload：?message=phpinfo();

![](https://img-blog.csdnimg.cn/54853c6f98724107af0c27fb2c5443a2.png)

### **Level：medium&high**

查看源码，使用了htmlspecialchars()函数无法绕过

![](https://img-blog.csdnimg.cn/a7e01030d8f348ad8a43db95f3bddb47.png)

## **Server-Side Includes (SSI) Injection**

SSI是英文"Server Side

Includes"的缩写，翻译成中文就是服务器端包含的意思。SSI是用于向HTML页面提供动态内容的Web应用程序上的指令。它们与CGI类似，不同之处在于SSI用于在加载当前页面之前或在页面可视化时执行某些操作。 为此，Web服务器在将页面提供给用户之前分析SSI,可在SHTML文件中使用SSI指令引用其他的html文件（#include），此时服务器会将SHTML中包含的SSI指令解释，再传送给客户端，此时的HTML中就不再有SSI指令了。Server-Side

Includes攻击允许通过在HTML页面中注入脚本或远程执行任意代码来利用Web应用程序。

一种对于这类漏洞的挖掘方式即是查看.stm，.shtm和.shtml的页面是否存在，但是缺少这些类型的页面并不意味着不存在SSI攻击。

默认Apache不开启SSI，SSI这种技术已经比较少用了 IIS和Apache都可以开启SSI功能

核心代码

```
<div id="main">

    <h1>Server-Side Includes (SSI) Injection</h1>

    <p>What is your IP address? Lookup your IP address... (<a href="http://sourceforge.net/projects/bwapp/files/bee-box/" target="_blank">bee-box</a> only)</p>

    <form action="<?php echo($_SERVER["SCRIPT_NAME"]);?>" method="POST">

        <p><label for="firstname">First name:</label><br />                                        //firstname表单
        <input type="text" id="firstname" name="firstname"></p>

        <p><label for="lastname">Last name:</label><br />                                          //lastname表单
        <input type="text" id="lastname" name="lastname"></p>

        <button type="submit" name="form" value="submit">Lookup</button>

    </form>

    <br />
    <?php

    if($field_empty == 1)                                                              //这里的PHP只是判断是否有输入
    {

        echo "<font color=\"red\">Please enter both fields...</font>";

    }

    else
    {

        echo "";

    }

    ?>

</div>
```

防护代码

```
$field_empty = 0;

function xss($data)
{

    switch($_COOKIE["security_level"])
    {

        case "0" :

            $data = no_check($data);
            break;

        case "1" :

            $data = xss_check_4($data);
            break;

        case "2" :

            $data = xss_check_3($data);
            break;

        default :

            $data = no_check($data);
            break;

    }

    return $data;

}

if(isset($_POST["form"]))
{

    $firstname = ucwords(xss($_POST["firstname"]));                                            //ucwords()首字母大写
    $lastname = ucwords(xss($_POST["lastname"]));

    if($firstname == "" or $lastname == "")
    {

        $field_empty = 1;

    }

    else
    {

        $line = '<p>Hello ' . $firstname . ' ' . $lastname . ',</p><p>Your IP address is:' . '</p><h1><!--#echo var="REMOTE_ADDR" --></h1>';

        // Writes a new line to the file
        $fp = fopen("ssii.shtml", "w");
        fputs($fp, $line, 200);
        fclose($fp);

        header("Location: ssii.shtml");

        exit;

    }

}

?>
```

#### **low：**

low级别，没有防护，能xss

![](https://img-blog.csdnimg.cn/1a4988fa9f314ad78fb46b203217e441.png)

#### **medium：**

```
function xss_check_4($data)
{

 // addslashes - returns a string with backslashes before characters that need to be quoted in database queries etc.
 // These characters are single quote ('), double quote ("), backslash (\) and NUL (the NULL byte).
 // Do NOT use this for XSS or HTML validations!!!

 return addslashes($data);

}
```

addslashes（）在符号前加反斜线

#### **high:**

```
function xss_check_3($data, $encoding = "UTF-8")
{

    // htmlspecialchars - converts special characters to HTML entities
    // '&' (ampersand) becomes '&'
    // '"' (double quote) becomes '"' when ENT_NOQUOTES is not set
    // "'" (single quote) becomes ''' (or ') only when ENT_QUOTES is set
    // '<' (less than) becomes '<'
    // '>' (greater than) becomes '>'

    return htmlspecialchars($data, ENT_QUOTES, $encoding);

}
```

将预定义的字符装换为html实体字符

文笔生疏，措辞浅薄，望各位大佬不吝赐教，万分感谢。

免责声明：由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

转载声明：儒道易行 拥有对此文章的修改和解释权，如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经作者允许，不得任意修改或者增减此文章的内容，不得以任何方式将其用于商业目的。

文章来源: https://xz.aliyun.com/t/12066
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)