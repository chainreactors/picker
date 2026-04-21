---
title: 2025 “泉城杯” 济南市网络安全大赛 题目复现
url: https://mp.weixin.qq.com/s/ZtpiJ1Oea5vJDXKm1o1CEw
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:44:39.022559
---

# 2025 “泉城杯” 济南市网络安全大赛 题目复现

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Hjtlibzdr5XicWrOjPtWkcTNNF3qNUEqicTUk7cPQwXcKVe9NCHQ4jUoNr5bYuRuiaRnAFsmpYibFPqojfAjl5WXKibAvqhhZJlMCrpicd0ngYNNIw/0?wx_fmt=jpeg)

# 2025 “泉城杯” 济南市网络安全大赛 题目复现

原创

小志z
小志z

志在片语

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 其实就是去年大概七月的事情 感觉时间好快 马上又要比CTF了 准备拿一些之前没做出来的逆向密码深入学习一下下（

> 2025 “泉城杯” 济南市网络安全大赛 题目分享：https://blog.x-z-z.com/article/2025-07-26-19-30

## Misc

### b64

```
题目名称：b64题目内容：b64题目分值：25.0题目难度：非常容易相关附件：b64.zip
```

打开压缩包 内容如下

```
REFTQ1RGe0hlbGxvX1dvcmxkfQ==
```

暗示Base64解码 进行解码 得到答案

![image-20250715103825106](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XicdLtUURHicuyFt6Y5FO2W3vhRKJHVjk3tEqb5blYyz1nX0SQXib0AdR0dPRAI4FqC4D1WqgicGDV6Ij3kTITBfPw8mHeh8qmiasr8/640?wx_fmt=png&from=appmsg "null")

### misc-pic-1-2

```
题目名称：misc-pic-1-2题目内容：数码相机照片中的秘密题目分值：25.0题目难度：非常容易相关附件：misc-pic-1-2的附件.zip
```

解压压缩包 找到图片文件 右键点击属性

![image-20250715104220608](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibBvuQPgrg7EkhibzqjAxpjOQjQgtswc7hKPWlqq36aDgnqjLJvFicIY27l9rM7wcbmCwtjfTspL2s36DSvia8Zh7ng432icj1QicRs/640?wx_fmt=png&from=appmsg "null")

复制备注 进行解码 解题成功

![image-20250715104237917](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X9td98BlLxzIzZOG75hMReXBbyXicLGIzr5lsJLfxy2zmdZiagYJrTpGtCULdK9yOeRg639DdCGD3rP1paFqJQOxJYVcp0Xiaoolw/640?wx_fmt=png&from=appmsg "null")

### ezusb

```
题目名称：ezusb题目内容：大黑阔给我发了一个流量包和一串看不懂的字符，里面究竟藏了什么惊天大秘密呢?题目分值：50.0题目难度：容易相关附件：ezusb的附件.zip
```

这道题 打开发现是一个sercet.txt和flag.pcapng

![image-20260412171559813](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibnEkFhIsJefRJjFARkO1fPtT01HZBWuubiaCEISBhyhcc3AZBASqMzqSibb7DZ9P5GGNGzyj2kxqYFQiccPyxib3ON8Nl3E1sxqfo/640?wx_fmt=png&from=appmsg "null")

打开后发现协议都为usb 用UsbKeyboardDataHacker解密

![image-20260412171645986](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8sGQs8xc0CTXKltMI2fqQsVH0TKtq3IV5iaSD9eMeHQ9TES3RH51At3G6FEhgUIyP2cfkEFUNuTc0aQJhjxZ0ia4AZ9lLItjUUk/640?wx_fmt=png&from=appmsg "null")

用UsbKeyboardDataHacker解密数据包

```
python3 UsbKeyboardDataHacker.py --input ~/Downloads/ezusb/flag.pcapng
```

![image-20260415154613741](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5Xib8Jln3ha8zrib8suJOFbP0sXKCxgapiaWJRqRI2icO8T7CoyeIqlqCgTjAqdRIuocdeEtAibZ9I7JxZcxpcu92L9EJCE0WWbOhhS4/640?wx_fmt=png&from=appmsg "null")

