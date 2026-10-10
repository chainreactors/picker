---
title: RSA常见题型
url: https://mp.weixin.qq.com/s/vaZwvQzSO4uFmAxyKMuJeg
source: Doonsec's feed
date: 2026-10-09
fetch_date: 2026-10-10T07:55:37.951777
---

# RSA常见题型

# RSA常见题型

原创

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# RSA-总结

这里我们总结一下，各个RSA题目的题型

# 1、基础RSA

一般最简单的RSA，就是会给出n,c,p,q,e

我们需要求得就是m，把数值转成字符就是需要的答案

我们需要根据这些公式

phi=(p-1)\*(q-1)
ed=1 mod phi 求d
m=c^d mod n
转化成脚本就是
phi=(p-1)\*(q-1)
d=pow(e,-1,phi)
m=pow(c,d,n)

# 2、dp，dq泄露问题

dp=d mod(p-1)

dq=d mod (q-1)

遇到的题型可能有两种

·只有dp泄露

·dp，dq同时泄露（和dp泄露一样的解法，dq好像没有什么用）

推导

dp=d mod (p-1)
dp=d+k(p-1)
d=dp-k(p-1)
ed=1 mod phi
ed=1+a\*phi
phi=(p-1)\*(q-1)
e\*(dp-k(p-1))=1+a\*(p-1)\*(q-1)
e\*dp=1+a\*(p-1)\*(q-1)+e\*k(p-1)
e\*dp=1+(p-1)\*(a\*(q-1)+ek)
e\*dp=1 mod(p-1)
所以e\*dp=1+k(p-1)
只需要通过爆破把p求出来就行
temp=e\*dp
for k in range(1,e):
    if (temp-1)%k==0:
        x=((temp-1) //k) +1
    if n%x:
        p=x
        break
通过这个求出p，再按常规解法就行

# 3、公钥解析，签名加密

这种题目给的附件一般就是

·一个公钥（.pem/.key)

·已经加密之后的flag.enc文件（通常是base64格式，也又可能是多个这个加密的文件组成的flag）

遇到这种题目我们一般的做题步骤就是

·通过kali中openssl工具解出n，e

openssl rsa -pubin -text -modulus -in 公钥文件

这个时候的到的n是16进制，我们需要转换成整数

n=int("xxx",16)
print(n)

把得到的n用yafu进行爆破得到p，q

yafu "factor(……)"

这里如果是普通的rsa，密文长度很短，把flag.enc进行base64解密得到的就是c，然后再按照传统解法得到m

但是如果密文长度很长256，那么可能用的就是OAEP这种填充方式，我们就需要在上面的基础上构造密钥信息

from Crypto.Cipher import PKCS1\_OAEP  #需要引入这两个模块
from Crypto.PublicKey import RSA
……
key\_info=RSA.construct((n, e, d, p, q))
key=PKCS1\_OAEP.new(key\_info)
flag=key.decrypt(c)

# 4、低解密指数攻击 \*

也称作维纳攻击

d小

m=cd mod n，这里e就远大于65537，e看起来特别大，且d直接求不了

可以通过连分数展开e/n来恢复出d

由ed-kφ(n)=1可以得到e/φ(n) - k/d = 1/(d·φ(n))

由于φ(n)约等于n，所以k/d ≈ e/n。而且误差 1/(d·φ(n)) < 1/(2d²)，根据连分数理论，k/d 必定是 e/n 连分数展开的一个收敛子。因此枚举 e/n 的所有收敛子，就能找到真正的 k/d。

import ContinuedFractions, Arithmetic
def hack\_RSA(e,n):
    \_, convergents = ContinuedFractions.rational\_to\_contfrac(e, n) #获取连分数收敛子
    for (k,d) in convergents: #遍历每个候选
        if k!=0 and (e\*d-1)%k == 0:
            phi = (e\*d-1)//k
            s = n - phi + 1
            discr = s\*s - 4\*n #二次方程遍历p，q是否为整数
            if(discr>=0):
                t = Arithmetic.is\_perfect\_square(discr)
                if t!=-1 and (s+t)%2==0:
                    return d

获得d之后就按照常规解法了

# 5、低加密指数攻击

低加密指数攻击就是e很小

如果是简单的，c=m^e mod n

e很小，远小于n，就可以直接对c进行开根号得到m

一般会结合广播攻击（多个n，多个c），低加密指数广播攻击需要用中国剩余定理CRT来解

根据中国剩余定理
M=n1\*n2\*n3……\*n9
mi=M //n[i]  i在1到9
mi\*yi==1mod n[i] ，yi是mi模ni的逆元
接下来我们就可以根据这个来推导
因为c=m^e mod n
所以m^e =c mod n
x+=c[i]\*mi\*yi  ,这里是中国剩余定理的概念已知x=c[i] mod n[i]那么x+=c[i]\*mi\*yi
x=x %M
再对x进行开根号得到m

# 6、公约数求解

这个公约数求解，就是公用p，一般会给出多个n，c，e（低加密指数攻击只能是一个e）

