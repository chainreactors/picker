---
title: CTFPlus逆向每周练习-冲刺！偷摸零！、only_flower、CTF+Binary练习题-Re-Day7、CTF+Binary练习题-Re-Day11、CTF+Binary练习题-Re-Day5
url: https://mp.weixin.qq.com/s/gj2ggdGuPVTXklhXWtKT_g
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:00:58.448038
---

# CTFPlus逆向每周练习-冲刺！偷摸零！、only_flower、CTF+Binary练习题-Re-Day7、CTF+Binary练习题-Re-Day11、CTF+Binary练习题-Re-Day5

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4a0MMkxrzyXnu875sgibUJaW61xZ4hicqvSRe3Qbj9y4goLS7TDAjqjLPtCBuiaB7nIX0aCwIQqYk2Xv7pkHjFY7JhhjelRHEwiaPM/0?wx_fmt=jpeg)

# CTFPlus逆向每周练习-冲刺！偷摸零！、only\_flower、CTF+Binary练习题-Re-Day7、CTF+Binary练习题-Re-Day11、CTF+Binary练习题-Re-Day5

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4a2urlNYaqLe5Q7I1b5ibu8QYQT6x0ic6qddxice6pI3jX9PPQtVvWUxJPrjDkEsOicjkqAicIcmhKsU4g6tKmnicAIdFzeNQBLfO1Lo/640?wx_fmt=png&from=appmsg)

# 1. 冲刺！偷摸零！

下载题目附件，是一个跑酷游戏的jar包，使用jd-gui打开查看，发现里面有一个sqlite数据库：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YnyRibEof4U4IYJpnjxiaB91kR30TicgXgicEt5QYc1ZBNmZ2O7laz8UjT8faRWNK7EHqcePvSYXsiaxgIkic4panM5PTBibhgNrfTmM/640?wx_fmt=png&from=appmsg)

导出后使用打开查看，找到了flag的第一部分：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Y9moEr7T9P1kUZgWchdxU2x9uAjnfA7dvxX0843hQW98yXICFde9qDNiaBiaQMEdrUE5QpZFKU1tiakvNKEpiaQDsTIyBwIM29eFU/640?wx_fmt=png&from=appmsg)

这里其实就是在登录页面的代码逻辑那里使用了SQL语句拼接，有sql注入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bWC0rUOBSaoOwlf4wz5CwIetSFTmVhiciclX4z7aqwHg8osR1kTr42HvDeaQoxHJpQ3dSziaG3VE0FIq7zQcOJ9V63lPR87tib4ibU/640?wx_fmt=png&from=appmsg)

第二部分的flag在GameOverView，查看代码发现加密逻辑是一个简单的异或：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YAJ9WQkSxicjNvCFYDr0MpibU9SBaD8v5YKzlxUuOiacjOx8Owmiaj5LWaIrNycTbd4AcSiazBHgABxCedCWLd4o6h3XKiaEl7BwbdA/640?wx_fmt=png&from=appmsg)

python脚本解密：

```
if __name__ == '__main__':    encrypted = [        5, 20, 7, 1, 103, 111, 10, 28, 10, 22,        52, 59, 10, 0, 38, 48, 10, 22, 16, 10,        29, 48, 39, 48, 116, 40]    key = 85    flag = ''    for i in range(len(encrypted)):        flag+= chr((encrypted[i] ^ key) & 0xff)    print(flag)
```

输出成功得到第二部分的flag：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4a5RMXqSia8aTqUQMhv74IebPHN8XS2Dyl8n4vkZJMAiczrnLdhtibR9HLTc8MrUXFXlhgwWKb8bYa07TgCkShzzPeu2prz2icmU6U/640?wx_fmt=png&from=appmsg)

拼接即可。

# 2. only\_flower

下载题目附件，是一个PE可执行程序，使用IDA静态分析找到主函数，发现被花指令混淆，里面有很多EB FF C0 48的无用指令，把这些都patch成nop，然后修改main函数的结束地址重新分析即可成功反编译成伪代码：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YicKv4Ebj5CpUicOQyvnbrnZ6e4oQgcEibaEHlPFnmKEOtxF1icpPnKtHicD3JhAciatThevRsCajGl9IWVVK7F5IJFUpeic5qOydh5s/640?wx_fmt=png&from=appmsg)

接收到用户输入的字符串后，调用checkcheck函数，进入checkcheck函数查看，发现也被花指令混淆：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bnxDrJCeowPdjH6F4KnNyw85zgZMiavzHNfam2CDrTVFCJf7rzJvD9TPibzTXpRkRJA5DWSf6L77XXpte4Qmc052KPlFFwzKPv8/640?wx_fmt=png&from=appmsg)

