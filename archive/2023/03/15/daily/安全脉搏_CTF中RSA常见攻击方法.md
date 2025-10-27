---
title: CTF中RSA常见攻击方法
url: https://www.secpulse.com/archives/197505.html
source: 安全脉搏
date: 2023-03-15
fetch_date: 2025-10-04T09:33:49.715824
---

# CTF中RSA常见攻击方法

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

# CTF中RSA常见攻击方法

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-14

17,149

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785634.png)

## 1.RSA原理

### 简介

RSA是一种非对称加密算法，是被研究得最广泛的公钥算法，从提出到现在已近三十年，经历了各种攻击的考验，逐渐为人们接受，普遍认为是目前最优秀的公钥方案之一。

### 加密过程

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785635.png)

### 字母符号含义

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785636.png)

### python解密RSA

```
import gmpy2
from Crypto.Util.number import bytes_to_long,long_to_bytes

p =
q =
e =
c =

n = p * q
phi_n = (p-1)*(q-1)
d = gmpy2.invert(e, phi_n)
m = pow(c, d, n)
print(long_to_bytes(m))
```

## 2.常见攻击方法

### 直接分解n

（1）网站在线分解n：http://factordb.com/

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785637.png "null")

（2）工具yafu分解n 下载：https://sourceforge.net/projects/yafu/ 常用命令`factor(n)`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785638.png "null")

如果报错mismatched parens，是因为n太长不能直接输入，可以把n放到txt文件里，使用命令`yafu-x64.exe "factor(@)" -batchfile rsa.txt`分解n，如果报错eof; done processing batchfile，打开txt再最后加个换行即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785640.png "null")

### 共模攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785642.png)

 具体题目中python代码如下：

```
import gmpy2
from Crypto.Util.number import bytes_to_long,long_to_bytes

n = 22708078815885011462462049064339185898712439277226831073457888403129378547350292420267016551819052430779004755846649044001024141485283286483130702616057274698473611149508798869706347501931583117632710700787228016480127677393649929530416598686027354216422565934459015161927613607902831542857977859612596282353679327773303727004407262197231586324599181983572622404590354084541788062262164510140605868122410388090174420147752408554129789760902300898046273909007852818474030770699647647363015102118956737673941354217692696044969695308506436573142565573487583507037356944848039864382339216266670673567488871508925311154801
c1 = 22322035275663237041646893770451933509324701913484303338076210603542612758956262869640822486470121149424485571361007421293675516338822195280313794991136048140918842471219840263536338886250492682739436410013436651161720725855484866690084788721349555662019879081501113222996123305533009325964377798892703161521852805956811219563883312896330156298621674684353919547558127920925706842808914762199011054955816534977675267395009575347820387073483928425066536361482774892370969520740304287456555508933372782327506569010772537497541764311429052216291198932092617792645253901478910801592878203564861118912045464959832566051361
e1 = 11187289
c2 = 18702010045187015556548691642394982835669262147230212731309938675226458555210425972429418449273410535387985931036711854265623905066805665751803269106880746769003478900791099590239513925449748814075904017471585572848473556490565450062664706449128415834787961947266259789785962922238701134079720414228414066193071495304612341052987455615930023536823801499269773357186087452747500840640419365011554421183037505653461286732740983702740822671148045619497667184586123657285604061875653909567822328914065337797733444640351518775487649819978262363617265797982843179630888729407238496650987720428708217115257989007867331698397
e2 = 9647291
r,s1,s2 = gmpy2.gcdext(e1,e2)
m = (pow(c1,s1,n) * pow(c2,s2,n)) % n
print(long_to_bytes(m))
```

### 低加密指数攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-16787856421.png)

具体题目中python代码如下：

```
import gmpy2
from Crypto.Util.number import bytes_to_long,long_to_bytes

def di(c, e, n):
    k = 0
    while True:
        me = c + n*k
        flag, result = gmpy2.iroot(me, e)
        if result == True:
            return flag
        k += 1
n = int('52d483c27cd806550fbe0e37a61af2e7cf5e0efb723dfc81174c918a27627779b21fa3c851e9e94188eaee3d5cd6f752406a43fbecb53e80836ff1e185d3ccd7782ea846c2e91a7b0808986666e0bdadbfb7bdd65670a589a4d2478e9adcafe97c6ee23614bcb2ecc23580f4d2e3cc1ecfec25c50da4bc754dde6c8bfd8d1fc16956c74d8e9196046a01dc9f3024e11461c294f29d7421140732fedacac97b8fe50999117d27943c953f18c4ff4f8c258d839764078d4b6ef6e8591e0ff5563b31a39e6374d0d41c8c46921c25e5904a817ef8e39e5c9b71225a83269693e0b7e3218fc5e5a1e8412ba16e588b3d6ac536dce39fcdfce81eec79979ea6872793',16)
e = int('3',16)
c = int('10652cdfaa6b63f6d7bd1109da08181e500e5643f5b240a9024bfa84d5f2cac9310562978347bb232d63e7289283871efab83d84ff5a7b64a94a79d34cfbd4ef121723ba1f663e514f83f6f01492b4e13e1bb4296d96ea5a353d3bf2edd2f449c03c4a3e995237985a596908adc741f32365',16)
m = di(c,e,n)
print(long_to_bytes(m))
```

### 低加密指数广播攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197505-1678785643.png)

具体题目中python代码如下：

```
import gmpy2
from functools import reduce
from Crypto.Util.number import bytes_to_long,long_to_bytes

def CRT(c,n):
    sum = 0
    # ni 的乘积,N=n1*n2*n3
    N = reduce(lambda x,y:x*y,n)
    # zip()将对象打包成元组
    for n_i, c_i in zip(n,c):
        N_i = N // n_i
        t_i = gmpy2.invert(N_i,n_i)
        sum += c_i * N_i * t_i
    return sum % N

n1 = 3313103242120000300202143122442322224001424104234131044411402030032430021043332142020312022124034002200312021423224341041431042442412142044444433230002441301220224223102011044110440301133023230141013312143032233124024304024044130332431321010104222401331222...