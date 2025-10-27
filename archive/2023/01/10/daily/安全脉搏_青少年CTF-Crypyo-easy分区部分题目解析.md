---
title: 青少年CTF-Crypyo-easy分区部分题目解析
url: https://www.secpulse.com/archives/194741.html
source: 安全脉搏
date: 2023-01-10
fetch_date: 2025-10-04T03:22:38.389458
---

# 青少年CTF-Crypyo-easy分区部分题目解析

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

# 青少年CTF-Crypyo-easy分区部分题目解析

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2023-01-09

19,355

# Crypto-easy

**1.BASE**

拿到附件用cyberchef自动解码得到flag  [![125407gy1rpo3y7myzoo7z.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/125407gy1rpo3y7myzoo7z-1024x364.png "125407gy1rpo3y7myzoo7z-1024x364.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/125407gy1rpo3y7myzoo7z.png)

**2.basic-crypto**

拿到附件发现是一串01的数字，这时候想到二进制转换  [![125658p1p66ufttcvf66pg.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/125658p1p66ufttcvf66pg-1024x746.png "125658p1p66ufttcvf66pg-1024x746.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/125658p1p66ufttcvf66pg.png)

然后base64在线解码

[![125957anen33jgt9z6sczj.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/125957anen33jgt9z6sczj-1024x630.png "125957anen33jgt9z6sczj-1024x630.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/125957anen33jgt9z6sczj.png)

接着根据提示想到凯撒密码解密

[![130144gjysv65ykyzxyz7z.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130144gjysv65ykyzxyz7z-1024x540.png "130144gjysv65ykyzxyz7z-1024x540.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130144gjysv65ykyzxyz7z.png)

最后通过字频查找找到flag

**3.CheckIn**

先用base64解码

[![130526l6bjbzz52jzcj57q.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130526l6bjbzz52jzcj57q-1024x528.png "130526l6bjbzz52jzcj57q-1024x528.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130526l6bjbzz52jzcj57q.png)

再用ROT47解码得到flag

[![130608h7bluh0fquq99vhu.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130608h7bluh0fquq99vhu-1024x448.png "130608h7bluh0fquq99vhu-1024x448.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130608h7bluh0fquq99vhu.png)

**4.childRSA**

先用[factordb](http://factordb.com/)分解N

[![130956k9r7r71d9b4db179.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130956k9r7r71d9b4db179-1024x288.png "130956k9r7r71d9b4db179-1024x288.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/130956k9r7r71d9b4db179.png)

然后套用脚本得到flag

```
from Crypto.Util.number import *
import gmpy2
n =
c =
e=
p=
q=
phi = (p-1)*(q-1)
d=gmpy2.invert(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
```

**5.crypto-classic1**

[![131339jrxzoxsy2t8xkxst.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/131339jrxzoxsy2t8xkxst.png "131339jrxzoxsy2t8xkxst.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/131339jrxzoxsy2t8xkxst.png) 查看附件根据提示知道这是键盘密码，低下头望着手中的键盘若有所思，你会发现每一组用空格隔开的字母串在键盘上连起来都围着一个字母，这时候把五个字母连起来你会得到一个五位数的压缩包密码 拿到压缩包附件，根据第二层提示维吉尼亚密码，查看维吉尼亚表格找到密钥进行解密得到最后flag

[![131743e893k9df9e3lapay.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/131743e893k9df9e3lapay-1024x402.png "131743e893k9df9e3lapay-1024x402.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/131743e893k9df9e3lapay.png)

**6.NO SOS**

拿到附件发现是一堆-和. 将他们替换成A和B（因为比较少所以建议手动替换） 然后根据提示培根密码解密得到flag

[![132321dzl0jjqt0rleb4ir.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/132321dzl0jjqt0rleb4ir-1024x405.png "132321dzl0jjqt0rleb4ir-1024x405.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/132321dzl0jjqt0rleb4ir.png)

**7.一起下棋**

根据提示下棋，推测是棋盘密码，进行解密得到flag

[![132508sarji7v5vnn6jooa.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/132508sarji7v5vnn6jooa-1024x465.png "132508sarji7v5vnn6jooa-1024x465.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/132508sarji7v5vnn6jooa.png)

**8.Morse**

根据提示先用Morse密码进行解密，然后16进制转换文本得到flag [![132744tqlr8x88o8l22r29.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/132744tqlr8x88o8l22r29-1024x293.png "132744tqlr8x88o8l22r29-1024x293.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/132744tqlr8x88o8l22r29.png)

**9.爱丽丝的兔子**

根据提示兔子我们猜测这是rabbit解密，得到一堆核心价值观

[![133239o33ade2idleod2lr.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/133239o33ade2idleod2lr-1024x206.png "133239o33ade2idleod2lr-1024x206.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/133239o33ade2idleod2lr.png)

然后这就很明显了，接着用核心价值观解密 又根据提示得知是栅栏密码解密，栅栏数为6得到最终flag（有些网站解不出来最好多解几次）

**10.Relayb64**

直接base64换表得到flag

[![134528a88g5r3z1fqb48rs.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/134528a88g5r3z1fqb48rs-1024x400.png "134528a88g5r3z1fqb48rs-1024x400.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/134528a88g5r3z1fqb48rs.png)

**11.ABBB**

拿到一堆AB字符先把AB转成-和. [![150450ckta57v88f7005ov.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/150450ckta57v88f7005ov-1024x654.png "150450ckta57v88f7005ov-1024x654.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/150450ckta57v88f7005ov.png)

然后morse解密一下

[![150530ctnza2y56n13n5hn.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/150530ctnza2y56n13n5hn-1024x410.png "150530ctnza2y56n13n5hn-1024x410.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/150530ctnza2y56n13n5hn.png)

然后放在字频分析里查flag，找到FLAG IS的样式，改掉大小写得到flag

[![150724irbrebtub7h2uh7h.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com...