---
title: 浅析JWT Attack
url: https://www.secpulse.com/archives/193450.html
source: 安全脉搏
date: 2022-12-15
fetch_date: 2025-10-04T01:31:02.001682
---

# 浅析JWT Attack

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

# 浅析JWT Attack

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-14

14,032

# 前言

在2022祥云杯时遇到有关JWT的题，当时没有思路，对JWT进行学习后来对此进行简单总结，希望能对正在学习JWT的师傅们有所帮助。

# JWT

JWT，即`JSON WEB TOKEN`，它是一种用于通信双方之间传递安全信息的简洁的、URL安全的表述性声明规范，是一种标准化的格式，用于在系统之间发送经过加密签名的JSON数据，·理论上可以包含任何类型的数据，但最常用于发送关于用户的信息（“声明”），以进行身份认证、会话处理和访问控制。

简单了解了它的定义后，我们接下来来看一下JWT的组成部分 它分为三个部分，如下所示

```
1、Headers:头部
2、Payload:有效载荷
3、Signature:签名
```

这三个部分以`.`符号来连接，所以JWT的格式通常是`xxx.yyy.zzz`这种样子

## Headers

`Headers`通常由两部分组成，`令牌的类型`和`签名算法`，常见的算法有很多种，例如 `HMAC SHA256` 或 `RSA`。但它也还有一个`kid`参数，这是一个可选参数，全称是`key ID`，它用于指定加密算法的密钥。

示例如下

```
ewogICJhbGciOiAiSFMyNTYiLAogICJ0eXAiOiAiSldUIgp9
```

这就是一个`Headers`，当我们对它进行Base64解码就可以看到它的具体内容，具体如下

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

`alg`指的就是算法，这里的算法就是`HS256`，`typ`指的是令牌类型。这里需要说明一点，就是明文在加密时其实采用的是`Base64URL`加密，这种加密方式并非`Base64encode`+`URLencode`，而是对一些特殊字符进行了替换，具体说明如下

> JWT 作为一个令牌(token)，有些场合可能会放到 URL(比如 api.example.com/?token=xxx)。Base64有三个字符+、/和=，在 URL 里面有特殊含义，所以要被替换掉：=被省略、+替换成-，/替换成\_ 。这就是 Base64URL 算法。

## Payload

有效载荷就是存放有效信息的地方，其中包含声明。声明包含三个部分 1、**已注册声明** 这个部分的话就是已经预先定义过的声明，常见的声明主要有以下几种

```
iss: jwt签发者
sub: jwt所面向的用户
aud: 接收jwt的一方
exp: jwt的过期时间，这个过期时间必须要大于签发时间
nbf: 定义在什么时间之前，该jwt都是不可用的.
iat: jwt的签发时间
jti: jwt的唯一身份标识，主要用来作为一次性token,从而回避重放攻击。
```

2、**公共的声明** 这些可以由使用 JWT 的人随意定义，一般用于添加用户的相关信息或其他业务需要的必要信息。但不建议添加敏感信息，因为该部分在客户端可进行解码. 3、**私有的声明** 这些是为在同意使用它们的各方之间共享信息而创建的自定义声明，私有声明是提供者和消费者所共同定义的声明，一般不建议存放敏感信息。

示例如下

```
ewoJInN1YiI6ICJhZG1pbiIsCiAgICAidXNlcl9yb2xlIiA6ICJhZG1pbiIsCiAgICAiaXNzIjogImFkbWluIiwKICAgICJpYXQiOiAxNTczNDQwNTgyLAogICAgImV4cCI6IDE1NzM5NDAyNjcsIAogICAgIm5iZiI6IDE1NzM0NDA1ODIsIAogICAgImp0aSI6ICJkZmY0MjE0MTIxZTgzMDU3NjU1ZTEwYmQ5NzUxZDY1NyIgICAKfQ
```

进行`base64URL`解码，结果如下

```
{
    "sub": "admin",    //jwt所面向的用户
    "user_role" : "admin",     //当前登录用户
    "iss": "admin",           //该JWT的签发者,有些是URL
    "iat": 1573440582,        //签发时间
    "exp": 1573940267,        //过期时间
    "nbf": 1573440582,        //该时间之前不接收处理该Token
    "jti": "dff4214121e83057655e10bd9751d657"   //Token唯一标识
}
```

## Signature

由于头部和有效载荷以明文形式存储，因此，需要使用签名来防止数据被篡改。所以这部分是一个签证信息，这个签证信息由三部分组成

```
1、header (base64URL编码)
2、payload (base64URL编码)
3、secret（密钥）
```

