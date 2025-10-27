---
title: 看雪2022 KCTF 秋季赛 | 第六题设计思路及解析
url: https://buaq.net/go-137836.html
source: unSafe.sh - 不安全
date: 2022-11-30
fetch_date: 2025-10-04T00:03:07.307624
---

# 看雪2022 KCTF 秋季赛 | 第六题设计思路及解析

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/11e75445163fbfeee446dab5cbecd523.jpg)

看雪2022 KCTF 秋季赛 | 第六题设计思路及解析

原创
*2022-11-29 18:1:26
Author: [mp.weixin.qq.com(查看原文)](/jump-137836.htm)
阅读量:14
收藏*

---

原创

2022 KCTF 秋季赛

看雪学苑

[*看雪 2022 KCTF秋季赛*](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458483668&idx=1&sn=df35db255afb9045521f889594e2acc5&chksm=b18e4b5e86f9c2484ce5f892774bd08973a0a1f7e297c1862742c85fc62cda5f1873afaba952&scene=21#wechat_redirect)已于11月15日中午12点正式开始！比赛延续上一届的模式并进行优化，对每道题设置了难度值、火力值、精致度等多类积分，用规则引导题目的难度和趣味度。大家请注意：签到题（https://ctf.pediy.com/game-season\_fight-216.htm）将持续开放，整个比赛期间均可提交答案，获得积分哦～

第六题《病疫先兆》今日已经关闭答题通道，据统计，24小时内共有41支战队成功提交flag！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQ1abK2Vppiarfib1ibAAczrXecPkVJRciaoAzrP2R08zdnLuqnMVMaKMq08gTlm4huYFUvDMnjtLrmQ/640?wx_fmt=png)

下面一起看看该赛题的设计思路和相关解析吧~

出题团队简介

第6题《病疫先兆》出题方 **中午吃什么** **战队**

**战队成员id：wx\_孤城、瑞皇、hmfzy**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQ1abK2Vppiarfib1ibAAczrXk43pDBBTNtIDUAxQQ24caWSfgRqibibicYQSbvRYhTRuFY8FTCqahyCibA/640?wx_fmt=png)

赛题设计思路

**战队名称：中午吃什么**

**参赛题目：CrackMe(Windows)**

**题目答案：14725KCTF83690**

使用方案一（老规则）

需要穷举爆破随机数种子（0-99999，穷举时间一分钟以内）

运行流程：输入序列号、输出success或error

详细的题目设计说明：
1、判断输入文本长度是否为14；

2、将输入文本拆分为3份(5字节、4字节、5字节)；
3、将2个5字节转为int，作为随机数种子调用srand；
4、调用rand生成20个int数据；
5、rand生成的数据和全局数组相等且4字节文本为KCTF则成功。

```
#include <stdio.h>#include <stdlib.h>
unsigned int arrSeed_14725[] = {    15356,    8563 ,    9659 ,    14347,    11283,    30142,    29542,    18083,    5057 ,    5531 ,    23391,    21327,    20023,    14852,    4865 ,    23820,    16725,    18665,    25042,    24920 };
unsigned int arrSeed_83690[] = {    11190,    27482,    980     ,    5419 ,    28164,    9548 ,    16558,    22218,    6113 ,    21959,    13889,    11580,    2625 ,    19397,    25139,    8167 ,    28165,    3950 ,    25496,    27351 };
int my_strlen(const char* StrDest){    return ('\0' != *StrDest) ? (1 + my_strlen(StrDest + 1)) : 0;}
#if 0//爆破代码int main(){    int i, j;    int isSuccess = 0;    for (i = 0; i < 99999; i++)    {        isSuccess = 1;        //printf("0x%08x\n", i);        srand(i);        for (j = 0; j < 20; j++)        {            if (rand() != arrSeed_14725[j])            {                isSuccess = 0;                break;            }        }        if (isSuccess != 0)        {            printf("种子1:[%d]\n", i);            //break;        }    }    isSuccess = 0;    for (i = 0; i < 99999; i++)    {        isSuccess = 1;        //printf("0x%08x\n", i);        srand(i);        for (j = 0; j < 20; j++)        {            if (rand() != arrSeed_83690[j])            {                isSuccess = 0;                break;            }        }        if (isSuccess != 0)        {            printf("种子2:[%d]\n", i);            //break;        }    }    system("pause");    return 0;}
#else
//题目程序int main(){    int i = 0;    char szBuffer[128] = { 0 };    char szSeed1[6];    unsigned int dwSeed1;    char szKCTF[5];    char szSeed2[6];    unsigned int dwSeed2;    int isSuccess1;    int isSuccess2;    int isSuccess3;
    //0-99999    //14725KCTF83690    printf("please input :\n");    scanf_s("%s", szBuffer, sizeof(szBuffer) - 1);    if (my_strlen(szBuffer) != 14)    {        printf("error\n");        system("pause");        return 0;    }
    szSeed1[5] = '\0';    for (i = 0; i < 5; i++)    {        szSeed1[i] = szBuffer[i + 0];    }    dwSeed1 = atoi(szSeed1);
    szKCTF[4] = '\0';    for (i = 0; i < 4; i++)    {        szKCTF[i] = szBuffer[i + 5];    }
    szSeed2[5] = '\0';    for (i = 0; i < 5; i++)    {        szSeed2[i] = szBuffer[i + 5 + 4];    }    dwSeed2 = atoi(szSeed2);    //printf("%d\n", dwSeed1);    //14725    //printf("%s\n", szKCTF);    //KCTF    //printf("%d\n", dwSeed2);    //83690
    isSuccess1 = 1;    isSuccess2 = 1;    isSuccess3 = 0;    srand(dwSeed1);    for (i = 0; i < 20; i++)    {        if (rand() != arrSeed_14725[i])        {            isSuccess1 = 0;            break;        }    }    srand(dwSeed2);    for (i = 0; i < 20; i++)    {        if (rand() != arrSeed_83690[i])        {            isSuccess1 = 0;            break;        }    }    if (szKCTF[0] == 'K' &&        szKCTF[1] == 'C' &&        szKCTF[2] == 'T' &&        szKCTF[3] == 'F')    {        isSuccess3 = 1;    }
    if (isSuccess1 != 0 && isSuccess2 != 0 && isSuccess3 != 0)    {        printf("success : %s\n", szBuffer);        system("pause");        return 0;    }    printf("error\n");    system("pause");    return 0;}
#endif
```