```
congratulations,you<SPACE>finlly<SPACE>find<SPACE>me,but<SPACE>what<SPACE>i<SPACE>want<SPACE>to<SPACE>tell<SPACE>you<SPACE>is<SPACE>that<SPACE>roman<SPACE>roland<SPACE>once<SPACE>said<SPACE>thar<SPACE>there<SPACE>is<SPACE>only<SPACE>one<SPACE>kind<SPACE>of<SPACE>heroism<SPACE>in<SPACE>the<SPACE>worlld,that<SPACE>is<SPACE>to<SPACE>know<SPACE>the<SPACE>cruelty<SPACE>of<SPACE>the<SPACE>life<SPACE>but<SPACE>still<SPACE>love<SPACE>it.<CAP><CAP>ok,<CAP><CAP>get<SPACE>to<SPACE>the<SPACE>point:the<SPACE>{}_<SPACE>three<SPACE>symbols<SPACE>were<SPACE>added<SPACE>to<SPACE>the<SPACE>front<SPACE>of<SPACE>the<SPACE>base64<SPACE>table<SPACE>and<SPACE>handed<SPACE>to<SPACE>caesar.if<SPACE>you<SPACE>can<SPACE>decrypto<SPACE>the<SPACE>sercet<SPACE>you<SPACE>can<SPACE>get<SPACE>the<SPACE>half<SPACE>of<SPACE>flag.
```

可以得到 base64的编码表前需要加入 "{}\_" 而且之前正好提供了一个密文

![image-20260415154807016](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibY298su9sTw3JQNM9dfpb7LFWRvKQxSvNMgibhEQSyM0BlnvKm88iaibI5uMXkwjhPN3JsPPZVdice5XebLRgnyMxiaJTkufNAWbpY/640?wx_fmt=png&from=appmsg "null")

用随波逐流 再配合表前加 "{}" 得到flag前段 DASCTF{JUST\_3aSY\_Ca3SaR\_aND\_MaUSE

![image-20260420125250055](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9ibJVJ2iaQg10vAGIBTpRoVQ4Mq8qUHCUZB8CAeUjppzRBkALdMvSB45pVwRFezejUTWWdsFBXvHqb9gmLd1d6ibBqibI9TriaGU8k/640?wx_fmt=png&from=appmsg "null")

提取设备的按键码

```
tshark -r flag.pcapng -T fields -e usb.capdata > usbdata.txt
```

用python脚本解析里面不同的位 并翻译成二进制 最后转ascii码

```
with open('usbdata.txt', 'r') as f:    bits = [line[2:4] for line in f if len(line) == 15 and line[2:4] != "00"]binary = ''.join(bits).replace('02', '0').replace('01', '1')result = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))print(result)
```

最后getflag的尾段 Keyb0rad\_@nd\_USB!}

![image-20260420143018421](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X9bppODqAWR86qkTacF2icibRKfL1iaMCSO5r64Ae0icOoZ3yXU0NFEeuqdP73OqxNIm6Qs9k2g2qdu3MYOlh3Hou5EI5A3tzGzang/640?wx_fmt=png&from=appmsg "null")

将flag组合一下可得 DASCTF{JUST**3aSY\_Ca3SaR\_aND\_MaUSEKeyb0rad**@nd\_USB!}

## Reverse

### ezre\_1

```
题目名称：ezre_1题目内容：这是一个普通的逆向题题目分值：50.0题目难度：容易相关附件：ezre_1的附件.zip
```

先查一下有没有壳 发现有upx壳

![image-20260401222610754](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5Xic3yFa3oJicNmWakrOaXGLCMQZwiclhJiawLamZ4KUxJ7u9jLJhvAv0ax2jTX4ficymwMrC5oC0sic4N1rS7zrtFENsYtBaYqb2JWzc/640?wx_fmt=png&from=appmsg "null")

用upx直接脱壳即可

```
.\upx.exe -d ezre.exe
```

![image-20260401222714402](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9ibDsaItpgdQExQAeMGJca7ly9hRlgxOUDo2vTIicPwmAkcQfYiar7BcI6DBAX6U8YeoibhqxWHHXiayUAAhuytdpE6K4gCl5J6HxE/640?wx_fmt=png&from=appmsg "null")

丢到ida 看样子反编译成功啦

![image-20260401222905633](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5X9whpVbob5msl6ticN35qn1cC3XicpEKMrDDRMCwbof3qvI70GGqa2XleibrU3GibtwORqbptREmT3mUz9Q7uiaRhc7gSvMX4wzfVaQ/640?wx_fmt=png&from=appmsg "null")

点进check 看一下函数逻辑