它的计算方式如下

```
Signature=HMACSHA256(base64UrlEncode(header) + "." +base64UrlEncode(payload),secret)
//假设这里是HS256算法，如果是其他算法的话开头设置为其他算法即可
```

现在了解了JWT的大致作用和其组成，接下来来学习一下JWT攻击。

# JWT 攻击

JWT攻击有多种情况，现在来对其进行逐一讲解。

## 敏感信息泄露

> JWT保证的是数据传输过程中的完整性而不是机密性。

因为JWT的`payload`部分是使用`Base64url`编码的，所以它其实是相当于明文传输的，当`payload`中携带了敏感信息时，我们对`payload`部分进行`Base64url`解码，就可以读取到`payload中`携带的敏感信息。

### 靶场演示

题目链接https://www.ctfhub.com/#/skilltree 题目描述如下

> JWT 的头部和有效载荷这两部分的数据是以明文形式传输的，如果其中包含了敏感信息的话，就会发生敏感信息泄露。试着找出FLAG。格式为 flag{}

进入环境后发现一个登录框

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193450-1670996182.png "null")

随便输入账号密码，登录后发现界面如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193450-16709961821.png "null")

查看此时的JWT

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193450-1670996183.png "null")

想到题目中说头部和载荷可能会有敏感泄露，将值取出分别进行`Base64URL`解码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193450-16709961831.png "null")

两处拼接一下，得到`ctfhub{bb89d985db8cea6a2f2d34cb}`

## 算法修改攻击

首先来简述一下JWT中两个常用的加密算法

> HMAC(HS256):是一种对称加密算法，使用秘密密钥对每条消息进行签名和验证 RSA(RS256)：是一种非对称加密算法，使用私钥加密明文，公钥解密密文。

从上面不难看出，`HS256`自始至终只有一个密钥，而`RS256`是有两个密钥的。在通常情况下，`HS256`的密钥我们是不能取到的，`RS256`的密钥也是很难获得的，`RS256`的的公钥相对较容易获取，但无论是`HS256`加密还是`RS256`加密，都是无法实现伪造JWT的，但当我们修改`RSA256`算法为`HS256`算法时，后端代码会使用公钥作为密钥，然后用`HS256`算法验证签名，如果我们此时有公钥，那么此时我们就可与实现JWT的伪造。

### 靶场演示

题目链接https://www.ctfhub.com/#/skilltree

题目描述

> 有些JWT库支持多种密码算法进行签名、验签。若目标使用非对称密码算法时，有时攻击者可以获取到公钥，此时可通过修改JWT头部的签名算法，将非对称密码算法改为对称密码算法，从而达到攻击者目的。

进入环境后发现题目代码

```
class JWTHelper {
  public static function encode($payload=array(), $key='', $alg='HS256') {
    return JWT::encode($payload, $key, $alg);
  }
  public static function decode($token, $key, $alg='HS256') {
    try{
            $header = JWTHelper::getHeader($token);
            $algs = array_merge(array($header->alg, $alg));
      return JWT::decode($token, $key, $algs);
    } catch(Exception $e){
      return false;
    }
    }
    public static function getHeader($jwt) {
        $tks = explode('.', $jwt);
        list($headb64, $bodyb64, $cryptob64) = $tks;
        $header = JWT::jsonDecode(JWT::urlsafeB64Decode($headb64));
        return $header;
    }
}

$FLAG = getenv("FLAG");
$PRIVATE_KEY = file_get_contents("/privatekey.pem");
$PUBLIC_KEY = file_get_contents("./publickey.pem");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!empty($_POST['username']) && !empty($_POST['password'])) {
        $token = "";
        if($_POST['username'] === 'admin' && $_POST['password'] === $FLAG){
            $jwt_payload = array(
                'username' => $_POST['username'],
                'role'=> 'admin',
            );
            $token = JWTHelper::encode($jwt_payload, $PRIVATE_KEY, 'RS256');
        } else {
            $jwt_payload = array(
                'username' => $_POST['username'],
                'role'=> 'guest',
            );
            $token = JWTHelper::encode($jwt_payload, $PRIVATE_KEY, 'RS256');
        }
        @setcookie("token", $token, time()+1800);
        header("Location: /index.php");
        exit();
    } else {
        @setcookie("token", "");
        header("Location: /index.php");
        exit();
    }
} else {
    if(!empty($_COOKIE['token']) && JWTHelper::decode($_COOKIE['token'], $PUBLIC_KEY) != false) {
        $obj = JWTHelp...