依旧修改无用的短跳转为nop重新分析，可以看到是判断flag格式的：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZfcvXHzsDWXKwVSAjwKgp3iam936esGZXJM9dWBIhNicVBGcdQBicoS8eqzG2epHutku5aYxTPt4icJXAb6PEkny2D8uDmskL5LIo/640?wx_fmt=png&from=appmsg)

然后调用encrypt加密函数，还是花指令，继续nop修改后F5分析：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4alDEQPbbD5k5tuuQzujXN7Fanz1k4Jcu8pTJ9359EiaxaSS8WwBc2JibsXzmOPAAeNlib3RHRN1z7YMyvqgsRKvTeO6M2UmaT9Lw/640?wx_fmt=png&from=appmsg)

针对每位根据key做rol8函数操作，再查看rol8函数：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aD9jgZG8pWF2L5TDhWp1dicoH8F5Y5C6qWbD3Spkib8Ula0BwNNClt5d9qrriakn6xAjU1ia1SlCSCScScJrad12cdiaW6uSRIfPnQ/640?wx_fmt=png&from=appmsg)

最后再跟正确的密文做比较，密文和key分别为：

```
key：GEEK2025cipher：0A 84 C2 84 51 48 5F F2  9E 8D D0 84 75 67 73 8FCA 57 D7 E6 14 6E 77 E2  29 FE DF CC
```

制作python脚本解密：

```
def rol8(b, n):    return (b << (8 - n)) & 0xff | (b >> n) & 0xffif __name__ == '__main__':    cipher = [0x0A,0x84,0xC2,0x84,0x51,0x48,0x5F,0xF2,0x9E,0x8D,0xD0,0x84,0x75,0x67,0x73,0x8F,0xCA,0x57,0xD7,0xE6,0x14,0x6E,0x77,0xE2,0x29,0xFE,0xDF,0xCC]    flag_len = len(cipher)    key_str = "GEEK2025"    k_len = len(key_str)    flag = ""    key = [ord(c) for c in key_str]    for i in range(flag_len):        tmp = rol8((cipher[i] - i) & 0xff, ord(key_str[i % k_len]) & 7)        flag += chr(tmp ^ key[i % k_len])    print(flag)
```

输出得到flag：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YaIArU5SzJKCJlDaObaUM3RaXiaicL79MRpTicwk7uWrS98enpm63OWkViat5oVzQRv7sUNOS7G3czWEwPp6TYtNwrib27dXAMGibV0/640?wx_fmt=png&from=appmsg)

# 3. CTF+Binary练习题-Re-Day7（1）[Score=2]

下载题目附件，使用ida打开静态分析，找到主函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4blUqz00ujzslsOtUg93gdPToI8P90tYBQfZJSu7qSuTH5PYTnicYVnWicQXlqaLvnmuh1bdTpFJpbS4UrHiag9icyQdiaqDXPciaBeU/640?wx_fmt=png&from=appmsg)

这里首先读取输入的字符串，然后调用sub\_140001110查看格式，然后提取大括号中间的字符串使用两个加密函数加密，分别是sub\_1400011c0和sub\_1400012e0，首先分析sub\_1400011c0：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZtF6gzeMmhoRgnWibVWlBhGMYjvjichMznaD7vPea1ACd1IbICpHJp1ugP7u8Zpd8AomPlpibFfJ5Jtemg0gg6yMOPzJrgjEE46A/640?wx_fmt=png&from=appmsg)

一个异或加密，v8的值随加密变化，接下来查看sub\_1400012e0加密函数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZnYVZrzk82qQtLlLqP8sicwEY6u15SxibZQ0zrbBwbsINPSkLlibWoC7F9ickHIhY01n3icSMWTL7PZ5XticickKIWJX6dfrPNxiaB2xc/640?wx_fmt=png&from=appmsg)

每次跟后一位异或，最后一个跟第1个异或，密文存储在unk\_1400184A0：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aELfS25trp8gu30ibmpMM2jHuAkrIdftvbWG2HwbXS9DT1qLUDRQyiaFQntolCe9um7p0DtWI9cEFC2Gop3xkyULZqj1OGFfDHQ/640?wx_fmt=png&from=appmsg)

制作python解密脚本：