```
int check(){  unsigned int v0; // eax  char Str[1024]; // [rsp+90h] [rbp+10h] BYREF  char Str2[48]; // [rsp+490h] [rbp+410h] BYREF  char v4[16]; // [rsp+4C0h] [rbp+440h] BYREF  char Buffer[8]; // [rsp+4D0h] [rbp+450h] BYREF  char *Str1; // [rsp+4D8h] [rbp+458h]  void *v7; // [rsp+4E0h] [rbp+460h]  void *v8; // [rsp+4E8h] [rbp+468h]
  system("cls");  puts("welcome to DASCTF");  puts("plz check your flag here!!!!");  strcpy(Buffer, "correct");  strcpy(v4, "error");  strcpy(Str2, "aOYanlkVkemSmRgYlWi0Nc1P3JPIfoMoQJ2I20w=");  v8 = malloc(0x37ui64);  printf("plz input your flag:");  scanf("%s", Str);  getchar();  v7 = malloc(0x400ui64);  memset(v7, 0, 0x400ui64);  v0 = strlen(Str);  v8 = (void *)base64_encode(Str, v7, v0);  Str1 = (char *)malloc(0x64ui64);  Str1 = (char *)chang(v8);  if ( !strcmp(Str1, Str2) )    return puts(Buffer);  else    return puts(v4);}
```

**预设正确的密文**是 `Str2 = "aOYanlkVkemSmRgYlWi0Nc1P3JPIfoMoQJ2I20w="`

**对输入进行 Base64 编码** `v8 = base64_encode(Str, v7, v0)`

**再经过 `chang()` 函数处理** `Str1 = chang(v8)` 最后有个比较

这样的话再进入chang函数看逻辑即可

![image-20260402193321240](https://mmbiz.qpic.cn/mmbiz_png/Hjtlibzdr5X8Kln4FJ8AXr66JeTusiabXRoZDueDckzU36icp2X04J6tibsJ1DH9AKfpxJBjEfwITGbcJTSxL2dk2W2x8ssro9YoByjkFzzb6co/640?wx_fmt=png&from=appmsg "null")

```
char *__fastcall chang(const char *a1){  void *v1; // rsp  int v2; // eax  void *v3; // rsp  __int64 v5[3]; // [rsp+20h] [rbp-60h] BYREF  char *Source; // [rsp+38h] [rbp-48h]  __int64 v7; // [rsp+40h] [rbp-40h]  char *Destination; // [rsp+48h] [rbp-38h]  __int64 v9; // [rsp+50h] [rbp-30h]  int v10; // [rsp+5Ch] [rbp-24h]  __int64 *v11; // [rsp+60h] [rbp-20h]  __int64 *v12; // [rsp+68h] [rbp-18h]  int i; // [rsp+74h] [rbp-Ch]  int v14; // [rsp+78h] [rbp-8h]  int v15; // [rsp+7Ch] [rbp-4h]
  v10 = strlen(a1);  v15 = 0;  v14 = 0;  v9 = v10 + 1 - 1i64;  v5[0] = v10 + 1;  v5[1] = 0i64;  v1 = alloca(16 * ((unsigned __int64)(v5[0] + 15) >> 4));  Destination = (char *)v5;  v2 = (v10 + 1) / 2;  v7 = v2 - 1i64;  v3 = alloca(16 * ((unsigned __int64)(v2 + 15i64) >> 4));  Source = (char *)v5;  v12 = v5;  v11 = v5;  for ( i = 0; i < v10; ++i )  {    if ( a1[i] == 32 )    {      ++v14;    }    else if ( v15 )    {      *(_BYTE *)v11 = a1[i];      v11 = (__int64 *)((char *)v11 + 1);      v15 = 0;    }    else    {      *(_BYTE *)v12 = a1[i];      v12 = (__int64 *)((char *)v12 + 1);      v15 = 1;    }  }  *(_BYTE *)v12 = 0;  *(_BYTE *)v11 = 0;  strcat(Destination, Source);  return Destination;}
```

大概含义是把输入字符串中的字符按照“奇偶位置”分成两段，然后拼接在一起 写一个简单的脚本来解密一下就好

我直接跑了一次 发现怎么样都是乱码

![image-20260402194046893](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibnIojYnHI3zhAS896PgCfxbicuPV5o72LWrbc3zdX7cYvEf3ogBzqicQQyGL3kbjydsyx0sMls5Ht3bJNzTukHpxaERZJXI3Rico/640?wx_fmt=png&from=appmsg "null")

把思路再回到ida 去跟进base64 encode函数

![image-20260402194124191](https://mmbiz.qpic.cn/sz_mmbiz_png/Hjtlibzdr5XibyIIVZQhaJKS...