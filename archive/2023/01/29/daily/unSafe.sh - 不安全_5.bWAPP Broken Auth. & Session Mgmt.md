---
title: 5.bWAPP Broken Auth. & Session Mgmt
url: https://buaq.net/go-146917.html
source: unSafe.sh - 不安全
date: 2023-01-29
fetch_date: 2025-10-04T05:07:12.905082
---

# 5.bWAPP Broken Auth. & Session Mgmt

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

![](https://8aqnet.cdn.bcebos.com/ba01cd5a6a1c135791dee81c931c1325.jpg)

5.bWAPP Broken Auth. & Session Mgmt

0x01、Broken Auth - CAPTCHA BypassingLow验证码绕过，本题验证码没有时间限制，所以提交一次验证码后，就可以暴力破解用户名和密
*2023-1-28 12:18:0
Author: [xz.aliyun.com(查看原文)](/jump-146917.htm)
阅读量:19
收藏*

---

## **0x01、Broken Auth - CAPTCHA Bypassing**

### **Low**

验证码绕过，本题验证码没有时间限制，所以提交一次验证码后，就可以暴力破解用户名和密码了

![](https://img-blog.csdnimg.cn/cfa7b4a88d1846eaa2c5f13f261747e0.png)

爆破结果如下

![](https://img-blog.csdnimg.cn/dbf925b278e046b7b8b097629227936e.png)

### **Medium&High**

方法同上，依旧可以暴力破解。

因此及时销毁验证码的有效性，添加时间限制是很必要的。

## **0x02、Broken Auth. - Forgotten Function**

### **Low**

首先我们审查源码，可以发现源码中使用了mysqli\_real\_escape\_string()函数，来进行防sql注入验证;

且验证了输入是否为email格式:

![](https://img-blog.csdnimg.cn/4c5b5ca53daf44c099cf696f582575ed.png)

暴力破解邮箱，邮箱正确了，会提示你的安全问题，也不会直接显示密码。

![](https://img-blog.csdnimg.cn/a2d6c6cad7b649a090cc17da4399a655.png)

### **Medium**

Medium

同样我们通过审查源码得知，在中级难度时，安全问题会发送邮箱。

![](https://img-blog.csdnimg.cn/ae923f69a0bf4e6284636348efdce7bd.png)

就是我们平时经常遇到的:， 忘记密码需要更改时, 要通过发送修改密码的邮件到绑定的邮箱来修改。

### **High**

会将sha1的随机哈希值发送到邮箱，通过安全问题找回页面重置安全问题

## **0x03、Broken Auth. - Insecure Login Forms**

### **Low**

右键审查元素, 发现用户账号密码信息泄露:

![](https://img-blog.csdnimg.cn/7efa301afa8a4d8c811c7a5f7db22c64.png)

账号：tonystark，密码：I am Iron Man，成功登录

![](https://img-blog.csdnimg.cn/943f4a2cb5da464282dfe485939a1439.png)

### **Medium**

右键审查元素, 同样发现了用户名的泄露， 通过查找发现unlock按钮的事件:

![](https://img-blog.csdnimg.cn/5bd1b0c8362344728777c58f88b3411c.png)

继续在网页源代码中找到 unlock\_secret()函数:

![](https://img-blog.csdnimg.cn/c79abfea15c14374947632fd3071e2a8.png)

```
var bWAPP = "bash update killed my shells!"

    var a = bWAPP.charAt(0);  var d = bWAPP.charAt(3);  var r = bWAPP.charAt(16);
    var b = bWAPP.charAt(1);  var e = bWAPP.charAt(4);  var j = bWAPP.charAt(9);
    var c = bWAPP.charAt(2);  var f = bWAPP.charAt(5);  var g = bWAPP.charAt(4);
    var j = bWAPP.charAt(9);  var h = bWAPP.charAt(6);  var l = bWAPP.charAt(11);
    var g = bWAPP.charAt(4);  var i = bWAPP.charAt(7);  var x = bWAPP.charAt(4);
    var l = bWAPP.charAt(11); var p = bWAPP.charAt(23); var m = bWAPP.charAt(4);
    var s = bWAPP.charAt(17); var k = bWAPP.charAt(10); var d = bWAPP.charAt(23);
    var t = bWAPP.charAt(2);  var n = bWAPP.charAt(12); var e = bWAPP.charAt(4);
    var a = bWAPP.charAt(1);  var o = bWAPP.charAt(13); var f = bWAPP.charAt(5);
    var b = bWAPP.charAt(1);  var q = bWAPP.charAt(15); var h = bWAPP.charAt(9);
    var c = bWAPP.charAt(2);  var h = bWAPP.charAt(2);  var i = bWAPP.charAt(7);
    var j = bWAPP.charAt(5);  var i = bWAPP.charAt(7);  var y = bWAPP.charAt(22);
    var g = bWAPP.charAt(1);  var p = bWAPP.charAt(4);  var p = bWAPP.charAt(28);
    var l = bWAPP.charAt(11); var k = bWAPP.charAt(14);
    var q = bWAPP.charAt(12); var n = bWAPP.charAt(12);
    var m = bWAPP.charAt(4);  var o = bWAPP.charAt(19);

    var secret = (d + "" + j + "" + k + "" + q + "" + x + "" + t + "" +o + "" + g + "" + h + "" + d + "" + p);secret
```

将如上关键代码进行解密

![](https://img-blog.csdnimg.cn/4fa4c41a78b1481abfdd7c72285a8c3b.png)

得到密码为hulk smash! 成功登录

![](https://img-blog.csdnimg.cn/7bf1da97926d465b8f39f48be1ba18ca.png)

### **High**

没有什么别的解法，只有默认账号密码 bee/bug，提示也是如此

![](https://img-blog.csdnimg.cn/9e969767c7ee4e429932b5cf6a85e1fc.png)

成功登录

![](https://img-blog.csdnimg.cn/7a53b6f6c6ee45fba7595d3c8620cac5.png)

## **0x04、Broken Auth. - Logout Management**

审查源码我们可以发现，Low/Medium/High三个级别的区别:

```
switch($_COOKIE["security_level"])
{
    case "0" :
        // Do nothing
        break;
    case "1" :
        // Destroys the session
        session_destroy();
        break;
    case "2" :
        // Unsets all of the session variables
        $_SESSION = array();
        // Destroys the session
        session_destroy();
        break;
    default :
        // Do nothing
        break;
}
```

**Low**

退出登录时，session没有销毁，可以账号依然有效:

![](https://img-blog.csdnimg.cn/177d3353f6eb432aba842fce4cd9cfcb.png)

重新加载刚刚注销的url

x.x.x./ba\_logout.php

发现仍然有效

![](https://img-blog.csdnimg.cn/dd186d5b7acc43a0bbf0a8895b0793ef.png)

### **Medium**

退出登录时，session已经销毁，需重新登录

### **High**

退出登录时，session先被清空，然后销毁，需要重新登录

## **0x05、Broken Auth. - Password Attacks**

### **Low**

用burpsuite等工具爆破即可

### **Medium**

增加了一个随机salt值来验证, 类似于token的作用。

第一种方法：

审查元素我们可以得到salt的值为7-mawE

![](https://img-blog.csdnimg.cn/c7b0385f9ad540fca2f94031fc24808e.png)

构造post请求，即可登陆成功

![](https://img-blog.csdnimg.cn/77e99da319dc4d0ca47f44c970a6094a.png)

第二种方法：

这里用burpsuite演示:

\1. 先选取爆破参数 password 和salt:

![](https://img-blog.csdnimg.cn/b19f38dc85504e6fb62073b29934a6d8.png)

\2. 从相应的页面中获取salt值:

![](https://img-blog.csdnimg.cn/916f56301a944a138d6b38e0dfb37e00.png)

\3. 将redirection设为always:

![](https://img-blog.csdnimg.cn/dae3bc20b04f41bf9b0b95bfa4baa927.png)

\4. 添加密码字典:

![](https://img-blog.csdnimg.cn/4ede6b3b032d41389eb09aac5994a5b9.png)

\5. 将salt设置好, 并且给第一次访问的salt赋值 (不然开始就被不合法验证了, 无法开始):

![](https://img-blog.csdnimg.cn/81ff5022f5644ba2ade79b9fe995a569.png)

\6. 由于设置了salt, 是一对一的验证, 只有获取上一个请求返回的salt值才能，做下一次请求, 因此只能单线程, 在option中设置线程为1:

![](https://img-blog.csdnimg.cn/3e663fd2b67d4a69abdea23fd5e881f3.png)

\7. start attack, 长度不同的那个即为正确密码:

![](https://img-blog.csdnimg.cn/84fb5419ed734482988449bf2993b785.png)

### **High**

加了图片验证码, 也是我们现实中经常遇到的:

## **0x06、Broken Auth. - Weak Passwords**

弱口令，直接挂字典用burp爆破。

### **Low**

test / test

### **Medium**

test / test123

### **High**

test / Test123

## **0x07、Session Mgmt. - Administrative Portals**

### **Low**

![](https://img-blog.csdnimg.cn/971a048043694fa5bf0b535b64037d33.png)

admin参数控制页面, 直接修改为1即可:

![](https://img-blog.csdnimg.cn/484c53ea128d486fa9f2014c7731349e.png)

### **Medium**

同样, 只不过控制的admin参数在cookie中:

![](https://img-blog.csdnimg.cn/f19aaebb723148d398d9f08f47cc8483.png)

直接修改为1即可:

![](https://img-blog.csdnimg.cn/eb15c4bff19d475da40f71174beb7bc2.png)

### **High**

需要修改session中的admin值为1, 或者直接用管理员账号bee/bug登录也可以。

## **0x08、Session Mgmt. - Cookies (HTTPOnly)**

### **Low**

审查源码, 发现 Cookies中httponly字段设置为false:

![](https://img-blog.csdnimg.cn/d9bd3a2345f1402eb47d8d6d96e7e5cd.png)

* setcookie(name,value,expire,path,domain,secure)

| 参数 | 描述 |
| --- | --- |
| name | 必需。规定 cookie 的名称。 |
| value | 必需。规定 cookie 的值。 |
| expire | 可选。规定 cookie 的有效期。 |
| path | 可选。规定 cookie 的服务器路径。 |
| domain | 可选。规定 cookie 的域名。 |
| secure | 可选。规定是否通过安全的 HTTPS 连接来传输 cookie。 |

点击 Click Here ，本地JS脚本可以直接访问到top\_security这个变量值:

![](https://img-blog.csdnimg.cn/2048e7d8071b4fee8f37e77712d99a24.png)

### **Medium**

Cookies中httponly字段设置为true:

![](https://img-blog.csdnimg.cn/f5a5cb625cc041a7ba4def75aa42e12f.png)

点击Click Here，本地JS脚本无法访问top\_security变量值了:

![](https://img-blog.csdnimg.cn/37fc20df91f6444cba6175992c4b5d03.png)

### **High**

Cookies中httponly字段设置为ture,同时缩短了cookies的生存时间

![](https://img-blog.csdnimg.cn/afee47315d1c49699d04bbf4213c3907.png)

与中级难度的区别在于，调整了Cookie的生存时间，仅有300秒（5分钟）:

![](https://img-blog.csdnimg.cn/0f9b4ed197c148e587ea8aafaaf09126.png)

## **0x09、Session Mgmt. - Session ID in URL**

三个等级的难度都一样, Session ID 暴露在URL中:

![](https://img-blog.csdnimg.cn/7b4a73daec0241c69e6b72ba3988e835.png)

Session ID 应该从不暴露在URL中。

## **0x10、Session Mgmt. - Strong Sessions**

本题主要是通过观察top\_security\_nossl和top\_security\_ssl的情况，

来了解Session的安全存储

### **Low**

没有任何安全可言

### **Medium**

可以观察到top\_security\_nossl的值是使用了HASH处理

![](https://img-blog.csdnimg.cn/c57bc22c279b4f68b9f21d52c5b115e1.png)

### **High**

在非SSL情况下，看不到top\_security\_ssl的值

改用HTTPS后，可以观察到top\_security\_nossl值

![](https://img-blog.csdnimg.cn/6c55c5d2e2ee46a7bc9c149439ad1baf.png)

文笔生疏，措辞浅薄，望各位大佬不吝赐教，万分感谢。

免责声明：由于传播或...