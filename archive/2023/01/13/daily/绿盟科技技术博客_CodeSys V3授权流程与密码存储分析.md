---
title: CodeSys V3授权流程与密码存储分析
url: http://blog.nsfocus.net/codesys-v3/
source: 绿盟科技技术博客
date: 2023-01-13
fetch_date: 2025-10-04T03:45:38.298103
---

# CodeSys V3授权流程与密码存储分析

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# CodeSys V3授权流程与密码存储分析

### CodeSys V3授权流程与密码存储分析

[2023-01-12](https://blog.nsfocus.net/codesys-v3/ "CodeSys V3授权流程与密码存储分析")[陈杰](https://blog.nsfocus.net/author/chenjie/ "View all posts by 陈杰")

阅读： 2,042

## ****一、前言****

CodeSys 在新版V3通讯协议中已经默认开启授权机制，用户必须设置账号密码才可以进一步使用。在设置密码成功后，用户必须登录后才能对PLC进行控制管理以及编程组态等操作。本文将分享CodeSys V3的授权流程和密码存储相关算法。

## ****二、密码存储****

新版CodeSys V3通讯协议账号相关信息默认存放于UserDatabase文件中，旧版本的CodeSys V3的密码是MD5加密的，新版做了改进，使用了scrypt算法来进行存放。该算法在CryptoDeriveKey中实现，如下所示：

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_0-300x123.png)

UserDatabase文件内容如下，其中“admin”为用户名，后面接着的是密码哈希信息。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_1-300x44.png)

* “d819a24df7bdc985”指的是scrypt的盐salt。
* “02f6……5cfd” 指的是scrypt算出的密码哈希。
* “512，8，1”指的是scrypt的N,r,p参数。

使用scrypt原因主要为该算法不仅计算所需时间长，而且占用的内存也多，使得并行计算多个摘要异常困难，因此利用彩虹表进行暴力攻击更加困难。

当然即使算法设计的再健全，也挡不住用户使用弱口令。在最新版的组态软件并没有强制要求密码强度，使得用户也可以设置诸如“123456”等弱口令密码。这就导致安全意识不强的用户会将密码设置成弱口令。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_2-300x157.png)

通过编写py脚本将scrypt哈希信息转换为标准的hashcat的scrypt hash格式，之后可以利用hashcat对该哈希进行爆破攻击。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_3-300x147.png)

生成得到的哈希如下所示：

|  |
| --- |
| SCRYPT:512:8:1:2BmiTfe9yYU=:Avat90uq9ScoWI3p+46HI8solorDp225o6Qi68wud34= |

运行hashcat.cat命令：hashcat.exe -m 8900 -a 0 scrypt.hash dict.txt，爆破成功率依赖于字典以及密码的复杂度，可以使用高性能的GPU，加快爆破速度。

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_4-300x137.png)

## ****三、授权流程****

客户端先通过CmpDevice的2号服务ID请求PLC获取公钥和challenge：

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_5-300x165.png)

PLC将会随机生成一个密钥对和一个32字节的challenge，响应包将包含公钥和challenge。

公钥信息如下所示：

**![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_6-300x146.png)**

32 字节challenge信息如下：

**![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_7-300x149.png)**

客户端在接收以上信息后，使用CryptoAsymmetricEncrypt函数加密密码，该函数如下所示：

**![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_8-300x149.png)**

使用python描述password\_info生成算法：

**![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_9-300x33.png)**

* RSA加密使用的是PKCS1\_OAEP，其中的哈希算法为SHA256。
* XOR算法是简单的逐位异或算法。

最后，客户端再次通过CmpDevice的2号服务ID下发到PLC中：

![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_10-300x229.png)

如果密码正确的话将会返回app key，每次进行操作都需要携带该授权key。

**![](https://blog.nsfocus.net/wp-content/uploads/2023/01/wps_doc_11-300x185.png)**

## ****四、总结****

通过研究CodeSys V3的密码存储算法以及授权登录算法，分析实现机制，总结出了离线爆破codesys v3 密码哈希的方法，同时发现该授权流程存在中间人攻击的可能性，建议开启CodeSys V3的TLS通信协议，保护通信数据安全，提升破解难度。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/irpf2-0/)

[Next](https://blog.nsfocus.net/microsoft/)

### Meet The Author

陈杰

工业物联网安全实验室

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)