```
if __name__ == '__main__':    cipher =[0x8e, 0x88, 0x03, 0xde, 0xdc, 0x03, 0x89, 0xd5, 0x53, 0x8d, 0xd4, 0x0d, 0xdf, 0xd2, 0x5c, 0x8d,        0x82, 0x08, 0xd1, 0x8e, 0x09, 0xd2, 0x80, 0x01, 0x82, 0x82, 0x07, 0x85, 0xd1, 0x54, 0xd5, 0x8d]    flag_list = [0] * 32    decrypt1_list =[0] * 32    decrypt1_list[31] = cipher[31] ^ cipher[0]    for i in range(30, -1, -1):        decrypt1_list[i] = cipher[i] ^ decrypt1_list[i + 1]    key = 0xbc    for i in range(32):        for j in range(i):            key = key ^ decrypt1_list[j]        flag_list[i] = decrypt1_list[i] ^ key    flag = ''    for i in range(32):        flag += chr(flag_list[i])    print(flag)
```

运行后得到flag：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bicQ8VVbBX10EXLYQNDeBicnslto4p9tWGogldNt2AQSFJnkGBzibR41eKOH0NXJL9QdnhQdgjd14pUZUL764u44fP9AMUcyp8uI/640?wx_fmt=png&from=appmsg)

# 4. CTF+Binary练习题-Re-Day11 [Score=2]

下载题目附件，拖入ida中静态分析找到主函数：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4alSrV3X5zec697yTvjeds17dia8UOMiaBrmSZhE3gCEVlNjjibAib92jljA5MzM5aibibQ22wb23LtUwIcRzD2OufJWSSVqRSWibAdIg/640?wx_fmt=png&from=appmsg)

输入字符串后调用了checkformat函数（重新命名的）检查格式，并把输入的字符串分割成了4个qword数：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aevblwv36cKFqoI9BqFibgC3kzTmpA0FXyqHKicgluPrf33pUcCuVZwBeUa5o0Cy19r4YqJbbQwz9fwIscibR3ImKR8xzk1qicwicE/640?wx_fmt=png&from=appmsg)

然后调用第一个加密函数sub\_4013B0，进行一系列异或操作

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YFHHKPicnwYPQh2iaMIUnlX5w4b1VSZObTfCTfyoTia6VmWJ3qibwedJCYH6hA15pEZZF6UHC7BuQQZ7ItR95nIep1FEApXYRL2kM/640?wx_fmt=png&from=appmsg)

第二个加密函数是sub\_401670：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4beHqPZAB4hnibUG8CkYIyPZalpbGic1pmMnq9pKQ6hv71ESHGwz9icPJpHUlTTGd1JplibQQ4CDxKY4N04QMef1n3uia8rN0F86Wd8/640?wx_fmt=png&from=appmsg)

这个加密函数首先定义了4个qword常数，然后判断flag的长度是否是8的倍数，不是的话进行填充，填充字节由余数决定，然后调用加密函数sub\_401590：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZaI8EicVPIj8euBkPTQsfF6yXw9D49knibenMMP6WgN5qbQPiar22jF8fOLEoSWBZQRPsofzWeWeDV0zicibo89UJMV6A93U2sH06I/640?wx_fmt=png&from=appmsg)

可以看到这里是一个tea加密，但是加密轮数被修改为了0x2E轮，加密完成后再存入结果地址中，最后跟，密文比较，密文（32字节）为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZOujoyibGYtBJpNndajbGibMicdmNgvED1pogcCYfNwc4f3hdiaJ8nmf0iaQDZtynwbicb3gkxBj0BIqFMZtcb5LV79UJkeicuWFk87o/640?wx_fmt=png&from=appmsg)

制作c语言解密脚本：

```
#include <stdint.h>#include <stdio.h>int main(void) {    const uint32_t enc[8] =    {        0xf2b22e23, 0xa98af84e, 0xc28f418b, 0x00d81799,        0xb534143f, 0x7e0513c3, 0x6c7095e7, 0x133909e0    };    const uint32_t key[4] =    {        0xA306D4A9, 0x7EDC188E, 0xA64C19F0, 0xCDD1E4B4    };    uint8_t flag_num[32] = {0};    for (int32_t i = 0; i < 32; i+=8) {        uint32_t sum_var = 0;        for (int k = 0; k < 0x2e; k++) {            sum_var -= 0x61c88647;        }        uint32_t v0 = enc[i / 4];        uint32_t v1 = enc[i / 4 + 1];        for (int32_t j = 0; j < 0x2e; j++) {            v1 -= ((v0 << 4) + key[2]) ^ ((v0 >> 5) + key[3]) ^ (v0 + sum_var);            v0 -= ((v1 << 4) + ke...