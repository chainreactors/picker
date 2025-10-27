---
title: wordperss_country-state-city-auto-dropdown插件未授权sql注入漏洞分析
url: https://forum.butian.net/share/3638
source: 奇安信攻防社区
date: 2024-07-25
fetch_date: 2025-10-06T17:41:08.312129
---

# wordperss_country-state-city-auto-dropdown插件未授权sql注入漏洞分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### wordperss\_country-state-city-auto-dropdown插件未授权sql注入漏洞分析

* [漏洞分析](https://forum.butian.net/topic/48)

WordPress的Country State City Dropdown CF 7插件是一款用于WordPress网站的插件，它可以与Contact Form 7（CF 7）表单插件配合使用，为用户提供了一个方便的方式来在表单中选择国家、州/省和城市。近期WordPress Country State City Dropdown CF7插件被爆出在版本2.7.2及之前的版本中存在SQL注入漏洞（CVE-2024-3495），本篇文章围绕该漏洞展开学习。

### 前言：
​ WordPress的Country State City Dropdown CF 7插件是一款用于WordPress网站的插件，它可以与Contact Form 7（CF 7）表单插件配合使用，为用户提供了一个方便的方式来在表单中选择国家、州/省和城市。近期WordPress Country State City Dropdown CF7插件被爆出在版本2.7.2及之前的版本中存在SQL注入漏洞（CVE-2024-3495），本篇文章围绕该漏洞展开学习。
### 0x01 漏洞描述：
​ WordPress Country State City Dropdown CF7插件在版本2.7.2及之前的版本中存在SQL注入漏洞（CVE-2024-3495）未经身份验证的远程攻击者可利用此漏洞获取数据库敏感信息。该漏洞是因为用户提供的参数未经足够转义并且现有SQL查询未经充分准备。这使得未经身份验证的攻击者可以将额外的SQL查询附加到已存在的查询中，从而提取数据库中的敏感信息。
\*\*影响版本：Country State City Dropdown CF7&lt;=2.7.2\*\*
### 0x02 环境搭建：
[Country State City Dropdown CF7插件下载地址](https://ca-valencia.wordpress.org/plugins/country-state-city-auto-dropdown)
下载插件后直接上传至wordpress中即可。
![image-20240605160020617](https://oss-yg-cztt.yun.qianxin.com/butian-public/f938194fdb70836d22bd6324423ed56d8e21f4847655f.jpg)
### 0x03 漏洞分析：
一、\*\*nonce：\*\*
首先了解一下wordpress中nonce的作用是什么？nonce字面意思一般指的是“使用一次的数字”，而在wordpress中nonce主要用于通过将查询字符串嵌入到URL 和表单来工作，确保请求有效并且来自合法用户。细节请看[此篇文章](https://www.wpdaxue.com/wordpress-nonce.html)
![image-20240614151548616](https://oss-yg-cztt.yun.qianxin.com/butian-public/f932047962b67ac456d014c7b65fc7bd1b85b3926befa.jpg)
在wordpress中nonce的生成：
通过调用wp\\_create\\_nonce函数生成nonce值，首先根据传入的$action判断action是否有效，下来根据当前用户登录状态返回uid，如果是登录状态则传回登录uid，如果没有登陆uid赋值为0通过`'nonce\_user\_logged\_out'` 过滤器来修改uid，再使用wp\\_hash() 函数生成nonce值。nonce值与当前用户uid和session绑定。（在WordPress中切换当前用户的身份，可以根据用户ID或用户名来指定，意味着无论是否登录，都可以生成nonce）
![image-20240626105013668](https://oss-yg-cztt.yun.qianxin.com/butian-public/f3403442b72694af1ff7c64724a0b695003f5755c58a6.jpg)
nonce有效期默认为12h
![image-20240626100417267](https://oss-yg-cztt.yun.qianxin.com/butian-public/f3219308a89f3d50f84a0b06b9dd55ab73207c255696f.jpg)
\*\*二、未授权sql注入\*\*
根据公开poc定位到问题所在位置wp-content/plugins/country-state-city-auto-dropdown/includes/ajax-actions.php：
这里主函数定义了tc\\_csca\\_get\\_states、tc\\_csca\\_get\\_cities函数，任选一个tc\\_csca\\_get\\_cities函数进行分析。先是使用check\\_ajax\\_referer函数对传入的nonce与后端生成的nonce进行校验。下来直接就定义全局变量$wpdb，用于后续sql查询。然后通过一个if语句判断是否设置了名为 `sid` 的 POST 参数，存在将其值赋给变量 `$sid`。其中`sanitize\_text\_field()` 函数用于清理和过滤输入。最后把经过处理的sid值代入sql查询语句。下面跟进看下这里的逻辑。
![image-20240607162848482](https://oss-yg-cztt.yun.qianxin.com/butian-public/f6036017a0ba83baf917893afbcd48750aabb74990b91.jpg)
跟进check\\_ajax\\_referer函数，可以看到此函数用于检验AJAX 请求中的安全性，主要校验传参进来的nonce与后端针对action生成得nonce是否相对应。逻辑如下：首先检查是否传入有效的action，然后从传入的参数中提取nonce值，下来使用 `wp\_verify\_nonce()` 函数来验证提取到的 nonce 的有效性，将 nonce 与指定的 `$action` 进行比较，并返回验证结果。验证完成后，函数触发一个动作钩子 `check\_ajax\_referer`，传递 `$action` 和验证结果 `$result`，最后如果验证失败且 `$stop` 参数为 `flase`函数终止并输出错误信息。
![image-20240611152824363](https://oss-yg-cztt.yun.qianxin.com/butian-public/f7404940d3502e78ec18d46c7500d620921fef2889549.jpg)
`$wpdb->prepare()` 方法用于准备 SQL 查询语句， `%1s` 是占位符，用于替换为传入的 `$sid` 参数的值，将整个查询语句准备好以供执行。查询语句构造是在wprdpress数据库city表中设置stste\\_id为传入的sid进行查询。
![image-20240612111633263](https://oss-yg-cztt.yun.qianxin.com/butian-public/f48676716ff15171328cc7046989e162ed4b1b1e4f9d0.jpg)
通过调用 `$wpdb->get\_results()` 方法执行查询，并将结果存储在 `$cities` 变量中。对WordPress 数据库操作感兴趣的可以参考[此篇手册](https://www.easywpbook.com/opt/wpdb.html)，这里不做过多解释。
![image-20240607165251253](https://oss-yg-cztt.yun.qianxin.com/butian-public/f887795a0bc5f752c92075710b0a513d07224d0a1d26b.jpg)
其中`sanitize\_text\_field()` 函数主要用于过滤输入的字符，保证输入的参数为字符串形式没有特殊符号也没有‘%’编码形式得字符。首先确认传入得$sid不是对象或者数组，如果是返回空，并把传入的字符强制转换为字符串形式。下来用内置filter过滤无效的 UTF-8 字符。后又过滤了'&lt;'、换行符、制表符、回车符、连续空格、百分号编码字符，把这些特殊字符用单个空格替换。这里过滤不全，过滤的空格可以使用注释符替换，过滤百分号编码，那么我们可以尝试其他编码形式去绕过。
![image-20240607163657562](https://oss-yg-cztt.yun.qianxin.com/butian-public/f50304541025988dccb948d838eab752c91e6a31327cd.jpg)
那么攻击者怎么获取到有效的nonce进行攻击呢？下来继续看源码。
已知nonce是通过wp\\_create\\_nonce生成得，那么全局搜索看看哪里调用该函数，通过搜索比对发现在country-state-city-auto-dropdown/trunk/includes/include-js-css.php中CF7插件把在后端生成的nonce通过wp\\_locallize函数callback到前端：
![image-20240607182722915](https://oss-yg-cztt.yun.qianxin.com/butian-public/f434556232349cac1ca663fa562bc1b7dc0709e483158.jpg)
![image-20240626105440064](https://oss-yg-cztt.yun.qianxin.com/butian-public/f76825500e875175f52ecd598a11f19489226bf8f8089.jpg)
![image-20240626105149262](https://oss-yg-cztt.yun.qianxin.com/butian-public/f75344653755698211993ce1a5aa55772b2be17d7601c.jpg)
先通过 `wp\_enqueue\_script()` 函数在 WordPress 前端页面中添加脚本和本地化数据。接着使用 `wp\_localize\_script()` 函数为js添加 `ajax\_url` 和 `nonce`本地化数据并且分别指定了 WordPress 后台 AJAX 请求的 URL 和安全性验证。这些数据会传递到 JavaScript 文件中，以便在前端 JavaScript 中可以使用。最后，通过 `add\_action('wp\_enqueue\_scripts', 'tc\_csca\_embedCssJs')` 将该函数挂载到 WordPress 的 `'wp\_enqueue\_scripts'` 动作上，以确保在前台页面加载时执行。
\*\*综上所述：\*\*
当前用户的nonce值无法被攻击者获取，但是生成的nonce会被传送到前端，所以可以在前端全局搜索获取nonce值进行利用。而在主函数中，仅检验nonce未检验当前用户是否有管理员权限，而对于传入的参数过滤不完全和可直接拼接造成了sql注入。所以导致未授权sql注入漏洞存在。
### 0x04 漏洞复现：
一、在首页源码中找到nonce
![image-20240605160129390](https://oss-yg-cztt.yun.qianxin.com/butian-public/f456584797af53e40f5657c351431f5b552e1c6d65e8e.jpg)
二、poc验证
```php
POST /wordpress/wp-admin/admin-ajax.php HTTP/1.1
Host: xxxxxxx
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: wordpress\_test\_cookie=WP%20Cookie%20check; Hm\_lvt\_8acef669ea66f479854ecd328d1f348f=1716965892; Hm\_lpvt\_8acef669ea66f479854ecd328d1f348f=1717138760
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 172
action=tc\_csca\_get\_cities&nonce\_ajax=edd043e9ec&sid=1+or+0+union+select+concat(0x64617461626173653a,database(),0x7c76657273696f6e3a,version(),0x7c757365723a,user()),2,3--+-
```
![image-20240605160352821](https://oss-yg-cztt.yun.qianxin.com/butian-public/f40449105cf50197b2a312888c2990ca38de847cc013d.jpg)
### 0x05 漏洞修复：
添加了管理员权限验证，使用if判断语句配合函数current\\_user\\_can()函数检查当前用户是否具有编辑、查看等管理员操作权限。有权限才可以继续执行下面的代码，没有权限则会返回 'message' =&gt; 'Not Allowed'
![image-20240611183431309](https://oss-yg-cztt.yun.qianxin.com/butian-public/f532746e77fdedb00c8dbf2fc444bbc2c72afb0a0518f.jpg)
在查询语句的时候使用单引号把占位符括起来'%1s'，防止 SQL 注入攻击。
![image-20240611183525225](https://oss-yg-cztt.yun.qianxin.com/butian-public/f7193083eb73c6232b91a940e6bc6ea53aa422c1b24ee.jpg)
更新之后nonce还是会传回前端
![image-20240614155009910](https://oss-yg-cztt.yun.qianxin.com/butian-public/f377593a30ce93fccb1a8a2c7287043cae4b4c20ee83b.jpg)
但是因为加了权限认证，直接调用tc\\_csca\\_get\\_ciies会返回not allowed。
![image-20240614155001795](https://oss-yg-cztt.yun.qianxin.com/butian-public/f510756b4db35fcc9c172dcad44b909fbb96d5cb02512.jpg)

* 发表于 2024-07-24 09:35:39
* 阅读 ( 30648 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![中铁13层打工人](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/bd481171367dd9c7aac272bf517c972393f08b4.jpg)](https://forum.butian.net/people/77)

[中铁13层打工人](https://forum.butian.net/people/77)

...