破解思路：
爆破2个5位数随机数种子(0-99999)
种子1+KCTF+种子2即为正确FALG

赛题解析

本赛题解析由看雪论坛专家**htg**给出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EQ1abK2Vppiarfib1ibAAczrXuQ7B8ibL9mMRSWIar9X0r19ARTVun4OUy4UyEAjNibXTARSgb9thibQvg/640?wx_fmt=png)

个人论坛主页：*https://bbs.pediy.com/user-home-542902.htm*

工具：IDA、Python

```
一
```

```
C:\Users\surface>C:\Users\surface\OneDrive\Crack\CTF\Kanxue2022KCTFAutumn\06\CrackMe\CrackMe.exeplease input :0123456789error请按任意键继续. . . C:\Users\surface>
```

代码错误时：输出error

```
二
```

## 主程序：

```
int __cdecl main(int argc, const char **argv, const char **envp){  int preValue; // eax  unsigned int preValueCopy; // ebx  int sufValue; // eax  unsigned int sufValueCopy; // edi  int *v7; // esi  int *v8; // esi  char inputSN[128]; // [esp+4h] [ebp-A0h] BYREF  char sufStr[8]; // [esp+84h] [ebp-20h] BYREF  char preStr[8]; // [esp+8Ch] [ebp-18h] BYREF  int v13; // [esp+94h] [ebp-10h]  int v14; // [esp+98h] [ebp-Ch]  int v15; // [esp+9Ch] [ebp-8h]   memset(inputSN, 0, sizeof(inputSN));  printf("please input :\n");  scanf_s("%s", inputSN);  if ( sub_B91000(inputSN) != 0xE )    goto LABEL_19;  preStr[5] = 0;                                // 字符串截断符：只允许5个字节  *(_DWORD *)preStr = *(_DWORD *)inputSN;  preStr[4] = inputSN[4];  preValue = atoi(preStr);  v15 = *(_DWORD *)&inputSN[5];  sufStr[5] = 0;                                // 字符串截断符：只允许5个字节  *(_DWORD *)sufStr = *(_DWORD *)&inputSN[9];  preValueCopy = preValue;  sufStr[4] = inputSN[0xD];  sufValue = atoi(sufStr);  v13 = 0;  sufValueCopy = sufValue;  v14 = 1;                                      // 需保证为1  srand(preValueCopy);  v7 = dword_B9F000;  while ( rand() == *v7 )                       // 依次获取的随机值需与内置全局数组相等  {    if ( (int)++v7 >= (int)dword_B9F050 )      goto LABEL_7;                             // 要跳出来。避开 v14=0  }  v14 = 0;                                      // 执行了这一步就错LABEL_7:  srand(sufValueCopy);  v8 = dword_B9F050;  while ( rand() == *v8 )                       // 依次获取的随机值需与内置全局数组相等  {    if ( (int)++v8 >= (int)&dword_B9F0A0 )      goto LABEL_12;                            // 要跳出来。避开 v14=0  }  v14 = 0;                                      // 执行了这一步就错LABEL_12:  if ( (_BYTE)v15 == 'K' && *(_WORD *)((char *)&v15 + 1) == 'TC' && HIBYTE(v15) == 'F' )// KCTF    v13 = 1;  if ( v14 && v13 )  {    printf("success : %s\n", inputSN);    system("pause");  }  else  {LABEL_19:    printf("error\n");    system("pause");  }  return 0;}
```

## 初始化随机种子

```
void __cdecl srand(unsigned int Seed){  *(_DWORD *)(_getptd() + 0x14) = Seed;}
```

## 随机函数：

```
int __cdecl rand(){  int v0; // ecx  unsigned int v1; // eax   v0 = _getptd();  v1 = 0x343FD * *(_DWORD *)(v0 + 0x14) + 0x269EC3;  *(_DWORD *)(v0 + 0x14) = v1;  return HIWORD(v1) & 0x7FFF;}
```

程序整理的逻辑结构清晰，最终通过 if ( v14 && v13 ) 之后，才判断正确。

```
三
```

## 1、获取用户字符串

## 2、检查字符串长度：0xE = 14

```
  if ( sub_B91000(inputSN) != 0xE )
```

## 3、将字符串分为三部分

### 第一部分：前5个字符，转为整数

```
preStr[5] = 0;                                // 字符串截断符：只允许5个字节*(_DWORD *)preStr = *(_DWORD *)inputSN;preStr[4] = inputSN[4];preValue = atoi(preStr);
```

### 第二部分：KCTF

```
v15 = *(_DWORD *)&inputSN[5];
```

### 第三部分：后5个字符，转为整数
...