因为公用p所以p=gmpy2.gcd(n1,n2) (前提是n1，n2不互素）

再常规解法

# 7、共模攻击

共模攻击就是n相同，e和c不一样

这里重要的就是两个结论

m=c1^s1 \*c2^s2 mod n
e1s1+e2s2=1
这里要用扩展欧几里得算法\_,s1,s2=gmpy2.gcdext(e1,e2)把e1s1+e2s2=1表示出来
m=c1^s1 \*c2^s2 mod n这里也是要用m=(pow(c1,s1,n)\*pow(c2,s2,n)) %n
这里就不需要求d了

# 8、费马分解

这种在题目中就会经常看到q=nextprime(q)

q-p过小，这种题目需要自己定义费马函数

n=p\*q
令a=(p+q)/2 ,b=(p-q)/2
那么n=a^2 -b^2
a^2 -n=b^2
也就是说找到一个a使a^2 -n是一个完全平方数,a肯定使是大于等于n开平方的（b很小）
所以用费马分解直接爆破出p=a+b,q=a-b

from math import isqrt
def fermat\_factor(n):
    a=isqrt(n)#初始化a，a必须满足a方大于n
    if a\*a      <n:
        a+=1
    while true:
        b2=a\*a -n
        b=isqrt(b2)
        if b\*b==b2: #这里必须要验证一下b2是否完全平方
            p=a+b
            q=a-b
            return p,q
        a+=1 #如果没有a必须再加

        </n:

得到p，q后常规求解

# 9、光滑数

一般分为

·p-1光滑

·p+1光滑

光滑数：一个整数，如果它的所有质因子都不超过某个界限p，，那就称p-光滑数

p-1光滑数指的是p-1这个数是光滑的

p-1光滑需要用到费马小定理

p-1核心思想

对质数p，若gcd(a,p)=1,根据费马小定理a^(p-1)=1mod p
对任意倍数m(p-1的倍数) ，a^m =1 mod p ,所以a^m -1就是p的倍数
因为n是p的倍数
所以gcd(a^m -1,n)=p
关键就是我们需要构造一个m使得它是p-1的倍数，同时不是q-1的倍数，就可以通过求gcd得到p
因为p-1光滑，我们就可以用所有小质数的幂的乘积去覆盖p-1

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib8dofAJGw4FugyeXvabRozBUqH31pE4XVFfKVL5naia8szL8I5uovQjd1hERQMSk2YKbknyOyZhtE4zht1re7A6qvHibwHItjqUQ/640?wx_fmt=png)

只要B足够大(大于p-1的最大因子），M就会是p-1的倍数
算法步骤
1. 选一个与 n 互素的 a（通常取 2）。
2. 令 m = 2，计算 a = a^m mod n。
3. 计算 p=gcd(a-1, n)。
4. 若得到p非平凡因子（≠1 且 ≠n），成功。
5. 否则 m += 1，重复。
解题脚本
a = 2
m = 2
while True:
    a=pow(a,m,n)
    p=gmpy2.gcd(a-1,n)
    if p!=1 and p!=n:
        break
    m +=1

p+1核心思想

lucas序列定义

V k =a^k +b^k -->V k =aV(k-1) -V k-2

取k=p+1

V p+1 =a^(p+1）+b^（p+1)

这里有个结论a^(p+1)=1,b^(p+1)=1

所以V p+1 =2

在模p的意义下V p+1 =2 mod p

V p+1 -2就是p的倍数

p=gcd(V p+1 -2,n)

算法步骤

1、选取一个整数a，通常取3

2、构造lucas序列，满足

v 0 =2，v 1 =a，V k =aV(k-1) -V k-2

3、选择m，使m是很多小质数幂的乘积，要覆盖p+1

4、V m =2 mod p

5、p=gcd(V m -2,n)

6、如果 p≠1且 p≠n，则成功分解

a = 3
m = 2
while True:
    a= pow(a, m, n)
    p = gmpy2.gcd(a - 2, n)
    if p != 1 and p != n:
        break
    m += 1

# 10、e 与 φ(n) 不互素

正常的rsa需要满足e，phi互质，满足这个条件可以按照正常的rsa解法来求

因为ed=1 mod phi

如果e，phi不互质的话，那么就求解不出来d

但是如果t=gcd(e,phi)，在t很小，m可开方的情况下是可以解出来的

需要重新构造一个e

t=gmpy2.gcd(e,phi)
if t !=1:
    e2=e//t
    d = pow(e2, -1, phi)
    m = pow(c, d, n)
    m2=gmpy2.iroot(m,t)[0]

这时候得到的m2才是我们需要得到的

# 11、 已知高位 / 低位攻击（Coppersmith）

核心一句话：如果知道一个模N的多项式方程的一个小根，可以用格基化把它求出来

如果存在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicIR2b9cZg0A4Ksxjk5iaGkKj5DUSds9z4esVg9BAC72vaNDP5f48xWkKBJOicYjoia9Y0H13eaDcCicQCVVuCDbmQd8O43D3mzibv4/640?wx_fmt=png)

满足这两个条件就可以把x0求出来

例如：

m的高位：m=m0 +x,m0已知，x未知但很小

m的低位：m=x \*2 k +m0，m0已知，x未知但很小

这两种都是求一个小未知量x

已知高位：

因为c =m^e mod n

所以(m0 +x)^e =c mod n

令f(x)=(m0 +x)^e -c

x就是f(x)=0 mod n的一个根，从而恢复m

同理已知低位也是这样

SageMath里面内置了coppersmith的小根方法

R.= PolynomialRing(Zmod(N)) #X是x的上界
f = (m0 + x)^e - c
f = f.monic() #确保最高项系数为1
roots = f.small\_roots(X=2^k, beta=1)  #X是x的上界,beta是因子大小参数，通常取1
if roots:
    x0=roots[0] #返回找到的小根列表第一个，通常只有第一个或者只有第一个为合法明文
    m=m0+x

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过